import configparser
import requests
import json

config = configparser.ConfigParser()
config.read('config.ini')

API_KEY = config['api']['key']

def api_get_lon_lat(city, state, country):
    url_base = 'http://api.openweathermap.org/geo/1.0/direct'
    
    url_full = f'{url_base}?q={city},{state},{country}&limit=1&appid={API_KEY}'
    
    response = requests.get(url_full)
    
    if response.status_code == 200:
        data = response.json()
        for entry in data:
            lat = entry['lat']
            lon = entry['lon']
            return lat, lon

def api_get_weather(lat, lon):
    
    url_base = 'https://api.openweathermap.org/data/2.5/weather'
    
    url_full = f'{url_base}?lat={lat}&lon={lon}&appid={API_KEY}&units=imperial'
    
    response = requests.get(url_full)
    
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        min = data['main']['temp_min']
        max = data['main']['temp_max']
        return temp, feels_like, pressure, humidity, min, max
    else:
        print(f'Error: {response.status_code}')
        return None
    
    