"""
Global configuration module
"""

import os
from dotenv import load_dotenv

load_dotenv()

# Docker

DOCKER_BASE_URL = os.getenv("DOCKER_BASE_URL") or "unix:///var/run/docker.sock"

# Master container

MASTER_IMAGE_NAME = os.getenv("MASTER_IMAGE_NAME")

MASTER_CONTAINER_NAME = os.getenv("MASTER_CONTAINER_NAME") or "data-farmer-master"

MASTER_FLASK_PORT = os.getenv("MASTER_FLASK_PORT") or 5555
