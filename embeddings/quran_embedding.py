from sentence_transformers import SentenceTransformer

class QuranEmbedding:

    def __init__(self):
        self.model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
        
    
    def embedding_encode(self,df:pd.DataFrame):
        embedding = self.model.encode(self.df["Arabic Text"].tolist())
        self.df["embedding"] = embedding.tolist()

        return self.df
