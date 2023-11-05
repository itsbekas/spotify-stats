from os import environ

from dotenv import load_dotenv

import spotifystats.core.database as db


def setup() -> None:
    load_dotenv(".env")

    mongodb_user = environ.get("SPOTIFYSTATS_MONGODB_USER")
    if mongodb_user is None:
        raise ValueError("SPOTIFYSTATS_MONGODB_USER is not set")

    mongodb_password = environ.get("SPOTIFYSTATS_MONGODB_PASSWORD")
    if mongodb_password is None:
        raise ValueError("SPOTIFYSTATS_MONGODB_PASSWORD is not set")

    mongodb_host = environ.get("SPOTIFYSTATS_MONGODB_HOST")
    if mongodb_host is None:
        raise ValueError("SPOTIFYSTATS_MONGODB_HOST is not set")

    mongodb_port = environ.get("SPOTIFYSTATS_MONGODB_PORT")
    if mongodb_port is None:
        raise ValueError("SPOTIFYSTATS_MONGODB_PORT is not set")

    mongodb_name = environ.get("SPOTIFYSTATS_MONGODB_DB_NAME")
    if mongodb_name is None:
        raise ValueError("SPOTIFYSTATS_MONGODB_DB_NAME is not set")

    mongodb_login = f"{mongodb_user}:{mongodb_password}"
    mongodb_host = f"{mongodb_host}:{mongodb_port}"

    mongodb_uri = f"mongodb://{mongodb_login}@{mongodb_host}/{mongodb_name}"

    db.connect(
        name=mongodb_name,
        host=mongodb_uri,
        uuidRepresentation="standard",
    )
