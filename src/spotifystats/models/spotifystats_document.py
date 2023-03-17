from pprint import pformat

from mongoengine import Document
from mongoengine.fields import DateTimeField


class SpotifyStatsDocument(Document):

    meta = {"allow_inheritance": True}

    # inline
    def __str__(self) -> str:
        fields = self.to_mongo().to_dict()
        return f"{type(self).__name__}({fields})"

    # newlines and indentation
    # def __str__(self) -> dict:
    #     fields = self.to_mongo().to_dict()
    #     return f"{type(self).__name__}(\n{pformat(fields, indent=4)}\n)"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def bruh(self):
        print(self.__dict__)
