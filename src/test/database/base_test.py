import pytest
from dotenv import load_dotenv
from mongomock import MongoClient

from spotifystats.repositories.base_repository import Database
from spotifystats.model.item import Item


@pytest.fixture()
def db():
    load_dotenv()
    db = Database("test_database", "test_collection")
    client: MongoClient = MongoClient()
    db._db = client["test_database"]
    db._collection = db._db["test_collection"]
    yield db

    db._collection.drop()


def test_add_item(db):
    item = Item({"id": "123", "name": "test"})
    db._add_item(item)
    assert db.count() == 1
    db._add_item(item)
    assert db.count() == 1


def test_get_item(db):
    item = Item({"id": "123", "name": "test"})
    db._add_item(item)
    result = db._get_item({"id": "123"})
    assert result == item


def test_get_item_by_id(db):
    item = Item({"id": "123", "name": "test"})
    db._add_item(item)
    result = db._get_item_by_id("123")
    assert result == item


def test_update_item(db):
    item = Item({"id": "123", "name": "test"})
    db._add_item(item)
    db._update_item({"id": "123"}, {"name": "updated"})
    result = db._get_item_by_id("123")
    assert result == {"id": "123", "name": "updated"}


def test_update_item_by_id(db):
    item = Item({"id": "123", "name": "test"})
    db._add_item(item)
    db._update_item_by_id("123", {"name": "updated"})
    result = db._get_item_by_id("123")
    assert result == {"id": "123", "name": "updated"}


def test_item_exists(db):
    item = Item({"id": "123", "name": "test"})
    db._add_item(item)
    assert db._item_exists("123") == True
    assert db._item_exists("invalid") == False


def test_count(db):
    item1 = Item({"id": "123", "name": "test1"})
    item2 = Item({"id": "456", "name": "test2"})
    db._add_item(item1)
    db._add_item(item2)
    assert db.count() == 2
