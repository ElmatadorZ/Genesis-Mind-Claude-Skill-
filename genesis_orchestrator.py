# genesis_orchestrator.py

from typing import Dict, Any

from genesis_core import GenesisMind
from multi_self import MultiSelfSystem
from decision_engine import DecisionEngine
from shadow_wrapper import ShadowWrapper
from shadow_genesis import ShadowGenesis


class GenesisOrchestrator:

    def __init__(self):
        self.core = GenesisMind()
        self.multi_self = MultiSelfSystem()
        self.decision_engine = DecisionEngine()
        self.shadow = ShadowWrapper(ShadowGenesis())

    def run(self, context: str) -> Dict[str, Any]:

        # 1. Core processing (ของเดิม)
        core_output = self.core.process(context)

        # 2. Shadow reflection
        shadow_echo = self.shadow.apply(context)

        # 3. Base decision
        base_decision = {
            "choice": "Act",
            "confidence": 0.6,
            "reason": core_output["shadow_check"]
        }

        # 4. Multi-self evaluation
        evaluated = self.multi_self.evaluate(base_decision)

        # 5. Final decision
        final = self.decision_engine.choose(evaluated)

        return {
            "context": context,
            "core": core_output,
            "shadow": shadow_echo,
            "multi_self": evaluated,
            "final_decision": final
        }
