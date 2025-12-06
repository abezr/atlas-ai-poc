"""Threat classification utilities for the AI POC."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class ThreatSignal:
    """Structured telemetry observed by the agent."""

    source: str
    description: str
    indicators: List[str]


@dataclass
class ThreatAssessment:
    """Structured view of classification results used by the agent."""

    category: str
    scores: Dict[str, float]
    evidence: Dict[str, List[str]]


class ThreatClassifier:
    """Rule-based classifier to simulate incident triage without ML deps."""

    def __init__(self) -> None:
        self.keywords = {
            "phishing": {"login", "credential", "spoof", "link", "email"},
            "malware": {"ransom", "exe", "payload", "trojan", "infect"},
            "intrusion": {"ssh", "privilege", "escalation", "brute", "port"},
            "anomaly": {"latency", "error", "spike", "anomaly", "drift"},
        }

    def classify(self, text: str, signals: List[ThreatSignal] | None = None) -> Dict[str, float]:
        signals = signals or []
        corpus = f"{text} " + " ".join(s.description for s in signals)
        lower = corpus.lower()
        scores: Dict[str, float] = {}

        for label, keys in self.keywords.items():
            matches = sum(1 for key in keys if key in lower)
            scores[label] = round(matches / max(len(keys), 1), 2)

        max_known = max(scores.values() or [0])
        scores["unknown"] = 0.0 if max_known > 0 else 1.0
        return scores

    def explain(self, text: str, signals: List[ThreatSignal] | None = None) -> Dict[str, List[str]]:
        """Return matched keywords per label to inform downstream decisions."""

        signals = signals or []
        corpus = f"{text} " + " ".join(s.description for s in signals)
        lower = corpus.lower()
        evidence: Dict[str, List[str]] = {}

        for label, keys in self.keywords.items():
            evidence[label] = [key for key in keys if key in lower]
        evidence["unknown"] = []
        return evidence

    def assess(self, text: str, signals: List[ThreatSignal] | None = None) -> ThreatAssessment:
        """Produce a structured assessment with category, scores, and evidence."""

        scores = self.classify(text, signals)
        evidence = self.explain(text, signals)
        category = self.prioritize(scores)
        return ThreatAssessment(category=category, scores=scores, evidence=evidence)

    def prioritize(self, scores: Dict[str, float]) -> str:
        """Return the most likely threat category, biased to security events."""

        ordered = sorted(scores.items(), key=lambda kv: kv[1], reverse=True)
        for label, score in ordered:
            if label != "unknown" and score > 0:
                return label
        return ordered[0][0] if ordered else "unknown"


class IncidentPrioritizer:
    """Assess severity from signals and classification scores."""

    def risk_score(self, scores: Dict[str, float], impacted_assets: int, regulated: bool = True) -> float:
        """Calculate a risk score informed by asset blast radius and compliance."""

        base = max(scores.values() or [0])
        modifier = 0.15 if regulated else 0.0
        blast_radius = min(impacted_assets / 8.0, 1.2)
        return round(base + modifier + blast_radius, 3)

    def determine_severity(self, scores: Dict[str, float], impacted_assets: int, regulated: bool = True) -> str:
        score = self.risk_score(scores, impacted_assets, regulated)

        if score >= 1.4:
            return "critical"
        if score >= 0.95:
            return "high"
        if score >= 0.55:
            return "medium"
        return "low"
