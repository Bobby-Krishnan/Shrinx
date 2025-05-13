from setuptools import setup, find_packages

setup(
    name="shrinx",
    version="0.1.0",
    description="A CLI tool for compressing natural language to save tokens in LLM pipelines.",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "transformers",
        "torch",
        "tqdm",
        "nltk"
    ],
    entry_points={
        "console_scripts": [
            "shrinx=compressor.cli:main"
        ]
    },
    python_requires=">=3.8"
)

def main():
    parser = argparse.ArgumentParser(description="Token Compression CLI Tool")
    parser.add_argument("input", help="Path to input JSON file")
    parser.add_argument("--output", help="Path to output compressed JSON file", required=True)
    parser.add_argument("--use_wizardlm", action="store_true", help="Use WizardLM for compression")
    parser.add_argument("--limit", type=int, help="Limit number of lines processed (optional)")
    
    args = parser.parse_args()
    run_compression(args.input, args.output, args.use_wizardlm)

