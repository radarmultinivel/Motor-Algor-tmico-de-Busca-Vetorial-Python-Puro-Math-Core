# Desenvolvido por L. A. Leandro Sao Jose dos Campos- SP
# Data: 25-05-2026

import math


def dot_product(a: list[float], b: list[float]) -> float:
    if len(a) != len(b):
        raise ValueError("Vectors must have the same dimension")
    total = 0.0
    for i in range(len(a)):
        total += a[i] * b[i]
    return total


def magnitude(v: list[float]) -> float:
    total = 0.0
    for component in v:
        total += component * component
    return math.sqrt(total)


def cosine_similarity(a: list[float], b: list[float]) -> float:
    dot = dot_product(a, b)
    mag_a = magnitude(a)
    mag_b = magnitude(b)
    if mag_a == 0.0 or mag_b == 0.0:
        return 0.0
    return dot / (mag_a * mag_b)
