import pandas as pd
from flask import Blueprint, render_template, request

from services.crop_prediction import recommend_crop
from utils.authentication import require_login

crop_bp = Blueprint('crop', __name__)

@crop_bp.route('/cropprediction', methods=['GET', 'POST'])
@require_login
def crop_prediction():
    """Handles the crop prediction form and displays results."""
    recommended_crop = None

    if request.method == 'POST':
        try:
            attributes = {
                'N': float(request.form.get('N', 0)),  # Default to 0 if missing
                'P': float(request.form.get('P', 0)),
                'K': float(request.form.get('K', 0)),
                'Zn': float(request.form.get('Zn', 0)),
                'Mg': float(request.form.get('Mg', 0)),
                'S': float(request.form.get('S', 0)),
                'pH': float(request.form.get('pH', 7.0)),  # Default to neutral pH
                'Rainfall': float(request.form.get('Rainfall', 0)),
                'Temperature': float(request.form.get('Temperature', 25.0)),  # Default reasonable values
                'Humidity': float(request.form.get('Humidity', 50.0))
            }
            recommended_crop = recommend_crop(attributes)
        except (TypeError, ValueError):
            return render_template('crop-prediction.html', error="Invalid input values. Please enter numbers only.")

    return render_template('crop-prediction.html', recommended_crop=recommended_crop)