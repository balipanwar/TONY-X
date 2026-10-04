from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass
class AgentTask:
    """Structured task payload for an agent."""

    task_id: str
    title: str
    objective: str
    context: Dict[str, Any] = field(default_factory=dict)
    constraints: List[str] = field(default_factory=list)
    required_outputs: List[str] = field(default_factory=list)


@dataclass
class AgentMessage:
    """Structured agent-to-agent communication message."""

    message_id: str
    sender: str
    receiver: str
    task_id: str
    message_type: str
    payload: Dict[str, Any]
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


@dataclass
class AgentResult:
    """Structured result returned by an agent after task execution."""

    agent_name: str
    task_id: str
    status: str
    summary: str
    payload: Dict[str, Any] = field(default_factory=dict)
    confidence: float = 0.0
    errors: List[str] = field(default_factory=list)


class BaseAgent(ABC):
    """Abstract base class for all TONY-X agents."""

    name: str = "BASE_AGENT"
    description: str = "Generic agent"
    capabilities: List[str] = []

    def __init__(self, name: Optional[str] = None, description: Optional[str] = None):
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if not self.capabilities:
            self.capabilities = ["generic"]

    @abstractmethod
    def execute(self, task: AgentTask) -> AgentResult:
        """Execute a task and return a typed result."""


class SimpleAgent(BaseAgent):
    """Simple reference agent used for orchestration tests."""

    def __init__(self, name: str = "SIMPLE_AGENT", description: str = "Reference agent"):
        super().__init__(name=name, description=description)
        self.capabilities = ["simple", "task_execution"]

    def execute(self, task: AgentTask) -> AgentResult:
        return AgentResult(
            agent_name=self.name,
            task_id=task.task_id,
            status="SUCCESS",
            summary=f"Executed task: {task.title}",
            payload={"objective": task.objective, "context": task.context},
            confidence=0.85,
        )
