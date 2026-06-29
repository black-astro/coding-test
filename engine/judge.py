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
from engine.runner import run_process, compile_solution, FUNC_HARNESS, python_exe

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


def _limits(problem):
    tl = problem.time_limit_ms or 2000
    ml = problem.memory_limit_mb or 256
    return tl, ml


def _verdict_for(run, expected_norm, actual_norm, tl_ms, ml_mb):
    """단일 실행 결과에 대한 판정."""
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

    if problem.type == "func":
        return _judge_func(problem, source_path)
    return _judge_stdin(problem, source_path, lang)


def _judge_stdin(problem, source_path: Path, lang: str) -> JudgeResult:
    tl_ms, ml_mb = _limits(problem)

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
        run = run_process(comp.run_cmd, inp, kill_s, cwd=comp.workdir)
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
    tl_ms, ml_mb = _limits(problem)
    kill_s = max(tl_ms * 3, tl_ms + 2000) / 1000.0

    cases = []
    with tempfile.TemporaryDirectory() as td:
        for i, tc in enumerate(problem.testcases, start=1):
            args = tc["args"]
            expected = _normalize(repr(tc["expected"]))
            args_path = Path(td) / f"args_{i}.json"
            args_path.write_text(json.dumps(args), encoding="utf-8")
            cmd = [python_exe(), str(FUNC_HARNESS), str(source_path),
                   str(args_path), problem.func_name]
            run = run_process(cmd, "", kill_s)
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
