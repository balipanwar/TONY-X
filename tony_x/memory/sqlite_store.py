from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

from .base_store import MemoryRecord, MemoryStore


@dataclass
class SQLiteMemoryRecord(MemoryRecord):
    pass


class SQLiteMemoryStore(MemoryStore):
    """A lightweight SQLite-backed memory store."""

    def __init__(self, db_path: str = "tony_x.db"):
        self.db_path = db_path
        self._initialize_db()

    def _initialize_db(self) -> None:
        conn = sqlite3.connect(self.db_path)
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS memory (
                key TEXT PRIMARY KEY,
                value TEXT NOT NULL,
                metadata TEXT,
                created_at TEXT NOT NULL
            )
            """
        )
        conn.commit()
        conn.close()

    def save(self, key: str, value: Dict[str, Any], metadata: Optional[Dict[str, Any]] = None) -> MemoryRecord:
        import json

        conn = sqlite3.connect(self.db_path)
        conn.execute(
            "INSERT OR REPLACE INTO memory(key, value, metadata, created_at) VALUES (?, ?, ?, ?)",
            (
                key,
                json.dumps(value),
                json.dumps(metadata or {}),
                datetime.now(timezone.utc).isoformat(),
            ),
        )
        conn.commit()
        conn.close()
        return MemoryRecord(key=key, value=value, metadata=metadata or {})

    def get(self, key: str) -> Optional[MemoryRecord]:
        import json

        conn = sqlite3.connect(self.db_path)
        row = conn.execute(
            "SELECT key, value, metadata FROM memory WHERE key = ?",
            (key,),
        ).fetchone()
        conn.close()

        if row is None:
            return None
        return MemoryRecord(key=row[0], value=json.loads(row[1]), metadata=json.loads(row[2] or "{}"))

    def list(self) -> List[MemoryRecord]:
        import json

        conn = sqlite3.connect(self.db_path)
        rows = conn.execute("SELECT key, value, metadata FROM memory").fetchall()
        conn.close()
        return [MemoryRecord(key=row[0], value=json.loads(row[1]), metadata=json.loads(row[2] or "{}")) for row in rows]

    def delete(self, key: str) -> None:
        conn = sqlite3.connect(self.db_path)
        conn.execute("DELETE FROM memory WHERE key = ?", (key,))
        conn.commit()
        conn.close()
