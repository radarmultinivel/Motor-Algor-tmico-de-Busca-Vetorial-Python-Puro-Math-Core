# Desenvolvido por L. A. Leandro Sao Jose dos Campos- SP
# Data: 25-05-2026

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from src.indexer.vector_db import VectorDatabase


def print_separator(char="=", width=70):
    print(char * width)


def main():
    db = VectorDatabase()

    db.upsert("doc_01", [0.12, 0.85, -0.34, 0.02, 0.55],
              "Contrato confidencial de TI")
    db.upsert("doc_02", [0.88, -0.11, 0.05, 0.41, -0.22],
              "Regulamento interno de RH")
    db.upsert("doc_03", [-0.45, 0.70, 0.92, -0.10, 0.33],
              "Relatorio financeiro Q4")
    db.upsert("doc_04", [0.25, 0.30, -0.80, 0.45, 0.11],
              "Politica de privacidade de dados")
    db.upsert("doc_05", [0.90, -0.05, 0.10, 0.50, -0.30],
              "Manual de integracao de sistemas")

    print_separator()
    print(" " * 15 + "MOTOR DE BUSCA VETORIAL (MATH CORE)")
    print(" " * 22 + "Cosine Similarity Engine")
    print_separator()

    print("\n>>> Documentos indexados (5):")
    print("    doc_01 | DIM=5 | TI")
    print("    doc_02 | DIM=5 | RH")
    print("    doc_03 | DIM=5 | Financeiro")
    print("    doc_04 | DIM=5 | Privacidade")
    print("    doc_05 | DIM=5 | Sistemas")
    print()

    query = [0.80, -0.10, 0.15, 0.45, -0.25]
    print_separator("-")
    print(f">>> Consulta (query vector): {query}")
    print(">>> Interpretacao: documento com perfil tecnologico/sistemico")
    print_separator("-")

    results = db.query(query, top_k=3)

    print(f"\n   TOP-3 RESULTADOS (rank decrescente de similaridade):\n")
    for i, r in enumerate(results, 1):
        print(f"   #{i} | ID: {r['id']}")
        print(f"       Score: {r['score']:.6f}")
        print(f"       Payload: {r['payload']}")
        print()

    close_match = results[0]
    print_separator("-")
    print(f">>> MELHOR CORRESPONDENCIA: {close_match['id']}")
    print(f">>> Score de similaridade: {close_match['score']:.6f}")
    print(">>> Quanto mais proximo de 1.0, maior a semelhanca semantica.")
    print_separator("=")


if __name__ == "__main__":
    main()
