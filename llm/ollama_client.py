# llm/ollama_client.py

from ollama import chat
from llm.base_llm import BaseLLM

class OllamaClient(BaseLLM):

    def __init__(self):
        self.model = "qwen3:4b"

    def invoke(self, prompt):

        response = chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]