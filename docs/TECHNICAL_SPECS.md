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
