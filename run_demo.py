"""Demo: NL request → agent plan → Angular component stub."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from ui_agent.agent import run_agent


def main() -> None:
    requests = [
        "Add a primary button labeled Submit",
        "Add a data table for employees with name and department columns",
    ]
    for req in requests:
        result = run_agent(req)
        print(f"Request: {req}")
        print(f"Plan: {result['plan']}")
        print(f"Component: {result['component']['name']}")
        print(f"Stub preview:\n{result['stub'][:240]}...")
        print("---")


if __name__ == "__main__":
    main()
