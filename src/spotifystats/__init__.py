#!/usr/bin/python

from spotifystats.service.stats import SpotifyStats
from spotifystats.util import init

def main():
    init()
    stats = SpotifyStats()
    stats.update()
