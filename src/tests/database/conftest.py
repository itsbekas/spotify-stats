from os import environ

import pytest
from dotenv import load_dotenv

import spotifystats.database as db
import spotifystats.models.album as alb
import spotifystats.models.artist as art
import spotifystats.models.artist_ranking as a_rnk
import spotifystats.models.play as play
import spotifystats.models.track as trk
import spotifystats.models.track_ranking as t_rnk


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
    yield
    alb.Album.drop_collection()
    art.Artist.drop_collection()
    a_rnk.ArtistRanking.drop_collection()
    play.Play.drop_collection()
    trk.Track.drop_collection()
    t_rnk.TrackRanking.drop_collection()
