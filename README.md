# UI Component Agent Bot

Turn a short UI request into an Angular button, table, or card. The tool returns a component file and separate input values, keeping the generated code predictable and easy to inspect.

## Run it on your computer

You need **Python 3.11 or newer**. Check with `python3 --version` on macOS/Linux or `py -3 --version` on Windows. If Python is missing, install it from [python.org](https://www.python.org/downloads/) and reopen your terminal.

### 1. Download the project

If you have Git, run:

```bash
git clone https://github.com/mkm-007/ui-agent-bot.git
cd ui-agent-bot
```

Without Git: select **Code → Download ZIP** on this GitHub page, extract the ZIP, and open a terminal in the extracted folder. You should see `README.md`, `start.py`, and `run_demo.py` in that folder. Open the folder in VS Code and choose **Terminal → New Terminal** if that is easier.

### 2. Start the interactive demo

**macOS / Linux:**

```bash
python3 start.py
```

**Windows PowerShell:**

```powershell
py -3 start.py
```

No package installation, API key, database account, or paid service is needed for this step. This is a terminal program: type your question/request at its prompt and press Enter. Type `quit` to stop, or press Ctrl+C.

Try this first:

```text
Add a primary button labeled Submit
```

The tool selects **AppButton**, with label **Submit** and variant **primary**. In interactive mode, type **save** after a result to write the component and its properties to a new folder under `output/`.

### 3. Run a single request

For scripts or a structured JSON response, use:

```bash
python3 run_demo.py --request "Add a primary button labeled Submit"
```

On Windows, replace `python3` with `py -3`. See [sample output](demo_output.txt) for a complete response. These commands finish after one request; `start.py` stays open for more.

## Requests to try

```text
Add a primary button labeled Submit
Add a secondary button labeled Cancel
Add a table with name and department columns
Add a card
```

Ask for one component at a time. A request for both a button and a card is rejected rather than choosing one arbitrarily. The supported properties are button label/variant and table columns. Card content uses defaults that you can edit.

## What happens when you run it

1. The Python program selects a component from the catalog.
2. It extracts supported input values into a `props` object.
3. It emits a complete standalone Angular component from a fixed template.
4. You can inspect or save the component and its properties.

Python generation needs no Node installation. It produces source files, **not a running website**. To use a generated file in your Angular application, import its component into the parent and bind the returned properties as inputs. For a button:

```html
<app-button [label]="'Submit'" [variant]="'primary'"></app-button>
```

Import `AppButton` from the saved component file in your parent component and add it to the parent's `imports` array. A table also needs row data; generation supplies an empty `rows` array.

## Check the Angular output

This optional check compiles the three example components. It does not start a browser app. Install **Node.js 24** (which includes npm) first, then run these commands from the repository folder:

```bash
python3 scripts/generate_examples.py
cd frontend
npm ci --ignore-scripts
npm run check
cd ..
```

On Windows, replace `python3` with `py -3`. A successful check finishes with no compiler errors. The generated files are in `frontend/generated/`; compiler output goes to `frontend/dist/`. The dependency lockfile makes the check reproducible.

## Current scope

The planner uses rules and a catalog, not a live language model. It handles buttons, tables, and cards, rather than arbitrary UI layouts. User text stays in property data and is not inserted into generated source. The tool does not edit an existing application or provide a visual preview.

## Run the tests (optional)

The demos use Python's standard library. **pytest is needed only for tests.** From the repository folder:

**macOS / Linux:**

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pytest -q
```

**Windows PowerShell:**

```powershell
py -3 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m pytest -q
```

The commands use the environment's Python directly, so you do not need to activate it or change PowerShell's execution policy. GitHub also runs the tests automatically.

## Troubleshooting

- **`python3` or `py` not found**: install Python, reopen your terminal, and check its version.
- **“Can't open file start.py”**: your terminal is in the wrong folder. Open the folder containing this README and `start.py`.
- **A download/install command fails**: downloading the ZIP, cloning, and installing test/compiler dependencies require internet. The Python demo runs offline once downloaded.
- **“Request exactly one supported component”**: try one of the examples above and request one component at a time.
- **No window opened**: this is a terminal generator. Use `save` to export the files, or run the optional compiler check.
- **`npm` not found**: install Node.js 24, then reopen your terminal. Node is optional for the Python demo.
- **Compiler says files are missing**: run `scripts/generate_examples.py` from the repository folder before compiling.

## About this project

A personal implementation inspired by my hands-on project experience at CATS, GITAM University. It uses sample data and does not include the original CATS source code.

[Implementation notes](ENGINEERING.md) · [GitHub portfolio](https://github.com/mkm-007/MKM)
