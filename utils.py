import docker


def get_docker_client(base_url: str):
    return docker.DockerClient(base_url=base_url)
