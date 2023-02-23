from mongoengine import Document, IntField, ListField, ReferenceField, StringField

from spotifystats.model import Album, Artist


class Track(Document):
    
    # Data from the Spotify API
    # See available fields: https://developer.spotify.com/documentation/web-api/reference/#/operations/get-track
    album = ReferenceField(Album)
    artists = ListField(ReferenceField(Artist))
    id = StringField(required=True, unique=True)
    genre = ListField(StringField())
    name = StringField(required=True)

    # Custom fields
    count = IntField(required=True, default=0)
    last_listened = IntField(required=True, default=0)
