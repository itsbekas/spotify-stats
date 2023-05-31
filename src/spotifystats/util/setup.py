from os import environ

import spotifystats.database as db


def setup() -> None:
    mongodb_name = environ.get("SPOTIFYSTATS_MONGODB_DB_NAME")
    if mongodb_name is None:
        raise ValueError("SPOTIFYSTATS_MONGODB_DB_NAME is not set")

    mongodb_uri = environ.get("SPOTIFYSTATS_MONGODB_URI")
    if mongodb_uri is None:
        raise ValueError("SPOTIFYSTATS_MONGODB_URI is not set")

    db.connect(
        name=mongodb_name,
        host=mongodb_uri,
        uuidRepresentation="standard",
    )
