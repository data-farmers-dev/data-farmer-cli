"""
Various utilities used throughout the application.
"""

from docker import DockerClient
from docker.models.containers import Container

from app import config


def get_docker_client() -> DockerClient:
    """
    :return: A DockerClient instance
    """
    return DockerClient(base_url=config.DOCKER_BASE_URL)


def get_master_container() -> Container:
    """
    :return: A Docker container of the master
    """
    client = get_docker_client()
    return client.containers.get(config.MASTER_CONTAINER_NAME)
