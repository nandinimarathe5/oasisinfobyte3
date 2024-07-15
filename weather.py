import requests
def get_weather_data(city, api_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

def main():
    city = 'London' 
    api_key = 'YOUR_API_KEY' 
    weather_data = get_weather_data(city, api_key)

    if 'main' in weather_data and 'weather' in weather_data:
        temperature_celsius = round(weather_data['main']['temp'] - 273.15)
        description = weather_data['weather'][0]['description']
        print(f'City: {city}')
        print(f'Temperature: {temperature_celsius}°C')
        print(f'Description: {description}')
    else:
        print('Failed to fetch weather data')
if _name_ == "_main_":
    main()