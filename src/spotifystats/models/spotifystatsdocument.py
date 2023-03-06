from mongoengine import Document
from pprint import pformat

class SpotifyStatsDocument(Document):

    meta = {
        'allow_inheritance': True
    }
    
    def __repr__(self) -> str:
        fields = self.to_mongo().to_dict()
        return f"{type(self).__name__}({fields})"

    # newlines and indentation
    # def __repr__(self) -> dict:
    #     fields = self.to_mongo().to_dict()
    #     return f"{type(self).__name__}(\n{pformat(fields, indent=4)}\n)"