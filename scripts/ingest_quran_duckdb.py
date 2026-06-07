import duckdb 
import pandas as pd
from database.duckdb import get_duckdb_connection
from read.

def ingest_quran_duckdb():
    connection = get_duckdb_connection()

    try:
        with connection as conn:
            conn. 