"""Tool registry and execution layer."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class ToolSpec:
    name: str
    description: str
    input_schema: Dict[str, Any]
    output_schema: Dict[str, Any]
    permissions: List[str] = field(default_factory=list)


class ToolRegistry:
    """Minimal tool registry with permission metadata."""

    def __init__(self):
        self._tools: Dict[str, ToolSpec] = {}

    def register(self, spec: ToolSpec) -> None:
        self._tools[spec.name] = spec

    def list_tools(self) -> List[str]:
        return sorted(self._tools.keys())

    def get(self, name: str) -> Optional[ToolSpec]:
        return self._tools.get(name)

    def execute(self, name: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        spec = self.get(name)
        if spec is None:
            raise ValueError(f"Tool not registered: {name}")
        return {"tool": name, "result": payload, "permissions": spec.permissions}
