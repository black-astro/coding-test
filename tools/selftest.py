"""자체 검증 도구.

모든 문제의 '정답 코드(reference_py)' 를 풀이 파일로 넣고 채점해 본다.
모든 문제가 통과해야 정상이다. (테스트케이스/엔진의 무결성 검증용)

실행:  python tools/selftest.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import tempfile

import problems
import practice
from engine.judge import judge as judge_problem

fail = 0
total = 0
with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as td:
    TMP = Path(td)
    for rank in problems.RANKS:
        for p in problems.ALL[rank]:
            total += 1
            path = TMP / f"{p.id}.py"
            path.write_text(p.reference_py, encoding="utf-8")
            res = judge_problem(p, path)
            status = "OK " if res.accepted else "FAIL"
            if not res.accepted:
                fail += 1
            print(f"[{status}] {p.id:<14} {p.title:<28} {res.passed}/{res.total}")
            if not res.accepted:
                fc = res.first_fail
                if fc:
                    print(f"        ↳ 입력={fc.given_input!r} 기대={fc.expected!r} 실제={fc.actual!r} 에러={fc.error!r}")
                elif res.unsupported or res.compile_error:
                    print(f"        ↳ {res.unsupported or res.compile_error}")

    # SQL 문제 — 정답 쿼리(reference_sql)를 풀이로 넣어 채점 엔진 경로 전체를 검증
    for p in practice.ALL.get("SQL", []):
        total += 1
        path = TMP / f"{p.id}.sql"
        path.write_text(p.reference_sql, encoding="utf-8")
        res = judge_problem(p, path, "sql")
        status = "OK " if res.accepted else "FAIL"
        if not res.accepted:
            fail += 1
        print(f"[{status}] {p.id:<14} {p.title:<28} {res.passed}/{res.total}")
        if not res.accepted:
            fc = res.first_fail
            if fc:
                print(f"        ↳ 기대={fc.expected!r} 실제={fc.actual!r} 에러={fc.error!r}")
            elif res.unsupported or res.compile_error:
                print(f"        ↳ {res.unsupported or res.compile_error}")

print("-" * 60)
print(f"총 {total}문제 중 통과 {total - fail}, 실패 {fail}")
sys.exit(1 if fail else 0)
