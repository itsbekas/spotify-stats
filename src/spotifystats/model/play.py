from mongoengine import Document, DateTimeField


class Play(Document):

    timestamp = DateTimeField(required=True, unique=True)
    track = ReferenceField()
