class QuranSearchService:

    def __init__(
        self,
        repository,
        embedder
    ):
        self.repository = repository
        self.embedder = embedder

    def search(self, query):

        query_embedding = self.embedder.encode(query)

        return self.repository.semantic_search(
            query_embedding
        )