import logging
from google.cloud.logging_v2 import Client
from google.cloud.logging_v2.handlers import CloudLoggingHandler

client = Client()
cloud_handler = CloudLoggingHandler(client)

logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)
logger.addHandler(cloud_handler)