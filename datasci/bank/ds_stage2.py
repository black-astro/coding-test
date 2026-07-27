"""2단계 연습문제 — 통계 · 전처리.

pandas 를 쓰는 문제들. 반환값은 repr 로 비교되므로
Series/DataFrame 이 아니라 순수 파이썬 타입으로 변환해서 돌려줘야 한다.
"""

from engine.models import Problem

STAGE = "2. 통계 · 전처리"


def _p(**kw):
    kw.setdefault("rank", "Bronze")
    kw.setdefault("style", "데이터분석")
    kw.setdefault("type", "func")
    kw.setdefault("func_name", "solution")
    kw.setdefault("category", STAGE)
    return Problem(**kw)


PROBLEMS = [

    _p(
        id="dsq2-01",
        title="기술통계 요약",
        topic="기술통계",
        description=(
            "값 리스트를 받아 [평균, 중앙값, 표준편차] 를 반환하세요.\n"
            "\n"
            "표준편차는 **표본 표준편차**(N-1 로 나누는 방식)로 계산합니다.\n"
            "pandas 의 Series.std() 기본 동작이며, numpy 의 std() 기본값(N)과 다릅니다.\n"
            "numpy 로 풀 경우 std(ddof=1) 을 써야 합니다.\n"
            "\n"
            "입력 길이는 항상 2 이상입니다.\n"
            "세 값 모두 소수 둘째 자리까지 반올림합니다."
        ),
        input_desc="values: 숫자 리스트 (길이 2 이상)",
        output_desc="[평균, 중앙값, 표본 표준편차]. 각각 round(x, 2)",
        examples=[
            {"args": [[88, 92, 79, 95, 61]], "output": [83.0, 88.0, 13.69]},
        ],
        hints=[
            "pandas Series 로 만들면 mean(), median(), std() 를 그대로 쓸 수 있습니다.",
            "pandas 의 std() 는 기본이 표본 표준편차(ddof=1)입니다.\n"
            "numpy 로 풀려면 arr.std(ddof=1) 처럼 명시해야 같은 값이 나옵니다.",
            "import pandas as pd\n"
            "s = pd.Series(values, dtype=float)\n"
            "return [round(float(s.mean()), 2), round(float(s.median()), 2),\n"
            "        round(float(s.std()), 2)]",
        ],
        testcases=[
            {"args": [[88, 92, 79, 95, 61]], "expected": [83.0, 88.0, 13.69]},
            {"args": [[70, 70, 70, 70]], "expected": [70.0, 70.0, 0.0]},
            {"args": [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], "expected": [5.5, 5.5, 3.03]},
            {"args": [[10, 20]], "expected": [15.0, 15.0, 7.07]},
            {"args": [[3000, 3200, 3100, 3300, 50000]],
             "expected": [12520.0, 3200.0, 20952.26]},
        ],
        reference_py=(
            "import pandas as pd\n"
            "\n"
            "def solution(values):\n"
            "    s = pd.Series(values, dtype=float)\n"
            "    return [round(float(s.mean()), 2), round(float(s.median()), 2),\n"
            "            round(float(s.std()), 2)]\n"
        ),
        template_py=(
            "import pandas as pd\n"
            "\n"
            "def solution(values):\n"
            "    # [평균, 중앙값, 표본 표준편차] 를 반환하세요. (각각 소수 둘째 자리)\n"
            "    return []\n"
        ),
    ),

    _p(
        id="dsq2-02",
        title="결측치 처리",
        topic="전처리",
        description=(
            "값 리스트에 빠진 값(None)이 섞여 있습니다.\n"
            "[유효한 값의 개수, 결측을 무시한 평균, 결측을 중앙값으로 채운 뒤의 평균]\n"
            "을 반환하세요.\n"
            "\n"
            "중앙값은 결측을 제외하고 계산합니다.\n"
            "유효한 값은 항상 1개 이상 있습니다.\n"
            "평균 두 개는 소수 둘째 자리까지 반올림합니다."
        ),
        input_desc="values: 숫자와 None 이 섞인 리스트",
        output_desc="[유효 개수(int), 결측 무시 평균(float), 중앙값으로 채운 평균(float)]",
        examples=[
            {"args": [[88, None, 79, 95, None]], "output": [3, 87.33, 87.6]},
        ],
        hints=[
            "pandas Series 로 만들면 None 이 자동으로 NaN 으로 바뀝니다.\n"
            "notna() 로 유효한 값을, isna() 로 결측을 판별할 수 있습니다.",
            "mean() 은 결측을 알아서 빼고 계산합니다.\n"
            "결측을 채우려면 fillna(채울 값) 을 쓰고, 그 결과에 다시 mean() 을 합니다.",
            "import pandas as pd\n"
            "s = pd.Series(values, dtype=float)\n"
            "return [int(s.notna().sum()),\n"
            "        round(float(s.mean()), 2),\n"
            "        round(float(s.fillna(s.median()).mean()), 2)]",
        ],
        testcases=[
            {"args": [[88, None, 79, 95, None]], "expected": [3, 87.33, 87.6]},
            {"args": [[1, 2, 3]], "expected": [3, 2.0, 2.0]},
            {"args": [[None, None, 5]], "expected": [1, 5.0, 5.0]},
            {"args": [[10, None, 20, None, 30]], "expected": [3, 20.0, 20.0]},
            {"args": [[5, None, 15, 25]], "expected": [3, 15.0, 15.0]},
        ],
        reference_py=(
            "import pandas as pd\n"
            "\n"
            "def solution(values):\n"
            "    s = pd.Series(values, dtype=float)\n"
            "    return [int(s.notna().sum()),\n"
            "            round(float(s.mean()), 2),\n"
            "            round(float(s.fillna(s.median()).mean()), 2)]\n"
        ),
        template_py=(
            "import pandas as pd\n"
            "\n"
            "def solution(values):\n"
            "    # [유효 개수, 결측 무시 평균, 중앙값으로 채운 평균] 을 반환하세요.\n"
            "    return []\n"
        ),
    ),

    _p(
        id="dsq2-03",
        title="부서별 요약표",
        topic="groupby",
        description=(
            "사원 목록을 받아 부서별로 [인원수, 평균 점수] 를 담은 딕셔너리를 반환하세요.\n"
            "\n"
            "  {부서명: [인원수, 평균점수], ...}\n"
            "\n"
            "키는 부서 이름의 사전순으로 정렬합니다.\n"
            "평균 점수는 소수 둘째 자리까지 반올림합니다."
        ),
        input_desc="rows: [{'name': 문자열, 'dept': 문자열, 'score': 정수}, ...]",
        output_desc="{부서명: [인원수(int), 평균점수(float)]} — 키는 사전순",
        examples=[
            {"args": [[{"name": "kim", "dept": "sales", "score": 80},
                       {"name": "lee", "dept": "dev", "score": 90},
                       {"name": "park", "dept": "sales", "score": 70}]],
             "output": {"dev": [1, 90.0], "sales": [2, 75.0]}},
        ],
        hints=[
            "pd.DataFrame(rows) 로 표를 만든 뒤 groupby('dept') 로 묶습니다.",
            "agg(['count', 'mean']) 를 쓰면 인원수와 평균을 한 번에 구할 수 있습니다.\n"
            "groupby 결과는 기본적으로 그룹 키 순으로 정렬됩니다.",
            "import pandas as pd\n"
            "df = pd.DataFrame(rows)\n"
            "g = df.groupby('dept')['score'].agg(['count', 'mean'])\n"
            "return {k: [int(v['count']), round(float(v['mean']), 2)]\n"
            "        for k, v in g.iterrows()}",
        ],
        testcases=[
            {"args": [[{"name": "kim", "dept": "sales", "score": 80},
                       {"name": "lee", "dept": "dev", "score": 90},
                       {"name": "park", "dept": "sales", "score": 70}]],
             "expected": {"dev": [1, 90.0], "sales": [2, 75.0]}},
            {"args": [[{"name": "a", "dept": "x", "score": 100}]],
             "expected": {"x": [1, 100.0]}},
            {"args": [[{"name": "a", "dept": "dev", "score": 88},
                       {"name": "b", "dept": "dev", "score": 92},
                       {"name": "c", "dept": "dev", "score": 79},
                       {"name": "d", "dept": "sales", "score": 61}]],
             "expected": {"dev": [3, 86.33], "sales": [1, 61.0]}},
            {"args": [[{"name": "a", "dept": "b", "score": 10},
                       {"name": "b", "dept": "a", "score": 20},
                       {"name": "c", "dept": "c", "score": 30}]],
             "expected": {"a": [1, 20.0], "b": [1, 10.0], "c": [1, 30.0]}},
            {"args": [[{"name": "a", "dept": "z", "score": 70},
                       {"name": "b", "dept": "z", "score": 75},
                       {"name": "c", "dept": "y", "score": 80},
                       {"name": "d", "dept": "y", "score": 85},
                       {"name": "e", "dept": "y", "score": 90}]],
             "expected": {"y": [3, 85.0], "z": [2, 72.5]}},
        ],
        reference_py=(
            "import pandas as pd\n"
            "\n"
            "def solution(rows):\n"
            "    df = pd.DataFrame(rows)\n"
            "    g = df.groupby('dept')['score'].agg(['count', 'mean'])\n"
            "    return {str(k): [int(v['count']), round(float(v['mean']), 2)]\n"
            "            for k, v in g.iterrows()}\n"
        ),
        template_py=(
            "import pandas as pd\n"
            "\n"
            "def solution(rows):\n"
            "    # {부서명: [인원수, 평균점수]} 를 반환하세요. 키는 사전순.\n"
            "    return {}\n"
        ),
    ),

    _p(
        id="dsq2-04",
        title="IQR 이상치 제거",
        topic="이상치",
        description=(
            "IQR 규칙으로 이상치를 제거하고 [제거된 개수, 남은 값들의 평균] 을 반환하세요.\n"
            "\n"
            "  Q1 = 하위 25% 지점,  Q3 = 상위 25% 지점\n"
            "  IQR = Q3 - Q1\n"
            "  정상 범위 : Q1 - 1.5×IQR  이상  ~  Q3 + 1.5×IQR  이하\n"
            "\n"
            "사분위수는 pandas 의 quantile() 기본 방식(선형 보간)으로 계산합니다.\n"
            "경계값은 정상으로 봅니다(이상 · 이하).\n"
            "\n"
            "평균은 소수 둘째 자리까지 반올림합니다."
        ),
        input_desc="values: 숫자 리스트 (길이 1 이상)",
        output_desc="[제거된 개수(int), 남은 값의 평균(float)]",
        examples=[
            {"args": [[88, 92, 79, 95, 61, 250]], "output": [2, 88.5]},
        ],
        hints=[
            "Series.quantile(0.25) 와 quantile(0.75) 로 Q1, Q3 를 구합니다.",
            "정상 범위를 구한 뒤 불리언 마스크로 걸러냅니다.\n"
            "조건이 두 개이므로 & 로 잇고 각 조건을 괄호로 감싸야 합니다.",
            "import pandas as pd\n"
            "s = pd.Series(values, dtype=float)\n"
            "q1, q3 = s.quantile(0.25), s.quantile(0.75)\n"
            "iqr = q3 - q1\n"
            "lo, hi = q1 - 1.5 * iqr, q3 + 1.5 * iqr\n"
            "keep = s[(s >= lo) & (s <= hi)]\n"
            "return [int(len(s) - len(keep)), round(float(keep.mean()), 2)]",
        ],
        testcases=[
            {"args": [[88, 92, 79, 95, 61, 250]], "expected": [2, 88.5]},
            {"args": [[10, 12, 11, 13, 12]], "expected": [0, 11.6]},
            {"args": [[1, 2, 3, 4, 100]], "expected": [1, 2.5]},
            {"args": [[5, 5, 5, 5]], "expected": [0, 5.0]},
            {"args": [[20, 22, 21, 23, 22, 200, 19]], "expected": [1, 21.17]},
        ],
        reference_py=(
            "import pandas as pd\n"
            "\n"
            "def solution(values):\n"
            "    s = pd.Series(values, dtype=float)\n"
            "    q1, q3 = s.quantile(0.25), s.quantile(0.75)\n"
            "    iqr = q3 - q1\n"
            "    lo, hi = q1 - 1.5 * iqr, q3 + 1.5 * iqr\n"
            "    keep = s[(s >= lo) & (s <= hi)]\n"
            "    return [int(len(s) - len(keep)), round(float(keep.mean()), 2)]\n"
        ),
        template_py=(
            "import pandas as pd\n"
            "\n"
            "def solution(values):\n"
            "    # IQR 규칙으로 이상치를 제거하고\n"
            "    # [제거된 개수, 남은 값의 평균] 을 반환하세요.\n"
            "    return []\n"
        ),
    ),

    _p(
        id="dsq2-05",
        title="상관계수 구하기",
        topic="상관관계",
        description=(
            "두 리스트의 피어슨 상관계수를 구해 반환하세요.\n"
            "\n"
            "두 리스트의 길이는 항상 같고 2 이상입니다.\n"
            "결과는 소수 넷째 자리까지 반올림합니다.\n"
            "\n"
            "  +1 에 가까우면 : 같이 커진다\n"
            "   0 에 가까우면 : 직선 관계가 없다\n"
            "  -1 에 가까우면 : 하나가 커지면 다른 건 작아진다"
        ),
        input_desc="a: 숫자 리스트, b: 숫자 리스트 (길이 동일, 2 이상)",
        output_desc="피어슨 상관계수(float). round(x, 4)",
        examples=[
            {"args": [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10]], "output": 1.0},
        ],
        hints=[
            "pandas Series 에는 corr() 메서드가 있습니다. sa.corr(sb) 형태로 씁니다.",
            "numpy 로 풀려면 np.corrcoef(a, b) 가 2x2 행렬을 돌려주므로\n"
            "[0][1] 위치의 값을 꺼내야 합니다.",
            "import pandas as pd\n"
            "sa = pd.Series(a, dtype=float)\n"
            "sb = pd.Series(b, dtype=float)\n"
            "return round(float(sa.corr(sb)), 4)",
        ],
        testcases=[
            {"args": [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10]], "expected": 1.0},
            {"args": [[1, 2, 3, 4, 5], [10, 8, 6, 4, 2]], "expected": -1.0},
            {"args": [[1, 2, 3, 4, 5], [3, 1, 4, 1, 5]], "expected": 0.3536},
            {"args": [[10, 20, 30], [15, 25, 32]], "expected": 0.9948},
            {"args": [[1, 2, 3, 4, 5, 6], [1, 4, 9, 16, 25, 36]], "expected": 0.9789},
        ],
        reference_py=(
            "import pandas as pd\n"
            "\n"
            "def solution(a, b):\n"
            "    sa = pd.Series(a, dtype=float)\n"
            "    sb = pd.Series(b, dtype=float)\n"
            "    return round(float(sa.corr(sb)), 4)\n"
        ),
        template_py=(
            "import pandas as pd\n"
            "\n"
            "def solution(a, b):\n"
            "    # 두 리스트의 피어슨 상관계수를 소수 넷째 자리까지 반환하세요.\n"
            "    return 0.0\n"
        ),
    ),

    _p(
        id="dsq2-06",
        title="중복 제거 후 상위 N",
        topic="전처리 · 정렬",
        description=(
            "사원 목록에 같은 이름이 중복으로 들어 있습니다.\n"
            "이름 기준으로 중복을 제거하되 **먼저 나온 행을 남기고**,\n"
            "점수가 높은 순으로 n 명의 이름을 반환하세요.\n"
            "\n"
            "점수가 같으면 이름의 사전순으로 앞선 사람이 먼저 옵니다.\n"
            "n 이 남은 인원보다 크면 전원을 반환합니다."
        ),
        input_desc="rows: [{'name': 문자열, 'score': 정수}, ...], n: 뽑을 인원(정수)",
        output_desc="이름 문자열 리스트",
        examples=[
            {"args": [[{"name": "kim", "score": 88}, {"name": "lee", "score": 95},
                       {"name": "kim", "score": 50}], 2],
             "output": ["lee", "kim"]},
        ],
        hints=[
            "DataFrame 의 drop_duplicates(subset=['name'], keep='first') 로 중복을 제거합니다.",
            "중복을 먼저 제거한 뒤 정렬해야 합니다. 순서를 바꾸면 결과가 달라집니다.\n"
            "정렬 기준이 두 개이므로 sort_values 에 리스트로 주고\n"
            "ascending 도 리스트로 방향을 각각 정합니다.",
            "import pandas as pd\n"
            "df = pd.DataFrame(rows).drop_duplicates(subset=['name'], keep='first')\n"
            "df = df.sort_values(['score', 'name'], ascending=[False, True])\n"
            "return df['name'].head(n).tolist()",
        ],
        testcases=[
            {"args": [[{"name": "kim", "score": 88}, {"name": "lee", "score": 95},
                       {"name": "kim", "score": 50}], 2],
             "expected": ["lee", "kim"]},
            {"args": [[{"name": "a", "score": 70}, {"name": "a", "score": 90}], 1],
             "expected": ["a"]},
            {"args": [[{"name": "b", "score": 80}, {"name": "a", "score": 80},
                       {"name": "c", "score": 90}], 3],
             "expected": ["c", "a", "b"]},
            {"args": [[{"name": "x", "score": 60}], 5], "expected": ["x"]},
            {"args": [[{"name": "kim", "score": 88}, {"name": "lee", "score": 92},
                       {"name": "park", "score": 79}, {"name": "lee", "score": 99},
                       {"name": "choi", "score": 95}], 3],
             "expected": ["choi", "lee", "kim"]},
        ],
        reference_py=(
            "import pandas as pd\n"
            "\n"
            "def solution(rows, n):\n"
            "    df = pd.DataFrame(rows).drop_duplicates(subset=['name'], keep='first')\n"
            "    df = df.sort_values(['score', 'name'], ascending=[False, True])\n"
            "    return [str(x) for x in df['name'].head(n).tolist()]\n"
        ),
        template_py=(
            "import pandas as pd\n"
            "\n"
            "def solution(rows, n):\n"
            "    # 이름 중복 제거(먼저 나온 것 유지) 후\n"
            "    # 점수 내림차순 · 동점이면 이름 오름차순으로 n 명의 이름을 반환하세요.\n"
            "    return []\n"
        ),
    ),

    _p(
        id="dsq2-07",
        title="등급 분포 세기",
        topic="파생 변수",
        description=(
            "점수 리스트를 등급으로 바꾼 뒤 등급별 인원수를 반환하세요.\n"
            "\n"
            "  A : 90점 이상\n"
            "  B : 80점 이상 90점 미만\n"
            "  C : 70점 이상 80점 미만\n"
            "  D : 70점 미만\n"
            "\n"
            "반환하는 딕셔너리에는 인원이 0명인 등급도 반드시 포함하며,\n"
            "키 순서는 A, B, C, D 순입니다."
        ),
        input_desc="scores: 정수 리스트",
        output_desc="{'A': 개수, 'B': 개수, 'C': 개수, 'D': 개수} — 순서 고정, 값은 int",
        examples=[
            {"args": [[95, 88, 72, 65, 91]], "output": {"A": 2, "B": 1, "C": 1, "D": 1}},
        ],
        hints=[
            "각 점수를 등급 문자로 바꾸는 함수를 만들고 리스트 전체에 적용합니다.",
            "0명인 등급도 포함해야 하므로, 먼저 {'A':0,'B':0,'C':0,'D':0} 을 만들어 두고\n"
            "세어 나가는 방식이 안전합니다. value_counts() 만 쓰면 0명 등급이 빠집니다.",
            "def grade(s):\n"
            "    if s >= 90: return 'A'\n"
            "    if s >= 80: return 'B'\n"
            "    if s >= 70: return 'C'\n"
            "    return 'D'\n"
            "\n"
            "result = {'A': 0, 'B': 0, 'C': 0, 'D': 0}\n"
            "for s in scores:\n"
            "    result[grade(s)] += 1\n"
            "return result",
        ],
        testcases=[
            {"args": [[95, 88, 72, 65, 91]], "expected": {"A": 2, "B": 1, "C": 1, "D": 1}},
            {"args": [[100, 100]], "expected": {"A": 2, "B": 0, "C": 0, "D": 0}},
            {"args": [[]], "expected": {"A": 0, "B": 0, "C": 0, "D": 0}},
            {"args": [[90, 89, 80, 79, 70, 69]],
             "expected": {"A": 1, "B": 2, "C": 2, "D": 1}},
            {"args": [[60, 61, 62]], "expected": {"A": 0, "B": 0, "C": 0, "D": 3}},
        ],
        reference_py=(
            "def solution(scores):\n"
            "    def grade(s):\n"
            "        if s >= 90:\n"
            "            return 'A'\n"
            "        if s >= 80:\n"
            "            return 'B'\n"
            "        if s >= 70:\n"
            "            return 'C'\n"
            "        return 'D'\n"
            "\n"
            "    result = {'A': 0, 'B': 0, 'C': 0, 'D': 0}\n"
            "    for s in scores:\n"
            "        result[grade(s)] += 1\n"
            "    return result\n"
        ),
        template_py=(
            "def solution(scores):\n"
            "    # 등급(A/B/C/D)별 인원수를 반환하세요.\n"
            "    # 0명인 등급도 포함하고, 키 순서는 A, B, C, D 입니다.\n"
            "    return {}\n"
        ),
    ),

    _p(
        id="dsq2-08",
        title="두 표 합쳐 집계하기",
        topic="merge",
        description=(
            "사원 표와 부서 표를 dept_id 로 합친 뒤,\n"
            "부서 이름별 평균 점수를 반환하세요.\n"
            "\n"
            "부서 표에 없는 dept_id 를 가진 사원은 집계에서 제외합니다(inner join).\n"
            "키는 부서 이름의 사전순으로 정렬하고,\n"
            "평균은 소수 둘째 자리까지 반올림합니다."
        ),
        input_desc=(
            "emp: [{'name': 문자열, 'dept_id': 정수, 'score': 정수}, ...]\n"
            "dept: [{'dept_id': 정수, 'dept_name': 문자열}, ...]"
        ),
        output_desc="{부서이름: 평균점수} — 키는 사전순, 값은 round(x, 2)",
        examples=[
            {"args": [[{"name": "kim", "dept_id": 1, "score": 80},
                       {"name": "lee", "dept_id": 2, "score": 90},
                       {"name": "park", "dept_id": 9, "score": 100}],
                      [{"dept_id": 1, "dept_name": "sales"},
                       {"dept_id": 2, "dept_name": "dev"}]],
             "output": {"dev": 90.0, "sales": 80.0}},
        ],
        hints=[
            "pd.merge(emp_df, dept_df, on='dept_id', how='inner') 로 두 표를 합칩니다.",
            "how='inner' 는 양쪽에 모두 있는 dept_id 만 남깁니다.\n"
            "합친 뒤 dept_name 으로 groupby 해서 평균을 구하면 됩니다.",
            "import pandas as pd\n"
            "e = pd.DataFrame(emp)\n"
            "d = pd.DataFrame(dept)\n"
            "m = pd.merge(e, d, on='dept_id', how='inner')\n"
            "g = m.groupby('dept_name')['score'].mean()\n"
            "return {str(k): round(float(v), 2) for k, v in g.items()}",
        ],
        testcases=[
            {"args": [[{"name": "kim", "dept_id": 1, "score": 80},
                       {"name": "lee", "dept_id": 2, "score": 90},
                       {"name": "park", "dept_id": 9, "score": 100}],
                      [{"dept_id": 1, "dept_name": "sales"},
                       {"dept_id": 2, "dept_name": "dev"}]],
             "expected": {"dev": 90.0, "sales": 80.0}},
            {"args": [[{"name": "a", "dept_id": 1, "score": 70},
                       {"name": "b", "dept_id": 1, "score": 80}],
                      [{"dept_id": 1, "dept_name": "x"}]],
             "expected": {"x": 75.0}},
            {"args": [[{"name": "a", "dept_id": 1, "score": 88},
                       {"name": "b", "dept_id": 2, "score": 92},
                       {"name": "c", "dept_id": 1, "score": 79},
                       {"name": "d", "dept_id": 2, "score": 61}],
                      [{"dept_id": 1, "dept_name": "beta"},
                       {"dept_id": 2, "dept_name": "alpha"}]],
             "expected": {"alpha": 76.5, "beta": 83.5}},
            {"args": [[{"name": "a", "dept_id": 5, "score": 100}],
                      [{"dept_id": 1, "dept_name": "x"}]],
             "expected": {}},
            {"args": [[{"name": "a", "dept_id": 1, "score": 88},
                       {"name": "b", "dept_id": 2, "score": 92},
                       {"name": "c", "dept_id": 3, "score": 79}],
                      [{"dept_id": 1, "dept_name": "c"},
                       {"dept_id": 2, "dept_name": "b"},
                       {"dept_id": 3, "dept_name": "a"}]],
             "expected": {"a": 79.0, "b": 92.0, "c": 88.0}},
        ],
        reference_py=(
            "import pandas as pd\n"
            "\n"
            "def solution(emp, dept):\n"
            "    e = pd.DataFrame(emp)\n"
            "    d = pd.DataFrame(dept)\n"
            "    m = pd.merge(e, d, on='dept_id', how='inner')\n"
            "    if len(m) == 0:\n"
            "        return {}\n"
            "    g = m.groupby('dept_name')['score'].mean()\n"
            "    return {str(k): round(float(v), 2) for k, v in g.items()}\n"
        ),
        template_py=(
            "import pandas as pd\n"
            "\n"
            "def solution(emp, dept):\n"
            "    # 두 표를 dept_id 로 inner join 한 뒤\n"
            "    # {부서이름: 평균점수} 를 반환하세요. 키는 사전순.\n"
            "    return {}\n"
        ),
    ),
]
