from src.models.weather import Coord, Weather, Main, Wind, Sys, WeatherData


def map_weather_response(weather_response):
    """
    Map the OpenWeather API response to the WeatherData object.

    :param weather_response: The JSON response from the OpenWeather API.
    :return: An instance of WeatherData populated with data from the response.
    """
    coord = Coord(weather_response['coord']['lon'], weather_response['coord']['lat'])

    # Assuming the first weather object
    weather_info = weather_response['weather'][0]
    weather = Weather(weather_info['main'], weather_info['description'])

    main = Main(
        weather_response['main']['temp'],
        weather_response['main']['feels_like'],
        weather_response['main']['pressure'],
        weather_response['main']['humidity']
    )

    wind = Wind(weather_response['wind']['speed'])
    sys = Sys(weather_response['sys']['country'])

    name = weather_response['name']
    dt = weather_response['dt']

    weather_data = WeatherData(coord, weather, main, wind, dt, sys, name)

    return weather_data
