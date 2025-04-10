import os
import fitz  # PyMuPDF
from typing import List

# --- CONFIG ---
PDF_DIR = "Insurance PDFs/"  # Folder where all your insurance PDFs are stored
OUTPUT_DIR = "./output_chunks"
MAX_CHARS_PER_CHUNK = 1500  # Approx. 300–400 words per chunk

# --- FUNCTIONS ---

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extracts full text from a single PDF file."""
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def chunk_text(text: str, max_chars: int = MAX_CHARS_PER_CHUNK) -> List[str]:
    """Splits text into chunks of approximately max_chars."""
    paragraphs = text.split('\n')
    chunks = []
    current_chunk = ""
    for para in paragraphs:
        if len(current_chunk) + len(para) < max_chars:
            current_chunk += para + "\n"
        else:
            chunks.append(current_chunk.strip())
            current_chunk = para + "\n"
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks

# --- MAIN ---

os.makedirs(OUTPUT_DIR, exist_ok=True)

def process_pdfs():
    for filename in os.listdir(PDF_DIR):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(PDF_DIR, filename)
            print(f"Processing: {filename}")
            text = extract_text_from_pdf(pdf_path)
            chunks = chunk_text(text)
            base_name = os.path.splitext(filename)[0]

            for i, chunk in enumerate(chunks):
                output_path = os.path.join(OUTPUT_DIR, f"{base_name}_chunk_{i+1}.txt")
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(chunk)
            print(f" -> {len(chunks)} chunks created")

if __name__ == "__main__":
    process_pdfs()
    print("All PDFs processed and chunked.")