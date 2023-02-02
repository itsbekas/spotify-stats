from abc import ABC
from enum import Enum
from os import environ

from pymongo import MongoClient

from spotifystats.model.item import Item


class Collection(Enum):
    ARTISTS = "artists"
    TRACKS = "tracks"
    RANKINGS = "rankings"
    COMMON = "common"
    HISTORY = "history"


class Database(ABC):
    def __init__(self, dbname: str, collection: str) -> None:
        client: MongoClient = MongoClient(environ["SPOTIFYSTATS_MONGODB_URI"])
        self._db = client[dbname]
        self._collection = self._db[collection]

    def _get_collection(self, collection: str):
        """Retrieves a collection from the database"""
        return self._db[collection]

    def _add_item(self, item: Item) -> None:
        if self._get_item_by_id(item.id) != None:
            return
        self._collection.insert_one(item.to_dict())

    def _get_item(self, query: dict):
        return self._collection.find_one(query)

    def _get_item_by_id(self, id: str):
        # log/raise error if doesn't exist
        return self._get_item({"id": id})

    def _get_item_field(self, collection, id, field):
        return self._collection.find_one_by_id(id)

    def _update_item(self, query, item):
        self._collection.update_one(query, {"$set": item})

    def _update_item_by_id(self, id: str, item: dict):
        self._update_item({"id": id}, item)

    def _item_exists(self, id: str) -> bool:
        """Given a query, checks if corresponding object already exists in a given collection"""
        return self._collection.count_documents({"id": id}, limit=1) != 0

    def count(self) -> int:
        return self._collection.count_documents({})
