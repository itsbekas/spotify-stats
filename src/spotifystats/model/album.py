from mongoengine import Document
from mongoengine.fields import ListField, ReferenceField, StringField

from ..model import Track


class Album(Document):
    id = StringField(primary_key=True)
    name = StringField(required=True)
    artists = ListField(ReferenceField("Artist"))
    tracks = ListField(ReferenceField("Track"))

    @classmethod
    def from_spotify_response(cls, response):
        return cls(
            id = response["id"],
            name = response["name"]
            artists = 
        )
    
    def add_track(self, track: Track):
        self.tracks.append(Track)
