from functools import wraps

import bcrypt
from flask import flash, redirect, session, url_for


def hash_password(password):
    """Hashes a password using bcrypt."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def check_password(password, hashed_password):
    """Verifies a password against its hashed version."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def require_login(view):
    """Decorator to protect routes that require authentication."""
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if 'email' not in session:
            flash('You must be logged in to access this page', 'error')
            return redirect(url_for('auth.login'))
        return view(*args, **kwargs)
    return wrapped_view
