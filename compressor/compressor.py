import subprocess
import json
import os
from transformers import pipeline, AutoTokenizer

# Load config and models globally (persistent)
def load_config():
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../config.json")
    with open(config_path, "r") as file:
        return json.load(file)

config = load_config()
summarizer = pipeline("summarization", model=config["model"]["hf_summarizer"])
tokenizer = AutoTokenizer.from_pretrained(config["model"]["hf_summarizer"])
topic_classifier = None  # Only loaded if needed for topics

# Token telemetry counters
original_token_total = 0
compressed_token_total = 0

def count_tokens(text: str) -> int:
    return len(tokenizer.encode(text, truncation=False))

def print_telemetry():
    global original_token_total, compressed_token_total
    tokens_saved = original_token_total - compressed_token_total
    if original_token_total > 0:
        reduction_percent = (tokens_saved / original_token_total) * 100
    else:
        reduction_percent = 0.0

    print("\n Compression Telemetry")
    print(f" Original Tokens:    {original_token_total}")
    print(f"  Compressed Tokens:  {compressed_token_total}")
    print(f" Tokens Saved:       {tokens_saved} ({reduction_percent:.2f}%)")

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
    global original_token_total, compressed_token_total

    original_tokens = count_tokens(text)
    original_token_total += original_tokens
    max_tokens = original_tokens

    if use_wizardlm:
        compressed = compress_with_wizardlm(text, max_tokens)
        if compressed:
            compressed_token_total += count_tokens(compressed)
            return compressed
        else:
            print("Falling back to Hugging Face for compression.")

    compressed = compress_with_hf(text, max_tokens)
    compressed_token_total += count_tokens(compressed)
    return compressed
