from mongoengine import Document
from mongoengine.fields import ListField, ReferenceField, StringField


class Album(Document):
    id = StringField(primary_key=True)
    name = StringField(required=True)
    artists = ListField(ReferenceField("Artist"))
    tracks = ListField(StringField())
