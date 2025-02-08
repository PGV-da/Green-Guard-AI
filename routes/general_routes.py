from flask import Blueprint, render_template
from utils.authentication import require_login

general_bp = Blueprint('general', __name__)

@general_bp.route('/index')
def index():
    """Renders the homepage."""
    return render_template('index.html')

@general_bp.route('/mycrop')
@require_login
def mycrop():
    """Renders the My Crop page."""
    return render_template('mycrop.html')

@general_bp.route('/aboutus')
@require_login
def aboutus():
    """Renders the About Us page."""
    return render_template('about-us.html')
