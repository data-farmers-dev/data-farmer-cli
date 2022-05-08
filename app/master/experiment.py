"""
Logic related to providing an experiment to the master.
"""
import requests

from app import config as app_config


def create(archive: str, plugin: str = "docker",
           workers: int = 2, tasks_per_worker: int = 2) -> dict:
    """
    Creates an experiment on the master side via a REST API call.

    :param archive: Path to the archive with the experiment definition.
    :param plugin: One of the plugins supported by the master.
    :param workers: Number of workers that the experiment should run on.
    :param tasks_per_worker: Limit of tasks that a single worker can execute.
    :return:
    """
    with open(archive, 'rb') as archive_file:
        files = {'experiment': archive_file}
        config = {'plugin': plugin, 'workers': workers, 'tasks_per_worker': tasks_per_worker}

        res = send(files, config)
        return res.json()


def send(files, config):
    """
    Makes a POST request to master with the experiment data.

    :param files: A dictionary with file objects
    :param config: A dictionary with the experiment config
    :return:
    """
    return requests.post(f"{app_config.MASTER_BASE_URL}/receiver/upload", files=files, data=config)
