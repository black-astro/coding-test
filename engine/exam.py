"""실전 모의고사 — 기업 코딩테스트처럼 난이도를 섞어 출제하고 합격/불합격을 판정.

실제 기업 코테는 보통 '쉬운 것 몇 + 어려운 것 몇'을 시간 제한 안에 푼다.
랭크 + 실전 + 종목 문제(전체 풀)에서 난이도 분포에 맞춰 무작위로 뽑는다.
"""

import random
from collections import defaultdict
from engine import profile

# 실제 기업 코테 패턴을 본뜬 프리셋
PRESETS = [
    {
        "id": "general",
        "title": "대기업 종합형 (네이버·카카오·라인)",
        "minutes": 90,
        "dist": {"Silver": 2, "Gold": 2, "Platinum": 1},   # 총 5문제
        "pass_solve": 3,
        "desc": "5문제 · 90분. 자료구조·그래프·DP·효율성 혼합. 3문제 이상 정답이면 합격권.",
    },
    {
        "id": "samsung",
        "title": "삼성 SW역량형 (구현·시뮬)",
        "minutes": 120,
        "dist": {"Gold": 1, "Platinum": 1},                # 총 2문제
        "pass_solve": 1,
        "desc": "2문제 · 120분. 구현/시뮬레이션 위주. 1문제만 완벽히 풀어도 통과권.",
    },
    {
        "id": "entry",
        "title": "실무 기본형 (스타트업·중견)",
        "minutes": 60,
        "dist": {"Bronze": 1, "Silver": 2},                # 총 3문제
        "pass_solve": 2,
        "desc": "3문제 · 60분. 기초 구현·자료구조. 2문제 이상이면 합격.",
    },
    {
        "id": "hard",
        "title": "고난도 종합 (상위권/금융권)",
        "minutes": 150,
        "dist": {"Gold": 2, "Platinum": 2},                # 총 4문제
        "pass_solve": 2,
        "desc": "4문제 · 150분. 골드·플래티넘 고난도. 2문제 이상이면 합격.",
    },
    {
        "id": "full",
        "title": "랜덤 풀세트 (랭크 전구간)",
        "minutes": 120,
        "dist": {"Bronze": 1, "Silver": 1, "Gold": 1, "Platinum": 1},
        "pass_solve": 3,
        "desc": "4문제 · 120분. 브론즈~플래티넘 한 문제씩. 3문제 이상이면 합격.",
    },
]


def get(preset_id):
    for p in PRESETS:
        if p["id"] == preset_id:
            return p
    return None


def count(preset) -> int:
    return sum(preset["dist"].values())


def assemble(preset, seed, all_problems):
    """난이도 분포에 맞춰 전체 풀에서 무작위로 문제를 뽑는다."""
    rng = random.Random(seed)
    by_rank = defaultdict(list)
    for p in all_problems:
        by_rank[p.rank].append(p)
    chosen = []
    for rank, n in preset["dist"].items():
        pool = list(by_rank.get(rank, []))
        rng.shuffle(pool)
        chosen.extend(pool[:n])
    rng.shuffle(chosen)
    return chosen


def grade(preset, problems_in_exam, solved_ids):
    """합격/불합격 판정 + 점수 산출."""
    total_score = sum(profile.problem_points(p) for p in problems_in_exam)
    got_score = sum(profile.problem_points(p) for p in problems_in_exam if p.id in solved_ids)
    n_total = len(problems_in_exam)
    n_solved = sum(1 for p in problems_in_exam if p.id in solved_ids)
    passed = n_solved >= preset["pass_solve"]
    return {
        "passed": passed,
        "n_total": n_total,
        "n_solved": n_solved,
        "need": preset["pass_solve"],
        "got_score": got_score,
        "total_score": total_score,
    }
