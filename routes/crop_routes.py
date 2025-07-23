import pickle
import pandas as pd
import numpy as np
from flask import Blueprint, render_template, request

from utils.authentication import require_login

crop_bp = Blueprint('crop', __name__)

model = pickle.load(open('models/crop_recommendation/model.pkl','rb'))
sc = pickle.load(open('models/crop_recommendation/standscaler.pkl','rb'))
mx = pickle.load(open('models/crop_recommendation/minmaxscaler.pkl','rb'))

# Crop dictionary
crop_dict = {
    1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya",
    7: "Orange", 8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes",
    12: "Mango", 13: "Banana", 14: "Pomegranate", 15: "Lentil", 16: "Blackgram",
    17: "Mungbean", 18: "Mothbeans", 19: "Pigeonpeas", 20: "Kidneybeans",
    21: "Chickpea", 22: "Coffee"
}

@crop_bp.route('/crop-recommendation')
def crop_recommendation():
    return render_template("crop-prediction.html")

@crop_bp.route("/predict", methods=['POST'])
@require_login
def predict():
    """Handles the crop prediction form and displays results."""
    # Get form data to pass back to template
    form_data = {
        'nitrogen': request.form.get('Nitrogen', ''),
        'phosphorus': request.form.get('Phosporus', ''),
        'potassium': request.form.get('Potassium', ''),
        'temperature': request.form.get('Temperature', ''),
        'humidity': request.form.get('Humidity', ''),
        'ph': request.form.get('pH', ''),
        'rainfall': request.form.get('Rainfall', '')
    }
    
    try:
        # Get input values
        N = float(request.form['Nitrogen'])
        P = float(request.form['Phosporus'])
        K = float(request.form['Potassium'])
        temp = float(request.form['Temperature'])
        humidity = float(request.form['Humidity'])
        ph = float(request.form['pH'])
        rainfall = float(request.form['Rainfall'])

        # Prepare feature list
        feature_list = [N, P, K, temp, humidity, ph, rainfall]
        single_pred = np.array(feature_list).reshape(1, -1)

        # Apply transformations
        mx_features = mx.transform(single_pred)
        sc_mx_features = sc.transform(mx_features)

        # Make prediction
        prediction = model.predict(sc_mx_features)[0]
        crop = crop_dict.get(prediction, "Unknown Crop")

        result = f"{crop} is the best crop to be cultivated right there."
    except Exception as e:
        result = f"Error: {str(e)}"

    return render_template('crop-prediction.html', result=result, form_data=form_data)
    