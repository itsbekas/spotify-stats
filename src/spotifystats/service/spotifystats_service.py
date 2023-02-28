class SpotifyStatsService:
    def get_average_duration(self):
        tracks = db.get_all_tracks()
        total_duration = sum(track.duration for track in tracks)
        average_duration = total_duration / len(tracks)
        return average_duration
