# genesis_full.py

from typing import Dict, Any, List
import uuid, json, os
from datetime import datetime


# =========================================================
# 🧬 VOLITION ENGINE (จาก VX Core)
# =========================================================

class VolitionEngine:

    def extract(self, text: str) -> Dict:
        return {
            "core": "seek leverage",
            "intent": "optimize outcome",
            "confidence": 0.7
        }


# =========================================================
# 👁️ SHADOW ENGINE (จาก Shadow Genesis)
# =========================================================

class ShadowEngine:

    def analyze(self, text: str) -> Dict:
        flags = []

        if "always" in text or "never" in text:
            flags.append("absolutism_bias")

        return {
            "flags": flags,
            "reflection": "What if your assumption is wrong?"
        }


# =========================================================
# 🧠 MEMORY SYSTEM
# =========================================================

class Memory:

    def __init__(self, path="state/memory.jsonl"):
        self.path = path
        os.makedirs(os.path.dirname(path), exist_ok=True)

    def add(self, data: Dict):
        with open(self.path, "a") as f:
            f.write(json.dumps(data) + "\n")

    def query(self, keyword: str):
        results = []
        if not os.path.exists(self.path):
            return results

        with open(self.path) as f:
            for line in f:
                if keyword in line:
                    results.append(json.loads(line))
        return results[-5:]


# =========================================================
# 🧠 AGENTS (Atlas / Skynet / Shadow)
# =========================================================

class Atlas:
    def think(self, problem: str):
        return "Preserve capital. Think long-term."

class Skynet:
    def think(self, problem: str):
        return "Speed matters. Execute if edge exists."

class Shadow:
    def think(self, problem: str):
        return "What if both are wrong?"


# =========================================================
# ⚔️ DECISION ENGINE
# =========================================================

class DecisionEngine:

    def decide(self, options: List[Dict]):

        best = max(options, key=lambda x: x["score"])

        return {
            "choice": best["name"],
            "confidence": best["score"],
            "reason": "Highest expected value"
        }


# =========================================================
# 🧠 GENESIS CORE
# =========================================================

class GenesisMind:

    def __init__(self):
        self.volition = VolitionEngine()
        self.shadow = ShadowEngine()
        self.memory = Memory()

        self.atlas = Atlas()
        self.skynet = Skynet()
        self.shadow_agent = Shadow()

        self.decision = DecisionEngine()

    def generate_options(self, problem: str):
        return [
            {"name": "Act Now", "score": 0.8},
            {"name": "Wait", "score": 0.6},
            {"name": "Do Nothing", "score": 0.3}
        ]

    def run(self, text: str) -> Dict[str, Any]:

        # 🧬 STEP 1: VOLITION
        vol = self.volition.extract(text)

        # 👁️ STEP 2: SHADOW CHECK
        shadow = self.shadow.analyze(text)

        # 🧠 STEP 3: MULTI-AGENT THINKING
        atlas_view = self.atlas.think(text)
        skynet_view = self.skynet.think(text)
        shadow_view = self.shadow_agent.think(text)

        # ⚔️ STEP 4: OPTIONS
        options = self.generate_options(text)

        # ⚔️ STEP 5: DECISION
        decision = self.decision.decide(options)

        # 🔁 STEP 6: MEMORY
        self.memory.add({
            "id": str(uuid.uuid4()),
            "time": str(datetime.now()),
            "input": text,
            "decision": decision
        })

        return {
            "input": text,
            "volition": vol,
            "shadow": shadow,
            "agents": {
                "atlas": atlas_view,
                "skynet": skynet_view,
                "shadow": shadow_view
            },
            "decision": decision
        }
