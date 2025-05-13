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
