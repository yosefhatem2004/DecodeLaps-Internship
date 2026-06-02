# YHM Logic Engine v2.5 — Production CLI

A production-grade, rule-based AI chatbot built using a deterministic "white-box" architecture. This system focuses on absolute predictability, zero-hallucination risk, and programmatic decision-making by matching user intent against structured knowledge patterns before transitioning into advanced vector mappings or deep learning models.

## Architecture & Data Flow

The system operates strictly on a deterministic **Input-Process-Output (IPO)** model, ensuring that every user interaction passes through an audit-friendly control layer:
```text
[ Raw User Input ] 
       │
       ▼ (Phase 1: Input Processing & Sanitization)
┌─────────────────────────────────┐
│ Lowercase, Trimmed Clean String │
└─────────────────────────────────┘
       │
       ▼ (Phase 2: Intent Evaluation Engine)
┌─────────────────────────────────┐
│    Exact Match Verification     │ ──► Found? ──► [ Output Response ]
└─────────────────────────────────┘
       │
       ▼ Not Found?
┌─────────────────────────────────┐
│     Partial Keyword Scan        │ ──► Found? ──► [ Output Response ]
└─────────────────────────────────┘
       │
       ▼ Not Found?
[ Fallback Help Dashboard Guidance ]
```
### Key Components

1. **Configuration & Data Layer:** Maintains an isolated dictionary of tuple-structured keywords mapped to direct, compliant responses.
2. **Sanitization Phase:** Enforces strict formatting (case-normalization and whitespace stripping) to keep string comparison robust.
3. **Intent Evaluation Engine:** Implements a two-tiered check (exact matching followed by partial fallback scans) to gracefully resolve human queries.
4. **Continuous Control Loop Loop:** Handles execution heartbeat safely, intercepting exit strategies (`exit`, `quit`, `terminate`, `kill`) or sudden keyboard interrupts without throwing unhandled exceptions.

## Features

- **100% Deterministic:** Eradicates standard LLM hallucination risks by relying entirely on deterministic logic workflows.
- **Fail-Safe Design:** Intercepts sudden system interruptions gracefully to prevent application loop crashes.
- **Dynamic Help System:** Provides a real-time dashboard of topics whenever a user types an invalid command or explicitly requests help.

## Getting Started

### Prerequisites

You only need standard Python installed on your local environment (Python 3.8+ recommended). This project utilizes zero third-party dependencies for maximum portability and compatibility.

### Running the Application

1. Clone this repository to your local computer:
   ```bash
   git clone [https://github.com/yourusername/yhm-logic-engine.git](https://github.com/yourusername/yhm-logic-engine.git)

Navigate into the project folder:
```bash
cd yhm-logic-engine

Run the CLI script directly using Python:
```bash
python main.py

Keyword Topic	Description
hello / hi	Say hello to trigger the welcome handler.
ai / intelligence	Read about the rule-based AI philosophy.
chatbot / bot	Review the rule-based chatbot control logic.
automation	Explore workflow automation and data compliance.
logic / whitebox	View the structural data flow framework map.
status / health	Monitor the system execution metrics.
help / ?	Display the interactive user help menu.
exit / quit	Safely close down the running control loop.

Development Context
This project serves as a cornerstone milestone for mastering core programmatic decision-making.
Building rule-based logic layers provides a necessary baseline architecture for auditing, data validation,
and safety controls before advancing to non-deterministic models like text vector spaces, TF-IDF statistical scoring, and neural collaborative filtering.
