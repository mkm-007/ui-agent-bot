# UI Component Agent Bot

Agent that maps natural-language UI requests to component specs and emits Angular-ready stubs.

**Background:** Centre for Advanced Technology Solutions, GITAM · May 2024 – Dec 2024  
**Stack:** Python agent · component catalog · Angular-style TypeScript stubs

---

## Problem

Internal UI prototyping was slow when every request started from a blank component. Staff/dev requests needed a controllable path from language → component → stub — not an open-ended chat toy.

## What it does

1. Parse a natural-language UI request  
2. Plan which catalog component to emit  
3. Emit an Angular-ready stub (plan → act → emit)  

## Quick start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
python run_demo.py
```

Demo output: [`demo_output.txt`](./demo_output.txt)

## Design notes

- Catalog-constrained components beat free-form codegen for predictable handoff  
- Explicit plan–act–emit loop makes agent behavior interviewable and testable  
- Frontend stubs under `frontend/` show the integration surface for Angular work  

## Layout

```
src/ui_agent/
frontend/
tests/
extensions/
run_demo.py
demo_output.txt
```

## Portfolio

[mkm-007/MKM](https://github.com/mkm-007/MKM) · [Live site](https://mkm-007.github.io/MKM/)
