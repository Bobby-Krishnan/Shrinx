#  Shrinx — Token Compression CLI Tool

Shrinx is a CLI tool for compressing natural language logs or datasets to reduce token count — optimized for large language model (LLM) pipelines. It normalizes JSON files, compresses messages via Hugging Face summarization (or WizardLM offline), and outputs compressed `.jsonl` files with topic tagging and full telemetry.

---

##  Features

-  Hugging Face summarization-based compression (`sshleifer/distilbart-xsum-6-6`)
-  WizardLM (LLaMA.cpp) optional local fallback
-  JSON-to-JSONL normalization
-  Topic classification for each message
-  Safe fallback for short or empty messages
-  Real-time token telemetry with % savings
-  `--limit` flag for testing or chunked runs
-  Pip-installable with local CLI command: `shrinx`

---

##  Installation (Local Development)

```bash
git clone https://github.com/your-username/shrinx.git
cd shrinx
python3 -m venv venv
source venv/bin/activate
pip install -e .

## 📥 Supported Input Format

Shrinx accepts `.json` files that are either:

```yaml
supported_input:
  formats:
    - type: json
      description: Accepts a .json file containing either:
      accepted_structures:
        - type: array
          description: An array of messages
          example:
            - role: user
              content: What is entropy?
            - role: assistant
              content: Entropy is disorder in a system.
        - type: object
          description: A single object (wrapped internally into one-line JSONL)

