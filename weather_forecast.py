import requests
import os
from datetime import datetime, timedelta

# Set up API key and base URL
API_KEY = os.environ.get('OPENWEATHER_API_KEY')
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

def fetch_weather_forecast(city, country_code, units='metric'):
    """Fetch weather forecast from OpenWeather API."""
    if not API_KEY:
        raise ValueError("API key not found. Please set the OPENWEATHER_API_KEY environment variable using:\n"
                         "set OPENWEATHER_API_KEY=your_api_key_here\n"
                         "or for permanent setting:\n"
                         "setx OPENWEATHER_API_KEY your_api_key_here")

    params = {
        'q': f"{city},{country_code}",
        'appid': API_KEY,
        'units': units
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def get_daily_forecast(data):
    """Extract daily forecast from the API response."""
    daily_forecast = {}
    for forecast in data['list']:
        date = datetime.fromtimestamp(forecast['dt']).date()
        if date not in daily_forecast:
            daily_forecast[date] = forecast
    return daily_forecast

def display_weather_forecast(data):
    """Display weather forecast information."""
    if not data:
        print("No weather data available.")
        return

    city = data['city']['name']
    country = data['city']['country']
    print(f"\nWeather Forecast for {city}, {country}:\n")

    daily_forecast = get_daily_forecast(data)
    for date, forecast in daily_forecast.items():
        temp = forecast['main']['temp']
        description = forecast['weather'][0]['description']
        
        print(f"Date: {date}")
        print(f"Temperature: {temp}°C")
        print(f"Description: {description}")
        print("-" * 30)

def main():
    city = input("Enter city name: ")
    country_code = input("Enter country code (e.g., US, GB, DE): ")

    try:
        forecast_data = fetch_weather_forecast(city, country_code)
        if forecast_data:
            display_weather_forecast(forecast_data)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
