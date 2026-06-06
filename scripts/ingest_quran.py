import pandas as pd
import numpy as np
import psycopg2
from pgvector.psycopg2 import register_vector
from sentence_transformers import SentenceTransformer
import json
import duckdb
from database.database import get_connection


print("Loading SentenceTransformer model...")
# model = SentenceTransformer('all-MiniLM-L6-v2')

quran = pd.read_csv("scripts/quran_structured_.csv")
print(quran.columns)

print("Connecting to Database:")

conn = get_connection()


try:
    with conn.cursor() as cur:
        print("Read data from postgres...5")
        cur.execute("select surah_no, surah_name, verse_no, verse_text, embedding from quran_verse")
        rows = cur.fetchall()

        print(f"successfully retrieved {len(rows)} from database")

        print("\nCreating local 'quran.duckdb' file...")
        local_conn = duckdb.connect("quran.duckdb")
        
        # Enable native vector/vss extension in DuckDB
        local_conn.execute("INSTALL vss; LOAD vss;")
        
        local_conn.execute("""
            CREATE TABLE IF NOT EXISTS quran_verses (
                surah_number INTEGER,
                surah_name VARCHAR,
                verse_number INTEGER,
                arabic_text TEXT,
                embedding FLOAT[384] -- DuckDB handles native float arrays beautifully!
            );
        """)
        local_conn.execute("DELETE FROM quran_verses;")
        
        # Format rows perfectly for DuckDB format mapping
        formatted_rows = []
        for r in rows:
            # Convert the Postgres vector format (string or list) into a native python list of floats
            vec_list = [float(x) for x in r[4]] if isinstance(r[4], (list, np.ndarray)) else json.loads(r[4])
            formatted_rows.append((r[0], r[1], r[2], r[3], vec_list))
            
        local_conn.executemany("""
            INSERT INTO quran_verses VALUES (?, ?, ?, ?, ?);
        """, formatted_rows)
        local_conn.close()
        print("Success! Created 'quran.duckdb' in your local repository folder.")

          
except Exception as e:
    print(f"An error occurred: {e}")
    conn.rollback()
finally:
    if conn:
        conn.close()