⚠️ This repository contains experimental, opinionated runtime interpretations.
It does not represent WAIL v1 behavior, guarantees, or scope.


# WAIL Runtime Demo

This repository contains a runnable demo of WAIL, a post-inference runtime layer for AI systems.

WAIL operates after model inference, observing and structuring execution-level signals without modifying the model or application logic.

This demo is intentionally minimal and designed to demonstrate:
- runtime execution tracing
- token-level observation
- experimental runtime deviation heuristics (demo-only)
- reproducible execution artifacts

---

## What This Demo Shows

When you run the demo and submit a prompt:
- a runtime execution is started
- tokens are observed sequentially
- execution timing is tracked in real time
- runtime deviations are flagged using experimental heuristics
- a structured execution trace is generated as a JSON artifact

The model output itself is not evaluated or judged.  
WAIL observes how the model executes, not what it says.

---

### Important Scope Note

Any flags, labels, or UI messages shown in this demo are:
- experimental
- heuristic
- derived for demonstration purposes only
- not part of WAIL v1

WAIL v1 produces runtime evidence, not judgments.

---

## Requirements

- Docker
- Docker Compose

---

## Run the Demo

Start the demo:

```bash
docker compose up
```

---

Open the web UI in your browser:

http://localhost:8501


---

## Using the Demo
- Enter any prompt in the UI
- Click Run
- Observe the runtime execution
- Download the generated execution trace JSON

Each run produces a deterministic, structured trace file under the traces/ directory

---

## Output
Each execution generates a JSON file containing:

- execution ID
- timestamps
- token observation events
- exploratory runtime flags (non-V1)
- execution summary

These artifacts are machine-readable, auditable, and comparable across runs.

---

## How to Stop

Stop the demo:

```bash
Ctrl + C
```

Clean up containers:

docker compose down

--- 

## Scope and Intent
This demo does not represent a full product UI.

It exists to demonstrate WAIL as a model-agnostic runtime infrastructure layer that can be embedded behind any AI system in production.

---

## Evaluation Disclaimer
This repository is provided solely for evaluation and demonstration purposes.

The code and artifacts are not intended for production use and may not reflect final architecture, performance, or security characteristics.

---

## No Production Use
This demo is provided as-is for technical evaluation only.

No warranties or guarantees are implied.
Use in production environments is explicitly not permitted.

---

## Notes

- the demo runs entirely locally
- no external services are contacted
- no telemetry or data collection is performed
- all execution artifacts remain on the user's machine