"""문제 데이터 구조 정의.

각 문제는 Problem 객체 하나로 표현된다.
새 문제를 추가하려면 각 랭크 파일(problems/bronze.py 등)의 리스트에
Problem(...) 를 하나 더 append 하기만 하면 된다.
"""

from dataclasses import dataclass, field


@dataclass
class Problem:
    # --- 식별 정보 ---
    id: str                     # 고유 ID 예) "bronze-01"
    rank: str                   # "Bronze" | "Silver" | "Gold" | "Platinum"
    title: str                  # 문제 제목
    style: str                  # 출제 스타일 예) "백준", "프로그래머스", "대기업"
    topic: str                  # 핵심 알고리즘 주제 예) "구현", "DP", "BFS"

    # --- 채점 방식 ---
    # "stdin": 표준입력을 받아 표준출력으로 답을 내는 백준 스타일
    # "func" : 함수를 구현해서 반환값으로 답을 내는 프로그래머스 스타일
    type: str = "stdin"
    func_name: str = "solution"     # type="func" 일 때 구현해야 할 함수 이름

    # --- 문제 설명 ---
    description: str = ""
    input_desc: str = ""
    output_desc: str = ""

    # --- 예제 ---
    # stdin: [{"input": "...", "output": "..."}]
    # func : [{"args": [...], "output": ...}]
    examples: list = field(default_factory=list)

    # --- 3단계 힌트 ---
    # hints[0]=1단계(접근 방향), [1]=2단계(자료구조/알고리즘 지목),
    # [2]=3단계(거의 정답 수준의 의사코드/핵심 코드)
    hints: list = field(default_factory=list)

    # --- 채점용 테스트케이스 (예제보다 많이) ---
    # stdin: [{"input": "...", "output": "..."}]
    # func : [{"args": [...], "expected": ...}]
    testcases: list = field(default_factory=list)

    # --- 정답 코드 (학습 참고용) ---
    reference_py: str = ""
    reference_java: str = ""
    reference_cpp: str = ""
    reference_js: str = ""

    # --- 풀이 템플릿 (solutions/ 에 자동 생성될 시작 코드) ---
    template_py: str = ""

    # --- 실전 코딩테스트 제약 ---
    # None 이면 problems/__init__.py 에서 랭크별 기본값으로 채워진다.
    time_limit_ms: int | None = None      # 시간 제한(ms)
    memory_limit_mb: int | None = None    # 메모리 제한(MB)

    # --- 실제 문제 매핑(선택) ---
    boj: str = ""        # 백준 문제 번호 등 출처 (예: "11399")
    tier: str = ""       # 세부 티어 (예: "S2", "G4")

    # --- 코딩테스트 유형 분류(선택) ---
    # 예: "구현/시뮬레이션", "DFS/BFS", "그리디", "DP" ...
    category: str = ""

    # --- 출제율(시험 출제 가중치) 1~5, 클수록 자주 출제 ---
    freq: int = 3


@dataclass
class Word:
    """영단어 학습 한 항목 (개발자 은어/IT 용어 + 일반 영어)."""
    word: str
    meaning: str            # 한글 뜻
    level: str              # "기초" | "중급" | "고급"
    category: str = "일반"  # "일반" | "IT"
    pos: str = ""           # 품사 (n/v/adj/adv 등)
    example: str = ""       # 영어 예문
    example_kr: str = ""    # 예문 해석


@dataclass
class Lesson:
    """언어 문법 학습 한 꼭지 (사이드바 'lang' / 'guide' 섹션).

    카드에 설명/사용처/단점/예시를 보여주고, code 를 에디터에 띄워 직접 실행해 본다.
    """
    id: str                 # 예) "py-basic-01"
    lang: str               # "python" | "java" | "cpp" | "guide"
    level: str              # "기초" | "중급" | "고급" (guide 는 자유)
    title: str              # 예) "리스트(list)"
    summary: str = ""       # 한 줄 요약
    explanation: str = ""   # 상세 설명(여러 줄)
    code: str = ""          # 실행 가능한 예시 코드(없으면 실행 버튼 비활성)
    usage: str = ""         # 어디에/어떻게 쓰면 좋은지
    cons: str = ""          # 단점/주의점
