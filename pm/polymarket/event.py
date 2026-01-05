from __future__ import annotations

from pm.polymarket.api.sources import EventRes
from pm.polymarket.client import Polymarket

# from pm.core import pick, maybe_float, parse_json_list_str, NotFoundError


class Event:
    client: "Polymarket"
    id: str | None = None
    slug: str | None = None

    _event: EventRes

    def __post_init__(self) -> None:
        if not self.slug and not self.id:
            raise ValueError("Event requires either slug or id!")
