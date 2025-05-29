"""
Setup script for GPT-2 Embeddings Explorer
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh 
                   if line.strip() and not line.startswith("#")]

setup(
    name="gpt2-embeddings-explorer",
    version="1.0.0",
    author="jirpo9",
    description="Interaktivní nástroj pro exploraci GPT-2 embeddingů",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jirpo9/gpt2-embeddings-explorer",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "gpt2-explorer=src.gpt2_embeddings:main",
        ],
    },
)