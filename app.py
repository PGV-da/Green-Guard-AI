from config import config


import base64
import csv
import os
import random
import sqlite3
from functools import wraps

import bcrypt
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from flask import (Flask, flash, jsonify, redirect, render_template, request,
                   session, url_for)
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from statsmodels.tsa.arima.model import ARIMA
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img

from disease import disease_data
from fertilizer import fertilizer_dic

app = Flask(__name__)
app.secret_key = config.SECRET_KEY

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/mycrop')
@require_login
def mycrop():
    return render_template('mycrop.html')


@app.route('/chatassistant')
@require_login
def chatassistant():
    return render_template('chat-assistant.html')

@app.route('/aboutus')
@require_login
def aboutus():
    return render_template('about-us.html')


if __name__ == '__main__':
    create_tables()
    app.run(debug=False)
