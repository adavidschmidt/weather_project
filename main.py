import psql
import time


list = []
# print(len(list))
if len(list) < 1:
    city = input('Please enter the city you would like the weather from: ')
    state = input('Please enter the state abbreviation for the city: ')
    country = input('Please enter the country the city and state are located (United States is usa): ')
    
    list.append([city, state, country])
banana = True
while banana:
    cont = input('Would you like to add more?(Y/n) ')
    cont = cont.lower()
    if cont == 'yes' or cont == 'y':
        city = input('Please enter the city you would like the weather from: ')
        state = input('Please enter the state abbreviation for the city: ')
        country = input('Please enter the country the city and state are located (United States is usa): ')
        
        list.append([city, state, country])
    else:
        banana = False

repeat = int(input('How often, in minutes, do you want to gather weather data? '))
repeat = repeat*60

quanity = int(input('How many data points do you want? '))

z = 0

while z != quanity:
    for i in list:
        city = i[0]
        state = i[1]
        country = i[2]
        lat, lon, location_id = psql.psql_get_lat_lon(city, state, country)
        psql.psql_add_weather(lat, lon, location_id)
    z += 1
    time.sleep(repeat)

        