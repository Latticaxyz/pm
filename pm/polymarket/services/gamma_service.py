from __future__ import annotations

from typing import Optional
from datetime import datetime

from pm.core import HTTPClient
from ..constants import GAMMA_EVENTS_PATH, GAMMA_MARKETS_PATH
from ..schemas.gamma_schema import MarketRes, MarketsRes, EventRes, EventsRes


class GammaService:
    def __init__(self, http: HTTPClient):
        self.http = http

    def list_markets(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order: Optional[str] = None,
        ascending: Optional[bool] = None,
        id: Optional[list[int]] = None,
        slug: Optional[list[str]] = None,
        clob_token_ids: Optional[list[str]] = None,
        condition_ids: Optional[list[str]] = None,
        market_maker_address: Optional[list[str]] = None,
        liquidity_num_min: Optional[float] = None,
        liquidity_num_max: Optional[float] = None,
        volume_num_min: Optional[float] = None,
        volume_num_max: Optional[float] = None,
        start_date_min: Optional[datetime] = None,
        start_date_max: Optional[datetime] = None,
        end_date_min: Optional[datetime] = None,
        end_date_max: Optional[datetime] = None,
        tag_id: Optional[int] = None,
        related_tags: Optional[bool] = None,
        cyom: Optional[bool] = None,
        uma_resolution_status: Optional[str] = None,
        game_id: Optional[str] = None,
        sports_market_types: Optional[list[str]] = None,
        rewards_min_size: Optional[float] = None,
        question_ids: Optional[list[str]] = None,
        include_tag: Optional[bool] = None,
        closed: Optional[bool] = None,
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
            "start_date_min": start_date_min,
            "start_date_max": start_date_max,
            "end_date_min": end_date_min,
            "end_date_max": end_date_max,
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
        return self.http.get_json(GAMMA_MARKETS_PATH, params=params)

    def get_market_by_slug(
        self, slug: str, include_tag: Optional[bool] = None
    ) -> MarketRes:
        return self.http.get_json(
            f"GAMMA_MARKETS_PATH/slug/{slug}", params={"include_tag": include_tag}
        )

    def get_market_by_id(self, id: str, include_tag: Optional[bool]) -> MarketRes:
        return self.http.get_json(
            f"{GAMMA_MARKETS_PATH}/{id}", params={"include_tag": include_tag}
        )

    # Need to implement this
    def get_market_tags(self):
        pass

    def list_events(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        order: Optional[str] = None,
        ascending: Optional[bool] = None,
        id: Optional[list[int]] = None,
        tag_id: Optional[int] = None,
        exclude_tag_id: Optional[list[int]] = None,
        slug: Optional[list[str]] = None,
        tag_slug: Optional[str] = None,
        related_tags: Optional[bool] = None,
        active: Optional[bool] = None,
        archived: Optional[bool] = None,
        featured: Optional[bool] = None,
        cyom: Optional[bool] = None,
        include_chat: Optional[bool] = None,
        include_template: Optional[bool] = None,
        recurrence: Optional[str] = None,
        closed: Optional[bool] = None,
        liquidity_min: Optional[float] = None,
        liquidity_max: Optional[float] = None,
        volume_min: Optional[float] = None,
        volume_max: Optional[float] = None,
        start_date_min: Optional[datetime] = None,
        start_date_max: Optional[datetime] = None,
        end_date_min: Optional[datetime] = None,
        end_date_max: Optional[datetime] = None,
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
            "start_date_min": start_date_min,
            "start_date_max": start_date_max,
            "end_date_min": end_date_min,
            "end_date_max": end_date_max,
        }
        return self.http.get_json(GAMMA_EVENTS_PATH, params=params)

    def get_event_by_id(
        self,
        id: str,
        include_chat: Optional[bool] = None,
        include_template: Optional[bool] = None,
    ) -> EventRes:
        return self.http.get_json(
            f"{GAMMA_EVENTS_PATH}/{id}",
            params={"include_chat": include_chat, "include_template": include_template},
        )

    def get_event_by_slug(
        self,
        slug: str,
        include_chat: Optional[bool] = None,
        include_template: Optional[bool] = None,
    ) -> EventRes:
        return self.http.get_json(
            f"{GAMMA_EVENTS_PATH}/slug/{slug}",
            params={"include_chat": include_chat, "include_template": include_template},
        )

    # Need to implement this
    def get_event_tags(self):
        pass
