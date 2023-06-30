import time

import click
import schedule
from spotifystats.service.import_history import import_streaming_history
from spotifystats.service.spotifystats_service import SpotifyStatsService


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


if __name__ == "__main__":
    cli()
