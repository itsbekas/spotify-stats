from __future__ import annotations

from typing import List

from mongoengine.fields import IntField, ListField, ReferenceField, StringField

import spotifystats.core.models.artist as art
import spotifystats.core.models.track as trk
from spotifystats.core.models.named_document import NamedDocument
from spotifystats.core.util.lists import NamedDocumentList


class Album(NamedDocument):
    popularity: int = IntField(default=-1)
    genres: List[str] = ListField(StringField())
    artists: List[art.Artist] = ListField(ReferenceField("Artist"))
    tracks: List[trk.Track] = ListField(ReferenceField("Track"))
    meta = {"collection": "albums"}

    @classmethod
    def from_spotify_response(cls, response) -> Album:
        popularity = response["popularity"] if "popularity" in response else None
        genres = response["genres"] if "genres" in response else []

        tracks = (
            [
                trk.Track.from_spotify_response(track_response)
                for track_response in response["tracks"]
            ]
            if "tracks" in response
            else []
        )

        artists = (
            [
                art.Artist.from_spotify_response(artist_response)
                for artist_response in response["artists"]
            ]
            if "artists" in response
            else []
        )

        return cls(
            spotify_id=response["id"],
            name=response["name"],
            popularity=popularity,
            genres=genres,
            artists=artists,
            tracks=tracks,
        )

    def get_popularity(self) -> int:
        return self.popularity

    def get_genres(self) -> List[str]:
        return self.genres

    def get_artists(self) -> List[art.Artist]:
        return NamedDocumentList(self.artists)

    def set_artist(self, index: int, artist: art.Artist) -> None:
        self.artists[index] = artist

    def get_tracks(self) -> List[trk.Track]:
        return NamedDocumentList(self.tracks)

    def add_track(self, track: trk.Track) -> None:
        # Check if album already has this track
        if track not in self.get_tracks():
            # Check if track is part of the album
            if self.get_id() in track.get_album().get_id():
                self.tracks.append(track)
