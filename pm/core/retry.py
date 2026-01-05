from __future__ import annotations

import random
from dataclasses import dataclass
from typing import cast

import httpx


@dataclass(frozen=True)
class RetryConfig:
    max_retries: int = 3
    backoff_base_s: float = 0.5
    backoff_cap_s: float = 8.0
    jitter_s: float = 0.25


class RetryPolicy:
    def __init__(self, cfg: RetryConfig | None = None):
        self.cfg = cfg or RetryConfig()

    def retryable_status(self, status_code: int) -> bool:
        return status_code in (408, 425, 429, 500, 502, 503, 504)

    def retryable_exception(self, exc: BaseException) -> bool:
        return isinstance(
            exc,
            (
                httpx.TimeoutException,
                httpx.ConnectError,
                httpx.ReadError,
                httpx.WriteError,
                httpx.PoolTimeout,
                httpx.RemoteProtocolError,
            ),
        )

    def backoff_seconds(self, attempt: int) -> float:
        base = self.cfg.backoff_base_s * (2**attempt)
        capped = min(self.cfg.backoff_cap_s, base)
        jitter = random.random() * self.cfg.jitter_s
        return cast(float, capped + jitter)

    def parse_retry_after(self, resp: httpx.Response) -> float | None:
        ra = resp.headers.get("retry-after")
        if not ra:
            return None
        try:
            return float(ra)
        except ValueError:
            return None
