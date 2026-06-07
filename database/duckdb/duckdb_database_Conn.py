import duckdb

def get_duckdb_connection():
    return duckdb.connect("database/duckdb/quran_ai.duckdb")