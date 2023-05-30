from __future__ import annotations

from mongoengine.fields import StringField

from spotifystats.models.dated_document import DatedDocument


class Ranking(DatedDocument):
    meta = {"abstract": True}

    SHORT = "short_term"
    MEDIUM = "medium_term"
    LONG = "long_term"
    TIME_CHOICES = (
        (SHORT, "Last 4 Weeks"),
        (MEDIUM, "Last 6 Months"),
        (LONG, "All Time"),
    )

    time_range = StringField(required=True, choices=TIME_CHOICES)

    def get_time_range(self) -> str:
        return self.time_range

    def set_time_range(self, time_range: str) -> None:
        self.time_range = time_range
