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

# 20개 티어(레벨): B5..B1, S5..S1, G5..G1, P5..P1
TIERS = [(r, n) for r in RANK_ORDER for n in (5, 4, 3, 2, 1)]

# 다음 랭크 진입 = 하위 랭크 경험치의 이만큼을 모았을 때(게임식 누적 곡선).
#  → 플래티넘 진입은 브론즈·실버·골드를 두루 풀어야만 도달 가능.
COMPLETE = 0.80

# 한 랭크 안에서 세부 티어(5→1) 진입 지점(누적 비율) — 위로 갈수록 가팔라짐(볼록)
SUB_TIER = [0.0, 0.18, 0.40, 0.64, 0.86]   # 티어 5,4,3,2,1


def problem_points(p) -> int:
    """문제 1개의 경험치 — 난이도(티어)별로 크게 다름(브론즈 ≪ 골드 ≪ 플래티넘)."""
    if getattr(p, "tier", "") in TIER_POINTS:
        return TIER_POINTS[p.tier]
    return RANK_BASE.get(p.rank, 10)


def compute(solved_ids: set, all_problems) -> dict:
    """경험치(XP) 기반 랭크/티어 산정.

    - XP = 푼 문제들의 경험치 합(난이도별 차등).
    - 다음 랭크 진입 임계값 = 하위 랭크 XP 누적의 COMPLETE 비율 → 위로 갈수록 누적이 커짐(게임식).
    - 결과의 rank_index 까지의 랭크 문제만 풀 수 있다(상위 랭크는 잠김).
    """
    total = Counter()
    solved = Counter()
    rxp_total = Counter()      # 랭크별 총 XP
    score = 0
    n_solved = 0
    for p in all_problems:
        pts = problem_points(p)
        total[p.rank] += 1
        rxp_total[p.rank] += pts
        if p.id in solved_ids:
            solved[p.rank] += 1
            score += pts
            n_solved += 1
    max_score = sum(rxp_total.values())

    # 각 랭크 진입에 필요한 누적 XP
    entry = {}
    cum = 0
    for r in RANK_ORDER:
        entry[r] = round(cum * COMPLETE)
        cum += rxp_total[r]

    # 현재 랭크 = 누적 XP 가 진입 임계값을 넘은 가장 높은 랭크
    # (문제 목록이 비어 총 XP 가 0이면 Bronze 고정 — 전 랭크 임계값 0 오판 방지)
    cur_idx = 0
    if max_score > 0:
        for i, r in enumerate(RANK_ORDER):
            if score >= entry[r]:
                cur_idx = i
    cur = RANK_ORDER[cur_idx]

    # 현재 랭크 안에서 세부 티어(5→1)
    lo = entry[cur]
    hi = entry[RANK_ORDER[cur_idx + 1]] if cur_idx + 1 < len(RANK_ORDER) else max(max_score, lo + 1)
    frac = 0.0 if hi <= lo else min(1.0, max(0.0, (score - lo) / (hi - lo)))
    sidx = max(0, min(4, sum(1 for t in SUB_TIER if frac >= t) - 1))   # 0..4
    num = 5 - sidx
    cur_t = SUB_TIER[sidx]
    nxt_t = SUB_TIER[sidx + 1] if sidx + 1 < 5 else 1.0
    progress = 100 if nxt_t <= cur_t else int(round((frac - cur_t) / (nxt_t - cur_t) * 100))
    progress = max(0, min(100, progress))

    code = f"{cur[0]}{num}"
    tier_kr = f"{RANK_KR[cur]} {num}"
    emoji = RANK_EMOJI[cur]

    # 다음 목표
    if num == 1 and cur_idx < len(RANK_ORDER) - 1:
        nxt = RANK_ORDER[cur_idx + 1]
        need = max(0, entry[nxt] - score)
        next_goal = f"{RANK_KR[nxt]} 승급(해금)까지 경험치 {need}"
    elif num == 1:
        next_goal = "최고 티어 달성! (P1)"
    else:
        need_xp = max(0, round(lo + nxt_t * (hi - lo) - score))
        next_goal = f"다음 티어({cur[0]}{num - 1})까지 경험치 {need_xp}"

    return {
        "score": score,
        "max_score": max_score,
        "n_solved": n_solved,
        "rank": cur,
        "rank_index": cur_idx,   # 0..3 — 이 랭크까지 문제 풀 수 있음(상위는 잠김)
        "code": code,            # B5~P1
        "tier_kr": tier_kr,
        "emoji": emoji,
        "progress": progress,    # 현재 세부 티어 내 진행률 0~100
        "rank_order": RANK_ORDER,
        "solved": dict(solved),
        "total": dict(total),
        "next_goal": next_goal,
    }

