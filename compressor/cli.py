import os
import json
import argparse
from compressor.parser import normalize_to_jsonl
from compressor.metadata import detect_type
from compressor.tokenizer import count_tokens
from compressor.compressor import compress_text, load_config
from compressor.topic_classifier import load_topic_classifier, classify_topic

def run_compression(input_file, output_file, use_wizardlm=True):
    temp_jsonl = "temp_input.jsonl"
    normalize_to_jsonl(input_file, temp_jsonl)
    
    topic_classifier = load_topic_classifier()
    turn = 1

    with open(temp_jsonl, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            msg = json.loads(line)
            content = msg["content"]
            compressed = compress_text(content, use_wizardlm)
            topic = classify_topic(content, topic_classifier)

            msg.update({
                "turn": turn,
                "type": detect_type(content),
                "topic": topic,
                "content": compressed
            })
            outfile.write(json.dumps(msg) + "\n")
            turn += 1

    os.remove(temp_jsonl)
