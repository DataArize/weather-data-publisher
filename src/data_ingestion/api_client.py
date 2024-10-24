import json

from requests import request

from src.config.constants import GEOCODING_PARAM_ZIP, API_KEY_PARAM, OPENWEATHER_GEOCODING_API_BASE_URL, METHOD_GET, \
    WEATHER_PARAM_LAT, WEATHER_PARAM_LON, OPENWEATHER_API_BASE_URL
from src.config.settings import API_KEY
from src.data_ingestion.mapper import map_weather_response
from src.exceptions.exception import CoordinatesError, WeatherApiError
from src.utils.logger import logger


class APIClient:
    def __init__(self, api_key):
        """
        Initialize the API client with the given API key.

        :param api_key: The API key for authenticating requests to the OpenWeather API.
        """
        self.api_key = api_key

    def fetch_coordinates(self, zip_code):
        """
        Fetch the geographical coordinates for a given ZIP code using the OpenWeather API.

        :param zip_code: The ZIP code for which to fetch coordinates, including the country code (e.g., '32789,US').
        :return: A dictionary containing the coordinates (latitude and longitude) if successful.
        :raises CoordinatesError: If the API request fails.
        """
        params = {GEOCODING_PARAM_ZIP: zip_code, API_KEY_PARAM: self.api_key}
        coordinates_response = request(
            url=OPENWEATHER_GEOCODING_API_BASE_URL,
            params=params,
            method=METHOD_GET,
        )

        if coordinates_response.status_code == 200:
            logger.info(f"Successfully fetched coordinates for {zip_code}")
            return coordinates_response.json()
        print(coordinates_response.text)
        logger.error(f"Error fetching coordinates: {coordinates_response.status_code} - {coordinates_response.text}")
        raise CoordinatesError(f"Failed to fetch coordinates: {coordinates_response.status_code}")

    def fetch_weather_information(self, zip_code="32789,US"):
        """
        Fetch the weather information for a specific location using its ZIP code.

        This function first fetches the geographical coordinates (latitude and longitude) for a given location (default: ZIP code '32789,US').
        It then uses these coordinates to fetch the current weather information from the OpenWeather API.

        :param zip_code: The ZIP code for which to fetch weather information (default: '32789,US').
        :raises ValueError: If latitude and longitude are not found in the response.
        :raises WeatherApiError: If there is an error fetching the weather data (non-200 response).
        :return: A dictionary containing the weather information if the request is successful.
        """
        coordinates = self.fetch_coordinates(zip_code)
        print(coordinates)
        lat = coordinates.get(WEATHER_PARAM_LAT)
        lon = coordinates.get(WEATHER_PARAM_LON)

        if lat is None or lon is None:
            logger.error("Latitude and longitude not found in the response.")
            raise ValueError("Could not extract latitude and longitude.")

        logger.info(f"Latitude: {lat}, Longitude: {lon}")

        params = {
            WEATHER_PARAM_LAT: lat,
            WEATHER_PARAM_LON: lon,
            API_KEY_PARAM: self.api_key,
        }

        weather_response = request(url=OPENWEATHER_API_BASE_URL, params=params, method=METHOD_GET)

        if weather_response.status_code == 200:
            logger.info(f"Successfully fetched weather information for lat: {lat}, lon: {lon}")
            weather_data = map_weather_response(weather_response.json())
            logger.info(f"message: {weather_data.__dict__}")
            return weather_data.to_dict()

        logger.error(f"Error fetching weather information, lat: {lat}, lon: {lon}, "
                     f"status: {weather_response.status_code}, message: {weather_response.text}")
        raise WeatherApiError(f"Error fetching weather information, lat: {lat}, lon: {lon}, "
                              f"status: {weather_response.status_code}, message: {weather_response.text}")