from __future__ import annotations

from typing import List, Optional

from .base_agent import AgentTask, AgentResult
from .registry import AgentRegistry


class AgentOrchestrator:
    """Route tasks to agents based on registration and capability metadata."""

    def __init__(self, agent_registry: Optional[AgentRegistry] = None):
        self.registry = agent_registry or AgentRegistry()

    def register_agent(self, agent) -> None:
        self.registry.register(agent)

    def dispatch(self, task: AgentTask, agent_name: Optional[str] = None) -> AgentResult:
        if agent_name is None:
            if not self.registry.list_agents():
                raise ValueError("No registered agents available for dispatch")
            agent_name = self.registry.list_agents()[0]

        agent = self.registry.get(agent_name)
        if agent is None:
            raise ValueError(f"Unknown agent: {agent_name}")

        return agent.execute(task)

    def available_agents(self) -> List[str]:
        return self.registry.list_agents()
