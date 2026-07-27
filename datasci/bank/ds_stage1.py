"""1단계 연습문제 — 데이터 기초.

전부 type="func" (Python 전용). 반환값은 repr 로 비교되므로
numpy 스칼라를 그대로 돌려주지 말고 float()/int()/list() 로 변환해야 한다.
"""

from engine.models import Problem

STAGE = "1. 데이터 기초"


def _p(**kw):
    kw.setdefault("rank", "Bronze")
    kw.setdefault("style", "데이터분석")
    kw.setdefault("type", "func")
    kw.setdefault("func_name", "solution")
    kw.setdefault("category", STAGE)
    return Problem(**kw)


PROBLEMS = [

    _p(
        id="dsq1-01",
        title="평균과 표준편차",
        topic="기술통계",
        description=(
            "점수 리스트를 받아 [평균, 표준편차] 를 반환하세요.\n"
            "\n"
            "표준편차는 모집단 표준편차(N 으로 나누는 방식)로 계산합니다.\n"
            "numpy 의 arr.std() 기본 동작과 같습니다.\n"
            "\n"
            "두 값 모두 소수 셋째 자리에서 반올림해 둘째 자리까지 남깁니다."
        ),
        input_desc="scores: 정수 리스트 (길이 1 이상)",
        output_desc="[평균, 표준편차] 형태의 실수 2개짜리 리스트. 각각 round(x, 2)",
        examples=[
            {"args": [[88, 92, 79, 95, 61]], "output": [83.0, 12.25]},
        ],
        hints=[
            "평균은 합계 ÷ 개수입니다. numpy 를 쓰면 arr.mean() 한 줄입니다.",
            "표준편차는 arr.std() 입니다. 다만 결과가 np.float64 타입이라\n"
            "그대로 반환하면 채점에서 오답 처리됩니다. float() 로 감싸세요.",
            "import numpy as np\n"
            "arr = np.array(scores)\n"
            "return [round(float(arr.mean()), 2), round(float(arr.std()), 2)]",
        ],
        testcases=[
            {"args": [[88, 92, 79, 95, 61]], "expected": [83.0, 12.25]},
            {"args": [[70, 70, 70, 70]], "expected": [70.0, 0.0]},
            {"args": [[40, 60, 80, 100]], "expected": [70.0, 22.36]},
            {"args": [[100]], "expected": [100.0, 0.0]},
            {"args": [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], "expected": [5.5, 2.87]},
        ],
        reference_py=(
            "import numpy as np\n"
            "\n"
            "def solution(scores):\n"
            "    arr = np.array(scores, dtype=float)\n"
            "    return [round(float(arr.mean()), 2), round(float(arr.std()), 2)]\n"
        ),
        template_py=(
            "import numpy as np\n"
            "\n"
            "def solution(scores):\n"
            "    # 평균과 표준편차를 구해 [평균, 표준편차] 로 반환하세요.\n"
            "    # 각각 소수 둘째 자리까지 반올림합니다.\n"
            "    return []\n"
        ),
    ),

    _p(
        id="dsq1-02",
        title="합격자 수와 합격률",
        topic="조건 필터링",
        description=(
            "점수 리스트와 기준 점수를 받아, 기준 점수 이상인 사람의\n"
            "[인원수, 합격률(%)] 를 반환하세요.\n"
            "\n"
            "합격률은 백분율로 계산하고 소수 첫째 자리까지 반올림합니다.\n"
            "  합격률 = 합격 인원 ÷ 전체 인원 × 100"
        ),
        input_desc="scores: 정수 리스트, cutoff: 기준 점수(정수)",
        output_desc="[인원수(int), 합격률(float)] — 합격률은 round(x, 1)",
        examples=[
            {"args": [[88, 92, 79, 95, 61], 80], "output": [3, 60.0]},
        ],
        hints=[
            "numpy 배열에 비교 연산을 하면 True/False 배열(마스크)이 나옵니다.",
            "마스크의 sum() 은 True 의 개수, mean() 은 True 의 비율입니다.\n"
            "비율에 100 을 곱하면 백분율이 됩니다.",
            "import numpy as np\n"
            "mask = np.array(scores) >= cutoff\n"
            "return [int(mask.sum()), round(float(mask.mean()) * 100, 1)]",
        ],
        testcases=[
            {"args": [[88, 92, 79, 95, 61], 80], "expected": [3, 60.0]},
            {"args": [[88, 92, 79, 95, 61], 100], "expected": [0, 0.0]},
            {"args": [[88, 92, 79, 95, 61], 60], "expected": [5, 100.0]},
            {"args": [[50, 60, 70], 60], "expected": [2, 66.7]},
            {"args": [[10, 20, 30, 40, 50, 60, 70], 45], "expected": [3, 42.9]},
        ],
        reference_py=(
            "import numpy as np\n"
            "\n"
            "def solution(scores, cutoff):\n"
            "    mask = np.array(scores) >= cutoff\n"
            "    return [int(mask.sum()), round(float(mask.mean()) * 100, 1)]\n"
        ),
        template_py=(
            "import numpy as np\n"
            "\n"
            "def solution(scores, cutoff):\n"
            "    # 기준 점수 이상인 인원수와 합격률(%)을 반환하세요.\n"
            "    return []\n"
        ),
    ),

    _p(
        id="dsq1-03",
        title="상위 N명 뽑기",
        topic="정렬",
        description=(
            "사람 목록에서 점수가 높은 순으로 n 명의 이름을 반환하세요.\n"
            "\n"
            "점수가 같으면 이름의 사전순(가나다·알파벳 순)으로 앞선 사람이 먼저 옵니다.\n"
            "n 이 전체 인원보다 크면 전원을 반환합니다."
        ),
        input_desc="people: [{'name': 문자열, 'score': 정수}, ...], n: 뽑을 인원(정수)",
        output_desc="이름 문자열 리스트 (점수 내림차순, 동점이면 이름 오름차순)",
        examples=[
            {"args": [[{"name": "kim", "score": 88}, {"name": "lee", "score": 95},
                       {"name": "park", "score": 95}], 2],
             "output": ["lee", "park"]},
        ],
        hints=[
            "sorted() 의 key 인자로 '무엇을 기준으로 비교할지' 지정합니다.",
            "기준이 두 개일 때는 튜플로 묶습니다. 점수는 내림차순이므로 음수를 붙이고,\n"
            "이름은 오름차순이라 그대로 둡니다: key=lambda r: (-r['score'], r['name'])",
            "ranked = sorted(people, key=lambda r: (-r['score'], r['name']))\n"
            "return [r['name'] for r in ranked[:n]]",
        ],
        testcases=[
            {"args": [[{"name": "kim", "score": 88}, {"name": "lee", "score": 95},
                       {"name": "park", "score": 95}], 2],
             "expected": ["lee", "park"]},
            {"args": [[{"name": "kim", "score": 88}, {"name": "lee", "score": 95},
                       {"name": "park", "score": 79}], 1],
             "expected": ["lee"]},
            {"args": [[{"name": "b", "score": 70}, {"name": "a", "score": 70}], 5],
             "expected": ["a", "b"]},
            {"args": [[{"name": "kim", "score": 60}], 3], "expected": ["kim"]},
            {"args": [[{"name": "c", "score": 90}, {"name": "a", "score": 90},
                       {"name": "b", "score": 95}], 3],
             "expected": ["b", "a", "c"]},
        ],
        reference_py=(
            "def solution(people, n):\n"
            "    ranked = sorted(people, key=lambda r: (-r['score'], r['name']))\n"
            "    return [r['name'] for r in ranked[:n]]\n"
        ),
        template_py=(
            "def solution(people, n):\n"
            "    # 점수 내림차순, 동점이면 이름 오름차순으로 n 명의 이름을 반환하세요.\n"
            "    return []\n"
        ),
    ),

    _p(
        id="dsq1-04",
        title="부서별 평균 점수",
        topic="그룹 집계",
        description=(
            "사원 목록을 받아 부서별 평균 점수를 딕셔너리로 반환하세요.\n"
            "\n"
            "평균은 소수 둘째 자리까지 반올림합니다.\n"
            "반환하는 딕셔너리의 키 순서는 부서 이름의 사전순으로 맞춰 주세요."
        ),
        input_desc="rows: [{'name': 문자열, 'dept': 문자열, 'score': 정수}, ...]",
        output_desc="{부서명: 평균점수} 딕셔너리. 키는 부서명 사전순, 값은 round(x, 2)",
        examples=[
            {"args": [[{"name": "kim", "dept": "sales", "score": 80},
                       {"name": "lee", "dept": "dev", "score": 90},
                       {"name": "park", "dept": "sales", "score": 70}]],
             "output": {"dev": 90.0, "sales": 75.0}},
        ],
        hints=[
            "부서별로 점수를 모아야 합니다. 딕셔너리에 리스트를 담아 누적하거나,\n"
            "합계와 인원수를 따로 세는 방법이 있습니다.",
            "d.setdefault(key, []).append(값) 을 쓰면 '없으면 빈 리스트로 시작'이 한 줄로 됩니다.\n"
            "키 순서를 맞추려면 마지막에 sorted() 로 정렬해 다시 딕셔너리를 만드세요.",
            "groups = {}\n"
            "for r in rows:\n"
            "    groups.setdefault(r['dept'], []).append(r['score'])\n"
            "return {k: round(sum(groups[k]) / len(groups[k]), 2) for k in sorted(groups)}",
        ],
        testcases=[
            {"args": [[{"name": "kim", "dept": "sales", "score": 80},
                       {"name": "lee", "dept": "dev", "score": 90},
                       {"name": "park", "dept": "sales", "score": 70}]],
             "expected": {"dev": 90.0, "sales": 75.0}},
            {"args": [[{"name": "a", "dept": "x", "score": 100}]],
             "expected": {"x": 100.0}},
            {"args": [[{"name": "a", "dept": "x", "score": 80},
                       {"name": "b", "dept": "x", "score": 90},
                       {"name": "c", "dept": "x", "score": 85}]],
             "expected": {"x": 85.0}},
            {"args": [[{"name": "a", "dept": "b", "score": 10},
                       {"name": "b", "dept": "a", "score": 20},
                       {"name": "c", "dept": "c", "score": 30}]],
             "expected": {"a": 20.0, "b": 10.0, "c": 30.0}},
            {"args": [[{"name": "a", "dept": "dev", "score": 88},
                       {"name": "b", "dept": "dev", "score": 92},
                       {"name": "c", "dept": "dev", "score": 79},
                       {"name": "d", "dept": "sales", "score": 61}]],
             "expected": {"dev": 86.33, "sales": 61.0}},
        ],
        reference_py=(
            "def solution(rows):\n"
            "    groups = {}\n"
            "    for r in rows:\n"
            "        groups.setdefault(r['dept'], []).append(r['score'])\n"
            "    return {k: round(sum(groups[k]) / len(groups[k]), 2) for k in sorted(groups)}\n"
        ),
        template_py=(
            "def solution(rows):\n"
            "    # 부서별 평균 점수를 {부서명: 평균} 으로 반환하세요.\n"
            "    # 키는 부서명 사전순, 평균은 소수 둘째 자리까지.\n"
            "    return {}\n"
        ),
    ),

    _p(
        id="dsq1-05",
        title="min-max 정규화",
        topic="스케일링",
        description=(
            "값 리스트를 0 ~ 1 사이로 정규화해 반환하세요.\n"
            "\n"
            "  정규화된 값 = (값 - 최솟값) / (최댓값 - 최솟값)\n"
            "\n"
            "모든 값이 같아서 최댓값 - 최솟값 이 0 이면 전부 0.0 을 반환합니다.\n"
            "(0 으로 나누기를 피하기 위한 규칙입니다)\n"
            "\n"
            "각 값은 소수 넷째 자리까지 반올림합니다."
        ),
        input_desc="values: 숫자 리스트 (길이 1 이상)",
        output_desc="0~1 로 정규화된 실수 리스트. 각 값은 round(x, 4)",
        examples=[
            {"args": [[10, 20, 30, 40, 50]], "output": [0.0, 0.25, 0.5, 0.75, 1.0]},
        ],
        hints=[
            "먼저 최솟값과 최댓값을 구합니다. numpy 배열이면 arr.min(), arr.max() 입니다.",
            "최댓값과 최솟값이 같은 경우를 먼저 걸러내야 0 으로 나누기를 피할 수 있습니다.\n"
            "그 경우 [0.0] * len(values) 를 반환하세요.",
            "import numpy as np\n"
            "arr = np.array(values, dtype=float)\n"
            "lo, hi = arr.min(), arr.max()\n"
            "if hi == lo:\n"
            "    return [0.0] * len(values)\n"
            "return [round(float(v), 4) for v in (arr - lo) / (hi - lo)]",
        ],
        testcases=[
            {"args": [[10, 20, 30, 40, 50]], "expected": [0.0, 0.25, 0.5, 0.75, 1.0]},
            {"args": [[5, 5, 5]], "expected": [0.0, 0.0, 0.0]},
            {"args": [[0, 100]], "expected": [0.0, 1.0]},
            {"args": [[3]], "expected": [0.0]},
            {"args": [[88, 92, 79, 95, 61]],
             "expected": [0.7941, 0.9118, 0.5294, 1.0, 0.0]},
        ],
        reference_py=(
            "import numpy as np\n"
            "\n"
            "def solution(values):\n"
            "    arr = np.array(values, dtype=float)\n"
            "    lo, hi = arr.min(), arr.max()\n"
            "    if hi == lo:\n"
            "        return [0.0] * len(values)\n"
            "    return [round(float(v), 4) for v in (arr - lo) / (hi - lo)]\n"
        ),
        template_py=(
            "import numpy as np\n"
            "\n"
            "def solution(values):\n"
            "    # 0~1 로 정규화한 리스트를 반환하세요. (소수 넷째 자리까지)\n"
            "    # 최댓값과 최솟값이 같으면 전부 0.0 입니다.\n"
            "    return []\n"
        ),
    ),

    _p(
        id="dsq1-06",
        title="성적표 과목별·개인별 평균",
        topic="2차원 배열 · axis",
        description=(
            "2차원 성적표(행=학생, 열=과목)를 받아\n"
            "[과목별 평균 리스트, 개인별 평균 리스트] 를 반환하세요.\n"
            "\n"
            "  과목별 평균 → 세로 방향(axis=0)으로 계산, 결과 개수 = 열 개수\n"
            "  개인별 평균 → 가로 방향(axis=1)으로 계산, 결과 개수 = 행 개수\n"
            "\n"
            "모든 평균은 소수 둘째 자리까지 반올림합니다."
        ),
        input_desc="table: 2차원 정수 리스트. table[i][j] 는 i번 학생의 j번 과목 점수",
        output_desc="[과목별 평균 리스트, 개인별 평균 리스트]. 각 값은 round(x, 2)",
        examples=[
            {"args": [[[80, 90, 70], [85, 95, 75], [60, 70, 65]]],
             "output": [[75.0, 85.0, 70.0], [80.0, 85.0, 65.0]]},
        ],
        hints=[
            "numpy 2차원 배열의 mean() 에 axis 를 지정하면 방향을 정할 수 있습니다.",
            "axis 는 '없어지는 축'입니다. axis=0 이면 행이 사라져 과목별 결과가,\n"
            "axis=1 이면 열이 사라져 개인별 결과가 나옵니다.\n"
            "결과를 리스트로 바꿀 때는 .tolist() 나 리스트 컴프리헨션을 씁니다.",
            "import numpy as np\n"
            "m = np.array(table, dtype=float)\n"
            "by_subject = [round(float(v), 2) for v in m.mean(axis=0)]\n"
            "by_person  = [round(float(v), 2) for v in m.mean(axis=1)]\n"
            "return [by_subject, by_person]",
        ],
        testcases=[
            {"args": [[[80, 90, 70], [85, 95, 75], [60, 70, 65]]],
             "expected": [[75.0, 85.0, 70.0], [80.0, 85.0, 65.0]]},
            {"args": [[[100, 100], [0, 0]]],
             "expected": [[50.0, 50.0], [100.0, 0.0]]},
            {"args": [[[70]]], "expected": [[70.0], [70.0]]},
            {"args": [[[1, 2, 3, 4], [5, 6, 7, 8]]],
             "expected": [[3.0, 4.0, 5.0, 6.0], [2.5, 6.5]]},
            {"args": [[[88, 92], [79, 95], [61, 73]]],
             "expected": [[76.0, 86.67], [90.0, 87.0, 67.0]]},
        ],
        reference_py=(
            "import numpy as np\n"
            "\n"
            "def solution(table):\n"
            "    m = np.array(table, dtype=float)\n"
            "    by_subject = [round(float(v), 2) for v in m.mean(axis=0)]\n"
            "    by_person = [round(float(v), 2) for v in m.mean(axis=1)]\n"
            "    return [by_subject, by_person]\n"
        ),
        template_py=(
            "import numpy as np\n"
            "\n"
            "def solution(table):\n"
            "    # [과목별 평균 리스트, 개인별 평균 리스트] 를 반환하세요.\n"
            "    return [[], []]\n"
        ),
    ),

    _p(
        id="dsq1-07",
        title="평균 vs 중앙값",
        topic="대표값",
        description=(
            "값 리스트를 받아 [평균, 중앙값, 차이] 를 반환하세요.\n"
            "\n"
            "  차이 = 평균 - 중앙값\n"
            "\n"
            "이 차이가 크면 극단값(이상치)이 평균을 끌고 갔다는 신호입니다.\n"
            "세 값 모두 소수 둘째 자리까지 반올림합니다."
        ),
        input_desc="values: 숫자 리스트 (길이 1 이상)",
        output_desc="[평균, 중앙값, 평균-중앙값]. 각각 round(x, 2)",
        examples=[
            {"args": [[3000, 3200, 3100, 3300, 50000]],
             "output": [12520.0, 3200.0, 9320.0]},
        ],
        hints=[
            "중앙값은 정렬했을 때 한가운데 값입니다. 개수가 짝수면 가운데 두 값의 평균입니다.",
            "numpy 에는 np.median() 이 있습니다. 평균은 arr.mean() 입니다.\n"
            "차이를 구할 때는 반올림하기 전 원래 값으로 빼야 오차가 없습니다.",
            "import numpy as np\n"
            "arr = np.array(values, dtype=float)\n"
            "mean = float(arr.mean())\n"
            "med = float(np.median(arr))\n"
            "return [round(mean, 2), round(med, 2), round(mean - med, 2)]",
        ],
        testcases=[
            {"args": [[3000, 3200, 3100, 3300, 50000]],
             "expected": [12520.0, 3200.0, 9320.0]},
            {"args": [[1, 2, 3, 4, 5]], "expected": [3.0, 3.0, 0.0]},
            {"args": [[1, 2, 3, 4]], "expected": [2.5, 2.5, 0.0]},
            {"args": [[10]], "expected": [10.0, 10.0, 0.0]},
            {"args": [[1, 1, 1, 1, 100]], "expected": [20.8, 1.0, 19.8]},
        ],
        reference_py=(
            "import numpy as np\n"
            "\n"
            "def solution(values):\n"
            "    arr = np.array(values, dtype=float)\n"
            "    mean = float(arr.mean())\n"
            "    med = float(np.median(arr))\n"
            "    return [round(mean, 2), round(med, 2), round(mean - med, 2)]\n"
        ),
        template_py=(
            "import numpy as np\n"
            "\n"
            "def solution(values):\n"
            "    # [평균, 중앙값, 평균-중앙값] 을 반환하세요. (각각 소수 둘째 자리)\n"
            "    return []\n"
        ),
    ),

    _p(
        id="dsq1-08",
        title="z-score 표준화",
        topic="스케일링",
        description=(
            "값 리스트를 표준화(z-score)해 반환하세요.\n"
            "\n"
            "  z = (값 - 평균) / 표준편차\n"
            "\n"
            "표준편차는 모집단 기준(N 으로 나누는 방식, numpy 의 std() 기본값)입니다.\n"
            "표준편차가 0 이면(모든 값이 같으면) 전부 0.0 을 반환합니다.\n"
            "\n"
            "각 값은 소수 넷째 자리까지 반올림합니다."
        ),
        input_desc="values: 숫자 리스트 (길이 1 이상)",
        output_desc="표준화된 실수 리스트. 각 값은 round(x, 4)",
        examples=[
            {"args": [[10, 20, 30]], "output": [-1.2247, 0.0, 1.2247]},
        ],
        hints=[
            "평균을 빼고 표준편차로 나눕니다. numpy 배열이면 브로드캐스팅으로 한 줄입니다.",
            "표준편차가 0 인 경우를 먼저 처리해야 0 으로 나누기를 피할 수 있습니다.\n"
            "결과를 반올림할 때 -0.0 이 나올 수 있으니 주의하세요.\n"
            "round(-0.00001, 4) 는 -0.0 이 되어 0.0 과 repr 이 다릅니다.",
            "import numpy as np\n"
            "arr = np.array(values, dtype=float)\n"
            "sd = arr.std()\n"
            "if sd == 0:\n"
            "    return [0.0] * len(values)\n"
            "z = (arr - arr.mean()) / sd\n"
            "return [round(float(v), 4) + 0.0 for v in z]",
        ],
        testcases=[
            {"args": [[10, 20, 30]], "expected": [-1.2247, 0.0, 1.2247]},
            {"args": [[5, 5, 5, 5]], "expected": [0.0, 0.0, 0.0, 0.0]},
            {"args": [[1, 2, 3, 4, 5]], "expected": [-1.4142, -0.7071, 0.0, 0.7071, 1.4142]},
            {"args": [[100]], "expected": [0.0]},
            {"args": [[88, 92, 79, 95, 61]],
             "expected": [0.4082, 0.7348, -0.3266, 0.9798, -1.7963]},
        ],
        reference_py=(
            "import numpy as np\n"
            "\n"
            "def solution(values):\n"
            "    arr = np.array(values, dtype=float)\n"
            "    sd = arr.std()\n"
            "    if sd == 0:\n"
            "        return [0.0] * len(values)\n"
            "    z = (arr - arr.mean()) / sd\n"
            "    return [round(float(v), 4) + 0.0 for v in z]\n"
        ),
        template_py=(
            "import numpy as np\n"
            "\n"
            "def solution(values):\n"
            "    # z-score 로 표준화한 리스트를 반환하세요. (소수 넷째 자리까지)\n"
            "    # 표준편차가 0 이면 전부 0.0 입니다.\n"
            "    return []\n"
        ),
    ),
]
