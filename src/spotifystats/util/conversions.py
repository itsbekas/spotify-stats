from __future__ import annotations

from datetime import datetime
from math import floor


def iso_to_datetime(iso_str: str) -> datetime:
    try:
        return datetime.strptime(iso_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    except ValueError:
        return datetime.strptime(iso_str, "%Y-%m-%dT%H:%M:%SZ")


def datetime_to_int(dt: datetime) -> int:
    return floor(dt.timestamp() * 1000)
