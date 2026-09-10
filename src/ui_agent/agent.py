"""Deterministic catalog planner with explicit refusal and separate bindings."""
from copy import deepcopy
import re
from ui_agent.catalog import COMPONENT_CATALOG, render_angular_stub


def select_component(request):
    if not isinstance(request, str) or not request.strip() or len(request) > 1000:
        raise ValueError('Request must contain 1-1000 characters')
    # Quoted labels are data, not component intent.
    intent = re.sub(r'"[^"]*"|\x27[^\x27]*\x27', '', request.lower())
    matches = [key for key, pattern in [('data-table', r'\b(table|grid)\b'), ('button', r'\bbutton\b'), ('card', r'\bcard\b')] if re.search(pattern, intent)]
    if len(matches) != 1:
        raise ValueError('Request exactly one supported component: button, table/grid, or card')
    return deepcopy(COMPONENT_CATALOG[matches[0]])


def plan_steps(request):
    component = select_component(request)
    configure = {'AppButton': 'configure_label_style', 'AppDataTable': 'configure_columns', 'AppCard': 'configure_content'}
    return ['parse_intent', 'select_component', configure[component['name']], 'validate_spec', 'emit_angular_stub']


def run_agent(request):
    component = select_component(request)
    props = {}
    if component['name'] == 'AppButton':
        match = re.search(r'\blabel(?:ed)?\s+["\x27]?(.+?)["\x27]?$', request, re.I)
        props = {'label': match.group(1) if match else 'Submit', 'variant': 'secondary' if re.search(r'\bsecondary\b', request, re.I) else 'primary'}
    elif component['name'] == 'AppDataTable':
        match = re.search(r'\bwith (.+?) columns\b', request, re.I)
        props = {'columns': [x.strip() for x in re.split(r',|\band\b', match.group(1)) if x.strip()] if match else [], 'rows': []}
    else:
        props = {'title': 'Card', 'body': ''}
    return {'mode': 'deterministic', 'plan': plan_steps(request), 'component': component,
            'props': props, 'stub': render_angular_stub(component)}
