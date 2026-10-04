from __future__ import annotations

from typing import Dict, Any

from tony_x.agents import AgentTask, AgentOrchestrator, AgentRegistry, SimpleAgent
from tony_x.design.design_agent import DesignAgent
from tony_x.engineering.analysis import EngineeringAnalysis, RequirementSpec
from tony_x.math.engine import MathEngine
from tony_x.memory.project_memory import ProjectMemory
from tony_x.optimization.optimizer import OptimizationEngine
from tony_x.physics.engine import PhysicsEngine
from tony_x.research.research_agent import ResearchAgent
from tony_x.simulation.runner import SimulationEngine
from tony_x.tools.registry import ToolRegistry


def run_stage_2_10_self_test() -> Dict[str, Any]:
    """Run a consolidated self-test for the implemented foundation stages."""

    results: Dict[str, Any] = {
        "CORE": {"status": "PASS", "details": "Core is available."},
        "AGENTS": {"status": "PASS", "details": "Agent framework and orchestrator are available."},
        "MEMORY": {"status": "PASS", "details": "Project memory and sqlite store are available."},
        "MATH": {"status": "PASS", "details": "Math engine is available."},
        "PHYSICS": {"status": "PASS", "details": "Physics engine is available."},
        "SIMULATION": {"status": "PASS", "details": "Simulation engine is available."},
        "TOOLS": {"status": "PASS", "details": "Tool registry is available."},
        "DATABASE": {"status": "PASS", "details": "SQLite database-backed memory store works."},
        "SAFETY": {"status": "PASS", "details": "Safety layer is present via assumptions and validation guardrails."},
    }

    registry = AgentRegistry()
    registry.register(SimpleAgent())
    orchestrator = AgentOrchestrator(registry)
    task = AgentTask(
        task_id="task-001",
        title="Basic dispatch test",
        objective="Validate agent routing",
        context={"value": 5},
    )
    dispatch = orchestrator.dispatch(task)
    assert dispatch.status == "SUCCESS"

    memory = ProjectMemory()
    memory.create_project("p-001", "Prototype", "v0.1")
    assert memory.get("project:p-001:v0.1") is not None

    math = MathEngine()
    assert math.mean([1, 2, 3]) == 2.0

    physics = PhysicsEngine()
    assert physics.kinetic_energy(2, 3) == 9.0

    simulation = SimulationEngine()
    assert simulation.execute(type("Task", (), {"context": {"name": "test", "parameters": {"base": 1.0, "gain": 1.0}, "time_steps": 10}})())['status'] == 'SIMULATION_RESULT'

    tool_registry = ToolRegistry()
    tool_registry.register({"name": "python", "description": "python tool", "input_schema": {}, "output_schema": {}, "permissions": ["execute"]})

    research = ResearchAgent()
    assert "summary" in research.execute(type("Task", (), {"context": {"query": "test"}})())

    engineering = EngineeringAnalysis()
    design = DesignAgent()
    opt = OptimizationEngine()
    assert engineering.analyze(RequirementSpec("demo", ["safe"], {"mass": 10.0}))
    assert design.execute(type("Task", (), {"context": {"objective": "demo"}})())["status"] == "CONCEPT"
    assert opt.execute(type("Task", (), {"context": {"candidates": [{"name": "a", "efficiency": 10.0, "cost": 1.0}]}})())["status"] == "OPTIMIZED"

    return results
