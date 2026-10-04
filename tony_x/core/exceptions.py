"""Custom exception definitions for TONY-X."""


class TONYXError(Exception):
    """Base exception for TONY-X application errors."""


class ConfigurationError(TONYXError):
    """Raised when configuration cannot be loaded or validated."""


class ProjectError(TONYXError):
    """Raised when a project cannot be created or updated safely."""


class AgentError(TONYXError):
    """Raised when an agent fails to execute a task."""


class ToolExecutionError(TONYXError):
    """Raised when an external tool fails during execution."""
