import base64
from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from utils.database import get_db_connection
from utils.authentication import require_login

community_bp = Blueprint('community', __name__)

@community_bp.route('/community')
@require_login
def community():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT users.first_name, messages.message, messages.image FROM messages '
                   'JOIN users ON users.id = messages.user_id')
    messages = cursor.fetchall()
    conn.close()

    # Decode images for rendering
    for i, msg in enumerate(messages):
        if msg["image"]:
            messages[i] = (msg["first_name"], msg["message"], base64.b64encode(msg["image"]).decode('utf-8'))
        else:
            messages[i] = (msg["first_name"], msg["message"], None)

    return render_template('community.html', messages=messages)

@require_login
@app.route('/send_message', methods=['POST'])
def send_message():
    user_email = session.get('email')
    message_text = request.form.get('message')
    message_image = request.files.get('image')

    if not user_email:
        flash('You must be logged in to send a message.', 'error')
        return redirect(url_for('auth.login'))

    conn = get_db_connection()
    cursor = conn.cursor()()

    cursor.execute('SELECT id FROM users WHERE email = ?', (user_email,))
    user = cursor.fetchone()

    if not user:
        flash('User not found.', 'error')
        return redirect(url_for('auth.login'))

    user_id = user['id']
    image_blob = message_image.read() if message_image else None

    cursor.execute('INSERT INTO messages (user_id, message, image) VALUES (?, ?, ?)',
                   (user_id, message_text, image_blob))
    conn.commit()
    conn.close()

    flash('Message sent successfully!', 'success')
    return redirect(url_for('community.community'))