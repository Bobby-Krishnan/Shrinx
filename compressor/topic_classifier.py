from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import json

def load_topic_classifier():
    """
    Loads the pre-trained Hugging Face topic classifier.
    """
    with open("../config.json", "r") as file:
        config = json.load(file)
        model_name = config["model"]["topic_classifier"]

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)
    return classifier

def classify_topic(text, classifier):
    """
    Classifies the topic of the text using the model.
    """
    result = classifier(text, top_k=1)
    return result[0]['label']
