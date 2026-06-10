class QuranRAGService:

    def __init__(
        self,
        search_service,
        context_builder,
        prompt_builder,
        llm
    ):
        self.search_service = search_service
        self.context_builder = context_builder
        self.prompt_builder = prompt_builder
        self.llm = llm

    def answer(self, question):

        retrieval = self.search_service.search(
            question
        )

        context = self.context_builder.build(
            retrieval
        )

        prompt = self.prompt_builder.build(
            question,
            context
        )

        response = self.llm.invoke(
            prompt
        )

        return response