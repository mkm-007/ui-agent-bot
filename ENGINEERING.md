# Implementation notes

The catalog keeps component selection and source generation separate. Properties returned by the parser are data, so a label containing quotes or code-like text cannot become executable TypeScript. Each result receives a copy of the catalog entry to avoid mutations leaking into later requests.

The generated components use typed inputs and fixed templates. Python tests cover properties, ambiguity, unsupported requests, source injection, and catalog isolation. The Angular compiler checks TypeScript and templates; browser rendering and host-application integration are separate concerns.
