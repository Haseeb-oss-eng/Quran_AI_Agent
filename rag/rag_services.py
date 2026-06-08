

class QuranRAGService:

    def __init__(self,question,retrieval,context_builder,prompt_builder,llm):
        self.question = question
        self.retrieval = retrieval
        self.context_builder = context_builder()
        self.prompt_builder = prompt_builder()
        self.llm = llm

    def pipeline(self):
        context_ = self.context(self.retrieval)

        prompt_builder_ = self.prompt_builder(context_)



    def answer(self):
        self.pipeline()

        return pass
