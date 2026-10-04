from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class SimulationScenario:
    name: str
    parameters: Dict[str, float]
    initial_conditions: Dict[str, float]
    time_steps: int = 100


@dataclass
class SimulationResult:
    scenario: str
    outputs: Dict[str, float]
    signal: str
    notes: List[str] = field(default_factory=list)


class SimulationEngine:
    """Simple parameterized simulation framework with sweep support."""

    def run_scenario(self, scenario: SimulationScenario) -> SimulationResult:
        base = scenario.parameters.get("base", 1.0)
        gain = scenario.parameters.get("gain", 0.5)
        time_steps = scenario.time_steps
        outputs = {"final_value": base + gain * time_steps}
        return SimulationResult(
            scenario=scenario.name,
            outputs=outputs,
            signal="SIMULATION_RESULT",
            notes=["This is a numerical approximation, not real-world validation."],
        )

    def run_sweep(self, scenarios: List[SimulationScenario]) -> List[SimulationResult]:
        return [self.run_scenario(s) for s in scenarios]

    def execute(self, task: Any) -> Dict[str, Any]:
        context = getattr(task, "context", {}) or {}
        scenario = SimulationScenario(
            name=context.get("name", "baseline"),
            parameters=context.get("parameters", {"base": 1.0, "gain": 0.1}),
            initial_conditions=context.get("initial_conditions", {"x0": 0.0}),
            time_steps=int(context.get("time_steps", 100)),
        )
        result = self.run_scenario(scenario)
        return {
            "status": "SIMULATION_RESULT",
            "scenario": result.scenario,
            "outputs": result.outputs,
            "notes": result.notes,
        }
