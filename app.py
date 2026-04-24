"""
User management API — fixed version.
"""

import sqlite3
import os
import bcrypt

DATABASE = "users.db"

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

def create_user(username, password):
    """Create a new user."""
    try:  # FIXED: handle potential database connection or query errors
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                       (username, hash_password(password)))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:  # FIXED: handle potential database connection or query errors
        raise Exception(f"Failed to create user: {e}")

def get_user(username):
    """Fetch user by username."""
    try:  # FIXED: handle potential database connection or query errors
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
        conn.close()
        return result
    except sqlite3.Error as e:  # FIXED: handle potential database connection or query errors
        raise Exception(f"Failed to get user: {e}")

def hash_password(password):
    """Hash a password."""
    try:  # FIXED: handle potential bcrypt errors
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    except Exception as e:  # FIXED: handle potential bcrypt errors
        raise Exception(f"Failed to hash password: {e}")

def read_user_file(filename):
    """Read a user-provided file."""
    base_dir = "/app/user_files/"
    filepath = os.path.abspath(os.path.join(base_dir, filename))
    if not filepath.startswith(os.path.abspath(base_dir)):
        raise ValueError("Invalid filename: path traversal detected")
    try:  # FIXED: handle potential file read errors
        with open(filepath, "r") as f:
            return f.read()
    except OSError as e:  # FIXED: handle potential file read errors
        raise Exception(f"Failed to read file: {e}")

def divide(a, b):
    """Divide two numbers."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):  # FIXED: handle non-numeric input
        raise TypeError("Both inputs must be numbers")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def get_all_users():
    """Return all users."""
    try:  # FIXED: handle potential database connection or query errors
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM users")
        result = cursor.fetchall()
        conn.close()
        return result
    except sqlite3.Error as e:  # FIXED: handle potential database connection or query errors
        raise Exception(f"Failed to get all users: {e}")

def load_config(config_file):
    """Load config."""
    try:
        with open(config_file) as f:
            return f.read()
    except OSError as e:  # FIXED: handle potential file read errors specifically
        raise Exception(f"Failed to load config: {e}")