from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class DesignConcept:
    design_id: str
    objective: str
    requirements: List[str]
    constraints: List[str]
    architecture: str
    subsystems: List[str]
    risks: List[str]
    assumptions: List[str] = field(default_factory=list)


class DesignAgent:
    """Generates candidate engineering concepts from requirements."""

    def execute(self, task: Any) -> Dict[str, Any]:
        context = getattr(task, "context", {}) or {}
        objective = context.get("objective", "prototype system")
        requirements = context.get("requirements", ["safe operation", "modular architecture"])
        concept = DesignConcept(
            design_id=context.get("design_id", "D-001"),
            objective=objective,
            requirements=requirements,
            constraints=context.get("constraints", ["no unverified claims", "must include assumptions"]),
            architecture=context.get("architecture", "modular layered architecture"),
            subsystems=context.get("subsystems", ["controller", "power", "sensing", "thermal"]),
            risks=context.get("risks", ["under-specified performance", "model simplification"]),
            assumptions=["This is a conceptual design, not a validated physical implementation."],
        )
        return {
            "status": "CONCEPT",
            "design": concept.__dict__,
            "simulation_plan": ["Run parameter sweep", "Compare candidate options", "Validate assumptions"],
        }
