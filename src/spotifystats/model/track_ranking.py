from mongoengine import EmbeddedDocument, ReferenceField, ListField
from spotifystats.model import Track


class TrackRanking(EmbeddedDocument):

    short_term = ListField(ReferenceField(Track))
    medium_term = ListField(ReferenceField(Track))
    long_term = ListField(ReferenceField(Track))
