#!/usr/bin/python

from stats import SpotifyStats
from util import init

def main():
    init()
    stats = SpotifyStats()
    stats.update()
