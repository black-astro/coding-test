# code T — 코딩테스트 연습기 (Python · Java · C++)

대한민국 대기업 코딩테스트 대비용 **올인원 연습 프로그램**입니다.
랭크별 문제, 유형별/종목별 학습, **언어 문법 강의(Python·Java·C++)**, **실전 모의고사(합격/불합격 판정)**,
그리고 **실행 시간·메모리 측정 채점**을 하나의 데스크톱 앱(PySide6, VSCode Dracula 테마)에서 제공합니다.

![rank](https://img.shields.io/badge/rank-Bronze~Platinum-blueviolet) ![langs](https://img.shields.io/badge/lang-Python%20%C2%B7%20Java%20%C2%B7%20C%2B%2B-44cc88)

---

## 1. 설치 & 실행

### 요구 사항
- **Python 3.10+** (필수)
- **JDK 17+** (Java로 풀 때) — 없으면 Java 채점만 비활성
- **g++ (MinGW)** (C++로 풀 때) — 없으면 C++ 채점만 비활성
- **Node.js** (JavaScript로 풀 때) — 없으면 JS 채점만 비활성
- SCSS 컴파일은 `libsass`(파이썬 패키지)로 자동 처리

### 설치
```bash
pip install -r requirements.txt      # PySide6, qtawesome, libsass
python gui.py                         # GUI 실행
```

지원 언어: **Python · Java · C++ · JavaScript** (문제 풀이/채점) + **CSS · SCSS** (웹 문법 학습).

> JDK / g++ 설치 방법은 앱 안의 **사이드바 → guide** 섹션에 단계별로 들어 있습니다.
> (또는 아래 5번 참고)

### CLI 버전도 있음
```bash
python main.py
```

---

## 2. 화면 구성 (VSCode 풍)

```
┌ [🥈 S2 · 1240p]  [Python|Java|C++]              ⟳   ▶ Run ┐   ← 헤더(내 랭크/점수·언어·실행)
├──────────────┬───────────────────────┬──────────────────────┤
│  사이드바      │   문제 (설명/예제)      │  console (코드 에디터) │
│  lank         │   ⏱시간 💾메모리        │  라인넘버·구문강조      │
│  real         │   (우클릭→힌트1·2·3·last)├──────────────────────┤
│  part         │                       │  terminal (채점 결과)  │
│  lang         │                       │  PASS/FAIL·시간·메모리 │
│  exam         │                       │                      │
│  guide        │                       │                      │
└──────────────┴───────────────────────┴──────────────────────┘
```

### 사이드바 섹션
| 섹션 | 내용 |
|------|------|
| **lank** | 랭크별 문제 — 🥉 Bronze / 🥈 Silver / 🥇 Gold / 💎 Platinum (각 50문제) |
| **real** | 유형별 실전 — 구현/DFS·BFS/DP/그리디/해시/이분탐색/세그트리 등 대기업 빈출 유형 |
| **part** | 종목별 학습 — 같은 알고리즘을 **기초→고급** 난이도순으로 (BFS가 실버~골드에 걸쳐 나오는 식) |
| **lang** | 언어 문법 강의 — **Python·Java·C++·JavaScript × 기초·중급·고급** + **CSS·SCSS** (설명+예시+사용처+단점, 직접 실행/컴파일) |
| **exam** | **실전 모의고사** — 난이도 섞어 출제, 제한시간, 합격/불합격 판정 |
| **guide** | 환경 설정 — JDK/g++ 설치·적용·사용법 |

---

## 3. 사용법

### 문제 풀기
1. 사이드바에서 문제 선택 → 가운데에 문제·예제·제한(시간/메모리)이 뜸
2. 상단 **언어 토글**(Python/Java/C++) 선택
3. 오른쪽 **console** 에디터에 코드 작성
4. **▶ Run (F5)** 또는 console에서 **우클릭 → 실행** → 아래 **terminal**에 케이스별 결과
   - `PASS / FAIL / TIMEOUT / MEM / ERROR / BUILD ERR` + 실행 시간(ms) + 최대 메모리
   - 모든 케이스 통과 시 `✓ all passed` → 진행상황 저장(✓)·점수 반영

### 힌트
- **문제 영역에서 우클릭** → `힌트 1 · 2 · 3 · last`
- 1→2→3 으로 갈수록 자세해지고, **last 는 정답 코드 + 풀이 설명**까지
- 힌트는 문제 본문 **아래쪽에 누적**되어 스크롤로 봄

### 정답/오답 & 랭크
- 문제별 점수가 있고, 헤더에 **내 랭크(B5~P1)·점수**가 작게 표시됨
- 랭크는 **양이 아니라 수준**으로 판정 — 브론즈·실버를 다 풀어도, 골드 문제를 풀어야 골드가 됨
  (누적 점수 기준치 + 해당 랭크 최소 해결 수를 모두 충족해야 승급)

### 문제 리셋(변형)
- 헤더 **⟳** → 확인 → '구구단 N단', 'A+B' 처럼 **변수 부분이 새 랜덤 값**으로 바뀜
  (외운 답이 안 통하게 → 다시 풀이 연습). 해당 문제 진행상황은 초기화됨

### 실전 모의고사 (exam)
- 사이드바 **exam** 에서 프리셋 선택:
  - 대기업 종합형(5문제·90분), 삼성 SW역량형(2문제·120분), 실무 기본형(3문제·60분), 고난도 종합(4문제·150분), 랜덤 풀세트
- 난이도가 섞여 **무작위 출제** → 제한시간 카운트다운(헤더 ⏳)
- 사이드바 **▶ 시험** 그룹에서 문제를 풀고, 상단 **제출**(또는 시간 종료 시 자동) → **합격/불합격** 판정
- 합격 기준: 정답 문제 수 ≥ 프리셋 기준(예: 5문제 중 3문제)

### 언어 문법 학습 (lang)
- Python/Java/C++ → 기초/중급/고급 → 항목 선택
- 카드에 **설명 · 어디에/어떻게 쓰나 · 단점 · 예시코드**, console에 예시가 올라가 **Run으로 직접 실행**

---

## 4. 채점 판정

| 판정 | 의미 |
|------|------|
| PASS | 정답 |
| FAIL | 오답(출력 불일치) |
| TIMEOUT | 시간 초과 |
| MEM | 메모리 초과 |
| ERROR | 런타임 에러 |
| BUILD ERR | 컴파일 에러 |

랭크별 기본 제한: 브론즈 1000ms/128MB · 실버 1500ms/256MB · 골드 2000ms/256MB · 플래티넘 3000ms/512MB
(stdin형 문제는 3개 언어 모두 채점, 함수 구현형은 Python 채점 + Java/C++ 정답 참고)

---

## 5. JDK / g++ 설치 (요약)

앱의 **guide** 섹션에 더 자세히 있습니다.

- **Java(JDK)**: https://adoptium.net 에서 JDK 21 설치(또는 `winget install EclipseAdoptium.Temurin.21.JDK`).
  설치 후 `javac -version` 이 보이면 자동 인식.
- **C++(g++)**: https://winlibs.com 의 MinGW-w64 zip을 풀어 `...\mingw64\bin` 을 PATH에 추가.
  `g++ --version` 이 보이면 자동 인식.

> JDK는 기본 포함되어 있지 않습니다(시스템 설치본 사용). **무설치 배포판**을 만들면
> `runtime/jdk`, `runtime/mingw`, `runtime/python` 을 함께 넣어 설치 없이 3개 언어가 동작합니다 → `BUILD.md`.

---

## 6. 무설치(포터블) 빌드

```bash
pip install pyinstaller
python build.py        # dist/codeT/codeT.exe 생성
```
자세한 toolchain 동봉 방법은 **BUILD.md** 참고.

---

## 7. 프로젝트 구조

```
codeTest/
├── gui.py               GUI 메인 (PySide6)
├── main.py              CLI 버전
├── engine/
│   ├── models.py        Problem / Lesson 데이터 구조
│   ├── runner.py        다국어 컴파일·실행·시간/메모리 측정
│   ├── judge.py         채점·판정
│   ├── profile.py       점수·랭크 판독
│   ├── topics.py        종목(알고리즘) 분류
│   ├── variants.py      문제 변형(리셋) 생성기
│   └── exam.py          실전 모의고사 구성·채점
├── problems/            랭크별 문제(200) + meta(티어/백준) + cpp(정답)
├── practice/            유형별 실전 문제(51) + cpp
├── lessons/             언어 문법 강의(Python/Java/C++) + 환경 가이드
├── tools/               selftest / verify_batch / verify_lessons / coverage
├── requirements.txt
├── build.py / BUILD.md  무설치 빌드
└── COMPARISON.md / CLAUDE.md
```

## 8. 검증
```bash
python tools/selftest.py        # 모든 정답 코드가 자기 테스트케이스를 통과하는지
python tools/coverage.py        # 랭크/유형 커버리지
```

---

만든 목적: **이 프로그램 하나로 Python·Java·C++ 문법을 익히고, 기초부터 플래티넘까지 코딩테스트를 연습**하며,
실전 모의고사로 합격선을 점검하는 것. (대기업 메인부서 기준 실버~골드면 통과권, 삼성 계열은 골드~플래티넘 권장)
