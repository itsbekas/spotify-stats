import glob
import json

import spotifystats.database as db
import spotifystats.models.play as pl
from spotifystats.service.spotify_api import SpotifyAPI
from spotifystats.service.spotifystats_service import SpotifyStatsService


def verify_track(response, track, artist):
    if response["track"][0]["name"].lower() != track.lower():
        print(f"Found {response['name']} instead of {track}")
        return False

    if response["track"][0]["artists"][0]["name"].lower() != artist.lower():
        print(f"Found {response['artists'][0]['name']} instead of {artist}")
        return False

    return True


def try_alternatives(api, track, artist):
    track = track.replace("'", "")
    response = api.search_track(track, artist)

    if response["track"] != []:
        return response


def import_track(api, track, artist):
    response = api.search_track(track, artist)

    if response["track"] == []:
        print(f"Could not find {track} by {artist}.")
        response = try_alternatives(api, track, artist)
        if response is None:
            return None

    while not verify_track(response, track, artist):
        response = api.get_next(response)

    return response


def parse_streaming_history(directory: str):
    files = glob.glob(f"{directory}/StreamingHistory*.json")

    results = []
    for file in files:
        with open(file, "r") as f:
            history = json.load(f)
            results.extend(history)

    if not results:
        print("No plays found.")
        return
    else:
        print(f"Found {len(results)} plays.")

    # snake case for compatibility with spotipy
    for result in results:
        result["played_at"] = result.pop("endTime")
        result["ms_played"] = result.pop("msPlayed")

    return results


def get_unique_tracks(history) -> dict:
    unique = {}
    for play in history:
        artist = play["artistName"]
        track = play["trackName"]
        if artist not in unique:
            unique[artist] = {}
        if track not in unique[artist]:
            unique[artist][track] = None
    return unique


def get_tracks_from_history(history):
    api = SpotifyAPI()
    # little hack to connect to the database
    SpotifyStatsService()

    tracks = get_unique_tracks(history)

    unique_count = len([track for artist in tracks for track in tracks[artist]])
    print(f"Found {unique_count} unique tracks")

    count = 0
    for artist in tracks:
        for track in tracks[artist]:
            response = import_track(api, track, artist)
            if response is None:
                raise Exception(f"Could not find track {track} by {artist}")

            tracks[artist][track] = response
            count += 1

    print(f"{count} tracks found.")

    return tracks


def save_streaming_history(results):
    for result in results:
        play = pl.Play.from_spotify_response(result)
        db.add_play(play)


def import_streaming_history(directory: str = "MyData"):
    print("This might take a while...")
    history = parse_streaming_history(directory)[:200]
    if history is None:
        return

    tracks = get_tracks_from_history(history)

    for play in history:
        play["track"] = tracks[play["artistName"]][play["trackName"]]

    save_streaming_history(history)

    print(f"Finished! Imported {len(history)} plays with {len(tracks)} tracks")
