"""커버리지 보강 36문제(gap_graph/gap_dp/gap_impl) C++ 정답 코드.

검증된 Java/Python 정답을 C++(g++ -std=c++17)로 번역한 것.
- type=="stdin": 표준입력/표준출력 완전한 int main() 프로그램.
- type=="func":  프로그래머스식 함수 구현형(참고용).
"""

CPP = {
    # ---------------- gap_dp ----------------
    "gd-01": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
long long solution(int n){
    vector<long long> dp(n + 2, 0);   // 경우의 수는 커질 수 있으므로 long long
    dp[0] = 1; dp[1] = 1;
    for (int i = 2; i <= n; i++)
        dp[i] = dp[i - 1] + dp[i - 2];   // 피보나치형 점화식
    return dp[n];
}
''',
    "gd-02": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    vector<int> dp(n, 0);
    dp[0] = a[0];
    if (n >= 2) dp[1] = a[0] + a[1];
    if (n >= 3) dp[2] = max(a[2] + a[1], max(a[2] + a[0], dp[1]));
    // 연속 3잔 금지: 직전을 안 마시거나, 2연속/1잔 패턴 선택
    for (int i = 3; i < n; i++)
        dp[i] = max(dp[i - 1], max(dp[i - 2] + a[i], dp[i - 3] + a[i - 1] + a[i]));
    cout << dp[n - 1] << "\n";
    return 0;
}
''',
    "gd-03": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
long long solution(int n, int m){
    vector<vector<long long>> dp(n, vector<long long>(m, 0));
    for (int i = 0; i < n; i++) dp[i][0] = 1;   // 첫 열은 경로 1가지
    for (int j = 0; j < m; j++) dp[0][j] = 1;   // 첫 행은 경로 1가지
    for (int i = 1; i < n; i++)
        for (int j = 1; j < m; j++)
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1];   // 위 + 왼쪽
    return dp[n - 1][m - 1];
}
''',
    "gd-04": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
int solution(vector<vector<int>> grid){
    int n = grid.size(), m = grid[0].size();
    const int NEG = INT_MIN;
    vector<vector<int>> dp(n, vector<int>(m, NEG));
    if (grid[0][0] == -1) return -1;   // 시작점이 막혔으면 불가
    dp[0][0] = grid[0][0];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == -1 || (i == 0 && j == 0)) continue;
            int best = NEG;
            if (i > 0 && dp[i - 1][j] != NEG) best = max(best, dp[i - 1][j]);
            if (j > 0 && dp[i][j - 1] != NEG) best = max(best, dp[i][j - 1]);
            if (best != NEG) dp[i][j] = best + grid[i][j];
        }
    return dp[n - 1][m - 1] != NEG ? dp[n - 1][m - 1] : -1;
}
''',
    "gd-05": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
bool solution(vector<int> nums, int target){
    vector<char> possible(target + 1, false);   // possible[s]: 합 s 가능 여부
    possible[0] = true;
    for (int x : nums) {
        if (x > target) continue;
        for (int s = target; s >= x; s--)        // 0/1 배낭식 역순 갱신
            if (possible[s - x]) possible[s] = true;
    }
    return possible[target];
}
''',
    "gd-06": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, k; cin >> n >> k;
    vector<int> coins(n);
    for (int i = 0; i < n; i++) cin >> coins[i];
    const int INF = 1 << 29;
    vector<int> dp(k + 1, INF);
    dp[0] = 0;
    for (int c : coins)
        for (int a = c; a <= k; a++)             // 무한 동전: 정방향 갱신
            if (dp[a - c] + 1 < dp[a]) dp[a] = dp[a - c] + 1;
    cout << (dp[k] != INF ? dp[k] : -1) << "\n";
    return 0;
}
''',
    "gd-07": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
int solution(vector<int> nums, int target){
    int n = nums.size(), count = 0;
    for (int mask = 0; mask < (1 << n); mask++) {   // 모든 부분집합 비트마스크
        int s = 0;
        for (int i = 0; i < n; i++)
            if (mask & (1 << i)) s += nums[i];
        if (s == target) count++;
    }
    return count;
}
''',
    "gd-08": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
int solution(vector<vector<int>> cost){
    int n = cost.size();
    const int INF = 1 << 29;
    vector<int> dp(1 << n, INF);   // dp[mask]: 배정된 일 집합 mask 의 최소 비용
    dp[0] = 0;
    for (int mask = 0; mask < (1 << n); mask++) {
        if (dp[mask] == INF) continue;
        int i = __builtin_popcount(mask);   // 다음 배정할 작업 인덱스
        if (i >= n) continue;
        for (int j = 0; j < n; j++) {
            if (mask & (1 << j)) continue;
            int nm = mask | (1 << j);
            int v = dp[mask] + cost[i][j];
            if (v < dp[nm]) dp[nm] = v;
        }
    }
    return dp[(1 << n) - 1];
}
''',
    "gd-09": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, q; cin >> n >> q;
    vector<long long> pre(n + 1, 0);   // 누적합
    for (int k = 1; k <= n; k++) {
        long long x; cin >> x;
        pre[k] = pre[k - 1] + x;
    }
    string sb;
    for (int t = 0; t < q; t++) {
        int i, j; cin >> i >> j;
        sb += to_string(pre[j] - pre[i - 1]);   // [i, j] 구간 합
        sb += '\n';
    }
    cout << sb;
    return 0;
}
''',
    "gd-10": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, m; cin >> n >> m;
    vector<vector<long long>> pre(n + 1, vector<long long>(m + 1, 0));
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++) {
            long long v; cin >> v;
            // 2차원 누적합: 포함-배제
            pre[i][j] = v + pre[i - 1][j] + pre[i][j - 1] - pre[i - 1][j - 1];
        }
    int q; cin >> q;
    string sb;
    for (int t = 0; t < q; t++) {
        int r1, c1, r2, c2; cin >> r1 >> c1 >> r2 >> c2;
        long long s = pre[r2][c2] - pre[r1 - 1][c2] - pre[r2][c1 - 1] + pre[r1 - 1][c1 - 1];
        sb += to_string(s);
        sb += '\n';
    }
    cout << sb;
    return 0;
}
''',
    "gd-11": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
static long long g_m, g_a;
long long power_dc(long long e){   // 분할 정복 거듭제곱
    if (e == 0) return 1 % g_m;
    long long h = power_dc(e / 2);
    h = h * h % g_m;
    if (e % 2 == 1) h = h * (g_a % g_m) % g_m;
    return h;
}
long long solution(long long a, long long b, long long m){
    g_a = a; g_m = m;
    return power_dc(b);
}
''',
    "gd-12": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
int solution(vector<int> nums){
    int n = nums.size() + 2;
    vector<int> a(n, 0);
    a[0] = 1; a[n - 1] = 1;                       // 양 끝에 가상의 1 추가
    for (int i = 0; i < (int)nums.size(); i++) a[i + 1] = nums[i];
    vector<vector<int>> dp(n, vector<int>(n, 0));   // dp[l][r]: (l, r) 구간 최대 점수
    for (int len = 2; len < n; len++)
        for (int left = 0; left + len < n; left++) {
            int right = left + len, best = 0;
            for (int k = left + 1; k < right; k++) {   // 마지막에 터뜨릴 풍선 k
                int v = a[left] * a[k] * a[right] + dp[left][k] + dp[k][right];
                if (v > best) best = v;
            }
            dp[left][right] = best;
        }
    return dp[0][n - 1];
}
''',

    # ---------------- gap_graph ----------------
    "gg-01": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int r, c; cin >> r >> c;
    vector<vector<int>> g(r, vector<int>(c)), dist(r, vector<int>(c, -1));
    queue<pair<int,int>> q;
    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++) {
            cin >> g[i][j];
            if (g[i][j] == 1) { dist[i][j] = 0; q.push({i, j}); }   // 익은 토마토에서 BFS 시작
        }
    int ans = 0;
    int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};
    while (!q.empty()) {
        auto [x, y] = q.front(); q.pop();
        for (int d = 0; d < 4; d++) {
            int nx = x + dx[d], ny = y + dy[d];
            if (nx >= 0 && nx < r && ny >= 0 && ny < c && dist[nx][ny] == -1) {
                dist[nx][ny] = dist[x][y] + 1;
                ans = max(ans, dist[nx][ny]);
                q.push({nx, ny});
            }
        }
    }
    cout << ans << "\n";
    return 0;
}
''',
    "gg-02": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int r, c; cin >> r >> c;
    vector<vector<int>> g(r, vector<int>(c)), dist(r, vector<int>(c, -1));
    queue<pair<int,int>> q;
    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++) {
            cin >> g[i][j];
            if (g[i][j] == 1) { dist[i][j] = 0; q.push({i, j}); }
        }
    int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};
    while (!q.empty()) {
        auto [x, y] = q.front(); q.pop();
        for (int d = 0; d < 4; d++) {
            int nx = x + dx[d], ny = y + dy[d];
            if (nx >= 0 && nx < r && ny >= 0 && ny < c && g[nx][ny] == 0 && dist[nx][ny] == -1) {
                dist[nx][ny] = dist[x][y] + 1;
                q.push({nx, ny});
            }
        }
    }
    int ans = 0;
    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++) {
            if (g[i][j] == 0 && dist[i][j] == -1) { cout << -1 << "\n"; return 0; }   // 못 익는 칸 존재
            ans = max(ans, dist[i][j]);
        }
    cout << ans << "\n";
    return 0;
}
''',
    "gg-03": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, m; cin >> n >> m;
    vector<vector<int>> adj(n + 1);
    vector<int> indeg(n + 1, 0);
    for (int i = 0; i < m; i++) {
        int a, b; cin >> a >> b;
        adj[a].push_back(b);
        indeg[b]++;
    }
    priority_queue<int, vector<int>, greater<int>> pq;   // 진입차수 0 중 가장 작은 번호 우선
    for (int i = 1; i <= n; i++) if (indeg[i] == 0) pq.push(i);
    string sb;
    while (!pq.empty()) {
        int x = pq.top(); pq.pop();
        sb += to_string(x);
        sb += ' ';
        for (int y : adj[x]) if (--indeg[y] == 0) pq.push(y);
    }
    if (!sb.empty() && sb.back() == ' ') sb.pop_back();   // 끝 공백 제거
    cout << sb << "\n";
    return 0;
}
''',
    "gg-04": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; cin >> n;
    vector<int> tcost(n + 1, 0);
    vector<vector<int>> adj(n + 1);
    vector<int> indeg(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        cin >> tcost[i];
        int v;
        while (cin >> v && v != -1) {   // 선행 건물 목록은 -1 로 종료
            adj[v].push_back(i);
            indeg[i]++;
        }
    }
    vector<int> dp(n + 1, 0), res(n + 1, 0);
    queue<int> q;
    for (int i = 1; i <= n; i++) if (indeg[i] == 0) q.push(i);
    while (!q.empty()) {
        int x = q.front(); q.pop();
        res[x] = dp[x] + tcost[x];
        for (int y : adj[x]) {
            if (res[x] > dp[y]) dp[y] = res[x];   // 가장 늦게 끝나는 선행에 맞춤
            if (--indeg[y] == 0) q.push(y);
        }
    }
    string sb;
    for (int i = 1; i <= n; i++) { sb += to_string(res[i]); sb += '\n'; }
    cout << sb;
    return 0;
}
''',
    "gg-05": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
vector<int> solution(int n, vector<vector<int>> edges, int start){
    vector<vector<pair<int,int>>> adj(n);
    for (auto& e : edges) adj[e[0]].push_back({e[1], e[2]});
    const long long INF = LLONG_MAX / 4;
    vector<long long> dist(n, INF);
    dist[start] = 0;
    priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<>> pq;
    pq.push({0, start});
    while (!pq.empty()) {                       // 다익스트라
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue;
        for (auto& e : adj[u]) {
            long long nd = d + e.second;
            if (nd < dist[e.first]) { dist[e.first] = nd; pq.push({nd, e.first}); }
        }
    }
    vector<int> res(n);
    for (int i = 0; i < n; i++) res[i] = (dist[i] == INF) ? -1 : (int)dist[i];
    return res;
}
''',
    "gg-06": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int v, e; cin >> v >> e;
    int k; cin >> k;
    vector<vector<pair<int,int>>> adj(v + 1);
    for (int i = 0; i < e; i++) {
        int a, b, w; cin >> a >> b >> w;
        adj[a].push_back({b, w});
    }
    const long long INF = LLONG_MAX / 4;
    vector<long long> dist(v + 1, INF);
    dist[k] = 0;
    priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<>> pq;
    pq.push({0, k});
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue;
        for (auto& ed : adj[u]) {
            long long nd = d + ed.second;
            if (nd < dist[ed.first]) { dist[ed.first] = nd; pq.push({nd, ed.first}); }
        }
    }
    string sb;
    for (int i = 1; i <= v; i++) {
        sb += (dist[i] == INF ? string("INF") : to_string(dist[i]));   // 도달 불가는 INF
        sb += '\n';
    }
    cout << sb;
    return 0;
}
''',
    "gg-07": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; cin >> n;
    int m; cin >> m;
    const long long INF = LLONG_MAX / 4;
    vector<vector<long long>> d(n + 1, vector<long long>(n + 1, INF));
    for (int i = 1; i <= n; i++) d[i][i] = 0;
    for (int i = 0; i < m; i++) {
        int a, b; long long c; cin >> a >> b >> c;
        if (c < d[a][b]) d[a][b] = c;   // 다중 간선 중 최소
    }
    for (int k = 1; k <= n; k++)        // 플로이드-워셜
        for (int i = 1; i <= n; i++) {
            if (d[i][k] == INF) continue;
            for (int j = 1; j <= n; j++)
                if (d[i][k] + d[k][j] < d[i][j]) d[i][j] = d[i][k] + d[k][j];
        }
    string sb;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            sb += (d[i][j] == INF ? string("0") : to_string(d[i][j]));   // 도달 불가는 0
            if (j < n) sb += ' ';
        }
        sb += '\n';
    }
    cout << sb;
    return 0;
}
''',
    "gg-08": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
static vector<int> g_parent;
static int dsu_find(int x){
    while (g_parent[x] != x) { g_parent[x] = g_parent[g_parent[x]]; x = g_parent[x]; }
    return x;
}
int solution(int n, vector<vector<int>> edges){
    g_parent.assign(n, 0);
    for (int i = 0; i < n; i++) g_parent[i] = i;
    for (auto& e : edges) {
        int ra = dsu_find(e[0]), rb = dsu_find(e[1]);
        if (ra != rb) g_parent[ra] = rb;   // 합치기
    }
    set<int> roots;
    for (int i = 0; i < n; i++) roots.insert(dsu_find(i));
    return (int)roots.size();   // 서로 다른 루트 개수 = 묶음 수
}
''',
    "gg-09": r'''#include <bits/stdc++.h>
using namespace std;
static vector<int> g_parent;
static int dsu_find(int x){
    while (g_parent[x] != x) { g_parent[x] = g_parent[g_parent[x]]; x = g_parent[x]; }
    return x;
}
int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int v, e; cin >> v >> e;
    vector<array<int,3>> edges(e);   // {가중치, a, b}
    for (int i = 0; i < e; i++) {
        int a, b, w; cin >> a >> b >> w;
        edges[i] = {w, a, b};
    }
    sort(edges.begin(), edges.end(),
         [](const array<int,3>& p, const array<int,3>& q){ return p[0] < q[0]; });
    g_parent.assign(v + 1, 0);
    for (int i = 0; i <= v; i++) g_parent[i] = i;
    long long total = 0;
    for (auto& ed : edges) {   // 크루스칼 MST
        int ra = dsu_find(ed[1]), rb = dsu_find(ed[2]);
        if (ra != rb) { g_parent[ra] = rb; total += ed[0]; }
    }
    cout << total << "\n";
    return 0;
}
''',
    "gg-10": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, m; cin >> n >> m;
    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; i++) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    vector<char> visited(n + 1, false);
    int cnt = 0;
    for (int s = 1; s <= n; s++) {
        if (!visited[s]) {
            cnt++;                       // 새 연결 요소 발견
            stack<int> stk; stk.push(s); visited[s] = true;
            while (!stk.empty()) {
                int x = stk.top(); stk.pop();
                for (int y : adj[x]) if (!visited[y]) { visited[y] = true; stk.push(y); }
            }
        }
    }
    cout << cnt << "\n";
    return 0;
}
''',
    "gg-11": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int r, c; cin >> r >> c;
    vector<string> g(r);
    for (int i = 0; i < r; i++) cin >> g[i];
    const int INF = INT_MAX / 4;
    vector<vector<int>> dist(r, vector<int>(c, INF));
    dist[0][0] = 0;
    deque<pair<int,int>> dq;
    dq.push_back({0, 0});
    int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};
    while (!dq.empty()) {                 // 0-1 BFS
        auto [x, y] = dq.front(); dq.pop_front();
        for (int d = 0; d < 4; d++) {
            int nx = x + dx[d], ny = y + dy[d];
            if (nx >= 0 && nx < r && ny >= 0 && ny < c) {
                int w = g[nx][ny] == '1' ? 1 : 0;   // 벽이면 비용 1
                if (dist[x][y] + w < dist[nx][ny]) {
                    dist[nx][ny] = dist[x][y] + w;
                    if (w == 0) dq.push_front({nx, ny});
                    else dq.push_back({nx, ny});
                }
            }
        }
    }
    cout << dist[r - 1][c - 1] << "\n";
    return 0;
}
''',
    "gg-12": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
static vector<vector<int>> g_adj;
static vector<char> g_visited;
static int g_end, g_cnt;
static void dfs_count(int u){
    if (u == g_end) { g_cnt++; return; }   // 도착하면 경로 1개
    for (int v : g_adj[u]) {
        if (!g_visited[v]) { g_visited[v] = true; dfs_count(v); g_visited[v] = false; }
    }
}
int solution(int n, vector<vector<int>> edges, int start, int end){
    g_adj.assign(n, {});
    for (auto& e : edges) g_adj[e[0]].push_back(e[1]);
    g_visited.assign(n, false);
    g_end = end; g_cnt = 0;
    g_visited[start] = true;
    dfs_count(start);
    return g_cnt;
}
''',

    # ---------------- gap_impl ----------------
    "gi-01": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
vector<vector<int>> solution(int n){
    vector<vector<int>> m(n, vector<int>(n, 0));
    int dr[] = {0, 1, 0, -1}, dc[] = {1, 0, -1, 0};   // 우 하 좌 상
    int r = 0, c = 0, d = 0;
    for (int v = 1; v <= n * n; v++) {
        m[r][c] = v;
        int nr = r + dr[d], nc = c + dc[d];
        if (!(nr >= 0 && nr < n && nc >= 0 && nc < n && m[nr][nc] == 0)) {
            d = (d + 1) % 4;                 // 막히면 방향 전환
            nr = r + dr[d]; nc = c + dc[d];
        }
        r = nr; c = nc;
    }
    return m;
}
''',
    "gi-02": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, m, R; cin >> n >> m >> R;
    vector<vector<int>> a(n, vector<int>(m));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) cin >> a[i][j];
    for (int layer = 0; layer < min(n, m) / 2; layer++) {
        int top = layer, bottom = n - 1 - layer, left = layer, right = m - 1 - layer;
        vector<pair<int,int>> pos;                // 테두리 좌표를 시계방향으로 수집
        for (int c = left; c <= right; c++) pos.push_back({top, c});
        for (int rr = top + 1; rr <= bottom; rr++) pos.push_back({rr, right});
        for (int c = right - 1; c >= left; c--) pos.push_back({bottom, c});
        for (int rr = bottom - 1; rr > top; rr--) pos.push_back({rr, left});
        int L = pos.size();
        vector<int> vals(L);
        for (int i = 0; i < L; i++) vals[i] = a[pos[i].first][pos[i].second];
        int rr = R % L;
        for (int i = 0; i < L; i++) {
            auto p = pos[i];
            a[p.first][p.second] = vals[((i - rr) % L + L) % L];   // R 칸 회전
        }
    }
    string sb;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            sb += to_string(a[i][j]);
            if (j < m - 1) sb += ' ';
        }
        sb += '\n';
    }
    cout << sb;
    return 0;
}
''',
    "gi-03": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
string solution(string s){
    if (s.empty()) return "";
    string sb;
    int i = 0, n = s.size();
    while (i < n) {
        int j = i;
        while (j < n && s[j] == s[i]) j++;   // 같은 문자 구간 끝까지
        sb += s[i];
        sb += to_string(j - i);              // 문자 + 반복 횟수
        i = j;
    }
    return sb;
}
''',
    "gi-04": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    string text, pat;
    getline(cin, text);
    getline(cin, pat);
    int n = text.size(), p = pat.size();
    vector<int> f(p, 0);
    int k = 0;
    for (int i = 1; i < p; i++) {            // 실패 함수 (KMP)
        while (k > 0 && pat[i] != pat[k]) k = f[k - 1];
        if (pat[i] == pat[k]) k++;
        f[i] = k;
    }
    string sb;
    int cnt = 0;
    k = 0;
    for (int i = 0; i < n; i++) {            // 본문 매칭
        while (k > 0 && text[i] != pat[k]) k = f[k - 1];
        if (text[i] == pat[k]) k++;
        if (k == p) {
            cnt++;
            sb += to_string(i - p + 2);      // 1-based 시작 위치
            sb += ' ';
            k = f[k - 1];
        }
    }
    cout << cnt << "\n";
    if (!sb.empty() && sb.back() == ' ') sb.pop_back();
    cout << sb << "\n";
    return 0;
}
''',
    "gi-05": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
long long solution(long long a, long long b, long long m){
    long long result = 1 % m;
    long long base = a % m;
    while (b > 0) {                       // 빠른 거듭제곱
        if (b & 1) result = result * base % m;
        base = base * base % m;
        b >>= 1;
    }
    return result;
}
''',
    "gi-06": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
static long long g_P;
static array<long long,3> egcd(long long a, long long b){   // {gcd, x, y}
    if (b == 0) return {a, 1, 0};
    auto r = egcd(b, a % b);
    return {r[0], r[2], r[1] - (a / b) * r[2]};
}
static long long modinv(long long a){
    auto r = egcd(((a % g_P) + g_P) % g_P, g_P);
    return ((r[1] % g_P) + g_P) % g_P;   // 모듈러 역원
}
long long solution(long long n, long long r, long long p){
    if (r < 0 || r > n) return 0;
    g_P = p;
    long long num = 1, den = 1;
    for (long long i = 0; i < r; i++) {
        num = num * ((n - i) % p) % p;
        den = den * ((i + 1) % p) % p;
    }
    return num * modinv(den) % p;
}
''',
    "gi-07": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; long long M;
    cin >> n >> M;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    int lo = 0, cnt = 0;
    long long s = 0;
    for (int hi = 0; hi < n; hi++) {     // 투 포인터 (양수 배열 가정)
        s += arr[hi];
        while (s > M && lo <= hi) s -= arr[lo++];
        if (s == M) cnt++;
    }
    cout << cnt << "\n";
    return 0;
}
''',
    "gi-08": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
int solution(int s, vector<int> nums){
    int lo = 0, total = 0, best = INT_MAX;
    for (int hi = 0; hi < (int)nums.size(); hi++) {
        total += nums[hi];
        while (total >= s) {                       // 조건 만족 시 왼쪽 좁히기
            best = min(best, hi - lo + 1);
            total -= nums[lo++];
        }
    }
    return best == INT_MAX ? 0 : best;
}
''',
    "gi-09": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    vector<int> ans(n, -1);
    vector<int> stk(n);
    int top = 0;
    for (int i = 0; i < n; i++) {        // 단조 감소 스택으로 오큰수 계산
        while (top > 0 && arr[stk[top - 1]] < arr[i]) ans[stk[--top]] = arr[i];
        stk[top++] = i;
    }
    string sb;
    for (int i = 0; i < n; i++) {
        sb += to_string(ans[i]);
        if (i < n - 1) sb += ' ';
    }
    cout << sb << "\n";
    return 0;
}
''',
    "gi-10": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
vector<int> solution(vector<int> ops){
    // 절댓값이 작은 것, 같으면 값이 작은 것이 먼저 나오는 최소 힙
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    vector<int> res;
    for (int x : ops) {
        if (x != 0) pq.push({abs(x), x});
        else {
            if (pq.empty()) res.push_back(0);
            else { res.push_back(pq.top().second); pq.pop(); }
        }
    }
    return res;
}
''',
    "gi-11": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, M; cin >> n >> M;
    priority_queue<long long, vector<long long>, greater<long long>> pq;   // 최소 힙
    for (int i = 0; i < n; i++) { long long x; cin >> x; pq.push(x); }
    for (int k = 0; k < M; k++) {        // 가장 작은 두 카드 합치기
        long long a = pq.top(); pq.pop();
        long long b = pq.top(); pq.pop();
        pq.push(a + b);
        pq.push(a + b);
    }
    long long sum = 0;
    while (!pq.empty()) { sum += pq.top(); pq.pop(); }
    cout << sum << "\n";
    return 0;
}
''',
    "gi-12": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
long long solution(vector<int> heights){
    int n = heights.size();
    long long best = 0;
    stack<pair<int,int>> st;   // {시작 인덱스, 높이}
    for (int i = 0; i <= n; i++) {
        int x = (i == n) ? 0 : heights[i];
        int start = i;
        while (!st.empty() && st.top().second > x) {
            auto t = st.top(); st.pop();
            best = max(best, (long long)t.second * (i - t.first));   // 넓이 갱신
            start = t.first;
        }
        st.push({start, x});
    }
    return best;
}
''',
}
