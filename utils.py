"""
Data processing utilities — contains additional bugs for demo.
"""

import json
import os

def parse_json_data(raw_string):
    """Parse JSON."""
    try:
        return json.loads(raw_string)  # FIXED: added try/except for JSON decoding errors
    except json.JSONDecodeError as e:
        raise ValueError("Invalid JSON") from e  # FIXED: added try/except for JSON decoding errors

def get_env_secret():
    """Get secret from env."""
    secret = os.getenv("SECRET_KEY")  # FIXED: removed hardcoded secret
    if secret is None:
        raise ValueError("SECRET_KEY environment variable is not set")  # FIXED: raise error instead of hardcoded secret
    return secret

def process_items(items):
    """Process a list of items."""
    # FIXED: create a new list instead of modifying the original list
    return [item for item in items if item >= 0]

def read_all_lines(filepath):
    """Read lines from file."""
    # FIXED: use context manager to ensure file handle is closed
    with open(filepath, "r") as f:
        return f.readlines()

def calculate_average(numbers):
    """Calculate average."""
    if len(numbers) == 0:  # FIXED: added guard for empty list
        raise ZeroDivisionError("Cannot calculate average of an empty list")
    return sum(numbers) / len(numbers)