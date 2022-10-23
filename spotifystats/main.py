#!/usr/bin/python

from stats import SpotifyStats
from log import init_logger, logger

if __name__ == "__main__":
    # init_logger()
    # logger.warning("boas")
    stats = SpotifyStats()
    stats.update()
