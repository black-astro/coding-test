"""언어별 문법 학습 (Python / Java / C++ · 기초·중급·고급) + 환경 가이드.

ALL    : {lang: {level: [Lesson]}}  (python/java/cpp)
GUIDES : [Lesson]                    (환경 설정 안내)
BY_ID  : id -> Lesson
"""

import importlib
import pkgutil
from pathlib import Path

LANGS = ["python", "java", "cpp", "javascript", "css", "scss"]
LANG_KR = {"python": "Python", "java": "Java", "cpp": "C++",
           "javascript": "JavaScript", "css": "CSS", "scss": "SCSS"}
LEVELS = ["기초", "중급", "고급"]

# content/ 폴더의 모듈 (동결 환경 대비 fallback)
_CONTENT_MODULES = [
    "guide",
    "py_basic", "py_mid", "py_adv",
    "java_basic", "java_mid", "java_adv",
    "cpp_basic", "cpp_mid", "cpp_adv",
    "js_lessons", "css_lessons", "scss_lessons",
    "js_lessons2", "css_lessons2", "scss_lessons2",
]

ALL = {lang: {lv: [] for lv in LEVELS} for lang in LANGS}
GUIDES = []

_dir = Path(__file__).parent / "content"
_names = []
if _dir.exists():
    _names = [i.name for i in pkgutil.iter_modules([str(_dir)])]
for _name in (_names or _CONTENT_MODULES):
    try:
        _m = importlib.import_module(f"lessons.content.{_name}")
    except ModuleNotFoundError:
        continue
    for _l in getattr(_m, "LESSONS", []):
        if _l.lang == "guide":
            GUIDES.append(_l)
        elif _l.lang in ALL:
            ALL[_l.lang].setdefault(_l.level, []).append(_l)

# id 정렬
for lang in LANGS:
    for lv in LEVELS:
        ALL[lang][lv].sort(key=lambda x: x.id)

BY_ID = {}
for lang in LANGS:
    for lv in LEVELS:
        for _l in ALL[lang][lv]:
            BY_ID[_l.id] = _l
for _l in GUIDES:
    BY_ID[_l.id] = _l


def total() -> int:
    return len(BY_ID)
