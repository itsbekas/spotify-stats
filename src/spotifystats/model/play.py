from mongoengine import Document
from mongoengine.fields import DateTimeField, ReferenceField


class Play(Document):
    track = ReferenceField("Track")
    timestamp = DateTimeField(primary_key=True)
