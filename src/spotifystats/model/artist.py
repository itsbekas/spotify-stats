from mongoengine import Document
from mongoengine.fields import ListField, StringField


class Artist(Document):
    id = StringField(primary_key=True)
    name = StringField(required=True)
    tracks = ListField(StringField())

    @classmethod
    def from_spotify_response(cls, response):
        return cls(id=response["id"], name=response["name"])
