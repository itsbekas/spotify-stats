from __future__ import annotations

from datetime import datetime

from mongoengine.fields import DateTimeField, StringField

from spotifystats.models.spotifystats_document import SpotifyStatsDocument


class NamedDocument(SpotifyStatsDocument):
    meta = meta = {"allow_inheritance": True, "indexes": ["spotify_id"]}

    spotify_id = StringField(required=True)
    name = StringField(required=True)
    last_retrieved = DateTimeField(default=None)

    def get_id(self) -> str:
        return self.spotify_id

    def get_name(self) -> str:
        return self.name

    def get_last_retrieved(self) -> datetime:
        return self.last_retrieved
