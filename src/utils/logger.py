import logging
import os
from google.cloud.logging_v2 import Client
from google.cloud.logging_v2.handlers import CloudLoggingHandler

from src.config.constants import ENVIRONMENT, TEST


def setup_logging():
    # Only setup cloud logging if NOT in a test environment
    if os.getenv(ENVIRONMENT) != TEST:
        client = Client()
        cloud_handler = CloudLoggingHandler(client)

        log = logging.getLogger(__name__)
        log.setLevel(logging.INFO)
        log.addHandler(cloud_handler)
    else:
        log = logging.getLogger(__name__)
        log.setLevel(logging.DEBUG)  # Set to DEBUG or INFO for test logs
        log.addHandler(logging.StreamHandler())  # Output logs to console during tests

    return log


# Initialize logger when needed
logger = setup_logging()
