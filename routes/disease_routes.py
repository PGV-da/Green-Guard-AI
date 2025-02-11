import os
from flask import Blueprint, request, render_template
from services.disease_detection import predict_and_visualize
from resources.disease import disease_data
from config import config
from utils.authentication import require_login

disease_bp = Blueprint('disease', __name__)

@disease_bp.route('/diseasedetection')
@require_login
def diseasedetection():
    return render_template('disease-detection.html')

@disease_bp.route('/predict', methods=['POST'])
@require_login
def predict():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('disease-detection.html', message='No file uploaded')

        file = request.files['file']

        if file.filename == '':
            return render_template('disease-detection.html', message='No file selected')

        if file:
            # Ensure the upload directory exists
            if not os.path.exists(config.UPLOAD_FOLDER):
                os.makedirs(config.UPLOAD_FOLDER)

            file_path = os.path.join(config.UPLOAD_FOLDER, file.filename)
            file.save(file_path)

            # Ensure the image exists before processing
            if not os.path.exists(file_path):
                return render_template('disease-detection.html', message='Error saving file')

            # Predict disease
            predicted_class, confidence = predict_and_visualize(file_path)
            check = confidence < 0.7  # If confidence is low, consider re-evaluating

            # Fetch disease details
            disease_info = disease_data.get(predicted_class, {'symptoms': 'Unknown', 'solution': 'Unknown'})

            return render_template('disease-detection.html', image_file=file_path,
                                   predicted_class=predicted_class, confidence=confidence,
                                   check=check, symptoms=disease_info['symptoms'],
                                   solution=disease_info['solution'])

    return render_template('disease-detection.html')