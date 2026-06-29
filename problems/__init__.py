"""모든 랭크의 문제를 한곳에 모아 제공한다.

기본 5문제(bronze.py 등) + problems/batches/ 의 모든 배치 파일을 자동 수집한다.

RANKS    : 랭크 순서 (브론즈 → 플래티넘)
ALL      : 랭크명 -> Problem 리스트 (id 기준 정렬)
BY_ID    : 문제 id -> Problem
"""

import importlib
import pkgutil
from pathlib import Path

from problems import bronze, silver, gold, platinum

RANKS = ["Bronze", "Silver", "Gold", "Platinum"]

# 한글 표기 (출력용)
RANK_KR = {
    "Bronze": "브론즈",
    "Silver": "실버",
    "Gold": "골드",
    "Platinum": "플래티넘",
}

ALL = {r: [] for r in RANKS}


def _submodules(pkgdir: Path, fallback):
    """폴더에서 모듈명을 찾되, 동결(PyInstaller) 환경이면 fallback 목록 사용."""
    names = []
    if pkgdir.exists():
        names = [i.name for i in pkgutil.iter_modules([str(pkgdir)])]
    return names or fallback


_BATCH_MODULES = ["bronze_a", "bronze_b", "bronze_c", "silver_a", "silver_b", "silver_c",
                  "gold_a", "gold_b", "gold_c", "platinum_a", "platinum_b", "platinum_c"]
_META_MODULES = ["bronze", "silver", "gold", "platinum"]

# 1) 기본 시드 문제
for _mod in (bronze, silver, gold, platinum):
    for _p in _mod.PROBLEMS:
        ALL[_p.rank].append(_p)

# 2) batches/ 폴더의 추가 문제 자동 수집
_batch_dir = Path(__file__).parent / "batches"
for _name in _submodules(_batch_dir, _BATCH_MODULES):
    try:
        _m = importlib.import_module(f"problems.batches.{_name}")
    except ModuleNotFoundError:
        continue
    for _p in getattr(_m, "PROBLEMS", []):
        ALL.setdefault(_p.rank, []).append(_p)

# 랭크별 기본 시간/메모리 제한 (문제에 값이 없으면 채움)
RANK_LIMITS = {
    "Bronze":   (1000, 128),
    "Silver":   (1500, 256),
    "Gold":     (2000, 256),
    "Platinum": (3000, 512),
}
for _r in RANKS:
    _tl, _ml = RANK_LIMITS[_r]
    for _p in ALL[_r]:
        if _p.time_limit_ms is None:
            _p.time_limit_ms = _tl
        if _p.memory_limit_mb is None:
            _p.memory_limit_mb = _ml

# 메타데이터(세부 티어 / 백준 번호) 적용
_meta_dir = Path(__file__).parent / "meta"
META = {}
for _name in _submodules(_meta_dir, _META_MODULES):
    try:
        _m = importlib.import_module(f"problems.meta.{_name}")
    except ModuleNotFoundError:
        continue
    META.update(getattr(_m, "META", {}))
for _r in RANKS:
    for _p in ALL[_r]:
        _info = META.get(_p.id)
        if _info:
            if not _p.tier:
                _p.tier = _info.get("tier", "")
            if not _p.boj:
                _p.boj = _info.get("boj", "")

# C++ 정답 코드 적용 (problems/cpp/*.py 의 CPP 맵)
_cpp_dir = Path(__file__).parent / "cpp"
CPP = {}
for _name in _submodules(_cpp_dir, ["bronze", "silver", "gold", "platinum"]):
    try:
        _m = importlib.import_module(f"problems.cpp.{_name}")
    except ModuleNotFoundError:
        continue
    CPP.update(getattr(_m, "CPP", {}))
for _r in RANKS:
    for _p in ALL[_r]:
        if not _p.reference_cpp and _p.id in CPP:
            _p.reference_cpp = CPP[_p.id]

# id 기준 정렬
for _r in RANKS:
    ALL[_r].sort(key=lambda p: p.id)

BY_ID = {p.id: p for r in RANKS for p in ALL[r]}


def count(rank: str) -> int:
    return len(ALL[rank])
