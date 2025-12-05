"""High-level orchestration utilities for the AI POC."""

from __future__ import annotations

from typing import List

from .chatbot import ChatbotAgent
from .data_pipeline import DataPipeline
from .integration import ConnectWiseClient, ConfluenceClient
from .logging_utils import AuditLogger
from .threat_detection import IncidentPrioritizer, ThreatClassifier


def bootstrap_agent(knowledge_docs: List[str]) -> ChatbotAgent:
    """Construct the agent with its dependencies and preload knowledge."""

    audit_logger = AuditLogger()
    data_pipeline = DataPipeline()
    classifier = ThreatClassifier()
    prioritizer = IncidentPrioritizer()
    connectwise = ConnectWiseClient(audit_logger)
    confluence = ConfluenceClient(audit_logger)

    agent = ChatbotAgent(
        data_pipeline=data_pipeline,
        classifier=classifier,
        prioritizer=prioritizer,
        audit_logger=audit_logger,
        connectwise=connectwise,
        confluence=confluence,
    )
    agent.load_knowledge(knowledge_docs)
    return agent
