"""
Various utilities used throughout the application.
"""

import docker


def get_docker_client(base_url: str):
    """
    :param base_url: URL to the Docker server
    :return: A DockerClient instance
    """
    return docker.DockerClient(base_url=base_url)
