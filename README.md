#  Shrinx — Token Compression CLI Tool

Shrinx is a Python-based command-line tool for compressing token-heavy JSON chat logs and datasets without losing semantic meaning. Optimized for large language model (LLM) pipelines, it helps reduce token counts to lower costs, improve latency, and increase API efficiency when working with models like OpenAI, Claude, or WizardLM. Shrinx normalizes `.json` files into `.jsonl`, compresses messages using Hugging Face summarization (or offline WizardLM if available), and adds topic classification with full compression telemetry — making it ideal for streamlining LLM-based applications at scale.

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
pip install -r requirements.txt      # Install dependencies
pip install -e .                     # Install Shrinx CLI locally
```

##  Supported Input Format

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
```

##  Output Format

The output is a `.jsonl` file where each line is a compressed, token-reduced message with metadata:

```yaml
output_format:
  type: jsonl
  description: Each line is a compressed message with metadata
  example:
    - role: user
      content: What is entropy?
      topic: Science
      type: user
      turn: 1
    - role: assistant
      content: Entropy is system disorder.
      topic: Science
      type: assistant
      turn: 2
```
##   Usage
Once installed, you can run the tool from your terminal using:

```bash
shrinx sample.json --output compressed_output.jsonl --use_wizardlm
```
##  Compression Telemetry

Shrinx prints a summary after every run to show the token reduction achieved:

```yaml
telemetry:
  original_tokens: 14123
  compressed_tokens: 6009
  tokens_saved: 8114
  savings_percent: 57.45
  sample_output:
    - message: Original Tokens: 14123
    - message: Compressed Tokens: 6009
    - message: Tokens Saved: 8114 (57.45%)
```

