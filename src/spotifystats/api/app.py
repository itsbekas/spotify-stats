from flask import Flask, jsonify

import spotifystats.core.database as db

app = Flask(__name__)


@app.route("/api/v1/top-artists", methods=["GET"])
def get_top_artists():
    """Get top artists."""
    artists = db.get_top_artists()
    return jsonify([artist.to_json() for artist in artists])


@app.route("/api/v1/top-tracks", methods=["GET"])
def get_top_tracks():
    """Get top tracks."""
    tracks = db.get_top_tracks()
    return jsonify([track.to_json() for track in tracks])
