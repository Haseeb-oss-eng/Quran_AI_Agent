from sentence_transformers import SentenceTransformer
import pandas as pd

class QuranEmbedding:

    def __init__(self):
        self.model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
        
    
    def embedding_encode(self,df:pd.DataFrame):
        embedding = self.model.encode(df["Arabic Text"].tolist())
        df["embedding"] = embedding.tolist()

        return df
