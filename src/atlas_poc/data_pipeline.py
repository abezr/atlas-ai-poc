"""Data ingestion and embedding utilities for the AI POC."""

from __future__ import annotations

import math
import re
from dataclasses import dataclass
from typing import Iterable, List


@dataclass
class EmbeddedDocument:
    """A preprocessed document with a deterministic embedding."""

    text: str
    vector: List[float]


class DataPipeline:
    """A simple ingest -> preprocess -> embed pipeline for RAG-like flows."""

    def __init__(self) -> None:
        self._stopwords = {"the", "and", "of", "to", "in", "for", "a"}

    def ingest(self, sources: Iterable[str]) -> List[str]:
        """Simulate ingestion from multiple sources (files, APIs, KBs)."""

        return [source.strip() for source in sources if source.strip()]

    def preprocess(self, text: str) -> str:
        """Normalize text and drop stopwords to reduce noise."""

        cleaned = re.sub(r"[^a-zA-Z0-9 ]", " ", text).lower()
        tokens = [t for t in cleaned.split() if t not in self._stopwords]
        return " ".join(tokens)

    def embed(self, text: str, dimensions: int = 8) -> List[float]:
        """Generate a lightweight deterministic embedding.

        The embedding hashes characters into buckets and normalizes the vector
        length. This avoids heavy dependencies while keeping similarity useful
        for retrieval in tests.
        """

        buckets = [0.0] * dimensions
        for idx, char in enumerate(text):
            bucket = idx % dimensions
            buckets[bucket] += (ord(char) % 37) / 37.0

        length = math.sqrt(sum(v * v for v in buckets)) or 1.0
        return [round(v / length, 4) for v in buckets]

    def build_index(self, sources: Iterable[str]) -> List[EmbeddedDocument]:
        """Create an embedded document index for retrieval."""

        documents: List[EmbeddedDocument] = []
        for source in self.ingest(sources):
            normalized = self.preprocess(source)
            documents.append(EmbeddedDocument(text=source, vector=self.embed(normalized)))
        return documents

    @staticmethod
    def cosine_similarity(a: List[float], b: List[float]) -> float:
        """Compute cosine similarity between vectors."""

        numerator = sum(x * y for x, y in zip(a, b))
        denom_a = math.sqrt(sum(x * x for x in a)) or 1.0
        denom_b = math.sqrt(sum(y * y for y in b)) or 1.0
        return round(numerator / (denom_a * denom_b), 4)

    def search(self, query: str, index: List[EmbeddedDocument], top_k: int = 3) -> List[EmbeddedDocument]:
        """Retrieve the most similar documents for a query."""

        normalized_query = self.preprocess(query)
        query_vector = self.embed(normalized_query)
        scored = [
            (self.cosine_similarity(query_vector, doc.vector), doc)
            for doc in index
        ]
        scored.sort(key=lambda pair: pair[0], reverse=True)
        return [doc for _, doc in scored[:top_k]]
