"""무설치 배포 빌드 스크립트 (PyInstaller).

사용:
    pip install pyinstaller
    python build.py

결과: dist/codeT/codeT.exe  (폴더 통째로 압축해서 배포)

무설치로 Python/Java/C++ 채점까지 되게 하려면, 빌드 후
dist/codeT/runtime/ 안에 toolchain 을 넣는다 (BUILD.md 참고):
    runtime/python/   ← python-embed (Python 채점용, 필수)
    runtime/jdk/      ← jlink 로 만든 미니 JDK (Java 채점용)
    runtime/mingw/    ← MinGW-w64 (C++ 채점용)
toolchain 이 없으면 그 언어 채점만 비활성화되고 앱은 정상 동작한다.
"""

import sys
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SEP = ";" if sys.platform == "win32" else ":"


def main():
    args = [
        sys.executable, "-m", "PyInstaller",
        "--noconfirm", "--clean",
        "--windowed",                       # 콘솔창 없이 GUI 로 실행
        "--name", "codeT",
        "--collect-submodules", "problems",   # 동적 import 되는 문제/레슨/단어 모듈 모두 포함
        "--collect-submodules", "practice",
        "--collect-submodules", "lessons",
        "--collect-submodules", "vocab",
        "--collect-all", "qtawesome",         # 아이콘 폰트 데이터
        "--collect-all", "sass",              # libsass 바이너리(SCSS 컴파일)
        "--add-data", f"{ROOT / 'engine' / '_func_harness.py'}{SEP}engine",
        "gui.py",
    ]
    print(">", " ".join(args))
    subprocess.run(args, check=True)
    print("\n[완료] dist/codeT/codeT.exe")
    print("무설치 채점용 toolchain 은 BUILD.md 를 보고 dist/codeT/runtime/ 에 넣으세요.")


if __name__ == "__main__":
    main()
