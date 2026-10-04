from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

from .base_store import MemoryRecord, MemoryStore


@dataclass
class ProjectMemoryEntry:
    project_id: str
    project_name: str
    version: str
    data: Dict[str, Any]
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


class ProjectMemory(MemoryStore):
    """Simple project memory store used for project lifecycle tracking."""

    def __init__(self):
        self._records: Dict[str, MemoryRecord] = {}

    def save(self, key: str, value: Dict[str, Any], metadata: Optional[Dict[str, Any]] = None) -> MemoryRecord:
        record = MemoryRecord(key=key, value=value, metadata=metadata or {})
        self._records[key] = record
        return record

    def get(self, key: str) -> Optional[MemoryRecord]:
        return self._records.get(key)

    def list(self) -> List[MemoryRecord]:
        return list(self._records.values())

    def delete(self, key: str) -> None:
        self._records.pop(key, None)

    def create_project(self, project_id: str, project_name: str, version: str = "v0.1") -> ProjectMemoryEntry:
        entry = ProjectMemoryEntry(project_id=project_id, project_name=project_name, version=version, data={})
        self.save(f"project:{project_id}:{version}", entry.__dict__)
        return entry

    def update_project(self, project_id: str, version: str, updates: Dict[str, Any]) -> ProjectMemoryEntry:
        key = f"project:{project_id}:{version}"
        existing = self.get(key)
        payload = dict(existing.value) if existing else {}
        payload.update(updates)
        self.save(key, payload)
        return ProjectMemoryEntry(project_id=project_id, project_name=payload.get("project_name", ""), version=version, data=payload)

    def project_versions(self, project_id: str) -> List[ProjectMemoryEntry]:
        entries: List[ProjectMemoryEntry] = []
        for item in self.list():
            if item.key.startswith(f"project:{project_id}:"):
                data = item.value
                entries.append(
                    ProjectMemoryEntry(
                        project_id=project_id,
                        project_name=data.get("project_name", ""),
                        version=data.get("version", "v0.1"),
                        data=data,
                    )
                )
        return entries
