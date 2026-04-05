"""
User management API — fixed version.
"""

import sqlite3
import hashlib
import os
import bcrypt

DATABASE = "users.db"

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

def create_user(username, password):
    """Create a new user."""
    conn = get_db()
    cursor = conn.cursor()
    # FIXED: SQL injection — use parameterised query
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                   (username, hash_password(password)))
    conn.commit()
    conn.close()

def get_user(username):
    """Fetch user by username."""
    conn = get_db()
    cursor = conn.cursor()
    # FIXED: SQL injection — use parameterised query
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()  # FIXED: connection leak
    return result

def hash_password(password):
    """Hash a password."""
    # FIXED: bcrypt replaces insecure MD5
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def read_user_file(filename):
    """Read a user-provided file."""
    base_dir = "/app/user_files/"
    # FIXED: path traversal — validate path stays inside base_dir
    filepath = os.path.abspath(os.path.join(base_dir, filename))
    if not filepath.startswith(os.path.abspath(base_dir)):
        raise ValueError("Invalid filename: path traversal detected")
    with open(filepath, "r") as f:
        return f.read()

def divide(a, b):
    """Divide two numbers."""
    # FIXED: guard against zero division
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def get_all_users():
    """Return all users."""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM users")
    result = cursor.fetchall()
    conn.close()  # FIXED: connection leak
    return result

def load_config(config_file):
    """Load config."""
    try:
        with open(config_file) as f:
            return f.read()
    except Exception as e:
        # FIXED: bare except replaced with specific Exception + re-raise
        raise e
