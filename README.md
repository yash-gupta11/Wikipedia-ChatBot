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

```
Wikipedia-ChatBot/
│-- main.py              # Entry point of the chatbot
│-- requirements.txt     # Dependencies
│-- README.md            # Project documentation
```
---

## ⚙️ Workflow
1. **User Input**  
   You enter the title of a Wikipedia page (e.g., `Cristiano Ronaldo`).  

2. **Wikipedia Fetch**  
   The script fetches the entire content of that Wikipedia page using `wikipedia-api`.  

3. **Text Splitting**  
   Content is chunked into smaller parts using `RecursiveCharacterTextSplitter` for better retrieval.  

4. **Embeddings & Vector Store**  
   Each chunk is embedded using HuggingFace (`all-MiniLM-L6-v2`) and stored in FAISS.  

5. **Retriever**  
   When you ask a question, FAISS retrieves the most relevant chunks of text.  

6. **LLM Answer Generation**  
   The retrieved chunks are passed to Ollama’s `phi3.5` model, which generates a response.  

7. **Final Output**  
   You get an AI-generated answer strictly based on the Wikipedia page content.  

---

## ▶️ How to Run
1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/Wikipedia-ChatBot.git
   cd Wikipedia-ChatBot
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the chatbot:
   ```bash
   python main.py

## 📌 Example Run
   ```bash
   Please enter the Title of the Wikipedia Page : Karthik Aryan
   Question: is karthik aryan career discussed in this page?
   Answer: Yes, the page includes details about his acting career.


