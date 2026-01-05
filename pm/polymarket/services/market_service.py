from __future__ import annotations

from pm.core.utils import as_dict

from pm.polymarket.models import MarketData
from pm.polymarket.handlers import GammaHandler


class MarketService:
    def __init__(self, gamma_handler: GammaHandler):
        self.gamma_handler = gamma_handler

    def _normalize_market(self, raw_market: MarketRes) -> MarketData:
        raw = _as_dict(raw_market)

    def get(
        self, *, slug: str | None = None, id: str | None = None
    ) -> MarketData | None:
        if slug:
            raw = self.gamma_handler.get_market_by_slug(slug=slug)
        elif id:
            raw = self.gamma_handler.get_market_by_id(id=id)
        else:
            raise ValueError("Market requires a slug=... or id-...")

        if not raw:
            return None

        return self._normalize_market(raw)
