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
    if secret is None or secret == "":  # FIXED: handle empty SECRET_KEY
        raise ValueError("SECRET_KEY environment variable is not set or is empty")
    return secret

def process_items(items):
    """Return items with negatives removed."""
    if not isinstance(items, list):  # FIXED: check if input is a list
        raise ValueError("Input must be a list")
    # FIXED: list comprehension avoids mutating list during iteration
    return [item for item in items if item >= 0]

def read_all_lines(filepath):
    """Read lines from file using context manager."""
    try:
        # FIXED: context manager ensures file is always closed
        with open(filepath, "r") as f:
            return f.readlines()
    except FileNotFoundError:  # FIXED: handle file not found
        raise ValueError(f"File {filepath} not found")
    except PermissionError:  # FIXED: handle permission error
        raise ValueError(f"Permission denied to read file {filepath}")

def calculate_average(numbers):
    """Calculate average with empty list guard."""
    if not isinstance(numbers, list):  # FIXED: check if input is a list
        raise ValueError("Input must be a list")
    if not numbers:
        # FIXED: raise ValueError instead of crashing with ZeroDivisionError
        raise ValueError("Cannot calculate average of an empty list")
    if not all(isinstance(x, (int, float)) for x in numbers):  # FIXED: check for non-numeric values
        raise ValueError("List must only contain numeric values")
    return sum(numbers) / len(numbers)