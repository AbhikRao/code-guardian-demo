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
    # FIXED: SQL injection — use parameterised queries
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

def get_user(username):
    """Fetch user by username. BUG: SQL injection vulnerability."""
    conn = get_db()
    cursor = conn.cursor()
    # FIXED: SQL injection again — use parameterised queries
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
    base_dir = "/app/user_files/"
    # FIXED: path traversal — use os.path.abspath() + startswith() check
    filepath = os.path.abspath(base_dir + filename)
    if not filepath.startswith(base_dir):
        raise ValueError("File path traversal attempt detected.")
    with open(filepath, "r") as f:
        return f.read()

def divide(a, b):
    """Divide two numbers. BUG: no zero division guard."""
    # FIXED: division by zero
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def get_all_users():
    """Return all users. BUG: never closes the connection."""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM users")
    # FIXED: connection leak — use context manager
    with conn:
        return cursor.fetchall()

def load_config(config_file):
    """Load config. BUG: broad exception swallows all errors silently."""
    try:
        with open(config_file) as f:
            return f.read()
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to load config file: {e}")
    except Exception as e:
        raise ValueError(f"Unexpected error while loading config file: {e}")