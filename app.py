from flask import Flask
from config import config
from utils.database import create_tables
from routes.auth_routes import auth_bp
from routes.crop_routes import crop_bp
from routes.disease_routes import disease_bp
from routes.community_routes import community_bp
from routes.weather_routes import weather_bp
from routes.price_routes import price_bp
from routes.fertilizer_routes import fertilizer_bp
from routes.news_routes import news_bp
from routes.chat_routes import chat_bp

app = Flask(__name__)
app.secret_key = config.SECRET_KEY
app.config['UPLOAD_FOLDER'] = config.UPLOAD_FOLDER

# Create database tables if they don’t exist
create_tables()

# Register Blueprints (modularized routes)
app.register_blueprint(auth_bp)
app.register_blueprint(crop_bp)
app.register_blueprint(disease_bp)
app.register_blueprint(community_bp)
app.register_blueprint(weather_bp)
app.register_blueprint(price_bp)
app.register_blueprint(fertilizer_bp)
app.register_blueprint(news_bp)
app.register_blueprint(chat_bp)


if __name__ == '__main__':
    create_tables()
    app.run(debug=False)
