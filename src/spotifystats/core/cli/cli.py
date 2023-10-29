import os
import time

import click
import schedule

from spotifystats.core.service.import_history import import_streaming_history
from spotifystats.core.service.spotifystats_service import SpotifyStatsService
from spotifystats.core.util import setup


# Create a click group
@click.group()
def cli():
    pass


# Create a click command
@cli.command("start")
def start():
    """Start the Spotify Stats CLI."""
    click.echo("Starting Spotify Stats CLI...")

    # Create a Spotify Stats Service
    service = SpotifyStatsService()
    service.update()

    schedule.every(30).minutes.do(service.update)

    while True:
        schedule.run_pending()
        time.sleep(1)


@cli.command("import")
@click.argument("directory")
def import_history(directory):
    """Import data from a file."""
    click.echo(f"Importing streaming history from {directory}...")
    import_streaming_history(directory)


@cli.command("run-api")
def run_web():
    """Run the web app."""

    from spotifystats.api.app import app

    setup()

    click.echo("Running web app...")

    host = os.environ.get("SPOTIFYSTATS_WEB_HOST", "0.0.0.0")
    port = int(os.environ.get("SPOTIFYSTATS_WEB_PORT", "5000"))

    app.run(host=host, port=port)


if __name__ == "__main__":
    cli()
