# Atlas AI POC

A lightweight proof-of-concept for Azure-first, agentic AI/ML pipelines tailored to financial investment firms. The system demonstrates autonomous infrastructure management and cybersecurity automation with attention to compliance and auditability.

## Goals
- Model Atlas Technica's vision using Azure Bot Framework, Azure OpenAI, and Cognitive Services concepts.
- Show retrieval-augmented, multi-turn chatbot behaviour with threat classification and remediation planning.
- Provide data pipelines, integration stubs, and logging practices suitable for regulated environments.

## Contents
- `docs/ARCHITECTURE.md` – C4 context/container/component diagrams for the POC.
- `src/atlas_poc/` – Data pipelines, classifier, agent, and integration stubs with explainable risk scoring.
- `tests/` – Unit tests for ingestion, classification, and agent orchestration.
- `ROADMAP.md` – Completed task list for the POC scope.

- `docs/EVALUATION_FRAMEWORK.md` – Accuracy, drift, validation, and observability guidance.
- `docs/MODEL_SELECTION_EXPERIMENTS.md` – Efficiency KPIs, experiments, and router strategy for choosing models.

## Quickstart
1. **Install Python 3.14 (latest stable)**

2. **Run tests**
   ```bash
   python -m unittest discover -s tests -p 'test_*.py'
   ```

## Notes
- External calls are mocked/stubbed to keep the POC runnable without Azure credentials.
- Replace stubs in `integration.py` with production-grade clients (Azure SDK, REST adapters) when targeting a real environment.
