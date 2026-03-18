"""
GENESIS MIND - FIRST PRINCIPLE CODEX
-----------------------------------
A reasoning kernel for deep analytical thinking

Part of: Genesis Mind Claude Skill
Created by: Bunyawat Dechanon (Money Atlas)

Core Philosophy:
- Think from First Principles
- Solve from root causes
- Optimize for system-level leverage
"""
"""
First Principle Codex
---------------------

A reasoning kernel for Genesis Mind.

Core ideas:
    - Reduce phenomena to First Principles (Atomic Truths)
    - Frame problems with Four Problem Truths
      (Problem, Cause, Resolution, Paths)
    - Evaluate options across multiple frames of reference
    - Simulate system-level effects and choose high-leverage moves
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Iterable, Tuple
import itertools
import math


# --------------------------------------------------------------------
# 1) DATA STRUCTURES
# --------------------------------------------------------------------

@dataclass
class AtomicTruth:
    key: str
    description: str
    tags: List[str] = field(default_factory=list)

    def matches(self, phenomenon: str) -> bool:
        """
        Very lightweight matcher.
        In production, this can call an LLM / embedding similarity.
        """
        tokens = set(self.description.lower().split())
        p_tokens = set(phenomenon.lower().split("_"))
        return len(tokens & p_tokens) > 0


@dataclass
class ProblemTruths:
    problem: str       # ปัญหา คืออะไร
    cause: str         # สาเหตุราก คืออะไร
    resolution: str    # ถ้าไม่มีปัญหาแล้ว โลกควรมีหน้าตาแบบไหน
    paths: List[str]   # เส้นทางหรือแนวทางกว้าง ๆ ที่พาไปสู่ resolution


@dataclass
class OptionPlan:
    atoms: List[AtomicTruth]
    description: str
    score_by_frame: Dict[str, float] = field(default_factory=dict)
    system_leverage: float = 0.0
    problem_reduction: float = 0.0


# --------------------------------------------------------------------
# 2) FIRST PRINCIPLE CODEX
# --------------------------------------------------------------------

class FirstPrincipleCodex:
    """
    First Principle Codex
    ---------------------
    - Holds atomic truths (First Principles)
    - Frames problems using Four Problem Truths
    - Evaluates options across frames of reference
    - Simulates system-level effects
    """

    # ---------------- CONSTRUCTOR ----------------

    def __init__(self, frames: Iterable[str] | None = None) -> None:
        self.atomics: Dict[str, AtomicTruth] = self._default_atomics()
        self.frames: List[str] = list(frames) if frames else [
            "self_now",
            "self_10y",
            "customer",
            "market",
            "system"
        ]
        self.problem_truths: ProblemTruths | None = None

    # ---------------- ATOMICS ----------------

    def _default_atomics(self) -> Dict[str, AtomicTruth]:
        """Base First Principles set. Extend as needed."""
        atoms = [
            AtomicTruth(
                "existence",
                "reality persists without any single observer",
                ["ontology", "reality", "objectivity"],
            ),
            AtomicTruth(
                "causation",
                "every effect traces back to one or more root causes",
                ["cause", "effect", "root_cause"],
            ),
            AtomicTruth(
                "entropy",
                "systems drift toward disorder without directed energy",
                ["entropy", "disorder", "energy"],
            ),
            AtomicTruth(
                "information",
                "information reduces uncertainty about the world",
                ["information", "uncertainty", "signal"],
            ),
            AtomicTruth(
                "leverage",
                "a well chosen vector multiplies the impact of input",
                ["leverage", "asymmetry", "efficiency"],
            ),
            AtomicTruth(
                "compounding",
                "repeated positive edge compounds into outsized outcomes",
                ["compound", "time", "growth"],
            ),
            AtomicTruth(
                "incentives",
                "behavior aligns with perceived reward gradients",
                ["incentive", "behavior", "reward"],
            ),
            AtomicTruth(
                "feedback",
                "systems self regulate via reinforcing and balancing loops",
                ["feedback", "loop", "system"],
            ),
        ]
        return {a.key: a for a in atoms}

    # ----------------------------------------------------------------
    # 3) KALAMA-STYLE FILTER (ข้อมูลที่ควรรับเข้า)
    # ----------------------------------------------------------------

    def kalama_filter(self, observations: Iterable[str]) -> List[str]:
        """
        Very simple epistemic filter:
        - drop pure rumor-like strings
        Production: replace with stronger checks / provenance.
        """
        clean: List[str] = []
        for obs in observations:
            o = obs.lower()
            if any(k in o for k in ["เขาว่า", "ลือ", "ข่าวลือ"]):
                continue
            clean.append(obs)
        return clean

    # ----------------------------------------------------------------
    # 4) REDUCE PHENOMENA TO ATOMICS
    # ----------------------------------------------------------------

    def derive_core_truths(self, phenomenon: str) -> List[AtomicTruth]:
        """
        Map a phenomenon to relevant atomic truths.
        """
        matched = [
            atom for atom in self.atomics.values()
            if atom.matches(phenomenon)
        ]
        # if nothing matches, fall back to a minimal explanatory set
        return matched or list(self.atomics.values())[:3]

    # ----------------------------------------------------------------
    # 5) FOUR PROBLEM TRUTHS (อริยสัจแบบปัญหา)
    # ----------------------------------------------------------------

    def define_problem_truths(self, problem: str) -> ProblemTruths:
        """
        Create a simple ProblemTruths structure.
        In practice these would be co-created with a human / LLM.
        """
        # toy heuristics – replace with richer reasoning if needed
        cause = f"root_causes_of({problem})"
        resolution = f"world_where({problem})_no_longer_exists"
        paths = [
            f"reduce_drivers_of({problem})",
            f"build_capabilities_against({problem})",
            f"redesign_system_around({problem})",
        ]
        self.problem_truths = ProblemTruths(
            problem=problem,
            cause=cause,
            resolution=resolution,
            paths=paths,
        )
        return self.problem_truths

    # ----------------------------------------------------------------
    # 6) GENERATE OPTIONS FROM ATOMICS + PROBLEM TRUTHS
    # ----------------------------------------------------------------

    def generate_options(
        self,
        phenomenon: str,
        max_depth: int = 3,
        max_options: int = 20,
    ) -> List[OptionPlan]:
        """
        Generate candidate options by combining atomic truths
        up to a given depth.
        """
        if self.problem_truths is None:
            raise ValueError("define_problem_truths() must be called first")

        core_atoms = self.derive_core_truths(phenomenon)
        options: List[OptionPlan] = []

        for depth in range(1, max_depth + 1):
            for combo in itertools.combinations(core_atoms, depth):
                desc = self._describe_option(combo, self.problem_truths)
                options.append(
                    OptionPlan(atoms=list(combo), description=desc)
                )
                if len(options) >= max_options:
                    return options

        return options

    def _describe_option(
        self, atoms: Iterable[AtomicTruth], pt: ProblemTruths
    ) -> str:
        keys = [a.key for a in atoms]
        return (
            f"Use {keys} to move from "
            f"problem='{pt.problem}' toward resolution='{pt.resolution}'"
        )

    # ----------------------------------------------------------------
    # 7) RELATIVITY LAYER – EVALUATE BY FRAME
    # ----------------------------------------------------------------

    def evaluate_option_in_frame(
        self, option: OptionPlan, frame: str
    ) -> float:
        """
        Scoring heuristic per frame.
        Score > 0 is good. Higher is better.
        """
        base = len(option.atoms)

        if frame == "self_now":
            # prefer simple, executable now
            return 10.0 / (1 + base)

        if frame == "self_10y":
            # prefer compounding + leverage
            has_compound = any(a.key == "compounding" for a in option.atoms)
            has_lev = any(a.key == "leverage" for a in option.atoms)
            return (5.0 + 3.0 * has_compound + 2.0 * has_lev) * math.log(
                1 + base
            )

        if frame == "customer":
            # prefer incentives + information clarity
            has_incentive = any(a.key == "incentives" for a in option.atoms)
            has_info = any(a.key == "information" for a in option.atoms)
            return 3.0 * has_incentive + 3.0 * has_info

        if frame == "market":
            # prefer feedback + leverage (adaptivity)
            has_fb = any(a.key == "feedback" for a in option.atoms)
            has_lev = any(a.key == "leverage" for a in option.atoms)
            return 2.0 * has_fb + 2.0 * has_lev

        if frame == "system":
            # prefer entropy awareness + feedback (stability)
            has_ent = any(a.key == "entropy" for a in option.atoms)
            has_fb = any(a.key == "feedback" for a in option.atoms)
            return 2.0 * has_ent + 2.0 * has_fb

        # default neutral
        return float(base)

    def evaluate_all_frames(self, option: OptionPlan) -> None:
        option.score_by_frame = {
            f: self.evaluate_option_in_frame(option, f)
            for f in self.frames
        }

    # ----------------------------------------------------------------
    # 8) SYSTEM THINKING++ – SIMULATE LEVERAGE & PROBLEM REDUCTION
    # ----------------------------------------------------------------

    def simulate_system_effects(self, option: OptionPlan) -> None:
        """
        Very compact proxy:
        - system_leverage ~ how many system-level atoms involved
        - problem_reduction ~ weighted sum of frame scores
        """
        system_keys = {"entropy", "feedback", "leverage", "compounding"}
        system_count = sum(1 for a in option.atoms if a.key in system_keys)
        option.system_leverage = float(system_count)

        if not option.score_by_frame:
            self.evaluate_all_frames(option)

        total = sum(option.score_by_frame.values())
        option.problem_reduction = total / max(1, len(self.frames))

    # ----------------------------------------------------------------
    # 9) CHOOSE BEST OPTION
    # ----------------------------------------------------------------

    def select_best_option(self, options: List[OptionPlan]) -> OptionPlan:
        """
        Select option that:
            - maximizes problem_reduction
            - then maximizes system_leverage
        """
        for op in options:
            self.evaluate_all_frames(op)
            self.simulate_system_effects(op)

        return max(
            options,
            key=lambda op: (op.problem_reduction, op.system_leverage),
        )


# --------------------------------------------------------------------
# 10) DEMO USAGE
# --------------------------------------------------------------------

if __name__ == "__main__":
    codex = FirstPrincipleCodex()

    # 1) นิยามปัญหาแบบสากล (Problem Truths)
    pt = codex.define_problem_truths(
        "retail_investors_lose_money_from_surface_level_thinking"
    )

    # 2) สร้างตัวเลือกจาก First Principles ที่เกี่ยวข้อง
    options = codex.generate_options(
        phenomenon="finance_entropy_investor_behavior"
    )

    # 3) เลือกทางที่ดีที่สุดตามกรอบอ้างอิง + ระบบ
    best = codex.select_best_option(options)

    print("=== PROBLEM TRUTHS ===")
    print(pt)
    print("\n=== BEST OPTION (First Principle Codex) ===")
    print("Description:", best.description)
    print("Frames:", best.score_by_frame)
    print("System leverage:", best.system_leverage)
    print("Problem reduction:", best.problem_reduction)
