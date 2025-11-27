#    Project:    Weather App (Text Version)
#    	•	Ask for a city name.
#    	•	Import a weather API (like requests + OpenWeatherMap).
#    	•	Print temperature and condition.
#    Skills:    uses imports and APIs 


#MODULES
import requests


#Basic User-Functions
def space(x=0):
    if x == 0:
        print()
    elif x == 'line':
        print('''
        
        —————————————————————
        ''')
    else:
        for count in range(3):
            print()
            
            
#Project User-Functions
def get_location(zip):
    url = f'{location_url_zip}zip={zip}&appid={my_api_key}'    #link
    http = requests.get(url)    #https status code
    print(f'Location HTTPS status code: {http}')
    if http.status_code == 200:    #method that reads the status code as int from requests module
        print('Success!')
        location_data = http.json()    #new variable assigned to the API results
        return location_data
    else:
        print(f'The server: {http} failed to return a successful value.')


def get_forcast(lat, lon):
    url = f'{forcast_url}lat={lat}&lon={lon}&appid={my_api_key}&units=imperial'    #link
    http = requests.get(url)    #https status code
    print(f'Forcast HTTPS status code: {http}')
    if http.status_code == 200:    #method that reads the status code as int from requests module
        print('Success!')
        forcast_data = http.json()    #new variable assigned to the API results
        return forcast_data
    else:
        print(f'The server: {http} failed to return a successful value.')


#VARIABLES
location_url_zip = 'http://api.openweathermap.org/geo/1.0/zip?'
my_api_key = 'f7d10bb35e39017b227c6fa95ab29064'
forcast_url = 'https://api.openweathermap.org/data/2.5/weather?'


#***STEP 1 - prompting user for location via zip***
print('Welcome to the Python Weather app')
space()
try:
    zip = int(input('Please enter you zip code: '))
except Exception:
    space()
    print('***Invalid entry: default zip set to: 79601')
    zip = 79601
space('line')
location_info = get_location(zip)


#***STEP 2 - use variable: 'location_info' latitude and longitude to get forcast***
space()
forcast_info = get_forcast(location_info["lat"], location_info["lon"])


#***STEP 3 - returning user location***
space('line')
#print(location_info)    #used to get the dictionary names to call when developing this ptoject
if location_info:
    print(f'        Name       :  {location_info["name"]}')
    print(f'        Country    :  {location_info["country"]}')
    print(f'        Latitude   :  {location_info["lat"]}')
    print(f'        Longitude  :  {location_info["lon"]}')
space('line')
#print(forcast_info)    #used to get the dictionary names to call when developing this ptoject
if forcast_info:
    print(f'        Temp       :  {forcast_info["main"]["temp"]}°F')
    print(f'        feels like :  {forcast_info["main"]["feels_like"]}°F')
    print(f'        Max Temp   :  {forcast_info["main"]["temp_max"]}°F')
    print(f'        Min Temp   :  {forcast_info["main"]["temp_min"]}°F')
    print(f'        Weather    :  {forcast_info["weather"][0]["description"]}')






    
