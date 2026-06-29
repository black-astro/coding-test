"""플래티넘 50문제 C++ 정답 코드 맵.

검증된 Java/Python 정답을 C++(g++ -std=c++17)로 정확히 번역한 것이다.
- stdin 문제: 완전한 int main() (#include <bits/stdc++.h>)
- func 문제 : 동등한 C++ 함수 (참고용, 채점은 Python 으로만 수행)
long long / 오버플로 / 모듈러 처리에 주의했다.
"""

CPP = {
    # ---------------------------------------------------------------- 01
    "platinum-01": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    // 가장 긴 공통 부분 수열(LCS): dp[i][j] = a[..i], b[..j] 의 LCS 길이
    int solution(const string& a, const string& b) {
        int n = a.size(), m = b.size();
        vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= m; j++)
                if (a[i - 1] == b[j - 1]) dp[i][j] = dp[i - 1][j - 1] + 1;
                else dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
        return dp[n][m];
    }
};
''',

    # ---------------------------------------------------------------- 02
    "platinum-02": r'''#include <bits/stdc++.h>
using namespace std;

// 다익스트라 최단 경로 (시작 정점 -> 모든 정점)
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int v, e, start;
    cin >> v >> e >> start;
    vector<vector<pair<int, int>>> g(v + 1); // (도착, 가중치)
    for (int i = 0; i < e; i++) {
        int a, b, w;
        cin >> a >> b >> w;
        g[a].push_back({b, w});
    }
    const long long INF = LLONG_MAX;
    vector<long long> dist(v + 1, INF);
    dist[start] = 0;
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> pq;
    pq.push({0, start});
    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();
        if (d > dist[u]) continue;
        for (auto [nx, w] : g[u]) {
            long long nd = d + w;
            if (nd < dist[nx]) {
                dist[nx] = nd;
                pq.push({nd, nx});
            }
        }
    }
    string out;
    for (int i = 1; i <= v; i++) {
        if (dist[i] == INF) out += "INF";
        else out += to_string(dist[i]);
        out += '\n';
    }
    cout << out;
    return 0;
}
''',

    # ---------------------------------------------------------------- 03
    "platinum-03": r'''#include <bits/stdc++.h>
using namespace std;

// 줄 세우기: 위상 정렬 (사전순 작은 정점 먼저 -> 최소 힙)
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<vector<int>> g(n + 1);
    vector<int> indeg(n + 1, 0);
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        g[a].push_back(b);
        indeg[b]++;
    }
    priority_queue<int, vector<int>, greater<>> pq;
    for (int i = 1; i <= n; i++) if (indeg[i] == 0) pq.push(i);
    string out;
    while (!pq.empty()) {
        int u = pq.top();
        pq.pop();
        out += to_string(u);
        out += ' ';
        for (int nx : g[u]) if (--indeg[nx] == 0) pq.push(nx);
    }
    if (!out.empty() && out.back() == ' ') out.pop_back();
    cout << out << "\n";
    return 0;
}
''',

    # ---------------------------------------------------------------- 04
    "platinum-04": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

// 질의: op="U" 면 (a=인덱스1based, b=값), 그 외("Q")는 (a=l, b=r)
struct Query { string op; int a, b; };

// 구간 합 세그먼트 트리 (반복식, iterative)
class Solution {
    int sz;
    vector<long long> tree;
    void update(int idx, long long val) {
        int p = sz + idx;
        tree[p] = val;
        p /= 2;
        while (p >= 1) { tree[p] = tree[2 * p] + tree[2 * p + 1]; p /= 2; }
    }
    long long query(int l, int r) {
        long long res = 0;
        l += sz; r += sz + 1;
        while (l < r) {
            if (l & 1) res += tree[l++];
            if (r & 1) res += tree[--r];
            l /= 2; r /= 2;
        }
        return res;
    }
public:
    vector<int> solution(const vector<int>& arr, const vector<Query>& queries) {
        int n = arr.size();
        sz = 1;
        while (sz < n) sz *= 2;
        tree.assign(2 * sz, 0);
        for (int i = 0; i < n; i++) tree[sz + i] = arr[i];
        for (int p = sz - 1; p >= 1; p--) tree[p] = tree[2 * p] + tree[2 * p + 1];
        vector<int> out;
        for (auto& q : queries) {
            if (q.op == "U") update(q.a - 1, q.b);
            else out.push_back((int)query(q.a - 1, q.b - 1));
        }
        return out;
    }
};
''',

    # ---------------------------------------------------------------- 05
    "platinum-05": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    // 동전 2: 무한 개로 target 을 만드는 최소 동전 수 (완전 배낭)
    int solution(const vector<int>& coins, int target) {
        const int INF = 1 << 29;
        vector<int> dp(target + 1, INF);
        dp[0] = 0;
        for (int c : coins)
            for (int k = c; k <= target; k++)
                dp[k] = min(dp[k], dp[k - c] + 1);
        return dp[target] == INF ? -1 : dp[target];
    }
};
''',

    # ---------------------------------------------------------------- 06
    "platinum-06": r'''#include <bits/stdc++.h>
using namespace std;

// 파일 합치기: 구간 DP (matrix-chain 형태). 누적합으로 구간 비용 계산
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<int> a(n);
    for (auto& x : a) cin >> x;
    vector<long long> pre(n + 1, 0);
    for (int i = 0; i < n; i++) pre[i + 1] = pre[i] + a[i];
    const long long INF = LLONG_MAX;
    vector<vector<long long>> dp(n, vector<long long>(n, 0));
    for (int len = 2; len <= n; len++)
        for (int i = 0; i + len - 1 < n; i++) {
            int j = i + len - 1;
            dp[i][j] = INF;
            long long s = pre[j + 1] - pre[i];
            for (int k = i; k < j; k++)
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + s);
        }
    cout << dp[0][n - 1] << "\n";
    return 0;
}
''',

    # ---------------------------------------------------------------- 07
    "platinum-07": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    // 행렬 곱셈 순서(체인): dp[i][j] = i..j 행렬을 곱하는 최소 연산 수
    // p[i-1]*p[k]*p[j] 와 누적합이 int 를 넘을 수 있어 long long 사용
    long long solution(const vector<int>& p) {
        int m = (int)p.size() - 1;
        if (m <= 1) return 0;
        const long long INF = LLONG_MAX;
        vector<vector<long long>> dp(m + 1, vector<long long>(m + 1, 0));
        for (int len = 2; len <= m; len++)
            for (int i = 1; i + len - 1 <= m; i++) {
                int j = i + len - 1;
                dp[i][j] = INF;
                for (int k = i; k < j; k++) {
                    long long cost = dp[i][k] + dp[k + 1][j]
                                   + (long long)p[i - 1] * p[k] * p[j];
                    if (cost < dp[i][j]) dp[i][j] = cost;
                }
            }
        return dp[1][m];
    }
};
''',

    # ---------------------------------------------------------------- 08
    "platinum-08": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

// 트리의 최대 가중 독립 집합 (트리 DP)
class Solution {
    vector<vector<int>> adj;
    vector<int> w;
    vector<long long> dp0, dp1; // dp0: u 미선택, dp1: u 선택
    vector<bool> vis;
    void dfs(int u) {
        vis[u] = true;
        dp1[u] = w[u];
        dp0[u] = 0;
        for (int nx : adj[u]) if (!vis[nx]) {
            dfs(nx);
            dp1[u] += dp0[nx];
            dp0[u] += max(dp0[nx], dp1[nx]);
        }
    }
public:
    long long solution(int n, const vector<pair<int, int>>& edges,
                       const vector<int>& weights) {
        adj.assign(n + 1, {});
        for (auto& e : edges) {
            adj[e.first].push_back(e.second);
            adj[e.second].push_back(e.first);
        }
        w.assign(n + 1, 0);
        for (int i = 0; i < n; i++) w[i + 1] = weights[i];
        dp0.assign(n + 1, 0);
        dp1.assign(n + 1, 0);
        vis.assign(n + 1, false);
        dfs(1);
        return max(dp0[1], dp1[1]);
    }
};
''',

    # ---------------------------------------------------------------- 09
    "platinum-09": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    // 외판원 순회: 비트마스크 DP (dp[mask][u] = mask 방문, 현재 u)
    int solution(const vector<vector<int>>& dist) {
        int n = dist.size();
        if (n == 1) return 0;
        const int INF = 1 << 29;
        vector<vector<int>> dp(1 << n, vector<int>(n, INF));
        dp[1][0] = 0;
        for (int mask = 0; mask < (1 << n); mask++)
            for (int u = 0; u < n; u++) {
                if (dp[mask][u] == INF || !(mask & (1 << u))) continue;
                for (int v = 0; v < n; v++) {
                    if (mask & (1 << v)) continue;
                    int nm = mask | (1 << v);
                    dp[nm][v] = min(dp[nm][v], dp[mask][u] + dist[u][v]);
                }
            }
        int full = (1 << n) - 1, ans = INF;
        for (int u = 0; u < n; u++)
            if (dp[full][u] != INF) ans = min(ans, dp[full][u] + dist[u][0]);
        return ans;
    }
};
''',

    # ---------------------------------------------------------------- 10
    "platinum-10": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    // 두 그룹 최소 차이 분할: 부분집합 합 가능 여부 DP
    int solution(const vector<int>& nums) {
        int total = 0;
        for (int x : nums) total += x;
        vector<char> possible(total + 1, false);
        possible[0] = true;
        for (int x : nums)
            for (int s = total; s >= x; s--)
                if (possible[s - x]) possible[s] = true;
        int best = total;
        for (int s = 0; s <= total; s++)
            if (possible[s]) best = min(best, abs(total - 2 * s));
        return best;
    }
};
''',

    # ---------------------------------------------------------------- 11
    "platinum-11": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

// 자릿수 합이 S 인 1..N 의 수 세기 (자릿수 DP)
class Solution {
    vector<int> digits;
    int L, S;
    vector<vector<vector<int>>> memo; // [pos][tight][sum]
    int go(int pos, int tight, int sum) {
        if (sum > S) return 0;
        if (pos == L) return sum == S ? 1 : 0;
        int& m = memo[pos][tight][sum];
        if (m != -1) return m;
        int limit = tight ? digits[pos] : 9, total = 0;
        for (int d = 0; d <= limit; d++)
            total += go(pos + 1, (tight && d == limit) ? 1 : 0, sum + d);
        return m = total;
    }
public:
    int solution(int N, int S) {
        if (N < 1) return 0;
        this->S = S;
        string s = to_string(N);
        L = s.size();
        digits.assign(L, 0);
        for (int i = 0; i < L; i++) digits[i] = s[i] - '0';
        memo.assign(L, vector<vector<int>>(2, vector<int>(S + 1, -1)));
        int res = go(0, 1, 0);
        if (S == 0) res -= 1; // 0 은 제외
        return res;
    }
};
''',

    # ---------------------------------------------------------------- 12
    "platinum-12": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    // 최장 팰린드롬 부분 수열 (구간 DP)
    int solution(const string& s) {
        int n = s.size();
        if (n == 0) return 0;
        vector<vector<int>> dp(n, vector<int>(n, 0));
        for (int i = 0; i < n; i++) dp[i][i] = 1;
        for (int len = 2; len <= n; len++)
            for (int i = 0; i + len - 1 < n; i++) {
                int j = i + len - 1;
                if (s[i] == s[j]) dp[i][j] = dp[i + 1][j - 1] + 2;
                else dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
            }
        return dp[0][n - 1];
    }
};
''',

    # ---------------------------------------------------------------- 13
    "platinum-13": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    // 연속 부분 수열 최대 합 (카데인)
    int solution(const vector<int>& nums) {
        int best = nums[0], cur = nums[0];
        for (size_t i = 1; i < nums.size(); i++) {
            cur = max(nums[i], cur + nums[i]);
            best = max(best, cur);
        }
        return best;
    }
};
''',

    # ---------------------------------------------------------------- 14
    "platinum-14": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    // 슬라이딩 윈도우 최댓값 (단조 감소 덱에 인덱스 저장)
    vector<int> solution(const vector<int>& nums, int k) {
        deque<int> dq;
        int n = nums.size();
        vector<int> res;
        for (int i = 0; i < n; i++) {
            while (!dq.empty() && nums[dq.back()] <= nums[i]) dq.pop_back();
            dq.push_back(i);
            if (dq.front() <= i - k) dq.pop_front();
            if (i >= k - 1) res.push_back(nums[dq.front()]);
        }
        return res;
    }
};
''',

    # ---------------------------------------------------------------- 15
    "platinum-15": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    // 팰린드롬 분할 최소 횟수
    int solution(const string& s) {
        int n = s.size();
        if (n <= 1) return 0;
        vector<vector<char>> pal(n, vector<char>(n, false));
        for (int i = 0; i < n; i++) pal[i][i] = true;
        for (int len = 2; len <= n; len++)
            for (int i = 0; i + len - 1 < n; i++) {
                int j = i + len - 1;
                if (s[i] == s[j]) pal[i][j] = (len == 2) || pal[i + 1][j - 1];
            }
        const int INF = 1 << 29;
        vector<int> cut(n, 0);
        for (int i = 0; i < n; i++) {
            if (pal[0][i]) { cut[i] = 0; continue; }
            int best = INF;
            for (int j = 1; j <= i; j++)
                if (pal[j][i]) best = min(best, cut[j - 1] + 1);
            cut[i] = best;
        }
        return cut[n - 1];
    }
};
''',

    # ---------------------------------------------------------------- 16
    "platinum-16": r'''#include <bits/stdc++.h>
using namespace std;

// 가장 긴 증가하는 부분 수열 (LIS) - O(n log n)
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<int> tails;
    tails.reserve(n);
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        auto it = lower_bound(tails.begin(), tails.end(), x);
        if (it == tails.end()) tails.push_back(x);
        else *it = x;
    }
    cout << tails.size() << "\n";
    return 0;
}
''',

    # ---------------------------------------------------------------- 17
    "platinum-17": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    // 편집 거리 (삽입/삭제/교체)
    int solution(const string& a, const string& b) {
        int n = a.size(), m = b.size();
        vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
        for (int i = 0; i <= n; i++) dp[i][0] = i;
        for (int j = 0; j <= m; j++) dp[0][j] = j;
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= m; j++)
                if (a[i - 1] == b[j - 1]) dp[i][j] = dp[i - 1][j - 1];
                else dp[i][j] = 1 + min({dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]});
        return dp[n][m];
    }
};
''',

    # ---------------------------------------------------------------- 18
    "platinum-18": r'''#include <bits/stdc++.h>
using namespace std;

// 정수 삼각형 최대 경로 합 (아래로 내려가며 DP)
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<vector<int>> tri(n);
    for (int i = 0; i < n; i++) {
        tri[i].resize(i + 1);
        for (int j = 0; j <= i; j++) cin >> tri[i][j];
    }
    for (int i = 1; i < n; i++)
        for (int j = 0; j <= i; j++) {
            if (j == 0) tri[i][j] += tri[i - 1][0];
            else if (j == i) tri[i][j] += tri[i - 1][i - 1];
            else tri[i][j] += max(tri[i - 1][j - 1], tri[i - 1][j]);
        }
    int ans = 0;
    for (int v : tri[n - 1]) ans = max(ans, v);
    cout << ans << "\n";
    return 0;
}
''',

    # ---------------------------------------------------------------- 19
    "platinum-19": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

class Solution {
    // [lo, hi) 구간 일직선 도둑질 최대값
    int robLinear(const vector<int>& a, int lo, int hi) {
        int prev = 0, cur = 0;
        for (int i = lo; i < hi; i++) {
            int t = max(cur, prev + a[i]);
            prev = cur;
            cur = t;
        }
        return cur;
    }
public:
    // 원형 배열 도둑질: 첫 집과 마지막 집은 동시에 못 턴다
    int solution(const vector<int>& money) {
        int n = money.size();
        if (n == 1) return money[0];
        return max(robLinear(money, 0, n - 1), robLinear(money, 1, n));
    }
};
''',

    # ---------------------------------------------------------------- 20
    "platinum-20": r'''#include <bits/stdc++.h>
using namespace std;

// 0/1 배낭 (1차원 DP, 무게 역순 순회)
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    if (!(cin >> n >> k)) return 0;
    vector<int> dp(k + 1, 0);
    for (int i = 0; i < n; i++) {
        int w, v;
        cin >> w >> v;
        for (int c = k; c >= w; c--) dp[c] = max(dp[c], dp[c - w] + v);
    }
    cout << dp[k] << "\n";
    return 0;
}
''',

    # ---------------------------------------------------------------- 21
    "platinum-21": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

struct Query { string op; int a, b; }; // "U":(idx,val), else "Q":(l,r)

// 구간 최솟값 세그먼트 트리 (갱신 + 질의)
class Solution {
    int sz;
    vector<long long> tree;
    static constexpr long long INF = LLONG_MAX;
    void update(int idx, long long val) {
        int p = sz + idx;
        tree[p] = val;
        p /= 2;
        while (p >= 1) { tree[p] = min(tree[2 * p], tree[2 * p + 1]); p /= 2; }
    }
    long long query(int l, int r) {
        long long res = INF;
        l += sz; r += sz + 1;
        while (l < r) {
            if (l & 1) res = min(res, tree[l++]);
            if (r & 1) res = min(res, tree[--r]);
            l /= 2; r /= 2;
        }
        return res;
    }
public:
    vector<int> solution(const vector<int>& arr, const vector<Query>& queries) {
        int n = arr.size();
        sz = 1;
        while (sz < n) sz *= 2;
        tree.assign(2 * sz, INF);
        for (int i = 0; i < n; i++) tree[sz + i] = arr[i];
        for (int p = sz - 1; p >= 1; p--) tree[p] = min(tree[2 * p], tree[2 * p + 1]);
        vector<int> out;
        for (auto& q : queries) {
            if (q.op == "U") update(q.a - 1, q.b);
            else out.push_back((int)query(q.a - 1, q.b - 1));
        }
        return out;
    }
};
''',

    # ---------------------------------------------------------------- 22
    "platinum-22": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

struct Query { string op; int a, b; }; // "U":(idx,val), else "Q":(l,r)

// 구간 최댓값 세그먼트 트리
class Solution {
    int sz;
    vector<long long> tree;
    static constexpr long long NEG = LLONG_MIN;
    void update(int idx, long long val) {
        int p = sz + idx;
        tree[p] = val;
        p /= 2;
        while (p >= 1) { tree[p] = max(tree[2 * p], tree[2 * p + 1]); p /= 2; }
    }
    long long query(int l, int r) {
        long long res = NEG;
        l += sz; r += sz + 1;
        while (l < r) {
            if (l & 1) res = max(res, tree[l++]);
            if (r & 1) res = max(res, tree[--r]);
            l /= 2; r /= 2;
        }
        return res;
    }
public:
    vector<int> solution(const vector<int>& arr, const vector<Query>& queries) {
        int n = arr.size();
        sz = 1;
        while (sz < n) sz *= 2;
        tree.assign(2 * sz, NEG);
        for (int i = 0; i < n; i++) tree[sz + i] = arr[i];
        for (int p = sz - 1; p >= 1; p--) tree[p] = max(tree[2 * p], tree[2 * p + 1]);
        vector<int> out;
        for (auto& q : queries) {
            if (q.op == "U") update(q.a - 1, q.b);
            else out.push_back((int)query(q.a - 1, q.b - 1));
        }
        return out;
    }
};
''',

    # ---------------------------------------------------------------- 23
    "platinum-23": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

struct Query { string op; int a, b; }; // "U":(idx,val), else "Q":(l,r)

// 구간 곱 나머지 세그먼트 트리 (MOD 1e9+7)
class Solution {
    static constexpr long long MOD = 1000000007LL;
    int sz;
    vector<long long> tree;
    void update(int idx, long long val) {
        int p = sz + idx;
        tree[p] = val % MOD;
        p /= 2;
        while (p >= 1) { tree[p] = tree[2 * p] * tree[2 * p + 1] % MOD; p /= 2; }
    }
    long long query(int l, int r) {
        long long res = 1;
        l += sz; r += sz + 1;
        while (l < r) {
            if (l & 1) res = res * tree[l++] % MOD;
            if (r & 1) res = res * tree[--r] % MOD;
            l /= 2; r /= 2;
        }
        return res;
    }
public:
    vector<int> solution(const vector<int>& arr, const vector<Query>& queries) {
        int n = arr.size();
        sz = 1;
        while (sz < n) sz *= 2;
        tree.assign(2 * sz, 1);
        for (int i = 0; i < n; i++) tree[sz + i] = arr[i] % MOD;
        for (int p = sz - 1; p >= 1; p--) tree[p] = tree[2 * p] * tree[2 * p + 1] % MOD;
        vector<int> out;
        for (auto& q : queries) {
            if (q.op == "U") update(q.a - 1, q.b);
            else out.push_back((int)query(q.a - 1, q.b - 1));
        }
        return out;
    }
};
''',

    # ---------------------------------------------------------------- 24
    "platinum-24": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

struct Query { string op; int a, b; }; // "A":(idx,delta), else "Q":(l,r)

// 펜윅 트리(BIT): 점 가산 + 구간합
class Solution {
    int n;
    vector<long long> bit;
    void add(int i, long long v) { for (; i <= n; i += i & -i) bit[i] += v; }
    long long prefix(int i) { long long s = 0; for (; i > 0; i -= i & -i) s += bit[i]; return s; }
public:
    vector<int> solution(const vector<int>& arr, const vector<Query>& queries) {
        n = arr.size();
        bit.assign(n + 1, 0);
        for (int i = 0; i < n; i++) add(i + 1, arr[i]);
        vector<int> out;
        for (auto& q : queries) {
            if (q.op == "A") add(q.a, q.b);
            else out.push_back((int)(prefix(q.b) - prefix(q.a - 1)));
        }
        return out;
    }
};
''',

    # ---------------------------------------------------------------- 25
    "platinum-25": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

// 뒤집힌 쌍(역순쌍)의 개수: 좌표압축 + BIT 를 뒤에서부터
class Solution {
    int m;
    vector<int> bit;
    void add(int i, int v) { for (; i <= m; i += i & -i) bit[i] += v; }
    int prefix(int i) { int s = 0; for (; i > 0; i -= i & -i) s += bit[i]; return s; }
public:
    long long solution(const vector<int>& arr) {
        int n = arr.size();
        vector<int> srt = arr;
        sort(srt.begin(), srt.end());
        srt.erase(unique(srt.begin(), srt.end()), srt.end());
        m = srt.size();
        bit.assign(m + 1, 0);
        long long inv = 0;
        for (int j = n - 1; j >= 0; j--) {
            int rk = (int)(lower_bound(srt.begin(), srt.end(), arr[j]) - srt.begin()) + 1;
            inv += prefix(rk - 1);
            add(rk, 1);
        }
        return inv;
    }
};
''',

    # ---------------------------------------------------------------- 26
    "platinum-26": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

// 최소 공통 조상(LCA): 희소 테이블(binary lifting)
class Solution {
    int LOG;
    vector<vector<int>> up;
    vector<int> depth;
    int lca(int u, int v) {
        if (depth[u] < depth[v]) swap(u, v);
        int d = depth[u] - depth[v];
        for (int k = 0; k < LOG; k++) if ((d >> k) & 1) u = up[k][u];
        if (u == v) return u;
        for (int k = LOG - 1; k >= 0; k--)
            if (up[k][u] != up[k][v]) { u = up[k][u]; v = up[k][v]; }
        return up[0][u];
    }
public:
    vector<int> solution(int n, const vector<pair<int, int>>& edges,
                         const vector<pair<int, int>>& queries) {
        vector<vector<int>> g(n + 1);
        for (auto& e : edges) {
            g[e.first].push_back(e.second);
            g[e.second].push_back(e.first);
        }
        LOG = 1;
        while ((1 << LOG) < n) LOG++;
        LOG++;
        up.assign(LOG, vector<int>(n + 1, 0));
        depth.assign(n + 1, 0);
        vector<bool> vis(n + 1, false);
        queue<int> dq;
        dq.push(1);
        vis[1] = true;
        while (!dq.empty()) {
            int u = dq.front();
            dq.pop();
            for (int v : g[u]) if (!vis[v]) {
                vis[v] = true; depth[v] = depth[u] + 1; up[0][v] = u; dq.push(v);
            }
        }
        for (int k = 1; k < LOG; k++)
            for (int v = 1; v <= n; v++) up[k][v] = up[k - 1][up[k - 1][v]];
        vector<int> res;
        for (auto& q : queries) res.push_back(lca(q.first, q.second));
        return res;
    }
};
''',

    # ---------------------------------------------------------------- 27
    "platinum-27": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

// 트리 위 두 정점의 거리 = depth[u] + depth[v] - 2*depth[lca(u,v)]
class Solution {
    int LOG;
    vector<vector<int>> up;
    vector<int> depth;
    int lca(int u, int v) {
        if (depth[u] < depth[v]) swap(u, v);
        int d = depth[u] - depth[v];
        for (int k = 0; k < LOG; k++) if ((d >> k) & 1) u = up[k][u];
        if (u == v) return u;
        for (int k = LOG - 1; k >= 0; k--)
            if (up[k][u] != up[k][v]) { u = up[k][u]; v = up[k][v]; }
        return up[0][u];
    }
public:
    vector<int> solution(int n, const vector<pair<int, int>>& edges,
                         const vector<pair<int, int>>& queries) {
        vector<vector<int>> g(n + 1);
        for (auto& e : edges) {
            g[e.first].push_back(e.second);
            g[e.second].push_back(e.first);
        }
        LOG = 1;
        while ((1 << LOG) < n) LOG++;
        LOG++;
        up.assign(LOG, vector<int>(n + 1, 0));
        depth.assign(n + 1, 0);
        vector<bool> vis(n + 1, false);
        queue<int> dq;
        dq.push(1);
        vis[1] = true;
        while (!dq.empty()) {
            int u = dq.front();
            dq.pop();
            for (int v : g[u]) if (!vis[v]) {
                vis[v] = true; depth[v] = depth[u] + 1; up[0][v] = u; dq.push(v);
            }
        }
        for (int k = 1; k < LOG; k++)
            for (int v = 1; v <= n; v++) up[k][v] = up[k - 1][up[k - 1][v]];
        vector<int> res;
        for (auto& q : queries) {
            int u = q.first, v = q.second;
            res.push_back(depth[u] + depth[v] - 2 * depth[lca(u, v)]);
        }
        return res;
    }
};
''',

    # ---------------------------------------------------------------- 28
    "platinum-28": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

struct Query { string op; int a; }; // "+"/"-":(값), "?":(k)

// 동적 K번째 작은 수: 값 위치 세그먼트 트리에서 트리 내려가며 탐색
class Solution {
    int sz;
    vector<int> tree;
    void update(int idx, int delta) {
        int p = sz + idx;
        tree[p] += delta;
        p /= 2;
        while (p >= 1) { tree[p] = tree[2 * p] + tree[2 * p + 1]; p /= 2; }
    }
    int kth(int k) {
        int p = 1;
        while (p < sz) {
            if (tree[2 * p] >= k) p = 2 * p;
            else { k -= tree[2 * p]; p = 2 * p + 1; }
        }
        return p - sz + 1;
    }
public:
    vector<int> solution(int m, const vector<Query>& queries) {
        sz = 1;
        while (sz < m) sz *= 2;
        tree.assign(2 * sz, 0);
        vector<int> out;
        for (auto& q : queries) {
            if (q.op == "+") update(q.a - 1, 1);
            else if (q.op == "-") update(q.a - 1, -1);
            else out.push_back(kth(q.a));
        }
        return out;
    }
};
''',

    # ---------------------------------------------------------------- 29
    "platinum-29": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

struct Query { string op; int a, b; }; // "I":(값), else "C":(lo,hi)

// 값 범위 안의 점 세기: 좌표압축 + 세그먼트 트리(빈도)
class Solution {
    int sz;
    vector<int> tree;
    void update(int i) {
        int p = sz + i;
        tree[p] += 1;
        p /= 2;
        while (p >= 1) { tree[p] = tree[2 * p] + tree[2 * p + 1]; p /= 2; }
    }
    int query(int l, int r) {
        if (l > r) return 0;
        int res = 0;
        l += sz; r += sz + 1;
        while (l < r) {
            if (l & 1) res += tree[l++];
            if (r & 1) res += tree[--r];
            l /= 2; r /= 2;
        }
        return res;
    }
public:
    vector<int> solution(const vector<Query>& queries) {
        vector<int> coords;
        for (auto& q : queries) if (q.op == "I") coords.push_back(q.a);
        sort(coords.begin(), coords.end());
        coords.erase(unique(coords.begin(), coords.end()), coords.end());
        int m = coords.size();
        sz = 1;
        while (sz < max(m, 1)) sz *= 2;
        tree.assign(2 * sz, 0);
        vector<int> out;
        for (auto& q : queries) {
            if (q.op == "I") {
                int idx = (int)(lower_bound(coords.begin(), coords.end(), q.a) - coords.begin());
                update(idx);
            } else {
                int lo = (int)(lower_bound(coords.begin(), coords.end(), q.a) - coords.begin());
                int hi = (int)(upper_bound(coords.begin(), coords.end(), q.b) - coords.begin()) - 1;
                out.push_back(query(lo, hi));
            }
        }
        return out;
    }
};
''',

    # ---------------------------------------------------------------- 30
    "platinum-30": r'''#include <bits/stdc++.h>
using namespace std;

// 최솟값 구간 질의 (입출력형 세그먼트 트리)
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<long long> arr(n);
    for (auto& x : arr) cin >> x;
    int sz = 1;
    while (sz < n) sz *= 2;
    const long long INF = LLONG_MAX;
    vector<long long> tree(2 * sz, INF);
    for (int i = 0; i < n; i++) tree[sz + i] = arr[i];
    for (int p = sz - 1; p >= 1; p--) tree[p] = min(tree[2 * p], tree[2 * p + 1]);
    string out;
    for (int q = 0; q < m; q++) {
        int t;
        cin >> t;
        if (t == 1) { // 1 i x : i번째 값을 x 로 변경
            int i;
            long long x;
            cin >> i >> x;
            int p = sz + i - 1;
            tree[p] = x;
            p /= 2;
            while (p >= 1) { tree[p] = min(tree[2 * p], tree[2 * p + 1]); p /= 2; }
        } else { // 2 l r : [l, r] 최솟값
            int l, r;
            cin >> l >> r;
            long long res = INF;
            l = l - 1 + sz;
            r = r + sz;
            while (l < r) {
                if (l & 1) res = min(res, tree[l++]);
                if (r & 1) res = min(res, tree[--r]);
                l /= 2; r /= 2;
            }
            out += to_string(res);
            out += '\n';
        }
    }
    cout << out;
    return 0;
}
''',

    # ---------------------------------------------------------------- 31
    "platinum-31": r'''#include <bits/stdc++.h>
using namespace std;

// 펜윅 트리 구간합 (입출력형). 갱신은 변화량(델타)으로 처리
int n;
vector<long long> bit;
void add(int i, long long v) { for (; i <= n; i += i & -i) bit[i] += v; }
long long prefix(int i) { long long s = 0; for (; i > 0; i -= i & -i) s += bit[i]; return s; }

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int m;
    if (!(cin >> n >> m)) return 0;
    vector<long long> cur(n + 1, 0);
    bit.assign(n + 1, 0);
    for (int i = 1; i <= n; i++) { cin >> cur[i]; add(i, cur[i]); }
    string out;
    for (int q = 0; q < m; q++) {
        int t;
        cin >> t;
        if (t == 1) {
            int i;
            long long x;
            cin >> i >> x;
            add(i, x - cur[i]);
            cur[i] = x;
        } else {
            int l, r;
            cin >> l >> r;
            out += to_string(prefix(r) - prefix(l - 1));
            out += '\n';
        }
    }
    cout << out;
    return 0;
}
''',

    # ---------------------------------------------------------------- 32
    "platinum-32": r'''#include <bits/stdc++.h>
using namespace std;

// 공통 조상 (입출력형 LCA, binary lifting)
int LOG;
vector<vector<int>> up;
vector<int> dep;

int lca(int u, int v) {
    if (dep[u] < dep[v]) swap(u, v);
    int d = dep[u] - dep[v];
    for (int k = 0; k < LOG; k++) if ((d >> k) & 1) u = up[k][u];
    if (u == v) return u;
    for (int k = LOG - 1; k >= 0; k--)
        if (up[k][u] != up[k][v]) { u = up[k][u]; v = up[k][v]; }
    return up[0][u];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<vector<int>> g(n + 1);
    for (int i = 0; i < n - 1; i++) {
        int a, b;
        cin >> a >> b;
        g[a].push_back(b);
        g[b].push_back(a);
    }
    LOG = 1;
    while ((1 << LOG) < n) LOG++;
    LOG++;
    up.assign(LOG, vector<int>(n + 1, 0));
    dep.assign(n + 1, 0);
    vector<bool> vis(n + 1, false);
    queue<int> dq;
    dq.push(1);
    vis[1] = true;
    while (!dq.empty()) {
        int u = dq.front();
        dq.pop();
        for (int v : g[u]) if (!vis[v]) {
            vis[v] = true; dep[v] = dep[u] + 1; up[0][v] = u; dq.push(v);
        }
    }
    for (int k = 1; k < LOG; k++)
        for (int v = 1; v <= n; v++) up[k][v] = up[k - 1][up[k - 1][v]];
    int m;
    cin >> m;
    string out;
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        out += to_string(lca(u, v));
        out += '\n';
    }
    cout << out;
    return 0;
}
''',

    # ---------------------------------------------------------------- 33
    "platinum-33": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

// 왼쪽의 더 큰 수 세기: 좌표압축 + BIT (지금까지 본 개수 - 자기 이하 개수)
class Solution {
    int m;
    vector<int> bit;
    void add(int i, int v) { for (; i <= m; i += i & -i) bit[i] += v; }
    int prefix(int i) { int s = 0; for (; i > 0; i -= i & -i) s += bit[i]; return s; }
public:
    vector<int> solution(const vector<int>& arr) {
        int n = arr.size();
        vector<int> srt = arr;
        sort(srt.begin(), srt.end());
        srt.erase(unique(srt.begin(), srt.end()), srt.end());
        m = srt.size();
        bit.assign(m + 1, 0);
        vector<int> out(n);
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            int rk = (int)(lower_bound(srt.begin(), srt.end(), arr[i]) - srt.begin()) + 1;
            out[i] = cnt - prefix(rk);
            add(rk, 1);
            cnt++;
        }
        return out;
    }
};
''',

    # ---------------------------------------------------------------- 34
    "platinum-34": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

struct Query { string op; int a, b; }; // "U":(idx,val), else "Q":(누적 임계값 v)

// 누적합 임계 위치 찾기: 세그먼트 트리에서 합이 v 이상이 되는 첫 위치
class Solution {
    int sz;
    vector<long long> tree;
    void update(int idx, long long val) {
        int p = sz + idx;
        tree[p] = val;
        p /= 2;
        while (p >= 1) { tree[p] = tree[2 * p] + tree[2 * p + 1]; p /= 2; }
    }
    int find(long long v) {
        if (tree[1] < v) return -1;
        int p = 1;
        while (p < sz) {
            if (tree[2 * p] >= v) p = 2 * p;
            else { v -= tree[2 * p]; p = 2 * p + 1; }
        }
        return p - sz + 1;
    }
public:
    vector<int> solution(const vector<int>& arr, const vector<Query>& queries) {
        int n = arr.size();
        sz = 1;
        while (sz < n) sz *= 2;
        tree.assign(2 * sz, 0);
        for (int i = 0; i < n; i++) tree[sz + i] = arr[i];
        for (int p = sz - 1; p >= 1; p--) tree[p] = tree[2 * p] + tree[2 * p + 1];
        vector<int> out;
        for (auto& q : queries) {
            if (q.op == "U") update(q.a - 1, q.b);
            else out.push_back(find((long long)q.a));
        }
        return out;
    }
};
''',

    # ---------------------------------------------------------------- 35
    "platinum-35": r'''#include <bits/stdc++.h>
using namespace std;

// 값 구간 개수 (입출력형): 오프라인 좌표압축 + 세그먼트 트리
int sz;
vector<int> tree;

void update(int i) {
    int p = sz + i;
    tree[p] += 1;
    p /= 2;
    while (p >= 1) { tree[p] = tree[2 * p] + tree[2 * p + 1]; p /= 2; }
}
int query(int l, int r) {
    if (l > r) return 0;
    int res = 0;
    l += sz; r += sz + 1;
    while (l < r) {
        if (l & 1) res += tree[l++];
        if (r & 1) res += tree[--r];
        l /= 2; r /= 2;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    if (!(cin >> q)) return 0;
    vector<array<int, 3>> ops(q); // {type, a, b}; type 0=I, 1=C
    vector<int> coords;
    for (int i = 0; i < q; i++) {
        string op;
        cin >> op;
        if (op == "I") {
            int x;
            cin >> x;
            ops[i] = {0, x, 0};
            coords.push_back(x);
        } else {
            int l, r;
            cin >> l >> r;
            ops[i] = {1, l, r};
        }
    }
    sort(coords.begin(), coords.end());
    coords.erase(unique(coords.begin(), coords.end()), coords.end());
    int m = coords.size();
    sz = 1;
    while (sz < max(m, 1)) sz *= 2;
    tree.assign(2 * sz, 0);
    string out;
    for (auto& o : ops) {
        if (o[0] == 0) {
            int idx = (int)(lower_bound(coords.begin(), coords.end(), o[1]) - coords.begin());
            update(idx);
        } else {
            int lo = (int)(lower_bound(coords.begin(), coords.end(), o[1]) - coords.begin());
            int hi = (int)(upper_bound(coords.begin(), coords.end(), o[2]) - coords.begin()) - 1;
            out += to_string(query(lo, hi));
            out += '\n';
        }
    }
    cout << out;
    return 0;
}
''',

    # ---------------------------------------------------------------- 36
    "platinum-36": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    // 문자열 패턴 등장 횟수 (KMP, 실패 함수 pi)
    int solution(const string& text, const string& pattern) {
        int n = text.size(), m = pattern.size();
        if (m == 0 || m > n) return 0;
        vector<int> pi(m, 0);
        int k = 0;
        for (int i = 1; i < m; i++) {
            while (k > 0 && pattern[i] != pattern[k]) k = pi[k - 1];
            if (pattern[i] == pattern[k]) pi[i] = ++k;
        }
        int count = 0;
        k = 0;
        for (int i = 0; i < n; i++) {
            while (k > 0 && text[i] != pattern[k]) k = pi[k - 1];
            if (text[i] == pattern[k]) {
                k++;
                if (k == m) { count++; k = pi[k - 1]; }
            }
        }
        return count;
    }
};
''',

    # ---------------------------------------------------------------- 37
    "platinum-37": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    // 패턴의 첫 등장 위치 (1-based, 없으면 -1). KMP 사용
    int solution(const string& text, const string& pattern) {
        int n = text.size(), m = pattern.size();
        if (m == 0) return 1;
        if (m > n) return -1;
        vector<int> pi(m, 0);
        int k = 0;
        for (int i = 1; i < m; i++) {
            while (k > 0 && pattern[i] != pattern[k]) k = pi[k - 1];
            if (pattern[i] == pattern[k]) pi[i] = ++k;
        }
        k = 0;
        for (int i = 0; i < n; i++) {
            while (k > 0 && text[i] != pattern[k]) k = pi[k - 1];
            if (text[i] == pattern[k]) {
                k++;
                if (k == m) return i - m + 2;
            }
        }
        return -1;
    }
};
''',

    # ---------------------------------------------------------------- 38
    "platinum-38": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

// 접두사로 시작하는 단어 수 (트라이). 각 노드 cnt = 그 노드를 지난 단어 수
class Solution {
    struct Node { map<char, int> ch; int cnt = 0; };
    vector<Node> nodes;
    int newNode() { nodes.push_back(Node()); return (int)nodes.size() - 1; }
public:
    vector<int> solution(const vector<string>& words, const vector<string>& queries) {
        nodes.clear();
        newNode(); // 루트 = 0
        for (auto& w : words) {
            int node = 0;
            for (char c : w) {
                auto it = nodes[node].ch.find(c);
                int nxt;
                if (it == nodes[node].ch.end()) { nxt = newNode(); nodes[node].ch[c] = nxt; }
                else nxt = it->second;
                node = nxt;
                nodes[node].cnt++;
            }
        }
        vector<int> res;
        for (auto& q : queries) {
            int node = 0;
            bool ok = true;
            for (char c : q) {
                auto it = nodes[node].ch.find(c);
                if (it == nodes[node].ch.end()) { ok = false; break; }
                node = it->second;
            }
            res.push_back(ok ? nodes[node].cnt : 0);
        }
        return res;
    }
};
''',

    # ---------------------------------------------------------------- 39
    "platinum-39": r'''#include <bits/stdc++.h>
using namespace std;

// Z 알고리즘 패턴 검색: s = pattern + 구분자 + text 의 Z 배열 이용
vector<int> zfunc(const string& s) {
    int n = s.size();
    vector<int> z(n, 0);
    if (n) z[0] = n;
    int l = 0, r = 0;
    for (int i = 1; i < n; i++) {
        if (i < r) z[i] = min(r - i, z[i - l]);
        while (i + z[i] < n && s[z[i]] == s[i + z[i]]) z[i]++;
        if (i + z[i] > r) { l = i; r = i + z[i]; }
    }
    return z;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string text, pattern;
    cin >> text >> pattern;
    int m = pattern.size();
    string s = pattern + char(1) + text;
    vector<int> z = zfunc(s);
    vector<int> pos;
    for (int i = m + 1; i < (int)s.size(); i++)
        if (z[i] >= m) pos.push_back(i - (m + 1) + 1);
    cout << pos.size() << "\n";
    if (!pos.empty()) {
        for (size_t k = 0; k < pos.size(); k++) {
            if (k) cout << ' ';
            cout << pos[k];
        }
        cout << "\n";
    }
    return 0;
}
''',

    # ---------------------------------------------------------------- 40
    "platinum-40": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

// 강한 연결 요소(SCC) 개수: 코사라주(Kosaraju), 반복식 DFS
class Solution {
public:
    int solution(int n, const vector<pair<int, int>>& edges) {
        vector<vector<int>> g(n + 1), rg(n + 1);
        for (auto& e : edges) {
            g[e.first].push_back(e.second);
            rg[e.second].push_back(e.first);
        }
        vector<bool> vis(n + 1, false);
        vector<int> order;
        for (int s = 1; s <= n; s++) {
            if (vis[s]) continue;
            vis[s] = true;
            vector<pair<int, int>> stk;
            stk.push_back({s, 0});
            while (!stk.empty()) {
                int node = stk.back().first;
                int idx = stk.back().second;
                if (idx < (int)g[node].size()) {
                    stk.back().second++;
                    int nxt = g[node][idx];
                    if (!vis[nxt]) { vis[nxt] = true; stk.push_back({nxt, 0}); }
                } else {
                    order.push_back(node);
                    stk.pop_back();
                }
            }
        }
        vector<bool> vis2(n + 1, false);
        int count = 0;
        for (int i = (int)order.size() - 1; i >= 0; i--) {
            int s = order[i];
            if (vis2[s]) continue;
            count++;
            vector<int> stk;
            stk.push_back(s);
            vis2[s] = true;
            while (!stk.empty()) {
                int node = stk.back();
                stk.pop_back();
                for (int nxt : rg[node]) if (!vis2[nxt]) { vis2[nxt] = true; stk.push_back(nxt); }
            }
        }
        return count;
    }
};
''',

    # ---------------------------------------------------------------- 41
    "platinum-41": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

// 가장 큰 강한 연결 요소의 크기 (코사라주)
class Solution {
public:
    int solution(int n, const vector<pair<int, int>>& edges) {
        vector<vector<int>> g(n + 1), rg(n + 1);
        for (auto& e : edges) {
            g[e.first].push_back(e.second);
            rg[e.second].push_back(e.first);
        }
        vector<bool> vis(n + 1, false);
        vector<int> order;
        for (int s = 1; s <= n; s++) {
            if (vis[s]) continue;
            vis[s] = true;
            vector<pair<int, int>> stk;
            stk.push_back({s, 0});
            while (!stk.empty()) {
                int node = stk.back().first;
                int idx = stk.back().second;
                if (idx < (int)g[node].size()) {
                    stk.back().second++;
                    int nxt = g[node][idx];
                    if (!vis[nxt]) { vis[nxt] = true; stk.push_back({nxt, 0}); }
                } else {
                    order.push_back(node);
                    stk.pop_back();
                }
            }
        }
        vector<bool> vis2(n + 1, false);
        int best = 0;
        for (int i = (int)order.size() - 1; i >= 0; i--) {
            int s = order[i];
            if (vis2[s]) continue;
            int size = 0;
            vector<int> stk;
            stk.push_back(s);
            vis2[s] = true;
            while (!stk.empty()) {
                int node = stk.back();
                stk.pop_back();
                size++;
                for (int nxt : rg[node]) if (!vis2[nxt]) { vis2[nxt] = true; stk.push_back(nxt); }
            }
            best = max(best, size);
        }
        return best;
    }
};
''',

    # ---------------------------------------------------------------- 42
    "platinum-42": r'''#include <bits/stdc++.h>
using namespace std;

// 최소 스패닝 트리 비용 (크루스칼 + 유니온 파인드, 경로 압축)
vector<int> parent;
int find(int x) {
    while (parent[x] != x) { parent[x] = parent[parent[x]]; x = parent[x]; }
    return x;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int v, e;
    if (!(cin >> v >> e)) return 0;
    vector<array<int, 3>> edges(e); // {가중치, a, b} - 가중치 기준 정렬
    for (int i = 0; i < e; i++) {
        int a, b, w;
        cin >> a >> b >> w;
        edges[i] = {w, a, b};
    }
    sort(edges.begin(), edges.end());
    parent.resize(v + 1);
    for (int i = 0; i <= v; i++) parent[i] = i;
    long long total = 0;
    for (auto& ed : edges) {
        int ra = find(ed[1]), rb = find(ed[2]);
        if (ra != rb) { parent[ra] = rb; total += ed[0]; }
    }
    cout << total << "\n";
    return 0;
}
''',

    # ---------------------------------------------------------------- 43
    "platinum-43": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

// 네트워크 연결 최소 비용 (프림, 최소 힙). edges[i] = {u, v, w}
class Solution {
public:
    int solution(int n, const vector<vector<int>>& edges) {
        vector<vector<pair<int, int>>> g(n + 1); // (가중치, 정점)
        for (auto& e : edges) {
            g[e[0]].push_back({e[2], e[1]});
            g[e[1]].push_back({e[2], e[0]});
        }
        vector<bool> vis(n + 1, false);
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
        pq.push({0, 1});
        int total = 0, cnt = 0;
        while (!pq.empty() && cnt < n) {
            auto [w, u] = pq.top();
            pq.pop();
            if (vis[u]) continue;
            vis[u] = true;
            total += w;
            cnt++;
            for (auto& nx : g[u]) if (!vis[nx.second]) pq.push(nx);
        }
        return total;
    }
};
''',

    # ---------------------------------------------------------------- 44
    "platinum-44": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

// 작업 스케줄링 최소 완료 시간 (위상 정렬 + DP). deps[i] = (a -> b)
class Solution {
public:
    int solution(int n, const vector<int>& times, const vector<pair<int, int>>& deps) {
        vector<vector<int>> g(n + 1);
        vector<int> indeg(n + 1, 0);
        for (auto& d : deps) { g[d.first].push_back(d.second); indeg[d.second]++; }
        vector<int> finish(n + 1, 0);
        queue<int> q;
        for (int i = 1; i <= n; i++)
            if (indeg[i] == 0) { finish[i] = times[i - 1]; q.push(i); }
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (int v : g[u]) {
                finish[v] = max(finish[v], finish[u] + times[v - 1]);
                if (--indeg[v] == 0) q.push(v);
            }
        }
        int ans = 0;
        for (int i = 1; i <= n; i++) ans = max(ans, finish[i]);
        return ans;
    }
};
''',

    # ---------------------------------------------------------------- 45
    "platinum-45": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

// 선수 과목과 최소 학기 수 (위상 정렬, 레벨 = 가장 긴 선행 경로 + 1)
class Solution {
public:
    int solution(int n, const vector<pair<int, int>>& prereqs) {
        vector<vector<int>> g(n + 1);
        vector<int> indeg(n + 1, 0);
        for (auto& p : prereqs) { g[p.first].push_back(p.second); indeg[p.second]++; }
        vector<int> level(n + 1, 0);
        queue<int> q;
        for (int i = 1; i <= n; i++)
            if (indeg[i] == 0) { level[i] = 1; q.push(i); }
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (int v : g[u]) {
                level[v] = max(level[v], level[u] + 1);
                if (--indeg[v] == 0) q.push(v);
            }
        }
        int ans = 0;
        for (int i = 1; i <= n; i++) ans = max(ans, level[i]);
        return ans;
    }
};
''',

    # ---------------------------------------------------------------- 46
    "platinum-46": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    // 거듭제곱 나머지 (분할 정복, 빠른 거듭제곱). 곱은 long long 으로 처리
    long long solution(long long a, long long b, long long m) {
        long long result = 1 % m;
        long long base = a % m;
        while (b > 0) {
            if (b & 1) result = (result * base) % m;
            base = (base * base) % m;
            b >>= 1;
        }
        return result;
    }
};
''',

    # ---------------------------------------------------------------- 47
    "platinum-47": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

// 행렬 거듭제곱 피보나치 (분할 정복). [[1,1],[1,0]]^n 의 [0][1] = F(n)
class Solution {
    long long mod;
    using Mat = array<array<long long, 2>, 2>;
    Mat mul(const Mat& A, const Mat& B) {
        return {{
            {{(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % mod,
              (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % mod}},
            {{(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % mod,
              (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % mod}}
        }};
    }
public:
    long long solution(long long n, long long m) {
        mod = m;
        Mat result = {{{{1, 0}}, {{0, 1}}}};
        Mat base = {{{{1, 1}}, {{1, 0}}}};
        long long e = n;
        while (e > 0) {
            if (e & 1) result = mul(result, base);
            base = mul(base, base);
            e >>= 1;
        }
        return result[0][1] % m;
    }
};
''',

    # ---------------------------------------------------------------- 48
    "platinum-48": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;

// 역순 쌍의 개수 (분할 정복 병합 정렬). 병합 중 누적 카운트
class Solution {
    long long cnt;
    vector<int> mergeSort(vector<int> a) {
        if (a.size() <= 1) return a;
        int mid = a.size() / 2;
        vector<int> left = mergeSort(vector<int>(a.begin(), a.begin() + mid));
        vector<int> right = mergeSort(vector<int>(a.begin() + mid, a.end()));
        vector<int> res;
        res.reserve(a.size());
        size_t i = 0, j = 0;
        while (i < left.size() && j < right.size()) {
            if (left[i] <= right[j]) res.push_back(left[i++]);
            else { res.push_back(right[j++]); cnt += (long long)(left.size() - i); }
        }
        while (i < left.size()) res.push_back(left[i++]);
        while (j < right.size()) res.push_back(right[j++]);
        return res;
    }
public:
    long long solution(const vector<int>& arr) {
        cnt = 0;
        mergeSort(arr);
        return cnt;
    }
};
''',

    # ---------------------------------------------------------------- 49
    "platinum-49": r'''#include <bits/stdc++.h>
using namespace std;

// 전화번호 목록 일관성 (트라이). 어떤 번호가 다른 번호의 접두사면 일관성 없음(NO)
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    struct Node {
        int ch[10];
        bool end;
        Node() { for (int i = 0; i < 10; i++) ch[i] = -1; end = false; }
    };
    vector<Node> nodes;
    nodes.push_back(Node()); // 루트
    bool bad = false;
    for (int t = 0; t < n; t++) {
        string num;
        cin >> num;
        if (bad) continue; // 이미 일관성 없음 - 입력만 소비
        int node = 0;
        for (char c : num) {
            if (nodes[node].end) bad = true; // 더 짧은 번호가 접두사
            int d = c - '0';
            if (nodes[node].ch[d] == -1) {
                nodes.push_back(Node());
                nodes[node].ch[d] = (int)nodes.size() - 1;
            }
            node = nodes[node].ch[d];
        }
        bool hasChild = false;
        for (int i = 0; i < 10; i++) if (nodes[node].ch[i] != -1) hasChild = true;
        if (hasChild) bad = true; // 현재 번호가 더 긴 번호의 접두사
        if (nodes[node].end) bad = true;
        nodes[node].end = true;
    }
    cout << (bad ? "NO" : "YES") << "\n";
    return 0;
}
''',

    # ---------------------------------------------------------------- 50
    "platinum-50": r'''#include <bits/stdc++.h>
using namespace std;

// 쿼드트리 압축 (분할 정복). 한 종류면 그 글자, 아니면 4분할 후 괄호로 묶기
vector<string> grid;

string rec(int r, int c, int size) {
    char first = grid[r][c];
    bool same = true;
    for (int i = 0; i < size && same; i++)
        for (int j = 0; j < size; j++)
            if (grid[r + i][c + j] != first) { same = false; break; }
    if (same) return string(1, first);
    int h = size / 2;
    return "(" + rec(r, c, h) + rec(r, c + h, h)
         + rec(r + h, c, h) + rec(r + h, c + h, h) + ")";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    grid.resize(n);
    for (int i = 0; i < n; i++) cin >> grid[i];
    cout << rec(0, 0, n) << "\n";
    return 0;
}
''',
}
