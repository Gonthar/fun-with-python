# src/fun_with_python/console.py
import textwrap

import click
import locale
import requests

from . import __version__

API_URL = "https://%s.wikipedia.org/api/rest_v1/page/random/summary"

@click.command()
@click.option("-l", "language", type=str,
        default=locale.getlocale()[0].split("_")[0],
        help="selected Wikipedia language")
@click.version_option(version=__version__)
def main(language):
    """The hypermodern Python project."""
    try:
        with requests.get(API_URL % language) as response:
            response.raise_for_status()
            data = response.json()

        title = data["title"]
        extract = data["extract"]

        click.secho(title, fg="cyan")
        click.echo(textwrap.fill(extract))
    except Exception:
        click.echo("Sorry, we weren't able to connect to Wikipedia. Maybe your internet is down?")
        
