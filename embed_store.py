import os
import glob
import pickle
from sentence_transformers import SentenceTransformer
import faiss


CHUNK_DIRS = ["output_chunks", "web_data"]
EMBEDDING_DIM = 384
INDEX_FILE = "vector.index"
DOCS_FILE = "docs.pkl"

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.IndexFlatL2(EMBEDDING_DIM)
documents = []

print("Reading chunks and creating embeddings...")

for folder in CHUNK_DIRS:
    for filepath in glob.glob(os.path.join(folder, "*.txt")):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if content:
                embedding = model.encode(content)
                index.add(embedding.reshape(1, -1))
                documents.append({"text": content, "source": filepath})

# Save FAISS index
faiss.write_index(index, INDEX_FILE)

# Save documents
with open(DOCS_FILE, "wb") as f:
    pickle.dump(documents, f)

print(f"Stored {len(documents)} documents in vector store.")