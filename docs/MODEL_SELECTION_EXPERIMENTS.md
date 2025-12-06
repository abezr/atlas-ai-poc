# Model Efficiency & Selection Experiments

Concrete KPIs, experiment design, and routing guidance to choose the most efficient LLM stack for the agentic POC.

## 1) KPI Characteristics for Model Efficiency
- **Cost per 1K tokens (prompt/completion)**: Provider list price x measured token counts; track separately for system prompts, tools, and responses.
- **Cost per resolved incident/ticket**: (LLM spend + infra) / (# incidents auto-resolved); report by severity to expose high-risk spend.
- **Quality-per-dollar (Qp$)**: Quality metric (e.g., F1, BLEU, human win-rate) divided by cost per 1K tokens.
- **Latency-adjusted efficiency**: (Quality score) / (latency × cost); favors models that are both faster and cheaper.
- **Throughput per $**: (# successful interactions) / (spend) over a time window; use for capacity planning.
- **Cache effectiveness**: Percentage of calls served via embedding cache/tool cache to reduce spend.
- **Context efficiency**: % of injected tokens that are cited/used; rewards tighter prompts and retrieval pruning.

## 2) Candidate Models (example set)
- GPT-4o (Azure OpenAI) — balanced quality/cost.
- GPT-4 (Azure OpenAI) — high quality baseline.
- GPT-4o-mini / gpt-35-turbo — low-cost fallback and first-pass classifier.
- Qwen/Qwen2.5-family — to be evaluated via [Gonka](https://gonka.ai/) where ingestion is free, enabling high-volume experimentation.

## 3) Offline Evaluation Experiments
- **E1: Threat classification benchmark**
  - Dataset: labeled SOC events (phishing, malware, brute-force, insider risk).
  - Metrics: precision/recall/F1, Qp$, latency p95, cost per labeled event.
  - Goal: find cheapest model that meets ≥0.9 F1 and <3s p95.
- **E2: RAG answer quality**
  - Dataset: KB queries + ground truth answers for infra/cyber playbooks.
  - Metrics: MRR/NDCG, win-rate vs. ground truth, hallucination rate, Qp$, context efficiency.
  - Variants: top-k=5/10/20, rerank on/off, prompt compression on/off.
- **E3: Plan quality for remediation**
  - Dataset: incidents requiring action plans (containment, monitoring, rollback).
  - Metrics: structured evaluation rubric (coverage, safety, actionability), cost per plan, latency.
- **E4: Tool-calling reliability**
  - Dataset: function-call scenarios (ticket creation, isolation request, cost report).
  - Metrics: call success rate, schema validity, retries invoked, cost per successful tool call.

## 4) Online / Shadow Experiments
- **E5: A/B shadow**
  - Route 5-10% traffic to challenger model; compare live latency, cost per ticket, CSAT proxy, and override rate.
- **E6: Canary by scenario**
  - Safety-sensitive flows (privilege, destructive actions) stay on tier-1 model; low-risk Q&A uses cheaper model. Measure incident rate and p95 latency separately.
- **E7: Budget guardrails**
  - Enforce daily/weekly spend caps; when forecast exceeds 90%, automatically downshift to cheaper model except for P0 incidents.

## 5) Multi-Model Router Strategy
- **Routing inputs**: intent, risk level, latency budget, context size, compliance flag, cache hit, and historical Qp$ per scenario.
- **Routing policy**: weighted score = (quality_weight × expected_quality) - (cost_weight × expected_cost) - (latency_weight × expected_latency).
- **Bandit approach**: start with epsilon-greedy; gradually anneal exploration as confidence in model scores grows.
- **Backstop**: force high-risk operations to stay on the most reliable model regardless of score; log overrides for audit.
- **Cold-start**: use offline E1–E4 scores to seed priors before live traffic.

## 6) Experiment Execution Playbook
- **Dataset prep**: create reproducible splits (train/dev/test) stored in blob storage; version with DVC or git-lfs.
- **Runner**: Python 3.14 test harness invoking each model with the same prompts and tool schemas; record tokens, latency, and responses.
- **Metrics store**: push results to Prometheus/Grafana for time-series Qp$ and cost burn; store per-run CSV/Parquet for audits.
- **Hallucination checks**: enforce JSON schema + citation coverage; compute failure rate.
- **Safety filter**: require allowlist for sensitive tools; mark any blocked attempts.

## 7) Decision Framework
- Define acceptance thresholds per use case (e.g., F1 ≥ 0.9, p95 < 3s, Qp$ in top 2 models).
- Rank models per use case by composite score (quality 50%, cost 30%, latency 20%) unless security requires stricter weighting.
- Select **primary** (best composite), **secondary** (cheap fallback), **router** policy, and **canary** for ongoing exploration.
- Re-evaluate weekly or when drift/price changes occur; Qwen evaluations via Gonka can be run frequently to refresh cost/quality curves without spend.
