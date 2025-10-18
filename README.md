# 🧠 RAG-CLI-Tutor

A lightweight, terminal-based Retrieval-Augmented Generation (RAG) teaching assistant powered by local embeddings and LLM inference.

This is a small learning project that behaves like a miniature language model.
It can answer questions based on just four video transcripts using RAG (though the CLI isn’t very polished yet, it works well for learning purposes).

I built this project to deepen my understanding of **embeddings**, **cosine similarity**, and **prompt-based generation**.  

## 🚀 Features
- Local embeddings using `bge-m3`
- Query understanding and similarity search with `cosine_similarity`
- Dynamic prompt generation for context-aware responses
- Writes outputs to `prompt.txt` and `response.txt`
- Fully offline, runs on local Ollama or compatible model server

## 🧩 Requirements
- Python 3.9+
- Local model server (e.g., [Ollama](https://ollama.ai)) running at `http://localhost:11434`
- `embeddings.joblib` file in project root

## ⚙️ Installation
```bash
pip install -r requirements.txt

## ✅ Project Progress

Here’s a quick view of my RAG-CLI-Tutor development progress:

### 🧱 Core Features
- [x] Implement basic RAG pipeline (retriever + generator)
- [x] Load and process local video transcripts
- [x] Perform embedding creation and cosine similarity search
- [x] Generate responses using LLM inference
- [ ] Improve CLI interface and usability
- [ ] Add error handling for empty or invalid input

### 🧠 Enhancements
- [ ] Add more video transcripts to improve knowledge base
- [ ] Support follow-up (contextual) questions
- [ ] Add logging for better debugging
- [ ] Optimize embedding storage for faster retrieval

### 🧩 Documentation
- [x] Write basic project README
- [x] Add project description and goals
- [ ] Add setup and usage instructions
- [ ] Create a demo GIF or terminal screenshot

---
*Progress will be updated as the project evolves!*
