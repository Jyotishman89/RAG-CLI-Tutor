# RAG Assistant — Backend scripts

This repository contains backend scripts for a RAG assistant. The main runnable script is `process_incoming.py`.

## Prerequisites
- Python 3.9+
- Local model server running (embedding & generation) at `http://localhost:11434` (or update endpoints in the code).
- `embeddings.joblib` file — place it locally (do **not** commit).

## Install dependencies
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
