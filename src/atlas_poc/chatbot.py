"""Agentic chatbot core simulating Azure Bot + OpenAI orchestration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Tuple

from .data_pipeline import DataPipeline, EmbeddedDocument
from .integration import ConnectWiseClient, ConfluenceClient, KnowledgeBaseEntry, Ticket
from .logging_utils import AuditLogger
from .threat_detection import IncidentPrioritizer, ThreatClassifier, ThreatSignal


@dataclass
class ConversationTurn:
    user: str
    agent: str


@dataclass
class ChatbotAgent:
    data_pipeline: DataPipeline
    classifier: ThreatClassifier
    prioritizer: IncidentPrioritizer
    audit_logger: AuditLogger
    connectwise: ConnectWiseClient
    confluence: ConfluenceClient
    memory: List[ConversationTurn] = field(default_factory=list)
    knowledge_index: List[EmbeddedDocument] = field(default_factory=list)

    def load_knowledge(self, documents: List[str]) -> None:
        self.knowledge_index = self.data_pipeline.build_index(documents)
        for doc in documents:
            self.audit_logger.log("ingest_doc", doc[:48], {"length": str(len(doc))})

    def _retrieve_context(self, query: str) -> List[str]:
        results = self.data_pipeline.search(query, self.knowledge_index)
        return [doc.text for doc in results]

    def _plan_response(self, user_input: str, context: List[str]) -> Tuple[str, str, str]:
        signals = [ThreatSignal(source="context", description=ctx, indicators=[]) for ctx in context]
        assessment = self.classifier.assess(user_input, signals)
        severity = self.prioritizer.determine_severity(assessment.scores, impacted_assets=len(context) or 1)

        if assessment.category in {"phishing", "malware", "intrusion"}:
            actions = [
                "isolate affected hosts or accounts",
                "rotate credentials and invalidate active sessions",
                "open incident ticket with mapped observables",
            ]
        else:
            actions = [
                "continue monitoring anomalies",
                "capture additional telemetry from logs",
                "prepare runbook update if issue persists",
            ]

        context_hint = context[0][:80] if context else "no context available"
        plan = (
            f"Detected {assessment.category} scenario at {severity} severity based on {len(assessment.evidence.get(assessment.category, []))} indicators. "
            f"Key evidence: {', '.join(assessment.evidence.get(assessment.category, []) or ['none'])}. "
            f"Closest context: {context_hint}. Recommended actions: {', '.join(actions)}"
        )

        return severity, plan, assessment.category

    def _create_ticket(self, summary: str, details: str, severity: str) -> str:
        ticket = Ticket(system="ConnectWise", summary=summary, details=details, severity=severity)
        return self.connectwise.create_ticket(ticket)

    def respond(self, user_input: str) -> str:
        context = self._retrieve_context(user_input)
        severity, plan, category = self._plan_response(user_input, context)
        ticket_id = self._create_ticket(summary=user_input[:60], details="\n".join(context), severity=severity)

        kb_entry = KnowledgeBaseEntry(title=f"Response for {ticket_id}", content=plan, tags=[severity])
        self.confluence.upsert_entry(kb_entry)

        response = f"{plan} Created ticket {ticket_id} and updated runbook '{kb_entry.title}'."
        self.memory.append(ConversationTurn(user=user_input, agent=response))
        self.audit_logger.log("respond", ticket_id, {"severity": severity, "category": category})
        return response
