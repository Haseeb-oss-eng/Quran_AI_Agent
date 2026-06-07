from datasource import QuranReader
from repository import QuranRepository
from embeddings import QuranEmbedding
from services import QuranIngestService

if __name__ == "__main__":
    quran_reader = QuranReader()
    quran_repo = QuranRepository()
    quran_embedding = QuranEmbedding()
    quran_services = QuranIngestService(quran_repo,quran_reader,quran_embedding)

    if quran_services.is_successfull:
        print("Data is ingested into Database")