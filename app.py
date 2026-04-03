"""
User management API — intentionally contains bugs for demo purposes.
"""

import sqlite3
import hashlib
import os

DATABASE = "users.db"

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

def create_user(username, password):
    """Create a new user. BUG: SQL injection vulnerability."""
    conn = get_db()
    cursor = conn.cursor()
    # BUG 1: SQL injection — user input directly in query string
    cursor.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')")
    conn.commit()
    conn.close()

def get_user(username):
    """Fetch user by username. BUG: SQL injection vulnerability."""
    conn = get_db()
    cursor = conn.cursor()
    # BUG 2: SQL injection again
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    return cursor.fetchone()

def hash_password(password):
    """Hash a password. BUG: uses MD5 which is cryptographically broken."""
    # BUG 3: MD5 is insecure for password hashing
    return hashlib.md5(password.encode()).hexdigest()

def read_user_file(filename):
    """Read a user-provided file. BUG: path traversal vulnerability."""
    # BUG 4: no path sanitization — attacker can pass ../../etc/passwd
    base_dir = "/app/user_files/"
    filepath = base_dir + filename
    with open(filepath, "r") as f:
        return f.read()

def divide(a, b):
    """Divide two numbers. BUG: no zero division guard."""
    # BUG 5: crashes if b is 0
    return a / b

def get_all_users():
    """Return all users. BUG: never closes the connection."""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM users")
    # BUG 6: connection leak — conn.close() never called
    return cursor.fetchall()

def load_config(config_file):
    """Load config. BUG: broad exception swallows all errors silently."""
    try:
        with open(config_file) as f:
            return f.read()
    except:
        # BUG 7: bare except hides real errors
        pass
