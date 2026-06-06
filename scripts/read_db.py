import duckdb
import pandas as pd

conn = duckdb.connect("database/quran.duckdb")

df = conn.execute("select * from quran_verses;").fetch_df()

print(df)