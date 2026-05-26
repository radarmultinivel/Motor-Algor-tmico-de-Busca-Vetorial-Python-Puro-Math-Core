# Desenvolvido por L. A. Leandro Sao Jose dos Campos- SP
# Data: 25-05-2026

import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.math_core.linear_algebra import dot_product, magnitude, cosine_similarity
from src.indexer.vector_db import VectorDatabase


class TestLinearAlgebra:
    def test_dot_product_basic(self):
        a = [1.0, 2.0, 3.0]
        b = [4.0, 5.0, 6.0]
        assert dot_product(a, b) == pytest.approx(32.0)

    def test_dot_product_negative(self):
        a = [-1.0, 2.0, -3.0]
        b = [4.0, -5.0, 6.0]
        assert dot_product(a, b) == pytest.approx(-32.0)

    def test_dot_product_dimension_mismatch(self):
        with pytest.raises(ValueError):
            dot_product([1.0, 2.0], [1.0, 2.0, 3.0])

    def test_magnitude_zero(self):
        assert magnitude([0.0, 0.0, 0.0]) == 0.0

    def test_magnitude_positive(self):
        assert magnitude([3.0, 4.0]) == pytest.approx(5.0)

    def test_magnitude_one(self):
        assert magnitude([1.0, 0.0, 0.0, 0.0]) == 1.0

    def test_cosine_identical_vectors(self):
        a = [0.12, 0.85, -0.34, 0.02, 0.55]
        assert cosine_similarity(a, a) == pytest.approx(1.0)

    def test_cosine_orthogonal_vectors(self):
        a = [1.0, 0.0]
        b = [0.0, 1.0]
        assert cosine_similarity(a, b) == pytest.approx(0.0)

    def test_cosine_opposite_vectors(self):
        a = [0.5, 0.5]
        b = [-0.5, -0.5]
        assert cosine_similarity(a, b) == pytest.approx(-1.0)

    def test_cosine_zero_vector(self):
        a = [0.0, 0.0, 0.0]
        b = [1.0, 2.0, 3.0]
        assert cosine_similarity(a, b) == 0.0

    def test_cosine_negative_coordinates(self):
        a = [-0.45, 0.70, 0.92, -0.10, 0.33]
        b = [0.12, 0.85, -0.34, 0.02, 0.55]
        result = cosine_similarity(a, b)
        assert -1.0 <= result <= 1.0


class TestVectorDatabase:
    def test_upsert_and_query_basic(self):
        db = VectorDatabase()
        db.upsert("a", [1.0, 0.0], "doc a")
        db.upsert("b", [0.0, 1.0], "doc b")
        results = db.query([1.0, 0.0], top_k=2)
        assert len(results) == 2
        assert results[0]["id"] == "a"
        assert results[0]["score"] == pytest.approx(1.0)
        assert results[1]["id"] == "b"
        assert results[1]["score"] == pytest.approx(0.0)

    def test_query_top_k_filtering(self):
        db = VectorDatabase()
        for i in range(10):
            db.upsert(f"doc_{i:02d}", [float(i % 5), float(i // 5)], f"payload {i}")
        results = db.query([1.0, 1.0], top_k=3)
        assert len(results) == 3

    def test_query_ordering_descending(self):
        db = VectorDatabase()
        db.upsert("c", [0.9, 0.1], "close")
        db.upsert("f", [0.1, 0.9], "far")
        results = db.query([1.0, 0.0], top_k=2)
        assert results[0]["id"] == "c"
        assert results[0]["score"] >= results[1]["score"]

    def test_query_payload_isolation(self):
        db = VectorDatabase()
        db.upsert("secret", [1.0, 0.0], "CONFIDENTIAL_KEY=abc123")
        results = db.query([1.0, 0.0], top_k=1)
        assert results[0]["payload"] == "CONFIDENTIAL_KEY=abc123"
        assert results[0]["id"] == "secret"

    def test_empty_database(self):
        db = VectorDatabase()
        assert db.query([1.0, 0.0], top_k=3) == []

    def test_update_existing_document(self):
        db = VectorDatabase()
        db.upsert("x", [1.0, 0.0], "old")
        db.upsert("x", [0.0, 1.0], "new")
        results = db.query([0.0, 1.0], top_k=1)
        assert results[0]["id"] == "x"
        assert results[0]["score"] == pytest.approx(1.0)
        assert results[0]["payload"] == "new"

    def test_negative_coordinates_ranking(self):
        db = VectorDatabase()
        db.upsert("neg", [-0.5, -0.5], "negative region")
        db.upsert("pos", [0.5, 0.5], "positive region")
        results = db.query([-0.5, -0.5], top_k=2)
        assert results[0]["id"] == "neg"
        assert results[0]["score"] == pytest.approx(1.0)
        assert results[1]["id"] == "pos"

    def test_large_dimensionality(self):
        a = [float(i) for i in range(100)]
        b = [float(i) for i in range(99, -1, -1)]
        sim = cosine_similarity(a, b)
        assert -1.0 <= sim <= 1.0


if __name__ == "__main__":
    sys.exit(pytest.main([__file__]))
