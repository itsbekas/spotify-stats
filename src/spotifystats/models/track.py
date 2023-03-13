from __future__ import annotations

from typing import TYPE_CHECKING

from mongoengine.fields import IntField, ListField, ReferenceField, StringField

import spotifystats.database as db
import spotifystats.models.album as alb
import spotifystats.models.artist as art
from spotifystats.models.named_document import NamedDocument


class Track(NamedDocument):
    album = ReferenceField("Album")
    artists = ListField(ReferenceField("Artist"))
    popularity = IntField()
    plays = ListField(ReferenceField("Play"))
    rankings = ListField(ReferenceField("Ranking"))

    @classmethod
    def from_spotify_response(cls, response) -> Track:

        album = db.get_album(response["album"]["id"])
        if album is None:
            album = alb.Album.from_spotify_response(response["album"])

        artists = []
        for artist_response in response["artists"]:
            artist = db.get_artist(artist_response["id"])
            if artist is None:
                artist = art.Artist.from_spotify_response(artist)
            artists.append(artist)

        return cls(
            spotify_id=response["id"],
            name=response["name"],
            album=album,
            artists=artists,
            popularity=response["popularity"],
        )
