#!/usr/bin/python

from unittest import TestCase, TestFixture

class DatabaseTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()

class TestArtist(DatabaseTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls._artist1 = {
            "_id": "6398b6297334cb9687e1616a",
            "id": '2YZyLoL8N0Wb9xBt1NhZWg',
            "name": 'Kendrick Lamar',
            "count": 0,
            "last_listened": 0
        }
        cls.artist2 = {
            "_id": "6398b6297334cb9687e1614e",
            "id": '4MvZhE1iuzttcoyepkpfdF',
            "name": 'ThxSoMch',
            "count": 0,
            "last_listened": 0
        }
    @classmethod
    def tearDownClass(cls):
        cls.

class TestDuplicateArtist()

class TestDuplicateTrack(TestCase):
