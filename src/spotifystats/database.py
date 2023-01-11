from pymongo import MongoClient
from os import environ
from enum import Enum

class Collection(Enum):
    ARTISTS = "artists"
    TRACKS = "tracks"
    RANKINGS = "rankings"
    COMMON = "common"
    HISTORY = "history"

def _valid_collection(collection):
    return collection in [collection.value for collection in Collection]

class Database:
    
    def __init__(self, dbname):
        #logger.info("Initializing Database")
        client = MongoClient(environ["SPOTIFYSTATS_MONGODB_URI"])
        self._db = client[dbname]
        self._add_item(Collection.COMMON.value, {"id": Collection.COMMON.value})
        #self.set_timestamp(0)

    def _get_collection(self, collection):
        return self._db[collection]

    def _add_item(self, collection, item):
        if self._get_item_by_id(collection, item["id"]) != None:
            return
        self._get_collection(collection).insert_one(item)

    def _get_item(self, collection, query):
        return self._get_collection(collection).find_one(query)

    def _get_item_by_id(self, collection, id):
        # log/raise error if doesn't exist
        return self._get_item(collection, {"id": id})

    def _get_item_field(self, collection, id, field):
        return self._get_collection(collection).find_one_by_id(id)

    def _update_item(self, collection, query, item):
        self._get_collection(collection).update_one(query, {"$set": item})

    def _update_item_by_id(self, collection, id, item):
        self._update_item(collection, {"id": id}, item)

    def _item_exists(self, collection, id):
        """Given a query, checks if corresponding object already exists in a given collection"""
        return self._get_collection(collection).count_documents({"id": id}, limit=1) != 0

    def _get_item_count(self, collection):
        return self._get_collection(collection).count_documents({})

    def get_timestamp(self):
        return self._get_item_by_id(Collection.COMMON.value, Collection.COMMON.value)["timestamp"]

    def set_timestamp(self, timestamp):
        return self._update_item_by_id(Collection.COMMON.value, Collection.COMMON.value, {"timestamp": timestamp})

    def get_artist_count(self):
        return self._get_item_count(Collection.ARTISTS.value)

    def get_track_count(self):
        return self._get_item_count(Collection.TRACKS.value)
    
    def get_ranking_count(self):
        return self._get_item_count(Collection.RANKINGS.value)

    def get_artist_listened_count(self, id):
        return self._get_item_by_id(Collection.ARTISTS.value, id)["count"]

    def get_artist_last_listened(self, id):
        return self._get_item_by_id(Collection.ARTISTS.value, id)["last_listened"]

    def get_track_listened_count(self, id):
        return self._get_item_by_id(Collection.TRACKS.value, id)["count"]

    def get_track_last_listened(self, id):
        return self._get_item_by_id(Collection.TRACKS.value, id)["last_listened"]

    def add_track(self, id, name, artists):
        if isinstance(artists, str):
            artists = [artists]

        track = {
            "id": id,
            "name": name,
            "artists": artists,
            "count": 0,
            "last_listened": 0
        }

        self._add_item(Collection.TRACKS.value, track)
    
    def update_track(self, id, timestamp):
        if (self.get_track_last_listened(id) >= timestamp):
            return
        
        count = self._get_item_by_id(Collection.TRACKS.value, id)["count"] + 1
        update = {
            "count": count,
            "last_listened": timestamp
        }

        self._update_item_by_id(Collection.TRACKS.value, id, update)

    def add_artist(self, id, name):
        artist = {
            "id": id,
            "name": name,
            "count": 0,
            "last_listened": 0
        }

        self._add_item(Collection.ARTISTS.value, artist)

    def update_artist(self, id: str, timestamp: int) -> None:
        if (self.get_artist_last_listened(id) >= timestamp):
            return

        count = self._get_item_by_id(Collection.ARTISTS.value, id)["count"] + 1
        update = {
            "count": count,
            "last_listened": timestamp
        }
        self._update_item_by_id(Collection.ARTISTS.value, id, update)

    def create_ranking(self, timestamp: int):
        ranking = {
            "id": timestamp,
        }

        self._add_item(Collection.RANKINGS.value, ranking)

    def add_ranking(self, timestamp, ids, collection, range):
        ranking = { f"{collection}-{range}": ids }

        self._update_item_by_id(Collection.RANKINGS.value, timestamp, ranking)

    def get_ranking(self, timestamp, range):
        return self._get_item(Collection.RANKINGS.value, timestamp)

    def add_history(self, history, timestamp):
        db_history = {
            "id": timestamp,
            "history": history
        }

        self._add_item(Collection.HISTORY.value, db_history)
