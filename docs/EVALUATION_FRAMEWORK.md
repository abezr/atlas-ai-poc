# AI/ML Evaluation Framework

Based on Agentic AI patterns from the provided image (Module 3, Sections 13.10, 15.10, 16.10)

## Overview
Comprehensive evaluation strategy for Agentic AI systems covering accuracy, observability, and production resilience.

## 1. Accuracy Scoring (Ground Truth vs Prediction)

### Threat Classification Evaluation

#### Metrics
- **Precision**: TP / (TP + FP) - Avoid false alarms
- **Recall**: TP / (TP + FN) - Catch all real threats
- **F1 Score**: Harmonic mean of precision and recall
- **Confusion Matrix**: Multi-class threat categorization

#### Ground Truth Collection
```python
# Label threats after human review
ground_truth = {
    "event_id": "evt-001",
    "predicted_class": "malware",
    "actual_class": "malware",
    "correct": True,
    "confidence": 0.87
}
```

#### Evaluation Pipeline
```python
for prediction in predictions:
    actual = ground_truth_db.get(prediction.event_id)
    score = calculate_accuracy(prediction, actual)
    metrics_store.record(score)
    
    if score < threshold:
        trigger_retraining()
```

### RAG Retrieval Quality

#### Metrics
- **MRR (Mean Reciprocal Rank)**: Position of first relevant document
- **NDCG (Normalized Discounted Cumulative Gain)**: Ranking quality
- **Precision@k**: Relevance of top-k results

#### LLM-as-a-Judge Pattern
```python
judge_prompt = f"""
Query: {query}
Retrieved Documents: {docs}

Rate relevance of each document (0-10 scale).
Consider: semantic similarity, factual accuracy, completeness.

Output JSON: {{"doc_1": 8, "doc_2": 3, ...}}
"""

scores = openai.chat(judge_prompt, model="gpt-4")
```

## 2. Drift Detection (Model vs Real Data)

### Concept Drift Monitoring

#### Statistical Tests
- **Kolmogorov-Smirnov Test**: Distribution shift detection
- **Population Stability Index (PSI)**: Feature drift measurement

#### Implementation
```python
def detect_drift(reference_data, current_data):
    psi = calculate_psi(reference_data, current_data)
    
    if psi > 0.2:  # Significant drift
        alert("Model drift detected")
        trigger_retraining()
    elif psi > 0.1:  # Minor drift
        schedule_evaluation()
```

### Prediction-Reality Gap

#### Automated Resolution Verification
```python
# Agent predicts: "Block IP 203.0.113.42 will stop attack"
action_result = execute_action("block_ip", "203.0.113.42")

# Wait 5 minutes, verify outcome
actual_result = verify_threat_stopped()

if actual_result != predicted_result:
    log_misprediction()
    update_model_feedback()
```

## 3. Response Validation

### Schema Validation

#### JSON Schema Enforcement
```python
response_schema = {
    "type": "object",
    "properties": {
        "action": {"type": "string", "enum": ["block", "alert", "investigate"]},
        "confidence": {"type": "number", "minimum": 0, "maximum": 1},
        "reasoning": {"type": "string", "minLength": 10}
    },
    "required": ["action", "confidence", "reasoning"]
}

if not validate(response, response_schema):
    raise ValidationError("Invalid agent response")
```

### Latency Monitoring

#### SLA Enforcement
```python
max_latency = 3000  # 3 seconds

start_time = time.now()
response = agent.execute(event)
latency = time.now() - start_time

if latency > max_latency:
    alert("Agent SLA violation")
    metrics.record("latency_breach", latency)
```

### Confidence Threshold

#### Risk-Based Gating
```python
if response.confidence < 0.7:
    # Low confidence - escalate to human
    escalate_to_human(response)
elif response.confidence < 0.9 and response.risk == "high":
    # Medium confidence + high risk - require approval
    request_approval(response)
else:
    # High confidence - auto-execute
    execute(response)
```

## 4. Feedback Loop (Agent Self-Evaluation)

### Self-Critique Pattern

#### Agent Reviews Its Own Output
```python
critique_prompt = f"""
You previously classified this event as: {classification}
Your reasoning was: {reasoning}

The actual outcome was: {actual_outcome}

Evaluate your performance:
1. Was your classification correct?
2. What did you miss?
3. How should you improve next time?
"""

self_evaluation = openai.chat(critique_prompt)
store_learning(self_evaluation)
```

### Retraining Triggers

#### Automated Model Updates
```python
if accuracy < 0.85 or drift_detected or error_rate > 0.05:
    # Collect recent labeled examples
    training_data = collect_feedback_data(days=30)
    
    # Fine-tune model
    new_model = fine_tune(
        base_model="gpt-4",
        training_data=training_data,
        hyperparameters={"epochs": 3, "batch_size": 4}
    )
    
    # A/B test new model
    deploy_canary(new_model, traffic_percentage=10)
```

## 5. Cost & Efficiency KPIs

### Spend-Aware Metrics
- **Cost per 1K tokens (prompt/completion)**: Map provider pricing to measured tokens to track burn per call family.
- **Cost per resolved incident/ticket**: (Total LLM + infra cost) / (# incidents auto-resolved). Separately track escalations vs. auto-remediations.
- **Cost per action plan**: Useful for remediation runbooks where only planning is done by LLM and execution is automated.
- **Cache hit ratio**: Percentage of responses served from vector cache/tool cache to avoid regeneration spend.

### Throughput vs. Budget
- **Requests per $**: Successful responses / total LLM spend over a window.
- **Throughput per token**: (# interactions) / (# tokens). Highlights prompt engineering wins (shorter prompts, distilled context).
- **Budget adherence**: % of days/months under budget cap; alert when forecast > 90% of cap.

### Latency & Resource Efficiency
- **p95 latency vs. SLA**: Track adherence to sub-3s target; correlate with cost to avoid over-provisioning.
- **CPU/GPU seconds per request**: Normalize infrastructure burn (Azure Container Apps/AKS) to attribute non-LLM costs.
- **Energy/compute efficiency**: Optional metric for sustainability reporting (kWh per 1K tokens if telemetry available).

### Accuracy/Cost Trade-off
- **Quality-per-dollar (Qp$)**: (Quality score such as F1 or win-rate) / (cost per 1K tokens). Enables ranking models on balanced efficiency.
- **Latency-aware routing score**: Weighted score combining accuracy, latency, and cost to drive dynamic router decisions.

### Token Hygiene
- **Prompt inflation**: Average prompt token length over time; flag regressions from new templates.
- **Context packing efficiency**: % of context tokens that were actually cited/used (from response citations vs. injected tokens).

## 6. Observability (Prometheus + Loki)

### Metrics to Track

#### Agent Performance
```prometheus
# Agent action success rate
agent_action_success_rate{agent="security", action="block_ip"}

# Agent response latency
agent_response_latency_seconds{agent="security", percentile="p95"}

# Agent memory usage
agent_memory_bytes{agent="security"}
```

#### ML Model Metrics
```prometheus
# Model accuracy over time
model_accuracy{model="threat_classifier", window="24h"}

# Prediction confidence distribution
model_confidence_distribution{model="threat_classifier", bucket="0.8-0.9"}

# Drift score
model_drift_psi{model="threat_classifier"}
```

### Logging with Loki

#### Structured Logs
```python
logger.info(
    "Agent action executed",
    extra={
        "agent_id": "sec-001",
        "action": "block_ip",
        "event_id": "evt-123",
        "confidence": 0.92,
        "latency_ms": 1234,
        "outcome": "success"
    }
)
```

### Distributed Tracing

#### OpenTelemetry Integration
```python
with tracer.start_as_current_span("security_agent_workflow") as span:
    span.set_attribute("event.id", event_id)
    
    # Observe
    with tracer.start_span("observe"):
        event = observe_threat()
    
    # Act
    with tracer.start_span("act"):
        action = plan_response(event)
    
    # Reconcile
    with tracer.start_span("reconcile"):
        verify_outcome(action)
```

## 7. Production Scenarios

### Auto-Scaling Use Case

#### Evaluation Criteria
- **Accuracy**: Did agent scale at right time?
- **Efficiency**: Was resource utilization optimized?
- **Cost**: Did action reduce spend?

#### Measurement
```python
# Ground truth: actual load spike
actual_spike_time = "2024-12-05T10:00:00Z"
predicted_spike_time = agent.prediction

# Accuracy: within 5-minute window
accurate = abs(actual_spike_time - predicted_spike_time) < 5min

# Efficiency: CPU stayed below 80%
efficient = max(cpu_usage) < 0.80

# Cost: saved vs. manual provisioning
cost_saved = baseline_cost - actual_cost
```

### Anomaly Detection Evaluation

#### False Positive Rate
```python
# Human labels after 24h review
for alert in alerts:
    human_label = await get_human_feedback(alert)
    
    if human_label == "benign" and alert.predicted == "anomaly":
        false_positives += 1

fpr = false_positives / total_alerts

if fpr > 0.05:  # > 5% FPR
    tune_threshold(direction="stricter")
```

### Policy Enforcement

#### Compliance Validation
```python
# Agent proposed: delete sensitive data
action = agent.propose_action()

# Validate against compliance rules
if not compliant_with_gdpr(action):
    block_action()
    alert_compliance_team()
    retrain_agent_on_policy()
```

## 8. Evaluation Dashboard

### Key Metrics Display

```
┌─────────────────────────────────────────┐
│ Agentic AI Evaluation Dashboard         │
├─────────────────────────────────────────┤
│ Accuracy (24h)                          │
│ ████████████████░░░░ 82%                │
│                                         │
│ Drift Score (PSI)                       │
│ ██░░░░░░░░░░░░░░░░░░ 0.08 (OK)        │
│                                         │
│ Latency P95                             │
│ ████████████████████ 2.1s              │
│                                         │
│ False Positive Rate                     │
│ ███░░░░░░░░░░░░░░░░░ 3.2%             │
│                                         │
│ Retraining Queue                        │
│ threat_classifier: pending              |
│ severity_scorer: scheduled 12/06        |
└─────────────────────────────────────────┘
```

## Implementation Checklist

- [ ] Set up metrics collection with Prometheus
- [ ] Configure Loki for structured logging
- [ ] Build ground truth labeling UI
- [ ] Implement drift detection pipeline
- [ ] Create response validation middleware
- [ ] Deploy feedback loop automation
- [ ] Set up Grafana dashboards
- [ ] Configure alerting rules
- [ ] Build A/B testing framework
- [ ] Document evaluation procedures
