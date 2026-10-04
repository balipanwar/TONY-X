"""Memory interfaces and implementation for project state."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class MemoryRecord:
    key: str
    value: Dict[str, Any]
    metadata: Dict[str, Any] = field(default_factory=dict)


class MemoryStore(ABC):
    """Persistent or transient memory interface."""

    @abstractmethod
    def save(self, key: str, value: Dict[str, Any], metadata: Optional[Dict[str, Any]] = None) -> MemoryRecord:
        raise NotImplementedError

    @abstractmethod
    def get(self, key: str) -> Optional[MemoryRecord]:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[MemoryRecord]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, key: str) -> None:
        raise NotImplementedError
