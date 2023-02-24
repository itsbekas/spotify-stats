from mongoengine import Document, fields


class Play(Document):
    track = fields.ReferenceField("Track")
    timestamp = fields.DateTimeField(primary_key=True)
