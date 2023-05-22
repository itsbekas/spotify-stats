from __future__ import annotations

from datetime import datetime

from mongoengine.fields import DateTimeField

from spotifystats.models.spotifystats_document import SpotifyStatsDocument


class DatedDocument(SpotifyStatsDocument):
    timestamp = DateTimeField(required=True, default=datetime.utcfromtimestamp(0))
    meta = {
        "allow_inheritance": True,
        "indexes": ["timestamp"],
        "ordering": ["-timestamp"],
    }

    def get_timestamp(self) -> datetime:
        return self.timestamp
