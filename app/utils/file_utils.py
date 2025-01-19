import os
import json
from datetime import datetime

from config import Config

# Ensure the temp directory exists
os.makedirs(Config.TEMP_DIR, exist_ok=True)

def save_data_to_file(filename, data):
    """
    Saves data to a JSON file for debugging or intermediate storage.

    Args:
        filename (str): The name of the file.
        data (dict or list): The data to be saved.

    Returns:
        str: The file path where the data was saved.
    """
    file_path = os.path.join(Config.TEMP_DIR, filename)
    
    # Save data as JSON
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
    
    return file_path

def load_data_from_file(filename):
    """
    Loads data from a JSON file for reprocessing.

    Args:
        filename (str): The name of the file to load.

    Returns:
        dict or list: The data loaded from the file.
    """
    file_path = os.path.join(Config.TEMP_DIR, filename)
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    return data

def clean_temp_files():
    """
    Cleans up temporary files in the temp directory.
    """
    for filename in os.listdir(Config.TEMP_DIR):
        file_path = os.path.join(Config.TEMP_DIR, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
