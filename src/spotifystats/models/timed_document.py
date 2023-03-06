from mongoengine.fields import DateTimeField

from spotifystats.models.spotifystats_document import SpotifyStatsDocument

class TimedDocument(SpotifyStatsDocument):

    meta = {
        'allow_inheritance': True
    }

    timestamp = DateTimeField(required=True)
    
