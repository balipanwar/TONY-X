from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class PhysicsModel:
    name: str
    inputs: Dict[str, float]
    assumptions: List[str] = field(default_factory=list)
    equations: List[str] = field(default_factory=list)
    result: Dict[str, float] = field(default_factory=dict)


class PhysicsEngine:
    """Basic physics approximations with explicit assumptions."""

    def projectile_range(self, velocity: float, angle_deg: float, g: float = 9.81) -> Dict[str, float]:
        theta = angle_deg * 3.141592653589793 / 180.0
        range_value = (velocity ** 2 * np.sin(2 * theta)) / g
        return {"range_m": float(range_value), "assumptions": ["Level ground and no drag"]}

    def kinetic_energy(self, mass_kg: float, velocity_m_s: float) -> float:
        return 0.5 * mass_kg * velocity_m_s ** 2

    def ideal_gas_pressure(self, n_moles: float, temperature_k: float, volume_m3: float) -> float:
        gas_constant = 8.31446261815324
        return (n_moles * gas_constant * temperature_k) / volume_m3

    def execute(self, task: Any) -> Dict[str, Any]:
        context = getattr(task, "context", {}) or {}
        velocity = float(context.get("velocity", 10.0))
        angle_deg = float(context.get("angle_deg", 45.0))
        mass = float(context.get("mass_kg", 1.0))
        return {
            "status": "SIMULATION_RESULT",
            "assumptions": ["Neglect drag and atmospheric resistance.", "Fields are treated as idealized."],
            "projectile_range_m": self.projectile_range(velocity, angle_deg)["range_m"],
            "kinetic_energy_j": self.kinetic_energy(mass, velocity),
            "equations": [
                "R = v^2 sin(2θ)/g",
                "KE = 0.5 * m * v^2",
                "PV = nRT",
            ],
        }
