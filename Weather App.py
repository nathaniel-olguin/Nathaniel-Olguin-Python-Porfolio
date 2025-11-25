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
def get_weather(city='Abilene'):
    url = f'{weather_url}q={city}&limit=5&appid={my_api_key}'
    http = requests.get(url)    #https status code
    print(f'HTTPS status code: {http}')
    
    if http.status_code == 200:    #method that reads the status code as int from requests module
        print('Success!')
        weather_data = http.json()
        return weather_data
    else:
        print(f'The server: {http} failed to return a successful value.')


#VARIABLES
weather_url = 'http://api.openweathermap.org/geo/1.0/direct?'
my_api_key = 'f7d10bb35e39017b227c6fa95ab29064'
# = https://api.weather.gov/


#STEP 1 - collecting user location
print('Welcome to the Python Weather app')
space()
city = input('Please enter your city: ').capitalize().strip()
space('line')


#STEP 2 - returning user location
get_weather(city)
weather_info = get_weather(city)

print(weather_info)    #check dictionary values
space()


#STEP 3 - 
if weather_info:
    print(f'Name: {weather_info[name].capitalize()}')
    print(f'Country: {weather_info[country].capitalize()}')
    print(f'State: {weather_info[state].capitalize()}')


