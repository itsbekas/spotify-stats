from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List
    import spotifystats.models.play as play
    import spotifystats.models.ranking as rnk

from mongoengine.fields import IntField, ListField, ReferenceField, StringField

import spotifystats.database as db
import spotifystats.models.album as alb
import spotifystats.models.artist as art
from spotifystats.models.named_document import NamedDocument


class Track(NamedDocument):
    album = ReferenceField("Album")
    artists = ListField(ReferenceField("Artist"))
    popularity = IntField(required=True)
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
                artist = art.Artist.from_spotify_response(artist_response)
            artists.append(artist)

        return cls(
            spotify_id=response["id"],
            name=response["name"],
            album=album,
            artists=artists,
            popularity=response["popularity"],
        )

    def get_album(self) -> alb.Album:
        return self.album

    def get_artists(self) -> art.Artist:
        return self.artists

    def get_popularity(self) -> int:
        return self.popularity

    def get_plays(self) -> List[play.Play]:
        return self.plays

    def get_rankings(self) -> List[rnk.Ranking]:
        return self.rankings
