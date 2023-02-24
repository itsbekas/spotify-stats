from mongoengine import Document
from mongoengine.fields import ListField, StringField


class Artist(Document):
    id = StringField(primary_key=True)
    name = StringField(required=True)
    tracks = ListField(StringField())
