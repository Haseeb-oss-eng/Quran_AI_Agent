from retrieval.quran_search import QuranSearchService
from repository.quran_repository import QuranRepository
from embeddings.embedding_services import QuranEmbedding

repository = QuranRepository()
embedder = QuranEmbedding()

quran_search = QuranSearchService(
    repository,
    embedder
)

result = quran_search.search(
    "Patience and Prayer"
)

print(result)