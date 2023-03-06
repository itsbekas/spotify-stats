from __future__ import annotations

import json
from typing import TYPE_CHECKING, List

from mongoengine.fields import ListField, ReferenceField, StringField

from spotifystats.models.spotifystatsdocument import SpotifyStatsDocument

if TYPE_CHECKING:
    import spotifystats.models.album as alb
    import spotifystats.models.track as trk


class Artist(SpotifyStatsDocument):
    id = StringField(primary_key=True)
    name = StringField(required=True)
    albums = ListField(ReferenceField("Album"))
    tracks = ListField(ReferenceField("Track"))

    @classmethod
    def from_spotify_response(cls, response):
        return cls(id=response["id"], name=response["name"])

    def get_id(self) -> str:
        return self.id
    
    def get_name(self) -> str:
        return self.name
    
    def get_albums(self) -> List[alb.Album]:
        return self.albums
    
    def add_album(self, album: alb.Album):
        self.albums.append(album)

    def get_tracks(self) -> List[trk.Track]:
        return self.tracks

    def add_track(self, track: trk.Track):
        self.tracks.append(track)
