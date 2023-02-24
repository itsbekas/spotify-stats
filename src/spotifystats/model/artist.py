from mongoengine import Document, StringField, ListField


class Artist(Document):
    id = StringField(primary_key=True)
    name = StringField(required=True)
    tracks = ListField(StringField())
