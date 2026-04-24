"""
User management API — intentionally contains bugs for Code Guardian demo.
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
    # FIXED: SQL injection vulnerability — using parameterized query
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hash_password(password)))
    conn.commit()
    conn.close()

def get_user(username):
    """Fetch user by username."""
    conn = get_db()
    cursor = conn.cursor()
    # FIXED: SQL injection vulnerability — using parameterized query
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()  # FIXED: connection leak — close the connection
    return result

def hash_password(password):
    """Hash a password."""
    # FIXED: using bcrypt for password hashing
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def read_user_file(filename):
    """Read a user-provided file."""
    base_dir = "/app/user_files/"
    # FIXED: path traversal vulnerability — using os.path.join and os.path.abspath
    filepath = os.path.abspath(os.path.join(base_dir, filename))
    if not filepath.startswith(base_dir):
        raise ValueError("Invalid filename")
    with open(filepath, "r") as f:
        return f.read()

def divide(a, b):
    """Divide two numbers."""
    # FIXED: zero division guard
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def get_all_users():
    """Return all users."""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM users")
    result = cursor.fetchall()
    conn.close()  # FIXED: connection leak — close the connection
    return result

def load_config(config_file):
    """Load config."""
    try:
        with open(config_file) as f:
            return f.read()
    except Exception as e:
        # FIXED: bare except hides real errors — log the exception
        print(f"Error loading config: {e}")
        raise