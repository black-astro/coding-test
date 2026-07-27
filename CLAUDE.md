# CLAUDE.md — 코딩테스트 연습기

이 저장소는 **대한민국 대기업 코딩테스트 대비 연습 도구**다.
Python·Java·C++ 로 풀고, 실행 시간·메모리까지 측정해 실전처럼 채점한다.

## 빠른 시작

```bash
python main.py                   # 연습 시작 (랭크별 + 유형별 실전)
python tools/selftest.py         # 모든 정답 코드 무결성 검증
python tools/verify_datasci.py   # 데이터분석 트랙 강의 코드 + 문제 검증
```

## 구성 요약

- **랭크별 문제**: 브론즈~플래티넘 각 50문제(총 200). `problems/`
- **유형별 실전 문제**: 대기업 빈출 유형별 묶음. `practice/`
- **데이터분석 트랙**: Python 전용 5단계 학습(기초→통계→ML→딥러닝→LLM). 강의 57 + 문제 31. `datasci/`
- **채점**: 정답/오답 + 시간(ms) + 최대 메모리 + TLE/MLE/RE/CE 판정. `engine/`
- **힌트**: 문제마다 1·2·3단계(3단계는 거의 정답)
- 자세한 사용법은 `README.md`, KT_BatchServer 비교는 `COMPARISON.md`

---

# 대기업 코딩테스트 유형 우선순위 (학습 가이드)

> 아래 우선순위에 맞춰 `practice/`(유형별 실전)와 `problems/`(랭크별)를 함께 풀면 된다.

## 1순위 — 무조건 잡아야 하는 유형

1. **구현 / 시뮬레이션** (가장 중요)
   - 지문 길고 조건 많고 배열/좌표/시간/상태가 바뀌는 걸 그대로 코드로.
   - 예: 로봇 이동, 게임판 회전, 블록 제거, 택배/주차/셔틀버스 시간, 문자열 규칙 처리
   - 삼성·카카오·현대/소프티어 단골
2. **DFS / BFS**
   - 예: 섬 개수, 네트워크 개수, 미로 최단거리, 연결 컴포넌트, 감염 전파, 상태 변화 탐색
   - **2차원 배열 + BFS** 거의 필수
3. **완전탐색 / 백트래킹**
   - 예: 순열/조합, 모든 할인 조합, 모든 경로, N개 중 M개, 비밀번호/후보키/메뉴 조합
   - Java면 `visited[]`, `List`, 재귀 백트래킹 연습
4. **정렬 + 조건 처리**
   - 예: 회의실 배정, 파일명 정렬, 로그 정렬, 점수 정렬, 우선순위 기준 정렬
   - Java `Arrays.sort`, `Collections.sort`, `Comparator` 자유롭게
5. **HashMap / HashSet**
   - 예: 중복 체크, 빈도수, 이름-값 매핑, 완주 못한 선수, 보석 쇼핑, 신고 결과
   - Java `Map<String,Integer>`, `Set<String>`, `getOrDefault()` 필수

## 2순위 — 합격권이면 꼭

6. **투 포인터 / 슬라이딩 윈도우 / 누적합** — 연속 부분합, 구간 합, 가장 긴 조건 구간
7. **이분탐색 / Parametric Search** — 입국심사, 징검다리, 예산, 최소 시간, 최대 거리
8. **그리디** — 구명보트, 체육복, 단속카메라, 회의실, 최소 비용 선택
9. **DP** — 계단 오르기, 정수 삼각형, 등굣길, 스티커, 도둑질, LIS

## 3순위 — 상위권/고난도

10. **다익스트라 / 최단거리** — 배달, 합승 택시 요금, 미로 탈출 (Java `PriorityQueue<Node>`)
11. **Union-Find** — 섬 연결, 네트워크 연결, 친구 관계, 사이클 판별
12. **Heap / PriorityQueue** — 더 맵게, 디스크 컨트롤러, 이중 우선순위 큐, 스케줄링
13. **트리 / 세그먼트 트리 / 펜윅 트리** — 구간 최대/최소, 구간 합 업데이트, 순위 계산, 대량 쿼리
    - 기본 유형 다 잡고 마지막에. 처음부터 들어가면 비효율.

## 회사별 경향

| 회사/계열 | 자주 나오는 유형 |
|-----------|------------------|
| 삼성 | 구현, 시뮬레이션, BFS/DFS, 배열 회전, 조건 많은 문제 |
| 카카오 | 구현, 문자열, 해시, 그래프, DP, 효율성 테스트 |
| 네이버/라인 | 자료구조, 문자열, 탐색, 구현, 그리디, DP |
| 현대/소프티어 | 구현, 그래프, BFS, 시뮬레이션, 최단거리 |
| 쿠팡/토스/배민 | 구현, 자료구조, 문자열, 효율성, 실무형 사고 |
| 금융/공기업 IT | 구현, SQL, 자료구조 기본, BFS/DFS, 정렬 |

## 추천 학습 순서

```
구현/시뮬레이션 → HashMap/정렬/스택큐 → 완전탐색 → DFS/BFS
→ 투포인터/누적합 → 이분탐색 → 그리디 → DP
→ 다익스트라/Union-Find → 세그먼트트리 등 고급
```

## Java 개발자가 익숙해야 할 것

```java
HashMap<String, Integer> map = new HashMap<>();
map.put(key, map.getOrDefault(key, 0) + 1);

PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);

Arrays.sort(arr);
Collections.sort(list, (a, b) -> a.score - b.score);

Queue<int[]> q = new ArrayDeque<>();
boolean[][] visited = new boolean[n][m];

while (left <= right) {            // 파라메트릭 이분탐색
    long mid = (left + right) / 2;
    if (ok(mid)) { answer = mid; right = mid - 1; }
    else { left = mid + 1; }
}
```

---

# 유형 ↔ 수록 문제 매핑 (커버리지)

`python tools/coverage.py` 로 최신 커버리지를 출력할 수 있다.
유형별 집중 연습은 메인 메뉴의 **"유형별 실전 연습"** 에서 카테고리별로 풀면 된다.

| 유형 | 랭크별(problems) 주요 수록 | 유형별 실전(practice) |
|------|---------------------------|----------------------|
| 구현/시뮬레이션 | Bronze 전반, Gold 시뮬 | ✅ |
| DFS/BFS | Gold 21~35(섬/단지/토마토/벽부수기) | ✅ |
| 완전탐색/백트래킹 | Gold 26~34(N과 M, N-Queen) | ✅ |
| 정렬 | Silver 06~20 | ✅ |
| 해시 | Silver 21~35 | ✅ |
| 투포인터/누적합 | Silver 36~50, Gold 36~50 | ✅ |
| 이분탐색 | Silver 06~20(나무/랜선), Gold | ✅ |
| 그리디 | Silver 36~50 | ✅ |
| DP | Gold 06~20, Platinum 06~20 | ✅ |
| 다익스트라/최단경로 | Platinum 02, Gold 36~50 | ✅ |
| 유니온파인드 | Gold 36~50 | ✅ |
| 힙/우선순위큐 | Silver 21~35, Gold | ✅ |
| 세그먼트트리 | Platinum 04, 21~35 | ✅ |
| SQL (SQLD 수준) | — | ✅ sql-01~50 (기초 함정/집계·JOIN/서브쿼리·윈도우) |

---

# 코드 작업 시 참고 (for future edits)

- 문제는 전부 `engine.models.Problem` 데이터로 정의된다. 새 문제는 해당 리스트에 `Problem(...)` 추가만 하면 메뉴에 자동 반영.
- `problems/__init__.py` 가 base + `batches/` + `meta/` 를 자동 수집한다.
- `practice/__init__.py` 가 `categories/` 를 자동 수집한다.
- 정답 코드(`reference_py`)는 **반드시** 자기 `testcases` 를 통과해야 한다 — 추가/수정 후 `python tools/selftest.py` 와 `python tools/verify_batch.py <파일>` 로 검증.
- 채점은 표준입출력(stdin)형은 Python/Java/C++ 모두, 함수형(func)은 Python만, SQL형(sql)은 내장 sqlite.
- SQL 문제는 `practice/sqlbank/batch_*.py` 에 정의하고 `practice/categories/sql.py` 가 import 시 `reference_sql` 을 실행해 기대 출력을 자동 계산한다(기대값-정답 불일치 원천 차단). 새 SQL 문제는 reference_sql 에 ORDER BY 필수 + 정렬 유일성 보장.
- C++ 채점은 `g++` 필요(미설치 시 자동 비활성). 자바는 javac 와 같은 JDK 의 java 를 사용(구버전 JRE 회피).

---

# 데이터분석 트랙 (`datasci/`) — 작업 규칙

Python 전용 학습 트랙. 코딩테스트 트랙과 **점수·랭크·시험이 섞이지 않게** 분리되어 있다.
`gui.py` 의 `_all_problems` 에 넣지 말 것 (랭크 점수·종목 분류·모의고사 출제에서 제외).
트리 갱신용으로만 `_ds_problems` 에 따로 담는다.

## 구조

```
datasci/
  __init__.py        STAGES(5단계) 정의 + content/·bank/ 자동 수집
  content/*.py       LESSONS = [Lesson(lang="datasci", level=<단계명>, ...)]
  bank/*.py          PROBLEMS = [Problem(type="func", category=<단계명>, ...)]
```

파일만 추가하면 메뉴에 자동 반영된다. `level`/`category` 는 `STAGES` 의 값과 정확히 일치해야 한다
(안 맞으면 stderr 경고를 내고 조용히 빠진다).
동결(PyInstaller) 환경 대비용 fallback 목록이 `__init__.py` 의 `_CONTENT_MODULES`/`_BANK_MODULES` 에
있으므로, **새 모듈 파일을 추가하면 이 목록에도 넣어야 한다.**

## 강의 작성 규칙 — 실행 결과와 설명이 반드시 일치해야 한다

이 트랙의 강의는 코드를 실행해 출력을 보며 배우는 구조다.
따라서 **설명에 쓴 주장이 실제 출력과 다르면 그 자체가 버그다.**
실제로 초안에서 아래 같은 불일치가 여럿 잡혔다.

- "차수가 오를수록 검증 오차가 는다" → 실제로는 U자(차수 5가 최적)였다
- "깊이를 늘리면 검증 정확도가 꺾인다" → 실제로는 안 꺾여서 데이터를 바꿔 재현시켰다
- "멀어질수록 위치 유사도가 떨어진다" → 삼각함수 주기성 탓에 단조 감소가 아니었다
- 데이터 누수 시연이 올바른 방법과 **완전히 같은 값**을 내 요점을 시연하지 못했다

그래서 강의를 추가·수정한 뒤에는 반드시 **출력을 눈으로 확인**한다.
수치를 본문에 인용했다면 그 숫자가 실제로 나오는지도 확인한다.

## 문제 작성 규칙 (채점 엔진 제약에서 나온 것 — 어기면 반드시 오답 처리됨)

- `type="func"` 고정. → 자동으로 Python 전용 채점이 되고 언어 버튼이 잠긴다.
- 인자(args)는 **JSON 직렬화**되므로 list/dict/int/float/str/None 만 가능.
  numpy 배열·DataFrame 을 인자로 넘길 수 없다 → 리스트로 주고 함수 안에서 변환한다.
- 반환값은 **repr() 문자열로 비교**한다. numpy 스칼라를 그대로 돌려주면
  repr 이 `np.float64(3.0)` 이 되어 오답이다 → `float()`/`int()`/`tolist()` 로 변환 필수.
- 실수 결과는 부동소수점 오차를 피하려고 문제에서 **반올림 자리수를 명시**한다.
- `std()` 의 기본 ddof 가 numpy(0)와 pandas(1)에서 다르다. 문제 지문에 어느 쪽인지 반드시 적는다.
- 제한값은 `datasci/__init__.py` 가 5000ms / 512MB 로 채운다
  (pandas import 실측 ≈ 1.9초 / 68MB — 기본값 2000ms 로는 빠듯하다).
- **정렬·순위가 유일하게 정해지도록** 테스트케이스를 만든다.
  `argsort` 는 동점일 때 순서가 보장되지 않아 채점이 흔들린다(SQL 문제의 ORDER BY 규칙과 같은 취지).
- `round()` 결과가 `-0.0` 이 되면 repr 이 `'-0.0'` 이라 `0.0` 과 불일치한다.
  reference 에서 `round(x, n) + 0.0` 으로 정규화한다.

## 테스트케이스는 오답을 실제로 걸러내야 한다

전부 통과하는지만 보는 것은 검증의 절반이다.
**틀린 구현을 넣었을 때 실패하는지**까지 확인해야 테스트가 제 역할을 한다.
실제로 이 검사에서 두 문제가 취약한 것으로 드러나 케이스를 보강했다.

- `dsq4-01` : 입력값이 작아 softmax 오버플로 방지를 빼먹어도 통과했다
  → `[800, 801, 802]` 추가 (방지 없으면 `nan`)
- `dsq4-03` : 확률 0 인 케이스가 없어 `clip` 을 빼먹어도 통과했다
  → `[[0.0, 1.0]], [0]` 추가 (clip 없으면 `-inf`)

새 문제를 추가하면 "이 문제에서 초보자가 빠지기 쉬운 실수"를 하나 정하고,
그 실수를 주입했을 때 실제로 오답이 나오는지 확인하자.

## 검증

```bash
python tools/verify_datasci.py             # 강의 코드 실행 + 문제 채점 전부
python tools/verify_datasci.py --lessons   # 강의 코드만
python tools/verify_datasci.py --problems  # 문제만
```

`tools/selftest.py` 도 데이터분석 문제를 함께 채점한다(numpy/pandas 없으면 자동 SKIP).
**기대값을 손으로 계산해 넣지 말 것.** 반드시 verify 를 돌려 실제 값과 대조한다.

## 의존성

numpy·pandas 가 필요하다. 없으면 앱은 정상 동작하고 해당 강의를 열 때 설치 안내만 뜬다.
배포(PyInstaller) 시에는 `runtime/python/` 의 embeddable python 에 따로 설치해야 한다 — `BUILD.md` 3-1 참고.
