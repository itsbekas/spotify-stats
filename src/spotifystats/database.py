from pymongo import MongoClient
from os import environ
from enum import Enum

class Collection(Enum):
    ARTISTS = "artists"
    TRACKS = "tracks"
    RANKINGS = "rankings"

def _valid_collection(collection):
    return collection in [collection.value for collection in Collection]

class Database:
    
    def __init__(self, dbname):
        #logger.info("Initializing Database")
        client = MongoClient(environ["SPOTIFYSTATS_MONGODB_URI"])
        self._db = client[dbname]

    def _get_collection(self, collection):
        return self._db[collection]

    def _add_item(self, collection, item):
        # check if collection is valid (assert)
        self._get_collection(collection).insert_one(item)

    def _get_item(self, collection, query):
        return self._get_collection(collection).find_one(query)

    def _get_item_by_id(self, collection, id):
        # log/raise error if doesn't exist
        return self._get_item(collection, {"id": id})

    def _update_item(self, collection, id, item):
        self._get_collection(collection).update_one({"id": id}, {"$set": item})

    def _item_exists(self, id, collection):
        """Given a query, checks if corresponding object already exists in a given collection"""
        return self._get_collection(collection).count_documents({"id": id}, limit=1) != 0

    def _get_item_count(self, collection):
        return self._get_collection(collection).count_documents({})

    def get_artist_count(self):
        return self._get_item_count(Collection.ARTISTS.value)

    def get_track_count(self):
        return self._get_item_count(Collection.TRACKS.value)
    
    def get_ranking_count(self):
        return self._get_item_count(Collection.RANKINGS.value)

    def get_artist_listened_count(self, id):
        return self._get_item_by_id(Collection.ARTISTS.value, id)["count"]

    def get_track_listened_count(self, id):
        return self._get_item_by_id(Collection.TRACKS.value, id)["count"]

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
        
        if (self._item_exists(id, Collection.TRACKS.value)):
            # log: Database.add_track: Track {id} already exists. Skipping.
            return

        self._add_item(Collection.TRACKS.value, track)
    
    def update_track(self, id, timestamp):
        count = self._get_item_by_id(Collection.TRACKS.value, id)["count"] + 1
        update = {
            "count": count,
            "last_listened": timestamp
        }

        self._update_item(Collection.TRACKS.value, id, update)

    def add_artist(self, id, name):
        artist = {
            "id": id,
            "name": name,
            "count": 0,
            "last_listened": 0
        }
        
        if (self._item_exists(id, Collection.ARTISTS.value)):
            # log: add_artist
            return

        self._add_item(Collection.ARTISTS.value, artist)

    def update_artist(self, id, timestamp):
        count = self._get_item_by_id(Collection.ARTISTS.value, id)["count"] + 1
        update = {
            "count": count,
            "last_listened": timestamp
        }
        self._update_item(Collection.ARTISTS.value, id, update)

    def create_ranking(self, timestamp):
        ranking = {
            "id": timestamp,
        }
        if (self._item_exists(timestamp, Collection.RANKINGS.value)):
            return

        self._add_item(Collection.RANKINGS.value, ranking)

    def add_ranking(self, timestamp, ids, collection, range):
        filter = { "id": timestamp }
        ranking = { f"{collection}-{range}": ids }

        self._update_item(Collection.RANKINGS.value, filter, ranking)

    def get_ranking(self, timestamp, range):
        return self._get_item(Collection.RANKINGS.value, {"id": timestamp })
