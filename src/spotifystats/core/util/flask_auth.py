from multiprocessing import Process, Queue
from time import sleep

from flask import Flask, request


def run_auth_flask(authorization_url: str, queue):
    app = Flask(__name__)

    @app.route("/")
    def index():
        return f'<a href="{authorization_url}">Authenticate with Spotify</a>'

    @app.route("/callback", methods=["GET"])
    def callback():
        # Add the URL to the queue
        queue.put(request.url)
        return "Authentication received"

    app.run(host="0.0.0.0", port=5000)


def wait_for_auth(authorization_url: str):
    queue = Queue()
    flask_process = Process(target=run_auth_flask, args=(authorization_url, queue))
    flask_process.start()

    # Monitor the queue for signals
    while True:
        if not queue.empty():
            flask_process.terminate()
            return queue.get()
        sleep(1)
