from __future__ import annotations

from datetime import datetime

from mongoengine.fields import DateTimeField, StringField

from spotifystats.core.models.spotifystats_document import SpotifyStatsDocument
from spotifystats.core.util.conversions import int_to_datetime


class NamedDocument(SpotifyStatsDocument):
    meta = {"abstract": True, "indexes": ["spotify_id", "name"]}

    spotify_id: str = StringField(required=True)
    name: str = StringField(required=True)
    last_retrieved: datetime = DateTimeField(default=int_to_datetime(0))

    def get_id(self) -> str:
        return self.spotify_id

    def get_name(self) -> str:
        return self.name

    def get_last_retrieved(self) -> datetime:
        return self.last_retrieved
