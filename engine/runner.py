"""다국어 실행/측정 엔진.

- 프로세스를 실행하며 **실행 시간(ms)** 과 **최대 메모리(KB)** 를 측정한다.
- Windows 에서는 psapi.GetProcessMemoryInfo 로 PeakWorkingSetSize 를 읽는다.
- 시간 초과 시 프로세스를 강제 종료한다.

언어별 컴파일/실행 명령을 제공한다. (python / java / cpp)
"""

import os
import sys
import time
import shutil
import subprocess
from pathlib import Path
from dataclasses import dataclass

IS_WINDOWS = (os.name == "nt")

# Windows 에서 콘솔 하위 프로세스(javac/java/g++/실행파일 등)가
# 새 콘솔 창을 띄우지 않도록 하는 플래그. (--windowed 빌드에서 창 깜빡임 방지)
_NO_WINDOW = subprocess.CREATE_NO_WINDOW if IS_WINDOWS else 0

ENGINE_DIR = Path(__file__).resolve().parent
FUNC_HARNESS = ENGINE_DIR / "_func_harness.py"


# ───────────────────────── 메모리 측정 (Windows) ─────────────────────────

if IS_WINDOWS:
    import ctypes
    from ctypes import wintypes

    class _PMC(ctypes.Structure):
        _fields_ = [
            ("cb", wintypes.DWORD),
            ("PageFaultCount", wintypes.DWORD),
            ("PeakWorkingSetSize", ctypes.c_size_t),
            ("WorkingSetSize", ctypes.c_size_t),
            ("QuotaPeakPagedPoolUsage", ctypes.c_size_t),
            ("QuotaPagedPoolUsage", ctypes.c_size_t),
            ("QuotaPeakNonPagedPoolUsage", ctypes.c_size_t),
            ("QuotaNonPagedPoolUsage", ctypes.c_size_t),
            ("PagefileUsage", ctypes.c_size_t),
            ("PeakPagefileUsage", ctypes.c_size_t),
        ]

    def _peak_working_set_kb(handle) -> int | None:
        try:
            c = _PMC()
            c.cb = ctypes.sizeof(c)
            ok = ctypes.windll.psapi.GetProcessMemoryInfo(
                wintypes.HANDLE(int(handle)), ctypes.byref(c), c.cb
            )
            return (c.PeakWorkingSetSize // 1024) if ok else None
        except Exception:
            return None
else:
    def _peak_working_set_kb(handle) -> int | None:
        return None


# ───────────────────────── 실행 결과 ─────────────────────────

@dataclass
class RunResult:
    stdout: str
    stderr: str
    returncode: int
    time_ms: float
    peak_mem_kb: int | None
    timed_out: bool


def run_process(cmd, stdin_text: str, timeout_s: float, cwd=None) -> RunResult:
    """명령을 실행하고 시간·메모리를 측정한다."""
    t0 = time.perf_counter()
    proc = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        cwd=cwd,
        creationflags=_NO_WINDOW,
    )
    timed_out = False
    try:
        out, err = proc.communicate(input=stdin_text, timeout=timeout_s)
    except subprocess.TimeoutExpired:
        timed_out = True
        proc.kill()
        out, err = proc.communicate()
    t1 = time.perf_counter()

    peak = None
    try:
        if IS_WINDOWS and getattr(proc, "_handle", None) is not None:
            peak = _peak_working_set_kb(proc._handle)
    except Exception:
        peak = None

    return RunResult(
        stdout=out or "",
        stderr=err or "",
        returncode=proc.returncode if proc.returncode is not None else -1,
        time_ms=(t1 - t0) * 1000.0,
        peak_mem_kb=peak,
        timed_out=timed_out,
    )


# ───────────────────────── 언어 지원 ─────────────────────────

LANGUAGES = {
    "python":     {"name": "Python",     "ext": ".py",   "filename": "solution.py"},
    "java":       {"name": "Java",       "ext": ".java", "filename": "Main.java"},
    "cpp":        {"name": "C++",        "ext": ".cpp",  "filename": "main.cpp"},
    "javascript": {"name": "JavaScript", "ext": ".js",   "filename": "solution.js"},
    # 웹(학습 전용) — 채점이 아니라 컴파일/렌더 결과를 보여줌
    "css":        {"name": "CSS",        "ext": ".css",  "filename": "style.css"},
    "scss":       {"name": "SCSS",       "ext": ".scss", "filename": "style.scss"},
}


def _app_base() -> Path:
    """배포 시 실행 파일이 있는 폴더(번들 toolchain 의 기준 경로)."""
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent.parent      # 프로젝트 루트(codeTest/)


def _bundled(*relparts) -> Path | None:
    """codeTest/runtime/<...> 또는 실행파일 옆 runtime/<...> 가 있으면 그 경로."""
    p = _app_base().joinpath("runtime", *relparts)
    return p if p.exists() else None


def python_exe() -> str:
    """Python 풀이 실행에 쓸 인터프리터.

    PyInstaller 로 빌드하면 sys.executable 이 앱 exe 가 되므로,
    번들된 파이썬(runtime/python/python.exe)을 우선 사용한다.
    """
    cand = "python.exe" if IS_WINDOWS else "bin/python3"
    bp = _bundled("python", cand)
    if bp:
        return str(bp)
    return sys.executable


def python_cmd(source_path):
    """Python 스크립트 실행 명령. 빌드(frozen) 시엔 exe 자신을 인터프리터로 사용."""
    cand = "python.exe" if IS_WINDOWS else "bin/python3"
    bp = _bundled("python", cand)
    if bp:
        return [str(bp), str(source_path)]
    if getattr(sys, "frozen", False):
        return [sys.executable, "--exec-py", str(source_path)]
    return [sys.executable, str(source_path)]


def func_cmd(harness, source_path, args_path, func_name):
    """함수형 하니스 실행 명령. frozen 시엔 exe 자신이 하니스를 대신 수행."""
    cand = "python.exe" if IS_WINDOWS else "bin/python3"
    bp = _bundled("python", cand)
    if bp:
        return [str(bp), str(harness), str(source_path), str(args_path), func_name]
    if getattr(sys, "frozen", False):
        return [sys.executable, "--func", str(source_path), str(args_path), func_name]
    return [sys.executable, str(harness), str(source_path), str(args_path), func_name]


def _java_tools():
    """javac/java 절대 경로. 번들 JDK(runtime/jdk) → 시스템 PATH 순으로 찾는다.

    (Windows PATH 에 깨진 구버전 JRE 의 java.exe 가 먼저 잡히는 문제도 피한다.)
    """
    ext = ".exe" if IS_WINDOWS else ""
    # 1) 번들된 JDK 우선 (무설치 배포)
    bj = _bundled("jdk", "bin", "javac" + ext)
    if bj:
        java = bj.with_name("java" + ext)
        if java.exists():
            return str(bj), str(java)
    # 2) 시스템 PATH
    javac = shutil.which("javac")
    if not javac:
        return None, None
    p = Path(javac)
    java = p.with_name("java" + ext) if IS_WINDOWS else p.with_name("java")
    if not java.exists():
        fallback = shutil.which("java")
        java = Path(fallback) if fallback else None
    return str(javac), (str(java) if java else None)


def compiler_available(lang: str) -> bool:
    if lang == "python":
        return True
    if lang == "java":
        javac, java = _java_tools()
        return javac is not None and java is not None
    if lang == "cpp":
        return any(shutil.which(c) for c in ("g++", "clang++"))
    if lang == "javascript":
        return shutil.which("node") is not None
    if lang == "scss":
        try:
            import sass  # noqa
            return True
        except ImportError:
            return shutil.which("sass") is not None
    if lang == "css":
        return True
    return False


def _cpp_compiler() -> str | None:
    ext = ".exe" if IS_WINDOWS else ""
    # 1) 번들된 MinGW(g++) 우선 (무설치 배포)
    bg = _bundled("mingw", "bin", "g++" + ext)
    if bg:
        return str(bg)
    # 2) 시스템 PATH
    for c in ("g++", "clang++"):
        found = shutil.which(c)
        if found:
            return found
    return None


@dataclass
class CompileResult:
    ok: bool
    run_cmd: list | None      # 실행 명령
    error: str                # 컴파일 에러 메시지(있으면)
    workdir: Path | None


def compile_solution(lang: str, source_path: Path) -> CompileResult:
    """필요 시 컴파일하고 실행 명령을 돌려준다. python 은 컴파일 없음."""
    # 실행 시 cwd 를 바꾸므로 항상 절대 경로로 고정한다.
    source_path = Path(source_path).resolve()
    if lang == "python":
        return CompileResult(True, python_cmd(source_path), "", source_path.parent)

    if lang == "java":
        javac, java = _java_tools()
        if not javac or not java:
            return CompileResult(False, None, "JDK(javac/java)를 찾을 수 없습니다.", None)
        workdir = source_path.parent
        # 자바는 public class Main 필요 → 파일명도 Main.java 여야 함
        main_java = workdir / "Main.java"
        if source_path.name != "Main.java":
            shutil.copyfile(source_path, main_java)
        proc = subprocess.run(
            [javac, "-encoding", "UTF-8", str(main_java)],
            capture_output=True, text=True, cwd=workdir,
            creationflags=_NO_WINDOW,
        )
        if proc.returncode != 0:
            return CompileResult(False, None, proc.stderr.strip(), workdir)
        return CompileResult(True, [java, "-cp", str(workdir), "Main"], "", workdir)

    if lang == "cpp":
        comp = _cpp_compiler()
        if not comp:
            return CompileResult(False, None,
                                 "C++ 컴파일러(g++/clang++)가 설치되어 있지 않습니다.", None)
        workdir = source_path.parent
        exe = workdir / ("prog.exe" if IS_WINDOWS else "prog")
        # -static: 번들 MinGW 의 DLL 없이도 실행되도록 정적 링크(무설치 배포 대비)
        proc = subprocess.run(
            [comp, "-O2", "-std=c++17", "-static", "-o", str(exe), str(source_path)],
            capture_output=True, text=True, cwd=workdir,
            creationflags=_NO_WINDOW,
        )
        if proc.returncode != 0:
            return CompileResult(False, None, proc.stderr.strip(), workdir)
        return CompileResult(True, [str(exe)], "", workdir)

    if lang == "javascript":
        node = shutil.which("node")
        if not node:
            return CompileResult(False, None, "Node.js(node)가 설치되어 있지 않습니다.", None)
        return CompileResult(True, [node, str(source_path)], "", source_path.parent)

    return CompileResult(False, None, f"지원하지 않는 언어: {lang}", None)


def run_scss(source_text: str):
    """SCSS 소스를 CSS 로 컴파일해 (ok, css, error) 반환. libsass(파이썬) 우선."""
    try:
        import sass  # libsass
        css = sass.compile(string=source_text, output_style="expanded")
        return True, css, ""
    except ImportError:
        pass
    except Exception as e:  # 컴파일 에러
        return False, "", str(e)
    # 폴백: 시스템 sass 풀패스
    exe = shutil.which("sass")
    if exe:
        try:
            proc = subprocess.run([exe, "--stdin", "--no-source-map"],
                                  input=source_text, capture_output=True, text=True, timeout=40,
                                  creationflags=_NO_WINDOW)
            if proc.returncode != 0:
                return False, "", (proc.stderr or "컴파일 실패").strip()
            return True, proc.stdout, ""
        except Exception as e:  # noqa
            return False, "", str(e)
    return False, "", "SCSS 컴파일러가 없습니다. (pip install libsass)"


def scss_available() -> bool:
    try:
        import sass  # noqa
        return True
    except ImportError:
        return shutil.which("sass") is not None
