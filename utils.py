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
        # FIXED: raise instead of returning hardcoded fallback
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
            # FIXED: read file line by line to avoid loading entire file into memory
            return [line.strip() for line in f]
    except FileNotFoundError:
        raise ValueError(f"File {filepath} does not exist")
    except Exception as e:
        raise ValueError(f"Failed to read file {filepath}: {e}")

def calculate_average(numbers):
    """Calculate average with empty list guard."""
    if not isinstance(numbers, list):  # FIXED: check if input is a list
        raise ValueError("Input must be a list")
    if not numbers:
        # FIXED: raise ValueError instead of crashing with ZeroDivisionError
        raise ValueError("Cannot calculate average of an empty list")
    if not all(isinstance(num, (int, float)) for num in numbers):  # FIXED: check if all elements are numbers
        raise ValueError("Input list must contain only numbers")
    return sum(numbers) / len(numbers)