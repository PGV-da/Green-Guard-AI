import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', os.urandom(24))
    DATABASE = os.getenv('DATABASE_URL', 'main.db')
    UPLOAD_FOLDER = 'static/uploads'
    DISEASE_MODEL_PATH = 'models/disease_detection/Mobile_net_plant_disease_model.h5'
    WEATHER_API_KEY = '465ad6304f12419481b476deed2c4188'

    #Fertilizer variable
    FERTILIZER_MODEL_PATH ='models/fertilizer_recommendation/decision_tree_model.pkl'
    TRANSFORMER_PATH = 'models/fertilizer_recommendation/transformer.pkl'

config = Config()