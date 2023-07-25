from flask import Flask, jsonify, request

import spotifystats.core.database as db

app = Flask(__name__)


# route: /api/v1/top-artists
# method: GET
# parameters
#   - limit: int


@app.route("/api/v1/top-artists", methods=["GET"])
def get_top_artists(limit: int = 50):
    """Get top artists."""
    limit = request.args.get("limit", default=50, type=int)
    artists = db.get_top_artists(limit)
    return jsonify([artist.to_json() for artist in artists])


@app.route("/api/v1/top-tracks", methods=["GET"])
def get_top_tracks(limit: int = 50):
    """Get top tracks."""
    limit = request.args.get("limit", default=50, type=int)
    tracks = db.get_top_tracks(limit)
    return jsonify([track.to_json() for track in tracks])
