from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import os


@dataclass
class Settings:
    """Application-level settings for TONY-X.

    This keeps configuration explicit and easy to extend.
    """

    app_name: str = "TONY-X"
    app_version: str = "0.1.0"
    project_root: Path = field(default_factory=lambda: Path(__file__).resolve().parents[2])
    environment: str = field(default_factory=lambda: os.getenv("TONY_X_ENV", "development"))
    log_level: str = field(default_factory=lambda: os.getenv("TONY_X_LOG_LEVEL", "INFO"))
    database_url: str = field(default_factory=lambda: os.getenv("TONY_X_DATABASE_URL", "sqlite:///tony_x.db"))
    research_enabled: bool = field(default_factory=lambda: os.getenv("TONY_X_RESEARCH_ENABLED", "true").lower() == "true")
    simulation_enabled: bool = field(default_factory=lambda: os.getenv("TONY_X_SIMULATION_ENABLED", "true").lower() == "true")

    def as_dict(self) -> dict:
        return {
            "app_name": self.app_name,
            "app_version": self.app_version,
            "environment": self.environment,
            "log_level": self.log_level,
            "database_url": self.database_url,
            "research_enabled": self.research_enabled,
            "simulation_enabled": self.simulation_enabled,
        }


DEFAULT_SETTINGS = Settings()
