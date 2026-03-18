# analyst_llm.py

from llm.llm_client import LLMClient

class AnalystLLM:

    name = "Analyst-LLM"

    def __init__(self):
        self.llm = LLMClient()

    def run(self, ctx, data):
        prompt = f"""
        Analyze this problem deeply:

        {data['problem']}

        Provide:
        - Key risks
        - Hidden assumptions
        - Strategic insight
        """

        response = self.llm.generate(prompt)

        result = {
            "analysis_text": response,
            "uncertainty": 0.5
        }

        ctx.memory.add("llm_analysis", result, tags=["analysis"], strength=0.9)

        return {**data, **result}
