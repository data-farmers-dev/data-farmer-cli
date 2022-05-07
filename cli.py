"""
The CLI definition using Typer library.
"""

import sys

import typer
from docker.errors import DockerException

import utils
import master

app = typer.Typer(add_completion=False)


@app.command()
def start_master(docker_base_url: str = 'unix://var/run/docker.sock', _max_workers: int = 2):
    """
    Starts the master container

    Requires Docker to be installed.

    --docker-base-url

        URL to the Docker server. For example, unix:///var/run/docker.sock or tcp://127.0.0.1:1234.

    --max-workers

        Maximum number of workers that the master can create.
    """

    try:
        client = utils.get_docker_client(docker_base_url)
        typer.secho("Successfully connected to the Docker daemon", fg=typer.colors.GREEN, bold=True)

        typer.secho("Starting the master Docker container...", fg=typer.colors.BLUE, bold=True)
        master.start(client)
    except DockerException as err:
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
