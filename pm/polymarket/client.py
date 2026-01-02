from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from pm.core import HTTPClient

from .config import PolymarketConfig
from .services import ClobService, GammaService


@dataclass
class Polymarket:
    _config: Optional[PolymarketConfig] = None

    def __post_init__(self) -> None:
        self._build(self._config)

    def _build(self, config: PolymarketConfig | None) -> None:
        self.config = config or PolymarketConfig()

        self._gamma_http = HTTPClient(self.config.gamma_http())
        self._clob_http = HTTPClient(self.config.clob_http())

        self.gamma = GammaService(self._gamma_http)
        self.clob = ClobService(self._clob_http)

    def set_config(self, config: PolymarketConfig) -> None:
        old_gamma = getattr(self, "_gamma_http", None)
        old_clob = getattr(self, "_clob_http", None)

        self._build(config)

        if old_gamma is not None:
            old_gamma.close()
        if old_clob is not None:
            old_clob.close()

    def Market(self, slug: str):
        from .market import Market

        return Market(slug=slug, client=self)

    def close(self) -> None:
        self._gamma_http.close()
        self._clob_http.close()
