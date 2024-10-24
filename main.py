from flask import jsonify

from src.config.settings import API_KEY
from src.data_ingestion.api_client import APIClient
from src.pubsub.publish import Publisher
from src.exceptions.exception import WeatherApiError, PublishError
from src.utils.logger import logger


def entry_point(request):
    """
    Cloud Function entry point for fetching weather information.

    Args:
        request (flask.Request): The incoming request object containing parameters for the function.

    Returns:
        tuple: A tuple containing the response as a JSON object and HTTP status code.
               - On success, returns a success message and a status code of 200.
               - On failure, returns the error message and a status code of 500.
    """
    try:
        # Extract ZIP code from request parameters if provided
        request_json = request.get_json(silent=True)
        zip_code = request_json.get('zip_code', '32789,US') if request_json else '32789,US'

        logger.info(f"Fetching weather information for ZIP code: {zip_code}")

        # Initialize the API client and fetch weather information
        api_client = APIClient(api_key=API_KEY)
        weather_data = api_client.fetch_weather_information(zip_code=zip_code)

        # Initialize the Publisher and publish the weather data
        publisher = Publisher()
        publish_message = publisher.publish(weather_data)

        logger.info(f"Weather information published successfully: {publish_message}")
        return jsonify({"message": publish_message}), 200

    except WeatherApiError as e:
        logger.error(f"Failed to fetch weather information: {e}")
        return jsonify({"error": "Failed to fetch weather information.", "details": str(e)}), 500

    except PublishError as e:
        logger.error(f"Failed to publish weather information: {e}")
        return jsonify({"error": "Failed to publish weather information.", "details": str(e)}), 500

    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500
