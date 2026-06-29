"""코딩테스트 연습기 — 메인 실행기 (CLI).

실행:  python main.py

기능:
  - 랭크(브론즈~플래티넘) → 문제 선택
  - Python / Java / C++ 중 언어 선택해서 풀기
  - 채점: 정답/오답 + 실행 시간(ms) + 최대 메모리(KB) + 시간/메모리 초과(TLE/MLE) 판정
  - 힌트 1·2·3단계 (요청할 때만 단계별로 공개)
  - 다음 문제 / 이전 문제로 이어서 진행
  - 푼 문제 진행 상황 저장(solutions/progress.json)
    python main.py            # 랭크별 + P) 유형별 실전 연습
    python tools/coverage.py  # 유형/랭크 커버리지
    python tools/selftest.py  # 정답코드 무결성
"""

import sys
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

import problems
import practice
from engine.judge import judge as judge_problem, VERDICT_KR
from engine import runner

SOLUTIONS_DIR = ROOT / "solutions"
PROGRESS_FILE = SOLUTIONS_DIR / "progress.json"

LINE = "─" * 64

# 세션 상태
session = {"lang": "python"}


# ───────────────────────── 진행 상황 저장 ─────────────────────────

def load_progress() -> set:
    if PROGRESS_FILE.exists():
        try:
            return set(json.loads(PROGRESS_FILE.read_text(encoding="utf-8")))
        except Exception:
            return set()
    return set()


def save_progress(solved: set):
    SOLUTIONS_DIR.mkdir(exist_ok=True)
    PROGRESS_FILE.write_text(json.dumps(sorted(solved), ensure_ascii=False, indent=0),
                             encoding="utf-8")


SOLVED = load_progress()


# ───────────────────────── 입출력 유틸 ─────────────────────────

def ask(prompt: str) -> str:
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print("\n종료합니다.")
        sys.exit(0)


def header(text: str):
    print("\n" + LINE)
    print(text)
    print(LINE)


def fmt_mem(kb):
    if kb is None:
        return "측정불가"
    if kb >= 1024:
        return f"{kb/1024:.1f} MB"
    return f"{kb} KB"


# ───────────────────────── 솔루션 파일 ─────────────────────────

JAVA_TEMPLATE = (
    "import java.util.*;\n"
    "import java.io.*;\n\n"
    "public class Main {\n"
    "    public static void main(String[] args) throws IOException {\n"
    "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
    "        // TODO: 표준입력을 읽고 정답을 표준출력으로 출력하세요.\n"
    "    }\n"
    "}\n"
)

CPP_TEMPLATE = (
    "#include <bits/stdc++.h>\n"
    "using namespace std;\n\n"
    "int main() {\n"
    "    ios_base::sync_with_stdio(false);\n"
    "    cin.tie(nullptr);\n"
    "    // TODO: 표준입력을 읽고 정답을 표준출력으로 출력하세요.\n"
    "    return 0;\n"
    "}\n"
)


def problem_dir(p) -> Path:
    return SOLUTIONS_DIR / p.id


def solution_file(p, lang) -> Path:
    return problem_dir(p) / runner.LANGUAGES[lang]["filename"]


def template_for(p, lang) -> str:
    if lang == "python":
        return p.template_py or "def solution():\n    pass\n"
    if lang == "java":
        return JAVA_TEMPLATE
    if lang == "cpp":
        return CPP_TEMPLATE
    return ""


def ensure_solution_file(p, lang) -> Path:
    problem_dir(p).mkdir(parents=True, exist_ok=True)
    path = solution_file(p, lang)
    if not path.exists():
        path.write_text(template_for(p, lang), encoding="utf-8")
    return path


# ───────────────────────── 문제 출력 ─────────────────────────

def difficulty_tag(p):
    parts = [problems.RANK_KR[p.rank]]
    if p.tier:
        parts.append(p.tier)
    if p.boj:
        parts.append(f"BOJ {p.boj}")
    return " · ".join(parts)


def show_problem(p):
    mark = "✓ " if p.id in SOLVED else ""
    header(f"{mark}[{p.id}] {p.title}   ({difficulty_tag(p)})")
    style = "표준입출력형(stdin)" if p.type == "stdin" else f"함수 구현형(func) — 함수명: {p.func_name}()"
    langs = "Python · Java · C++" if p.type == "stdin" else "Python (Java/C++는 정답 코드 참고용)"
    print(f"출제 스타일 : {p.style} · {p.topic}")
    print(f"채점 방식   : {style}")
    print(f"풀이 가능   : {langs}")
    print(f"제한        : 시간 {p.time_limit_ms} ms · 메모리 {p.memory_limit_mb} MB")
    print("\n[문제]")
    print(p.description)
    if p.input_desc:
        print("\n[입력]")
        print(p.input_desc)
    if p.output_desc:
        print("\n[출력]")
        print(p.output_desc)
    print("\n[예제]")
    for i, ex in enumerate(p.examples, 1):
        if p.type == "stdin":
            print(f"  · 예제 {i}")
            print("    입력:")
            for ln in ex["input"].rstrip("\n").split("\n"):
                print(f"      {ln}")
            print("    출력:")
            for ln in str(ex["output"]).rstrip("\n").split("\n"):
                print(f"      {ln}")
        else:
            args_repr = ", ".join(repr(a) for a in ex["args"])
            print(f"  · {p.func_name}({args_repr})  →  {ex['output']!r}")


# ───────────────────────── 풀기 / 채점 ─────────────────────────

def choose_language():
    print("\n언어 선택:  1) Python   2) Java   3) C++")
    sel = ask("언어> ")
    m = {"1": "python", "2": "java", "3": "cpp"}
    if sel in m:
        session["lang"] = m[sel]
        ok = runner.compiler_available(session["lang"])
        name = runner.LANGUAGES[session["lang"]]["name"]
        print(f"→ 현재 언어: {name}" + ("" if ok else "  (※ 컴파일러 미설치 — 채점하려면 설치 필요)"))
    else:
        print("변경하지 않았습니다.")


def start_solving(p):
    lang = session["lang"]
    if p.type == "func" and lang != "python":
        print(f"\n※ 이 문제는 함수 구현형이라 {runner.LANGUAGES[lang]['name']}로는 채점되지 않습니다.")
        print("  Python으로 풀거나, 정답 코드 보기로 참고하세요.")
        return
    path = ensure_solution_file(p, lang)
    header(f"풀기 시작 — {runner.LANGUAGES[lang]['name']}")
    print(f"풀이 파일:\n  {path}")
    print("\n이 파일을 열어 코드를 작성한 뒤 '채점하기'를 선택하세요.")
    if p.type == "func":
        print(f"\n※ '{p.func_name}' 함수를 정의하고 결과를 return 하세요.")
    else:
        print("\n※ 표준입력(input/Scanner/cin)으로 읽고 표준출력(print/System.out/cout)으로 출력하세요.")


def run_judge(p):
    lang = session["lang"]
    if p.type == "func" and lang != "python":
        print(f"\n※ 함수 구현형 문제는 Python으로만 채점됩니다. 현재 언어: {runner.LANGUAGES[lang]['name']}")
        return
    if not runner.compiler_available(lang):
        print(f"\n※ {runner.LANGUAGES[lang]['name']} 컴파일러가 없어 채점할 수 없습니다. (README의 설치 안내 참고)")
        return
    path = solution_file(p, lang)
    if not path.exists():
        ensure_solution_file(p, lang)
        print(f"\n풀이 파일을 새로 만들었습니다:\n  {path}\n코드를 작성한 뒤 다시 채점하세요.")
        return

    header(f"채점 결과 — {runner.LANGUAGES[lang]['name']}  (제한: {p.time_limit_ms}ms / {p.memory_limit_mb}MB)")
    result = judge_problem(p, path, lang)

    if result.unsupported:
        print(result.unsupported)
        return
    if result.compile_error:
        print("✗ 컴파일 에러(CE)\n")
        print(result.compile_error)
        return

    for c in result.cases:
        kr = VERDICT_KR.get(c.verdict, c.verdict)
        flag = "O" if c.passed else "X"
        print(f"  케이스 {c.index}: {flag} {kr}({c.verdict})  "
              f"· {c.time_ms:.0f}ms · {fmt_mem(c.peak_mem_kb)}")
        if not c.passed:
            if c.verdict in ("WA",):
                print(f"      입력    : {c.given_input}")
                print(f"      기대값  : {c.expected}")
                print(f"      내 출력 : {c.actual}")
            elif c.verdict == "RE" and c.error:
                print(f"      에러    : {c.error}")
            elif c.verdict == "TLE":
                print(f"      제한 {p.time_limit_ms}ms 초과")
            elif c.verdict == "MLE":
                print(f"      제한 {p.memory_limit_mb}MB 초과")
    print(LINE)
    if result.accepted:
        print(f"  ★ 정답(AC)!  {result.passed}/{result.total} 통과  "
              f"· 최대 {result.max_time_ms:.0f}ms · {fmt_mem(result.max_mem_kb)}")
        if p.id not in SOLVED:
            SOLVED.add(p.id)
            save_progress(SOLVED)
            print("  (진행 상황에 저장됨)")
    else:
        print(f"  ✗ 통과 {result.passed}/{result.total}.  힌트를 보거나 코드를 고쳐 다시 도전하세요.")


# ───────────────────────── 힌트 / 정답 ─────────────────────────

def show_hint(p, level):
    header(f"힌트 {level}단계")
    if level - 1 < len(p.hints):
        print(p.hints[level - 1])
        if level == 3:
            print("\n(3단계 힌트는 거의 정답 수준입니다.)")
    else:
        print("이 단계의 힌트가 없습니다.")


def show_reference(p, lang):
    name = {"python": "Python", "java": "Java", "cpp": "C++"}[lang]
    header(f"정답 코드 ({name})")
    code = {"python": p.reference_py, "java": p.reference_java, "cpp": p.reference_cpp}[lang]
    if code.strip():
        print(code)
    else:
        print(f"{name} 정답 코드가 아직 준비되지 않았습니다.")


# ───────────────────────── 문제 메뉴 ─────────────────────────

def problem_menu(plist, idx, ctx_label=""):
    """plist 의 idx 번째 문제를 다룬다. 반환: 다음에 볼 idx 또는 None(뒤로)."""
    p = plist[idx]
    show_problem(p)
    while True:
        cur_lang = runner.LANGUAGES[session["lang"]]["name"]
        print("\n" + "-" * 48)
        loc = f"{ctx_label} " if ctx_label else ""
        print(f"[{p.id}] {p.title}   | 현재 언어: {cur_lang}  ({loc}{idx+1}/{len(plist)})")
        print("  1) 문제 다시 보기      2) 언어 선택")
        print("  3) 풀기 시작           4) 채점하기")
        print("  5) 힌트 1단계   6) 힌트 2단계   7) 힌트 3단계(거의 정답)")
        print("  8) 정답 Python   9) 정답 Java   10) 정답 C++")
        print("  n) 다음 문제     p) 이전 문제     0) 목록으로")
        sel = ask("선택> ").lower()
        if sel == "1":
            show_problem(p)
        elif sel == "2":
            choose_language()
        elif sel == "3":
            start_solving(p)
        elif sel == "4":
            run_judge(p)
        elif sel == "5":
            show_hint(p, 1)
        elif sel == "6":
            show_hint(p, 2)
        elif sel == "7":
            show_hint(p, 3)
        elif sel == "8":
            show_reference(p, "python")
        elif sel == "9":
            show_reference(p, "java")
        elif sel == "10":
            show_reference(p, "cpp")
        elif sel == "n":
            if idx + 1 < len(plist):
                return idx + 1
            print("마지막 문제입니다.")
        elif sel == "p":
            if idx - 1 >= 0:
                return idx - 1
            print("첫 문제입니다.")
        elif sel == "0":
            return None
        else:
            print("잘못된 입력입니다.")


def rank_menu(rank):
    plist = problems.ALL[rank]
    while True:
        solved_cnt = sum(1 for p in plist if p.id in SOLVED)
        header(f"{problems.RANK_KR[rank]} ({rank}) — {len(plist)}문제 · 푼 문제 {solved_cnt}개")
        for i, p in enumerate(plist, 1):
            mark = "✓" if p.id in SOLVED else " "
            tier = f"[{p.tier}]" if p.tier else ""
            print(f"  {mark} {i:2d}) [{p.id}] {p.title:<22} {tier:<5} · {p.topic} · {p.style}")
        print("   0) 뒤로")
        sel = ask("문제 번호(또는 0)> ")
        if sel == "0":
            return
        if sel.isdigit() and 1 <= int(sel) <= len(plist):
            idx = int(sel) - 1
            while idx is not None:
                idx = problem_menu(plist, idx, problems.RANK_KR[rank])
        else:
            print("잘못된 입력입니다.")


# ───────────────────────── 유형별 실전 연습 ─────────────────────────

def category_menu(cat):
    plist = practice.ALL.get(cat, [])
    while True:
        solved_cnt = sum(1 for p in plist if p.id in SOLVED)
        header(f"[유형] {cat} — {len(plist)}문제 · 푼 문제 {solved_cnt}개")
        desc = practice.CATEGORY_DESC.get(cat, "")
        if desc:
            print(f"  ({desc})")
        if not plist:
            print("\n  아직 이 유형의 실전 문제가 없습니다.")
            ask("\n[Enter] 로 돌아가기 ")
            return
        for i, p in enumerate(plist, 1):
            mark = "✓" if p.id in SOLVED else " "
            print(f"  {mark} {i:2d}) [{p.id}] {p.title:<26} · {p.style}")
        print("   0) 뒤로")
        sel = ask("문제 번호(또는 0)> ")
        if sel == "0":
            return
        if sel.isdigit() and 1 <= int(sel) <= len(plist):
            idx = int(sel) - 1
            while idx is not None:
                idx = problem_menu(plist, idx, cat)
        else:
            print("잘못된 입력입니다.")


def practice_menu():
    while True:
        header(f"유형별 실전 연습   (총 {practice.total()}문제 · 현재 언어: {runner.LANGUAGES[session['lang']]['name']})")
        print("  대기업 코테 빈출 유형 (우선순위순)")
        for i, cat in enumerate(practice.CATEGORIES, 1):
            cnt = practice.count(cat)
            sc = sum(1 for p in practice.ALL.get(cat, []) if p.id in SOLVED)
            tag = f"{cnt}문제 · {sc}개 완료" if cnt else "준비 중"
            print(f"  {i:2d}) {cat:<16} — {tag}")
        print("   0) 뒤로")
        sel = ask("유형 번호(또는 0)> ")
        if sel == "0":
            return
        if sel.isdigit() and 1 <= int(sel) <= len(practice.CATEGORIES):
            category_menu(practice.CATEGORIES[int(sel) - 1])
        else:
            print("잘못된 입력입니다.")


def main_menu():
    print("\n" + "=" * 64)
    print("   코딩테스트 연습기  (백준 / 프로그래머스 / 대기업 스타일)")
    print("   Python · Java · C++  |  시간·메모리 측정 · 3단계 힌트")
    print("=" * 64)
    while True:
        total_solved = len(SOLVED)
        header(f"랭크 선택   (현재 언어: {runner.LANGUAGES[session['lang']]['name']} · 총 푼 문제 {total_solved}개)")
        for i, rank in enumerate(problems.RANKS, 1):
            cnt = problems.count(rank)
            sc = sum(1 for p in problems.ALL[rank] if p.id in SOLVED)
            print(f"  {i}) {problems.RANK_KR[rank]:<5} ({rank})  — {cnt}문제 · {sc}개 완료")
        print(f"  P) 유형별 실전 연습  — {practice.total()}문제 (대기업 빈출 유형별)")
        print("  L) 언어 선택      0) 종료")
        sel = ask("선택> ").lower()
        if sel == "0":
            print("수고하셨습니다!")
            return
        if sel == "l":
            choose_language()
        elif sel == "p":
            practice_menu()
        elif sel.isdigit() and 1 <= int(sel) <= len(problems.RANKS):
            rank_menu(problems.RANKS[int(sel) - 1])
        else:
            print("잘못된 입력입니다.")


if __name__ == "__main__":
    main_menu()
