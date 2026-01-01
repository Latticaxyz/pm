from __future__ import annotations

from typing import Any

from pm.core import HTTPClient
from ..constants import GAMMA_EVENTS_PATH, GAMMA_MARKETS_PATH


class GammaService:
    def __init__(self, http: HTTPClient):
        self.http = http

    def get_market_by_slug(self, slug: str) -> dict[str, Any]:
        data = self.http.get_json(GAMMA_MARKETS_PATH, params={"slug": slug})
        if isinstance(data, list):
            return data[0] if data else {}
        return data

    async def aget_market_by_slug(self, slug: str) -> dict[str, Any]:
        data = await self.http.aget_json(GAMMA_MARKETS_PATH, params={"slug": slug})
        if isinstance(data, list):
            return data[0] if data else {}
        return data

    def get_market(self, market_id: str) -> dict[str, Any]:
        return self.http.get_json(f"{GAMMA_MARKETS_PATH}/{market_id}")

    async def aget_market(self, market_id: str) -> dict[str, Any]:
        return await self.http.aget_json(f"{GAMMA_MARKETS_PATH}/{market_id}")

    def get_event(self, event_id: str) -> dict[str, Any]:
        return self.http.get_json(f"{GAMMA_EVENTS_PATH}/{event_id}")

    async def aget_event(self, event_id: str) -> dict[str, Any]:
        return await self.http.aget_json(f"{GAMMA_EVENTS_PATH}/{event_id}")
