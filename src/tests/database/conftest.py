from os import environ

import pytest
from dotenv import load_dotenv
from mongoengine.connection import get_db

import spotifystats.database as db


@pytest.fixture(scope="package")
def mongo():
    load_dotenv()

    mongodb_name = environ.get("SPOTIFYSTATS_MONGODB_DB_NAME")
    if mongodb_name is None:
        raise ValueError("SPOTIFYSTATS_MONGODB_DB_NAME is not set")

    mongodb_uri = environ.get("SPOTIFYSTATS_MONGODB_URI")
    if mongodb_uri is None:
        raise ValueError("SPOTIFYSTATS_MONGODB_URI is not set")

    db.connect(
        db=mongodb_name + "-test",
        host=mongodb_uri,
        uuidRepresentation="standard",
    )
    yield
    db.disconnect()


# create a fixture to clear the database before each test
@pytest.fixture(autouse=True)
def clear_db(mongo):
    mongodb_name = environ.get("SPOTIFYSTATS_MONGODB_DB_NAME")
    if mongodb_name is None:
        raise ValueError("SPOTIFYSTATS_MONGODB_DB_NAME is not set")
    # clear the database using mongoengine
    get_db().connection.drop_database(mongodb_name + "-test")
    yield
