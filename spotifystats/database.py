from pymongo import MongoClient
from log import logger

collections = ["artists", "tracks", "song-count", "history"]

class Database:
    
    def __init__(self):
        #logger.info("Initializing Database")
        client = MongoClient("mongodb://localhost:27017/")
        self.__db = client["spotify-stats"]

    def get_collection(self, collection):
        if collection not in collections:
            raise ValueError("Invalid Collection: {}".format(collection))
        return self.__db[collection]

    def get_item(self, collection, id):
        # log/raise error if doesn't exist
        
        a = self.get_collection(collection).find_one("_id", id)
        print(a)

    def item_exists(self, id, collection):
        """Given an id, checks if corresponding object already exists in a given collection"""
        return self.get_collection(collection).count_documents({"_id": id}, limit=1) != 0 

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

        self.get_collection("tracks").insert_one(track)
    
    def update_track(self, id, timestamp):
        count = self.get_item("tracks", id)["count"] + 1
        track = {
            "$set": {
                "count": count,
                "last_listened": timestamp
            }
        }

    def add_artist(self, id, name):
        artist = {
            "_id": id,
            "name": name
        }
        
        if (self.item_exists(id, "artists")):
            # log: add_artist
            return

        self.get_collection("artists").insert_one(artist)

    def create_history(self, timestamp):
        history = {
            "_id": timestamp,
        }

        self.get_collection("history").insert_one(history)

    def add_history(self, timestamp, ids, collection, range):
        # To find the existing record
        query = {
            "_id": timestamp
        }
        # New info to be added
        entry = {
            "$set": {
                "{}.{}".format(collection, range): ids
            }
        }

        self.get_collection("history").update_one({"_id"}, entry)
    