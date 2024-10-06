# Weather-Forecast-Fetcher

Weather-Forecast-Fetcher is a Python application that fetches and displays weather forecasts using the OpenWeather API. It provides both daily and hourly forecasts for cities worldwide.

## Features

- Fetch weather forecasts for any city
- Display daily or hourly forecasts
- View forecasts for today, all available days, or a specific date
- Uses OpenWeather API for accurate and up-to-date weather information

## Requirements

- Python 3.6+
- `requests` library
- OpenWeather API key

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/Weather-Forecast-Fetcher.git
   cd Weather-Forecast-Fetcher
   ```

2. Install the required library:
   ```
   pip install requests
   ```

3. Set up your OpenWeather API key:
   - Sign up for a free API key at [OpenWeather](https://openweathermap.org/api)
   - Set the API key as an environment variable:
     - For Windows:
       ```
       set OPENWEATHER_API_KEY=your_api_key_here
       ```
     - For permanent setting on Windows:
       ```
       setx OPENWEATHER_API_KEY your_api_key_here
       ```
     - For Unix-based systems:
       ```
       export OPENWEATHER_API_KEY=your_api_key_here
       ```

## Usage

Run the script:

```
python weather_forecast.py
```

Follow the prompts to enter:
1. City name
2. Country code
3. Forecast interval (daily/hourly)
4. Forecast type (today/all/specific)
5. Specific date (if applicable)

The application will then display the requested weather forecast.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
