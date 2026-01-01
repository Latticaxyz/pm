from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .client import Polymarket
from .config import PolymarketConfig
from .resources.market import Market as MarketResource


@dataclass
class PolymarketAPI:
    config: Optional[PolymarketConfig] = None

    def __post__init__(self) -> None:
        self._client = Polymarket(config=self.config)

    @property
    def client(self) -> Polymarket:
        return self._client

    def Market(self, slug: str) -> MarketResource:
        return MarketResource(slug=slug, client=self._client)

    def close(self) -> None:
        self._client.close()

    async def aclose(self) -> None:
        await self._client.aclose()
