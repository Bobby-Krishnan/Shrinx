import subprocess
import json
from transformers import pipeline
import os


def load_config():
    # Always find the config.json in the root of the project
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../config.json")
    with open(config_path, "r") as file:
        return json.load(file)

config = load_config()
summarizer = pipeline("summarization", model=config["model"]["hf_summarizer"])

def compress_with_wizardlm(text: str, max_tokens: int) -> str:
    cmd = [
        config["model"]["wizardlm_binary"],
        "--model", config["model"]["wizardlm_model_path"],
        "--temp", "0.7",
        "--repeat_penalty", "1.2",
        "--n_predict", str(max_tokens),
        "-p", f"Compress without losing meaning: {text}"
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        print(f"WizardLM failed with error: {e}. Using Hugging Face instead.")
        return None

def compress_with_hf(text: str, max_tokens: int) -> str:
    return summarizer(text, max_length=max_tokens, min_length=int(max_tokens * 0.1))[0]["summary_text"]

def compress_text(text: str, use_wizardlm: bool = True) -> str:
    max_tokens = len(text.split())
    
    if use_wizardlm:
        compressed = compress_with_wizardlm(text, max_tokens)
        if compressed:
            return compressed
        else:
            print("Falling back to Hugging Face for compression.")
    
    return compress_with_hf(text, max_tokens)

