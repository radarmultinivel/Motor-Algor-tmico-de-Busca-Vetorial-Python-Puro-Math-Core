# Motor Algorítmico de Busca Vetorial (Math Core)

**Desenvolvido por L. A. Leandro — São José dos Campos, SP**
**Data: 25-05-2026**

---

## 1. Objetivo do Programa

Implementar um motor de busca vetorial (*vector search engine*) em Python puro, sem dependências externas de álgebra linear ou bancos de dados vetoriais comerciais. O sistema demonstra o fundamento matemático da similaridade semântica entre vetores multidimensionais — mesma lógica empregada por sistemas como Pinecone, ChromaDB, FAISS e Milvus em Large Language Models (LLMs).

O programa recebe um vetor de consulta (*query vector*), percorre uma coleção de vetores indexados em memória e aplica a **Similaridade de Cosseno** para ranquear os documentos mais próximos semanticamente.

---

## 2. Requisitos

### 2.1 Funcionais

| ID | Requisito | Descrição |
|----|-----------|-----------|
| RF-01 | Produto Escalar | Calcular a soma das multiplicações elemento a elemento entre dois vetores |
| RF-02 | Norma L2 | Calcular a raiz quadrada da soma dos quadrados dos elementos de um vetor |
| RF-03 | Similaridade de Cosseno | Calcular o cosseno do ângulo entre dois vetores no espaço n-dimensional |
| RF-04 | Inserção/Atualização | Inserir ou atualizar um documento com vetor e payload textual |
| RF-05 | Consulta Top-K | Retornar os K documentos mais similares ordenados por score decrescente |
| RF-06 | Isolamento de Payload | Separar o vetor numérico do metadado textual por ID anônimo |
| RF-07 | Tratamento de Vetor Nulo | Retornar similaridade 0.0 quando qualquer vetor tiver magnitude nula |

### 2.2 Não Funcionais

| ID | Requisito | Descrição |
|----|-----------|-----------|
| RNF-01 | Zero Dependências | Nenhuma biblioteca externa de álgebra linear (sem NumPy, SciPy, FAISS) |
| RNF-02 | Python Puro | Apenas tipos primitivos (`list`, `dict`) e módulo `math` nativo |
| RNF-03 | Portabilidade | Deve executar em qualquer plataforma com Python 3.11+ |
| RNF-04 | Testabilidade | Cobertura de testes unitários com PyTest para todas as operações matemáticas |

---

## 3. Especificações Técnicas

### 3.1 Stack Tecnológica

| Camada | Tecnologia |
|--------|------------|
| Linguagem | Python 3.11+ |
| Runtime | CPython 3.12 |
| Testes | PyTest 8.x |
| Build | Nenhum (scripts nativos) |
| Versionamento | Git + GitHub |

### 3.2 Estrutura do Projeto

```
motor-busca-vetorial/
├── .gitignore
├── LICENSE
├── requirements.txt
├── README.md
└── src/
    ├── __init__.py
    ├── math_core/
    │   ├── __init__.py
    │   └── linear_algebra.py      # Funções matemáticas puras
    ├── indexer/
    │   ├── __init__.py
    │   └── vector_db.py           # Banco vetorial em memória
    └── main.py                    # Interface de demonstração
```

### 3.3 Dependências

- **Runtime:** Nenhuma (apenas biblioteca padrão do Python)
- **Desenvolvimento:** `pytest>=8.0` (instalado via `requirements.txt`)

---

## 4. Fluxograma da Arquitetura

```
┌─────────────────────────────────────────────────────────────┐
│                        main.py                              │
│  (Interface CLI / Demonstração Interativa)                  │
└────────────────────┬────────────────────────────────────────┘
                     │  importa
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                   vector_db.py                               │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              VectorDatabase                           │   │
│  │                                                       │   │
│  │  self._storage = {                                    │   │
│  │    "doc_01": {"vector": [...], "payload": "..."},     │   │
│  │    ...                                                │   │
│  │  }                                                    │   │
│  │                                                       │   │
│  │  Métodos:                                             │   │
│  │    upsert(id, vector, payload) → None                 │   │
│  │    query(vector, top_k) → list[dict]                  │   │
│  └───────────────┬───────────────────────────────────────┘   │
└──────────────────┼───────────────────────────────────────────┘
                   │  importa
                   ▼
┌─────────────────────────────────────────────────────────────┐
│                  linear_algebra.py                           │
│                                                             │
│  dot_product(a, b)  →  Σ(a[i] * b[i])                      │
│         ↓                                                   │
│  magnitude(v)       →  √(Σ(v[i]²))                         │
│         ↓                                                   │
│  cosine_similarity(a, b)  →  dot(a,b) / (|a| * |b|)        │
│                                                             │
│  Fluxo da consulta:                                         │
│                                                             │
│  Query Vector → dot_product → magnitude → cosine_similarity │
│                                                ↓            │
│                                        Score ∈ [-1, 1]      │
│                                                ↓            │
│                                       Ordenação decrescente │
│                                                ↓            │
│                                       Retorno Top-K         │
└─────────────────────────────────────────────────────────────┘
```

---

## 5. Instalação

### 5.1 Pré-requisitos

- Python 3.11 ou superior instalado
- Git (opcional, para clonar)

### 5.2 Passo a Passo

```bash
# 1. Clonar o repositório
git clone https://github.com/L-A-Leandro/motor-busca-vetorial.git
cd motor-busca-vetorial

# 2. (Opcional) Criar ambiente virtual
python -m venv .venv

# Windows:
.venv\Scripts\activate
# Linux/macOS:
# source .venv/bin/activate

# 3. Executar a demonstração
python src/main.py

# 4. (Opcional) Instalar pytest e rodar testes
pip install -r requirements.txt
python -m pytest tests/ -v
```

---

## 6. Manual do Usuário

### 6.1 Execução

Execute o programa com:

```bash
python src/main.py
```

### 6.2 Tela de Demonstração

```
======================================================================
               MOTOR DE BUSCA VETORIAL (MATH CORE)
                      Cosine Similarity Engine
======================================================================

>>> Documentos indexados (5):
    doc_01 | DIM=5 | TI
    doc_02 | DIM=5 | RH
    doc_03 | DIM=5 | Financeiro
    doc_04 | DIM=5 | Privacidade
    doc_05 | DIM=5 | Sistemas

----------------------------------------------------------------------
>>> Consulta (query vector): [0.8, -0.1, 0.15, 0.45, -0.25]
>>> Interpretacao: documento com perfil tecnologico/sistemico
----------------------------------------------------------------------

   TOP-3 RESULTADOS (rank decrescente de similaridade):

   #1 | ID: doc_05
       Score: 0.996211
       Payload: Manual de integracao de sistemas

   #2 | ID: doc_02
       Score: 0.990828
       Payload: Regulamento interno de RH

   #3 | ID: doc_04
       Score: 0.231558
       Payload: Politica de privacidade de dados

----------------------------------------------------------------------
>>> MELHOR CORRESPONDENCIA: doc_05
>>> Score de similaridade: 0.996211
>>> Quanto mais proximo de 1.0, maior a semelhanca semantica.
======================================================================
```

### 6.3 Interpretação dos Resultados

- **Score = 1.0** → Vetores idênticos (máxima similaridade semântica)
- **Score = 0.0** → Vetores ortogonais (sem relação semântica)
- **Score = -1.0** → Vetores opostos (sentidos opostos no espaço vetorial)
- **Score entre 0 e 1** → Grau de proximidade proporcional ao valor

### 6.4 API de Referência

#### `linear_algebra.py`

| Função | Assinatura | Retorno |
|--------|-----------|---------|
| `dot_product` | `(a: list[float], b: list[float]) -> float` | Produto escalar |
| `magnitude` | `(v: list[float]) -> float` | Norma L2 |
| `cosine_similarity` | `(a: list[float], b: list[float]) -> float` | Similaridade de cosseno |

#### `vector_db.py`

| Método | Assinatura | Retorno |
|--------|-----------|---------|
| `upsert` | `(document_id: str, vector: list[float], payload: str) -> None` | — |
| `query` | `(query_vector: list[float], top_k: int = 3) -> list[dict]` | Lista com `id`, `score`, `payload` |

---

## 7. Testes

### 7.1 Execução dos Testes

```bash
python -m pytest tests/ -v
```

### 7.2 Cenários Testados

| Categoria | Teste | Descrição |
|-----------|-------|-----------|
| **Produto Escalar** | `test_dot_product_basic` | Multiplicação básica entre vetores positivos |
| | `test_dot_product_negative` | Multiplicação com coordenadas negativas |
| | `test_dot_product_dimension_mismatch` | Erro para vetores de dimensões diferentes |
| **Norma L2** | `test_magnitude_zero` | Vetor nulo retorna 0 |
| | `test_magnitude_positive` | Triângulo 3-4-5 retorna 5 |
| | `test_magnitude_one` | Vetor unitário retorna 1 |
| **Similaridade de Cosseno** | `test_cosine_identical_vectors` | Vetores idênticos retornam 1.0 |
| | `test_cosine_orthogonal_vectors` | Vetores perpendiculares retornam 0.0 |
| | `test_cosine_opposite_vectors` | Vetores opostos retornam -1.0 |
| | `test_cosine_zero_vector` | Vetor nulo retorna 0.0 |
| | `test_cosine_negative_coordinates` | Valida intervalo [-1, 1] com negativos |
| **Banco Vetorial** | `test_upsert_and_query_basic` | Inserção e consulta básica |
| | `test_query_top_k_filtering` | Filtro de top-k funciona |
| | `test_query_ordering_descending` | Ordenação estritamente decrescente |
| | `test_query_payload_isolation` | Payload isolado por ID |
| | `test_empty_database` | Banco vazio retorna lista vazia |
| | `test_update_existing_document` | Atualização de documento existente |
| | `test_negative_coordinates_ranking` | Ranking com coordenadas negativas |
| | `test_large_dimensionality` | Vetores de 100 dimensões |

### 7.3 Resultado Esperado

```
============================= 19 passed in 0.20s ==============================
```

---

## 8. Fórmulas Matemáticas

### Produto Escalar (Dot Product)

```
dot(A, B) = Σ(A[i] × B[i])  para i = 1 até n
```

### Norma L2 (Magnitude)

```
|V| = √(Σ(V[i]²))  para i = 1 até n
```

### Similaridade de Cosseno

```
cos(θ) = dot(A, B) / (|A| × |B|)
```

Onde `θ` é o ângulo entre os vetores A e B no espaço n-dimensional.

---

## 9. Licença

MIT License — Copyright (c) 2026 L. A. Leandro

---

**Contato:** L. A. Leandro — São José dos Campos, SP
