"""유형/랭크 커버리지 요약.

실행: python tools/coverage.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import problems
import practice

print("=" * 56)
print(" 랭크별 문제 수")
print("=" * 56)
for r in problems.RANKS:
    print(f"  {problems.RANK_KR[r]:<6} ({r:<8}) : {len(problems.ALL[r])}문제")
print(f"  {'합계':<6}            : {sum(len(problems.ALL[r]) for r in problems.RANKS)}문제")

print("\n" + "=" * 56)
print(" 유형별 실전 문제 수 (practice)")
print("=" * 56)
for c in practice.CATEGORIES:
    n = practice.count(c)
    bar = "■" * n
    print(f"  {c:<16} : {n:>2}문제  {bar}")
print(f"  {'합계':<16} : {practice.total():>2}문제")
