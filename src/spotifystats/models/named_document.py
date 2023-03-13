from mongoengine.fields import DateTimeField, StringField

from spotifystats.models.spotifystats_document import SpotifyStatsDocument


class NamedDocument(SpotifyStatsDocument):

    meta = {"allow_inheritance": True}

    spotify_id = StringField(required=True)
    name = StringField(required=True)
    last_retrieved = DateTimeField(required=True, default=None)

    def get_id(self):
        return self.spotify_id
