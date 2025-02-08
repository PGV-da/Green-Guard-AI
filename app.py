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


# Load the dataset
data = pd.read_csv('data/crop_data.csv')



# Select relevant columns for modeling
X = data[['N', 'P', 'K', 'Zn', 'Mg', 'S', 'pH', 'Rainfall', 'Temperature', 'Humidity']]
y = data['Crop_Subcategory']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

def recommend_crop(attributes):
    attribute_values = [list(attributes.values())]
    crop = rf_model.predict(attribute_values)[0]
    return crop
model = load_model('Mobile_net_plant_disease_model.h5')

def require_login(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if 'email' not in session:
            flash('You must be logged in to access this page', 'error')
            return redirect(url_for('login'))
        return view(**kwargs)
    return wrapped_view


class_indices = {
    0: 'Apple___alternaria_leaf_spot',
    1: 'Apple___black_rot',
    2: 'Apple___brown_spot',
    3: 'Apple___gray_spot',
    4: 'Apple___healthy',
    5: 'Apple___rust',
    6: 'Apple___scab',
    7: 'Bell_pepper___bacterial_spot',
    8: 'Bell_pepper___healthy',
    9: 'Blueberry___healthy',
    10: 'Cassava___bacterial_blight',
    11: 'Cassava___brown_streak_disease',
    12: 'Cassava___green_mottle',
    13: 'Cassava___healthy',
    14: 'Cassava___mosaic_disease',
    15: 'Cherry___healthy',
    16: 'Cherry___powdery_mildew',
    17: 'Corn___common_rust',
    18: 'Corn___gray_leaf_spot',
    19: 'Corn___healthy',
    20: 'Corn___northern_leaf_blight',
    21: 'Grape___black_measles',
    22: 'Grape___black_rot',
    23: 'Grape___healthy',
    24: 'Grape___isariopsis_leaf_spot',
    25: 'Grape_leaf_blight',
    26: 'Orange___citrus_greening',
    27: 'Peach___bacterial_spot',
    28: 'Peach___healthy',
    29: 'Potato___bacterial_wilt',
    30: 'Potato___early_blight',
    31: 'Potato___healthy',
    32: 'Potato___late_blight',
    33: 'Potato___nematode',
    34: 'Potato___pests',
    35: 'Potato___phytophthora',
    36: 'Potato___virus',
    37: 'Raspberry___healthy',
    38: 'Rice___bacterial_blight',
    39: 'Rice___blast',
    40: 'Rice___brown_spot',
    41: 'Rice___tungro',
    42: 'Soybean___healthy',
    43: 'Squash___powdery_mildew',
    44: 'Strawberry___healthy',
    45: 'Strawberry___leaf_scorch',
    46: 'Sugarcane___healthy',
    47: 'Sugarcane___mosaic',
    48: 'Sugarcane___red_rot',
    49: 'Sugarcane___rust',
    50: 'Sugarcane___yellow_leaf',
    51: 'Tomato___bacterial_spot',
    52: 'Tomato___early_blight',
    53: 'Tomato___healthy',
    54: 'Tomato___late_blight',
    55: 'Tomato___leaf_curl',
    56: 'Tomato___leaf_mold',
    57: 'Tomato___mosaic_virus',
    58: 'Tomato___septoria_leaf_spot',
    59: 'Tomato___spider_mites',
    60: 'Tomato___target_spot'
}

def predict_and_visualize(image_path):
    img = load_img(image_path, target_size=(224, 224))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array /= 255.0  # Normalize
    prediction = model.predict(img_array)[0]
    predicted_class_index = np.argmax(prediction)
    predicted_class = class_indices[predicted_class_index]
    confidence = prediction[predicted_class_index]
    return predicted_class, confidence


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        password = request.form['password']
        repeat_password = request.form['repeat_password']

        if not (first_name and last_name and email and password and repeat_password):
            flash('All fields are required', 'error')
            return render_template('register.html')

        if password != repeat_password:
            flash('Passwords do not match', 'error')
            return render_template('register.html')

        # Hash the password before storing
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        try:
            # Check if the email already exists
            cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
            existing_user = cursor.fetchone()
            if existing_user:
                flash('Email already exists', 'error')
                return render_template('register.html')

            # Insert the new user into the database
            cursor.execute('INSERT INTO users (first_name, last_name, phone_number, email, password) VALUES (?, ?, ?, ?, ?)',
                           (first_name, last_name, phone_number, email, hashed_password))
            conn.commit()
            flash('Account created successfully', 'success')
            return redirect(url_for('login'))

        except sqlite3.Error as e:
            flash('An error occurred while registering. Please try again.', 'error')
            print("Error:", e)

        finally:
            conn.close()

    return render_template('register.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if not (email and password):
            flash('Email and password are required', 'error')
            return render_template('login.html')

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Check if user exists
        cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
        user = cursor.fetchone()

        conn.close()

        if user and bcrypt.checkpw(password.encode('utf-8'), user[5].encode('utf-8')):
            session['email'] = email
            print("Login successful")
            # Redirect to some page after successful login
            return redirect(url_for('index'))
        else:
            flash('Invalid email or password', 'error')
            return render_template('login.html')

    return render_template('login.html')

@app.route('/community')
@require_login
def community():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM messages')
    messages = cursor.fetchall()
    conn.close()
    return render_template('community.html', messages=messages)
@require_login
@app.route('/send_message', methods=['POST'])
def send_message():
    if 'email' not in session:
        flash('You must be logged in to send a message', 'error')
        return redirect(url_for('login'))

    user_email = session['email']
    message_text = request.form['message']
    message_image = request.files['image'] if 'image' in request.files else None

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute('SELECT first_name FROM users WHERE email = ?', (user_email,))
    user_id = cursor.fetchone()[0]

    if message_image:
        image_blob = message_image.read()
        # Encode image data as Base64
        image_base64 = base64.b64encode(image_blob).decode('utf-8')
        cursor.execute('INSERT INTO messages (user_id, message, image) VALUES (?, ?, ?)',
                   (user_id, message_text, image_base64))
    else:
        cursor.execute('INSERT INTO messages (user_id, message) VALUES (?, ?)',
                   (user_id, message_text))
    conn.commit()
    conn.close()
    return redirect(url_for('community'))


@app.route('/predict', methods=['POST'])
@require_login
def predict():
    if 'file' not in request.files:
        return render_template('disease-detection.html', message='No file part')
    
    file = request.files['file']
    
    if file.filename == '':
        return render_template('disease-detection.html', message='No selected file')
    
    if file:
        # Create the 'uploads' directory if it doesn't exist
        if not os.path.exists('static/uploads'):
            os.makedirs('static/uploads')
        
        # Save the uploaded file
        file_path = os.path.join('static/uploads/', file.filename)
        file.save(file_path)
        
        # Verify that the image file exists
        if not os.path.exists(file_path):
            return render_template('disease-detection.html', message='Uploaded file does not exist')
        
        # Predict the uploaded image
        predicted_class, confidence = predict_and_visualize(file_path)
        check=False
        if confidence<0.7000000:
            check=True
        
        # Get disease data
        disease_info = disease_data.get(predicted_class, {'symptoms': 'Unknown', 'solution': 'Unknown'})
        
        # Pass the file path, predicted class, confidence, and disease info to the result template
        return render_template('disease-detection.html', image_file=file_path, predicted_class=predicted_class, confidence=confidence,check=check, symptoms=disease_info['symptoms'], solution=disease_info['solution'])

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

@app.route('/diseasedetection')
@require_login
def diseasedetection():
    return render_template('disease-detection.html')

@app.route('/cropprediction', methods=['GET', 'POST'])
@require_login
def cropprediction():
    recommended_crop = None

    if request.method == 'POST':
        lat = request.form['lat']
        lon = request.form['lon']
        # Fetch weather data from OpenWeather API
        weather_data = fetch_weather_data(lat, lon)

        # Use default values if data is not available
        temperature = weather_data.get('main', {}).get('temp')
        rainfall = weather_data.get('rain', {}).get('1h')
        humidity = weather_data.get('main', {}).get('humidity')

        # Check if temperature, rainfall, and humidity are not None before converting to float
        temperature = float(temperature) if temperature is not None else 0.0
        rainfall = float(rainfall) if rainfall is not None else 0.0
        humidity = float(humidity) if humidity is not None else 0.0

        # Get input attributes from the form
        attributes = {
            'N': float(request.form['N']),
            'P': float(request.form['P']),
            'K': float(request.form['K']),
            'Zn': float(request.form['Zn']),
            'Mg': float(request.form['Mg']),
            'S': float(request.form['S']),
            'pH': float(request.form['pH']),
            'Rainfall': rainfall,
            'Temperature': temperature,
            'Humidity': humidity
        }

        # Recommend crop
        recommended_crop = recommend_crop(attributes)

        return render_template('crop-prediction.html', recommended_crop=recommended_crop)
    return render_template('crop-prediction.html', recommended_crop=None)

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
