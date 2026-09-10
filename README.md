# UI Component Agent Bot

Convert one supported UI request into a typed Angular component and separate input properties.

> **Independent portfolio reconstruction.** Inspired by project categories I worked on while gaining practical experience at CATS, GITAM. I do not have access to the original CATS codebases. This repository was created later with AI coding assistance (Cursor/Codex), uses demonstration inputs, and is not original institutional code or evidence of a production deployment. Features and tests below describe this reconstruction only.

## Try it

Python 3.11+; the runtime uses only Python's standard library. No API keys or paid services are needed.

```bash
python -m venv .venv
source .venv/bin/activate
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m pytest -q
python run_demo.py
python run_demo.py --request "Add a table with name and department columns"
```

The checked-in [demo output](demo_output.txt) is generated from the current implementation. Tests run automatically on pushes and pull requests.

## Architecture

```text
Request → catalog selection → validated specification → fixed Angular template + JSON properties
```

## Implemented

- Button, table/grid, and card components with typed inputs and standalone declarations.
- Button label/variant and table column extraction into data properties.
- Unsupported and ambiguous requests fail explicitly.
- User text is never interpolated into generated source; catalog results are copied to prevent mutation.
- Angular compiler configuration validates all three emitted templates.

## Scope and limitations

This is a deterministic catalog workflow, not an autonomous LLM agent. It emits components; it does not insert them into an existing app, supply a live preview, or automatically bind returned properties. Integrators must bind props as Angular inputs. Arbitrary component requests and complex language are unsupported. Compiler checks do not establish browser usability or full accessibility compliance.

## Verification

`tests/` covers successful requests and failure cases. Read the tests alongside the source; test counts are evidence of exercised cases, not a claim of production readiness. [Engineering notes](ENGINEERING.md) explain boundaries and review prompts.

## Background and attribution

The historical CATS work involved Angular, Python, LLM consumption, database querying, document retrieval, and agent-oriented UI workflows, as described by the portfolio owner. Those historical technologies are not automatically dependencies or implemented capabilities here. Public reconstruction work must be described separately from institutional experience in resumes and interviews. Do not backdate these commits or claim institutional adoption.

AI tools assisted implementation. The portfolio owner should run the demo, inspect the code, and be able to explain its decisions and limitations before presenting it as personal proficiency. No confidential CATS code, data, or documents are included.

[Portfolio](https://github.com/mkm-007/MKM)

## Compile generated Angular components

Node 24 and npm are required for this optional check. Angular 20.3 and TypeScript 5.9 are locked through `frontend/package-lock.json`.

```bash
python scripts/generate_examples.py
cd frontend
npm ci --ignore-scripts
npm run check
```

`frontend/generated/` contains the emitted examples; `props` in the Python result must be supplied as inputs by a host application. The compiler check validates TypeScript and Angular templates, not an end-to-end web app.
