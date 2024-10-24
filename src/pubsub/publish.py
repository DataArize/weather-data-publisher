import json
import time
from google.api_core.exceptions import GoogleAPICallError, RetryError

from src.config.constants import PUBSUB_TOPIC_NAME
from src.config.settings import publisher, PROJECT_ID
from src.exceptions.exception import PublishError
from src.utils.logger import logger

class Publisher:

    @staticmethod
    def publish(message, retries=3, backoff_factor=2):
        """
        Publish a message to the specified Pub/Sub topic with retry logic.

        :param message: The message to be published as a dictionary.
        :param retries: The number of retries before giving up (default: 3).
        :param backoff_factor: Factor to multiply delay time between retries (default: 2).
        :raises PublishError: If the message fails to publish.
        :return: A success message upon successful publishing.
        """
        topic_path = publisher.topic_path(PROJECT_ID, PUBSUB_TOPIC_NAME)
        message_bytes = json.dumps(message).encode("utf-8")

        for attempt in range(retries):
            try:
                publish_future = publisher.publish(topic_path, data=message_bytes)
                publish_future.result()  # Block until the message is successfully published
                logger.info(f"Message published successfully to topic {PUBSUB_TOPIC_NAME}: {message}")
                return "Message published successfully."
            except (GoogleAPICallError, RetryError, Exception) as e:
                logger.error(f"Attempt {attempt + 1} - Error publishing message to {PUBSUB_TOPIC_NAME}: {e}")
                if attempt < retries - 1:  # If not the last attempt, back off
                    time.sleep(backoff_factor ** attempt)
                else:
                    raise PublishError(f"Failed to publish message after {retries} attempts: {e}")
