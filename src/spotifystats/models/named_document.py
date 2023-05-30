from __future__ import annotations

from datetime import datetime

from mongoengine.fields import DateTimeField, StringField

from spotifystats.models.spotifystats_document import SpotifyStatsDocument
from spotifystats.util.conversions import int_to_datetime


class NamedDocument(SpotifyStatsDocument):
    meta = {"abstract": True, "indexes": ["spotify_id", "name"]}

    spotify_id = StringField(required=True)
    name = StringField(required=True)
    last_retrieved = DateTimeField(default=int_to_datetime(0))

    def get_id(self) -> str:
        return self.spotify_id

    def get_name(self) -> str:
        return self.name

    def get_last_retrieved(self) -> datetime:
        return self.last_retrieved
