from __future__ import annotations

from datetime import datetime
from typing import cast

from pm.core import HTTPClient
from pm.polymarket.api.sources import EventRes, EventsRes, MarketRes, MarketsRes
from pm.polymarket.constants import GAMMA_EVENTS_PATH, GAMMA_MARKETS_PATH


class GammaHandler:
    http: HTTPClient

    def __init__(self, http: HTTPClient):
        self.http = http

    def list_markets(
        self,
        limit: int | None = None,
        offset: int | None = None,
        order: str | None = None,
        ascending: bool | None = None,
        id: list[int] | None = None,
        slug: list[str] | None = None,
        clob_token_ids: list[str] | None = None,
        condition_ids: list[str] | None = None,
        market_maker_address: list[str] | None = None,
        liquidity_num_min: float | None = None,
        liquidity_num_max: float | None = None,
        volume_num_min: float | None = None,
        volume_num_max: float | None = None,
        start_date_min: datetime | None = None,
        start_date_max: datetime | None = None,
        end_date_min: datetime | None = None,
        end_date_max: datetime | None = None,
        tag_id: int | None = None,
        related_tags: bool | None = None,
        cyom: bool | None = None,
        uma_resolution_status: str | None = None,
        game_id: str | None = None,
        sports_market_types: list[str] | None = None,
        rewards_min_size: float | None = None,
        question_ids: list[str] | None = None,
        include_tag: bool | None = None,
        closed: bool | None = None,
    ) -> MarketsRes:
        params = {
            "limit": limit,
            "offset": offset,
            "order": order,
            "ascending": ascending,
            "id": id,
            "slug": slug,
            "clob_token_ids": clob_token_ids,
            "condition_ids": condition_ids,
            "market_maker_address": market_maker_address,
            "liquidity_num_min": liquidity_num_min,
            "liquidity_num_max": liquidity_num_max,
            "volume_num_min": volume_num_min,
            "volume_num_max": volume_num_max,
            "start_date_min": start_date_min.isoformat() if start_date_min else None,
            "start_date_max": start_date_max.isoformat() if start_date_max else None,
            "end_date_min": end_date_min.isoformat() if end_date_min else None,
            "end_date_max": end_date_max.isoformat() if end_date_max else None,
            "tag_id": tag_id,
            "related_tags": related_tags,
            "cyom": cyom,
            "uma_resolution_status": uma_resolution_status,
            "game_id": game_id,
            "sports_market_types": sports_market_types,
            "rewards_min_size": rewards_min_size,
            "question_ids": question_ids,
            "include_tag": include_tag,
            "closed": closed,
        }
        return cast(MarketsRes, self.http.get_json(GAMMA_MARKETS_PATH, params=params))

    def get_market_by_slug(self, slug: str, include_tag: bool | None = None) -> MarketRes:
        return cast(
            MarketRes,
            self.http.get_json(f"{GAMMA_MARKETS_PATH}/slug/{slug}", params={"include_tag": include_tag}),
        )

    def get_market_by_id(self, id: str, include_tag: bool | None = None) -> MarketRes:
        return cast(
            MarketRes,
            self.http.get_json(f"{GAMMA_MARKETS_PATH}/{id}", params={"include_tag": include_tag}),
        )

    def get_market_tags(self) -> None:
        pass

    def list_events(
        self,
        limit: int | None = None,
        offset: int | None = None,
        order: str | None = None,
        ascending: bool | None = None,
        id: list[int] | None = None,
        tag_id: int | None = None,
        exclude_tag_id: list[int] | None = None,
        slug: list[str] | None = None,
        tag_slug: str | None = None,
        related_tags: bool | None = None,
        active: bool | None = None,
        archived: bool | None = None,
        featured: bool | None = None,
        cyom: bool | None = None,
        include_chat: bool | None = None,
        include_template: bool | None = None,
        recurrence: str | None = None,
        closed: bool | None = None,
        liquidity_min: float | None = None,
        liquidity_max: float | None = None,
        volume_min: float | None = None,
        volume_max: float | None = None,
        start_date_min: datetime | None = None,
        start_date_max: datetime | None = None,
        end_date_min: datetime | None = None,
        end_date_max: datetime | None = None,
    ) -> EventsRes:
        params = {
            "limit": limit,
            "offset": offset,
            "order": order,
            "ascending": ascending,
            "id": id,
            "tag_id": tag_id,
            "exclude_tag_id": exclude_tag_id,
            "slug": slug,
            "tag_slug": tag_slug,
            "related_tags": related_tags,
            "active": active,
            "archived": archived,
            "featured": featured,
            "cyom": cyom,
            "include_chat": include_chat,
            "include_template": include_template,
            "recurrence": recurrence,
            "closed": closed,
            "liquidity_min": liquidity_min,
            "liquidity_max": liquidity_max,
            "volume_min": volume_min,
            "volume_max": volume_max,
            "start_date_min": start_date_min.isoformat() if start_date_min else None,
            "start_date_max": start_date_max.isoformat() if start_date_max else None,
            "end_date_min": end_date_min.isoformat() if end_date_min else None,
            "end_date_max": end_date_max.isoformat() if end_date_max else None,
        }
        return cast(EventsRes, self.http.get_json(GAMMA_EVENTS_PATH, params=params))

    def get_event_by_id(
        self,
        id: str,
        include_chat: bool | None = None,
        include_template: bool | None = None,
    ) -> EventRes:
        return cast(
            EventRes,
            self.http.get_json(
                f"{GAMMA_EVENTS_PATH}/{id}",
                params={
                    "include_chat": include_chat,
                    "include_template": include_template,
                },
            ),
        )

    def get_event_by_slug(
        self,
        slug: str,
        include_chat: bool | None = None,
        include_template: bool | None = None,
    ) -> EventRes:
        return cast(
            EventRes,
            self.http.get_json(
                f"{GAMMA_EVENTS_PATH}/slug/{slug}",
                params={
                    "include_chat": include_chat,
                    "include_template": include_template,
                },
            ),
        )

    def get_event_tags(self) -> None:
        pass
