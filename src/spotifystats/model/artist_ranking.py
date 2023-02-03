from mongoengine import EmbeddedDocument, ReferenceField, ListField
from spotifystats.model import Artist


class ArtistRanking(EmbeddedDocument):

    short_term = ListField(ReferenceField(Artist))
    medium_term = ListField(ReferenceField(Artist))
    long_term = ListField(ReferenceField(Artist))
