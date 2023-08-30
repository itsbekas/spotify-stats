from datetime import datetime

from flask import Flask, jsonify, request
from flask_cors import CORS

import spotifystats.core.database as db

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = True


@app.route("/api/v1/top-artists", methods=["GET"])
def get_top_artists():
    """Get top artists."""
    limit = request.args.get("limit", default=50, type=int)
    artists = db.get_top_artists(limit)
    return jsonify([artist.to_json() for artist in artists])


@app.route("/api/v1/top-tracks", methods=["GET"])
def get_top_tracks():
    """Get top tracks."""
    limit = request.args.get("limit", default=50, type=int)
    tracks = db.get_top_tracks(limit)
    return jsonify([track.to_json() for track in tracks])


@app.route("/api/v1/plays", methods=["GET"])
def get_plays():
    """Get plays."""
    start_date_str = request.args.get("start_date", default="1970-01-01", type=str)
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date_str = request.args.get("end_date", default="2070-01-01", type=str)
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    limit = request.args.get("limit", default=50, type=int)
    plays = db.get_plays_in_range(start_date, end_date, limit)
    return jsonify([play.to_json() for play in plays])
