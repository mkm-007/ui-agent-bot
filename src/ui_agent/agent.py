from __future__ import annotations

from ui_agent.catalog import COMPONENT_CATALOG, render_angular_stub


def plan_steps(request: str) -> list[str]:
    r = request.lower()
    steps = ["parse_intent", "select_component"]
    if "table" in r or "grid" in r:
        steps.append("configure_columns")
    if "button" in r:
        steps.append("configure_label_style")
    steps.append("emit_angular_stub")
    return steps


def select_component(request: str) -> dict:
    r = request.lower()
    if "table" in r or "grid" in r:
        return COMPONENT_CATALOG["data-table"]
    if "button" in r:
        return COMPONENT_CATALOG["button"]
    return COMPONENT_CATALOG["card"]


def run_agent(request: str) -> dict:
    """Minimal agentic loop: plan → act → emit artifact."""
    plan = plan_steps(request)
    component = select_component(request)
    stub = render_angular_stub(component, request)
    return {"plan": plan, "component": component, "stub": stub}
