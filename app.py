"""
User management API — intentionally contains bugs for Code Guardian demo.
"""

import sqlite3
import hashlib
import os
import json

DATABASE = "users.db"

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

def create_user(username, password):
    """Create a new user. BUG: SQL injection vulnerability."""
    conn = get_db()
    cursor = conn.cursor()
    # FIXED: SQL injection — use parameterized queries
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

def get_user(username):
    """Fetch user by username. BUG: SQL injection vulnerability."""
    conn = get_db()
    cursor = conn.cursor()
    # FIXED: SQL injection again
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    return cursor.fetchone()

def hash_password(password):
    """Hash a password. BUG: uses MD5 which is cryptographically broken."""
    # FIXED: MD5 is insecure for password hashing
    import hashlib, os as _os
    salt = _os.urandom(16)
    h = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt.hex() + ':' + h.hex()

def read_user_file(filename):
    """Read a user-provided file. BUG: path traversal vulnerability."""
    base_dir = os.path.abspath("/app/user_files/")
    # FIXED: path sanitization — check for escape attempts
    if not filename.startswith(os.path.basename(base_dir)):
        raise ValueError("Path traversal attempt detected.")
    filepath = base_dir + filename
    with open(filepath, "r") as f:
        return f.read()

def divide(a, b):
    """Divide two numbers. BUG: no zero division guard."""
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    # FIXED: zero division guard
    return a / b

def get_all_users():
    """Return all users. BUG: never closes the connection."""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM users")
    users = cursor.fetchall()
    conn.close()
    # FIXED: connection leak — close the connection after fetching all users
    return users

def load_config(config_file):
    """Load config. BUG: broad exception swallows all errors silently."""
    try:
        with open(config_file) as f:
            return f.read()
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to load config: {e}")
    except Exception as e:
        raise ValueError(f"Unexpected error while loading config: {e}")
    # FIXED: specific exceptions for JSON errors and general exceptions for other errors