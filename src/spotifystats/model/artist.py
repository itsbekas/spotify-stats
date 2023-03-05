from mongoengine import Document
from mongoengine.fields import ListField, ReferenceField, StringField

import spotifystats.model.album as alb
import spotifystats.model.track as trk


class Artist(Document):
    id = StringField(primary_key=True)
    name = StringField(required=True)
    albums = ListField(ReferenceField("Album"))
    tracks = ListField(ReferenceField("Track"))

    @classmethod
    def from_spotify_response(cls, response):
        return cls(id=response["id"], name=response["name"])

    def add_album(self, album: alb.Album):
        self.albums.append(album)

    def add_track(self, track: trk.Track):
        self.tracks.append(track)
