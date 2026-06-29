"""유형별 실전 문제 모음 (대한민국 대기업 코딩테스트 빈출 유형).

대기업 코테에서 자주 나오는 유형을 우선순위 순서로 묶었다.
practice/categories/ 의 모든 모듈을 자동 수집해 카테고리별로 제공한다.

CATEGORIES : 유형 순서 (우선순위순)
ALL        : 카테고리명 -> Problem 리스트
BY_ID      : 문제 id -> Problem
"""

import importlib
import pkgutil
from pathlib import Path

# 대기업 코테 빈출 유형 (우선순위순)
CATEGORIES = [
    "구현/시뮬레이션",
    "DFS/BFS",
    "완전탐색/백트래킹",
    "정렬",
    "해시",
    "투포인터/누적합",
    "이분탐색",
    "그리디",
    "DP",
    "다익스트라/최단경로",
    "유니온파인드",
    "힙/우선순위큐",
    "세그먼트트리",
]

# 유형별 한 줄 설명 (CLI 표시용)
CATEGORY_DESC = {
    "구현/시뮬레이션": "지문이 길고 조건이 많은 문제를 그대로 코드로. 삼성·카카오·현대 단골",
    "DFS/BFS": "2차원 배열 탐색, 최단거리, 연결요소, 전파. 대기업 단골",
    "완전탐색/백트래킹": "입력이 작을 때 모든 경우를 탐색. 순열·조합·후보키",
    "정렬": "정렬 기준(Comparator) 잡기. 1~2번 문제로 자주",
    "해시": "중복/빈도/매핑. getOrDefault, Set",
    "투포인터/누적합": "큰 입력에서 O(N²) 못 쓸 때 구간을 움직인다",
    "이분탐색": "정답 자체를 이분탐색(파라메트릭). 입국심사·예산",
    "그리디": "정렬 기준을 잘 잡아야. 왜 최적인지 설명 가능해야",
    "DP": "점화식 세우기. 계단·삼각형·배낭·LIS",
    "다익스트라/최단경로": "가중치 그래프 최단거리. PriorityQueue 필수",
    "유니온파인드": "연결 여부·그룹 합치기. find/union",
    "힙/우선순위큐": "우선순위가 계속 바뀌는 문제. 더 맵게·스케줄링",
    "세그먼트트리": "구간 질의+갱신, 대량 쿼리. 상위권/고난도",
}

ALL = {c: [] for c in CATEGORIES}

_CATEGORY_MODULES = ["impl", "sort", "bfs", "bruteforce", "hash", "twopointer",
                     "binsearch", "greedy", "dp", "dijkstra", "union", "heap", "segtree"]

_cat_dir = Path(__file__).parent / "categories"
_names = []
if _cat_dir.exists():
    _names = [i.name for i in pkgutil.iter_modules([str(_cat_dir)])]
for _name in (_names or _CATEGORY_MODULES):
    try:
        _m = importlib.import_module(f"practice.categories.{_name}")
    except ModuleNotFoundError:
        continue
    _cat = getattr(_m, "CATEGORY", None)
    for _p in getattr(_m, "PROBLEMS", []):
        ALL.setdefault(_cat, []).append(_p)

# 카테고리·기본 제한 채우기
for _c, _plist in ALL.items():
    for _p in _plist:
        if not _p.category:
            _p.category = _c
        if _p.time_limit_ms is None:
            _p.time_limit_ms = 2000
        if _p.memory_limit_mb is None:
            _p.memory_limit_mb = 256
    _plist.sort(key=lambda p: p.id)

# C++ 정답 코드 적용 (practice/cpp/*.py 의 CPP 맵)
_cpp_dir = Path(__file__).parent / "cpp"
_CPP = {}
_cpp_names = []
if _cpp_dir.exists():
    _cpp_names = [i.name for i in pkgutil.iter_modules([str(_cpp_dir)])]
for _name in (_cpp_names or ["impl", "bfs", "bruteforce", "sort", "hash", "twopointer",
                             "binsearch", "greedy", "dp", "dijkstra", "union", "heap", "segtree"]):
    try:
        _m = importlib.import_module(f"practice.cpp.{_name}")
    except ModuleNotFoundError:
        continue
    _CPP.update(getattr(_m, "CPP", {}))
for _plist in ALL.values():
    for _p in _plist:
        if not _p.reference_cpp and _p.id in _CPP:
            _p.reference_cpp = _CPP[_p.id]

BY_ID = {p.id: p for plist in ALL.values() for p in plist}


def count(category: str) -> int:
    return len(ALL.get(category, []))


def total() -> int:
    return sum(len(v) for v in ALL.values())
