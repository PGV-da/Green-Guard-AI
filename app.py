from config import config


import base64
import csv
import os
import random
import sqlite3
from functools import wraps

import bcrypt
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from flask import (Flask, flash, jsonify, redirect, render_template, request,
                   session, url_for)
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from statsmodels.tsa.arima.model import ARIMA
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img

from disease import disease_data
from fertilizer import fertilizer_dic

app = Flask(__name__)
app.secret_key = config.SECRET_KEY

# Custom Jinja2 filter for base64 encoding
def b64encode_image(image):
    if image:
        return b64encode(image).decode('utf-8')
    return None

# Register the filter with Jinja2
app.jinja_env.filters['b64encode_image'] = b64encode_image

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/mycrop')
@require_login
def mycrop():
    return render_template('mycrop.html')

@app.route('/price')
@require_login
def price():
    return render_template('price.html')

@app.route('/currentweather')
@require_login
def currentweather():
    return render_template('currentweather.html')

@app.route('/upcomingweather')
@require_login
def upcomingweather():
    return render_template('upcomingweather.html')


@app.route('/news')
@require_login
def news():
    url = 'https://timesofindia.indiatimes.com/topic/tamil-nadu-agriculture'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_articles = []

    for article in soup.find_all('div', class_='uwU81'):
        title = article.find('div', class_='fHv_i').text.strip()
        news_url = article.find('a')['href']
        content = article.find('p', class_='oxXSK').text.strip().split('\n')[0] if '\n' in article.find('p', class_='oxXSK').text.strip() else article.find('p', class_='oxXSK').text.strip()  # Split by newline and take only the first line if there is a newline
        news_articles.append({'title': title, 'url': news_url, 'content': content})

    return render_template('news.html', news_articles=news_articles)


def fetch_weather_data(lat, lon):
    api_key = '465ad6304f12419481b476deed2c4188'
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
@app.route('/fertilizer-recommendation')
@require_login
def fertilizerrecommendation():
    return render_template('fertilizer-recommendation.html',fertilizer=None)


def read_csv():
    crops_data = {}
    with open('data/crop_data.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            crop_name = row['Crop_Subcategory']
            crop_values = {}
            for key, value in row.items():
                if key == 'Crop_Subcategory':
                    continue
                if '-' in value:
                    value_range = value.split('-')
                    min_value = float(value_range[0])
                    max_value = float(value_range[1])
                    crop_values[key] = (min_value, max_value)
                else:
                    value = float(value)
                    crop_values[key] = (value, value)  # For single values, min and max are the same
            crops_data[crop_name] = crop_values
    return crops_data



@app.route('/recommend', methods=['POST'])
@require_login
def recommend():
    crops_data = read_csv()
    
    # Your existing code to process user input and find matching crop subcategory
    selected_crop = request.form['crop']
    n = float(request.form['N'])
    k = float(request.form['K'])
    p = float(request.form['P'])
    zn = float(request.form['Zn'])
    mg = float(request.form['Mg'])
    s = float(request.form['S'])

    for attribute in ['NHigh', 'NLow', 'PHigh', 'PLow', 'KHigh', 'KLow', 'MgHigh', 'MgLow', 'ZnHigh', 'ZnLow', 'SHigh', 'SLow']:
        if attribute in fertilizer_dic:
            recommendation = fertilizer_dic[attribute]
            # Check conditions and return recommendation
            if attribute == 'NHigh' and crops_data[selected_crop]['N'][0] <= n <= crops_data[selected_crop]['N'][1]:
                return render_template('fertilizer-recommendation.html', fertilizer=recommendation)
            elif attribute == 'NLow' and n < crops_data[selected_crop]['N'][0]:
                return render_template('fertilizer-recommendation.html', fertilizer=recommendation)
            elif attribute == 'PHigh' and crops_data[selected_crop]['P'][0] <= p <= crops_data[selected_crop]['P'][1]:
                return render_template('fertilizer-recommendation.html', fertilizer=recommendation)
            elif attribute == 'PLow' and p < crops_data[selected_crop]['P'][0]:
                return render_template('fertilizer-recommendation.html', fertilizer=recommendation)
            elif attribute == 'KHigh' and crops_data[selected_crop]['K'][0] <= k <= crops_data[selected_crop]['K'][1]:
                return render_template('fertilizer-recommendation.html', fertilizer=recommendation)
            elif attribute == 'KLow' and k < crops_data[selected_crop]['K'][0]:
                return render_template('fertilizer-recommendation.html', fertilizer=recommendation)
            elif attribute == 'MgHigh' and crops_data[selected_crop]['Mg'][0] <= mg <= crops_data[selected_crop]['Mg'][1]:
                return render_template('fertilizer-recommendation.html', fertilizer=recommendation)
            elif attribute == 'MgLow' and mg < crops_data[selected_crop]['Mg'][0]:
                return render_template('fertilizer-recommendation.html', fertilizer=recommendation)
            elif attribute == 'ZnHigh' and crops_data[selected_crop]['Zn'][0] <= zn <= crops_data[selected_crop]['Zn'][1]:
                return render_template('fertilizer-recommendation.html', fertilizer=recommendation)
            elif attribute == 'ZnLow' and zn < crops_data[selected_crop]['Zn'][0]:
                return render_template('fertilizer-recommendation.html', fertilizer=recommendation)
            elif attribute == 'SHigh' and crops_data[selected_crop]['S'][0] <= s <= crops_data[selected_crop]['S'][1]:
                return render_template('fertilizer-recommendation.html', fertilizer=recommendation)
            elif attribute == 'SLow' and s < crops_data[selected_crop]['S'][0]:
                return render_template('fertilizer-recommendation.html', fertilizer=recommendation)

    return render_template('fertilizer-recommendation.html', fertilizer='No recommendation found')
@app.route('/forecast', methods=['GET'])
@require_login
def forecast():
    # Get the selected crop from the query parameters
    selected_crop = request.args.get('crop')

    # Load the data from CSV based on the selected crop
    data = pd.read_csv(f'data/{selected_crop}.csv', header=None, names=['Date', 'Value'])

    # Convert 'Date' column to datetime
    data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m')

    # Set 'Date' column as index
    data.set_index('Date', inplace=True)

    # Fit ARIMA model
    model = ARIMA(data['Value'], order=(1,1,1))  # Example order, you might need to adjust
    fit_model = model.fit()

    # Forecast
    forecast = fit_model.forecast(steps=4)  # Example forecast for next 4 periods

    # Prepare data for Plotly
    forecast_dates = pd.date_range(start=data.index[-1], periods=5, freq='M')[1:]
    forecast_dates_str = forecast_dates.strftime('%Y-%m-%d').tolist()
    forecast_values = forecast.tolist()

    # Convert the Plotly figure to JSON
    plot_data = {'index': forecast_dates_str, 'values': forecast_values}

    return jsonify(plot_data)

@app.route('/priceprediction')
@require_login
def priceprediction():
    return render_template('price-prediction.html')

@app.route('/chatassistant')
@require_login
def chatassistant():
    return render_template('chat-assistant.html')

class GardeningAssistant:
    def __init__(self):
        self.greetings = [
            "Hi there! I'm your gardening assistant Bloom. How can I help you today?",
            "Hello! Welcome to the gardening assistant. I am Bloom. What do you need assistance with?",
            "Greetings! I'm Bloom, your gardening companion. How can I assist you today?",
            "Hey there! I'm Bloom, ready to help you with all things gardening.",
            "Hello, gardening enthusiast! I'm Bloom, here to assist you with your gardening needs."
        ]

        self.goodbyes = [
            "Goodbye! Happy gardening!",
            "See you later!",
            "Farewell! May your garden bloom beautifully.",
            "Until next time! Happy gardening!",
            "Take care! Happy gardening with Bloom!"
        ]

        self.plant_info = {
                "Rice": "Rice is a staple food in Tamil Nadu, typically grown in flooded fields called paddies. Main varieties include Samba, Ponni, and Kuruvai. Requires plenty of water and fertile soil.",
    "Wheat": "Wheat is not as commonly grown in Tamil Nadu as rice but is still important. Cultivated in the winter season (Rabi crop), requires well-drained soil and cool temperatures.",
    "Maize": "Maize is an important crop in Tamil Nadu, grown mainly in the rainy season (Kharif crop). Requires well-drained soil and is relatively drought-tolerant.",
    "Sugarcane": "Sugarcane is a major cash crop in Tamil Nadu, requires fertile soil and a tropical climate. Harvested after about 10-12 months of growth.",
    "Cotton": "Cotton is grown in Tamil Nadu for its fiber. Requires a warm climate and well-drained soil. Planted in summer and harvested in the fall.",
    "Groundnut": "Groundnut, or peanut, is grown in Tamil Nadu for its edible oil and protein-rich seeds. Requires well-drained soil and is usually planted in the summer.",
    "Millets": "Millets such as pearl millet (bajra) and finger millet (ragi) are important food crops in Tamil Nadu. Drought-tolerant and can grow in poor soil conditions.",
    "Pulses": "Pulses such as black gram, green gram, and chickpeas are grown in Tamil Nadu for their protein-rich seeds. Require well-drained soil and are usually planted in winter.",
    "Oilseeds": "Oilseeds such as sesame, groundnut, and sunflower are grown in Tamil Nadu for their oil-rich seeds. Require well-drained soil and warm temperatures.",
    "Tea": "Tea is grown in the Nilgiri Hills of Tamil Nadu, requires cool temperatures and well-drained soil. Harvested throughout the year.",
    "Coffee": "Coffee is grown in the Nilgiri Hills and other parts of Tamil Nadu. Requires a cool climate and well-drained soil. Harvested once a year."
}
        self.crops_in_tamilnadu = ["Rice", "Wheat", "Maize", "Sugarcane", "Cotton", "Groundnut", "Millets", "Pulses", "Oilseeds", "Tea", "Coffee"]
        self.modules = {
            "Disease Detection": "diseasedetection",
            "Crop Prediction": "cropprediction",
            "Fertilizer Recommendation": "fertilizerrecommendation",
            "Price Prediction": "priceprediction",
            "Commodity Prices": "commodityprices",
            "Current Weather": "currentweather",
            "Upcoming Weather": "upcomingweather",
            "News": "news",
            "Community": "community"
        }

    def greet(self):
        return random.choice(self.greetings)

    def say_goodbye(self):
        return random.choice(self.goodbyes)


    def get_crops_in_tamilnadu(self):
        return "Crops available in Tamil Nadu include: {}".format(", ".join(self.crops_in_tamilnadu))

    def suggest_modules(self):
        return "You can get help from the following modules in the app: {}".format(", ".join(self.modules.keys()))

    def get_module_url(self, module_name):
        if module_name in self.modules:
            return self.modules[module_name]
        else:
            return None
    def get_plant_info(self, plant):
        if plant.capitalize() in self.plant_info:
            return self.plant_info[plant.capitalize()]
        else:
            return "I'm sorry, I don't have information about that plant. Can I help you with something else?"


    def handle_user_input(self, user_input):
        user_input = user_input.lower()
        if "hello" in user_input or "hi" in user_input:
            return self.greet()
        elif "bye" in user_input or "goodbye" in user_input:
            return self.say_goodbye()
        elif any(plant.lower() in user_input.split() for plant in self.plant_info.keys()):
            plant = next((plant for plant in self.plant_info.keys() if plant.lower() in user_input.split()), None)
            return self.get_plant_info(plant)
        elif "crops in tamilnadu" in user_input or "crops" in user_input:
            return self.get_crops_in_tamilnadu()
        elif any(module_name.lower() in user_input for module_name in self.modules.keys()):
            module_name = next((module_name for module_name in self.modules.keys() if module_name.lower() in user_input), None)
            if module_name:
                return f"For {module_name} module, visit: <a href='{self.get_module_url(module_name)}'>{self.get_module_url(module_name)}</a>"
            else:
                return "I'm sorry, I didn't understand that. Can you please rephrase or ask a different question?"
        elif "help" in user_input or "module" in user_input:
            return self.suggest_modules()
        else:
            return "I'm sorry, I didn't understand that. Can you please rephrase or ask a different question?"



assistant = GardeningAssistant()

@app.route('/chat', methods=['POST'])
@require_login
def chat():
    user_input = request.json.get('message')
    response = assistant.handle_user_input(user_input)
    return jsonify({'message': response})

@app.route('/aboutus')
@require_login
def aboutus():
    return render_template('about-us.html')


if __name__ == '__main__':
    create_tables()
    app.run(debug=False)
