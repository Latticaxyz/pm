from __future__ import annotations

from typing import Any

from pm.core import HTTPClient
from pm.polymarket.sources import OrderBookSummaryRes
from ..constants import CLOB_ORDERBOOK_PATH, CLOB_TRADES_PATH


class ClobHandler:
    def __init__(self, http: HTTPClient):
        self.http = http

    def get_orderbook_summary(self, token_id: str) -> OrderBookSummaryRes:
        return self.http.get_json(CLOB_ORDERBOOK_PATH, params={"token_id": token_id})

    def get_trades(self, token_id: str, *, limit: int = 50) -> dict[str, Any]:
        return self.http.get_json(CLOB_TRADES_PATH, params={"token_id": token_id})
