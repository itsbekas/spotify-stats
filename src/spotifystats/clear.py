from os import environ

from dotenv import load_dotenv
from pymongo import MongoClient


def main():
    load_dotenv()
    client = MongoClient(environ["SPOTIFYSTATS_MONGODB_URI"])
    client.drop_database("spotify-stats")
