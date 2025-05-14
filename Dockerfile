# Use Python 3.10 slim image
FROM python:3.10-slim

# Avoid writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies (e.g., git)
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Copy everything into container
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -e .

# Preload Hugging Face summarization model
RUN python -c "from transformers import pipeline; pipeline('summarization', model='sshleifer/distilbart-xsum-6-6')"

# Optional: ENTRYPOINT for clean CLI use
ENTRYPOINT ["shrinx"]

