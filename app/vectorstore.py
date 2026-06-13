import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from app.data_loader import load_data

class VectorStore:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.texts = load_data()

        self.embeddings = self.model.encode(self.texts, show_progress_bar=True)

        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(np.array(self.embeddings))

    def search(self, query, k=5):
        query_vec = self.model.encode([query])
        distances, indices = self.index.search(np.array(query_vec), k)

        return [self.texts[i] for i in indices[0]]