from transformers import AutoTokenizer
import json
import os

# Load tokenizer for the same model used in compression
config_path = os.path.join(os.path.dirname(__file__), "../config.json")
with open(config_path, "r") as f:
    config = json.load(f)

hf_model_name = config["model"]["hf_summarizer"]
tokenizer = AutoTokenizer.from_pretrained(hf_model_name)

def count_tokens(text):
    return len(tokenizer.encode(text, truncation=False))
