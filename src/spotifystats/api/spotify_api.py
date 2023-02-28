class SpotifyAPI:
    # ... (other methods)

    def search_track(self, query):
        result = self.sp.search(q=query, type="track")
        tracks = [
            Track.from_spotify_response(item) for item in result["tracks"]["items"]
        ]
        # store the tracks in the database using the data access layer
        db.add_tracks(tracks)
        return tracks
