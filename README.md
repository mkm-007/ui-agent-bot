# UI Component Agent Bot

**Resume project · SPT work unit**  
**Capability:** natural-language UI intent → structured component plan → Angular-ready stub  
**Background:** Centre for Advanced Technology Solutions, GITAM · May 2024 – Dec 2024  
**Stack:** Python agent · component catalog · Angular-style TypeScript stubs

---

## Problem

Internal UI prototyping was slow when every request started from a blank component. Staff/dev requests needed a controllable path from language → component → stub — not an open-ended chat toy.

## What I built

1. Parse a natural-language UI request  
2. Plan which catalog component to emit  
3. Emit an Angular-ready stub (plan → act → emit)  

Resume anchor: *Built an agent that maps natural-language UI requests to component specs and emits Angular-ready stubs. Owned plan–act–emit loop and front-end integration for faster internal UI prototyping.*

## SPT bar (junior standard)

| Step | Artifact |
|------|----------|
| Build | `src/ui_agent/` · `frontend/` |
| Verify | `python -m pytest -q` |
| Demo | `python run_demo.py` · [`demo_output.txt`](./demo_output.txt) |
| Document | this README |

## Quick start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
python run_demo.py
```

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

Full Experience · Projects · SPT → [mkm-007/MKM](https://github.com/mkm-007/MKM)
