"""
CLI commands related to the master
"""

import sys
import typer

from app import utils
from app import master

app = typer.Typer(add_completion=False)


@app.command()
def start(max_workers: int = 2, auto_remove: bool = True):
    """
    Starts the master container

    Requires Docker to be installed.

    --max-workers

        Maximum number of workers that the master can create.

    --auto-remove

        Remove the container when it has finished running.
    """

    try:
        utils.get_docker_client()
        typer.secho("Successfully connected to the Docker daemon", fg=typer.colors.GREEN, bold=True)

        typer.secho("Starting the master Docker container...", fg=typer.colors.BLUE, bold=True)
        container = master.manage.run(max_workers=max_workers, auto_remove=auto_remove)
        typer.secho(f"Master Docker container has successfully started! Name: {container.name}",
                    fg=typer.colors.GREEN, bold=True)
    except Exception as err:
        typer.secho("An error was encountered:", fg=typer.colors.RED, bold=True)
        typer.echo(err)
        sys.exit(1)


@app.command()
def stop():
    """
    Stops the master container
    """

    try:
        container = utils.get_master_container()
        container.stop()
        typer.secho("Master Docker container has been successfully stopped!",
                    fg=typer.colors.GREEN, bold=True)
    except Exception as err:
        typer.secho("An error was encountered:", fg=typer.colors.RED, bold=True)
        typer.echo(err)
        sys.exit(1)


@app.command()
def list_plugins():
    """
    Lists plugins that are supported by the master node

    Requires the master node to be started.
    """

    # for now let's display only the docker plugin
    typer.secho("Supported plugins", fg=typer.colors.BLUE)
    typer.echo("  - docker")


if __name__ == "__main__":
    app()
