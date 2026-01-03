from __future__ import annotations

from dataclasses import dataclass


class pmError(Exception):
    """Base pm Error"""


@dataclass
class HTTPError(pmError):
    status_code: int
    message: str = "HTTP error"
    url: str | None = None
    body_snippet: str | None = None

    def __str__(self) -> str:
        base = f"{self.status_code}: {self.message}"
        if self.url:
            base += f" ({self.url})"
        if self.body_snippet:
            base += f" :: {self.body_snippet}"
        return base


class NotFoundError(HTTPError):
    """404"""


class RateLimitError(HTTPError):
    """429"""


class AuthError(HTTPError):
    """401"""


class ServerError(HTTPError):
    """5xx"""
