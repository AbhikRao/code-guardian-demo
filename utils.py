"""
Data processing utilities — contains additional bugs for demo.
"""

import json
import os

def parse_json_data(raw_string):
    """Parse JSON. BUG: no error handling."""
    # BUG 1: crashes with unhandled exception on invalid JSON
    return json.loads(raw_string)

def get_env_secret():
    """Get secret from env. BUG: hardcoded fallback secret."""
    # BUG 2: hardcoded secret is a security risk
    return os.getenv("SECRET_KEY", "supersecret123hardcoded")

def process_items(items):
    """Process a list of items. BUG: modifies list while iterating."""
    # BUG 3: mutating a list during iteration causes skipped elements
    for item in items:
        if item < 0:
            items.remove(item)
    return items

def read_all_lines(filepath):
    """Read lines from file. BUG: file handle never closed."""
    # BUG 4: resource leak — no context manager or explicit close
    f = open(filepath, "r")
    return f.readlines()

def calculate_average(numbers):
    """Calculate average. BUG: no empty list guard."""
    # BUG 5: ZeroDivisionError when list is empty
    return sum(numbers) / len(numbers)
