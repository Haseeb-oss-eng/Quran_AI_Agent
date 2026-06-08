from retrieval.quran_search import QuranSearch
from repository.quran_repository import QuranRepository
from embeddings.embedding_services import QuranEmbedding

class QuranSearchService:

    def build_search(self):
        repository = QuranRepository()
        embedder = QuranEmbedding()

        quran_search = QuranSearch(
            repository,
            embedder
        )

        return quran_search