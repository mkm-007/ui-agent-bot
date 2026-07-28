# UI Component Agent Bot

Agent that maps natural-language UI requests to component specs and emits Angular-ready stubs (plan → act → emit).

**Origin:** Centre for Advanced Technology Solutions, GITAM University (May 2024 – Dec 2024)  
**Stack:** Python agent · component catalog · Angular-style TypeScript stubs

## Quick start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
python run_demo.py
```

## What it does

1. Accept a natural-language UI request
2. Plan which component to emit
3. Produce an Angular-ready stub from the catalog

See [`demo_output.txt`](./demo_output.txt) for a captured run. Frontend stubs live under `frontend/`.

## Layout

```
src/ui_agent/      # agent planner + component catalog
frontend/          # Angular-style component stubs (TS)
tests/
extensions/        # JD add-ons (LangChain tools, richer UI)
run_demo.py
demo_output.txt
```

## Resume anchor

Built an agent that maps natural-language UI requests to component specs and emits Angular-ready stubs. Owned plan–act–emit loop and front-end integration for faster internal UI prototyping.

## License

Personal portfolio / educational use.
