"""
The CLI definition using Typer library.
Combines subcommands interfaces into one interface.
"""
import typer

from . import master
from . import experiment

__all__ = [master, experiment]

app = typer.Typer(add_completion=False)
app.add_typer(master.app, name="master")
app.add_typer(experiment.app, name="experiment")
