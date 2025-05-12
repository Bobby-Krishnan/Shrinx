import os
import json

def load_topic_classifier():
    # Automatically calculate the absolute path to config.json
    config_path = os.path.join(os.path.dirname(__file__), "../config.json")
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    
    with open(config_path, "r") as file:
        config = json.load(file)
    
    return config
