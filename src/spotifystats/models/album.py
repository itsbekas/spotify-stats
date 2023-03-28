from __future__ import annotations

from typing import TYPE_CHECKING, List

from mongoengine.fields import ListField, ReferenceField

import spotifystats.models.artist as art
from spotifystats.models.named_document import NamedDocument
from spotifystats.util.lists import NamedDocumentList

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
        return NamedDocumentList(self.artists)

    def get_tracks(self) -> List[trk.Track]:
        return NamedDocumentList(self.tracks)

    def add_track(self, track: trk.Track) -> None:
        # Check if album already has this track
        if track not in self.get_tracks():
            # Check if track is part of the album
            if self.get_id() in track.get_album().get_id():
                self.tracks.append(track)
