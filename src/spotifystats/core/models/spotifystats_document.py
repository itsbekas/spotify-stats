# from pprint import pformat

import json

from mongoengine import Document


class SpotifyStatsDocument(Document):
    meta = {"abstract": True}

    # inline
    def __str__(self) -> str:
        fields = self.to_mongo().to_dict()
        return f"{type(self).__name__}({fields})"

    # newlines and indentation
    # def __str__(self) -> dict:
    #     fields = self.to_mongo().to_dict()
    #     return f"{type(self).__name__}(\n{pformat(fields, indent=4)}\n)"

    def to_json(self):
        document = self.to_mongo().to_dict()

        print(document)

        if "_id" in document:
            document.pop("_id")

        if "spotify_id" in document:
            document["id"] = str(document.pop("spotify_id"))

        if "track" in document:
            document["track"] = str(document["track"])

        if "last_retrieved" in document:
            document["last_retrieved"] = document["last_retrieved"].isoformat()

        if "timestamp" in document:
            document["timestamp"] = document["timestamp"].isoformat()

        if "rankings" in document:
            document.pop("rankings")

        # return document as json object
        return json.loads(json.dumps(document))
