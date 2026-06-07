import psycopg2
from config import settings

def get_connection():
    return psycopg2.connect(
        host=settings.POSTGRES_HOST,
        database="quran_ai",
        user="postgres",
        password="postgres"
    )