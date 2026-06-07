--Postgres
create extension VECTOR;
create table quran_verse(id SERIAL PRIMARY KEY, surah_no int not null, surah_name text not null, verse_no int not null, verse_text text not null, embedding VECTOR(384));

--Duckdb
INSTALL vss; LOAD vss;
create table quran_verse(id SERIAL PRIMARY KEY, surah_no int not null, surah_name text not null, verse_no int not null, verse_text text not null, embedding VECTOR(384));