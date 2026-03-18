# genesis_core.py

from typing import List, Dict, Any

# ===== IMPORT AGENTS =====
from decision_engine import DecisionEngine, Option
from decision_memory import DecisionMemory


# ===== BASIC MEMORY =====
class Memory:
    def __init__(self):
        self.store = []

    def add(self, key: str, value: Any, tags=None, strength: float = 0.5):
        self.store.append({
            "key": key,
            "value": value,
            "tags": tags or [],
            "strength": strength
        })

    def query(self, tag: str):
        return [item for item in self.store if tag in item["tags"]]


# ===== AGENTS =====
class DecomposerAgent:
    name = "Decomposer"

    def run(self, ctx, task: str):
        return {
            "problem": task,
            "subtasks": ["analyze", "evaluate", "decide"]
        }


class AnalystAgent:
    name = "Analyst"

    def run(self, ctx, data):
        return {
            "insight": f"Analyzed: {data['problem']}",
            "uncertainty": 0.4
        }


class SynthesizerAgent:
    name = "Synthesizer"

    def run(self, ctx, data):
        return {
            "options": [
                Option("Option A", upside=0.7, downside=0.5, probability=0.6, reversibility=0.7),
                Option("Option B", upside=0.5, downside=0.2, probability=0.5, reversibility=0.9)
            ]
        }


class DecisionAgent:
    name = "Decision"

    def __init__(self):
        self.engine = DecisionEngine(risk_tolerance=0.6)

    def run(self, ctx, data):
        decision = self.engine.evaluate(data["options"])

        ctx.memory.add(
            "decision",
            decision,
            tags=["decision"],
            strength=0.9
        )

        return decision


class OutputAgent:
    name = "Output"

    def run(self, ctx, decision):
        return {
            "final_decision": decision.chosen,
            "confidence": decision.confidence,
            "reasoning": decision.reasoning,
            "risk": decision.risk
        }


# ===== CONTEXT =====
class Context:
    def __init__(self):
        self.memory = Memory()
        self.decision_memory = DecisionMemory()


# ===== GENESIS CORE =====
class GenesisMind:

    def __init__(self):
        self.ctx = Context()

        self.pipeline = [
            DecomposerAgent(),
            AnalystAgent(),
            SynthesizerAgent(),
            DecisionAgent(),
            OutputAgent()
        ]

    def run(self, task: str) -> Dict[str, Any]:
        data = task

        for agent in self.pipeline:
            data = agent.run(self.ctx, data)

        return data
        from shadow_genesis import ShadowGenesis

class ShadowAgent:
    name = "Shadow"

    def __init__(self):
        self.shadow = ShadowGenesis()

    def run(self, ctx, data):
        return self.shadow.run(ctx, data)
