import os
from google.cloud import pubsub_v1
from src.config.constants import (
    PROJECT_ID_KEY,
    OPENWEATHER_API_KEY,
    ERROR_MSG_PROJECT_ID_NOT_SET,
    ERROR_MSG_API_KEY_NOT_SET,
)
from src.exceptions.exception import ProjectIdError, ApiKeyError


def load_configuration():
    project_id = os.getenv(PROJECT_ID_KEY)
    if not project_id:
        raise ProjectIdError(ERROR_MSG_PROJECT_ID_NOT_SET)

    api_key = os.getenv(OPENWEATHER_API_KEY)
    if not api_key:
        raise ApiKeyError(ERROR_MSG_API_KEY_NOT_SET)

    return project_id, api_key


PROJECT_ID, API_KEY = load_configuration()

# Initialize Pub/Sub publisher
publisher = pubsub_v1.PublisherClient()
