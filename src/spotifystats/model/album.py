from __future__ import annotations

from typing import TYPE_CHECKING

from mongoengine import Document
from mongoengine.fields import ListField, ReferenceField, StringField

if TYPE_CHECKING:
    from spotifystats.model.track import Track


class Album(Document):
    id = StringField(primary_key=True)
    name = StringField(required=True)
    artists = ListField(ReferenceField("Artist"))
    tracks = ListField(ReferenceField("Track"))

    @classmethod
    def from_spotify_response(cls, response):
        return cls(id=response["id"], name=response["name"])

    def add_track(self, track: Track) -> None:
        self.tracks.append(track)
