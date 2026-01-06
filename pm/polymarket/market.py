from __future__ import annotations

from dataclasses import dataclass
from typing import TypedDict

from pm.core import NotFoundError, maybe_float, parse_json_list_str, pick
from pm.polymarket.api.sources import MarketRes
from pm.polymarket.client import Polymarket


class MarketInfo(TypedDict):
    id: str | None
    slug: str | None
    condition_id: str | None
    token_ids: list[str] | None
    outcomes: list[str] | None
    outcome_prices: list[float] | None
    last_trade_price: float | None
    best_bid: float | None
    best_ask: float | None


@dataclass
class Market:
    client: "Polymarket"
    id: str | None = None
    slug: str | None = None

    _market: MarketRes | None = None

    def __post_init__(self) -> None:
        if not self.slug and not self.id:
            raise ValueError("Market requires either slug or id!")

    @classmethod
    def from_api_response(cls, *, client: "Polymarket", market: MarketRes) -> "Market":
        slug = pick(market, "slug", "market_slug", "marketSlug") or None
        mid = pick(market, "id", "marketId", "market_id") or None
        return cls(client=client, slug=slug, id=mid, _market=market)

    def _load_market(self) -> MarketRes:
        if self._market is not None:
            return self._market

        if self.slug:
            data: MarketRes = self.client.gamma.get_market_by_slug(self.slug)
            if data:
                self._market = data
                return data

            if self.id:
                data2: MarketRes = self.client.gamma.get_market_by_id(self.id)
                if data2:
                    self._market = data2
                    return data2
                raise ValueError(f"Market not found for slug={self.slug!r} or id={self.id!r}")

            raise NotFoundError(404, "Market not found", url=f"(slug={self.slug})")

        if self.id:
            data3: MarketRes = self.client.gamma.get_market_by_id(self.id)
            if not data3:
                raise NotFoundError(404, "Market not found", url=f"(id={self.id})")
            self._market = data3
            return data3

        # This should be unreachable from __post_init__
        raise ValueError("Market requires either slug or id!")

    @property
    def raw(self) -> MarketRes:
        return self._load_market()

    @property
    def info(self) -> MarketInfo:
        self._load_market()
        return {
            "id": self.market_id,
            "slug": self.slug,
            "condition_id": self.condition_id,
            "token_ids": self.token_ids,
            "outcomes": self.outcomes,
            "outcome_prices": self.prices,
            "last_trade_price": self.price,
            "best_bid": self.best_bid,
            "best_ask": self.best_ask,
        }

    @property
    def market_id(self) -> str:
        return pick(self._load_market(), "id", "market_id", "marketId")

    @property
    def condition_id(self) -> str:
        return pick(self._load_market(), "condition_id")

    @property
    def token_ids(self) -> list[str]:
        return parse_json_list_str(self._load_market().get("clobTokenIds"))

    @property
    def outcomes(self) -> list[str]:
        return parse_json_list_str(self._load_market().get("outcomes"))

    @property
    def prices(self) -> list[float]:
        raw = parse_json_list_str(self._load_market().get("outcomePrices"))
        out: list[float] = []
        for x in raw:
            fx = maybe_float(x)
            if fx is not None:
                out.append(fx)
        return out

    @property
    def price(self) -> float | None:
        ltp = maybe_float(self._load_market().get("lastTradePrice"))
        if ltp is not None:
            return ltp
        ps = self.prices
        return ps[0] if ps else None

    @property
    def best_bid(self) -> float | None:
        return maybe_float(self._load_market().get("best_bid"))

    @property
    def best_ask(self) -> float | None:
        return maybe_float(self._load_market().get("best_ask"))
