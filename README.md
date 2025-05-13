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


