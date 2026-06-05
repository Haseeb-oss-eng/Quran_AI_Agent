from sentence_transformers import SentenceTransformer
from sentence_transformers import util
import torch


with open("example/quran-simple-clean.txt",'r',encoding='UTF-8') as fl:
    quran = fl.readlines()

quran_verses = [str(lines).strip() for lines in quran if lines.strip()]

print(quran_verses[2])

model = SentenceTransformer( "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

embedding = model.encode(quran_verses)

user_query = "patience and prayer"

query_embedding = model.encode(user_query)

cosin_sim = util.cos_sim(query_embedding, embedding)[0]

top_sim = torch.topk(cosin_sim,k=3)

for score , idx in zip(top_sim.values, top_sim.indices):
    verse_index = idx.item()

    print("Quran verse similar",quran_verses[verse_index])
