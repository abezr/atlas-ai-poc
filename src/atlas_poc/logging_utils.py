"""Audit logging for compliance and traceability."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Dict, List


@dataclass
class AuditRecord:
    action: str
    resource: str
    metadata: Dict[str, str]
    timestamp: datetime


class AuditLogger:
    """Collect audit events for AI decisions and actions."""

    def __init__(self) -> None:
        self.records: List[AuditRecord] = []

    def log(self, action: str, resource: str, metadata: Dict[str, str]) -> None:
        self.records.append(
            AuditRecord(
                action=action,
                resource=resource,
                metadata=metadata,
                timestamp=datetime.now(timezone.utc),
            )
        )

    def latest(self) -> AuditRecord | None:
        return self.records[-1] if self.records else None
