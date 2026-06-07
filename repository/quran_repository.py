from database.duckdb import get_duckdb_connection

class QuranRepository:

    def __init__(self):
        self.db = get_duckdb_connection()

    def create_extension(self):
        self.db.execute("INSTALL vss; LOAD vss;")
        return True

    def create_table(self):
        if not create_extension():
            self.create_extension()
        self.db.execute("create table if not exist quran_verse(id SERIAL PRIMARY KEY, surah_no int not null, surah_name text not null, verse_no int not null, verse_text text not null, embedding VECTOR(384));")
        return True

    def insert_data(self,data:pd.DataFrame):
        if not self.create_table():
            self.create_table()
        self.db.executemany("""
                INSERT INTO quran SELECT surah_no, surah_name, verse_no, verse_text, embedding FROM quran_verse;

            """)
        return True

    def select_from(self,limit = 1):
        return self.db.execute("""SELECT surah_no, surah_name, verse_no, verse_text, embedding FROM quran_verse ?;""",limit).fetch_df()

    def table_length(self):
        return self.db.execute("""SELECT count(surah_no) FROM quran_verse;""").fetch_df()
