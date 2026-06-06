import pandas as pd
import numpy as np
import psycopg2
from pgvector.psycopg2 import register_vector
from sentence_transformers import SentenceTransformer
from database.database import get_connection


print("Loading SentenceTransformer model...")
model = SentenceTransformer('all-MiniLM-L6-v2')

quran = pd.read_csv("scripts/quran_structured_.csv")
print(quran.columns)

print("Connecting to Database:")

conn = get_connection()


try:
    with conn.cursor() as cur:
        # dataset = len(quran)
        # batch_size = 256
        # register_vector(conn)

        # for i in range(0,dataset,batch_size):
        #     batch_df = quran.iloc[i:i+batch_size]

        #     text = batch_df["Arabic Text"].tolist()
        #     embeddings = model.encode(text)

        #     insert_data = []

        #     for idx, row in enumerate(batch_df.itertuples()):
        #         insert_data.append((
        #             row._1,
        #             row._2,
        #             row._3,
        #             row._4,
        #             embeddings[idx]
        #         ))

    
            # 1. Define your query string
        select_query = """
                SELECT * FROM quran_verse LIMIT 5;
            """
            
            # 2. YOU MUST EXECUTE IT FIRST!
        cur.execute(select_query)
            
            # 3. Fetch the results and assign them to a variable (fix indentation)
        rows = cur.fetchall()
            
            # 4. Print out your results to see them in the terminal
        for row in rows:
            print(row)
                
            # Note: conn.commit() is only strictly necessary for INSERT/UPDATE/DELETE.
            # But keeping it here won't break a SELECT query.
        conn.commit() 
          
except Exception as e:
    print(f"An error occurred: {e}")
    conn.rollback()
finally:
    if conn:
        conn.close()