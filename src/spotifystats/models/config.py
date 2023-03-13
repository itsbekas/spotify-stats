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
    
    def get_last_updated(self) -> datetime:
        return self.last_updated

    def set_last_updated(self, timestamp: datetime) -> None:
        self.last_updated = timestamp
