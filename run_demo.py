"""Emit a validated component specification and source as JSON."""
import argparse
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent / 'src'))
from ui_agent.agent import run_agent

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--request', default='Add a primary button labeled Submit')
    args = parser.parse_args()
    try:
        print(json.dumps(run_agent(args.request), indent=2))
    except ValueError as exc:
        print(json.dumps({'status': 'refused', 'error': str(exc)}))
        return 2
    return 0
if __name__ == '__main__':
    raise SystemExit(main())
