import duckdb

def get_duckdb_connection():
    return duckdb.connect("data/database/quran_ai.duckdb")