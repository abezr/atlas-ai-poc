import sys
import pathlib
import unittest

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT / "src"))

from atlas_poc.chatbot import ChatbotAgent
from atlas_poc.data_pipeline import DataPipeline
from atlas_poc.integration import ConnectWiseClient, ConfluenceClient
from atlas_poc.logging_utils import AuditLogger
from atlas_poc.pipeline import bootstrap_agent
from atlas_poc.threat_detection import IncidentPrioritizer, ThreatClassifier, ThreatSignal


class TestDataPipeline(unittest.TestCase):
    def test_embedding_similarity(self):
        pipeline = DataPipeline()
        index = pipeline.build_index([
            "Reset admin credentials and rotate secrets.",
            "Isolate infected VM and run malware scan.",
        ])
        results = pipeline.search("How to isolate malware?", index, top_k=1)
        self.assertTrue(results)
        self.assertIn("malware", results[0].text.lower())


class TestThreatDetection(unittest.TestCase):
    def test_classification_and_priority(self):
        classifier = ThreatClassifier()
        signals = [ThreatSignal(source="log", description="login brute force", indicators=["ssh", "port"])]
        assessment = classifier.assess("Repeated SSH login errors", signals)
        category = assessment.category
        self.assertEqual(category, "intrusion")
        self.assertIn("ssh", assessment.evidence["intrusion"])

        prioritizer = IncidentPrioritizer()
        score = prioritizer.risk_score(assessment.scores, impacted_assets=5)
        severity = prioritizer.determine_severity(assessment.scores, impacted_assets=5)
        self.assertGreater(score, 0.5)
        self.assertIn(severity, {"medium", "high", "critical"})


class TestAgentWorkflow(unittest.TestCase):
    def setUp(self):
        self.agent = bootstrap_agent(
            [
                "Standard phishing response runbook includes credential reset.",
                "Cloud firewall playbook for malware isolation and ticketing.",
            ]
        )

    def test_response_creates_ticket_and_runbook(self):
        reply = self.agent.respond("We detected malware spreading laterally in the subnet")
        self.assertIn("ticket", reply.lower())
        self.assertEqual(len(self.agent.connectwise.created), 1)
        self.assertEqual(len(self.agent.confluence.entries), 1)

    def test_memory_tracks_conversation(self):
        self.agent.respond("Investigate suspicious login pattern")
        self.agent.respond("Follow-up with credential reset")
        self.assertEqual(len(self.agent.memory), 2)


if __name__ == "__main__":
    unittest.main()
