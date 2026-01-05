from __future__ import annotations

from typing import Any, cast

from pm.core import HTTPClient
from pm.polymarket.constants import DATA_OI_PATH


class DataHandler:
    http: HTTPClient

    def __init__(self, http: HTTPClient):
        self.http = http

    def get_global_oi(self) -> dict[str, Any]:
        return cast(dict[str, Any], self.http.get_json(f"{DATA_OI_PATH}"))

    def get_market_oi(self, condition_id: str) -> dict[str, Any]:
        data = self.http.get_json(DATA_OI_PATH, params={"market": condition_id})
        if isinstance(data, list):
            return cast(dict[str, Any], data[0] if data else {})
        return cast(dict[str, Any], data)
