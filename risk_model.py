# risk_model.py

class RiskModel:

    def classify(self, downside: float) -> str:
        if downside > 0.7:
            return "HIGH RISK"
        elif downside > 0.4:
            return "MEDIUM RISK"
        return "LOW RISK"

    def should_act(self, probability: float, threshold: float = 0.6) -> bool:
        return probability >= threshold
