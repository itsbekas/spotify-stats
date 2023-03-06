import datetime

from mongoengine.fields import DateTimeField

from spotifystats.models.spotifystatsdocument import SpotifyStatsDocument


class Config(SpotifyStatsDocument):
    last_updated = DateTimeField(required=True, default=datetime.datetime.now)

    @staticmethod
    def get_config():
        """
        Get the singleton Config document. If it doesn't exist, create it.
        """
        config = Config.objects.first()
        if not config:
            # Create the Config document with default values
            config = Config()
            config.save()
        return config
