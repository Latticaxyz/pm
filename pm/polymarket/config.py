from __future__ import annotations

from dataclasses import dataclass

from pm.core import HTTPClientConfig, RetryConfig

from .constants import (
    DEFAULT_CLOB_BASE_URL,
    DEFAULT_DATA_BASE_URL,
    DEFAULT_GAMMA_BASE_URL,
    DEFAULT_USER_AGENT,
)


@dataclass(frozen=True)
class PolymarketConfig:

    timeout_s: float = 20.0
    connect_timeout_s: float = 5.0
    proxy: str | None = None
    http2: bool = True
    user_agent: str = DEFAULT_USER_AGENT

    retries: RetryConfig = RetryConfig(max_retries=3)

    def gamma_http(self) -> HTTPClientConfig:
        return HTTPClientConfig(
            base_url=DEFAULT_GAMMA_BASE_URL,
            timeout_s=self.timeout_s,
            connect_timeout_s=self.connect_timeout_s,
            proxy=self.proxy,
            http2=self.http2,
            user_agent=self.user_agent,
            retries=self.retries,
        )

    def clob_http(self) -> HTTPClientConfig:
        return HTTPClientConfig(
            base_url=DEFAULT_CLOB_BASE_URL,
            timeout_s=self.timeout_s,
            connect_timeout_s=self.connect_timeout_s,
            proxy=self.proxy,
            http2=self.http2,
            user_agent=self.user_agent,
            retries=self.retries,
        )

    def data_http(self) -> HTTPClientConfig:
        return HTTPClientConfig(
            base_url=DEFAULT_DATA_BASE_URL,
            timeout_s=self.timeout_s,
            connect_timeout_s=self.connect_timeout_s,
            proxy=self.proxy,
            http2=self.http2,
            user_agent=self.user_agent,
            retries=self.retries,
        )
