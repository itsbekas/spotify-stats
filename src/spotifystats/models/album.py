from __future__ import annotations

from typing import TYPE_CHECKING, List

from mongoengine.fields import ListField, ReferenceField

import spotifystats.database as db
import spotifystats.models.artist as art
from spotifystats.models.named_document import NamedDocument

if TYPE_CHECKING:
    import spotifystats.models.track as trk


class Album(NamedDocument):
    artists = ListField(ReferenceField("Artist"))
    tracks = ListField(ReferenceField("Track"))

    @classmethod
    def from_spotify_response(cls, response) -> Album:

        artists = [
            art.Artist.from_spotify_response(artist_response)
            for artist_response in response["artists"]
        ]

        return cls(spotify_id=response["id"], name=response["name"], artists=artists)

    def get_id(self) -> str:
        return self.id

    def get_name(self) -> str:
        return self.name

    def get_artists(self) -> List[art.Artist]:
        return self.artists

    def add_artist(self, artist: art.Artist) -> None:
        if artist not in self.get_artists():
            self.artists.append(artist)

    def get_tracks(self) -> List[trk.Track]:
        return self.tracks

    def add_track(self, track: trk.Track) -> None:
        self.tracks.append(track)
