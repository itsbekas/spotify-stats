from pymongo import MongoClient
from log import logger
from os import environ

collections = ["spotifystats"]
documents = ["artists", "tracks", "song-count", "history"]

def _valid_collection(collection):
    return collection in collections

def _valid_document(document):
    return document in documents

class Database:
    
    def __init__(self):
        #logger.info("Initializing Database")
        client = MongoClient(environ["SPOTIFYSTATS_MONGODB_URI"])
        self.__db = client["spotify-stats"]

    def __get_collection(self):
        return self.__db["spotifystats"]

    def __add_item(self, document, item, filter={}):
        # check if collection is valid (assert)
        self.__get_collection().update_one(filter, {"$push": {document: item}}, upsert=True)

    def __get_item(self, document, id):
        # log/raise error if doesn't exist
        return self.__get_collection().find_one({document: {"id": id}})

    def __update_item(self, collection, query, item):
        self.__get_collection().update_one({collection: query}, item)

    def __item_exists(self, id, collection):
        """Given an id, checks if corresponding object already exists in a given collection"""
        return self.__get_collection().count_documents({collection: {"ids": {"$in": id}}}, limit=1) != 0 

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
        
        if (self.__item_exists(id, "tracks")):
            # log: Database.add_track: Track {id} already exists. Skipping.
            return

        self.__add_item("tracks", track)
    
    def update_track(self, id, timestamp):
        count = self.__get_item("tracks", id)["count"] + 1
        track = {
            "$set": {
                "count": count,
                "last_listened": timestamp
            }
        }
        self.__update_item("tracks", {"id": id}, track)

    def add_artist(self, id, name):
        artist = {
            "id": id,
            "name": name
        }
        
        if (self.__item_exists(id, "artists")):
            # log: add_artist
            return

        self.__add_item("artists", artist)

    def create_ranking(self, timestamp):
        ranking = {
            "timestamp": timestamp,
        }

        self.__add_item("ranking", ranking)

    def add_ranking(self, timestamp, ids, collection, range):
        filter = {
            "timestamp": timestamp
        }

        ranking = {
            f"{collection}-{range}": ids + ["bruh"]
        }

        self.__add_item("ranking", ranking)
