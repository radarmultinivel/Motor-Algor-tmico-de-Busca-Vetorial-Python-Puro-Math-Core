# Desenvolvido por L. A. Leandro Sao Jose dos Campos- SP
# Data: 25-05-2026

from src.math_core.linear_algebra import cosine_similarity


class VectorDatabase:
    def __init__(self):
        self._storage: dict[str, dict] = {}

    def upsert(self, document_id: str, vector: list[float], payload: str) -> None:
        self._storage[document_id] = {"vector": vector, "payload": payload}

    def query(self, query_vector: list[float], top_k: int = 3) -> list[dict]:
        scored = []
        for doc_id, data in self._storage.items():
            score = cosine_similarity(query_vector, data["vector"])
            scored.append({
                "id": doc_id,
                "score": round(score, 6),
                "payload": data["payload"],
            })
        scored.sort(key=lambda x: x["score"], reverse=True)
        return scored[:top_k]
