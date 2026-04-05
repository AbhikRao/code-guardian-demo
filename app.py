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
    # Check if username already exists
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    if cursor.fetchone():  # FIXED: check if username already exists
        raise ValueError("Username already exists")
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
    if not result:  # FIXED: handle case where username is not found
        raise ValueError("Username not found")
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
    try:  # FIXED: handle case where file does not exist or cannot be read
        with open(filepath, "r") as f:
            return f.read()
    except FileNotFoundError:
        raise ValueError("File not found")
    except PermissionError:
        raise ValueError("Permission denied")

def divide(a, b):
    """Divide two numbers."""
    # FIXED: guard against zero division
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):  # FIXED: handle non-numeric input
        raise TypeError("Both inputs must be numbers")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def get_all_users():
    """Return all users."""
    conn = get_db()
    cursor = conn.cursor()
    try:  # FIXED: handle case where database query fails
        cursor.execute("SELECT username FROM users")
        result = cursor.fetchall()
        conn.close()  # FIXED: connection leak
        return result
    except sqlite3.Error as e:
        raise ValueError("Database query failed") from e

def load_config(config_file):
    """Load config."""
    try:
        with open(config_file) as f:
            return f.read()
    except FileNotFoundError:  # FIXED: handle case where config file does not exist
        raise ValueError("Config file not found")
    except PermissionError:  # FIXED: handle case where config file cannot be read
        raise ValueError("Permission denied")
    except Exception as e:  # FIXED: catch specific Exception instead of base Exception
        raise ValueError("Failed to load config") from e