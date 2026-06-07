import duckdb

def get_duckdb_connection():
    return conn.connect(f"database/duckdb/quran.duckdb")