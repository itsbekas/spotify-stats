#!/usr/bin/python

import unittest
from database import Database

class DatabaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.db = Database("spotify-stats-test")
    
    def tearDownClass(cls) -> None:
        cls.db.drop_database("spotify-stats-test")

class TestArtist(DatabaseTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        artist1 = {
            "_id": "6398b6297334cb9687e1616a",
            "id": '2YZyLoL8N0Wb9xBt1NhZWg',
            "name": 'Kendrick Lamar',
            "count": 0,
            "last_listened": 0
        }
        artist2 = {
            "_id": "6398b6297334cb9687e1614e",
            "id": '4MvZhE1iuzttcoyepkpfdF',
            "name": 'ThxSoMch',
            "count": 0,
            "last_listened": 0
        }
        cls.db.add_artist(artist1["id"], artist1["name"])
        cls.db.add_artists(artist2["id"], artist2["name"])

    @classmethod
    def tearDownClass(cls):
        pass

class TestDuplicateArtist():
    pass

class TestDuplicateTrack(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()