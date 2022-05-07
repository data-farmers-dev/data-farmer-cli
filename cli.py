"""
The CLI definition using Typer library.
"""

import sys

import typer

import config
import utils
import master

app = typer.Typer(add_completion=False)


@app.command()
def start_master(_max_workers: int = 2):
    """
    Starts the master container

    Requires Docker to be installed.

    --max-workers

        Maximum number of workers that the master can create.
    """

    try:
        client = utils.get_docker_client(config.DOCKER_BASE_URL)
        typer.secho("Successfully connected to the Docker daemon", fg=typer.colors.GREEN, bold=True)

        typer.secho("Starting the master Docker container...", fg=typer.colors.BLUE, bold=True)
        master.manage.create(client)
    except Exception as err:
        typer.secho("Could not connect to the Docker daemon:", fg=typer.colors.RED, bold=True)
        typer.echo(err)
        sys.exit(1)


@app.command()
def list_plugins():
    """
    Lists plugins that are supported by the master node

    Requires the master node to be started.
    """
    typer.secho("TBD", fg=typer.colors.BLUE)


@app.command()
def run_experiment():
    """
    Runs an experiment with a given configuration

    Requires the master node to be started.
    """
    typer.secho("TBD", fg=typer.colors.BLUE)
