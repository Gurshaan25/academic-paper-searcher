import pickle
import os
from sentence_transformers import SentenceTransformer
import numpy as np

class VectorStore:
    def __init__(self, path):
        self.path = path
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.vectors = []
        if os.path.exists(path):
            self.load()

    def add_many(self, summaries):
        texts = [s["summary"] for s in summaries]
        vecs = self.model.encode(texts)
        for s, v in zip(summaries, vecs):
            self.vectors.append((s, v))
        self.save()

    def search(self, query, top_k=3):
        qvec = self.model.encode([query])[0]
        sims = [(s, np.dot(qvec, v)/(np.linalg.norm(qvec)*np.linalg.norm(v))) for s, v in self.vectors]
        sims.sort(key=lambda x: x[1], reverse=True)
        return [s for s, _ in sims[:top_k]]

    def save(self):
        with open(self.path, "wb") as f:
            pickle.dump(self.vectors, f)

    def load(self):
        with open(self.path, "rb") as f:
            self.vectors = pickle.load(f)
