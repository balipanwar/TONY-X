from __future__ import annotations

from typing import Dict, List, Optional

from .base_agent import BaseAgent


class AgentRegistry:
    """Registry that stores and retrieves agent implementations."""

    def __init__(self):
        self._agents: Dict[str, BaseAgent] = {}

    def register(self, agent: BaseAgent) -> None:
        self._agents[agent.name] = agent

    def unregister(self, agent_name: str) -> None:
        self._agents.pop(agent_name, None)

    def get(self, agent_name: str) -> Optional[BaseAgent]:
        return self._agents.get(agent_name)

    def list_agents(self) -> List[str]:
        return sorted(self._agents.keys())

    def has_agent(self, agent_name: str) -> bool:
        return agent_name in self._agents

    def clear(self) -> None:
        self._agents.clear()
