from mongoengine import DateTimeField, Document, EmbeddedDocumentField

from spotifystats.model import ArtistRanking, TrackRanking


class Ranking(Document):

    timestamp = DateTimeField(required=True, unique=True)
    artists = EmbeddedDocumentField(ArtistRanking)
    tracks = EmbeddedDocumentField(TrackRanking)
