# 📖 Wikipedia ChatBot

A simple chatbot that allows you to query any **Wikipedia page** and get AI-generated answers.  
This project uses **LangChain**, **HuggingFace embeddings**, **FAISS vector store**, and **Ollama LLM** to create a context-aware chatbot powered by Wikipedia.

---

## 🚀 Features
- Fetches live content from Wikipedia pages.
- Splits and processes text into chunks for efficient retrieval.
- Embeds text using HuggingFace models (`all-MiniLM-L6-v2`).
- Stores embeddings in FAISS for similarity-based retrieval.
- Uses **Ollama LLM (`phi3.5`)** to answer questions.
- Ensures answers are **only based on Wikipedia content** (no hallucinations).

---

## 🛠️ Tech Stack
- [LangChain](https://www.langchain.com/) – Framework for building LLM apps.  
- [HuggingFace Transformers](https://huggingface.co/) – Embeddings.  
- [FAISS](https://faiss.ai/) – Vector database for similarity search.  
- [Ollama](https://ollama.com/) – Local LLM inference.  
- [Wikipedia API](https://pypi.org/project/Wikipedia-API/) – Fetching live Wikipedia data.  
- Python 3.9+  

---

## 📂 Project Structure
