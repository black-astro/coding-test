# 무설치(포터블) 빌드 가이드 — code T

목표: 받는 사람이 **아무것도 설치하지 않고** exe 하나로 실행하고,
**Python·Java·C++ 채점까지** 되게 만든다.

핵심 아이디어: 앱은 `실행파일 옆 runtime/` 폴더에서 toolchain 을 먼저 찾는다.
- `runtime/python/` → Python 실행기 (Python 채점용, **필수**)
- `runtime/jdk/` → 미니 JDK (Java 채점용)
- `runtime/mingw/` → MinGW-w64 g++ (C++ 채점용)

해당 폴더가 없으면 그 언어 채점만 비활성화되고 앱은 정상 동작한다.
(코드상 `engine/runner.py` 의 `_bundled()` 가 이 경로들을 찾는다.)

---

## 1) 앱 빌드 (PyInstaller)

```bash
pip install pyinstaller
python build.py
```

→ `dist/codeT/codeT.exe` 와 `dist/codeT/_internal/` 생성.
이 `dist/codeT` 폴더가 배포 단위다(통째로 zip).

> 앱 자체(Python+PySide6)는 PyInstaller 가 포함하므로, 받는 사람은
> Python/PySide6 설치가 필요 없다. 아래 toolchain 은 "채점 실행"용이다.

## 2) Python 채점기 넣기 (필수)

빌드된 exe 는 더 이상 일반 python 인터프리터가 아니라서, 채점용 파이썬을 따로 넣는다.

1. https://www.python.org/downloads/windows/ 에서
   **"Windows embeddable package (64-bit)"** 다운로드 (약 10MB).
2. 압축을 풀어 `dist/codeT/runtime/python/` 에 넣는다.
   (`dist/codeT/runtime/python/python.exe` 가 있어야 함)
3. 표준 라이브러리만 쓰면 추가 설정 불필요. (문제 풀이는 stdlib 만 사용)

## 3) Java 채점기 넣기 (선택)

미니 JDK 를 `jlink` 로 만들어 넣으면 Java 채점이 켜진다.

```bash
# JDK 21 이 설치된 PC에서 (배포자만 1회):
jlink --add-modules java.base,jdk.compiler,java.logging ^
      --strip-debug --no-header-files --no-man-pages --compress=2 ^
      --output minijdk
```

→ 생성된 `minijdk` 폴더를 `dist/codeT/runtime/jdk/` 로 복사.
(`dist/codeT/runtime/jdk/bin/javac.exe`, `java.exe` 가 있어야 함. 약 50–70MB)

## 4) C++ 채점기 넣기 (선택)

MinGW-w64 를 넣으면 C++ 채점이 켜진다.

1. MinGW-w64 (예: WinLibs standalone build, https://winlibs.com ) 다운로드.
2. 압축 안의 `mingw64` 내용을 `dist/codeT/runtime/mingw/` 로 복사.
   (`dist/codeT/runtime/mingw/bin/g++.exe` 가 있어야 함. 약 100–300MB)
3. C++ 는 `-static` 로 컴파일하므로 결과 실행파일은 DLL 의존성이 없다.

## 5) 최종 폴더 구조

```
codeT/                     ← 이 폴더를 zip 으로 배포
├── codeT.exe
├── _internal/            (PyInstaller 런타임)
├── runtime/
│   ├── python/python.exe        (필수)
│   ├── jdk/bin/javac.exe ...     (Java 채점 시)
│   └── mingw/bin/g++.exe ...     (C++ 채점 시)
└── solutions/            (실행 중 자동 생성: 내 풀이 + progress.json)
```

## 용량 가이드

| 구성 | 대략 용량 |
|------|-----------|
| 앱(codeT.exe + _internal, PySide6 포함) | ~120–180 MB |
| + python embed | +10 MB |
| + 미니 JDK(jlink) | +50–70 MB |
| + MinGW(g++) | +100–300 MB |

Python만 채점하면 가볍게(~150MB), 3개 언어 다 넣으면 ~400–500MB 정도다.
C++ 가 가장 무거우니, 필요 없으면 `runtime/mingw` 를 빼면 된다.

## 참고
- toolchain 경로 탐색은 `engine/runner.py` 의 `_bundled / python_exe / _java_tools / _cpp_compiler` 에 구현.
- 빌드된 앱은 `solutions/` 와 `progress.json` 을 exe 옆에 쓴다(쓰기 가능 위치).
