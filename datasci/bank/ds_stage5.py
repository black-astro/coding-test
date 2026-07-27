"""5단계 연습문제 — LLM · 트랜스포머.

동점(tie)이 생기면 정렬 순서가 불안정해져 채점이 흔들린다.
그래서 모든 테스트케이스는 **순위가 유일하게 정해지도록** 설계했다.
"""

from engine.models import Problem

STAGE = "5. LLM · 트랜스포머"


def _p(**kw):
    kw.setdefault("rank", "Bronze")
    kw.setdefault("style", "데이터분석")
    kw.setdefault("type", "func")
    kw.setdefault("func_name", "solution")
    kw.setdefault("category", STAGE)
    return Problem(**kw)


PROBLEMS = [

    _p(
        id="dsq5-01",
        title="문자 단위 토크나이저",
        topic="토크나이저",
        description=(
            "말뭉치로 문자 단위 사전을 만들고, 주어진 문장을 인코딩·디코딩하세요.\n"
            "\n"
            "  1) 말뭉치에 등장한 문자를 중복 없이 모아 **오름차순 정렬**한다\n"
            "     (정렬해야 실행할 때마다 번호가 같아진다)\n"
            "  2) 앞에서부터 0, 1, 2 ... 번호를 붙인다\n"
            "  3) 문장을 번호 리스트로 바꾼다(인코딩)\n"
            "  4) 번호 리스트를 다시 문자열로 되돌린다(디코딩)\n"
            "\n"
            "[사전 크기, 인코딩 결과, 디코딩 결과] 를 반환하세요.\n"
            "질의 문장의 모든 문자는 말뭉치에 반드시 포함되어 있습니다."
        ),
        input_desc="text: 말뭉치 문자열, query: 인코딩할 문자열",
        output_desc="[사전 크기(int), 번호 리스트, 디코딩된 문자열]",
        examples=[
            {"args": ["abcabc", "cab"], "output": [3, [2, 0, 1], "cab"]},
        ],
        hints=[
            "set 으로 중복을 없애고 sorted 로 정렬하면 사전이 됩니다.",
            "문자→번호, 번호→문자 두 방향의 딕셔너리를 만들어 두면 편합니다.\n"
            "  stoi = {c: i for i, c in enumerate(chars)}\n"
            "디코딩 결과는 원래 문장과 같아야 합니다. 이것이 토크나이저의 검증 방법입니다.",
            "chars = sorted(set(text))\n"
            "stoi = {c: i for i, c in enumerate(chars)}\n"
            "itos = {i: c for c, i in stoi.items()}\n"
            "ids = [stoi[c] for c in query]\n"
            "return [len(chars), ids, ''.join(itos[i] for i in ids)]",
        ],
        testcases=[
            {"args": ["abcabc", "cab"], "expected": [3, [2, 0, 1], "cab"]},
            {"args": ["나는 밥", "밥나"], "expected": [4, [3, 1], "밥나"]},
            {"args": ["aaa", "a"], "expected": [1, [0], "a"]},
            {"args": ["xyz", "zyx"], "expected": [3, [2, 1, 0], "zyx"]},
            {"args": ["hello", "leo"], "expected": [4, [2, 0, 3], "leo"]},
        ],
        reference_py=(
            "def solution(text, query):\n"
            "    chars = sorted(set(text))\n"
            "    stoi = {c: i for i, c in enumerate(chars)}\n"
            "    itos = {i: c for c, i in stoi.items()}\n"
            "    ids = [stoi[c] for c in query]\n"
            "    return [len(chars), ids, ''.join(itos[i] for i in ids)]\n"
        ),
        template_py=(
            "def solution(text, query):\n"
            "    # [사전 크기, 인코딩 결과, 디코딩 결과] 를 반환하세요.\n"
            "    # 사전은 문자를 오름차순 정렬해 만듭니다.\n"
            "    return []\n"
        ),
    ),

    _p(
        id="dsq5-02",
        title="어텐션 가중치 계산",
        topic="어텐션",
        description=(
            "Q 와 K 를 받아 스케일드 닷프로덕트 어텐션의 **가중치**를 구하세요.\n"
            "\n"
            "  1) score = Q @ Kᵀ / √d_k        (d_k = Q 의 열 개수)\n"
            "  2) 각 행에 softmax 를 적용한다\n"
            "\n"
            "softmax 는 행별로 최댓값을 뺀 뒤 계산하세요(오버플로 방지).\n"
            "각 행의 합은 1 이 됩니다.\n"
            "\n"
            "결과는 소수 넷째 자리까지 반올림합니다."
        ),
        input_desc="Q: 2차원 리스트 (질의 개수 × d_k), K: 2차원 리스트 (키 개수 × d_k)",
        output_desc="어텐션 가중치 2차원 리스트 — 각 값 round(x, 4)",
        examples=[
            {"args": [[[1, 0]], [[1, 0], [0, 1]]], "output": [[0.6698, 0.3302]]},
        ],
        hints=[
            "Q @ K.T 로 모든 질의-키 쌍의 점수를 한 번에 구합니다.",
            "√d_k 로 나누는 이유는 차원이 크면 내적 값이 커져\n"
            "softmax 가 한쪽으로 극단적으로 쏠리기 때문입니다.\n"
            "softmax 는 axis=1(행 방향)으로 적용해야 하며 keepdims=True 가 필요합니다.",
            "import numpy as np\n"
            "Qa = np.array(Q, dtype=float)\n"
            "Ka = np.array(K, dtype=float)\n"
            "s = Qa @ Ka.T / np.sqrt(Qa.shape[1])\n"
            "e = np.exp(s - s.max(axis=1, keepdims=True))\n"
            "w = e / e.sum(axis=1, keepdims=True)\n"
            "return [[round(float(v), 4) for v in row] for row in w]",
        ],
        testcases=[
            {"args": [[[1, 0]], [[1, 0], [0, 1]]], "expected": [[0.6698, 0.3302]]},
            {"args": [[[1, 0], [0, 1]], [[1, 0], [0, 1]]],
             "expected": [[0.6698, 0.3302], [0.3302, 0.6698]]},
            {"args": [[[0, 0]], [[1, 1], [2, 2]]], "expected": [[0.5, 0.5]]},
            {"args": [[[1, 1]], [[1, 1], [-1, -1]]], "expected": [[0.9442, 0.0558]]},
        ],
        reference_py=(
            "import numpy as np\n"
            "\n"
            "def solution(Q, K):\n"
            "    Qa = np.array(Q, dtype=float)\n"
            "    Ka = np.array(K, dtype=float)\n"
            "    s = Qa @ Ka.T / np.sqrt(Qa.shape[1])\n"
            "    e = np.exp(s - s.max(axis=1, keepdims=True))\n"
            "    w = e / e.sum(axis=1, keepdims=True)\n"
            "    return [[round(float(v), 4) + 0.0 for v in row] for row in w]\n"
        ),
        template_py=(
            "import numpy as np\n"
            "\n"
            "def solution(Q, K):\n"
            "    # 스케일드 닷프로덕트 어텐션의 가중치를 반환하세요.\n"
            "    return []\n"
        ),
    ),

    _p(
        id="dsq5-03",
        title="causal mask 적용",
        topic="어텐션",
        description=(
            "GPT 같은 생성 모델은 **뒤쪽 토큰을 미리 보면 안 됩니다.**\n"
            "어텐션 점수 행렬에 causal mask 를 적용한 뒤 softmax 를 구하세요.\n"
            "\n"
            "  · i 번째 행은 0 ~ i 번째 열까지만 볼 수 있다\n"
            "  · 그보다 오른쪽(j > i)은 -무한대로 만들어 softmax 후 0 이 되게 한다\n"
            "\n"
            "즉 대각선 위쪽(상삼각)을 차단합니다.\n"
            "각 행의 합은 1 이 되고, 결과는 소수 넷째 자리까지 반올림합니다."
        ),
        input_desc="scores: 정사각 2차원 리스트 (어텐션 점수)",
        output_desc="마스크 적용 후 softmax 결과 2차원 리스트 — 각 값 round(x, 4)",
        examples=[
            {"args": [[[1, 2], [3, 4]]], "output": [[1.0, 0.0], [0.2689, 0.7311]]},
        ],
        hints=[
            "np.triu(np.ones((n, n)), k=1) 은 대각선 위쪽만 1인 행렬을 만듭니다.\n"
            "k=1 은 '대각선 자기 자신은 제외' 라는 뜻입니다.",
            "그 행렬에 아주 작은 수(-1e9)를 곱해 점수에 더하면,\n"
            "softmax 를 통과했을 때 그 자리가 0 이 됩니다.\n"
            "0번 행은 자기 자신만 볼 수 있으므로 항상 [1.0, 0, 0, ...] 이 됩니다.",
            "import numpy as np\n"
            "S = np.array(scores, dtype=float)\n"
            "n = S.shape[0]\n"
            "mask = np.triu(np.ones((n, n)), k=1) * -1e9\n"
            "z = S + mask\n"
            "e = np.exp(z - z.max(axis=1, keepdims=True))\n"
            "w = e / e.sum(axis=1, keepdims=True)\n"
            "return [[round(float(v), 4) for v in row] for row in w]",
        ],
        testcases=[
            {"args": [[[1, 2], [3, 4]]], "expected": [[1.0, 0.0], [0.2689, 0.7311]]},
            {"args": [[[0, 0, 0], [0, 0, 0], [0, 0, 0]]],
             "expected": [[1.0, 0.0, 0.0], [0.5, 0.5, 0.0], [0.3333, 0.3333, 0.3333]]},
            {"args": [[[5]]], "expected": [[1.0]]},
            {"args": [[[1, 9], [0, 0]]], "expected": [[1.0, 0.0], [0.5, 0.5]]},
        ],
        reference_py=(
            "import numpy as np\n"
            "\n"
            "def solution(scores):\n"
            "    S = np.array(scores, dtype=float)\n"
            "    n = S.shape[0]\n"
            "    mask = np.triu(np.ones((n, n)), k=1) * -1e9\n"
            "    z = S + mask\n"
            "    e = np.exp(z - z.max(axis=1, keepdims=True))\n"
            "    w = e / e.sum(axis=1, keepdims=True)\n"
            "    return [[round(float(v), 4) + 0.0 for v in row] for row in w]\n"
        ),
        template_py=(
            "import numpy as np\n"
            "\n"
            "def solution(scores):\n"
            "    # causal mask 를 적용한 뒤 행별 softmax 를 반환하세요.\n"
            "    return []\n"
        ),
    ),

    _p(
        id="dsq5-04",
        title="top-k 샘플링 필터",
        topic="샘플링",
        description=(
            "확률 분포에서 상위 k 개만 남기고 나머지는 0 으로 만든 뒤,\n"
            "합이 1 이 되도록 다시 정규화해 반환하세요.\n"
            "\n"
            "  1) 확률이 높은 순으로 k 개를 고른다\n"
            "  2) 나머지는 0 으로 만든다\n"
            "  3) 남은 값들의 합으로 나눠 정규화한다\n"
            "\n"
            "입력 확률에 동점은 없습니다(상위 k 개가 유일하게 정해집니다).\n"
            "결과는 소수 넷째 자리까지 반올림합니다."
        ),
        input_desc="p: 확률 리스트(합이 1), k: 남길 개수(정수)",
        output_desc="필터링 후 정규화된 확률 리스트 — 각 값 round(x, 4)",
        examples=[
            {"args": [[0.5, 0.3, 0.15, 0.05], 2], "output": [0.625, 0.375, 0.0, 0.0]},
        ],
        hints=[
            "np.argsort 는 오름차순 인덱스를 줍니다. [::-1] 로 뒤집으면 내림차순입니다.",
            "0 으로 채운 배열을 만들고 상위 k 개 위치에만 원래 값을 넣으세요.\n"
            "그 다음 전체 합으로 나누면 정규화됩니다.\n"
            "위치(순서)는 원래 배열 그대로 유지해야 합니다.",
            "import numpy as np\n"
            "a = np.array(p, dtype=float)\n"
            "out = np.zeros_like(a)\n"
            "idx = np.argsort(a)[::-1][:k]\n"
            "out[idx] = a[idx]\n"
            "out = out / out.sum()\n"
            "return [round(float(v), 4) for v in out]",
        ],
        testcases=[
            {"args": [[0.5, 0.3, 0.15, 0.05], 2], "expected": [0.625, 0.375, 0.0, 0.0]},
            {"args": [[0.4, 0.3, 0.2, 0.1], 1], "expected": [1.0, 0.0, 0.0, 0.0]},
            {"args": [[0.4, 0.3, 0.2, 0.1], 4], "expected": [0.4, 0.3, 0.2, 0.1]},
            {"args": [[0.1, 0.6, 0.3], 2], "expected": [0.0, 0.6667, 0.3333]},
            {"args": [[0.7, 0.2, 0.1], 2], "expected": [0.7778, 0.2222, 0.0]},
        ],
        reference_py=(
            "import numpy as np\n"
            "\n"
            "def solution(p, k):\n"
            "    a = np.array(p, dtype=float)\n"
            "    out = np.zeros_like(a)\n"
            "    idx = np.argsort(a)[::-1][:k]\n"
            "    out[idx] = a[idx]\n"
            "    out = out / out.sum()\n"
            "    return [round(float(v), 4) + 0.0 for v in out]\n"
        ),
        template_py=(
            "import numpy as np\n"
            "\n"
            "def solution(p, k):\n"
            "    # 상위 k 개만 남기고 정규화한 확률 리스트를 반환하세요.\n"
            "    return []\n"
        ),
    ),

    _p(
        id="dsq5-05",
        title="RAG 문서 검색",
        topic="RAG",
        description=(
            "질문과 가장 관련 있는 문서를 코사인 유사도로 찾으세요.\n"
            "\n"
            "  1) 모든 문서를 공백으로 나눠 나온 단어를 모아 **정렬해** 어휘를 만든다\n"
            "  2) 각 문서·질문을 '단어 등장 여부' 벡터로 만든다 (있으면 1, 없으면 0)\n"
            "  3) 각 벡터를 길이 1 로 정규화한다\n"
            "  4) 질문 벡터와의 내적(= 코사인 유사도)이 큰 순으로 상위 k 개를 고른다\n"
            "\n"
            "길이가 0 인 벡터를 나누지 않도록 분모에 1e-9 를 더하세요.\n"
            "유사도에 동점은 없습니다.\n"
            "\n"
            "[[문서 번호, 유사도], ...] 를 반환하고 유사도는 소수 넷째 자리까지 반올림합니다."
        ),
        input_desc="docs: 문서 문자열 리스트, query: 질문 문자열, k: 반환 개수(정수)",
        output_desc="[[문서 인덱스(int), 유사도(float)], ...] — 유사도 내림차순",
        examples=[
            {"args": [["매출 증가", "비용 절감", "매출 목표 설정"], "매출 증가", 2],
             "output": [[0, 1.0], [2, 0.4082]]},
        ],
        hints=[
            "어휘는 모든 문서의 단어를 모아 sorted 로 정렬해 만듭니다.\n"
            "정렬해야 실행할 때마다 벡터 순서가 같아집니다.",
            "벡터를 길이 1 로 정규화(단위벡터)하면 내적이 곧 코사인 유사도가 됩니다.\n"
            "  v / (np.linalg.norm(v) + 1e-9)\n"
            "질문에만 있고 문서에 없는 단어는 어휘에 없으므로 자연히 무시됩니다.",
            "import numpy as np\n"
            "vocab = sorted({w for d in docs for w in d.split()})\n"
            "def embed(t):\n"
            "    s = set(t.split())\n"
            "    v = np.array([1.0 if w in s else 0.0 for w in vocab])\n"
            "    return v / (np.linalg.norm(v) + 1e-9)\n"
            "D = np.array([embed(d) for d in docs])\n"
            "sims = D @ embed(query)\n"
            "top = np.argsort(sims)[::-1][:k]\n"
            "return [[int(i), round(float(sims[i]), 4)] for i in top]",
        ],
        testcases=[
            {"args": [["매출 증가", "비용 절감", "매출 목표 설정"], "매출 증가", 2],
             "expected": [[0, 1.0], [2, 0.4082]]},
            {"args": [["a b c", "d e", "a b"], "a b", 1], "expected": [[2, 1.0]]},
            {"args": [["x y z", "y", "w"], "y", 2], "expected": [[1, 1.0], [0, 0.5774]]},
            {"args": [["p q", "r s"], "p", 1], "expected": [[0, 0.7071]]},
            {"args": [["학생 공부", "교사 수업 준비"], "학생", 2],
             "expected": [[0, 0.7071], [1, 0.0]]},
        ],
        reference_py=(
            "import numpy as np\n"
            "\n"
            "def solution(docs, query, k):\n"
            "    vocab = sorted({w for d in docs for w in d.split()})\n"
            "\n"
            "    def embed(t):\n"
            "        s = set(t.split())\n"
            "        v = np.array([1.0 if w in s else 0.0 for w in vocab])\n"
            "        return v / (np.linalg.norm(v) + 1e-9)\n"
            "\n"
            "    D = np.array([embed(d) for d in docs])\n"
            "    sims = D @ embed(query)\n"
            "    top = np.argsort(sims)[::-1][:k]\n"
            "    return [[int(i), round(float(sims[i]), 4) + 0.0] for i in top]\n"
        ),
        template_py=(
            "import numpy as np\n"
            "\n"
            "def solution(docs, query, k):\n"
            "    # 코사인 유사도 상위 k 개 문서를 [[인덱스, 유사도], ...] 로 반환하세요.\n"
            "    return []\n"
        ),
    ),
]
