from mongoengine import Document, StringField, ListField, ReferenceField


class Album(Document):
    id = StringField(primary_key=True)
    name = StringField(required=True)
    artists = ListField(ReferenceField("Artist"))
    tracks = ListField(StringField())
