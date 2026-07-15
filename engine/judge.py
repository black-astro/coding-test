"""채점 엔진 — 정답/오답 + 시간·메모리 판정 (Python / Java / C++).

판정(verdict):
    AC  정답
    WA  오답 (출력 불일치)
    TLE 시간 초과
    MLE 메모리 초과
    RE  런타임 에러
    CE  컴파일 에러

- 표준입출력형(stdin) 문제: python/java/cpp 모두 채점.
- 함수 구현형(func) 문제: python 만 채점(하니스 사용). java/cpp 는 정답 코드 참고용.
"""

import json
import tempfile
from pathlib import Path
from dataclasses import dataclass, field

from engine import runner
from engine.runner import run_process, compile_solution, FUNC_HARNESS, python_exe, func_cmd

import sys

VERDICT_KR = {
    "AC": "정답",
    "WA": "오답",
    "TLE": "시간 초과",
    "MLE": "메모리 초과",
    "RE": "런타임 에러",
    "CE": "컴파일 에러",
}


@dataclass
class CaseResult:
    index: int
    verdict: str            # AC/WA/TLE/MLE/RE
    given_input: str
    expected: str
    actual: str
    time_ms: float = 0.0
    peak_mem_kb: int | None = None
    error: str = ""

    @property
    def passed(self) -> bool:
        return self.verdict == "AC"


@dataclass
class JudgeResult:
    total: int
    passed: int
    cases: list
    accepted: bool
    lang: str = "python"
    compile_error: str = ""
    max_time_ms: float = 0.0
    max_mem_kb: int | None = None
    unsupported: str = ""    # 채점 불가 사유(있으면)

    @property
    def first_fail(self):
        for c in self.cases:
            if not c.passed:
                return c
        return None


def _normalize(text: str) -> str:
    lines = [ln.rstrip() for ln in str(text).replace("\r\n", "\n").split("\n")]
    while lines and lines[-1] == "":
        lines.pop()
    return "\n".join(lines)


# 언어별 제한 배수 — 문제 고유 제한(문제별)에 곱해 실제 적용 제한(언어별)을 구한다.
#  C++ 은 1.0(가장 빡빡), 인터프리터/VM 언어는 런타임 특성만큼만 더 준다.
#  실제 온라인 저지가 언어별로 시간/메모리를 차등 적용하는 것과 같은 취지로, 빡빡하게 유지.
LANG_TIME_MULT = {"python": 3.0, "java": 2.0, "cpp": 1.0, "javascript": 2.0}
LANG_MEM_MULT  = {"python": 1.5, "java": 2.0, "cpp": 1.0, "javascript": 1.5}


def effective_limits(problem, lang: str = "python"):
    """문제별 기본 제한 × 언어별 배수 = 실제 적용 (시간 ms, 메모리 MB)."""
    tl = problem.time_limit_ms or 2000
    ml = problem.memory_limit_mb or 256
    return (int(round(tl * LANG_TIME_MULT.get(lang, 1.0))),
            int(round(ml * LANG_MEM_MULT.get(lang, 1.0))))


def _limits(problem, lang: str = "python"):
    return effective_limits(problem, lang)


def _verdict_for(run, expected_norm, actual_norm, tl_ms, ml_mb):
    """단일 실행 결과에 대한 판정."""
    if getattr(run, "mem_exceeded", False):
        return "MLE"            # 실행 중 메모리 한도 초과로 강제 종료됨
    if run.timed_out or run.time_ms > tl_ms:
        return "TLE"
    if run.returncode != 0:
        return "RE"
    if run.peak_mem_kb is not None and run.peak_mem_kb > ml_mb * 1024:
        return "MLE"
    if actual_norm == expected_norm:
        return "AC"
    return "WA"


def judge(problem, source_path, lang: str = "python") -> JudgeResult:
    source_path = Path(source_path)

    if problem.type == "func" and lang != "python":
        return JudgeResult(
            0, 0, [], False, lang=lang,
            unsupported="함수 구현형 문제는 Python 으로만 채점됩니다. (Java/C++ 정답 코드는 참고용으로 볼 수 있어요)",
        )

    try:
        if problem.type == "func":
            return _judge_func(problem, source_path)
        return _judge_stdin(problem, source_path, lang)
    except Exception as e:
        # 채점기 내부 오류(테스트케이스 형식 문제 등)가 앱 크래시로 이어지지 않게 격리
        return JudgeResult(
            0, 0, [], False, lang=lang,
            unsupported=f"채점 중 내부 오류가 발생했습니다: {type(e).__name__}: {e}",
        )


def _judge_stdin(problem, source_path: Path, lang: str) -> JudgeResult:
    tl_ms, ml_mb = _limits(problem, lang)

    comp = compile_solution(lang, source_path)
    if not comp.ok:
        return JudgeResult(
            len(problem.testcases), 0, [], False, lang=lang,
            compile_error=comp.error or "컴파일 실패",
        )

    # 시간 초과 강제 종료 한도(여유분 포함)
    kill_s = max(tl_ms * 3, tl_ms + 2000) / 1000.0

    cases = []
    for i, tc in enumerate(problem.testcases, start=1):
        inp = tc["input"]
        expected = _normalize(tc["output"])
        run = run_process(comp.run_cmd, inp, kill_s, cwd=comp.workdir, mem_limit_mb=ml_mb)
        actual = _normalize(run.stdout)
        verdict = _verdict_for(run, expected, actual, tl_ms, ml_mb)
        err = ""
        if verdict == "RE":
            err = run.stderr.strip().splitlines()[-1] if run.stderr.strip() else f"종료코드 {run.returncode}"
        cases.append(CaseResult(
            i, verdict, inp.strip(), expected, actual,
            time_ms=run.time_ms, peak_mem_kb=run.peak_mem_kb, error=err,
        ))
    return _summarize(cases, lang)


def _judge_func(problem, source_path: Path) -> JudgeResult:
    tl_ms, ml_mb = _limits(problem, "python")
    kill_s = max(tl_ms * 3, tl_ms + 2000) / 1000.0

    cases = []
    # ignore_cleanup_errors: TLE 로 강제 종료된 자식이 파일을 물고 있어도(Windows) 정리 예외 방지
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as td:
        for i, tc in enumerate(problem.testcases, start=1):
            args = tc["args"]
            expected = _normalize(repr(tc["expected"]))
            args_path = Path(td) / f"args_{i}.json"
            args_path.write_text(json.dumps(args), encoding="utf-8")
            cmd = func_cmd(FUNC_HARNESS, source_path, args_path, problem.func_name)
            run = run_process(cmd, "", kill_s, mem_limit_mb=ml_mb)
            actual = _normalize(run.stdout)
            verdict = _verdict_for(run, expected, actual, tl_ms, ml_mb)
            err = ""
            if verdict == "RE":
                tail = run.stderr.strip().splitlines()
                err = tail[-1] if tail else f"종료코드 {run.returncode}"
            cases.append(CaseResult(
                i, verdict,
                ", ".join(repr(a) for a in args),
                expected, actual,
                time_ms=run.time_ms, peak_mem_kb=run.peak_mem_kb, error=err,
            ))
    return _summarize(cases, "python")


def _summarize(cases, lang) -> JudgeResult:
    passed = sum(1 for c in cases if c.passed)
    max_t = max((c.time_ms for c in cases), default=0.0)
    mems = [c.peak_mem_kb for c in cases if c.peak_mem_kb is not None]
    max_m = max(mems) if mems else None
    return JudgeResult(
        total=len(cases), passed=passed, cases=cases,
        accepted=(passed == len(cases) and len(cases) > 0),
        lang=lang, max_time_ms=max_t, max_mem_kb=max_m,
    )
