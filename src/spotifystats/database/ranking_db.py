from __future__ import annotations

from typing import TYPE_CHECKING

import spotifystats.database as db

import spotifystats.models.ranking as rnk
import spotifystats.models.artist_ranking as a_rnk
import spotifystats.models.track_ranking as t_rnk


def add_artist_ranking(ranking: a_rnk.ArtistRanking) -> None:
    artists = ranking.get_artists()
    for i, artist in enumerate(artists):
        db_artist = db.get_artist(artist.get_id())
        if db_artist is None:
            db.add_artist(artist)
        else:
            artists[i] = db_artist
    
    ranking.save()

    for artist in ranking.get_artists():
        artist.add_ranking(ranking)
        artist.save()

def add_track_ranking(ranking: t_rnk.TrackRanking) -> None:
    tracks = ranking.get_tracks()
    for i, track in enumerate(tracks):
        db_track = db.get_track(track.get_id())
        if db_track is None:
            db.add_track(track)
        else:
            tracks[i] = db_track

    ranking.save()

    for track in ranking.get_tracks():
        track.add_ranking(ranking)
        track.save()
