import os
import json
import argparse
from .parser import normalize_to_jsonl
from .metadata import detect_type
from .tokenizer import count_tokens
from .compressor import compress_text, load_config, print_telemetry
from .topic_classifier import load_topic_classifier, classify_topic

def run_compression(input_file, output_file, use_wizardlm=True):
    print(f"[INFO] Starting compression with input: {input_file} and output: {output_file}")
    temp_jsonl = "temp_input.jsonl"
    print(f"[INFO] Normalizing input file: {input_file} -> {temp_jsonl}")
    normalize_to_jsonl(input_file, temp_jsonl)
    
    topic_classifier = load_topic_classifier()
    print(f"[INFO] Loading topic classifier...")

    turn = 1
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

    # Print final token telemetry
    print_telemetry()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Token Compression CLI Tool")
    parser.add_argument("input", help="Path to input JSON file")
    parser.add_argument("--output", help="Path to output compressed JSON file", required=True)
    parser.add_argument("--use_wizardlm", action="store_true", help="Use WizardLM for compression")

    args = parser.parse_args()
    run_compression(args.input, args.output, args.use_wizardlm)
