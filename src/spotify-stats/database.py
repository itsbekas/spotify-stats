from pymongo import MongoClient

class Database:
    
    def __init__(self):
        client = MongoClient("mongodb://localhost:27017/")
        db = client["spotify-stats"]
        self.__artists = db["artists"]
        self.__tracks = db["tracks"]
        self.__songcount = db["song-count"]
        self.__history = db["history"]

    def add_track(self, id, name, artists):
        if isinstance(artists, str):
            artists = [artists]

        track = {
            "_id": id,
            "name": name,
            "artists": artists,
        }
        
        if (track):
            pass

        self.__tracks.insert_one(track)

    def add_artist(self, id, name):
        artist = {
            "_id": id,
            "name": name
        }
        self.__artists.insert_one(artist)
    