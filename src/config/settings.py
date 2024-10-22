import os
from src.config.constants import PROJECT_ID_KEY
from src.exceptions.exception import ProjectIdError, ApiKeyError

PROJECT_ID = os.getenv(PROJECT_ID_KEY)

if not PROJECT_ID:
    raise ProjectIdError(f"The project ID environment variable {PROJECT_ID_KEY} is not set.")


api_key = os.getenv('OPENWEATHER_API_KEY')
print(api_key)
if not api_key:
    raise ApiKeyError("The API key is not set. Please set the OPENWEATHER_API_KEY environment variable.")
