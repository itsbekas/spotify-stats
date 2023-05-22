from __future__ import annotations

from typing import List

from mongoengine.fields import IntField, ListField, ReferenceField, StringField

import spotifystats.models.artist as art
import spotifystats.models.track as trk
from spotifystats.models.named_document import NamedDocument
from spotifystats.util.lists import NamedDocumentList


class Album(NamedDocument):
    popularity = IntField(default=-1)
    genres = ListField(StringField())
    artists = ListField(ReferenceField("Artist"))
    tracks = ListField(ReferenceField("Track"))

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

    def get_tracks(self) -> List[trk.Track]:
        return NamedDocumentList(self.tracks)

    def add_track(self, track: trk.Track) -> None:
        # Check if album already has this track
        if track not in self.get_tracks():
            # Check if track is part of the album
            if self.get_id() in track.get_album().get_id():
                self.tracks.append(track)
