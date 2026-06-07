import duckdb

class DuckdbConnection:
    def __init__(self):
        self.db = duckdb.connect(f"database/duckdb/quran_ai.duckdb")
    def get_duckdb_connection():
        return self.db