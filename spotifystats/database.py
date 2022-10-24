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

    def __add_item(self, document, item):
        # check if collection is valid (assert)
        self.__get_collection().insert_one({"$push": {document: item}})

    def __get_item(self, document, id):
        # log/raise error if doesn't exist
        return self.__get_collection().find_one({document: {"_id": id}})

    def __update_item(self, collection, query, item):
        self.__get_collection().update_one({collection: query}, item)

    def item_exists(self, id, collection):
        """Given an id, checks if corresponding object already exists in a given collection"""
        return self.__get_collection().count_documents({collection: {"_id": id}}, limit=1) != 0 

    def add_track(self, id, name, artists):
        if isinstance(artists, str):
            artists = [artists]

        track = {
            "_id": id,
            "name": name,
            "artists": artists,
            "count": 0,
            "last_listened": 0
        }
        
        if (self.item_exists(id, "tracks")):
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
        self.__update_item("tracks", {"_id": id}, track)

    def add_artist(self, id, name):
        artist = {
            "_id": id,
            "name": name
        }
        
        if (self.item_exists(id, "artists")):
            # log: add_artist
            return

        self.__add_item("artists", artist)

    def create_history(self, timestamp):
        history = {
            "timestamp": timestamp,
        }

        self.__add_item("history", history)

    def add_history(self, timestamp, ids, collection, range):
        # New info to be added
        entry = {
            "$set": {
                "{}.{}".format(collection, range): ids
            }
        }

        self.__update_item("history", {"_id": timestamp}, entry)
