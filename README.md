# 📄 README.md

## RAG Chatbot Assignment - Angel One Support + Insurance PDFs

### Objective
Build a Retrieval-Augmented Generation (RAG) chatbot that can answer user queries based on:
1. Angel One Support webpages
2. Attached Insurance PDFs

If the answer is **not found in the provided data**, the bot must respond with:
> "I don't know"

---

### Project Structure
```
rag_chatbot/
├── pdf_extractor.py          # Extracts and chunks PDF content
├── web_scraper.py            # Scrapes and chunks AngelOne support site
├── embed_store.py            # Embeds and stores chunks in vector DB
├── rag_pipeline.py           # RAG logic: query → retrieve → respond
├── app.py                    # Streamlit app for chatbot UI
├── requirements.txt          # Python dependencies
└── README.md                 # Setup & run instructions
```

---

### Setup Instructions

#### 1. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 2. Install dependencies
```bash
pip install -r requirements.txt
```

#### 3. Extract PDF content
```bash
python pdf_extractor.py
```

#### 4. Scrape Angel One support site
```bash
python web_scraper.py
```

#### 5. Create embeddings & store
```bash
python embed_store.py
```

#### 6. Launch chatbot
```bash
streamlit run app.py
```

---

### Technologies Used
- `PyMuPDF` for PDF extraction
- `BeautifulSoup` / `requests` for web scraping
- `SentenceTransformers` for embeddings
- `FAISS` or `ChromaDB` for vector storage
- `LangChain` or custom pipeline for RAG logic
- `Streamlit` for chatbot interface
