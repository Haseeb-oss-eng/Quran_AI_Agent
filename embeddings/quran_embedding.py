from sentence_transformers import SentenceTransformer
from config import settings
import pandas as pd

class QuranEmbedding:

    def __init__(self):
        self.model = SentenceTransformer(settings.EMBEDDING_MODEL)
        
    
    def embedding_encode(self,df:pd.DataFrame):
        embedding = self.model.encode(df["Arabic Text"].tolist())
        df["embedding"] = embedding.tolist()

        return df
