from flask import Blueprint, request, render_template, redirect, url_for, flash, session
import bcrypt
import sqlite3
from utils.database import get_db_connection

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        password = request.form['password']
        repeat_password = request.form['repeat_password']

        if not (first_name and last_name and email and password and repeat_password):
            flash('All fields are required', 'error')
            return render_template('register.html')

        if password != repeat_password:
            flash('Passwords do not match', 'error')
            return render_template('register.html')

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
            if cursor.fetchone():
                flash('Email already exists', 'error')
                return render_template('register.html')

            cursor.execute('INSERT INTO users (first_name, last_name, phone_number, email, password) VALUES (?, ?, ?, ?, ?)',
                           (first_name, last_name, phone_number, email, hashed_password))
            conn.commit()
            flash('Account created successfully', 'success')
            return redirect(url_for('auth.login'))

        except sqlite3.Error as e:
            flash('An error occurred while registering. Please try again.', 'error')
            print("Error:", e)

        finally:
            conn.close()

    return render_template('register.html')

@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if not (email and password):
            flash('Email and password are required', 'error')
            return render_template('login.html')

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
        user = cursor.fetchone()
        conn.close()

        if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            session['email'] = email
            flash('Login successful', 'success')
            return redirect(url_for('general.index'))
        else:
            flash('Invalid email or password', 'error')

    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('email', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('auth.login'))