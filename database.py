from pymongo import MongoClient

class Database:
    
    def __init__(self):
        __client = MongoClient("mongodb://localhost:27017/")

    def get_client(self):
        return self.__client
    