class Coord:
    def __init__(self, lon, lat):
        self.lon = lon
        self.lat = lat

    def to_dict(self):
        return {
            "lon": self.lon,
            "lat": self.lat
        }

class Weather:
    def __init__(self, main, description):
        self.main = main
        self.description = description

    def to_dict(self):
        return {
            "main": self.main,
            "description": self.description
        }

class Main:
    def __init__(self, temp, feels_like, pressure, humidity):
        self.temp = temp
        self.feels_like = feels_like
        self.pressure = pressure
        self.humidity = humidity

    def to_dict(self):
        return {
            "temp": self.temp,
            "feels_like": self.feels_like,
            "pressure": self.pressure,
            "humidity": self.humidity
        }

class Wind:
    def __init__(self, speed):
        self.speed = speed

    def to_dict(self):
        return {
            "speed": self.speed
        }

class Sys:
    def __init__(self, country):
        self.country = country

    def to_dict(self):
        return {
            "country": self.country
        }

class WeatherData:
    def __init__(self, coord, weather, main, wind, dt, sys, name):
        self.coord = coord
        self.weather = weather
        self.main = main
        self.wind = wind
        self.dt = dt
        self.sys = sys
        self.name = name

    def to_dict(self):
        return {
            "coord": self.coord.to_dict(),
            "weather": self.weather.to_dict(),
            "main": self.main.to_dict(),
            "wind": self.wind.to_dict(),
            "dt": self.dt,
            "sys": self.sys.to_dict(),
            "name": self.name
        }
