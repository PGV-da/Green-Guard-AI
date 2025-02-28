import csv
import pickle
import pandas as pd

from flask import Blueprint, render_template, url_for, request

from resources.fertilizer import fertilizer_details, fertilizer_images
from utils.authentication import require_login
from config import config

fertilizer_bp = Blueprint('fertilizer', __name__)

with open(config.FERTILIZER_MODEL_PATH, "rb") as model_file:
    model = pickle.load(model_file)

with open(config.TRANSFORMER_PATH, "rb") as transformer_file:
    transformer = pickle.load(transformer_file)

@fertilizer_bp.route('/fertilizer-recommendation')
@require_login
def fertilizer_recommendation():
    """Displays the fertilizer recommendation page."""
    return render_template('fertilizer-recommendation.html', fertilizer=None)

@fertilizer_bp.route('/recommend', methods=['POST'])
@require_login
def recommend():
    """Processes user input and recommends fertilizers based on soil conditions."""
    try:
        # Retrieve form data
        form_data = request.form

        # Create input dictionary matching the dataset column names
        input_data = {
            "Soil_color": form_data["Soil_color"],
            "Nitrogen": float(form_data["Nitrogen"]),
            "Phosphorus": float(form_data["Phosphorus"]),
            "Potassium": float(form_data["Potassium"]),
            "pH": float(form_data["pH"]),
            "Rainfall": float(form_data["Rainfall"]),
            "Temperature": float(form_data["Temperature"]),
            "Crop": form_data["Crop"]
        }

        # Convert to DataFrame
        input_df = pd.DataFrame([input_data])

        # Transform the data using the loaded transformer
        transformed_input = transformer.transform(input_df)

        # Make a prediction
        prediction = model.predict(transformed_input)
        fertilizer_name = prediction[0]
        
        # Fetch fertilizer details
        details = fertilizer_details.get(fertilizer_name, {
            "description": "Description not available.",
            "uses": "Uses not available.",
            "when_to_use": "Timing not available.",
            "amount": "Amount not available.",
            "tips": "Application tips not available."
        })
        image = fertilizer_images.get(fertilizer_name, "default.png")  # Use default image if not found
        image_url = url_for('static', filename=f"images/fertilizer_images/{image}")

        return render_template(
        "fertilizer_result.html",
        fertilizer_name=fertilizer_name,
        description=details["description"],
        uses=details["uses"],
        when_to_use=details["when_to_use"],
        amount=details["amount"],
        tips=details["tips"],
        image_url=image_url
    )

    except Exception as e:
        return f"Error during prediction: {e}"