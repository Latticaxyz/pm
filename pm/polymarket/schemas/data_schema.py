from __future__ import annotations

from typing import Required, TypeAlias, TypedDict


class TradeRes(TypedDict, total=False):
    proxyWallet: Required[str]
    side: Required[str]
    asset: Required[str]
    conditionId: Required[str]
    size: Required[float]
    price: Required[float]
    timestamp: Required[int]
    title: Required[str]
    slug: Required[str]
    icon: Required[str]
    eventSlug: Required[str]
    outcome: Required[str]
    outcomeIndex: Required[int]
    name: Required[str]
    pseudonym: Required[str]
    bio: Required[str]
    profileImage: Required[str]
    profileImageOptimized: Required[str]
    transactionHash: Required[str]


TradesRes: TypeAlias = list[TradeRes]


class HolderRes(TypedDict, total=False):
    proxyWallet: Required[str]
    bio: Required[str]
    asset: Required[str]
    pseudonym: Required[str]
    amount: Required[float]
    displayUsernamePublic: Required[bool]
    outcomeIndex: Required[int]
    name: Required[str]
    profileImage: Required[str]
    profileImageOptimized: Required[str]


class TokenHoldersRes(TypedDict, total=False):
    token: Required[str]
    holders: Required[list[HolderRes]]


TopHoldersRes: TypeAlias = list[TokenHoldersRes]


class OpenInterestRes(TypedDict, total=False):
    market: Required[str]
    value: Required[float]


OpenInterestListRes: TypeAlias = list[OpenInterestRes]


class EventMarketVolumeRes(TypedDict, total=False):
    market: Required[str]
    value: Required[float]


class LiveVolumeRes(TypedDict, total=False):
    total: Required[float]
    markets: Required[list[EventMarketVolumeRes]]


LiveVolumeListRes: TypeAlias = list[LiveVolumeRes]
