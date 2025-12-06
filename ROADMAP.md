Request
{
  "owner": "abezr",
  "repo": "atlas-agentic-ai-poc",
  "branch": "main",
  "message": "docs: Add project roadmap, technical requirements and evaluation framework",
  "files": [
    {
      "path": "ROADMAP.md",
      "content": <<'CONTENT'
# Atlas Agentic AI POC - Implementation Roadmap

## Overview
Phased implementation plan for autonomous AI agents managing IT infrastructure and cybersecurity for investment firms.

## Phase 1: Foundation (Week 1-2)

### 1.1 Infrastructure Setup
- [ ] Task 1.1.1: Set up Azure free-tier resources (App Services, Cosmos DB, Bot Service)
- [ ] Task 1.1.2: Configure Azure OpenAI service with GPT-4 and text-embedding-ada-002
- [ ] Task 1.1.3: Set up CI/CD pipeline with GitHub Actions
- [ ] Task 1.1.4: Configure Application Insights for observability

### 1.2 Core Architecture
- [ ] Task 1.2.1: Implement MCP server with Model Context Protocol
- [ ] Task 1.2.2: Build Agent Orchestrator with spawn → observe → act → reconcile lifecycle
- [ ] Task 1.2.3: Create base Agent abstract class with memory management
- [ ] Task 1.2.4: Implement event routing system with isolation scopes

### 1.3 Data Pipeline
- [ ] Task 1.3.1: Set up Cosmos DB with vector search capabilities
- [ ] Task 1.3.2: Build embedding pipeline for knowledge base ingestion
- [ ] Task 1.3.3: Create vector store indexing service
- [ ] Task 1.3.4: Implement state management for agent memory

## Phase 2: RAG & LLM Integration (Week 3-4)

### 2.1 Retrieval-Augmented Generation
- [ ] Task 2.1.1: Implement hybrid search (keyword + vector + reranking)
- [ ] Task 2.1.2: Build retrieval pipeline with Azure Cognitive Search
- [ ] Task 2.1.3: Create prompt template system with few-shot examples
- [ ] Task 2.1.4: Implement context window management (token limits)

### 2.2 LLM Orchestration
- [ ] Task 2.2.1: Create OpenAI client wrapper with retry logic
- [ ] Task 2.2.2: Implement streaming responses for chatbot
- [ ] Task 2.2.3: Build function calling interface for agent actions
- [ ] Task 2.2.4: Create LLM response validation and parsing

### 2.3 Knowledge Base
- [ ] Task 2.3.1: Ingest sample IT troubleshooting guides
- [ ] Task 2.3.2: Add cybersecurity incident response playbooks
- [ ] Task 2.3.3: Include Azure infrastructure best practices
- [ ] Task 2.3.4: Load compliance and regulatory documentation

## Phase 3: Agent Implementation (Week 5-7)

### 3.1 Security Agent
- [ ] Task 3.1.1: Build threat event observer (webhook consumer)
- [ ] Task 3.1.2: Implement ML-based threat classifier
- [ ] Task 3.1.3: Create severity scoring model
- [ ] Task 3.1.4: Build automated response executor
- [ ] Task 3.1.5: Implement fallback patterns (circuit breaker, timeout)
- [ ] Task 3.1.6: Add human-in-the-loop escalation for high-risk actions

### 3.2 Infrastructure Agent
- [ ] Task 3.2.1: Implement Azure resource monitoring
- [ ] Task 3.2.2: Build auto-scaling policy engine
- [ ] Task 3.2.3: Create cost optimization analyzer
- [ ] Task 3.2.4: Implement resource provisioning executor
- [ ] Task 3.2.5: Add compliance validation for infrastructure changes

### 3.3 Service Desk Agent
- [ ] Task 3.3.1: Build conversational interface with Azure Bot Framework
- [ ] Task 3.3.2: Implement intent classification and entity extraction
- [ ] Task 3.3.3: Create ticket management integration (simulated ConnectWise)
- [ ] Task 3.3.4: Build knowledge retrieval for user queries
- [ ] Task 3.3.5: Implement multi-turn dialogue management

## Phase 4: Multi-Agent Orchestration (Week 8-9)

### 4.1 Agent Coordination
- [ ] Task 4.1.1: Implement trigger chains for cross-agent workflows
- [ ] Task 4.1.2: Build shared state management between agents
- [ ] Task 4.1.3: Create conflict resolution mechanism
- [ ] Task 4.1.4: Implement agent mesh communication

### 4.2 Advanced Patterns
- [ ] Task 4.2.1: Build policy enforcement layer
- [ ] Task 4.2.2: Implement anomaly detection for agent behavior
- [ ] Task 4.2.3: Create agent self-evaluation with feedback loop
- [ ] Task 4.2.4: Add retry logic with exponential backoff

## Phase 5: Production Readiness (Week 10-12)

### 5.1 Evaluation Pipeline
- [ ] Task 5.1.1: Build ground truth dataset for accuracy scoring
- [ ] Task 5.1.2: Implement drift detection comparing predictions vs. reality
- [ ] Task 5.1.3: Create response validation framework (schema, latency, confidence)
- [ ] Task 5.1.4: Build automated retraining trigger system
- [ ] Task 5.1.5: Implement A/B testing for prompt variations

### 5.2 Observability
- [ ] Task 5.2.1: Set up Prometheus + Loki for agentic flows monitoring
- [ ] Task 5.2.2: Create dashboards for agent performance metrics
- [ ] Task 5.2.3: Implement distributed tracing for multi-agent workflows
- [ ] Task 5.2.4: Build alerting system for agent failures

### 5.3 Security & Compliance
- [ ] Task 5.3.1: Implement RBAC for agent actions
- [ ] Task 5.3.2: Add data encryption at rest and in transit
- [ ] Task 5.3.3: Create audit logging for all agent decisions
- [ ] Task 5.3.4: Build GDPR compliance controls for data handling
- [ ] Task 5.3.5: Implement secret management with Azure Key Vault

### 5.4 Integration & Testing
- [ ] Task 5.4.1: Build integration tests for agent workflows
- [ ] Task 5.4.2: Create load testing suite for chatbot performance
- [ ] Task 5.4.3: Implement chaos engineering for fault tolerance validation
- [ ] Task 5.4.4: Build deployment automation scripts

### 5.5 Documentation & Demo
- [ ] Task 5.5.1: Create user guide for interacting with chatbot
- [ ] Task 5.5.2: Write technical documentation for agent architecture
- [ ] Task 5.5.3: Build demo scenarios showcasing autonomous capabilities
- [ ] Task 5.5.4: Create video walkthrough of key features

## Success Metrics

### Technical KPIs
- Agent response latency < 3 seconds (p95)
- Threat classification accuracy > 90%
- RAG retrieval precision > 85%
- Infrastructure action success rate > 95%
- System uptime > 99.5%

### Business KPIs
- Mean time to detect (MTTD) threats < 5 minutes
- Mean time to respond (MTTR) incidents < 15 minutes
- Ticket auto-resolution rate > 40%
- Infrastructure cost optimization > 20%
- User satisfaction score > 4/5

## Risk Management

### Technical Risks
- **LLM hallucination**: Mitigated by response validation and confidence thresholds
- **Agent loop failures**: Handled by circuit breakers and timeout controls
- **Data quality issues**: Addressed by evaluation pipeline and drift detection

### Business Risks
- **Regulatory compliance**: All actions logged with audit trail
- **Security vulnerabilities**: Defense-in-depth with RBAC and encryption
- **Cost overruns**: Budget monitoring and alerts on Azure consumption
CONTENT
    },
    {
      "path": "docs/TECHNICAL_SPECS.md",
      "content": <<'TECH'
# Technical Specifications

## Technology Stack

### Backend Services
- **Language**: C# (.NET 8) and Python 3.14+
- **Framework**: ASP.NET Core WebAPI
- **Agent Runtime**: Custom orchestrator with MCP protocol
- **Message Queue**: Azure Service Bus (for agent communication)

### Frontend
- **Framework**: React 18 with TypeScript
- **UI Library**: Material-UI
- **State Management**: Redux Toolkit
- **Real-time**: SignalR for WebSocket connections

### AI/ML
- **LLM**: Azure OpenAI (GPT-4, GPT-4-turbo)
- **Embeddings**: text-embedding-ada-002
- **ML Framework**: Azure Machine Learning
- **Model Training**: Python with scikit-learn, PyTorch

### Data Storage
- **Vector Database**: Azure Cosmos DB for MongoDB (vCore)
- **State Store**: Azure Cosmos DB (NoSQL API)
- **Cache**: Azure Redis Cache
- **Blob Storage**: Azure Storage Account

### Observability
- **Metrics**: Azure Monitor + Application Insights
- **Logs**: Azure Log Analytics
- **Tracing**: OpenTelemetry with Jaeger
- **Dashboards**: Grafana with Prometheus (alternative)

### Security
- **Authentication**: Azure AD + OAuth 2.0
- **Secrets**: Azure Key Vault
- **Encryption**: TLS 1.3, AES-256 at rest
- **Compliance**: GDPR, SOC 2 Type II controls

### DevOps
- **CI/CD**: GitHub Actions
- **Infrastructure**: Azure Resource Manager (ARM) templates
- **Containers**: Docker + Azure Container Apps
- **Monitoring**: Azure DevOps + Application Insights

## Architecture Patterns

### Agent Lifecycle (MCP)

```
Spawn → Observe → Act → Reconcile

1. Spawn: Initialize agent with config, memory, and tools
2. Observe: Monitor events from external systems
3. Act: Execute decisions based on LLM reasoning
4. Reconcile: Validate outcomes, update memory, trigger retries
```

### Multi-Agent Patterns

#### Trigger Chains
```
SecurityAgent detects threat → InfraAgent isolates VM → ServiceAgent notifies users
```

#### Shared State
```
Incident context stored in Cosmos DB, accessible by all agents
```

#### Conflict Resolution
```
Priority-based: Security > Infrastructure > Service Desk
Voting mechanism for non-critical decisions
```

### RAG Pipeline

```
Query → Embedding → Vector Search → Reranking → Context Injection → LLM → Response

1. Embedding: Convert query to 1536-dim vector
2. Vector Search: Cosine similarity top-k retrieval (k=20)
3. Reranking: Cross-encoder model for relevance scoring
4. Context Injection: Top-5 documents injected into prompt
5. LLM: GPT-4 with temperature=0.3 for deterministic output
```

### Fault Tolerance

#### Circuit Breaker
```csharp
if (failureCount > threshold) {
    state = CircuitState.Open;
    return fallbackResponse;
}
```

#### Timeout Control
```csharp
await Task.WhenAny(
    agentAction,
    Task.Delay(timeoutMs)
);
```

#### Retry with Exponential Backoff
```csharp
for (int i = 0; i < maxRetries; i++) {
    try {
        return await ExecuteAction();
    } catch (TransientException) {
        await Task.Delay(Math.Pow(2, i) * baseDelay);
    }
}
```

## Data Models

### Agent State
```json
{
  "agentId": "sec-agent-001",
  "type": "SecurityAgent",
  "status": "active",
  "memory": {
    "conversationHistory": [...],
    "incidentContext": {...},
    "learnedPatterns": [...]
  },
  "metrics": {
    "actionsExecuted": 42,
    "successRate": 0.95,
    "avgLatency": 2.3
  }
}
```

### Threat Event
```json
{
  "eventId": "evt-2024-001",
  "timestamp": "2024-12-05T20:00:00Z",
  "source": "Azure Security Center",
  "type": "suspicious-login",
  "severity": "high",
  "details": {
    "user": "admin@client.com",
    "ipAddress": "203.0.113.42",
    "location": "Unknown"
  },
  "classification": "brute-force-attempt",
  "confidenceScore": 0.87
}
```

### RAG Document
```json
{
  "docId": "kb-azure-001",
  "title": "Azure VM Auto-Scaling Best Practices",
  "content": "...",
  "embedding": [0.123, -0.456, ...],
  "metadata": {
    "source": "confluence",
    "category": "infrastructure",
    "lastUpdated": "2024-11-01"
  }
}
```

## API Specifications

### MCP Agent API

#### Spawn Agent
```http
POST /api/agents/spawn
Content-Type: application/json

{
  "type": "SecurityAgent",
  "config": {
    "observeSources": ["siem", "azure-security"],
    "autoRemediate": true
  }
}
```

#### Send Event to Agent
```http
POST /api/agents/{agentId}/events
Content-Type: application/json

{
  "eventType": "security.threat.detected",
  "payload": {...}
}
```

### Chatbot API

#### Send Message
```http
POST /api/bot/messages
Content-Type: application/json

{
  "conversationId": "conv-123",
  "text": "What is the status of incident INC-2024-001?",
  "userId": "user-456"
}
```

#### Response
```json
{
  "messageId": "msg-789",
  "text": "Incident INC-2024-001 has been automatically resolved...",
  "suggestions": [
    "View incident details",
    "Create follow-up ticket"
  ],
  "citations": [
    {"title": "Incident Response Playbook", "url": "..."}
  ]
}
```

## Performance Requirements

### Latency Targets
- Chatbot response: < 3s (p95)
- Agent action execution: < 5s (p95)
- RAG retrieval: < 500ms (p95)
- Vector search: < 100ms (p95)

### Throughput
- Chatbot messages: 100 req/s
- Agent events: 1000 events/s
- Concurrent agents: 50+

### Scalability
- Horizontal scaling for agent workers
- Auto-scaling based on queue depth
- Multi-region deployment for HA

## Security Controls

### Authentication & Authorization
- OAuth 2.0 with Azure AD
- Role-based access control (RBAC)
- Service principal for agent-to-service auth

### Data Protection
- TLS 1.3 for all network traffic
- AES-256 encryption at rest
- PII masking in logs

### Audit & Compliance
- All agent actions logged with timestamp, user, and outcome
- Immutable audit trail in Azure Log Analytics
- GDPR right-to-erasure implementation

### Threat Model
- Prompt injection mitigation: Input validation, output filtering
- Data exfiltration prevention: Network policies, DLP
- Privilege escalation: Least privilege principle, MFA
TECH
    },
    {
      "path": "docs/EVALUATION_FRAMEWORK.md",
      "content": <<'EVAL'
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

## 5. Observability (Prometheus + Loki)

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

## 6. Production Scenarios

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

## 7. Evaluation Dashboard

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
│ threat_classifier: pending              │
│ severity_scorer: scheduled 12/06        │
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
EVAL
    }
  ]
}
