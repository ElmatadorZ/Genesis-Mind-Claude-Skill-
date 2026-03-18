# genesis_core_vx.py

from typing import Dict, Any
from core.decision_engine import DecisionEngine, Option


# =========================================================
# 🧠 VX CORE (YOUR ORIGINAL — REFACTORED)
# =========================================================

class VXCore:

    def __init__(self):
        self.context = {}
        self.volition = {}
        self.meaning_web = {}
        self.shadow_map = {}
        self.insight_log = {}
        self.truth_index = {}

    def process(self, raw_text):

        self.context = self.capture_context(raw_text)
        self.volition = self.extract_volition(raw_text)

        key = self.link_meaning(self.volition)

        shadow = self.map_shadow_intent(self.volition.get("core"))
        resonance = self.calculate_resonance(raw_text)

        insight = self.construct_insight(
            self.context,
            self.volition,
            shadow,
            resonance
        )

        self.insight_log[key] = insight

        return {
            "context": self.context,
            "volition": self.volition,
            "shadow": shadow,
            "resonance": resonance,
            "insight": insight
        }

    def capture_context(self, text):
        return {
            "length": len(text),
            "words": text.split(),
            "tone": "neutral"
        }

    def extract_volition(self, text):
        return {
            "core": "seek understanding",
            "polarity": 1.0,
            "subtext": "transcend duality",
            "conflict_index": 0.2
        }

    def link_meaning(self, volition):
        key = hash(volition.get("core", "") + volition.get("subtext", ""))
        self.meaning_web[key] = volition
        return key

    def map_shadow_intent(self, motive):
        return {
            "hidden_drive": "dissolve self-other boundary",
            "confidence": 0.8
        }

    def calculate_resonance(self, text):
        return min(1.0, len(text) / 150)

    def construct_insight(self, context, volition, shadow, resonance):
        return {
            "reflection": f"{volition['core']} → {shadow['hidden_drive']}",
            "resonance": resonance
        }


# =========================================================
# ⚔️ FUSION GENESIS MIND
# =========================================================

class GenesisMindVX:

    def __init__(self):
        self.vx = VXCore()
        self.decision_engine = DecisionEngine(risk_tolerance=0.6)

    def generate_options(self, insight):

        return [
            Option("Act Now", 0.8, 0.6, 0.6, 0.5),
            Option("Wait & Observe", 0.5, 0.2, 0.5, 0.9),
        ]

    def run(self, task: str) -> Dict[str, Any]:

        # 🧠 STEP 1: Consciousness Layer
        vx_data = self.vx.process(task)

        # ⚔️ STEP 2: Option Creation
        options = self.generate_options(vx_data["insight"])

        # ⚔️ STEP 3: Decision
        decision = self.decision_engine.evaluate(options)

        # 🧬 FINAL OUTPUT
        return {
            "input": task,
            "volition": vx_data["volition"],
            "shadow": vx_data["shadow"],
            "insight": vx_data["insight"],
            "decision": decision.chosen,
            "confidence": decision.confidence,
            "reasoning": decision.reasoning
        }
