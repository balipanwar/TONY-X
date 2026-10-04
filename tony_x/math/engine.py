from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional

import numpy as np


@dataclass
class MathResult:
    inputs: Dict[str, Any]
    equations: List[str]
    assumptions: List[str]
    result: float
    units: str = "dimensionless"
    uncertainty: Optional[float] = None


class MathEngine:
    """Small but expandable math engine for algebra, stats, and numerics."""

    def solve_quadratic(self, a: float, b: float, c: float) -> Dict[str, float]:
        disc = (b ** 2) - 4 * a * c
        if disc < 0:
            raise ValueError("Quadratic has no real roots")
        root1 = (-b + np.sqrt(disc)) / (2 * a)
        root2 = (-b - np.sqrt(disc)) / (2 * a)
        return {"root_1": float(root1), "root_2": float(root2)}

    def mean(self, values: List[float]) -> float:
        return float(np.mean(values))

    def std_dev(self, values: List[float]) -> float:
        return float(np.std(values, ddof=1)) if len(values) > 1 else 0.0

    def trapezoid_integral(self, x: List[float], y: List[float]) -> float:
        if len(x) != len(y):
            raise ValueError("x and y arrays must have same length")
        return float(np.trapz(y, x))

    def determinant(self, matrix: List[List[float]]) -> float:
        arr = np.array(matrix, dtype=float)
        return float(np.linalg.det(arr))

    def execute(self, task: Any) -> Dict[str, Any]:
        context = getattr(task, "context", {}) or {}
        values = context.get("values", [1.0, 2.0, 3.0])
        result = {
            "mean": self.mean(values),
            "std_dev": self.std_dev(values),
            "inputs": context,
            "assumptions": ["Values are treated as numeric samples.", "No external model calibration has been applied."],
            "status": "CALCULATED_RESULT",
        }
        return result
