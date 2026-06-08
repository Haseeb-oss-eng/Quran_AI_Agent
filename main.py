from rag.context_builder import ContextBuilder
from rag.prompt_builder  import PromptBuilder
from retrieval.quran_search import QuranSearchService
from repository.quran_repository import QuranRepository
from embeddings.query_embedding import QuranEmbedding
from rag.rag_services  import QuranRAGService
from llm.ollama_client import OllamaClient

llm = OllamaClient()

repository = QuranRepository()

embedder = QuranEmbedding()

search_service = QuranSearchService(
    repository,
    embedder
)

context_builder = ContextBuilder()

prompt_builder = PromptBuilder()


rag = QuranRAGService(
    search_service,
    context_builder,
    prompt_builder,
    llm
)

question = input(
    "Enter your question: "
)

answer = rag.answer(
    question
)

print(answer)
