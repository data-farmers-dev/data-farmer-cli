"""
Logic for managing the master Docker container.
"""

from docker.models.containers import Container

from app import config
from app import utils


def run(max_workers: int, auto_remove: bool) -> Container:
    """
    Starts a master Docker container.

    :param max_workers: Maximum number of workers that the master can create.
    :param auto_remove: Remove the container when it has finished running.
    :return: Container object of the master (started)
    """
    client = utils.get_docker_client()
    return client.containers.run(
        config.MASTER_IMAGE_NAME,
        detach=True,
        remove=auto_remove,
        name=config.MASTER_CONTAINER_NAME,
        ports={'5555/tcp': config.MASTER_FLASK_PORT},
        environment={
            'HOST': '0.0.0.0',
            'MAX_WORKERS': max_workers
        },
        volumes=["/var/run/docker.sock:/var/run/docker.sock"]
    )
