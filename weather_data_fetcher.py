import requests

api_key = 'bdc4371d3dc48b3a9dfbb173bba90f54'

city = input('Enter city name: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['main']
    print(f'Current Temperature in {city} city is: {int(temp-273.15)}°C') 
    print(f'Current Weather conditions in {city} city is: {desc}')
else:
    print('404 : Error fetching weather data')
