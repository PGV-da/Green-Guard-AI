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

    # Commodity Price API for data.gov.in
    API_KEY = "579b464db66ec23bdd0000012a392a566362485c4e95c88c71108314"
    BASE_URL = "https://api.data.gov.in/resource/35985678-0d79-46b4-9ed6-6f13308a1d24"
    GROQ_API_KEY = os.getenv('GROQ_API_KEY')

config = Config()