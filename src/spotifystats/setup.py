from pymongo import MongoClient
from os import environ
from dotenv import load_dotenv

from spotifystats.repositories.base_repository import Collection


def main():
    load_dotenv()
    client = MongoClient(environ["SPOTIFYSTATS_MONGODB_URI"])
    db = client["spotify-stats"]
    db["common"].insert_one({"id": Collection.COMMON.value, "timestamp": 0})
