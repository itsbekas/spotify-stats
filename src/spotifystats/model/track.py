from mongoengine import Document
from mongoengine.fields import (
    DateTimeField,
    IntField,
    ListField,
    ReferenceField,
    StringField,
)
from ..model import Album, Artist


class Track(Document):
    id = StringField(primary_key=True)
    name = StringField(required=True)
    album = ReferenceField("Album")
    artists = ListField(ReferenceField("Artist"))
    popularity = IntField()
    plays = ListField(ReferenceField("Play"))
    rankings = ListField(ReferenceField("Ranking"))

    @classmethod
    def from_spotify_response(cls, response):
        album = Album.objects(id=response["album"]["id"]).first()
        artists = [
            Artist.objects(id=a["id"]).first() or Artist.from_spotify_response(a)
            for a in response["artists"]
        ]
        return cls(
            id=response["id"],
            name=response["name"],
            album=album,
            artists=artists,
            popularity=response["popularity"],
        )
