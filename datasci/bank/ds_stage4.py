"""4단계 연습문제 — 딥러닝."""

from engine.models import Problem

STAGE = "4. 딥러닝"


def _p(**kw):
    kw.setdefault("rank", "Bronze")
    kw.setdefault("style", "데이터분석")
    kw.setdefault("type", "func")
    kw.setdefault("func_name", "solution")
    kw.setdefault("category", STAGE)
    return Problem(**kw)


PROBLEMS = [

    _p(
        id="dsq4-01",
        title="활성화 함수 3종",
        topic="활성화 함수",
        description=(
            "값 리스트를 받아 [ReLU 결과, sigmoid 결과, softmax 결과] 를 반환하세요.\n"
            "\n"
            "  ReLU(z)    = max(0, z)\n"
            "  sigmoid(z) = 1 / (1 + e^-z)\n"
            "  softmax(z) = e^z / Σe^z        (합이 1)\n"
            "\n"
            "softmax 는 오버플로를 막기 위해 최댓값을 뺀 뒤 계산하세요.\n"
            "  e^(z - max) / Σ e^(z - max)\n"
            "결과는 수학적으로 동일하지만 큰 값이 들어와도 안전합니다.\n"
            "\n"
            "모든 값은 소수 넷째 자리까지 반올림합니다."
        ),
        input_desc="z: 숫자 리스트",
        output_desc="[ReLU 리스트, sigmoid 리스트, softmax 리스트] — 각 값 round(x, 4)",
        examples=[
            {"args": [[-1, 0, 1]],
             "output": [[0.0, 0.0, 1.0], [0.2689, 0.5, 0.7311], [0.09, 0.2447, 0.6652]]},
        ],
        hints=[
            "numpy 배열로 바꾸면 세 함수 모두 한 줄로 계산됩니다.\n"
            "ReLU 는 np.maximum(0, z) 입니다. np.max 가 아닙니다.",
            "softmax 에서 최댓값을 빼는 이유는 e^1000 이 무한대가 되는 것을 막기 위함입니다.\n"
            "분자와 분모에 같은 상수를 곱하는 것과 같아 결과는 변하지 않습니다.",
            "import numpy as np\n"
            "a = np.array(z, dtype=float)\n"
            "relu = np.maximum(0, a)\n"
            "sig = 1 / (1 + np.exp(-a))\n"
            "e = np.exp(a - a.max())\n"
            "sm = e / e.sum()\n"
            "return [[round(float(v), 4) for v in arr] for arr in (relu, sig, sm)]",
        ],
        testcases=[
            {"args": [[-1, 0, 1]],
             "expected": [[0.0, 0.0, 1.0], [0.2689, 0.5, 0.7311], [0.09, 0.2447, 0.6652]]},
            {"args": [[2.0, 1.0, 0.1]],
             "expected": [[2.0, 1.0, 0.1], [0.8808, 0.7311, 0.525], [0.659, 0.2424, 0.0986]]},
            {"args": [[0, 0]], "expected": [[0.0, 0.0], [0.5, 0.5], [0.5, 0.5]]},
            {"args": [[-5, 5]], "expected": [[0.0, 5.0], [0.0067, 0.9933], [0.0, 1.0]]},
            {"args": [[1, 2, 3, 4]],
             "expected": [[1.0, 2.0, 3.0, 4.0], [0.7311, 0.8808, 0.9526, 0.982],
                          [0.0321, 0.0871, 0.2369, 0.6439]]},
            # 오버플로 방지를 빼먹으면 e^800 이 inf 가 되어 nan 이 나온다
            {"args": [[800.0, 801.0, 802.0]],
             "expected": [[800.0, 801.0, 802.0], [1.0, 1.0, 1.0],
                          [0.09, 0.2447, 0.6652]]},
        ],
        reference_py=(
            "import numpy as np\n"
            "\n"
            "def solution(z):\n"
            "    a = np.array(z, dtype=float)\n"
            "    relu = np.maximum(0, a)\n"
            "    sig = 1 / (1 + np.exp(-a))\n"
            "    e = np.exp(a - a.max())\n"
            "    sm = e / e.sum()\n"
            "    return [[round(float(v), 4) + 0.0 for v in arr]\n"
            "            for arr in (relu, sig, sm)]\n"
        ),
        template_py=(
            "import numpy as np\n"
            "\n"
            "def solution(z):\n"
            "    # [ReLU, sigmoid, softmax] 결과 리스트를 반환하세요.\n"
            "    return [[], [], []]\n"
        ),
    ),

    _p(
        id="dsq4-02",
        title="신경망 한 층 순전파",
        topic="순전파",
        description=(
            "입력 벡터 x, 가중치 행렬 W, 편향 b 를 받아\n"
            "ReLU 를 통과한 출력을 반환하세요.\n"
            "\n"
            "  z = x @ W + b\n"
            "  출력 = max(0, z)\n"
            "\n"
            "x 의 길이는 W 의 행 개수와 같고, 출력 길이는 W 의 열 개수와 같습니다.\n"
            "결과는 소수 넷째 자리까지 반올림합니다."
        ),
        input_desc="x: 숫자 리스트, W: 2차원 리스트(행=입력차원, 열=출력차원), b: 숫자 리스트",
        output_desc="ReLU 통과 후 출력 리스트 — 각 값 round(x, 4)",
        examples=[
            {"args": [[1, 2], [[1, 0], [0, 1]], [0, 0]], "output": [1.0, 2.0]},
        ],
        hints=[
            "@ 는 numpy 의 행렬곱 연산자입니다. x @ W 로 계산합니다.",
            "모양을 확인하세요. x 가 (2,), W 가 (2, 2) 면 x @ W 는 (2,) 입니다.\n"
            "순서를 바꿔 W @ x 로 쓰면 모양이 안 맞거나 다른 결과가 나옵니다.",
            "import numpy as np\n"
            "z = np.array(x, dtype=float) @ np.array(W, dtype=float) + np.array(b, dtype=float)\n"
            "return [round(float(v), 4) for v in np.maximum(0, z)]",
        ],
        testcases=[
            {"args": [[1, 2], [[1, 0], [0, 1]], [0, 0]], "expected": [1.0, 2.0]},
            {"args": [[1, 1], [[1, -1], [1, -1]], [0, 0]], "expected": [2.0, 0.0]},
            {"args": [[2, 3], [[0.5, 0.5], [0.5, -0.5]], [1, 1]], "expected": [3.5, 0.5]},
            {"args": [[0, 0], [[1, 1], [1, 1]], [-1, 2]], "expected": [0.0, 2.0]},
            {"args": [[1, 2, 3], [[1, 0], [0, 1], [1, 1]], [0.5, 0.5]],
             "expected": [4.5, 5.5]},
        ],
        reference_py=(
            "import numpy as np\n"
            "\n"
            "def solution(x, W, b):\n"
            "    z = (np.array(x, dtype=float) @ np.array(W, dtype=float)\n"
            "         + np.array(b, dtype=float))\n"
            "    return [round(float(v), 4) + 0.0 for v in np.maximum(0, z)]\n"
        ),
        template_py=(
            "import numpy as np\n"
            "\n"
            "def solution(x, W, b):\n"
            "    # z = x @ W + b 를 구하고 ReLU 를 통과시켜 반환하세요.\n"
            "    return []\n"
        ),
    ),

    _p(
        id="dsq4-03",
        title="교차엔트로피 손실",
        topic="손실 함수",
        description=(
            "각 데이터의 클래스별 확률과 정답 라벨을 받아\n"
            "평균 교차엔트로피 손실을 반환하세요.\n"
            "\n"
            "  L = 평균( -log(정답 클래스의 확률) )\n"
            "\n"
            "log(0) 이 되는 것을 막기 위해 확률을 최소 1e-12 로 잘라내고 계산하세요.\n"
            "결과는 소수 넷째 자리까지 반올림합니다."
        ),
        input_desc="probs: 2차원 리스트(행=데이터, 열=클래스별 확률), labels: 정답 클래스 번호 리스트",
        output_desc="평균 교차엔트로피(float) — round(x, 4)",
        examples=[
            {"args": [[[0.7, 0.2, 0.1], [0.1, 0.8, 0.1]], [0, 1]], "output": 0.2899},
        ],
        hints=[
            "정답 클래스의 확률만 뽑아내면 됩니다.\n"
            "원-핫 행렬을 만들 필요 없이 인덱싱으로 바로 꺼낼 수 있습니다.",
            "numpy 에서 P[np.arange(n), labels] 로 각 행의 정답 위치 값만 뽑습니다.\n"
            "np.clip(p, 1e-12, 1.0) 으로 log(0) 을 막으세요.",
            "import numpy as np\n"
            "P = np.array(probs, dtype=float)\n"
            "y = np.array(labels)\n"
            "p = np.clip(P[np.arange(len(y)), y], 1e-12, 1.0)\n"
            "return round(float(-np.log(p).mean()), 4)",
        ],
        testcases=[
            {"args": [[[0.7, 0.2, 0.1], [0.1, 0.8, 0.1]], [0, 1]], "expected": 0.2899},
            {"args": [[[1.0, 0.0]], [0]], "expected": 0.0},
            {"args": [[[0.5, 0.5], [0.5, 0.5]], [0, 1]], "expected": 0.6931},
            {"args": [[[0.1, 0.9]], [0]], "expected": 2.3026},
            {"args": [[[0.25, 0.25, 0.25, 0.25]], [2]], "expected": 1.3863},
            # clip 을 빼먹으면 log(0) = -inf 가 되어 틀린다
            {"args": [[[0.0, 1.0]], [0]], "expected": 27.631},
        ],
        reference_py=(
            "import numpy as np\n"
            "\n"
            "def solution(probs, labels):\n"
            "    P = np.array(probs, dtype=float)\n"
            "    y = np.array(labels)\n"
            "    p = np.clip(P[np.arange(len(y)), y], 1e-12, 1.0)\n"
            "    return round(float(-np.log(p).mean()), 4) + 0.0\n"
        ),
        template_py=(
            "import numpy as np\n"
            "\n"
            "def solution(probs, labels):\n"
            "    # 평균 교차엔트로피 손실을 소수 넷째 자리까지 반환하세요.\n"
            "    return 0.0\n"
        ),
    ),

    _p(
        id="dsq4-04",
        title="CNN 출력 크기와 파라미터 수",
        topic="CNN",
        description=(
            "정사각 이미지에 합성곱을 적용할 때의\n"
            "[출력 한 변의 크기, 학습 파라미터 개수] 를 반환하세요.\n"
            "\n"
            "  출력 크기 = (입력 - 커널 + 2×패딩) // 스트라이드 + 1\n"
            "\n"
            "  파라미터 = 출력채널 × (입력채널 × 커널 × 커널 + 1)\n"
            "             └ 마지막 +1 은 출력 채널마다 하나씩 있는 편향입니다\n"
            "\n"
            "두 값 모두 정수입니다."
        ),
        input_desc=(
            "size: 입력 한 변, k: 커널 크기, pad: 패딩, stride: 스트라이드,\n"
            "ch_in: 입력 채널 수, ch_out: 출력 채널 수 (모두 정수)"
        ),
        output_desc="[출력 크기(int), 파라미터 개수(int)]",
        examples=[
            {"args": [8, 3, 0, 1, 1, 1], "output": [6, 10]},
        ],
        hints=[
            "공식을 그대로 옮기면 됩니다. 나눗셈은 // (몫)을 씁니다.",
            "파라미터는 '필터 하나의 크기 × 입력채널' 에 편향 1개를 더한 뒤,\n"
            "출력 채널 수만큼 곱합니다.\n"
            "예: 3채널 입력, 5x5 커널, 16채널 출력 → 16 × (3×5×5 + 1) = 16 × 76 = 1216",
            "out = (size - k + 2 * pad) // stride + 1\n"
            "params = ch_out * (ch_in * k * k + 1)\n"
            "return [out, params]",
        ],
        testcases=[
            {"args": [8, 3, 0, 1, 1, 1], "expected": [6, 10]},
            {"args": [8, 3, 1, 1, 1, 1], "expected": [8, 10]},
            {"args": [8, 3, 0, 2, 1, 1], "expected": [3, 10]},
            {"args": [32, 5, 2, 1, 3, 16], "expected": [32, 1216]},
            {"args": [28, 3, 0, 1, 1, 32], "expected": [26, 320]},
        ],
        reference_py=(
            "def solution(size, k, pad, stride, ch_in, ch_out):\n"
            "    out = (size - k + 2 * pad) // stride + 1\n"
            "    params = ch_out * (ch_in * k * k + 1)\n"
            "    return [int(out), int(params)]\n"
        ),
        template_py=(
            "def solution(size, k, pad, stride, ch_in, ch_out):\n"
            "    # [출력 한 변 크기, 파라미터 개수] 를 반환하세요.\n"
            "    return []\n"
        ),
    ),

    _p(
        id="dsq4-05",
        title="최대 풀링",
        topic="CNN",
        description=(
            "2차원 행렬에 size×size 최대 풀링을 적용한 결과를 반환하세요.\n"
            "\n"
            "겹치지 않게(스트라이드 = size) 잘라 각 영역의 최댓값만 남깁니다.\n"
            "행·열 개수가 size 로 나눠떨어지지 않으면 **남는 부분은 버립니다.**\n"
            "\n"
            "결과의 각 값은 소수 넷째 자리까지 반올림합니다."
        ),
        input_desc="m: 2차원 숫자 리스트, size: 풀링 크기(정수)",
        output_desc="풀링 결과 2차원 리스트 — 각 값 round(x, 4)",
        examples=[
            {"args": [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 2],
             "output": [[6.0, 8.0], [14.0, 16.0]]},
        ],
        hints=[
            "출력 크기는 (행 // size, 열 // size) 입니다.",
            "각 출력 칸 (i, j) 는 원본의 [i*size:(i+1)*size, j*size:(j+1)*size] 영역에 대응합니다.\n"
            "그 영역의 최댓값을 취하면 됩니다.",
            "import numpy as np\n"
            "M = np.array(m, dtype=float)\n"
            "oh, ow = M.shape[0] // size, M.shape[1] // size\n"
            "return [[round(float(M[i*size:(i+1)*size, j*size:(j+1)*size].max()), 4)\n"
            "         for j in range(ow)] for i in range(oh)]",
        ],
        testcases=[
            {"args": [[[1, 2], [3, 4]], 2], "expected": [[4.0]]},
            {"args": [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 2],
             "expected": [[6.0, 8.0], [14.0, 16.0]]},
            {"args": [[[0, 0], [0, 0]], 2], "expected": [[0.0]]},
            {"args": [[[1, 5, 2, 6], [3, 1, 4, 2]], 2], "expected": [[5.0, 6.0]]},
            {"args": [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2], "expected": [[5.0]]},
        ],
        reference_py=(
            "import numpy as np\n"
            "\n"
            "def solution(m, size):\n"
            "    M = np.array(m, dtype=float)\n"
            "    oh, ow = M.shape[0] // size, M.shape[1] // size\n"
            "    return [[round(float(M[i * size:(i + 1) * size,\n"
            "                          j * size:(j + 1) * size].max()), 4) + 0.0\n"
            "             for j in range(ow)] for i in range(oh)]\n"
        ),
        template_py=(
            "import numpy as np\n"
            "\n"
            "def solution(m, size):\n"
            "    # size x size 최대 풀링 결과를 반환하세요.\n"
            "    # 나눠떨어지지 않는 나머지는 버립니다.\n"
            "    return []\n"
        ),
    ),
]
