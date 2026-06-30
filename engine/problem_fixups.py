"""문제 보정 — 티어 재조정(TIER_OVERRIDE) + 중복 제거(EXCLUDE).

검토(solved.ac 기준 추정)로 드러난 문제:
 - 같은 문제가 여러 배치에 다른 티어로 중복 → 골드 T4 쏠림·랭크 모순
 - 티어가 전반적으로 1단계 과대(특히 플래티넘 상당수가 실제 골드/실버)

여기서 id 한 곳만 고치면 로더가 일괄 적용한다. 티어 코드의 첫 글자(B/S/G/P)가
랭크를 결정하므로, 코드만 바꿔도 랭크가 자동으로 따라간다.
"""

RANK_OF = {"B": "Bronze", "S": "Silver", "G": "Gold", "P": "Platinum"}

# 중복으로 제거할 문제 id (각 군집에서 stdin/적정 랭크 버전을 남기고 나머지 제거)
EXCLUDE = {
    "bronze-45",    # 약수의 개수 (← bronze-24 stdin 유지)
    "gg-08",        # 네트워크 묶음 개수 (← bfs-02 유지)
    "gold-50",      # 요세푸스 (← silver-25 stdin·적정티어 유지)
    "gold-07",      # 포도주 시식 (← gd-02 유지)
    "gd-11",        # 거듭제곱 나머지 (← gi-05 유지)
    "platinum-46",  # 거듭제곱 나머지 (중복)
    "gold-04",      # LIS (← platinum-16 stdin 유지)
    "gold-08",      # 정수 삼각형 (← dp-01 유지)
    "platinum-18",  # 정수 삼각형 (중복)
    "platinum-13",  # 연속 부분합 (← gold-09 유지)
    "gold-42",      # 회의실 배정 (← greedy-04 유지)
    "gold-47",      # 최소 비용 경로 (← dijkstra-02 유지)
    "heap-03",      # 카드 합치기 (← gold-49 유지)
    "silver-24",    # 오큰수(func) (← gi-09 stdin 유지)
}

# id -> 새 티어 코드 (첫 글자가 랭크). 미지정 문제는 원래 값 유지.
TIER_OVERRIDE = {
    # --- 브론즈 → 실버 (오분류) ---
    "hash-01": "S4",         # 완주하지 못한 선수(해시)

    # --- 실버 → 브론즈 (과대) ---
    "silver-19": "B3", "silver-48": "B2", "silver-41": "B2", "silver-01": "B2",
    # --- 실버 → 골드 (과소) ---
    "gg-03": "G3", "gg-05": "G4",
    # --- 실버 내 미세 조정 ---
    "silver-16": "S3", "silver-45": "S4", "silver-50": "S4", "silver-27": "S4",

    # --- 골드 → 실버 (T4 쏠림 주범) ---
    "gold-05": "S3", "gold-06": "S3", "gold-09": "S2", "gold-19": "S3",
    "gold-21": "S2", "gold-22": "S2", "gold-29": "S2", "gold-31": "S1",
    "gold-35": "S1", "gold-45": "S4", "gold-33": "S1", "gold-02": "S1",
    "gold-23": "S1", "gold-26": "S3", "gold-27": "S3", "gold-10": "S3",
    "gold-12": "S1", "gd-10": "S1", "gd-02": "S1",
    "hash-04": "S2", "heap-01": "S5", "impl-04": "S3",
    # --- 골드 내 하향(G3→G5 등, 분산) ---
    "gold-03": "G5", "gold-13": "G5", "gold-17": "G5", "gold-44": "G5",
    "gold-40": "G5", "gold-41": "G5", "gd-06": "G5",
    "binsearch-01": "G5", "binsearch-04": "G4", "twopointer-04": "G3",
    "dijkstra-01": "G4",
    # --- 골드 상향(진짜 G1) ---
    "gi-04": "G1", "gi-06": "G1",

    # --- 플래티넘 → 실버/골드 (과대) ---
    "platinum-50": "S1", "platinum-10": "S1",
    "platinum-01": "G5", "platinum-02": "G5", "platinum-03": "G3",
    "platinum-05": "G5", "platinum-07": "G3", "platinum-09": "G1",
    "platinum-12": "G2", "platinum-16": "G2", "platinum-17": "G3",
    "platinum-19": "G3", "platinum-20": "G5", "platinum-42": "G4",
    "platinum-43": "G4", "platinum-44": "G3", "platinum-45": "G3",
    "platinum-47": "G3", "platinum-49": "G4", "bfs-05": "G3", "dijkstra-03": "G3",
    # --- 플래티넘 내 하향(P1→P4) ---
    "platinum-40": "P4", "platinum-41": "P4", "platinum-28": "P4",
}


def _retier(p):
    code = TIER_OVERRIDE.get(p.id)
    if code:
        p.tier = code
        p.rank = RANK_OF[code[0]]


def apply_to_rank_buckets(ALL):
    """problems/ 처럼 ALL 이 랭크별 dict 인 경우 — 제외 + 재티어 + 랭크별 재배치."""
    flat = [p for r in list(ALL) for p in ALL[r] if p.id not in EXCLUDE]
    for p in flat:
        _retier(p)
    for r in list(ALL):
        ALL[r] = []
    for p in flat:
        ALL.setdefault(p.rank, []).append(p)


def apply_to_category_buckets(ALL):
    """practice/ 처럼 ALL 이 카테고리별 dict 인 경우 — 제외 + 재티어(카테고리 유지)."""
    for c in list(ALL):
        ALL[c] = [p for p in ALL[c] if p.id not in EXCLUDE]
        for p in ALL[c]:
            _retier(p)
