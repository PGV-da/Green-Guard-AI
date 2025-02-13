import pandas as pd
from flask import Blueprint, jsonify, render_template, request
from statsmodels.tsa.arima.model import ARIMA

from utils.authentication import require_login

price_bp = Blueprint('price', __name__)

@price_bp.route('/price')
@require_login
def price():
    return render_template('price.html')

@price_bp.route('/priceprediction')
@require_login
def price_prediction():
    """Renders the price prediction page."""
    return render_template('price-prediction.html')

@price_bp.route('/forecast', methods=['GET'])
@require_login
def forecast():
    """Forecasts crop prices using an ARIMA model."""
    selected_crop = request.args.get('crop')

    if not selected_crop:
        return jsonify({'error': 'No crop selected'}), 400

    try:
        # Load crop price data
        data = pd.read_csv(f'data/{selected_crop}.csv', header=None, names=['Date', 'Value'])
        data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m')
        data.set_index('Date', inplace=True)

        # Fit ARIMA model
        model = ARIMA(data['Value'], order=(1,1,1))  # Example order (p,d,q) - should be fine-tuned
        fit_model = model.fit()

        # Forecast for the next 4 months
        forecast = fit_model.forecast(steps=4)
        forecast_dates = pd.date_range(start=data.index[-1], periods=5, freq='M')[1:]

        return jsonify({
            'index': forecast_dates.strftime('%Y-%m-%d').tolist(),
            'values': forecast.tolist()
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500