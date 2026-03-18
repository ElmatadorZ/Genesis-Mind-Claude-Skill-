# llm_client.py

import requests

class LLMClient:

    def __init__(self, api_key=None):
        self.api_key = api_key

    def generate(self, prompt: str) -> str:
        # MOCK (replace with OpenAI / Claude later)
        return f"[LLM RESPONSE SIMULATION]\n{prompt}"
