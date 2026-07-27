"""데이터분석 · AI 학습 트랙 (Python 전용).

파이썬 초보 → 데이터 다루기 → 통계/전처리 → 머신러닝 → 딥러닝 → LLM 까지
단계별로 이어지는 학습 트랙이다. 코딩테스트 트랙(problems/·practice/)과는
점수·랭크·시험이 섞이지 않도록 완전히 분리해서 관리한다.

STAGES        : 단계 순서 (1 → 5)
STAGE_DESC    : 단계별 한 줄 설명
LESSONS       : 단계명 -> Lesson 리스트   (읽고 Run 으로 실행해 보는 개념 강의)
PROBLEMS      : 단계명 -> Problem 리스트  (직접 풀고 채점받는 연습문제)
LESSON_BY_ID  : id -> Lesson
BY_ID         : id -> Problem

콘텐츠 추가 방법
  · 레슨 : datasci/content/*.py 에
           LESSONS = [Lesson(lang="datasci", level=<단계명>, ...)]
  · 문제 : datasci/bank/*.py 에
           PROBLEMS = [Problem(type="func", category=<단계명>, ...)]
  두 폴더 모두 자동 수집되므로 파일만 추가하면 메뉴에 바로 반영된다.
"""

import sys
import importlib
import pkgutil
from pathlib import Path


def _warn(msg):
    print(f"[datasci] 경고: {msg}", file=sys.stderr)


# ───────────────────────── 단계 정의 ─────────────────────────

STAGES = [
    "1. 데이터 기초",
    "2. 통계 · 전처리",
    "3. 머신러닝",
    "4. 딥러닝",
    "5. LLM · 트랜스포머",
]

STAGE_DESC = {
    "1. 데이터 기초": "리스트·딕셔너리로 데이터 다루기 → numpy 배열. 모든 분석의 출발점",
    "2. 통계 · 전처리": "pandas DataFrame, 결측치·이상치, 평균/분산/상관. 실무에서 가장 오래 붙잡는 단계",
    "3. 머신러닝": "회귀·분류·군집을 numpy 로 직접 구현하며 원리 이해",
    "4. 딥러닝": "퍼셉트론 → 역전파 → 신경망. 수식이 코드로 어떻게 바뀌는지",
    "5. LLM · 트랜스포머": "토크나이저·임베딩·어텐션. GPT 가 문장을 만드는 원리",
}

# 단계별 학습 목표(사이드바/가이드 표시용)
STAGE_GOAL = {
    "1. 데이터 기초": "숫자 묶음을 자유롭게 만들고 · 걸러내고 · 요약할 수 있다",
    "2. 통계 · 전처리": "표(表) 형태의 실제 데이터를 씻어내고 요약해 인사이트를 뽑을 수 있다",
    "3. 머신러닝": "데이터로 규칙을 '학습'한다는 게 무슨 뜻인지 코드로 설명할 수 있다",
    "4. 딥러닝": "신경망이 오차를 줄여가는 과정을 직접 구현할 수 있다",
    "5. LLM · 트랜스포머": "GPT 계열 모델의 핵심 부품을 하나씩 짚어 설명할 수 있다",
}


# ───────────────────────── 의존 라이브러리 확인 ─────────────────────────

def missing_deps() -> list:
    """이 트랙에 필요한데 아직 설치되지 않은 패키지 목록."""
    miss = []
    for name in ("numpy", "pandas"):
        try:
            importlib.import_module(name)
        except ImportError:
            miss.append(name)
    return miss


def deps_ready() -> bool:
    return not missing_deps()


# ───────────────────────── 콘텐츠 자동 수집 ─────────────────────────

LESSONS = {s: [] for s in STAGES}
PROBLEMS = {s: [] for s in STAGES}

# 동결(PyInstaller) 환경에서 pkgutil 이 비는 경우를 대비한 fallback 목록
_CONTENT_MODULES = ["stage1_basic", "stage2_pandas",
                    "stage3_ml", "stage3_ml_b",
                    "stage4_dl", "stage4_dl_b",
                    "stage5_llm", "stage5_llm_b"]
_BANK_MODULES = ["ds_stage1", "ds_stage2", "ds_stage3",
                 "ds_stage4", "ds_stage5"]


def _collect(pkg: str, fallback: list, attr: str):
    """datasci/<pkg>/ 의 모든 모듈에서 <attr> 리스트를 모아 반환."""
    out = []
    d = Path(__file__).parent / pkg
    names = []
    if d.exists():
        names = [i.name for i in pkgutil.iter_modules([str(d)])]
    for name in (names or fallback):
        try:
            m = importlib.import_module(f"datasci.{pkg}.{name}")
        except ModuleNotFoundError as e:
            _warn(f"모듈 '{pkg}/{name}' 를 건너뜁니다 — {e}")
            continue
        out.extend(getattr(m, attr, []))
    return out


for _les in _collect("content", _CONTENT_MODULES, "LESSONS"):
    if _les.level in LESSONS:
        LESSONS[_les.level].append(_les)
    else:
        _warn(f"레슨 '{_les.id}' 의 단계 '{_les.level}' 가 STAGES 에 없습니다 — 건너뜁니다.")

for _p in _collect("bank", _BANK_MODULES, "PROBLEMS"):
    if _p.category in PROBLEMS:
        PROBLEMS[_p.category].append(_p)
    else:
        _warn(f"문제 '{_p.id}' 의 단계 '{_p.category}' 가 STAGES 에 없습니다 — 건너뜁니다.")

# id 순 정렬 + 중복 id 제거
for _bucket in (LESSONS, PROBLEMS):
    for _s in STAGES:
        _seen, _uniq = set(), []
        for _x in sorted(_bucket[_s], key=lambda i: i.id):
            if _x.id in _seen:
                _warn(f"중복 id '{_x.id}' — 나중 정의를 무시합니다.")
                continue
            _seen.add(_x.id)
            _uniq.append(_x)
        _bucket[_s] = _uniq

# 문제 기본값 — 데이터분석 문제는 Python 전용(func)이며
# numpy/pandas import 오버헤드(실측 pandas ≈ 1.9초 / 68MB)를 감안해 제한을 넉넉히 준다.
for _s in STAGES:
    for _p in PROBLEMS[_s]:
        if _p.time_limit_ms is None:
            _p.time_limit_ms = 5000
        if _p.memory_limit_mb is None:
            _p.memory_limit_mb = 512

LESSON_BY_ID = {les.id: les for s in STAGES for les in LESSONS[s]}
BY_ID = {p.id: p for s in STAGES for p in PROBLEMS[s]}
ALL_PROBLEMS = [p for s in STAGES for p in PROBLEMS[s]]


def lesson_count(stage: str = "") -> int:
    if stage:
        return len(LESSONS.get(stage, []))
    return len(LESSON_BY_ID)


def problem_count(stage: str = "") -> int:
    if stage:
        return len(PROBLEMS.get(stage, []))
    return len(BY_ID)


def total() -> int:
    return lesson_count() + problem_count()
