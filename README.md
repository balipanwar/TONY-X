# TONY-X

Technology Research & Invention AI.

This repository is the staged foundation for a modular, real scientific-engineering AI system.

## Current Stage

Stage 1: Core + Configuration

This stage establishes:
- Python project scaffolding
- configuration system
- logging
- application exceptions
- CLI entrypoint
- self-test harness
- package structure for future agent modules

## Status

The codebase is intentionally minimal but production-oriented and modular. It is designed to expand through future engineering stages without breaking the foundation.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m tony_x.cli --self-test
```

## CLI

```bash
tony --self-test
```
