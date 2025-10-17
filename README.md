# RAG-Based CLI Assistant

A lightweight terminal-based Retrieval-Augmented Generation (RAG) assistant powered by local embeddings and LLM inference.

## Features
- Local embeddings using `bge-m3`
- Query understanding and similarity search with `cosine_similarity`
- Dynamic prompt generation for context-aware responses
- Writes outputs to `prompt.txt` and `response.txt`
- Fully offline, runs on local Ollama or compatible model server

## Requirements
- Python 3.9+
- Local model server (e.g., [Ollama](https://ollama.ai)) running at `http://localhost:11434`
- `embeddings.joblib` file in project root

## Installation
```bash
pip install -r requirements.txt
