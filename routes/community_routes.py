import base64
from datetime import datetime

from flask import (Blueprint, flash, redirect, render_template, request,
                   session, url_for)

from utils.authentication import require_login
from utils.database import get_db_connection

community_bp = Blueprint('community', __name__)

@community_bp.route('/community')
@require_login
def community():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT users.first_name, messages.message, messages.image, messages.created_at FROM messages '
                   'JOIN users ON users.id = messages.user_id ORDER BY messages.created_at ASC')
    messages = cursor.fetchall()
    conn.close()

    formatted_messages = []

    for msg in messages:
        image_b64 = base64.b64encode(msg["image"]).decode('utf-8') if msg["image"] else None
        
        # Format timestamp
        timestamp = msg["created_at"] if msg["created_at"] else None
        formatted_timestamp = None
        if timestamp:
            try:
                # Parse the timestamp and format it nicely
                dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
                formatted_timestamp = dt.strftime('%b %d, %H:%M')
            except:
                formatted_timestamp = timestamp
        
        formatted_messages.append({
            "name": msg["first_name"],
            "message": msg["message"],
            "image": image_b64,
            "created_at": formatted_timestamp
        })

    return render_template('community.html', messages=formatted_messages)

@community_bp.route('/send_message', methods=['POST'])
@require_login
def send_message():
    user_email = session.get('email')
    message_text = request.form.get('message')
    message_image = request.files.get('image')

    if not user_email:
        flash('You must be logged in to send a message.', 'error')
        return redirect(url_for('auth.login'))

    conn = get_db_connection()
    cursor = conn.cursor()

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