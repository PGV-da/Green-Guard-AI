from flask import Blueprint, request, render_template
from services.crop_prediction import recommend_crop
import pandas as pd

crop_bp = Blueprint('crop', __name__)

@crop_bp.route('/cropprediction', methods=['GET', 'POST'])
def crop_prediction():
    recommended_crop = None

    if request.method == 'POST':
        attributes = {
            'N': float(request.form['N']),
            'P': float(request.form['P']),
            'K': float(request.form['K']),
            'Zn': float(request.form['Zn']),
            'Mg': float(request.form['Mg']),
            'S': float(request.form['S']),
            'pH': float(request.form['pH']),
            'Rainfall': float(request.form['Rainfall']),
            'Temperature': float(request.form['Temperature']),
            'Humidity': float(request.form['Humidity'])
        }

        recommended_crop = recommend_crop(attributes)

    return render_template('crop-prediction.html', recommended_crop=recommended_crop)