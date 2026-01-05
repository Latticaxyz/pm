from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from pm.core import HTTPClient
from pm.polymarket.api.handlers import ClobHandler, DataHandler, GammaHandler
from pm.polymarket.config import PolymarketConfig

if TYPE_CHECKING:
    from .market import Market  # noqa: F401


@dataclass
class Polymarket:
    _config: PolymarketConfig | None = None

    config: PolymarketConfig = field(init=False)
    gamma: GammaHandler = field(init=False)
    clob: ClobHandler = field(init=False)
    data: DataHandler = field(init=False)
    _gamma_http: HTTPClient = field(init=False)
    _clob_http: HTTPClient = field(init=False)
    _data_http: HTTPClient = field(init=False)

    def __post_init__(self) -> None:
        self._build(self._config)

    def _build(self, config: PolymarketConfig | None) -> None:
        self.config = config or PolymarketConfig()

        self._gamma_http = HTTPClient(self.config.gamma_http())
        self._clob_http = HTTPClient(self.config.clob_http())
        self._data_http = HTTPClient(self.config.data_http())

        self.gamma = GammaHandler(self._gamma_http)
        self.clob = ClobHandler(self._clob_http)
        self.data = DataHandler(self._data_http)

    def set_config(self, config: PolymarketConfig) -> None:
        old_gamma = getattr(self, "_gamma_http", None)
        old_clob = getattr(self, "_clob_http", None)
        old_data = getattr(self, "_data_http", None)

        self._build(config)

        if old_gamma is not None:
            old_gamma.close()
        if old_clob is not None:
            old_clob.close()
        if old_data is not None:
            old_data.close()

    def Market(self, slug: str) -> "Market":  # noqa: F811
        from .market import Market

        return Market(slug=slug, client=self)

    def close(self) -> None:
        self._gamma_http.close()
        self._clob_http.close()
        self._data_http.close()
