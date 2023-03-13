from __future__ import annotations

from typing import TYPE_CHECKING

from mongoengine.fields import ListField, ReferenceField, StringField

from spotifystats.models.timed_document import TimedDocument


class Ranking(TimedDocument):
    SHORT = "short"
    MEDIUM = "medium"
    LONG = "long"
    TIME_CHOICES = (
        (SHORT, "Last 4 Weeks"),
        (MEDIUM, "Last 6 Months"),
        (LONG, "All Time"),
    )

    ARTIST = "artist"
    TRACK = "track"
    TYPE_CHOICES = ((ARTIST, "Artist"), (TRACK, "Track"))

    type = StringField(choices=TYPE_CHOICES)
    time_range = StringField(choices=TIME_CHOICES)
    tracks = ListField(ReferenceField("Track"))

    @classmethod
    def from_spotify_response(cls, response) -> Ranking:
        return cls(type="bruh")
