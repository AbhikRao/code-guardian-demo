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
    """Create a new user."""
    conn = get_db()
    cursor = conn.cursor()
    # FIXED: SQL injection vulnerability due to user input directly in query string
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hash_password(password)))
    conn.commit()
    conn.close()

def get_user(username):
    """Fetch user by username."""
    conn = get_db()
    cursor = conn.cursor()
    # FIXED: SQL injection vulnerability due to user input directly in query string
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()  # FIXED: connection leak due to unclosed database connection
    return result

def hash_password(password):
    """Hash a password."""
    # FIXED: uses MD5 which is cryptographically broken
    salt = os.urandom(16)
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt.hex() + ':' + hashed.hex()

def read_user_file(filename):
    """Read a user-provided file."""
    base_dir = "/app/user_files/"
    # FIXED: path traversal vulnerability due to lack of path sanitization
    filepath = os.path.abspath(base_dir + filename)
    if not filepath.startswith(os.path.abspath(base_dir)):
        raise ValueError("Invalid filename")
    with open(filepath, "r") as f:
        return f.read()

def divide(a, b):
    """Divide two numbers."""
    # FIXED: division by zero error due to lack of zero division guard
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def get_all_users():
    """Return all users."""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM users")
    result = cursor.fetchall()
    conn.close()  # FIXED: connection leak due to unclosed database connection
    return result

def load_config(config_file):
    """Load config."""
    try:
        with open(config_file) as f:
            return json.load(f)  # FIXED: use json.load to parse JSON
    except json.JSONDecodeError as e:
        # FIXED: bare except hides real errors
        print(f"Error loading config: {e}")
    except Exception as e:
        # FIXED: bare except hides real errors
        print(f"An error occurred: {e}")