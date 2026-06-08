# llm/fake_llm.py

from llm.base_llm import BaseLLM

class FakeLLM(BaseLLM):

    def invoke(self, prompt: str):

        return f"""
        ===== LLM RECEIVED =====

        {prompt}

        ===== END =====
        """