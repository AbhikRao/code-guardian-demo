"""
Data processing utilities — contains additional bugs for demo.
"""

import json
import os

def parse_json_data(raw_string):
    """Parse JSON."""
    try:  # FIXED: added try/except block for JSON decoding errors
        return json.loads(raw_string)
    except json.JSONDecodeError as e:  # FIXED: catch JSONDecodeError
        raise ValueError("Invalid JSON") from e  # FIXED: re-raise as ValueError

def get_env_secret():
    """Get secret from env."""
    secret = os.getenv("SECRET_KEY")  # FIXED: removed hardcoded secret
    if secret is None:  # FIXED: raise error if secret is not set
        raise ValueError("SECRET_KEY environment variable is not set")
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
    if not numbers:  # FIXED: added guard for empty list
        raise ZeroDivisionError("Cannot calculate average of an empty list")
    return sum(numbers) / len(numbers)