from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/api/v1/top-artists", methods=["GET"])
def get_top_artists():
    """Get top artists."""
    return jsonify({"top_artists": []})
