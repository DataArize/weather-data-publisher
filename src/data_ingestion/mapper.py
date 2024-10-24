from src.models.weather import Coord, Weather, Main, Wind, Sys, WeatherData


def map_weather_response(weather_response):
    """
    Map the OpenWeather API response to the WeatherData object.

    :param weather_response: The JSON response from the OpenWeather API.
    :return: An instance of WeatherData populated with data from the response.
    :raises KeyError: If required fields are missing from the response.
    """
    # Validate fields in the response
    coord_data = weather_response.get('coord', {})
    main_data = weather_response.get('main', {})
    wind_data = weather_response.get('wind', {})
    sys_data = weather_response.get('sys', {})
    weather_list = weather_response.get('weather', [])

    # Extract coordinates
    coord = Coord(coord_data.get('lon'), coord_data.get('lat'))

    # Handle weather information (assuming the first element if available)
    if not weather_list:
        raise KeyError("Weather information is missing in the response.")

    weather_info = weather_list[0]
    weather = Weather(weather_info.get('main', 'N/A'), weather_info.get('description', 'No description'))

    # Main weather data
    main = Main(
        temp=main_data.get('temp', 0),
        feels_like=main_data.get('feels_like', 0),
        pressure=main_data.get('pressure', 0),
        humidity=main_data.get('humidity', 0)
    )

    # Wind and system data
    wind = Wind(wind_data.get('speed', 0))
    sys = Sys(sys_data.get('country', 'Unknown'))

    # Location name and timestamp
    name = weather_response.get('name', 'Unknown location')
    dt = weather_response.get('dt', 0)

    # Construct the WeatherData object
    weather_data = WeatherData(coord, weather, main, wind, dt, sys, name)

    return weather_data
