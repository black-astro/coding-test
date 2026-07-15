"""알고리즘 템플릿 스니펫 — 에디터 우클릭 '템플릿 삽입' 메뉴 데이터.

SNIPPETS[lang] = [(이름, 코드), ...]
코드는 커서 위치에 그대로 삽입된다 (완성형 뼈대 — 문제에 맞게 수정해서 사용).
"""

SNIPPETS = {
    "python": [
        ("빠른 입력 (sys.stdin)", """import sys
input = sys.stdin.readline
"""),
        ("BFS (2차원 격자)", """from collections import deque

def bfs(grid, n, m, sy, sx):
    dist = [[-1] * m for _ in range(n)]
    dist[sy][sx] = 0
    q = deque([(sy, sx)])
    while q:
        y, x = q.popleft()
        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and dist[ny][nx] == -1 and grid[ny][nx] == 1:
                dist[ny][nx] = dist[y][x] + 1
                q.append((ny, nx))
    return dist
"""),
        ("DFS (재귀 + 방문 체크)", """import sys
sys.setrecursionlimit(10 ** 6)

def dfs(v, graph, visited):
    visited[v] = True
    for nxt in graph[v]:
        if not visited[nxt]:
            dfs(nxt, graph, visited)
"""),
        ("이분탐색 (파라메트릭)", """def ok(mid):
    # mid 가 조건을 만족하면 True
    return True

lo, hi, ans = 1, 10 ** 9, 0
while lo <= hi:
    mid = (lo + hi) // 2
    if ok(mid):
        ans = mid
        hi = mid - 1        # 최솟값 탐색(최댓값이면 lo = mid + 1)
    else:
        lo = mid + 1
"""),
        ("우선순위 큐 (heapq)", """import heapq

pq = []                       # (우선순위, 값)
heapq.heappush(pq, (3, "c"))
heapq.heappush(pq, (1, "a"))
while pq:
    prio, val = heapq.heappop(pq)
"""),
        ("Union-Find", """parent = list(range(n + 1))

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb:
        parent[rb] = ra
"""),
        ("투 포인터 (연속 부분합)", """left = total = cnt = 0
for right in range(n):
    total += arr[right]
    while total > target:
        total -= arr[left]
        left += 1
    if total == target:
        cnt += 1
"""),
        ("누적합 (구간 합)", """prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + arr[i]
# 구간 [l, r] 합 (1-indexed): prefix[r] - prefix[l - 1]
"""),
        ("다익스트라", """import heapq

def dijkstra(start, graph, n):
    INF = float("inf")
    dist = [INF] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, v = heapq.heappop(pq)
        if d > dist[v]:
            continue
        for nxt, w in graph[v]:
            nd = d + w
            if nd < dist[nxt]:
                dist[nxt] = nd
                heapq.heappush(pq, (nd, nxt))
    return dist
"""),
        ("백트래킹 (조합/순열)", """def backtrack(picked, start):
    if len(picked) == m:
        print(*picked)
        return
    for i in range(start, n + 1):          # 순열이면 start 대신 1 + used[] 체크
        picked.append(i)
        backtrack(picked, i + 1)
        picked.pop()

backtrack([], 1)
"""),
    ],
    "java": [
        ("빠른 입력 (BufferedReader)", """BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
StringTokenizer st = new StringTokenizer(br.readLine());
int n = Integer.parseInt(st.nextToken());
"""),
        ("BFS (2차원 격자)", """static int[] dy = {-1, 1, 0, 0}, dx = {0, 0, -1, 1};

static int[][] bfs(int[][] grid, int n, int m, int sy, int sx) {
    int[][] dist = new int[n][m];
    for (int[] row : dist) Arrays.fill(row, -1);
    ArrayDeque<int[]> q = new ArrayDeque<>();
    dist[sy][sx] = 0;
    q.add(new int[]{sy, sx});
    while (!q.isEmpty()) {
        int[] cur = q.poll();
        for (int d = 0; d < 4; d++) {
            int ny = cur[0] + dy[d], nx = cur[1] + dx[d];
            if (ny >= 0 && ny < n && nx >= 0 && nx < m
                    && dist[ny][nx] == -1 && grid[ny][nx] == 1) {
                dist[ny][nx] = dist[cur[0]][cur[1]] + 1;
                q.add(new int[]{ny, nx});
            }
        }
    }
    return dist;
}
"""),
        ("DFS (재귀)", """static void dfs(int v, List<List<Integer>> graph, boolean[] visited) {
    visited[v] = true;
    for (int nxt : graph.get(v)) {
        if (!visited[nxt]) dfs(nxt, graph, visited);
    }
}
"""),
        ("이분탐색 (파라메트릭)", """long lo = 1, hi = 1_000_000_000L, ans = 0;
while (lo <= hi) {
    long mid = (lo + hi) / 2;
    if (ok(mid)) { ans = mid; hi = mid - 1; }   // 최솟값(최댓값이면 lo = mid + 1)
    else lo = mid + 1;
}
"""),
        ("우선순위 큐", """PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
pq.offer(new int[]{3, 1});
while (!pq.isEmpty()) {
    int[] top = pq.poll();
}
"""),
        ("Union-Find", """static int[] parent;

static int find(int x) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

static void union(int a, int b) {
    int ra = find(a), rb = find(b);
    if (ra != rb) parent[rb] = ra;
}
"""),
        ("다익스트라", """static long[] dijkstra(int start, List<List<int[]>> graph, int n) {
    long[] dist = new long[n + 1];
    Arrays.fill(dist, Long.MAX_VALUE);
    dist[start] = 0;
    PriorityQueue<long[]> pq = new PriorityQueue<>((a, b) -> Long.compare(a[0], b[0]));
    pq.offer(new long[]{0, start});
    while (!pq.isEmpty()) {
        long[] cur = pq.poll();
        if (cur[0] > dist[(int) cur[1]]) continue;
        for (int[] e : graph.get((int) cur[1])) {   // e = {다음 정점, 가중치}
            long nd = cur[0] + e[1];
            if (nd < dist[e[0]]) {
                dist[e[0]] = nd;
                pq.offer(new long[]{nd, e[0]});
            }
        }
    }
    return dist;
}
"""),
        ("백트래킹 (조합)", """static int n, m;
static int[] picked;

static void backtrack(int depth, int start) {
    if (depth == m) {
        // picked 사용
        return;
    }
    for (int i = start; i <= n; i++) {
        picked[depth] = i;
        backtrack(depth + 1, i + 1);
    }
}
"""),
    ],
    "cpp": [
        ("빠른 입출력", """ios_base::sync_with_stdio(false);
cin.tie(nullptr);
"""),
        ("BFS (2차원 격자)", """int dy[4] = {-1, 1, 0, 0}, dx[4] = {0, 0, -1, 1};
vector<vector<int>> dist(n, vector<int>(m, -1));
queue<pair<int, int>> q;
dist[sy][sx] = 0;
q.push({sy, sx});
while (!q.empty()) {
    auto [y, x] = q.front(); q.pop();
    for (int d = 0; d < 4; d++) {
        int ny = y + dy[d], nx = x + dx[d];
        if (ny >= 0 && ny < n && nx >= 0 && nx < m
                && dist[ny][nx] == -1 && grid[ny][nx] == 1) {
            dist[ny][nx] = dist[y][x] + 1;
            q.push({ny, nx});
        }
    }
}
"""),
        ("이분탐색 (파라메트릭)", """long long lo = 1, hi = 1e9, ans = 0;
while (lo <= hi) {
    long long mid = (lo + hi) / 2;
    if (ok(mid)) { ans = mid; hi = mid - 1; }   // 최솟값(최댓값이면 lo = mid + 1)
    else lo = mid + 1;
}
"""),
        ("우선순위 큐 (최소 힙)", """priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
pq.push({3, 1});
while (!pq.empty()) {
    auto [prio, val] = pq.top(); pq.pop();
}
"""),
        ("Union-Find", """vector<int> parent;

int find(int x) {
    while (parent[x] != x) x = parent[x] = parent[parent[x]];
    return x;
}

void unite(int a, int b) {
    int ra = find(a), rb = find(b);
    if (ra != rb) parent[rb] = ra;
}
"""),
        ("다익스트라", """vector<long long> dijkstra(int start, vector<vector<pair<int, int>>>& g, int n) {
    const long long INF = 4e18;
    vector<long long> dist(n + 1, INF);
    dist[start] = 0;
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> pq;
    pq.push({0, start});
    while (!pq.empty()) {
        auto [d, v] = pq.top(); pq.pop();
        if (d > dist[v]) continue;
        for (auto [nxt, w] : g[v]) {
            if (d + w < dist[nxt]) {
                dist[nxt] = d + w;
                pq.push({dist[nxt], nxt});
            }
        }
    }
    return dist;
}
"""),
    ],
    "javascript": [
        ("표준입력 전체 읽기", """const lines = require('fs').readFileSync(0, 'utf8').trim().split('\\n');
"""),
        ("BFS (2차원 격자)", """function bfs(grid, n, m, sy, sx) {
    const dist = Array.from({length: n}, () => Array(m).fill(-1));
    const q = [[sy, sx]];
    dist[sy][sx] = 0;
    let head = 0;
    const dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    while (head < q.length) {
        const [y, x] = q[head++];
        for (const [dy, dx] of dirs) {
            const ny = y + dy, nx = x + dx;
            if (ny >= 0 && ny < n && nx >= 0 && nx < m
                    && dist[ny][nx] === -1 && grid[ny][nx] === 1) {
                dist[ny][nx] = dist[y][x] + 1;
                q.push([ny, nx]);
            }
        }
    }
    return dist;
}
"""),
        ("이분탐색 (파라메트릭)", """let lo = 1, hi = 1e9, ans = 0;
while (lo <= hi) {
    const mid = Math.floor((lo + hi) / 2);
    if (ok(mid)) { ans = mid; hi = mid - 1; }   // 최솟값(최댓값이면 lo = mid + 1)
    else lo = mid + 1;
}
"""),
        ("Union-Find", """const parent = Array.from({length: n + 1}, (_, i) => i);

function find(x) {
    while (parent[x] !== x) x = parent[x] = parent[parent[x]];
    return x;
}

function union(a, b) {
    const ra = find(a), rb = find(b);
    if (ra !== rb) parent[rb] = ra;
}
"""),
    ],
    "sql": [
        ("SELECT 기본 뼈대", """SELECT 컬럼1, 컬럼2
FROM 테이블
WHERE 조건
ORDER BY 정렬키;
"""),
        ("GROUP BY 집계", """SELECT 그룹컬럼, COUNT(*) AS cnt
FROM 테이블
GROUP BY 그룹컬럼
HAVING COUNT(*) >= 2
ORDER BY cnt DESC, 그룹컬럼;
"""),
        ("JOIN 뼈대", """SELECT a.컬럼, b.컬럼
FROM A a
JOIN B b ON a.id = b.a_id
WHERE 조건
ORDER BY a.id;
"""),
        ("윈도우 함수 (순위)", """SELECT name, score,
       RANK() OVER (ORDER BY score DESC) AS rnk
FROM 테이블
ORDER BY rnk, name;
"""),
    ],
}
