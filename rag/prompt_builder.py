
class PromptBuilder:

    def build(self,question,context):

        return f"""
                    You are a Quran assistant.

                    Answer only using the context.

                    Context:
                    {context}

                    Question:
                    {question}
                """