import os
from unittest.mock import patch, Mock

import pytest

from src.config.constants import OPENWEATHER_API_KEY
from src.data_ingestion.api_client import APIClient
from src.exceptions.exception import CoordinatesError, WeatherApiError

API_KEY = os.getenv(OPENWEATHER_API_KEY)

@pytest.fixture
def api_client():
    return APIClient(API_KEY)


def test_fetch_coordinates_success(api_client):
    with patch('src.data_ingestion.api_client.request') as mock_request:
        mock_request.return_value.status_code = 200
        mock_request.return_value.json.return_value = {
            "lat": 28.5978,
            "lon": -81.3534
        }

        coordinates = api_client.fetch_coordinates("32789,US")

        assert coordinates['lat'] == 28.5978
        assert coordinates['lon'] == -81.3534


def test_fetch_coordinates_failure(api_client):
    with patch('src.data_ingestion.api_client.request') as mock_request:
        mock_request.return_value.status_code = 404
        mock_request.return_value.text = 'Not Found'

        with pytest.raises(CoordinatesError) as exc_info:
            api_client.fetch_coordinates("invalid_zip")

        assert "Failed to fetch coordinates" in str(exc_info.value)


def test_fetch_weather_information_success(api_client):
    with patch('src.data_ingestion.api_client.request') as mock_request:
        # Mock the coordinates response
        mock_coordinates_response = Mock()
        mock_coordinates_response.status_code = 200
        mock_coordinates_response.json.return_value = {"lat": 28.5978, "lon": -81.3534}

        # Mock the weather information response
        mock_weather_response = Mock()
        mock_weather_response.status_code = 200
        mock_weather_response.json.return_value = {
            "main": {"temp": 294.71, "feels_like": 295.4, "pressure": 1017, "humidity": 95},
            "weather": [{"main": "Clouds", "description": "few clouds"}],
            "wind": {"speed": 3.09},
            "sys": {"country": "US"},
            "name": "Winter Park"
        }

        # Set the side effect of the mock_request call
        mock_request.side_effect = [mock_coordinates_response, mock_weather_response]

        # Call the method under test
        weather_info = api_client.fetch_weather_information("32789,US")

        # Assert the response
        assert weather_info['main']['temp'] == 294.71
        assert weather_info['name'] == "Winter Park"


def test_fetch_weather_information_failure(api_client):
    with patch('src.data_ingestion.api_client.request') as mock_request:
        # Mock the coordinates response to succeed
        mock_coordinates_response = Mock()
        mock_coordinates_response.status_code = 200
        mock_coordinates_response.json.return_value = {"lat": 28.5978, "lon": -81.3534}

        # Mock the weather information response to fail
        mock_weather_response = Mock()
        mock_weather_response.status_code = 500
        mock_weather_response.text = 'Internal Server Error'

        # Set the side effects of the mock_request call
        mock_request.side_effect = [mock_coordinates_response, mock_weather_response]

        # Assert that WeatherApiError is raised during weather information fetch
        with pytest.raises(WeatherApiError) as exc_info:
            api_client.fetch_weather_information("32789,US")

        # Verify the error message
        assert "Error fetching weather information" in str(exc_info.value)