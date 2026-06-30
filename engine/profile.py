"""점수 / 랭크 판독 엔진.

설계 원칙:
  - 각 문제는 티어별 '점수'를 가진다(어려울수록 큼). 총점 = 진척도(rating).
  - 사용자의 '랭크'는 양이 아니라 '수준'으로 판독한다:
    어떤 랭크로 인정받으려면 그 랭크 문제를 최소 GATE 개 이상 풀어야 한다.
    → 브론즈+실버를 모두 풀어도 골드 문제를 안 풀면 골드가 되지 않는다.
  - 랭크 안의 세부 티어(V→I)는 그 랭크 해결 비율로 정한다.

문제의 PK 는 Problem.id (예: "gold-07", "bfs-03") 이며, 진행상황(progress.json)도
이 id 집합으로 저장된다.
"""

from collections import Counter

RANK_ORDER = ["Bronze", "Silver", "Gold", "Platinum"]
RANK_KR = {"Bronze": "브론즈", "Silver": "실버", "Gold": "골드", "Platinum": "플래티넘"}
RANK_EMOJI = {"Bronze": "🥉", "Silver": "🥈", "Gold": "🥇", "Platinum": "💎"}

# 티어별 점수 (세부 티어가 있으면 우선 적용)
TIER_POINTS = {
    "B5": 5, "B4": 6, "B3": 7, "B2": 8, "B1": 10,
    "S5": 15, "S4": 18, "S3": 21, "S2": 25, "S1": 30,
    "G5": 50, "G4": 60, "G3": 72, "G2": 86, "G1": 100,
    "P5": 160, "P4": 190, "P3": 230, "P2": 280, "P1": 340,
}
# 세부 티어가 없을 때 랭크 기준 점수
RANK_BASE = {"Bronze": 7, "Silver": 21, "Gold": 72, "Platinum": 230}

# 그 랭크로 '인정'받기 위한 최소 해결 수 (양치기 방지)
GATE = {"Bronze": 1, "Silver": 5, "Gold": 5, "Platinum": 4}

# 그 랭크가 되기 위한 누적 점수 기준치
#  → 골드가 되려면 브론즈·실버에서 쌓은 점수 + 골드 점수가 함께 필요하다.
RATING_GATE = {"Bronze": 0, "Silver": 250, "Gold": 1100, "Platinum": 2800}


def problem_points(p) -> int:
    if getattr(p, "tier", "") in TIER_POINTS:
        return TIER_POINTS[p.tier]
    return RANK_BASE.get(p.rank, 10)


def compute(solved_ids: set, all_problems) -> dict:
    """solved_ids: 푼 문제 id 집합. all_problems: Problem 목록(랭크+실전 전부)."""
    total = Counter()
    solved = Counter()
    score = 0
    n_solved = 0
    max_score = 0
    for p in all_problems:
        pts = problem_points(p)
        max_score += pts
        total[p.rank] += 1
        if p.id in solved_ids:
            solved[p.rank] += 1
            score += pts
            n_solved += 1

    # 현재 랭크 = (누적 점수 기준치 통과) AND (그 랭크 최소 해결 수 통과) 한 가장 높은 랭크
    cur = None
    for rank in RANK_ORDER:
        if score >= RATING_GATE[rank] and solved[rank] >= GATE[rank]:
            cur = rank

    if cur:
        n, tot = solved[cur], (total[cur] or 1)
        band = (n / tot) * 5
        idx = min(4, int(band))                # 0..4  (적게 풀수록 5, 많이 풀수록 1)
        num = 5 - idx                          # 5..1  (B5 가장 낮고 B1 가장 높음)
        letter = cur[0]                        # B/S/G/P
        code = f"{letter}{num}"                # 예: G4
        tier_kr = f"{RANK_KR[cur]} {num}"
        emoji = RANK_EMOJI[cur]
        progress = max(0, min(100, int(round((band - idx) * 100))))   # 현재 세부티어 내 진행률
    else:
        # 아직 랭크 진입 전 — 기본값은 브론즈 5, 게이지 0%부터 시작
        code, tier_kr, emoji = "B5", f"{RANK_KR['Bronze']} 5", RANK_EMOJI["Bronze"]
        progress = min(100, int(solved["Bronze"] / max(1, GATE["Bronze"]) * 100))

    # 다음 목표 안내 (점수/문제 수 둘 다 고려)
    next_goal = None
    if cur is None:
        nxt = "Bronze"
        need_n = max(GATE[nxt] - solved[nxt], 0)
        next_goal = f"브론즈 {need_n}문제 더 풀면 랭크 시작" if need_n else "브론즈 진입 가능"
    else:
        i = RANK_ORDER.index(cur)
        if i < len(RANK_ORDER) - 1:
            nxt = RANK_ORDER[i + 1]
            need_n = max(GATE[nxt] - solved[nxt], 0)
            need_s = max(RATING_GATE[nxt] - score, 0)
            parts = []
            if need_n:
                parts.append(f"{RANK_KR[nxt]} 문제 {need_n}개")
            if need_s:
                parts.append(f"점수 {need_s}")
            next_goal = (f"{RANK_KR[nxt]} 승급까지 " + " + ".join(parts)) if parts \
                else f"{RANK_KR[nxt]} 승급 가능!"

    return {
        "score": score,
        "max_score": max_score,
        "n_solved": n_solved,
        "rank": cur,
        "code": code,            # B5~P1
        "tier_kr": tier_kr,
        "emoji": emoji,
        "progress": progress,    # 현재 세부 티어 내 진행률 0~100
        "rank_order": RANK_ORDER,
        "solved": dict(solved),
        "total": dict(total),
        "rating_gate": RATING_GATE,
        "next_goal": next_goal,
    }

