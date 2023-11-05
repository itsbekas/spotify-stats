import threading

from flask import Flask

callback_reached = False


def wait_for_auth(authorization_url: str):
    callback_reached = False

    app = Flask(__name__)

    @app.route("/")
    def index():
        return f'<a href="{authorization_url}">Authenticate with Spotify</a>'

    @app.route("/callback", methods=["GET"])
    def callback():
        global callback_reached
        callback_reached = True
        return "Authentication received"

    flask_thread = threading.Thread(target=app.run)
    flask_thread.start()

    while not callback_reached:
        pass

    flask_thread.join()

    print("Authentication received")
