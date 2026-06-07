from database.duckdb.duckdb_connection import get_duckdb_connection
import pandas as pd

class QuranRepository:

    def __init__(self):
        self.db = get_duckdb_connection()

    def create_extension(self):
        # Install and load the vector similarity search extension
        self.db.execute("INSTALL vss; LOAD vss;")
        return True

    def create_table(self):
        self.create_extension()
        self.db.execute("CREATE SEQUENCE IF NOT EXISTS quran_verse_id_seq START 1;")
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS quran_verse (
                id INT PRIMARY KEY DEFAULT nextval('quran_verse_id_seq'), 
                surah_no INT NOT NULL, 
                surah_name TEXT NOT NULL, 
                verse_no INT NOT NULL, 
                verse_text TEXT NOT NULL, 
                embedding FLOAT[384]
            );
        """)
        return True

    def insert_data(self, data: pd.DataFrame):
        self.create_table()
        
        self.db.execute("""
            INSERT INTO quran_verse (surah_no, surah_name, verse_no, verse_text, embedding) 
            SELECT "Surah Number", "Surah Name", "Verse Number", "Arabic Text", "embedding" FROM data;
        """)
        return True

    def select_from(self, limit=1):
        return self.db.execute("""
            SELECT surah_no, surah_name, verse_no, verse_text, embedding 
            FROM quran_verse 
            LIMIT ?;
        """, [limit]).fetch_df()

    @property
    def table_length(self):
        result = self.db.execute("SELECT COUNT(*) FROM quran_verse;").fetchone()
        return result[0] if result else 0
