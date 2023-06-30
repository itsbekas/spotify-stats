from flask import Flask

# create a flask app
app = Flask(__name__)


# create a basic route
@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/top-artists")
def top_artists():
    return "Top Artists"


@app.route("/top-tracks")
def top_tracks():
    return "Top Tracks"


# run the app
if __name__ == "__main__":
    # run the flask app
    app.run(debug=True)
