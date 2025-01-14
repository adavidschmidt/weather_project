import configparser
import psycopg2
import weather_api
import pytz
from datetime import datetime

config = configparser.ConfigParser()
config.read('config.ini')

db_config = config['postgresql']

conn = psycopg2.connect(
    host=db_config['host'],
    database=db_config['database'],
    user=db_config['user'],
    password=db_config['password'],
    port=db_config['port']
)

cur = conn.cursor()


# function to run sql query to get and check if the cit_state is in the database yet
# will run the api to get the lon and lat from OpenWeatherMap if city_state is not in database
def psql_get_lat_lon(city, state, country):
    city_state = f'{city}, {state}'
    city_state = city_state.lower()
    country = country.lower()
    cur.execute("SELECT latitude, longitude, location_id from location where city_state = %s", (city_state,))
    data = cur.fetchone()
    if data:
        latitude, longitude, location_id = float(data[0]), float(data[1]), int(data[2])
        print(1)
        return latitude, longitude, location_id
    else:
        latitude, longitude = weather_api.api_get_lon_lat(city, state, country)
        cur.execute('insert into location(city_state, country, longitude, latitude) values (%s, %s, %s, %s)',
                    (city_state, country, longitude, latitude))
        conn.commit()
        cur.execute("SELECT latitude, longitude, location_id from location where city_state = %s", (city_state,))
        data = cur.fetchone()
        if data:
            latitude, longitude, location_id = float(data[0]), float(data[1]), int(data[2])
            print(2)
            return latitude, longitude, location_id
        
def psql_add_weather(lat, lon, location_id):
    data = weather_api.api_get_weather(lat, lon)
    est = pytz.timezone('US/Eastern')
    now = datetime.now(est)
    temp, feel, pressure, humidity, min, max = data
    cur.execute('insert into weather(temperature_fahrenheit, feels_like_fahrenheit, pressure, humidity, location_id, datetime, min_temp, max_temp) values (%s, %s, %s, %s, %s, %s, %s, %s)',
                (temp, feel, pressure, humidity, location_id, now, min, max))
    conn.commit()
    