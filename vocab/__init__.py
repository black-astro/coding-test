"""영단어 학습 — 개발자 IT 용어/은어 + 일반 영어 (기초→고급).

데이터: vocab/data/*.py 의 WORDS 리스트 자동 수집.
진행상황(암기/퀴즈)은 sqlite(vocab/progress.py)로 관리.
"""

import importlib
import pkgutil
from pathlib import Path

LEVELS = ["기초", "중급", "고급"]
CATEGORIES = ["일반", "IT"]

_DATA_MODULES = ["basic", "inter", "adv", "it_terms", "it_slang", "everyday", "backend", "extra"]

ALL = []
_dir = Path(__file__).parent / "data"
_names = []
if _dir.exists():
    _names = [i.name for i in pkgutil.iter_modules([str(_dir)])]
for _name in (_names or _DATA_MODULES):
    try:
        _m = importlib.import_module(f"vocab.data.{_name}")
    except ModuleNotFoundError:
        continue
    ALL.extend(getattr(_m, "WORDS", []))

# 중복 제거(같은 단어는 처음 것만)
_seen = set()
_uniq = []
for _w in ALL:
    key = _w.word.lower()
    if key in _seen:
        continue
    _seen.add(key)
    _uniq.append(_w)
ALL = _uniq

BY_LEVEL = {lv: [] for lv in LEVELS}
for _w in ALL:
    BY_LEVEL.setdefault(_w.level, []).append(_w)


def total() -> int:
    return len(ALL)
