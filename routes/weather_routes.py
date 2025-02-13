import requests
from flask import Blueprint, render_template, request

from config import config
from utils.authentication import require_login

weather_bp = Blueprint('weather', __name__)

def fetch_weather_data(lat, lon):
    """Fetches weather data from OpenWeather API."""
    api_url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={config.WEATHER_API_KEY}&units=metric'
    response = requests.get(api_url)
    return response.json() if response.status_code == 200 else None

@weather_bp.route('/currentweather')
@require_login
def current_weather():
    """Renders the current weather page."""
    return render_template('currentweather.html')

@weather_bp.route('/upcomingweather')
@require_login
def upcoming_weather():
    """Renders the upcoming weather forecast page."""
    return render_template('upcomingweather.html')

@weather_bp.route('/weather', methods=['POST'])
@require_login
def get_weather():
    """Handles the weather request based on user input."""
    lat = request.form.get('lat')
    lon = request.form.get('lon')

    if not lat or not lon:
        return render_template('currentweather.html', message="Invalid location provided.")

    weather_data = fetch_weather_data(lat, lon)

    if not weather_data:
        return render_template('currentweather.html', message="Failed to fetch weather data.")

    return render_template('currentweather.html', weather=weather_data)