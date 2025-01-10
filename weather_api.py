import configparser
import requests
import json

config = configparser.ConfigParser()
config.read('config.ini')

API_KEY = config['api']['key']

def getLonLat(city, state, country):
    url_base = 'http://api.openweathermap.org/geo/1.0/direct'
    
    url_full = f'{url_base}?q={city},{state},{country}&limit=1&appid={API_KEY}'
    
    response = requests.get(url_full)
    
    if response.status_code == 200:
        data = response.json()
        for entry in data:
            lat = entry['lat']
            lon = entry['lon']
            return lat, lon

def getWeather(lat, lon):
    
    url_base = 'https://api.openweathermap.org/data/2.5/weather'
    
    url_full = f'{url_base}?lat={lat}&lon={lon}&appid={API_KEY}&units=imperial'
    
    response = requests.get(url_full)
    
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        pressure = data['main']['pressure']
        humidity = data['main']['pressure']
        return temp, feels_like, pressure, humidity
    else:
        print(f'Error: {response.status_code}')
        return None
    
    
data = getLonLat('Clayton', 'NC', 'USA')

lat, lon = data

weather = getWeather(lat, lon)

if weather:
    print(weather)