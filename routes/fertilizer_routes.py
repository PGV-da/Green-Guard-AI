import csv

from flask import Blueprint, render_template, request

from resources.fertilizer import fertilizer_dic
from utils.authentication import require_login

fertilizer_bp = Blueprint('fertilizer', __name__)

def read_csv():
    """Reads crop data from a CSV file and stores it in a dictionary."""
    crops_data = {}
    with open('data/crop_data.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            crop_name = row['Crop_Subcategory']
            crop_values = {key: tuple(map(float, value.split('-'))) if '-' in value else (float(value), float(value))
                           for key, value in row.items() if key != 'Crop_Subcategory'}
            crops_data[crop_name] = crop_values
    return crops_data

@fertilizer_bp.route('/fertilizer-recommendation')
@require_login
def fertilizer_recommendation():
    """Displays the fertilizer recommendation page."""
    return render_template('fertilizer-recommendation.html', fertilizer=None)

@fertilizer_bp.route('/recommend', methods=['POST'])
@require_login
def recommend():
    """Processes user input and recommends fertilizers based on soil conditions."""
    crops_data = read_csv()
    selected_crop = request.form.get('crop', '')

    # Validate crop selection
    if selected_crop not in crops_data:
        return render_template('fertilizer-recommendation.html', fertilizer="Crop not found in database.")

    try:
        n, p, k, zn, mg, s = map(float, [request.form['N'], request.form['P'], request.form['K'],
                                         request.form['Zn'], request.form['Mg'], request.form['S']])
    except ValueError:
        return render_template('fertilizer-recommendation.html', fertilizer="Invalid input. Please enter numbers.")

    attributes = {'N': n, 'P': p, 'K': k, 'Zn': zn, 'Mg': mg, 'S': s}

    for attribute, recommendation in fertilizer_dic.items():
        condition = crops_data[selected_crop]
        if attribute in attributes and condition[attribute][0] <= attributes[attribute] <= condition[attribute][1]:
            return render_template('fertilizer-recommendation.html', fertilizer=recommendation)

    return render_template('fertilizer-recommendation.html', fertilizer='No recommendation found.')
