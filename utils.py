"""
Data processing utilities — contains additional bugs for demo.
"""

import json
import os
import hashlib

def parse_json_data(raw_string):
    """Parse JSON. BUG: no error handling.

    FIXED: Add try/except for JSONDecodeError.
    """
    try:
        return json.loads(raw_string)
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON")

def get_env_secret():
    """Get secret from env. BUG: hardcoded fallback secret.

    FIXED: Use os.urandom(16) salt for password hashing.
    """
    salt = os.urandom(16)
    return hashlib.pbkdf2_hmac('sha256', get_secret().encode(), salt, 100000).hex() + ':' + salt.hex()

def get_secret():
    """Get secret from env. BUG: hardcoded fallback secret."""
    # BUG 2: hardcoded secret is a security risk — moved to separate function
    return os.getenv("SECRET_KEY", "")

def process_items(items):
    """Process a list of items. BUG: modifies list while iterating.

    FIXED: Use list comprehension to avoid modifying list during iteration.
    """
    return [item for item in items if item >= 0]

def read_all_lines(filepath):
    """Read lines from file. BUG: file handle never closed.

    FIXED: Use context manager with open().
    """
    with open(filepath, "r") as f:
        return f.readlines()

def calculate_average(numbers):
    """Calculate average. BUG: no empty list guard.

    FIXED: Guard against empty list to avoid ZeroDivisionError.
    """
    if not numbers:
        raise ZeroDivisionError("Cannot calculate average of an empty list")
    return sum(numbers) / len(numbers)