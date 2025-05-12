import json

def normalize_to_jsonl(input_file, temp_jsonl):
    """
    Detects and converts JSON to JSONL if needed.
    """
    with open(input_file, 'r') as json_file:
        data = json.load(json_file)

    with open(temp_jsonl, 'w') as jsonl_file:
        # If the JSON is a list of messages (standard format)
        if isinstance(data, list):
            for message in data:
                if "role" in message and "content" in message:
                    jsonl_file.write(json.dumps(message) + "\n")
        elif isinstance(data, dict):
            # If JSON is nested under a conversation key
            for key, messages in data.items():
                if isinstance(messages, list):
                    for message in messages:
                        if "role" in message and "content" in message:
                            jsonl_file.write(json.dumps(message) + "\n")
        else:
            raise ValueError("Unsupported JSON format.")
