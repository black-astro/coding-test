"""배치 파일 1개를 검증한다.

각 문제의 reference_py 를 실제로 실행해 testcases 를 모두 통과하는지 확인하고,
id 중복/필수 필드 누락도 점검한다.

실행:
    python tools/verify_batch.py problems/batches/bronze_a.py
"""

import sys
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from engine.judge import judge as judge_problem

if len(sys.argv) < 2:
    print("사용법: python tools/verify_batch.py <배치파일경로>")
    sys.exit(2)

path = Path(sys.argv[1])
if not path.is_absolute():
    path = ROOT / path

import tempfile

spec = importlib.util.spec_from_file_location("batchmod", path)
mod = importlib.util.module_from_spec(spec)
try:
    spec.loader.exec_module(mod)
except Exception as e:
    print(f"[FAIL] {path.name} 로드 실패: {type(e).__name__}: {e}")
    sys.exit(1)

problems = getattr(mod, "PROBLEMS", [])

fail = 0
seen = set()
print(f"검증 대상: {path.name}  (문제 {len(problems)}개)")
print("-" * 64)
with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as td:
    TMP = Path(td)
    for p in problems:
        issues = []
        if p.id in seen:
            issues.append("id 중복")
        seen.add(p.id)
        if len(p.hints) < 3:
            issues.append("힌트 3개 미만")
        if not p.testcases:
            issues.append("테스트케이스 없음")
        if not p.reference_py.strip():
            issues.append("파이썬 정답 없음")
        # 자바 정답은 표준입출력형만 필수 (func 는 Python 전용 채점)
        if p.type == "stdin" and not p.reference_java.strip():
            issues.append("자바 정답 없음")

        sp = TMP / f"{p.id}.py"
        sp.write_text(p.reference_py, encoding="utf-8")
        res = judge_problem(p, sp)
        ok = res.accepted and not issues
        if not ok:
            fail += 1
        status = "OK " if ok else "FAIL"
        print(f"[{status}] {p.id:<16} {p.title:<28} {res.passed}/{res.total} {('· ' + ', '.join(issues)) if issues else ''}")
        if not res.accepted:
            fc = res.first_fail
            if fc:
                print(f"        ↳ 입력={fc.given_input!r} 기대={fc.expected!r} 실제={fc.actual!r} 에러={fc.error!r}")
            elif res.unsupported or res.compile_error:
                print(f"        ↳ {res.unsupported or res.compile_error}")

print("-" * 64)
print(f"통과 {len(problems) - fail} / {len(problems)},  실패 {fail}")
sys.exit(1 if fail else 0)
