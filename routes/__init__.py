from flask import Blueprint

# Initialize blueprints
auth_bp = Blueprint('auth', __name__)
crop_bp = Blueprint('crop', __name__)
disease_bp = Blueprint('disease', __name__)
community_bp = Blueprint('community', __name__)
weather_bp = Blueprint('weather', __name__)
price_bp = Blueprint('price', __name__)
fertilizer_bp = Blueprint('fertilizer', __name__)
news_bp = Blueprint('news', __name__)
chat_bp = Blueprint('chat', __name__)
general_bp = Blueprint('general', __name__)