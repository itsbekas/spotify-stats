from mongoengine import Document, StringField, ReferenceField, DateTimeField, IntField


class Track(Document):
    id = StringField(primary_key=True)
    name = StringField(required=True)
    album = ReferenceField("Album")
    artists = ListField(ReferenceField("Artist"))
    popularity = IntField()
    listening_count = IntField()
    last_time_listened = DateTimeField()
