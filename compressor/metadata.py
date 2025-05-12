def detect_type(text: str) -> str:
    """
    Detects the type of the message (question, inform).
    """
    return "question" if text.strip().endswith("?") else "inform"
