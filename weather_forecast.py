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

def get_hourly_forecast(data):
    """Extract hourly forecast from the API response."""
    return data['list']

def display_weather_forecast(data, forecast_type='all', specific_date=None, is_hourly=False):
    """Display weather forecast information."""
    if not data:
        print("No weather data available.")
        return

    city = data['city']['name']
    country = data['city']['country']
    print(f"\nWeather Forecast for {city}, {country}:\n")

    if is_hourly:
        hourly_forecast = get_hourly_forecast(data)
        if forecast_type == 'specific' and specific_date:
            specific_datetime = datetime.combine(specific_date, datetime.min.time())
            for forecast in hourly_forecast:
                forecast_datetime = datetime.fromtimestamp(forecast['dt'])
                if forecast_datetime.date() == specific_date:
                    display_hour_forecast(forecast_datetime, forecast)
        elif forecast_type == 'today':
            today = datetime.now().date()
            for forecast in hourly_forecast:
                forecast_datetime = datetime.fromtimestamp(forecast['dt'])
                if forecast_datetime.date() == today:
                    display_hour_forecast(forecast_datetime, forecast)
        else:  # 'all' or any other input
            for forecast in hourly_forecast:
                forecast_datetime = datetime.fromtimestamp(forecast['dt'])
                display_hour_forecast(forecast_datetime, forecast)
    else:
        daily_forecast = get_daily_forecast(data)
        if forecast_type == 'specific' and specific_date:
            if specific_date in daily_forecast:
                display_day_forecast(specific_date, daily_forecast[specific_date])
            else:
                print(f"No forecast available for {specific_date}")
        elif forecast_type == 'today':
            today = datetime.now().date()
            if today in daily_forecast:
                display_day_forecast(today, daily_forecast[today])
            else:
                print("No forecast available for today")
        else:  # 'all' or any other input
            for date, forecast in daily_forecast.items():
                display_day_forecast(date, forecast)

def display_day_forecast(date, forecast):
    """Display forecast for a single day."""
    temp = forecast['main']['temp']
    description = forecast['weather'][0]['description']
    
    print(f"Date: {date}")
    print(f"Temperature: {temp}°C")
    print(f"Description: {description}")
    print("-" * 30)

def display_hour_forecast(datetime, forecast):
    """Display forecast for a single hour."""
    temp = forecast['main']['temp']
    description = forecast['weather'][0]['description']
    
    print(f"Date and Time: {datetime}")
    print(f"Temperature: {temp}°C")
    print(f"Description: {description}")
    print("-" * 30)

def main():
    city = input("Enter city name: ")
    country_code = input("Enter country code (e.g., US, GB, DE): ")
    
    forecast_interval = input("Enter forecast interval (daily/hourly): ").lower()
    is_hourly = forecast_interval == 'hourly'
    
    forecast_type = input("Enter forecast type (today/all/specific): ").lower()
    specific_date = None
    
    if forecast_type == 'specific':
        date_input = input("Enter date (YYYY-MM-DD): ")
        try:
            specific_date = datetime.strptime(date_input, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Using 'all' forecast type.")
            forecast_type = 'all'

    try:
        forecast_data = fetch_weather_forecast(city, country_code)
        if forecast_data:
            display_weather_forecast(forecast_data, forecast_type, specific_date, is_hourly)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
