"""
Storage utilities for loading and saving data.
"""

import json

DATA_FILE = "data/database.json"


def load_data():
    """
    Load data from JSON file.
    """

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return {
            "users": [],
            "projects": [],
            "tasks": []
        }

    except json.JSONDecodeError:
        return {
            "users": [],
            "projects": [],
            "tasks": []
        }


def save_data(data):
    """
    Save data to JSON file.
    """

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)