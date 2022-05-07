"""
Various utilities used throughout the application.
"""

import docker

import config


def get_docker_client() -> docker.DockerClient:
    """
    :return: A DockerClient instance
    """
    return docker.DockerClient(base_url=config.DOCKER_BASE_URL)
