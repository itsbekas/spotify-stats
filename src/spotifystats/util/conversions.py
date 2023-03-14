from __future__ import annotations

from datetime import datetime
from math import floor
from typing import TYPE_CHECKING


def iso_to_datetime(iso_str: str) -> datetime:
    return datetime.strptime(iso_str, '%Y-%m-%dT%H:%M:%S.%fZ')

def datetime_to_int(dt: datetime) -> int:
    return floor(dt.timestamp() * 1000)