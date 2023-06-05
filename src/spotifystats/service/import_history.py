import glob
import json

import spotifystats.database as db
import spotifystats.models.play as pl
from spotifystats.service.spotify_api import SpotifyAPI
from spotifystats.service.spotifystats_service import SpotifyStatsService


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


def get_tracks_from_history(history):
    api = SpotifyAPI()
    # little hack to connect to the database
    SpotifyStatsService()

    # count tracks to be found
    test = []
    for play in history:
        id = play["artistName"] + play["trackName"]
        if id not in test:
            test.append(id)
    print(f"{len(test)} tracks to be found.")

    # do something
    tracks = {}
    count = 0
    for play in history:
        artist = play["artistName"]
        track = play["trackName"]
        if artist not in tracks:
            tracks[artist] = {}
        if track not in tracks[artist]:
            tracks[artist][track] = api.find_track(track, artist)
            if count == 44:
                print(artist, track)
            count += 1
            if count % 100 == 0:
                print(f"{count} tracks found.")

    print(f"{count} tracks found.")

    return tracks


def save_streaming_history(results):
    for result in results:
        play = pl.Play.from_spotify_response(result)
        db.add_play(play)


def import_streaming_history(directory: str = "MyData"):
    print("This might take a while...")
    history = parse_streaming_history(directory)
    if history is None:
        return

    tracks = get_tracks_from_history(history)

    for play in history:
        play["track"] = tracks[play["artistName"]][play["trackName"]]

    save_streaming_history(history)

    print(f"Finished! Imported {len(history)} plays with {len(tracks)} tracks.")
