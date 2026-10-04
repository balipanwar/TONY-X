"""Agent registration and orchestration for TONY-X."""

from .base_agent import AgentMessage, AgentResult, AgentTask, BaseAgent, SimpleAgent
from .registry import AgentRegistry
from .orchestrator import AgentOrchestrator

__all__ = [
    "AgentMessage",
    "AgentResult",
    "AgentTask",
    "BaseAgent",
    "SimpleAgent",
    "AgentRegistry",
    "AgentOrchestrator",
]
