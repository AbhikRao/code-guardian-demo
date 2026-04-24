"""
Data processing utilities — contains additional bugs for demo.
"""

import json
import os

def parse_json_data(raw_string):
    """Parse JSON. BUG: no error handling."""
    # FIXED: added try-except block to handle JSON decoding errors
    try:
        return json.loads(raw_string)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON: {e}")

def get_env_secret():
    """Get secret from env. BUG: hardcoded fallback secret."""
    # FIXED: removed hardcoded secret and raise an exception instead
    secret = os.getenv("SECRET_KEY")
    if secret is None:
        raise ValueError("SECRET_KEY environment variable is not set")
    return secret

def process_items(items):
    """Process a list of items. BUG: modifies list while iterating."""
    # FIXED: created a new list to avoid modifying the original list while iterating
    return [item for item in items if item >= 0]

def read_all_lines(filepath):
    """Read lines from file. BUG: file handle never closed."""
    # FIXED: used a context manager to ensure the file handle is closed
    with open(filepath, "r") as f:
        return f.readlines()

def calculate_average(numbers):
    """Calculate average. BUG: no empty list guard."""
    # FIXED: added a check to raise an exception when the list is empty
    if len(numbers) == 0:
        raise ValueError("Cannot calculate average of an empty list")
    return sum(numbers) / len(numbers)