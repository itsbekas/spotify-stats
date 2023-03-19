from __future__ import annotations

from typing import TYPE_CHECKING

from mongoengine.fields import ListField, ReferenceField, StringField

from spotifystats.models.dated_document import DatedDocument


class Ranking(DatedDocument):
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

    rank_type = StringField(required=True, choices=TYPE_CHOICES)
    time_range = StringField(required=True, choices=TIME_CHOICES)
    tracks = ListField(ReferenceField("Track"))

    @classmethod
    def from_spotify_response(cls, response) -> Ranking:
        return cls(type="bruh")

    def get_type(self):
        return self.rank_type

    def get_time_range(self):
        return self.time_range

    def get_tracks(self):
        return self.tracks
