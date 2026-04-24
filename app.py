"""
User management API — fixed version.
"""

import psycopg2  # FIXED: sqlite3 replaced with more secure postgresql
import hashlib
import os
import bcrypt

DATABASE = "users.db"

def get_db():
    conn = psycopg2.connect(
        dbname="users",
        user="username",
        password="password",
        host="localhost"
    )  # FIXED: connection details for postgresql
    return conn

def create_user(username, password):
    """Create a new user."""
    try:  # FIXED: added try-except block for database connection and query errors
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)",
                       (username, hash_password(password)))
        conn.commit()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)  # FIXED: handle potential database connection or query errors
        conn.close()

def get_user(username):
    """Fetch user by username."""
    try:  # FIXED: added try-except block for database connection and query errors
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()
        conn.close()
        return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)  # FIXED: handle potential database connection or query errors
        conn.close()

def hash_password(password):
    """Hash a password."""
    try:  # FIXED: added try-except block for bcrypt errors
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    except Exception as e:
        print(e)  # FIXED: handle potential bcrypt errors

def read_user_file(filename):
    """Read a user-provided file."""
    base_dir = "/app/user_files/"
    filepath = os.path.abspath(os.path.join(base_dir, filename))
    if not filepath.startswith(os.path.abspath(base_dir)):
        raise ValueError("Invalid filename: path traversal detected")
    try:  # FIXED: added try-except block for file read errors
        with open(filepath, "r") as f:
            return f.read()
    except FileNotFoundError:
        print("File not found")  # FIXED: handle potential file read errors
    except Exception as e:
        print(e)

def divide(a, b):
    """Divide two numbers."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):  # FIXED: added type check
        raise TypeError("Both inputs must be numbers")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def get_all_users():
    """Return all users."""
    try:  # FIXED: added try-except block for database connection and query errors
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM users")
        result = cursor.fetchall()
        conn.close()
        return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)  # FIXED: handle potential database connection or query errors
        conn.close()

def load_config(config_file):
    """Load config."""
    try:
        with open(config_file) as f:
            return f.read()
    except FileNotFoundError:
        print("Config file not found")  # FIXED: handle potential file read errors
    except Exception as e:
        raise e