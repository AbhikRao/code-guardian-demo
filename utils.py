"""
Data processing utilities — contains additional bugs for demo.
"""

import json
import os

def parse_json_data(raw_string):
    """Parse JSON. BUG: no error handling."""
    try:
        # FIXED: added error handling for JSON decoding errors
        return json.loads(raw_string)
    except json.JSONDecodeError as e:
        # FIXED: added error handling for JSON decoding errors
        raise ValueError(f"Invalid JSON: {e}") from e

def get_env_secret():
    """Get secret from env. BUG: hardcoded fallback secret."""
    # FIXED: removed hardcoded secret to prevent security risk
    secret = os.getenv("SECRET_KEY")
    if secret is None:
        # FIXED: raise an error instead of using a hardcoded secret
        raise ValueError("SECRET_KEY environment variable is not set")
    return secret

def process_items(items):
    """Process a list of items. BUG: modifies list while iterating."""
    # FIXED: create a new list to avoid modifying the original list during iteration
    return [item for item in items if item >= 0]

def read_all_lines(filepath):
    """Read lines from file. BUG: file handle never closed."""
    # FIXED: use a context manager to ensure the file is closed after reading
    with open(filepath, "r") as f:
        return f.readlines()

def calculate_average(numbers):
    """Calculate average. BUG: no empty list guard."""
    # FIXED: check for an empty list to prevent ZeroDivisionError
    if len(numbers) == 0:
        # FIXED: raise an error instead of attempting to calculate the average of an empty list
        raise ValueError("Cannot calculate average of an empty list")
    return sum(numbers) / len(numbers)