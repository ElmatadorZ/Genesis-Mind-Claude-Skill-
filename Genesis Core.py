import uuid
from datetime import datetime

# ==============================
# 🧠 MEMORY CORE
# ==============================
class Memory:
    def __init__(self):
        self.short_term = []
        self.long_term = []

    def store(self, data):
        self.short_term.append(data)

    def commit(self):
        self.long_term.extend(self.short_term)
        self.short_term = []

    def recall(self, keyword):
        return [m for m in self.long_term if keyword in str(m)]


# ==============================
# ⚔️ FIRST PRINCIPLE ENGINE
# ==============================
class FirstPrinciple:
    def analyze(self, problem):
        return {
            "truth": f"Core truth of '{problem}'",
            "assumptions": f"Hidden assumptions in '{problem}'",
            "leverage": f"Key leverage point in '{problem}'"
        }


# ==============================
# 🌐 SYSTEM THINKING
# ==============================
class SystemThinking:
    def map(self, problem):
        return {
            "actors": ["users", "market", "power players"],
            "incentives": ["profit", "control", "growth"],
            "risks": ["uncertainty", "volatility"]
        }


# ==============================
# 🤖 AGENT SYSTEM
# ==============================
class Agent:
    def __init__(self, role):
        self.role = role

    def run(self, problem):
        return f"[{self.role}] insight on {problem}"


class AgentFactory:
    def create_agents(self, problem):
        return [
            Agent("Analyst"),
            Agent("Strategist"),
            Agent("Skeptic"),
            Agent("Forecaster")
        ]


# ==============================
# 🎯 DECISION ENGINE
# ==============================
class DecisionEngine:
    def decide(self, insights):
        return f"Best Action based on {len(insights)} insights"


# ==============================
# 🧬 EVOLUTION CORE
# ==============================
class Evolution:
    def reflect(self, result):
        return f"Improvement from result: {result}"


# ==============================
# 🧠 GENESIS CORE
# ==============================
class GenesisCore:

    def __init__(self):
        self.memory = Memory()
        self.fp = FirstPrinciple()
        self.system = SystemThinking()
        self.factory = AgentFactory()
        self.decision_engine = DecisionEngine()
        self.evolution = Evolution()

    def run(self, problem):

        print(f"\n=== GENESIS CORE ACTIVATED ===")
        print(f"Time: {datetime.now()}")
        print(f"Problem: {problem}")

        # 1. First Principle
        fp_result = self.fp.analyze(problem)

        # 2. System Thinking
        system_map = self.system.map(problem)

        # 3. Multi-Agent
        agents = self.factory.create_agents(problem)
        insights = [agent.run(problem) for agent in agents]

        # 4. Decision
        decision = self.decision_engine.decide(insights)

        # 5. Memory
        self.memory.store({
            "id": str(uuid.uuid4()),
            "problem": problem,
            "decision": decision
        })

        # 6. Evolution
        evolution = self.evolution.reflect(decision)

        # Output
        print("\n--- FIRST PRINCIPLE ---")
        print(fp_result)

        print("\n--- SYSTEM ---")
        print(system_map)

        print("\n--- AGENT INSIGHTS ---")
        for i in insights:
            print(i)

        print("\n--- DECISION ---")
        print(decision)

        print("\n--- EVOLUTION ---")
        print(evolution)


# ==============================
# 🚀 RUN SYSTEM
# ==============================

if __name__ == "__main__":
    core = GenesisCore()
    core.run("Global financial war impact on coffee industry")
