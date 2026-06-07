from datasource.quran_reader import QuranReader
from repository.quran_repository import QuranRepository
from embeddings.quran_embedding import QuranEmbedding
from services.quran_ingest_services import QuranIngestService

if __name__ == "__main__":
    quran_reader = QuranReader()
    quran_repo = QuranRepository()
    quran_embedding = QuranEmbedding()
    quran_services = QuranIngestService(quran_repo,quran_reader,quran_embedding)

    if quran_services.is_successful:
        print("Data is ingested into Database")
    else:
        print("Data is not Inserted...")