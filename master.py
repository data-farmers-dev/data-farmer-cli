"""
Logic for creating and interacting with the
master container.
"""

import docker


def start(_client: docker.DockerClient):
    """
    Starts a master Docker container.
    :param _client: A DockerClient instance
    :return: TBD
    """
