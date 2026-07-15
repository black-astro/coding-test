"""실전 모의고사 — 기업 코딩테스트처럼 난이도를 섞어 출제하고 합격/불합격을 판정.

실제 기업 코테는 보통 '쉬운 것 몇 + 어려운 것 몇'을 시간 제한 안에 푼다.
랭크 + 실전 + 종목 문제(전체 풀)에서 난이도 분포에 맞춰 무작위로 뽑는다.
"""

import random
from collections import defaultdict
from engine import profile

# 시험마다 플래티넘은 1~2문제 랜덤으로 들어가고, 최소 1문제는 반드시 포함된다.
PLATINUM_RANGE = (1, 2)

# 프리셋 — dist 는 플래티넘 외 분포(플래티넘은 위 규칙으로 자동 추가).
#  pass_ratio: 출제 문제들의 총 배점 중 몇 %를 따야 합격인지.
#  난이도별 배점이 다르므로(플래티넘이 브론즈의 수십 배) 쉬운 문제 몇 개로는 합격 못 함.
PRESETS = [
    {
        "id": "entry",
        "title": "입문 세트",
        "minutes": 120,
        "dist": {"Bronze": 2, "Silver": 3, "Gold": 1},       # +플래티넘 1~2 = 6~7문제
        "pass_ratio": 0.45,
        "desc": "6~7문제 · 120분. 기초 위주 + 플래티넘 1~2문제(필수 1). 합격: 총 배점의 45% 이상.",
    },
    {
        "id": "standard",
        "title": "표준 세트",
        "minutes": 150,
        "dist": {"Silver": 2, "Gold": 3},                    # +플래티넘 1~2 = 6~7문제
        "pass_ratio": 0.55,
        "desc": "6~7문제 · 150분. 자료구조·그래프·DP·효율성 혼합. 합격: 총 배점의 55% 이상.",
    },
    {
        "id": "impl",
        "title": "구현 집중 (긴 시간)",
        "minutes": 150,
        "dist": {"Gold": 4},                                 # +플래티넘 1~2 = 5~6문제
        "pass_ratio": 0.50,
        "desc": "5~6문제 · 150분. 구현/시뮬레이션 위주의 장문제. 합격: 총 배점의 50% 이상.",
    },
    {
        "id": "hard",
        "title": "고난도 종합",
        "minutes": 180,
        "dist": {"Gold": 5},                                 # +플래티넘 1~2 = 6~7문제
        "pass_ratio": 0.50,
        "desc": "6~7문제 · 180분. 골드·플래티넘 고난도. 합격: 총 배점의 50% 이상.",
    },
    {
        "id": "full",
        "title": "실전 풀세트",
        "minutes": 240,
        "dist": {"Bronze": 2, "Silver": 3, "Gold": 3},       # +플래티넘 1~2 = 9~10문제
        "pass_ratio": 0.55,
        "desc": "9~10문제 · 240분. 쉬움~어려움 전 구간을 실제 시험처럼 길게. 합격: 총 배점의 55% 이상.",
    },
]


# 사이드바 '시험'의 단일 도전 — 기본 7문제, 플래티넘 1~2 랜덤(최소 1), 매번 랜덤 출제
CHALLENGE = {
    "id": "challenge",
    "title": "실전 코딩테스트 도전",
    "minutes": 180,
    "dist": {"Silver": 2, "Gold": 3},                  # +플래티넘 1~2 = 6~7문제
    "pass_ratio": 0.55,
    "desc": "실전형 6~7문제(플래티넘 1~2문제, 최소 1 필수) · 180분. 매번 랜덤 출제. 합격: 총 배점의 55% 이상.",
}


def get(preset_id):
    for p in PRESETS + [CHALLENGE]:
        if p["id"] == preset_id:
            return p
    return None


def count(preset) -> int:
    # 플래티넘은 1~2 랜덤이라 최대값 기준으로 표시
    return sum(preset["dist"].values()) + PLATINUM_RANGE[1]


def _weighted_sample(rng, pool, n):
    """출제율(freq) 가중치로 중복 없이 n개 뽑기."""
    pool = list(pool)
    weights = [max(1, getattr(p, "freq", 3)) for p in pool]
    out = []
    for _ in range(min(n, len(pool))):
        i = rng.choices(range(len(pool)), weights=weights, k=1)[0]
        out.append(pool.pop(i))
        weights.pop(i)
    return out


def assemble(preset, seed, all_problems):
    """난이도 분포(dist)에 맞춰 전체 풀에서 출제율 가중 무작위로 뽑고,
    플래티넘 문제를 1~2개(최소 1 필수) 랜덤으로 추가한다."""
    rng = random.Random(seed)
    by_rank = defaultdict(list)
    for p in all_problems:
        if p.type == "sql":              # SQL 은 별도 연습 유형 — 코딩 모의고사엔 제외
            continue
        by_rank[p.rank].append(p)
    chosen = []
    for rank, n in preset["dist"].items():       # dist 에는 플래티넘이 없음
        chosen.extend(_weighted_sample(rng, by_rank.get(rank, []), n))

    # 플래티넘 1~2문제 랜덤(최소 1 필수)
    lo, hi = PLATINUM_RANGE
    n_plat = rng.randint(lo, hi)
    chosen.extend(_weighted_sample(rng, by_rank.get("Platinum", []), n_plat))

    rng.shuffle(chosen)
    return chosen


def pass_score(preset, problems_in_exam) -> int:
    """합격 기준 점수 = 출제 문제들의 총 배점 × pass_ratio."""
    total = sum(profile.problem_points(p) for p in problems_in_exam)
    ratio = preset.get("pass_ratio", 0.55)
    return int(round(total * ratio))


def grade(preset, problems_in_exam, solved_ids):
    """합격/불합격 판정 — 합산 점수(난이도별 배점) 기준."""
    total_score = sum(profile.problem_points(p) for p in problems_in_exam)
    got_score = sum(profile.problem_points(p) for p in problems_in_exam if p.id in solved_ids)
    n_total = len(problems_in_exam)
    n_solved = sum(1 for p in problems_in_exam if p.id in solved_ids)
    need_score = pass_score(preset, problems_in_exam)
    passed = got_score >= need_score
    return {
        "passed": passed,
        "n_total": n_total,
        "n_solved": n_solved,
        "need_score": need_score,
        "got_score": got_score,
        "total_score": total_score,
    }
