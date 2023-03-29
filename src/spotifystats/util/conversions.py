from __future__ import annotations

from datetime import datetime
from math import floor

from dateutil import parser


def iso_to_datetime(iso_str: str) -> datetime:
    return parser.parse(iso_str)


def datetime_to_int(dt: datetime) -> int:
    return floor(dt.timestamp() * 1000)
