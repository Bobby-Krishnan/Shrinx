import os
import json

def load_topic_classifier():
    config_path = os.path.join(os.path.dirname(__file__), "../config.json")
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    
    with open(config_path, "r") as file:
        config = json.load(file)
    
    return config

def classify_topic(text, classifier):
    # Placeholder for your topic classification logic
    # Replace this with your real classification model
    return "General"  # Example: Always returns "General" topic
