from mongoengine import Document, IntField, StringField


class Artist(Document):

    id = StringField(required=True, unique=True, primary_key=True)
    name = StringField(required=True)
    count = IntField(required=True, default=0)
    last_listened = IntField(required=True, default=0)
