"""Interactive local demo. Run with Python 3.11 or newer; no dependencies."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent / 'src'))

import json
import tempfile
from ui_agent.agent import run_agent

def main():
    print('Angular component generator')
    print('Try: Add a primary button labeled Submit')
    print('Or: Add a table with name and department columns | Add a card')
    print('Type save to export the last result, or quit to exit.\n')
    last = None
    while True:
        try:
            request = input('Request> ').strip()
        except (EOFError, KeyboardInterrupt):
            print('\nGoodbye.'); return
        if request.lower() in {'quit', 'exit'}:
            print('Goodbye.'); return
        if not request:
            continue
        if request.lower() == 'save':
            if last is None:
                print('Generate a component first.\n'); continue
            try:
                root = Path(__file__).resolve().parent / 'output'
                root.mkdir(exist_ok=True)
                folder = Path(tempfile.mkdtemp(prefix='component-', dir=root))
                (folder / 'component.ts').write_text(last['stub'], encoding='utf-8')
                (folder / 'props.json').write_text(json.dumps(last['props'], indent=2), encoding='utf-8')
                print(f'Saved component.ts and props.json in {folder}\n')
            except OSError as exc:
                print(f'Could not save files: {exc}\n')
            continue
        try:
            last = run_agent(request)
            print('Component:', last['component']['name'])
            print('Inputs:', json.dumps(last['props'], indent=2))
            print('\n' + last['stub'])
            print('Type save to export these files.\n')
        except ValueError as exc:
            last = None
            print(str(exc), '\n')

if __name__ == '__main__':
    main()
