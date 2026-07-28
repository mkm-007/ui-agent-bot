from __future__ import annotations

COMPONENT_CATALOG = {
    "button": {
        "name": "AppButton",
        "selector": "app-button",
        "inputs": ["label", "variant"],
    },
    "data-table": {
        "name": "AppDataTable",
        "selector": "app-data-table",
        "inputs": ["columns", "rows"],
    },
    "card": {
        "name": "AppCard",
        "selector": "app-card",
        "inputs": ["title", "body"],
    },
}


def render_angular_stub(component: dict, request: str) -> str:
    """Emit a TypeScript Angular-style component stub from the agent decision."""
    name = component["name"]
    selector = component["selector"]
    inputs = ", ".join(f"@Input() {i}: any;" for i in component["inputs"])
    return f"""// Generated from request: {request}
import {{ Component, Input }} from '@angular/core';

@Component({{
  selector: '{selector}',
  template: `<div class="{selector}">{{{{ /* bound inputs */ }}}}</div>`,
}})
export class {name} {{
  {inputs}
}}
"""
