#!/usr/bin/python

import unittest
from spotifystats.database.base import Database, MongoClient, environ
from spotifystats.model import Artist
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

class TestDatabase(DatabaseTest):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()

    def tearDown(cls):
        client = MongoClient(environ["SPOTIFYSTATS_MONGODB_URI"])
        client[TESTDB]["A"].drop()
    
    def testAddItem(cls):
        cls.db._add_item("A", {"id": 1})
        cls.assertEqual(cls.db._get_item_count("A"), 1)

    def testAddField(cls):
        cls.db._add_item("A", {"id": 1})
        cls.db._update_item_by_id("A", 1, {"field": "value"})
        cls.assertEqual(cls.db._get_item_by_id("A", 1)["field"], "value")

class TestArtists(DatabaseTest):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.artist1 = Artist("id1", "Name" 
        cls.artist2 = {"id": '2', "name": 'B'}
        cls.timestamp = 1

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()

    def tearDown(cls):
        client = MongoClient(environ["SPOTIFYSTATS_MONGODB_URI"])
        client[TESTDB][Collection.ARTISTS.value].drop()

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
        cls.db.update_artist(cls.artist1["id"], cls.timestamp)
        cls.assertEqual(cls.db.get_artist_listened_count(cls.artist1["id"]), 1)
        cls.assertEqual(cls.db.get_artist_last_listened(cls.artist1["id"]), cls.timestamp)

class TestTracks(DatabaseTest):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.track1 = {"id": '1', "name": 'A', "artists": ['11']}
        cls.track2 = {"id": '2', "name": 'B', "artists": ['22']}
        cls.timestamp = 1

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()

    def tearDown(cls):
        client = MongoClient(environ["SPOTIFYSTATS_MONGODB_URI"])
        client[TESTDB][Collection.TRACKS.value].drop()

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
        cls.db.update_track(cls.track1["id"], cls.timestamp)
        cls.assertEqual(cls.db.get_track_listened_count(cls.track1["id"]), 1)
        cls.assertEqual(cls.db.get_track_last_listened(cls.track1["id"]), cls.timestamp)

class TestRankings(DatabaseTest):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.ranking1 = {
            
        }

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()

    def tearDown(cls):
        client = MongoClient(environ["SPOTIFYSTATS_MONGODB_URI"])
        client[TESTDB][Collection.RANKINGS.value].drop()

    def test_createRanking(cls):
        cls.db.create_ranking(1)
        cls.assertEqual(cls.db.get_ranking_count(), 1)

    def test_createTwoRankings(cls):
        cls.db.create_ranking(1)
        cls.db.create_ranking(2)
        cls.assertEqual(cls.db.get_ranking_count(), 2)

    def test_createDuplicateRanking(cls):
        cls.db.create_ranking(1)
        cls.db.create_ranking(2)
        cls.db.create_ranking(1)
        cls.assertEqual(cls.db.get_ranking_count(), 2)

    def test_addRanking(cls):
        cls.db.create_ranking(1)
        artists = ["1", "2", "3"]
        cls.db.add_ranking(1, artists, Collection.ARTISTS.value, "short_term")
        cls.assertEqual(cls.db._get_item_by_id(Collection.RANKINGS.value, 1)[Collection.ARTISTS.value+"-short_term"], artists)

if __name__ == "__main__":
    unittest.main()
