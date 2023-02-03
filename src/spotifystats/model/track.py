from mongoengine import Document, IntField, ListField, ReferenceField, StringField

from spotifystats.model import Artist


class Track(Document):

    id = StringField(required=True, unique=True)
    name = StringField(required=True)
    artists = ListField(ReferenceField(Artist))
    genre = ListField(StringField())
    count = IntField(required=True, default=0)
    last_listened = IntField(required=True, default=0)
