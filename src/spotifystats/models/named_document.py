from mongoengine.fields import DateTimeField, StringField

from spotifystats.models.spotifystats_document import SpotifyStatsDocument


class NamedDocument(SpotifyStatsDocument):

    meta = {
        'allow_inheritance': True
    }

    id = StringField(primary_key=True)
    name = StringField(required=True)
    last_retrieved = DateTimeField(required=True, default=None)
