from mongoengine import Document
from mongoengine.fields import (
    DateTimeField,
    IntField,
    ListField,
    ReferenceField,
    StringField,
)


class Track(Document):
    id = StringField(primary_key=True)
    name = StringField(required=True)
    album = ReferenceField("Album")
    artists = ListField(ReferenceField("Artist"))
    popularity = IntField()
    listening_count = IntField()
    last_time_listened = DateTimeField()
