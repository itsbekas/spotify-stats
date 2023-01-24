#!/usr/bin/python

import unittest
from os import environ

from dotenv import load_dotenv
from pymongo import MongoClient

from spotifystats.database import ArtistDatabase

TESTDB = "spotify-stats-test"


class DatabaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()

    @classmethod
    def tearDownClass(cls) -> None:
        client = MongoClient(environ["SPOTIFYSTATS_MONGODB_URI"])
        client.drop_database(TESTDB)


class TestArtists(DatabaseTest):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.db = ArtistDatabase(TESTDB)

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()
