# Weather Data Fetcher

### Overview
The Weather Data Fetcher is a Python application that retrieves weather information using the OpenWeather API and publish it to Google Cloud Pub/Sub. It allows users to fetch geographical coordinates based on ZIP codes and obtain current weather data for specific locations.

### Features

- **Fetch Coordinates by ZIP Code:** Retrieve geographical coordinates (latitude and longitude) using a specified ZIP code.
- **Fetch Weather Information:** Obtain current weather information for a location based on its coordinates, with data mapped to a user-friendly format.
- **Event Publishing:** Publish weather data events to Google Cloud Pub/Sub, allowing for real-time data processing and analysis.
- **Error Handling:** Custom error handling for API requests, including logging for insights into interactions and errors.
- **Input Validation:** Basic validation to ensure valid input formats for ZIP codes.
- **Unit Testing:** Comprehensive unit tests to ensure the functionality of the API client methods.

### Technologies Used

- Python
- OpenWeather API
- Google Cloud Pub/Sub (for data publishing)
- Requests library for API calls

### Installation

1. **clone the Repository:**
   ```
   git clone https://github.com/yourusername/weather-data-fetcher.git
   cd weather-data-fetcher
   ```
2. **Set Up a Virtual Environment:**
    ```
    python -m venv venv
    source venv/bin/activate 
    ```
3. **Install Dependencies:**
    ```
    pip install -r requirements.txt
    ```
4. **Set Up Environment Variables:**
    
    Ensure you have the following environment variables set up for your application to run:

   * OPENWEATHER_API_KEY: Your API key for the OpenWeather API.
   * PROJECT_ID: Your Google Cloud project ID.
   * TOPIC_NAME: The name of the Pub/Sub topic for publishing weather data.

### Usage

#### Fetching Weather Data
1. Create an Instance of the API Client:
    ```
    from src.data_ingestion.api_client import APIClient
    api_key = 'your_openweather_api_key'
    client = APIClient(api_key)
    ```
2. Fetch Weather Information:
    ```
    zip_code = '32789,US'
    weather_data = client.fetch_weather_information(zip_code)
    print(weather_data)
    ```

### Publishing to Google Cloud Pub/Sub
The fetched weather data can also be published to a Google Cloud Pub/Sub topic using the Publisher class:

```
from src.publisher import Publisher

publisher = Publisher()
message = {
    "coord": {"lon": -81.3534, "lat": 28.5978},
    "weather": {"main": "Clouds", "description": "few clouds"},
    "main": {"temp": 294.71, "feels_like": 295.4, "pressure": 1017, "humidity": 95},
    "wind": {"speed": 3.09},
    "dt": 1729661941,
    "sys": {"country": "US"},
    "name": "Winter Park"
}

publisher.publish(message)

```

### Error Handling

The application raises custom errors in case of API request failures:

* CoordinatesError: Raised if fetching coordinates fails.
* WeatherApiError: Raised if fetching weather data fails.

Errors are logged for debugging and troubleshooting.

### Unit Testing

Unit tests for the API client can be run using:
```
pytest tests/
```

### Contributing

Contributions are welcome! Please follow these steps:

* Fork the repository.
* Create a new branch for your feature or bug fix.
* Make your changes and commit them.
* Push to your branch and create a pull request.

### License
This project is for personal use only. No license is granted for public use, distribution, or modification.
