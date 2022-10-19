#!/usr/bin/python
from common import SpotifyStats
from common import __extract_track

if __name__ == "__main__":
    stats = SpotifyStats()
    stats.update()
    __extract_track({"id":"boas", "name":"skrr", "artists":["yo", "ya"]})