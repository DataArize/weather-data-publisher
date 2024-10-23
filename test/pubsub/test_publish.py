from unittest.mock import patch, MagicMock

import pytest

from src.exceptions.exception import PublishError
from src.pubsub.publish import Publisher


def test_publish_success():
    message = {
        "coord": {"lat": 28.5978, "lon": -81.3534},
        "main": {"temp": 294.71, "feels_like": 295.4, "pressure": 1017, "humidity": 95},
        "weather": [{"main": "Clouds", "description": "few clouds"}],
        "wind": {"speed": 3.09},
        "sys": {"country": "US"},
        "name": "Winter Park"
    }

    # Mock the publisher and the publish_future.result() method
    with patch('src.pubsub.publish.publisher') as mock_publisher:
        mock_publish_future = MagicMock()
        mock_publish_future.result.return_value = None  # Simulate successful publishing
        mock_publisher.publish.return_value = mock_publish_future

        # Call the publish method - this will use the mocked publisher
        response = Publisher.publish(message)

        assert response == "Message published successfully."
        mock_publisher.publish.assert_called_once()  # Ensure publish was called once


def test_publish_failure():
    message = {
        "coord": {"lat": 28.5978, "lon": -81.3534},
        "main": {"temp": 294.71, "feels_like": 295.4, "pressure": 1017, "humidity": 95},
        "weather": [{"main": "Clouds", "description": "few clouds"}],
        "wind": {"speed": 3.09},
        "sys": {"country": "US"},
        "name": "Winter Park"
    }

    with patch('src.pubsub.publish.publisher') as mock_publisher:
        mock_publish_future = MagicMock()
        mock_publish_future.result.side_effect = Exception("Publish error")  # Simulate a failure
        mock_publisher.publish.return_value = mock_publish_future

        with pytest.raises(PublishError) as exc_info:
            Publisher.publish(message)

        assert "Failed to publish message after 3 attempts" in str(exc_info.value)