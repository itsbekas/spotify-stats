from __future__ import annotations

from datetime import datetime

from mongoengine.fields import DateTimeField

from spotifystats.core.models.spotifystats_document import SpotifyStatsDocument


class DatedDocument(SpotifyStatsDocument):
    timestamp: datetime = DateTimeField(required=True)
    meta = {
        "abstract": True,
        "indexes": ["timestamp"],
        "ordering": ["-timestamp"],
    }

    def get_timestamp(self) -> datetime:
        return self.timestamp
