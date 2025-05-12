import json

def normalize_to_jsonl(input_file, output_file):
    with open(input_file, "r") as infile:
        data = json.load(infile)  # This will correctly parse JSON Array

    with open(output_file, "w") as outfile:
        if isinstance(data, list):  # JSON Array
            for item in data:
                outfile.write(json.dumps(item) + "\n")
        elif isinstance(data, dict):  # Single JSON Object
            outfile.write(json.dumps(data) + "\n")
        else:
            raise ValueError("Unsupported JSON format. Must be a list or dictionary.")
