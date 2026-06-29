"""레슨 모듈 검증 — 각 Lesson 의 예시 code 가 실제로 실행되는지 확인.

실행:  python tools/verify_lessons.py lessons/content/py_mid.py

python/java 는 실제 실행(returncode 0)까지 확인한다.
cpp 는 g++ 가 없으면 건너뛴다(빌드 시 검증).
"""

import sys
import tempfile
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from engine.runner import compile_solution, run_process, compiler_available

path = Path(sys.argv[1])
if not path.is_absolute():
    path = ROOT / path
spec = importlib.util.spec_from_file_location("lessonmod", path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

FN = {"python": "sol.py", "java": "Main.java", "cpp": "main.cpp"}
fail = 0
ran = 0
print(f"검증: {path.name}  (레슨 {len(getattr(mod, 'LESSONS', []))}개)")
print("-" * 60)
for l in getattr(mod, "LESSONS", []):
    if l.lang not in FN or not l.code.strip():
        print(f"  skip(읽기전용) {l.id}")
        continue
    if not compiler_available(l.lang):
        print(f"  skip(no {l.lang}) {l.id}")
        continue
    d = Path(tempfile.mkdtemp())
    sp = d / FN[l.lang]
    sp.write_text(l.code, encoding="utf-8")
    comp = compile_solution(l.lang, sp)
    if not comp.ok:
        print(f"  CE   {l.id}: {comp.error.strip().splitlines()[-1][:70] if comp.error.strip() else ''}")
        fail += 1
        continue
    r = run_process(comp.run_cmd, "", 10, cwd=comp.workdir)
    ran += 1
    if r.returncode == 0:
        print(f"  OK   {l.id}  ({r.time_ms:.0f}ms)")
    else:
        tail = r.stderr.strip().splitlines()[-1][:70] if r.stderr.strip() else f"rc {r.returncode}"
        print(f"  RE   {l.id}: {tail}")
        fail += 1
print("-" * 60)
print(f"실행 {ran}개, 실패 {fail}")
sys.exit(1 if fail else 0)
