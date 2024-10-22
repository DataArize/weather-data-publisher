from src.config.settings import api_key
from src.data_ingestion.api_client import APIClient


def entry_point(request):
    """
    Cloud Function entry point for fetching weather information.

    Args:
        request (flask.Request): The incoming request object containing parameters for the function.

    Returns:
        tuple: A tuple containing the weather data and HTTP status code.
               - On success, returns the fetched weather data and a status code of 200.
               - On failure, returns the error message and a status code of 500.
    """
    try:
        api_client = APIClient(api_key=api_key)
        weather_data = api_client.fetch_weather_information(zip_code="32789,US")
        return weather_data, 200
    except Exception as e:
        return str(e), 500