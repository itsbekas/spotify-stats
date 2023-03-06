from __future__ import annotations

from typing import TYPE_CHECKING, List

from mongoengine.fields import ListField, ReferenceField, StringField

import spotifystats.models.artist as art
from spotifystats.models.spotifystatsdocument import SpotifyStatsDocument

if TYPE_CHECKING:
    import spotifystats.models.track as trk

class Album(SpotifyStatsDocument):
    id = StringField(primary_key=True)
    name = StringField(required=True)
    artists = ListField(ReferenceField("Artist"))
    tracks = ListField(ReferenceField("Track"))

    @classmethod
    def from_spotify_response(cls, response):
        return cls(
            id = response["id"],
            name = response["name"],
            artists = [art.Artist.from_spotify_response(artist) for artist in response["artists"]]
        )

    def get_id(self) -> str:
        return self.id
    
    def get_name(self) -> str:
        return self.name
    
    def get_artists(self) -> List[art.Artist]:
        # TODO: test if [artist.fetch() for artist in self.artists] is necessary, maybe lazyreference
        return self.artists
    
    def add_track(self, track: trk.Track) -> None:
        self.tracks.append(track)

    def get_tracks(self) -> List[trk.Track]:
        return self.tracks
    