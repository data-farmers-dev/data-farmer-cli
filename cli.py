import typer
import docker
from docker.errors import DockerException

app = typer.Typer()


@app.command()
def start_master(docker_base_url: str = 'unix://var/run/docker.sock', max_workers: int = 2):
    """
    Starts the master container

    Requires Docker to be installed.

    --docker-base-url

        URL to the Docker server. For example, unix:///var/run/docker.sock or tcp://127.0.0.1:1234.

    --max-workers

        Maximum number of workers that the master can create.
    """

    try:
        client = docker.DockerClient(base_url=docker_base_url)
        typer.secho("Successfully connected to the Docker daemon", fg=typer.colors.GREEN, bold=True)
    except DockerException as err:
        typer.secho("Could not connect to the Docker daemon:", fg=typer.colors.RED, bold=True)
        typer.echo(err)


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
