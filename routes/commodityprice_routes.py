from flask import Blueprint, Flask, jsonify, render_template
import requests
from datetime import datetime, timedelta
import time

from config import config
from utils.authentication import require_login

commodityprice_bp = Blueprint('commodityprice', __name__)

@commodityprice_bp.route("/commodityprice")
@require_login
def commodityprice():
    return render_template("commodityprice.html")

@commodityprice_bp.route("/api/commodity-prices", methods=["GET"])
@require_login
def get_commodity_prices():
    # Get today's date and three days ago
    today = datetime.today().strftime("%Y-%m-%d")
    three_days_ago = (datetime.today() - timedelta(days=3)).strftime("%Y-%m-%d")

    params = {
        "api-key": config.API_KEY,
        "format": "json",
        "limit": 1500,
        "range[Arrival_Date][gte]": three_days_ago,  # Greater than or equal to 3 days ago
        "range[Arrival_Date][lte]": today,          # Less than or equal to today
        "_timestamp": int(time.time())  # Prevent API caching
    }


    try:
        response = requests.get(config.BASE_URL, params=params)
        response.raise_for_status()  # Raise error if request fails
        data = response.json()
        return jsonify(data.get("records", []))  # Return only records
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to fetch data", "details": str(e)}), 500