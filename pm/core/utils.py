from __future__ import annotations

import json
from typing import Any, Mapping


def pick(d: Mapping[str, Any], *keys: str) -> str:
    for k in keys:
        v = d.get(k)
        if v is None:
            continue
        s = str(v).strip()
        if s:
            return s
    return ""


def maybe_float(v: Any) -> float | None:
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return float(v)
    if isinstance(v, str):
        s = v.strip()
        if not s:
            return None
        try:
            return float(s)
        except ValueError:
            return None
    return None


def parse_json_list_str(v: Any) -> list[str]:
    if v is None:
        return []
    if isinstance(v, list):
        return [str(x) for x in v]
    if isinstance(v, str):
        s = v.strip()
        if not s:
            return []
        if s.startswith("[") and s.endswith("]"):
            try:
                out = json.loads(s)
                if isinstance(out, list):
                    return [str(x) for x in out]
            except Exception:
                return []
        return [s]
    return []


def as_dict(x: Any) -> dict[str, Any]:
    return dict(x) if isinstance(x, dict) else {}
