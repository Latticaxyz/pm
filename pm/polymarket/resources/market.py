from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

from pm.core import NotFoundError
from ..client import Polymarket


def _pick(d: dict[str, Any], *keys: str) -> str:
    for k in keys:
        v = d.get(k)
        if v is None:
            continue
        s = str(v)
        if s:
            return s
    return ""


@dataclass
class Market:
    slug: str
    client: Polymarket

    _market: Optional[dict[str, Any]] = None
    _event: Optional[dict[str, Any]] = None

    def _ensure_market(self) -> dict[str, Any]:
        if self._market is None:
            data = self.client.gamma.get_market_by_slug(self.slug)
            if not data:
                raise NotFoundError(404, "Market not found", url=f"(slug={self.slug})")
            self._market = data
        return self._market

    async def _aensure_market(self) -> dict[str, Any]:
        if self._market is None:
            data = await self.client.gamma.aget_market_by_slug(self.slug)
            if not data:
                raise NotFoundError(404, "Market not found", url=f"(slug={self.slug})")
            self._market = data
        return self._market

    @property
    def info(self) -> dict[str, Any]:
        return self._ensure_market()

    async def ainfo(self) -> dict[str, Any]:
        return await self._aensure_market()

    @property
    def market_id(self) -> str:
        m = self._ensure_market()
        return _pick(m, "id", "marketId", "market_id")

    @property
    def event_id(self) -> str:
        m = self._ensure_market()
        return _pick(m, "eventId", "event_id")

    @property
    def token_id(self) -> str:
        m = self._ensure_market()
        return _pick(m, "tokenId", "token_id")

    def event(self) -> dict[str, Any]:
        if self._event is None:
            eid = self.event_id
            if not eid:
                return {}
            self._event = self.client.gamma.get_event(eid)
        return self._event

    async def aevent(self) -> dict[str, Any]:
        if self._event is None:
            eid = self.event_id
            if not eid:
                return {}
            self._event = await self.client.gamma.aget_event(eid)
        return self._event

    def orderbook(self) -> dict[str, Any]:
        tid = self.token_id
        if not tid:
            return {}
        return self.client.clob.get_orderbook(tid)

    async def aorderbook(self) -> dict[str, Any]:
        m = await self._aensure_market()
        tid = _pick(m, "tokenId", "token_id", "clobTokenId", "clob_token_id")
        if not tid:
            return {}
        return await self.client.clob.aget_orderbook(tid)
