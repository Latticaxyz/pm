from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, MutableMapping, Protocol, TypeAlias

import httpx

from .errors import AuthError, HTTPError, NotFoundError, RateLimitError, ServerError
from .retry import RetryConfig, RetryPolicy

Headers = Mapping[str, str]
Params = Mapping[str, str | int | float | bool | list[int] | list[str] | None]

# Type this at the service layer
# https://stackoverflow.com/questions/51291722/define-a-jsonable-type-using-mypy-pep-526
JSON: TypeAlias = Any


class Close(Protocol):
    def close(self) -> None: ...


def merge_headers(base: Headers | None, extra: Headers | None) -> MutableMapping[str, str]:
    out: MutableMapping[str, str] = {}
    if base:
        out.update(base)
    if extra:
        out.update(extra)
    return out


def time_sleep(seconds: float) -> None:
    import time

    time.sleep(seconds)


@dataclass(frozen=True)
class HTTPClientConfig:
    base_url: str
    timeout_s: float = 20.0
    connect_timeout_s: float = 5.0
    proxy: str | None = None
    http2: bool = False
    user_agent: str = "pm/0.1"
    retries: RetryConfig = RetryConfig()


class HTTPClient:
    def __init__(self, cfg: HTTPClientConfig, *, default_headers: Headers | None = None):
        self.cfg = cfg
        self._retry = RetryPolicy(cfg.retries)

        self._default_headers = merge_headers({"User-Agent": cfg.user_agent}, default_headers)

        self._sync: httpx.Client | None = None

    def _get_sync(self) -> httpx.Client:
        if self._sync is None:
            self._sync = httpx.Client(
                base_url=self.cfg.base_url.rstrip("/"),
                timeout=httpx.Timeout(self.cfg.timeout_s, connect=self.cfg.connect_timeout_s),
                proxy=self.cfg.proxy,
                http2=self.cfg.http2,
                headers=dict(self._default_headers),
                follow_redirects=True,
            )
        return self._sync

    def close(self) -> None:
        if self._sync is not None:
            self._sync.close()
            self._sync = None

    def _raise_for_status(self, resp: httpx.Response) -> None:
        if resp.status_code < 400:
            return

        url = str(resp.request.url)
        snippet = None
        try:
            text = resp.text
            snippet = text[:300] if text else None
        except Exception:
            snippet = None

        msg = "Request failed"

        if resp.status_code == 404:
            raise NotFoundError(resp.status_code, msg, url=url, body_snippet=snippet)
        if resp.status_code == 429:
            raise RateLimitError(resp.status_code, "Rate limited", url=url, body_snippet=snippet)
        if resp.status_code in (401, 403):
            raise AuthError(
                resp.status_code,
                "Unauthorized/Forbidden",
                url=url,
                body_snippet=snippet,
            )
        if resp.status_code >= 500:
            raise ServerError(resp.status_code, "Upstream error", url=url, body_snippet=snippet)

        raise HTTPError(resp.status_code, msg, url=url, body_snippet=snippet)

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Params | None = None,
        json: JSON = None,
        headers: Headers | None = None,
    ) -> httpx.Response:
        client = self._get_sync()
        req_headers = merge_headers(self._default_headers, headers)

        last_exc: BaseException | None = None

        for attempt in range(self._retry.cfg.max_retries + 1):
            try:
                resp = client.request(method, path, params=params, json=json, headers=req_headers)
                if self._retry.retryable_status(resp.status_code) and attempt < self._retry.cfg.max_retries:
                    ra = self._retry.parse_retry_after(resp)
                    wait = ra if ra is not None else self._retry.backoff_seconds(attempt)
                    time_sleep(wait)
                    continue

                self._raise_for_status(resp)
                return resp

            except BaseException as e:
                last_exc = e
                if not self._retry.retryable_exception(e) or attempt >= self._retry.cfg.max_retries:
                    raise
                time_sleep(self._retry.backoff_seconds(attempt))

        raise RuntimeError("unreachable") from last_exc

    def get_json(self, path: str, *, params: Params | None = None, headers: Headers | None = None) -> JSON:
        resp = self.request("GET", path, params=params, headers=headers)
        return resp.json()
