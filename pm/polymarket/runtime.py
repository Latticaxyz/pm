from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from ._client import _Client
from .config import PolymarketConfig
from .resources.market import Market as MarketResource


@dataclass
class Polymarket:
    _config: Optional[PolymarketConfig] = None

    def __post_init__(self) -> None:
        self._client = _Client(config=self._config)

    def set_config(self, config: PolymarketConfig) -> None:
        old = self._client
        self._client = _Client(config=config)
        old.close()

    def Market(self, slug: str) -> MarketResource:
        return MarketResource(slug=slug, client=self._client)

    def close(self) -> None:
        self._client.close()
