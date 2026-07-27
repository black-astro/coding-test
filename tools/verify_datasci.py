"""데이터분석 트랙 검증 도구.

1) 모든 레슨의 예시 코드(code)를 실제로 실행해 에러가 없는지 확인한다.
2) 모든 연습문제의 정답 코드(reference_py)를 채점 엔진에 넣어 전부 통과하는지 확인한다.
   (func 형 문제는 반환값 repr 비교이므로, numpy 스칼라를 그대로 반환하면 여기서 걸린다)

실행:  python tools/verify_datasci.py
      python tools/verify_datasci.py --lessons   (레슨만)
      python tools/verify_datasci.py --problems  (문제만)
"""

import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import datasci
from engine.runner import run_process, python_cmd
from engine.judge import judge as judge_problem

ONLY = sys.argv[1] if len(sys.argv) > 1 else ""


def check_lessons(tmp: Path) -> int:
    fail = 0
    total = 0
    print("=" * 70)
    print("레슨 예시 코드 실행 검증")
    print("=" * 70)
    for stage in datasci.STAGES:
        lst = datasci.LESSONS[stage]
        if not lst:
            continue
        print(f"\n[{stage}] {len(lst)}개")
        for les in lst:
            if not les.code.strip():
                print(f"  [SKIP] {les.id:<20} (예시 코드 없음)")
                continue
            total += 1
            path = tmp / f"{les.id}.py"
            path.write_text(les.code, encoding="utf-8")
            run = run_process(python_cmd(path), "", 60.0)
            ok = (run.returncode == 0 and not run.timed_out)
            print(f"  [{'OK ' if ok else 'FAIL'}] {les.id:<20} {les.title:<28} {run.time_ms:6.0f}ms")
            if not ok:
                fail += 1
                tail = run.stderr.strip().splitlines()
                for ln in tail[-4:]:
                    print(f"         ↳ {ln}")
    print(f"\n레슨: {total - fail}/{total} 통과")
    return fail


def check_problems(tmp: Path) -> int:
    fail = 0
    total = 0
    print("\n" + "=" * 70)
    print("연습문제 정답 코드 채점 검증")
    print("=" * 70)
    for stage in datasci.STAGES:
        lst = datasci.PROBLEMS[stage]
        if not lst:
            continue
        print(f"\n[{stage}] {len(lst)}개")
        for p in lst:
            total += 1
            path = tmp / f"{p.id}.py"
            path.write_text(p.reference_py, encoding="utf-8")
            res = judge_problem(p, path)
            ok = res.accepted
            if not ok:
                fail += 1
            print(f"  [{'OK ' if ok else 'FAIL'}] {p.id:<14} {p.title:<30} "
                  f"{res.passed}/{res.total}  {res.max_time_ms:6.0f}ms")
            if not ok:
                fc = res.first_fail
                if fc:
                    print(f"         ↳ 입력={fc.given_input!r}")
                    print(f"           기대={fc.expected!r}")
                    print(f"           실제={fc.actual!r}  {fc.error}")
                elif res.unsupported or res.compile_error:
                    print(f"         ↳ {res.unsupported or res.compile_error}")
    print(f"\n문제: {total - fail}/{total} 통과")
    return fail


def main():
    miss = datasci.missing_deps()
    if miss:
        print(f"[경고] 다음 패키지가 없습니다: {', '.join(miss)}")
        print("       python -m pip install " + " ".join(miss))
        return 1

    fail = 0
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as td:
        tmp = Path(td)
        if ONLY != "--problems":
            fail += check_lessons(tmp)
        if ONLY != "--lessons":
            fail += check_problems(tmp)

    print("\n" + "=" * 70)
    if fail:
        print(f"❌ 실패 {fail}건")
        return 1
    print(f"✅ 전부 통과 — 레슨 {datasci.lesson_count()}개 · 문제 {datasci.problem_count()}개")
    return 0


if __name__ == "__main__":
    sys.exit(main())
