from __future__ import annotations

from typing import Required, TypeAlias, TypedDict


class OrderBookLevelRes(TypedDict):
    price: str
    size: str


class OrderBookSummaryRes(TypedDict, total=False):
    market: Required[str]
    asset_id: Required[str]
    timestamp: Required[str]
    hash: Required[str]
    bids: Required[list[OrderBookLevelRes]]
    asks: Required[list[OrderBookLevelRes]]
    min_order_size: Required[str]
    tick_size: Required[str]
    neg_risk: Required[bool]


OrderBooksSummariesRes: TypeAlias = list[OrderBookSummaryRes]


class OrderBookHistoryRes(TypedDict, total=False):
    count: Required[int]
    data: Required[list[OrderBookSummaryRes]]


class PriceRes(TypedDict, total=False):
    price: Required[str]


class SideToPriceRes(TypedDict, total=False):
    BUY: str
    SELL: str


PricesRes: TypeAlias = dict[str, SideToPriceRes]


class MidpointRes(TypedDict, total=False):
    mid: Required[str]


class PricesHistoryPointRes(TypedDict, total=False):
    t: Required[int]
    p: Required[float]


class PricesHistoryRes(TypedDict, total=False):
    history: Required[list[PricesHistoryPointRes]]


SpreadsRes: TypeAlias = dict[str, str]
