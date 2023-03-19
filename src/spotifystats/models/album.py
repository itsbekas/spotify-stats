from __future__ import annotations

from typing import TYPE_CHECKING, List

from mongoengine.fields import ListField, ReferenceField

import spotifystats.models.artist as art
from spotifystats.models.named_document import NamedDocument

from spotifystats.util import is_duplicate

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

    def get_artists(self) -> List[art.Artist]:
        return self.artists

    def get_tracks(self) -> List[trk.Track]:
        return self.tracks

    def add_track(self, track: trk.Track) -> None:
        if not is_duplicate(track, self.get_tracks()):
            self.tracks.append(track)
