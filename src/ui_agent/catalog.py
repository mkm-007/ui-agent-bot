"""Fixed Angular templates: user text never becomes executable source."""
from copy import deepcopy

COMPONENT_CATALOG = {
    'button': {'name': 'AppButton', 'selector': 'app-button', 'inputs': ['label', 'variant']},
    'data-table': {'name': 'AppDataTable', 'selector': 'app-data-table', 'inputs': ['columns', 'rows']},
    'card': {'name': 'AppCard', 'selector': 'app-card', 'inputs': ['title', 'body']},
}
TEMPLATES = {
    'app-button': ('<button type="button" [attr.data-variant]="variant">{{ label }}</button>', "@Input() label: string = 'Submit';\n  @Input() variant: 'primary' | 'secondary' = 'primary';"),
    'app-card': ('<article><h2>{{ title }}</h2><p>{{ body }}</p></article>', "@Input() title: string = 'Card';\n  @Input() body: string = '';"),
    'app-data-table': ('<table><caption>{{ caption }}</caption><thead><tr><th scope="col" *ngFor="let column of columns">{{ column }}</th></tr></thead><tbody><tr *ngFor="let row of rows"><td *ngFor="let column of columns">{{ row[column] }}</td></tr></tbody></table>', "@Input() caption: string = 'Data';\n  @Input() columns: string[] = [];\n  @Input() rows: Record<string, string | number>[] = [];"),
}


def render_angular_stub(component, request=''):
    """Emit a complete standalone component; request is deliberately not interpolated."""
    selector = component['selector']
    canonical = next((c for c in COMPONENT_CATALOG.values() if c['selector'] == selector), None)
    if component != canonical:
        raise ValueError('Only catalog components can be rendered')
    template, inputs = TEMPLATES[selector]
    return f'''import {{ Component, Input }} from '@angular/core';
import {{ CommonModule }} from '@angular/common';

@Component({{
  selector: '{selector}',
  standalone: true,
  imports: [CommonModule],
  template: `{template}`,
}})
export class {component['name']} {{
  {inputs}
}}
'''
