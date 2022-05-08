"""
CLI commands related to an experiment
"""

import typer

app = typer.Typer(add_completion=False)


@app.command()
def start(archive: str, plugin: str = "docker",
                   workers: int = 2, tasks_per_worker: int = 2):
    """
    \b
    Runs an experiment with a given configuration
    Requires the master node to be started.

    \b
    ARCHIVE
        Path to the archive with the experiment definition.
        It consists of a bash script that executes the user's program,
        the user's program itself, and the JSON parameters config file.

    \b
    --plugin
        One of the plugins supported by the master. See `master list-plugins`.

    \b
    --workers
        Number of workers that the experiment should run on.
        Can't be greater than `--max-workers` used with `master start`.

    \b
    --tasks-per-worker
        Limit of tasks that a single worker can execute.
    """
    typer.secho("TBD", fg=typer.colors.BLUE)


if __name__ == "__main__":
    app()
