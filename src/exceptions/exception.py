class ProjectIdError(Exception):
    """Raised when the Project ID is missing or invalid."""
    pass

class ApiKeyError(Exception):
    """Raised when the API key is missing or invalid."""
    pass

class WeatherApiError(Exception):
    """Raised when there is an error in fetching weather data from the API."""
    pass

class CoordinatesError(Exception):
    """Raised when the coordinates (latitude and longitude) cannot be fetched or are invalid."""
    pass

class PublishError(Exception):
    """Raised when the publishing failed """
    pass