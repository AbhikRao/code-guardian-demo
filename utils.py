"""
Data processing utilities — fixed version.
"""

import json
import os

def parse_json_data(raw_string):
    """Parse JSON with proper error handling."""
    try:
        return json.loads(raw_string)
    except json.JSONDecodeError as e:
        # FIXED: raise ValueError instead of crashing with unhandled exception
        raise ValueError(f"Invalid JSON: {e}")

def get_env_secret():
    """Get secret from env — no hardcoded fallback."""
    secret = os.getenv("SECRET_KEY")
    if secret is None:
        # FIXED: raise instead of returning hardcoded fallback
        raise ValueError("SECRET_KEY environment variable is not set")
    return secret

def process_items(items):
    """Return items with negatives removed."""
    # FIXED: list comprehension avoids mutating list during iteration
    return [item for item in items if item >= 0]

def read_all_lines(filepath):
    """Read lines from file using context manager."""
    # FIXED: context manager ensures file is always closed
    with open(filepath, "r") as f:
        return f.readlines()

def calculate_average(numbers):
    """Calculate average with empty list guard."""
    if not numbers:
        # FIXED: raise ValueError instead of crashing with ZeroDivisionError
        raise ValueError("Cannot calculate average of an empty list")
    return sum(numbers) / len(numbers)
