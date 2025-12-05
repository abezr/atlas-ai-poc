"""Enterprise integration stubs for the AI POC."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List

from .logging_utils import AuditLogger


@dataclass
class Ticket:
    """A simplified support ticket representation."""

    system: str
    summary: str
    details: str
    severity: str


@dataclass
class KnowledgeBaseEntry:
    """Represents an internal KB article or runbook."""

    title: str
    content: str
    tags: List[str] = field(default_factory=list)


class ConnectWiseClient:
    """Stubbed client for ConnectWise Manage."""

    def __init__(self, audit_logger: AuditLogger) -> None:
        self.audit_logger = audit_logger
        self.created: List[Ticket] = []

    def create_ticket(self, ticket: Ticket) -> str:
        self.created.append(ticket)
        self.audit_logger.log(
            action="create_ticket",
            resource=ticket.summary,
            metadata={"system": ticket.system, "severity": ticket.severity},
        )
        return f"CW-{len(self.created):04d}"


class ConfluenceClient:
    """Stubbed client for Confluence/SPO."""

    def __init__(self, audit_logger: AuditLogger) -> None:
        self.audit_logger = audit_logger
        self.entries: Dict[str, KnowledgeBaseEntry] = {}

    def fetch_runbook(self, tag: str) -> KnowledgeBaseEntry | None:
        for entry in self.entries.values():
            if tag in entry.tags:
                self.audit_logger.log("fetch_runbook", entry.title, {"tag": tag})
                return entry
        return None

    def upsert_entry(self, entry: KnowledgeBaseEntry) -> str:
        self.entries[entry.title] = entry
        self.audit_logger.log("upsert_runbook", entry.title, {"tags": entry.tags})
        return entry.title
