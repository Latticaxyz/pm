from __future__ import annotations

from pm.core import HTTPClient
from .config import PolymarketConfig
from .services import GammaService, ClobService


class Polymarket:
    def __init__(self, config: PolymarketConfig | None = None):
        self.config = config or PolymarketConfig()

        self._gamma_http = HTTPClient(self.config.gamma_http())
        self._clob_http = HTTPClient(self.config.clob_http())

        self.gamma = GammaService(self._gamma_http)
        self.clob = ClobService(self._clob_http)

    def close(self) -> None:
        self._gamma_http.close()
        self._clob_http.close()

    async def aclose(self) -> None:
        await self._gamma_http.aclose()
        await self._clob_http.aclose()
