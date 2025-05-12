from transformers import AutoTokenizer

# Load the Hugging Face Tokenizer (same as the model you will use)
tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")

def count_tokens(text: str) -> int:
    """
    Counts tokens in the given text using the Hugging Face tokenizer.
    """
    tokens = tokenizer(text)["input_ids"]
    return len(tokens)
