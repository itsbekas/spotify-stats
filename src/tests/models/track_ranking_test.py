import spotifystats.models.track as trk
import spotifystats.models.track_ranking as t_rnk


def test_create_track_ranking_from_response(
    ranking_tracks_long, top_tracks_long, timestampL
):
    ranking = t_rnk.TrackRanking.from_spotify_response(ranking_tracks_long)

    tracks = []
    for track in top_tracks_long:
        tracks.append(trk.Track.from_spotify_response(track))

    assert isinstance(ranking, t_rnk.TrackRanking)
    assert ranking.get_timestamp() == timestampL
    assert ranking.get_time_range() == "long_term"
    assert len(ranking.get_tracks()) == 50

    tracks = ranking.get_tracks()

    for i in range(50):
        assert tracks[i].get_id() == top_tracks_long[i]["id"]
