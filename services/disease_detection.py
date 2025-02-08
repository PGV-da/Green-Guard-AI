import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from config import config

# Load pre-trained model
model = load_model(config.MODEL_PATH)

# Class indices for disease classification
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
    """Runs the trained model on the given image and returns the predicted disease."""
    img = load_img(image_path, target_size=(224, 224))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array /= 255.0  # Normalize

    prediction = model.predict(img_array)[0]
    predicted_class_index = np.argmax(prediction)
    predicted_class = class_indices[predicted_class_index]
    confidence = prediction[predicted_class_index]

    return predicted_class, confidence