"""3단계 연습문제 — 머신러닝.

모든 기대값은 tools/verify_datasci.py 로 실측해 확정했다.
반환값은 repr 비교이므로 numpy 스칼라를 그대로 돌려주면 안 된다.
"""

from engine.models import Problem

STAGE = "3. 머신러닝"


def _p(**kw):
    kw.setdefault("rank", "Bronze")
    kw.setdefault("style", "데이터분석")
    kw.setdefault("type", "func")
    kw.setdefault("func_name", "solution")
    kw.setdefault("category", STAGE)
    return Problem(**kw)


PROBLEMS = [

    _p(
        id="dsq3-01",
        title="회귀 평가지표 4종",
        topic="평가지표",
        description=(
            "실제값과 예측값을 받아 [MSE, RMSE, MAE, R²] 를 반환하세요.\n"
            "\n"
            "  MSE  = 평균( (실제-예측)² )\n"
            "  RMSE = √MSE\n"
            "  MAE  = 평균( |실제-예측| )\n"
            "  R²   = 1 - Σ(실제-예측)² / Σ(실제-실제평균)²\n"
            "\n"
            "실제값이 모두 같은 경우(R² 의 분모가 0)는 입력으로 주어지지 않습니다.\n"
            "네 값 모두 소수 넷째 자리까지 반올림합니다."
        ),
        input_desc="true: 숫자 리스트, pred: 숫자 리스트 (길이 동일, 2 이상)",
        output_desc="[MSE, RMSE, MAE, R²] — 각각 round(x, 4)",
        examples=[
            {"args": [[3, 5, 7, 9], [2.5, 5.5, 7.5, 8.5]], "output": [0.25, 0.5, 0.5, 0.95]},
        ],
        hints=[
            "numpy 배열로 바꾸면 (true - pred) 로 오차 배열을 한 번에 구할 수 있습니다.",
            "R² 의 분모는 '실제값과 실제평균의 차이 제곱합' 입니다.\n"
            "이는 '평균으로만 예측했을 때의 오차' 를 뜻하며, 모델이 그보다\n"
            "얼마나 나은지를 재는 기준이 됩니다.",
            "import numpy as np\n"
            "t = np.array(true, dtype=float)\n"
            "p = np.array(pred, dtype=float)\n"
            "mse = float(((t - p) ** 2).mean())\n"
            "mae = float(np.abs(t - p).mean())\n"
            "r2 = float(1 - ((t - p) ** 2).sum() / ((t - t.mean()) ** 2).sum())\n"
            "return [round(mse, 4), round(float(np.sqrt(mse)), 4),\n"
            "        round(mae, 4), round(r2, 4)]",
        ],
        testcases=[
            {"args": [[3, 5, 7, 9], [2.5, 5.5, 7.5, 8.5]], "expected": [0.25, 0.5, 0.5, 0.95]},
            {"args": [[1, 2, 3], [1, 2, 3]], "expected": [0.0, 0.0, 0.0, 1.0]},
            {"args": [[10, 20, 30], [20, 20, 20]], "expected": [66.6667, 8.165, 6.6667, 0.0]},
            {"args": [[1, 2, 3, 4], [2, 2, 2, 2]], "expected": [1.5, 1.2247, 1.0, -0.2]},
            {"args": [[5, 10], [6, 9]], "expected": [1.0, 1.0, 1.0, 0.84]},
        ],
        reference_py=(
            "import numpy as np\n"
            "\n"
            "def solution(true, pred):\n"
            "    t = np.array(true, dtype=float)\n"
            "    p = np.array(pred, dtype=float)\n"
            "    mse = float(((t - p) ** 2).mean())\n"
            "    mae = float(np.abs(t - p).mean())\n"
            "    ss_res = float(((t - p) ** 2).sum())\n"
            "    ss_tot = float(((t - t.mean()) ** 2).sum())\n"
            "    r2 = 1 - ss_res / ss_tot\n"
            "    return [round(mse, 4) + 0.0, round(float(np.sqrt(mse)), 4) + 0.0,\n"
            "            round(mae, 4) + 0.0, round(r2, 4) + 0.0]\n"
        ),
        template_py=(
            "import numpy as np\n"
            "\n"
            "def solution(true, pred):\n"
            "    # [MSE, RMSE, MAE, R2] 를 소수 넷째 자리까지 반환하세요.\n"
            "    return []\n"
        ),
    ),

    _p(
        id="dsq3-02",
        title="경사하강법 한 스텝",
        topic="선형회귀",
        description=(
            "단순 선형회귀 y = wx + b 에서 경사하강법을 **한 번만** 수행한 뒤의\n"
            "[새 w, 새 b] 를 반환하세요.\n"
            "\n"
            "손실은 MSE 이고 기울기는 다음과 같습니다 (n = 데이터 개수).\n"
            "\n"
            "  오차 e = y - (w·x + b)\n"
            "  ∂L/∂w = -2 × 평균( x · e )\n"
            "  ∂L/∂b = -2 × 평균( e )\n"
            "\n"
            "  새 w = w - 학습률 × ∂L/∂w\n"
            "  새 b = b - 학습률 × ∂L/∂b\n"
            "\n"
            "두 값 모두 소수 여섯째 자리까지 반올림합니다."
        ),
        input_desc="x: 숫자 리스트, y: 숫자 리스트, w: 실수, b: 실수, lr: 학습률(실수)",
        output_desc="[새 w, 새 b] — 각각 round(x, 6)",
        examples=[
            {"args": [[1, 2, 3], [2, 4, 6], 0.0, 0.0, 0.1], "output": [1.866667, 0.8]},
        ],
        hints=[
            "먼저 현재 w, b 로 예측값을 구하고 오차 e = y - 예측 을 계산합니다.",
            "기울기 공식을 그대로 옮기면 됩니다.\n"
            "주의: 부호를 헷갈리기 쉽습니다. 기울기의 **반대 방향**으로 이동해야\n"
            "손실이 줄어듭니다. 즉 w = w - lr * dw 입니다.",
            "import numpy as np\n"
            "xa = np.array(x, dtype=float)\n"
            "ya = np.array(y, dtype=float)\n"
            "e = ya - (w * xa + b)\n"
            "dw = -2 * (xa * e).mean()\n"
            "db = -2 * e.mean()\n"
            "return [round(w - lr * dw, 6), round(b - lr * db, 6)]",
        ],
        testcases=[
            {"args": [[1, 2, 3], [2, 4, 6], 0.0, 0.0, 0.1], "expected": [1.866667, 0.8]},
            {"args": [[1, 2], [3, 5], 1.0, 1.0, 0.05], "expected": [1.25, 1.15]},
            {"args": [[0, 1], [0, 1], 0.5, 0.0, 0.1], "expected": [0.55, 0.05]},
            {"args": [[2, 4, 6], [1, 2, 3], 0.0, 0.0, 0.01], "expected": [0.186667, 0.04]},
            {"args": [[1, 1, 1], [1, 1, 1], 1.0, 0.0, 0.1], "expected": [1.0, 0.0]},
        ],
        reference_py=(
            "import numpy as np\n"
            "\n"
            "def solution(x, y, w, b, lr):\n"
            "    xa = np.array(x, dtype=float)\n"
            "    ya = np.array(y, dtype=float)\n"
            "    e = ya - (w * xa + b)\n"
            "    dw = -2 * float((xa * e).mean())\n"
            "    db = -2 * float(e.mean())\n"
            "    return [round(w - lr * dw, 6) + 0.0, round(b - lr * db, 6) + 0.0]\n"
        ),
        template_py=(
            "import numpy as np\n"
            "\n"
            "def solution(x, y, w, b, lr):\n"
            "    # 경사하강법 한 스텝 후의 [w, b] 를 반환하세요.\n"
            "    return []\n"
        ),
    ),

    _p(
        id="dsq3-03",
        title="분류 평가지표",
        topic="평가지표",
        description=(
            "이진 분류의 실제 라벨과 예측 라벨을 받아\n"
            "[정확도, 정밀도, 재현율, F1] 을 반환하세요.\n"
            "\n"
            "  TP = 실제 1 · 예측 1      FP = 실제 0 · 예측 1\n"
            "  FN = 실제 1 · 예측 0      TN = 실제 0 · 예측 0\n"
            "\n"
            "  정확도 = (TP+TN) / 전체\n"
            "  정밀도 = TP / (TP+FP)     분모가 0 이면 0.0\n"
            "  재현율 = TP / (TP+FN)     분모가 0 이면 0.0\n"
            "  F1     = 2×정밀도×재현율 / (정밀도+재현율)   분모가 0 이면 0.0\n"
            "\n"
            "네 값 모두 소수 넷째 자리까지 반올림합니다."
        ),
        input_desc="y_true: 0/1 리스트, y_pred: 0/1 리스트 (길이 동일)",
        output_desc="[정확도, 정밀도, 재현율, F1] — 각각 round(x, 4)",
        examples=[
            {"args": [[1, 1, 0, 0, 1], [1, 0, 0, 0, 1]], "output": [0.8, 1.0, 0.6667, 0.8]},
        ],
        hints=[
            "numpy 배열의 비교 연산과 & 를 조합하면 TP/FP/FN/TN 을 셀 수 있습니다.\n"
            "예: ((pred == 1) & (true == 1)).sum()",
            "분모가 0 인 경우를 반드시 처리해야 합니다.\n"
            "양성 예측이 하나도 없으면 정밀도는 정의되지 않는데, 이 문제에서는 0.0 으로 둡니다.\n"
            "마지막 테스트케이스처럼 '전부 0 으로 찍는' 모델은 정확도만 0.9 로 높습니다.\n"
            "불균형 데이터에서 정확도가 속이는 대표적인 예입니다.",
            "import numpy as np\n"
            "t = np.array(y_true); p = np.array(y_pred)\n"
            "tp = int(((p == 1) & (t == 1)).sum())\n"
            "fp = int(((p == 1) & (t == 0)).sum())\n"
            "fn = int(((p == 0) & (t == 1)).sum())\n"
            "tn = int(((p == 0) & (t == 0)).sum())\n"
            "acc = (tp + tn) / len(t)\n"
            "pr = tp / (tp + fp) if (tp + fp) else 0.0\n"
            "rc = tp / (tp + fn) if (tp + fn) else 0.0\n"
            "f1 = 2 * pr * rc / (pr + rc) if (pr + rc) else 0.0\n"
            "return [round(acc, 4), round(pr, 4), round(rc, 4), round(f1, 4)]",
        ],
        testcases=[
            {"args": [[1, 1, 0, 0, 1], [1, 0, 0, 0, 1]], "expected": [0.8, 1.0, 0.6667, 0.8]},
            {"args": [[1, 1, 1, 1], [1, 1, 1, 1]], "expected": [1.0, 1.0, 1.0, 1.0]},
            {"args": [[0, 0, 0], [1, 1, 1]], "expected": [0.0, 0.0, 0.0, 0.0]},
            {"args": [[1, 0, 1, 0], [0, 0, 0, 0]], "expected": [0.5, 0.0, 0.0, 0.0]},
            {"args": [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
             "expected": [0.9, 0.0, 0.0, 0.0]},
        ],
        reference_py=(
            "import numpy as np\n"
            "\n"
            "def solution(y_true, y_pred):\n"
            "    t = np.array(y_true)\n"
            "    p = np.array(y_pred)\n"
            "    tp = int(((p == 1) & (t == 1)).sum())\n"
            "    fp = int(((p == 1) & (t == 0)).sum())\n"
            "    fn = int(((p == 0) & (t == 1)).sum())\n"
            "    tn = int(((p == 0) & (t == 0)).sum())\n"
            "    acc = (tp + tn) / len(t)\n"
            "    pr = tp / (tp + fp) if (tp + fp) else 0.0\n"
            "    rc = tp / (tp + fn) if (tp + fn) else 0.0\n"
            "    f1 = 2 * pr * rc / (pr + rc) if (pr + rc) else 0.0\n"
            "    return [round(acc, 4) + 0.0, round(pr, 4) + 0.0,\n"
            "            round(rc, 4) + 0.0, round(f1, 4) + 0.0]\n"
        ),
        template_py=(
            "import numpy as np\n"
            "\n"
            "def solution(y_true, y_pred):\n"
            "    # [정확도, 정밀도, 재현율, F1] 을 반환하세요.\n"
            "    # 분모가 0 이면 해당 지표는 0.0 입니다.\n"
            "    return []\n"
        ),
    ),

    _p(
        id="dsq3-04",
        title="지니 불순도",
        topic="의사결정나무",
        description=(
            "라벨 리스트의 지니 불순도를 구해 반환하세요.\n"
            "\n"
            "  지니 = 1 - Σ (각 클래스 비율)²\n"
            "\n"
            "  · 모두 같은 클래스면 0 (완전 순수)\n"
            "  · 클래스가 고르게 섞일수록 커진다\n"
            "\n"
            "라벨은 0 이상의 정수이고 클래스 개수는 정해져 있지 않습니다.\n"
            "빈 리스트가 들어오면 0.0 을 반환합니다.\n"
            "결과는 소수 넷째 자리까지 반올림합니다."
        ),
        input_desc="labels: 0 이상의 정수 리스트 (빈 리스트 가능)",
        output_desc="지니 불순도(float) — round(x, 4)",
        examples=[
            {"args": [[0, 0, 1, 1]], "output": 0.5},
        ],
        hints=[
            "각 클래스가 몇 번 나왔는지 세고, 전체 개수로 나눠 비율을 구합니다.",
            "collections.Counter 나 np.bincount 를 쓸 수 있습니다.\n"
            "클래스 번호가 0부터 연속이 아닐 수도 있으니 등장한 값만 세면 됩니다.\n"
            "빈 리스트를 먼저 걸러내지 않으면 0 으로 나누기가 발생합니다.",
            "from collections import Counter\n"
            "if not labels:\n"
            "    return 0.0\n"
            "n = len(labels)\n"
            "g = 1.0\n"
            "for c in Counter(labels).values():\n"
            "    g -= (c / n) ** 2\n"
            "return round(g, 4)",
        ],
        testcases=[
            {"args": [[0, 0, 1, 1]], "expected": 0.5},
            {"args": [[1, 1, 1, 1]], "expected": 0.0},
            {"args": [[0, 0, 0, 1]], "expected": 0.375},
            {"args": [[]], "expected": 0.0},
            {"args": [[0, 1, 2]], "expected": 0.6667},
            {"args": [[0, 0, 1, 1, 2, 2]], "expected": 0.6667},
        ],
        reference_py=(
            "from collections import Counter\n"
            "\n"
            "def solution(labels):\n"
            "    if not labels:\n"
            "        return 0.0\n"
            "    n = len(labels)\n"
            "    g = 1.0\n"
            "    for c in Counter(labels).values():\n"
            "        g -= (c / n) ** 2\n"
            "    return round(g, 4) + 0.0\n"
        ),
        template_py=(
            "def solution(labels):\n"
            "    # 지니 불순도를 소수 넷째 자리까지 반환하세요.\n"
            "    # 빈 리스트면 0.0 입니다.\n"
            "    return 0.0\n"
        ),
    ),

    _p(
        id="dsq3-05",
        title="k-means 한 스텝",
        topic="군집",
        description=(
            "k-means 의 '할당 → 갱신' 을 **한 번만** 수행하세요.\n"
            "\n"
            "  1) 각 점을 가장 가까운 중심에 배정한다 (유클리드 거리)\n"
            "  2) 각 군집에 속한 점들의 평균으로 중심을 옮긴다\n"
            "\n"
            "어느 점도 배정되지 않은 중심은 **그대로 둡니다**(빈 군집 처리).\n"
            "거리가 완전히 같은 경우는 입력으로 주어지지 않습니다.\n"
            "\n"
            "[배정된 군집 번호 리스트, 새 중심 리스트] 를 반환하세요.\n"
            "새 중심의 각 좌표는 소수 넷째 자리까지 반올림합니다."
        ),
        input_desc="points: [[x, y], ...], centers: [[x, y], ...]",
        output_desc="[군집번호 리스트(int), 새 중심 리스트([[x, y], ...] float)]",
        examples=[
            {"args": [[[0, 0], [1, 1], [10, 10], [11, 11]], [[0, 0], [10, 10]]],
             "output": [[0, 0, 1, 1], [[0.5, 0.5], [10.5, 10.5]]]},
        ],
        hints=[
            "각 점과 각 중심의 거리를 모두 구해야 합니다.\n"
            "거리 비교만 할 것이므로 제곱근을 씌우지 않아도 결과는 같습니다.",
            "numpy 브로드캐스팅을 쓰면 반복문 없이 거리 행렬을 만들 수 있습니다.\n"
            "  X[:, None, :] 는 (n, 1, d), C[None, :, :] 는 (1, k, d)\n"
            "  둘을 빼면 (n, k, d) 가 되고 마지막 축을 더하면 (n, k) 거리 행렬입니다.\n"
            "빈 군집을 처리하지 않으면 빈 배열의 평균이 nan 이 되어 틀립니다.",
            "import numpy as np\n"
            "X = np.array(points, dtype=float)\n"
            "C = np.array(centers, dtype=float)\n"
            "d = ((X[:, None, :] - C[None, :, :]) ** 2).sum(axis=2)\n"
            "lab = d.argmin(axis=1)\n"
            "new = []\n"
            "for j in range(len(C)):\n"
            "    m = X[lab == j].mean(axis=0) if (lab == j).any() else C[j]\n"
            "    new.append([round(float(v), 4) for v in m])\n"
            "return [lab.tolist(), new]",
        ],
        testcases=[
            {"args": [[[0, 0], [1, 1], [10, 10], [11, 11]], [[0, 0], [10, 10]]],
             "expected": [[0, 0, 1, 1], [[0.5, 0.5], [10.5, 10.5]]]},
            {"args": [[[0, 0], [2, 2]], [[0, 0], [5, 5]]],
             "expected": [[0, 0], [[1.0, 1.0], [5.0, 5.0]]]},
            {"args": [[[1, 1], [2, 2], [3, 3]], [[0, 0], [10, 10]]],
             "expected": [[0, 0, 0], [[2.0, 2.0], [10.0, 10.0]]]},
            {"args": [[[0, 0], [0, 4], [6, 0], [6, 4]], [[0, 1], [6, 3]]],
             "expected": [[0, 0, 1, 1], [[0.0, 2.0], [6.0, 2.0]]]},
        ],
        reference_py=(
            "import numpy as np\n"
            "\n"
            "def solution(points, centers):\n"
            "    X = np.array(points, dtype=float)\n"
            "    C = np.array(centers, dtype=float)\n"
            "    d = ((X[:, None, :] - C[None, :, :]) ** 2).sum(axis=2)\n"
            "    lab = d.argmin(axis=1)\n"
            "    new = []\n"
            "    for j in range(len(C)):\n"
            "        m = X[lab == j].mean(axis=0) if (lab == j).any() else C[j]\n"
            "        new.append([round(float(v), 4) + 0.0 for v in m])\n"
            "    return [[int(v) for v in lab], new]\n"
        ),
        template_py=(
            "import numpy as np\n"
            "\n"
            "def solution(points, centers):\n"
            "    # [군집번호 리스트, 새 중심 리스트] 를 반환하세요.\n"
            "    # 빈 군집의 중심은 그대로 둡니다.\n"
            "    return [[], []]\n"
        ),
    ),
]
