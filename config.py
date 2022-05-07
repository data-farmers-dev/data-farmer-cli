"""
Global configuration module
"""

import os
from dotenv import load_dotenv

load_dotenv()

DOCKER_BASE_URL = os.getenv("DOCKER_BASE_URL") or "unix:///var/run/docker.sock"
