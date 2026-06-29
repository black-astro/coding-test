# CLAUDE.md — 코딩테스트 연습기

이 저장소는 **대한민국 대기업 코딩테스트 대비 연습 도구**다.
Python·Java·C++ 로 풀고, 실행 시간·메모리까지 측정해 실전처럼 채점한다.

## 빠른 시작

```bash
python main.py              # 연습 시작 (랭크별 + 유형별 실전)
python tools/selftest.py    # 모든 정답 코드 무결성 검증
```

## 구성 요약

- **랭크별 문제**: 브론즈~플래티넘 각 50문제(총 200). `problems/`
- **유형별 실전 문제**: 대기업 빈출 유형별 묶음. `practice/`
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

---

# 코드 작업 시 참고 (for future edits)

- 문제는 전부 `engine.models.Problem` 데이터로 정의된다. 새 문제는 해당 리스트에 `Problem(...)` 추가만 하면 메뉴에 자동 반영.
- `problems/__init__.py` 가 base + `batches/` + `meta/` 를 자동 수집한다.
- `practice/__init__.py` 가 `categories/` 를 자동 수집한다.
- 정답 코드(`reference_py`)는 **반드시** 자기 `testcases` 를 통과해야 한다 — 추가/수정 후 `python tools/selftest.py` 와 `python tools/verify_batch.py <파일>` 로 검증.
- 채점은 표준입출력(stdin)형은 Python/Java/C++ 모두, 함수형(func)은 Python만.
- C++ 채점은 `g++` 필요(미설치 시 자동 비활성). 자바는 javac 와 같은 JDK 의 java 를 사용(구버전 JRE 회피).
