import glob
import json

import spotifystats.core.database as db
import spotifystats.core.models.play as pl
from spotifystats.core.service.spotify_api import SpotifyAPI
from spotifystats.core.service.spotifystats_service import SpotifyStatsService


def parse_streaming_history(history):
    parsed_history = []
    for play in history:
        track_uri = play["spotify_track_uri"]
        # Podcast episodes don't have a track uri
        if track_uri is None:
            continue
        parsed_history.append(
            {
                "track_id": track_uri.split(":")[-1],
                "played_at": play["ts"],
            }
        )

    return parsed_history


def get_streaming_history(directory: str):
    files = glob.glob(f"{directory}/Streaming_History_Audio_*.json")

    sorted_files = sorted(files, key=lambda x: int(x.split("_")[-1].split(".")[0]))

    history = []
    for file in sorted_files:
        with open(file, "r") as f:
            _history = json.load(f)
            history.extend(_history)

    if not history:
        print("No plays found.")
        return []
    else:
        print(f"Found {len(history)} plays.")

    return parse_streaming_history(history)


def get_unique_tracks(history):
    return list(set([play["track_id"] for play in history]))


def get_tracks_from_history(history):
    api = SpotifyAPI()
    # little hack to connect to the database
    SpotifyStatsService()

    track_ids = get_unique_tracks(history)

    print(f"Found {len(track_ids)} unique tracks")

    track_count = len(track_ids)

    # get batches of 50 from track_ids
    track_ids = [track_ids[i : i + 50] for i in range(0, len(track_ids), 50)]  # noqa

    tracks = {}
    for batch in track_ids:
        response = api.get_tracks_by_ids(batch)

        for index, track in enumerate(response):
            # Use request's id to ignore track relinking:
            # https://developer.spotify.com/documentation/web-api/concepts/track-relinking
            tracks[batch[index]] = track

        print(f"\rRetrieved {len(tracks.keys())}/{track_count} tracks", end="")

    print(f"\rRetrieved {len(tracks.keys())} tracks.{' '*20}")

    return tracks


def save_streaming_history(history, tracks):
    print_counter = len(history) // 100

    for count, _play in enumerate(history):
        play = pl.Play.from_spotify_response(
            {"played_at": _play["played_at"], "track": tracks[_play["track_id"]]}
        )
        db.add_play(play)

        if count % print_counter == 0:
            print(f"\rSaved {int(count/len(history)*100)}% of the plays", end="")

    print(f"\rSaved {len(history)} plays.{' '*20}")


def import_streaming_history(directory: str = "MyData"):
    print("This might take a while...")
    history = get_streaming_history(directory)
    if history is None:
        return

    tracks = get_tracks_from_history(history)

    save_streaming_history(history, tracks)

    print(f"Finished! Imported {len(history)} plays with {len(tracks)} tracks")
