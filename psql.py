import configparser
import psycopg2
import weather_api


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
    cur.execute("SELECT latitude, longitude from location where city_state = %s", (city_state,))
    data = cur.fetchone()
    if data:
        latitude, longitude = float(data[0]), float(data[1])
        print(1)
        return latitude, longitude
    else:
        latitude, longitude = weather_api.api_get_lon_lat(city, state, country)
        cur.execute('insert into location(city_state, country, longitude, latitude) values (%s, %s, %s, %s)',
                    (city_state, country, longitude, latitude))
        conn.commit()
        cur.execute("SELECT latitude, longitude from location where city_state = %s", (city_state,))
        data = cur.fetchone()
        if data:
            latitude, longitude = float(data[0]), float(data[1])
            print(2)
            return latitude, longitude
        
print(psql_get_lat_lon('clayton', 'nc', 'usa'))