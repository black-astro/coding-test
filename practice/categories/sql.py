# -*- coding: utf-8 -*-
"""SQL 실전 문제 (sql-01 ~ sql-50) — SQLD 시험 통과 수준.

- 기초/함정(브론즈) · 집계/JOIN(실버) · 서브쿼리/윈도우(골드) 3개 은행을 합친다.
- 테스트케이스의 기대 출력(output)은 여기서 reference_sql 을 실제로 실행해 채운다.
  → 기대값과 정답 쿼리가 어긋날 수 없다(구성상 항상 일치).
- reference_sql 이 실행조차 안 되는 문제는 목록에서 제외하고 경고만 남긴다.
"""

import sys

from engine.sqlrun import run_query
from practice.sqlbank.batch_a import PROBLEMS_PART as _A
from practice.sqlbank.batch_b import PROBLEMS_PART as _B
from practice.sqlbank.batch_c import PROBLEMS_PART as _C

CATEGORY = "SQL"

PROBLEMS = []
for _p in (_A + _B + _C):
    try:
        for _tc in _p.testcases:
            _tc["output"], _ = run_query(_tc["input"], _p.reference_sql)
        # 예시 결과는 첫 테스트케이스의 실제 결과로 채움 (지문-정답 불일치 방지)
        if _p.examples and _p.testcases:
            _p.examples[0]["output"] = _p.testcases[0]["output"]
        PROBLEMS.append(_p)
    except Exception as _e:  # noqa
        print(f"[sql] {_p.id} 준비 실패로 제외: {_e}", file=sys.stderr)
