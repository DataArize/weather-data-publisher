# Project-related constants
from jinja2 import Environment

PROJECT_ID_KEY = "GOOGLE_CLOUD_PROJECT"

# OpenWeather API related constants
OPENWEATHER_API_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
OPENWEATHER_GEOCODING_API_BASE_URL = "http://api.openweathermap.org/geo/1.0/zip"
OPENWEATHER_API_KEY = "OPENWEATHER_API_KEY"
GEOCODING_PARAM_ZIP = "zip"
API_KEY_PARAM = "appid"

# Weather data parameters
WEATHER_PARAM_LAT = "lat"
WEATHER_PARAM_LON = "lon"

# Pub/Sub related constants
PUBSUB_TOPIC_NAME = "real-time-weather-feed"

# General purpose constants
METHOD_GET = "GET"
ENCODING_UTF8 = "utf-8"

# Error messages (if needed)
ERROR_MSG_PROJECT_ID_NOT_SET = f"The project ID environment variable {PROJECT_ID_KEY} is not set."
ERROR_MSG_API_KEY_NOT_SET = "The API key is not set. Please set the OPENWEATHER_API_KEY environment variable."

# Environments
ENVIRONMENT = "ENVIRONMENT"
TEST = "TEST"