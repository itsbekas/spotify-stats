# from pprint import pformat

from mongoengine import Document


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
