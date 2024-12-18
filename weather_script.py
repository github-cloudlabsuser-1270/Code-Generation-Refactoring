import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    return response.json()

def main():
    api_key = "da7ded826d39dbf7308da72a2198823a"  # Replace with your actual API key
    city = input("Enter city name: ")
    weather_data = get_weather(city, api_key)
    
    if weather_data.get("cod") != 200:
        print("Error:", weather_data.get("message"))
    else:
        print(f"Weather in {city}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Weather: {weather_data['weather'][0]['description']}")

if __name__ == "__main__":
    main()