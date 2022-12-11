#!/usr/bin/python

from stats import SpotifyStats
from util import init

if __name__ == "__main__":
    init()
    stats = SpotifyStats()
    stats.update()
