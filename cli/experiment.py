"""
CLI commands related to an experiment
"""

import typer

app = typer.Typer(add_completion=False)


@app.command()
def start(archive: str, plugin: str = "docker",
                   workers: int = 2, tasks_per_worker: int = 2):
    """
    Runs an experiment with a given configuration

    Requires the master node to be started.
    """
    typer.secho("TBD", fg=typer.colors.BLUE)


if __name__ == "__main__":
    app()
