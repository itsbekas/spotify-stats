import click
import schedule

from spotifystats.service.spotifystats_service import SpotifyStatsService


# Create a click group
@click.group()
def cli():
    pass


# Create a click command
@cli.command()
def start():
    """Start the Spotify Stats CLI."""
    click.echo("Starting Spotify Stats CLI...")

    # Create a Spotify Stats Service
    service = SpotifyStatsService()
    service.update()

    schedule.every(5).seconds.do(click.echo, "Running Spotify Stats Service...")


if __name__ == "__main__":
    cli()
