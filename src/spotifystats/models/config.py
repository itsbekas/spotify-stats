import datetime

from mongoengine import Document
from mongoengine.fields import DateTimeField


class Config(Document):
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
    
    @staticmethod
    def set_last_updated(timestamp: datetime) -> None:
        cfg = Config.get_config()
        cfg.last_updated = timestamp
        cfg.save()
