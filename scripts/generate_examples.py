"""Emit all catalog components for an actual Angular compiler check."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from ui_agent.agent import run_agent
root = Path(__file__).resolve().parents[1] / 'frontend' / 'generated'
root.mkdir(exist_ok=True)
for kind in ['button', 'table', 'card']:
    (root / f'{kind}.ts').write_text(run_agent(f'Add a {kind}')['stub'])
