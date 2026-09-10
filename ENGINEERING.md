# Engineering notes

## Design boundary

Request → catalog selection → validated specification → fixed Angular template + JSON properties

This is a deterministic catalog workflow, not an autonomous LLM agent. It emits components; it does not insert them into an existing app, supply a live preview, or automatically bind returned properties. Integrators must bind props as Angular inputs. Arbitrary component requests and complex language are unsupported. Compiler checks do not establish browser usability or full accessibility compliance.

## Review walkthrough

1. Run `python run_demo.py` and locate the code producing every output field.
2. Run `python -m pytest -q`; change a fixture and explain why its assertion changes.
3. Explain one refusal case and one case the current implementation cannot handle.
4. Trace an input from parsing to the final result, including validation and source/data boundaries.

## Future work (not implemented)

A model-backed extension should have a typed input/output contract, mocked provider tests, explicit opt-in credentials, timeouts, and a measured evaluation set. Treat model output as untrusted. Never send private CATS material to a model. Add infrastructure only when its behavior can be tested and demonstrated; adding a library name alone is not an upgrade.
