import pickle
import faiss
from sentence_transformers import SentenceTransformer
import numpy as np

# Load index and docs
INDEX_FILE = "vector.index"
DOCS_FILE = "docs.pkl"
EMBEDDING_DIM = 384

index = faiss.read_index(INDEX_FILE)
with open(DOCS_FILE, "rb") as f:
    documents = pickle.load(f)

model = SentenceTransformer("all-MiniLM-L6-v2")

# Simulated language model (can swap with OpenAI, etc.)
def generate_answer(query, context_docs):
    context = "\n---\n".join(doc["text"] for doc in context_docs)
    if query.lower() in context.lower():
        return f"Based on our documents: {query} => {context_docs[0]['text'][:300]}..."
    else:
        return "I don't know"

def get_relevant_docs(query, k=5):
    query_vec = model.encode([query])
    D, I = index.search(np.array(query_vec), k)
    return [documents[i] for i in I[0] if i < len(documents)]

def answer_query(query):
    relevant_docs = get_relevant_docs(query)
    return generate_answer(query, relevant_docs)

# Example usage
if __name__ == "__main__":
    while True:
        q = input("Ask a question (or 'exit'): ")
        if q.lower() == 'exit':
            break
        print("\n", answer_query(q), "\n")