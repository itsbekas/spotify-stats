#!/usr/bin/python

import unittest
from spotifystats.database import Database, MongoClient, environ
from spotifystats.util import load_dotenv

TESTDB = "spotify-stats-test"

class DatabaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.db = Database(TESTDB)
    
    @classmethod
    def tearDownClass(cls) -> None:
        client = MongoClient(environ["SPOTIFYSTATS_MONGODB_URI"])
        client.drop_database(TESTDB)

class TestArtists(DatabaseTest):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.artist1 = {"id": '2YZyLoL8N0Wb9xBt1NhZWg', "name": 'Kendrick Lamar'}
        cls.artist2 = {"id": '4MvZhE1iuzttcoyepkpfdF', "name": 'ThxSoMch'}

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()

    def tearDown(cls):
        client = MongoClient(environ["SPOTIFYSTATS_MONGODB_URI"])
        client[TESTDB]["artists"].drop()

    def test_addArtist(cls):
        cls.db.add_artist(cls.artist1["id"], cls.artist1["name"])
        cls.assertEqual(cls.db.get_artist_count(), 1)
    
    def test_addTwoArtists(cls):
        cls.db.add_artist(cls.artist1["id"], cls.artist1["name"])
        cls.db.add_artist(cls.artist2["id"], cls.artist2["name"])
        cls.assertEqual(cls.db.get_artist_count(), 2)
    
    def test_addDuplicateArtist(cls):
        cls.db.add_artist(cls.artist1["id"], cls.artist1["name"])
        cls.db.add_artist(cls.artist2["id"], cls.artist2["name"])
        cls.db.add_artist(cls.artist1["id"], cls.artist1["name"])
        cls.assertEqual(cls.db.get_artist_count(), 2)

    def test_updateArtist(cls):
        cls.db.add_artist(cls.artist1["id"], cls.artist1["name"])
        cls.db.update_artist(cls.artist1["id"], 100)
        cls.assertEqual(cls.db.get_listened_count(cls.artist1["id"], "artists"), 1)

class TestTracks(DatabaseTest):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.track1 = {"id": '5Gt9bxniM1SxN61yRzRhXL', "name": 'United In Grief', "artists": [ '2YZyLoL8N0Wb9xBt1NhZWg' ]}
        cls.track2 = {"id": '1EzhAHxkdYfsoJjnt2usC2', "name": 'Bitty (1400/999)', "artists": [ '3HMU8O8ZHfiLP83JFsRfo5' ]}

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()

    def tearDown(cls):
        client = MongoClient(environ["SPOTIFYSTATS_MONGODB_URI"])
        client[TESTDB]["tracks"].drop()

    def test_addTrack(cls):
        cls.db.add_track(cls.track1["id"], cls.track1["name"], cls.track1["artists"])
        cls.assertEqual(cls.db.get_track_count(), 1)

    def test_addTwoTracks(cls):
        cls.db.add_track(cls.track1["id"], cls.track1["name"], cls.track1["artists"])
        cls.db.add_track(cls.track2["id"], cls.track2["name"], cls.track2["artists"])
        cls.assertEqual(cls.db.get_track_count(), 2)

    def test_addDuplicateTrack(cls):
        cls.db.add_track(cls.track1["id"], cls.track1["name"], cls.track1["artists"])
        cls.db.add_track(cls.track2["id"], cls.track2["name"], cls.track2["artists"])
        cls.db.add_track(cls.track1["id"], cls.track1["name"], cls.track1["artists"])
        cls.assertEqual(cls.db.get_track_count(), 2)

    def test_updateTrack(cls):
        cls.db.add_track(cls.track1["id"], cls.track1["name"], cls.track1["artists"])
        cls.db.update_track(cls.track1["id"], 100)
        cls.assertEqual(cls.db.get_listened_count(cls.track1["id"], "tracks"), 1)

class TestRankings(DatabaseTest):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()

    def tearDown(cls):
        client = MongoClient(environ["SPOTIFYSTATS_MONGODB_URI"])
        client[TESTDB]["rankings"].drop()

    def test_addRanking(cls):
        cls.db

if __name__ == "__main__":
    unittest.main()
