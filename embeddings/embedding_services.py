from sentence_transformers import SentenceTransformer
from config import settings
import pandas as pd

class QuranEmbedding:

    def __init__(self):
        self.model = SentenceTransformer(settings.EMBEDDING_MODEL)
        
    
    def encode(self, text):
        return self.model.encode(text).tolist()

    def encode_batch(self, texts):
        return self.model.encode(texts).tolist()