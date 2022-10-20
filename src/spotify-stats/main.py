#!/usr/bin/python

from src.stats import SpotifyStats
import src.common as common

if __name__ == "__main__":
    common.get_logger()
    stats = SpotifyStats()
    stats.update()