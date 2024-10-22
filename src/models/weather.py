# Classes for Weather Data
class Coord:
    def __init__(self, lon, lat):
        self.lon = lon
        self.lat = lat

class Weather:
    def __init__(self, main, description):
        self.main = main
        self.description = description

class Main:
    def __init__(self, temp, feels_like, pressure, humidity):
        self.temp = temp
        self.feels_like = feels_like
        self.pressure = pressure
        self.humidity = humidity

class Wind:
    def __init__(self, speed):
        self.speed = speed

class Sys:
    def __init__(self, country):
        self.country = country

class WeatherData:
    def __init__(self, coord, weather, main, wind, dt, sys, name):
        self.coord = coord
        self.weather = weather
        self.main = main
        self.wind = wind
        self.dt = dt
        self.sys = sys
        self.name = name
