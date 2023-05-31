from datetime import datetime

from mongoengine import DateTimeField, Document

from spotifystats.util.conversions import int_to_datetime


class Config(Document):
    last_ranking_update: datetime = DateTimeField(default=int_to_datetime(0))

    meta = {"collection": "config"}

    def get_last_ranking_update(self) -> datetime:
        return self.last_ranking_update

    def set_last_ranking_update(self, last_ranking_update: datetime) -> None:
        self.last_ranking_update = last_ranking_update
