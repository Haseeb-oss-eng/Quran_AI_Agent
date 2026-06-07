import duckdb

conn = duckdb.connect("database/duckdb/quran_ai.duckdb")

row = conn.execute("""SELECT count(surah_no) from quran_verse;""").fetchone()

print("total rows:",row[0])

print("Sample Datasets:")
df = conn.sql("""SELECT surah_no, verse_no, verse_text from quran_verse limit 1;""").df()

print(df)