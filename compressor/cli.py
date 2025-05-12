import os
import json
import argparse
from .parser import normalize_to_jsonl
from .metadata import detect_type
from .tokenizer import count_tokens
from .compressor import compress_text, load_config
from .topic_classifier import load_topic_classifier, classify_topic

def run_compression(input_file, output_file, use_wizardlm=True):
    temp_jsonl = "temp_input.jsonl"
    print(f"[INFO] Normalizing input file: {input_file} -> {temp_jsonl}")
    normalize_to_jsonl(input_file, temp_jsonl)
    
    topic_classifier = load_topic_classifier()
    turn = 1
    print(f"[INFO] Loading topic classifier...")

    with open(temp_jsonl, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            print(f"[DEBUG] Processing line: {line.strip()}")
            msg = json.loads(line)
            content = msg.get("content", "")
            if not content:
                print(f"[WARNING] Missing content in message: {msg}")
                continue

            compressed = compress_text(content, use_wizardlm)
            topic = classify_topic(content, topic_classifier)

            print(f"[DEBUG] Compressed Text: {compressed}")
            print(f"[DEBUG] Classified Topic: {topic}")

            msg.update({
                "turn": turn,
                "type": detect_type(content),
                "topic": topic,
                "content": compressed
            })
            outfile.write(json.dumps(msg) + "\n")
            turn += 1

    os.remove(temp_jsonl)
    print(f"[INFO] Compression completed. Output saved to {output_file}")
