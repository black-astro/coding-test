"""Gold 난이도 문제별 C++ 정답 코드 맵.

검증된 Java/Python 정답을 C++(g++ -std=c++17)로 정확히 번역한 것이다.
- stdin 문제: 완전한 int main() (#include <bits/stdc++.h>).
- func 문제: 동등한 C++ 함수(struct Solution / 자유 함수).
"""

CPP = {
    # gold-01 : 1로 만들기 (DP) - 함수 구현형: 참고용 C++ 정답
    "gold-01": r'''#include <bits/stdc++.h>
using namespace std;

// 함수 구현형: 참고용 C++ 정답
struct Solution {
    int solution(int n) {
        vector<int> dp(n + 1, 0);
        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i - 1] + 1;                       // 1 빼기
            if (i % 2 == 0) dp[i] = min(dp[i], dp[i / 2] + 1); // 2로 나누기
            if (i % 3 == 0) dp[i] = min(dp[i], dp[i / 3] + 1); // 3으로 나누기
        }
        return dp[n];
    }
};
''',

    # gold-02 : 미로 탐색 (BFS)
    "gold-02": r'''#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    vector<string> g(n);
    for (int i = 0; i < n; i++) cin >> g[i];
    vector<vector<int>> dist(n, vector<int>(m, 0));
    dist[0][0] = 1;
    queue<pair<int,int>> q;
    q.push({0, 0});
    int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};
    while (!q.empty()) {
        auto [x, y] = q.front(); q.pop();
        for (int d = 0; d < 4; d++) {
            int nx = x + dx[d], ny = y + dy[d];
            if (nx >= 0 && nx < n && ny >= 0 && ny < m && g[nx][ny] == '1' && dist[nx][ny] == 0) {
                dist[nx][ny] = dist[x][y] + 1;
                q.push({nx, ny});
            }
        }
    }
    printf("%d\n", dist[n - 1][m - 1]);
    return 0;
}
''',

    # gold-03 : 0/1 배낭 문제 - 함수 구현형: 참고용 C++ 정답
    "gold-03": r'''#include <bits/stdc++.h>
using namespace std;

// 함수 구현형: 참고용 C++ 정답
struct Solution {
    int solution(vector<int> weights, vector<int> values, int capacity) {
        vector<int> dp(capacity + 1, 0);
        for (size_t i = 0; i < weights.size(); i++)
            for (int w = capacity; w >= weights[i]; w--)
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i]);
        return dp[capacity];
    }
};
''',

    # gold-04 : 가장 긴 증가하는 부분 수열 (LIS) - 함수 구현형: 참고용 C++ 정답
    "gold-04": r'''#include <bits/stdc++.h>
using namespace std;

// 함수 구현형: 참고용 C++ 정답
struct Solution {
    int solution(vector<int> nums) {
        int n = nums.size(), best = 1;
        vector<int> dp(n);
        for (int i = 0; i < n; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++)
                if (nums[j] < nums[i]) dp[i] = max(dp[i], dp[j] + 1);
            best = max(best, dp[i]);
        }
        return best;
    }
};
''',

    # gold-05 : 두 수의 합 (투 포인터) - 함수 구현형: 참고용 C++ 정답
    "gold-05": r'''#include <bits/stdc++.h>
using namespace std;

// 함수 구현형: 참고용 C++ 정답
struct Solution {
    bool solution(vector<int> nums, int target) {
        vector<int> s = nums;
        sort(s.begin(), s.end());
        int l = 0, r = (int)s.size() - 1;
        while (l < r) {
            int t = s[l] + s[r];
            if (t == target) return true;
            else if (t < target) l++;
            else r--;
        }
        return false;
    }
};
''',

    # gold-06 : 계단 오르기 최대 점수
    "gold-06": r'''#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<int> s(n);
    for (int i = 0; i < n; i++) scanf("%d", &s[i]);
    vector<int> dp(n, 0);
    dp[0] = s[0];
    if (n >= 2) dp[1] = s[0] + s[1];
    if (n >= 3) dp[2] = max(s[0] + s[2], s[1] + s[2]);
    for (int i = 3; i < n; i++)
        dp[i] = max(dp[i - 2] + s[i], dp[i - 3] + s[i - 1] + s[i]);
    printf("%d\n", dp[n - 1]);
    return 0;
}
''',

    # gold-07 : 포도주 시식 최대량
    "gold-07": r'''#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<int> w(n);
    for (int i = 0; i < n; i++) scanf("%d", &w[i]);
    vector<int> dp(n, 0);
    dp[0] = w[0];
    if (n >= 2) dp[1] = w[0] + w[1];
    if (n >= 3) dp[2] = max(dp[1], max(w[0] + w[2], w[1] + w[2]));
    for (int i = 3; i < n; i++)
        dp[i] = max(dp[i - 1], max(dp[i - 2] + w[i], dp[i - 3] + w[i - 1] + w[i]));
    printf("%d\n", dp[n - 1]);
    return 0;
}
''',

    # gold-08 : 정수 삼각형 최대 경로
    "gold-08": r'''#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<vector<int>> tri(n);
    for (int i = 0; i < n; i++) {
        tri[i].resize(i + 1);
        for (int j = 0; j <= i; j++) scanf("%d", &tri[i][j]);
    }
    for (int i = n - 2; i >= 0; i--)
        for (int j = 0; j <= i; j++)
            tri[i][j] += max(tri[i + 1][j], tri[i + 1][j + 1]);
    printf("%d\n", tri[0][0]);
    return 0;
}
''',

    # gold-09 : 연속 부분 수열 최대 합 - 함수 구현형: 참고용 C++ 정답
    "gold-09": r'''#include <bits/stdc++.h>
using namespace std;

// 함수 구현형: 참고용 C++ 정답
struct Solution {
    int solution(vector<int> nums) {
        int cur = nums[0], best = nums[0];
        for (size_t i = 1; i < nums.size(); i++) {
            cur = max(nums[i], cur + nums[i]);
            best = max(best, cur);
        }
        return best;
    }
};
''',

    # gold-10 : 2 x n 타일 채우기
    "gold-10": r'''#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    const int MOD = 10007;
    vector<int> dp(n + 1, 0);
    dp[1] = 1;
    if (n >= 2) dp[2] = 2;
    for (int i = 3; i <= n; i++) dp[i] = (dp[i - 1] + dp[i - 2]) % MOD;
    printf("%d\n", dp[n]);
    return 0;
}
''',

    # gold-11 : 편집 거리 최소 연산 - 함수 구현형: 참고용 C++ 정답
    "gold-11": r'''#include <bits/stdc++.h>
using namespace std;

// 함수 구현형: 참고용 C++ 정답
struct Solution {
    int solution(string a, string b) {
        int m = a.size(), n = b.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        for (int i = 0; i <= m; i++) dp[i][0] = i;
        for (int j = 0; j <= n; j++) dp[0][j] = j;
        for (int i = 1; i <= m; i++)
            for (int j = 1; j <= n; j++) {
                if (a[i - 1] == b[j - 1]) dp[i][j] = dp[i - 1][j - 1];
                else dp[i][j] = 1 + min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1]));
            }
        return dp[m][n];
    }
};
''',

    # gold-12 : RGB 집 색칠 비용 - 함수 구현형: 참고용 C++ 정답
    "gold-12": r'''#include <bits/stdc++.h>
using namespace std;

// 함수 구현형: 참고용 C++ 정답
struct Solution {
    int solution(vector<vector<int>> costs) {
        vector<int> prev = costs[0];
        for (size_t i = 1; i < costs.size(); i++) {
            vector<int> cur(3);
            cur[0] = costs[i][0] + min(prev[1], prev[2]);
            cur[1] = costs[i][1] + min(prev[0], prev[2]);
            cur[2] = costs[i][2] + min(prev[0], prev[1]);
            prev = cur;
        }
        return min(prev[0], min(prev[1], prev[2]));
    }
};
''',

    # gold-13 : 가장 큰 정사각형 넓이 - 함수 구현형: 참고용 C++ 정답
    "gold-13": r'''#include <bits/stdc++.h>
using namespace std;

// 함수 구현형: 참고용 C++ 정답
struct Solution {
    int solution(vector<vector<int>> matrix) {
        if (matrix.empty() || matrix[0].empty()) return 0;
        int m = matrix.size(), n = matrix[0].size(), best = 0;
        vector<vector<int>> dp(m, vector<int>(n, 0));
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (matrix[i][j] == 1) {
                    if (i == 0 || j == 0) dp[i][j] = 1;
                    else dp[i][j] = min(dp[i - 1][j], min(dp[i][j - 1], dp[i - 1][j - 1])) + 1;
                    best = max(best, dp[i][j]);
                }
        return best * best;
    }
};
''',

    # gold-14 : 장애물 격자 경로 수 - 함수 구현형: 참고용 C++ 정답
    "gold-14": r'''#include <bits/stdc++.h>
using namespace std;

// 함수 구현형: 참고용 C++ 정답
struct Solution {
    int solution(vector<vector<int>> grid) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 0));
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) dp[i][j] = 0;
                else if (i == 0 && j == 0) dp[i][j] = 1;
                else {
                    int up = i > 0 ? dp[i - 1][j] : 0;
                    int left = j > 0 ? dp[i][j - 1] : 0;
                    dp[i][j] = up + left;
                }
            }
        return dp[m - 1][n - 1];
    }
};
''',

    # gold-15 : 부분집합 합 존재 판별 - 함수 구현형: 참고용 C++ 정답
    "gold-15": r'''#include <bits/stdc++.h>
using namespace std;

// 함수 구현형: 참고용 C++ 정답
struct Solution {
    bool solution(vector<int> nums, int target) {
        if (target < 0) return false;
        vector<char> dp(target + 1, false);
        dp[0] = true;
        for (int x : nums)
            for (int s = target; s >= x; s--)
                if (dp[s - x]) dp[s] = true;
        return dp[target];
    }
};
''',

    # gold-16 : 동전 조합 경우의 수
    "gold-16": r'''#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    vector<int> coins(n);
    for (int i = 0; i < n; i++) scanf("%d", &coins[i]);
    vector<int> dp(k + 1, 0);
    dp[0] = 1;
    for (int c : coins)
        for (int j = c; j <= k; j++)
            dp[j] += dp[j - c];
    printf("%d\n", dp[k]);
    return 0;
}
''',

    # gold-17 : 최장 공통 부분 수열 길이 - 함수 구현형: 참고용 C++ 정답
    "gold-17": r'''#include <bits/stdc++.h>
using namespace std;

// 함수 구현형: 참고용 C++ 정답
struct Solution {
    int solution(string a, string b) {
        int m = a.size(), n = b.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        for (int i = 1; i <= m; i++)
            for (int j = 1; j <= n; j++) {
                if (a[i - 1] == b[j - 1]) dp[i][j] = dp[i - 1][j - 1] + 1;
                else dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        return dp[m][n];
    }
};
''',

    # gold-18 : 연속 부분 수열 최대 곱 - 함수 구현형: 참고용 C++ 정답
    "gold-18": r'''#include <bits/stdc++.h>
using namespace std;

// 함수 구현형: 참고용 C++ 정답
struct Solution {
    int solution(vector<int> nums) {
        int curMax = nums[0], curMin = nums[0], ans = nums[0];
        for (size_t i = 1; i < nums.size(); i++) {
            int x = nums[i];
            int a = x, b = curMax * x, c = curMin * x;
            curMax = max(a, max(b, c));
            curMin = min(a, min(b, c));
            ans = max(ans, curMax);
        }
        return ans;
    }
};
''',

    # gold-19 : 이친수 개수 세기
    "gold-19": r'''#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    long long zero = 0, one = 1;
    for (int i = 0; i < n - 1; i++) {
        long long nz = zero + one, no = zero;
        zero = nz; one = no;
    }
    printf("%lld\n", zero + one);
    return 0;
}
''',

    # gold-20 : 최장 회문 부분 수열 - 함수 구현형: 참고용 C++ 정답
    "gold-20": r'''#include <bits/stdc++.h>
using namespace std;

// 함수 구현형: 참고용 C++ 정답
struct Solution {
    int solution(string s) {
        int n = s.size();
        if (n == 0) return 0;
        vector<vector<int>> dp(n, vector<int>(n, 0));
        for (int i = 0; i < n; i++) dp[i][i] = 1;
        for (int len = 2; len <= n; len++)
            for (int i = 0; i + len - 1 < n; i++) {
                int j = i + len - 1;
                if (s[i] == s[j])
                    dp[i][j] = (len > 2 ? dp[i + 1][j - 1] : 0) + 2;
                else dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
            }
        return dp[0][n - 1];
    }
};
''',

    # gold-21 : 연결 요소의 개수
    "gold-21": r'''#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    vector<char> visited(n + 1, false);
    int cnt = 0;
    for (int s = 1; s <= n; s++) {
        if (!visited[s]) {
            cnt++;
            visited[s] = true;
            queue<int> q;
            q.push(s);
            while (!q.empty()) {
                int x = q.front(); q.pop();
                for (int y : adj[x]) {
                    if (!visited[y]) { visited[y] = true; q.push(y); }
                }
            }
        }
    }
    printf("%d\n", cnt);
    return 0;
}
''',

    # gold-22 : 섬의 개수 (8방향) - 함수 구현형: 참고용 C++ 정답
    "gold-22": r'''#include <bits/stdc++.h>
using namespace std;

// 함수 구현형: 참고용 C++ 정답
struct Solution {
    int solution(vector<vector<int>> grid) {
        if (grid.empty() || grid[0].empty()) return 0;
        int n = grid.size(), m = grid[0].size(), cnt = 0;
        vector<vector<char>> visited(n, vector<char>(m, false));
        int dx[] = {-1, -1, -1, 0, 0, 1, 1, 1};
        int dy[] = {-1, 0, 1, -1, 1, -1, 0, 1};
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 1 && !visited[i][j]) {
                    cnt++;
                    visited[i][j] = true;
                    queue<pair<int,int>> q;
                    q.push({i, j});
                    while (!q.empty()) {
                        auto [x, y] = q.front(); q.pop();
                        for (int d = 0; d < 8; d++) {
                            int nx = x + dx[d], ny = y + dy[d];
                            if (nx >= 0 && nx < n && ny >= 0 && ny < m && grid[nx][ny] == 1 && !visited[nx][ny]) {
                                visited[nx][ny] = true;
                                q.push({nx, ny});
                            }
                        }
                    }
                }
            }
        }
        return cnt;
    }
};
''',

    # gold-23 : 단지번호붙이기
    "gold-23": r'''#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<string> g(n);
    for (int i = 0; i < n; i++) cin >> g[i];
    vector<vector<char>> visited(n, vector<char>(n, false));
    vector<int> sizes;
    int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (g[i][j] == '1' && !visited[i][j]) {
                visited[i][j] = true;
                queue<pair<int,int>> q;
                q.push({i, j});
                int cnt = 0;
                while (!q.empty()) {
                    auto [x, y] = q.front(); q.pop();
                    cnt++;
                    for (int d = 0; d < 4; d++) {
                        int nx = x + dx[d], ny = y + dy[d];
                        if (nx >= 0 && nx < n && ny >= 0 && ny < n && g[nx][ny] == '1' && !visited[nx][ny]) {
                            visited[nx][ny] = true;
                            q.push({nx, ny});
                        }
                    }
                }
                sizes.push_back(cnt);
            }
        }
    }
    sort(sizes.begin(), sizes.end());
    printf("%d\n", (int)sizes.size());
    for (int s : sizes) printf("%d\n", s);
    return 0;
}
''',

    # gold-24 : 토마토 익히기
    "gold-24": r'''#include <bits/stdc++.h>
using namespace std;

int main() {
    int m, n;
    scanf("%d %d", &m, &n);
    vector<vector<int>> g(n, vector<int>(m));
    queue<pair<int,int>> q;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            scanf("%d", &g[i][j]);
            if (g[i][j] == 1) q.push({i, j});
        }
    int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};
    int days = 0;
    while (!q.empty()) {
        queue<pair<int,int>> nq;
        while (!q.empty()) {
            auto [x, y] = q.front(); q.pop();
            for (int d = 0; d < 4; d++) {
                int nx = x + dx[d], ny = y + dy[d];
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && g[nx][ny] == 0) {
                    g[nx][ny] = 1;
                    nq.push({nx, ny});
                }
            }
        }
        if (!nq.empty()) days++;
        q = move(nq);
    }
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            if (g[i][j] == 0) { printf("-1\n"); return 0; }
    printf("%d\n", days);
    return 0;
}
''',

    # gold-25 : 벽 부수고 이동하기
    "gold-25": r'''#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    vector<string> g(n);
    for (int i = 0; i < n; i++) cin >> g[i];
    // visited[x][y][b] : b=1이면 이미 벽을 한 번 부순 상태
    vector<vector<array<char,2>>> visited(n, vector<array<char,2>>(m, {0, 0}));
    queue<array<int,4>> q;  // {x, y, b, dist}
    q.push({0, 0, 0, 1});
    visited[0][0][0] = true;
    int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};
    while (!q.empty()) {
        auto c = q.front(); q.pop();
        int x = c[0], y = c[1], b = c[2], d = c[3];
        if (x == n - 1 && y == m - 1) { printf("%d\n", d); return 0; }
        for (int dir = 0; dir < 4; dir++) {
            int nx = x + dx[dir], ny = y + dy[dir];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (g[nx][ny] == '0' && !visited[nx][ny][b]) {
                visited[nx][ny][b] = true;
                q.push({nx, ny, b, d + 1});
            } else if (g[nx][ny] == '1' && b == 0 && !visited[nx][ny][1]) {
                visited[nx][ny][1] = true;
                q.push({nx, ny, 1, d + 1});
            }
        }
    }
    printf("-1\n");
    return 0;
}
''',

    # gold-26 : N과 M (순열)
    "gold-26": r'''#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<char> used;
vector<int> chosen;
string out;

void bt(int depth) {
    if (depth == m) {
        for (int i = 0; i < m; i++) {
            out += to_string(chosen[i]);
            if (i < m - 1) out += ' ';
        }
        out += '\n';
        return;
    }
    for (int i = 1; i <= n; i++) {
        if (!used[i]) {
            used[i] = true;
            chosen[depth] = i;
            bt(depth + 1);
            used[i] = false;
        }
    }
}

int main() {
    scanf("%d %d", &n, &m);
    used.assign(n + 1, false);
    chosen.assign(m, 0);
    bt(0);
    printf("%s", out.c_str());
    return 0;
}
''',

    # gold-27 : N과 M (조합)
    "gold-27": r'''#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<int> chosen;
string out;

void bt(int start, int depth) {
    if (depth == m) {
        for (int i = 0; i < m; i++) {
            out += to_string(chosen[i]);
            if (i < m - 1) out += ' ';
        }
        out += '\n';
        return;
    }
    for (int i = start; i <= n; i++) {
        chosen[depth] = i;
        bt(i + 1, depth + 1);
    }
}

int main() {
    scanf("%d %d", &n, &m);
    chosen.assign(m, 0);
    bt(1, 0);
    printf("%s", out.c_str());
    return 0;
}
''',

    # gold-28 : N-퀸 배치 가짓수 - 함수 구현형: 참고용 C++ 정답
    "gold-28": r'''#include <bits/stdc++.h>
using namespace std;

// 함수 구현형: 참고용 C++ 정답
struct Solution {
    int n, cnt = 0;
    vector<char> cols, diag1, diag2;
    int solution(int n) {
        this->n = n;
        cnt = 0;
        cols.assign(n, false);
        diag1.assign(2 * n, false);
        diag2.assign(2 * n, false);
        bt(0);
        return cnt;
    }
    void bt(int r) {
        if (r == n) { cnt++; return; }
        for (int c = 0; c < n; c++) {
            if (!cols[c] && !diag1[r + c] && !diag2[r - c + n]) {
                cols[c] = diag1[r + c] = diag2[r - c + n] = true;
                bt(r + 1);
                cols[c] = diag1[r + c] = diag2[r - c + n] = false;
            }
        }
    }
};
''',

    # gold-29 : 부분수열의 합 가짓수 - 함수 구현형: 참고용 C++ 정답
    "gold-29": r'''#include <bits/stdc++.h>
using namespace std;

// 함수 구현형: 참고용 C++ 정답
struct Solution {
    vector<int> nums;
    int n, S, cnt = 0;
    int solution(vector<int> nums, int S) {
        this->nums = nums;
        this->n = nums.size();
        this->S = S;
        cnt = 0;
        bt(0, 0, 0);
        return cnt;
    }
    void bt(int i, int total, int picked) {
        if (i == n) {
            if (picked > 0 && total == S) cnt++;
            return;
        }
        bt(i + 1, total + nums[i], picked + 1);
        bt(i + 1, total, picked);
    }
};
''',

    # gold-30 : 합이 목표가 되는 조합 수 - 함수 구현형: 참고용 C++ 정답
    "gold-30": r'''#include <bits/stdc++.h>
using namespace std;

// 함수 구현형: 참고용 C++ 정답
struct Solution {
    vector<int> nums;
    int n, k, target, cnt = 0;
    int solution(vector<int> nums, int k, int target) {
        this->nums = nums;
        this->n = nums.size();
        this->k = k;
        this->target = target;
        cnt = 0;
        bt(0, 0, 0);
        return cnt;
    }
    void bt(int start, int c, int total) {
        if (c == k) {
            if (total == target) cnt++;
            return;
        }
        for (int i = start; i < n; i++) {
            bt(i + 1, c + 1, total + nums[i]);
        }
    }
};
''',

    # gold-31 : 안전 영역 최대 개수
    "gold-31": r'''#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    vector<vector<int>> g(n, vector<int>(n));
    int top = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) {
            scanf("%d", &g[i][j]);
            top = max(top, g[i][j]);
        }
    int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};
    int best = 0;
    for (int h = 0; h < top; h++) {
        vector<vector<char>> visited(n, vector<char>(n, false));
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (g[i][j] > h && !visited[i][j]) {
                    cnt++;
                    visited[i][j] = true;
                    queue<pair<int,int>> q;
                    q.push({i, j});
                    while (!q.empty()) {
                        auto [x, y] = q.front(); q.pop();
                        for (int d = 0; d < 4; d++) {
                            int nx = x + dx[d], ny = y + dy[d];
                            if (nx >= 0 && nx < n && ny >= 0 && ny < n && g[nx][ny] > h && !visited[nx][ny]) {
                                visited[nx][ny] = true;
                                q.push({nx, ny});
                            }
                        }
                    }
                }
            }
        }
        best = max(best, cnt);
    }
    printf("%d\n", best);
    return 0;
}
''',

    # gold-32 : 단어 변환 최단 길이 - 함수 구현형: 참고용 C++ 정답
    "gold-32": r'''#include <bits/stdc++.h>
using namespace std;

// 함수 구현형: 참고용 C++ 정답
struct Solution {
    bool oneDiff(const string& a, const string& b) {
        int diff = 0;
        for (size_t i = 0; i < a.size(); i++) if (a[i] != b[i]) diff++;
        return diff == 1;
    }
    int solution(string begin, string target, vector<string> words) {
        bool inList = false;
        for (auto& w : words) if (w == target) inList = true;
        if (!inList) return 0;
        set<string> visited;
        visited.insert(begin);
        queue<pair<string,int>> q;
        q.push({begin, 0});
        while (!q.empty()) {
            auto [cur, d] = q.front(); q.pop();
            if (cur == target) return d;
            for (auto& w : words) {
                if (!visited.count(w) && oneDiff(cur, w)) {
                    visited.insert(w);
                    q.push({w, d + 1});
                }
            }
        }
        return 0;
    }
};
''',

    # gold-33 : 스타트와 링크 팀 나누기
    "gold-33": r'''#include <bits/stdc++.h>
using namespace std;

int n, half;
vector<vector<int>> s;
int best = INT_MAX;
vector<char> pick;

void choose(int idx, int cnt) {
    if (cnt == half) {
        int ts = 0, os = 0;
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++) {
                if (pick[i] && pick[j]) ts += s[i][j] + s[j][i];
                else if (!pick[i] && !pick[j]) os += s[i][j] + s[j][i];
            }
        best = min(best, abs(ts - os));
        return;
    }
    if (idx == n) return;
    pick[idx] = true;
    choose(idx + 1, cnt + 1);
    pick[idx] = false;
    choose(idx + 1, cnt);
}

int main() {
    scanf("%d", &n);
    s.assign(n, vector<int>(n));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) scanf("%d", &s[i][j]);
    half = n / 2;
    pick.assign(n, false);
    choose(0, 0);
    printf("%d\n", best);
    return 0;
}
''',

    # gold-34 : 알파벳 최대 칸 이동
    "gold-34": r'''#include <bits/stdc++.h>
using namespace std;

int r, c, best = 0;
vector<string> g;
bool used[26];

void dfs(int x, int y, int length) {
    if (length > best) best = length;
    int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};
    for (int d = 0; d < 4; d++) {
        int nx = x + dx[d], ny = y + dy[d];
        if (nx >= 0 && nx < r && ny >= 0 && ny < c) {
            int idx = g[nx][ny] - 'A';
            if (!used[idx]) {
                used[idx] = true;
                dfs(nx, ny, length + 1);
                used[idx] = false;
            }
        }
    }
}

int main() {
    scanf("%d %d", &r, &c);
    g.resize(r);
    for (int i = 0; i < r; i++) cin >> g[i];
    used[g[0][0] - 'A'] = true;
    dfs(0, 0, 1);
    printf("%d\n", best);
    return 0;
}
''',

    # gold-35 : 숨바꼭질 최소 시간
    "gold-35": r'''#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    const int MAX = 100001;
    vector<int> dist(MAX, -1);
    dist[n] = 0;
    queue<int> q;
    q.push(n);
    while (!q.empty()) {
        int x = q.front(); q.pop();
        if (x == k) { printf("%d\n", dist[x]); return 0; }
        int nexts[] = {x - 1, x + 1, x * 2};
        for (int nx : nexts) {
            if (nx >= 0 && nx < MAX && dist[nx] == -1) {
                dist[nx] = dist[x] + 1;
                q.push(nx);
            }
        }
    }
    printf("%d\n", dist[k]);
    return 0;
}
''',

    # gold-36 : 다익스트라 최단 거리
    "gold-36": r'''#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    int s;
    scanf("%d", &s);
    vector<vector<pair<int,int>>> g(n + 1);  // {정점, 가중치}
    for (int i = 0; i < m; i++) {
        int u, v, w;
        scanf("%d %d %d", &u, &v, &w);
        g[u].push_back({v, w});
    }
    const long long INF = LLONG_MAX / 4;
    vector<long long> dist(n + 1, INF);
    dist[s] = 0;
    priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<>> pq;
    pq.push({0, s});
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue;
        for (auto& [v, w] : g[u]) {
            long long nd = d + w;
            if (nd < dist[v]) { dist[v] = nd; pq.push({nd, v}); }
        }
    }
    string out;
    for (int i = 1; i <= n; i++) {
        out += (dist[i] == INF ? "INF" : to_string(dist[i]));
        out += '\n';
    }
    printf("%s", out.c_str());
    return 0;
}
''',

    # gold-37 : 플로이드-워셜 모든 쌍 최단 거리
    "gold-37": r'''#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    const long long INF = LLONG_MAX / 4;
    vector<vector<long long>> d(n + 1, vector<long long>(n + 1, INF));
    for (int i = 1; i <= n; i++) d[i][i] = 0;
    for (int e = 0; e < m; e++) {
        int u, v, w;
        scanf("%d %d %d", &u, &v, &w);
        if (w < d[u][v]) d[u][v] = w;
    }
    for (int k = 1; k <= n; k++)
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++)
                if (d[i][k] + d[k][j] < d[i][j]) d[i][j] = d[i][k] + d[k][j];
    string out;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            out += to_string(d[i][j] == INF ? 0 : d[i][j]);
            if (j < n) out += ' ';
        }
        out += '\n';
    }
    printf("%s", out.c_str());
    return 0;
}
''',

    # gold-38 : 무방향 그래프 사이클 판별 - 함수 구현형: 참고용 C++ 정답
    "gold-38": r'''#include <bits/stdc++.h>
using namespace std;

// 함수 구현형: 참고용 C++ 정답
struct Solution {
    vector<int> parent;
    int find(int x) {
        while (parent[x] != x) { parent[x] = parent[parent[x]]; x = parent[x]; }
        return x;
    }
    bool solution(int n, vector<vector<int>> edges) {
        parent.resize(n + 1);
        for (int i = 0; i <= n; i++) parent[i] = i;
        for (auto& e : edges) {
            int ru = find(e[0]), rv = find(e[1]);
            if (ru == rv) return true;
            parent[ru] = rv;
        }
        return false;
    }
};
''',

    # gold-39 : 친구 네트워크 크기 - 함수 구현형: 참고용 C++ 정답
    "gold-39": r'''#include <bits/stdc++.h>
using namespace std;

// 함수 구현형: 참고용 C++ 정답
struct Solution {
    unordered_map<string, string> parent;
    unordered_map<string, int> sz;
    void add(const string& x) {
        if (!parent.count(x)) { parent[x] = x; sz[x] = 1; }
    }
    string find(string x) {
        while (parent[x] != x) { parent[x] = parent[parent[x]]; x = parent[x]; }
        return x;
    }
    vector<int> solution(vector<vector<string>> operations) {
        vector<int> res(operations.size());
        for (size_t i = 0; i < operations.size(); i++) {
            string a = operations[i][0], b = operations[i][1];
            add(a); add(b);
            string ra = find(a), rb = find(b);
            if (ra != rb) { parent[ra] = rb; sz[rb] += sz[ra]; }
            res[i] = sz[find(a)];
        }
        return res;
    }
};
''',

    # gold-40 : 연결 그래프 판별 - 함수 구현형: 참고용 C++ 정답
    "gold-40": r'''#include <bits/stdc++.h>
using namespace std;

// 함수 구현형: 참고용 C++ 정답
struct Solution {
    vector<int> parent;
    int find(int x) {
        while (parent[x] != x) { parent[x] = parent[parent[x]]; x = parent[x]; }
        return x;
    }
    bool solution(int n, vector<vector<int>> edges) {
        parent.resize(n + 1);
        for (int i = 0; i <= n; i++) parent[i] = i;
        for (auto& e : edges) parent[find(e[0])] = find(e[1]);
        set<int> roots;
        for (int i = 1; i <= n; i++) roots.insert(find(i));
        return roots.size() == 1;
    }
};
''',

    # gold-41 : 부분집합 합 개수 (비트마스크) - 함수 구현형: 참고용 C++ 정답
    "gold-41": r'''#include <bits/stdc++.h>
using namespace std;

// 함수 구현형: 참고용 C++ 정답
struct Solution {
    int solution(vector<int> nums, int target) {
        int n = nums.size(), cnt = 0;
        for (int mask = 1; mask < (1 << n); mask++) {
            long long s = 0;
            for (int i = 0; i < n; i++) if ((mask >> i & 1) == 1) s += nums[i];
            if (s == target) cnt++;
        }
        return cnt;
    }
};
''',

    # gold-42 : 회의실 배정 최대 개수 - 함수 구현형: 참고용 C++ 정답
    "gold-42": r'''#include <bits/stdc++.h>
using namespace std;

// 함수 구현형: 참고용 C++ 정답
struct Solution {
    int solution(vector<vector<int>> meetings) {
        sort(meetings.begin(), meetings.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] != b[1] ? a[1] < b[1] : a[0] < b[0];
        });
        int cnt = 0;
        long long end = LLONG_MIN;
        for (auto& m : meetings) {
            if (m[0] >= end) { cnt++; end = m[1]; }
        }
        return cnt;
    }
};
''',

    # gold-43 : LRU 캐시 실행 시간 - 함수 구현형: 참고용 C++ 정답
    "gold-43": r'''#include <bits/stdc++.h>
using namespace std;

// 함수 구현형: 참고용 C++ 정답
struct Solution {
    int solution(int cacheSize, vector<string> requests) {
        if (cacheSize == 0) return (int)requests.size() * 5;
        list<string> cache;
        int time = 0;
        for (string raw : requests) {
            string c = raw;
            for (auto& ch : c) ch = tolower((unsigned char)ch);
            auto it = find(cache.begin(), cache.end(), c);
            if (it != cache.end()) {
                cache.erase(it);
                cache.push_back(c);
                time += 1;
            } else {
                if ((int)cache.size() >= cacheSize) cache.pop_front();
                cache.push_back(c);
                time += 5;
            }
        }
        return time;
    }
};
''',

    # gold-44 : 강의실 최소 개수 - 함수 구현형: 참고용 C++ 정답
    "gold-44": r'''#include <bits/stdc++.h>
using namespace std;

// 함수 구현형: 참고용 C++ 정답
struct Solution {
    int solution(vector<vector<int>> lectures) {
        int n = lectures.size();
        vector<int> starts(n), ends(n);
        for (int i = 0; i < n; i++) { starts[i] = lectures[i][0]; ends[i] = lectures[i][1]; }
        sort(starts.begin(), starts.end());
        sort(ends.begin(), ends.end());
        int rooms = 0, mx = 0, i = 0, j = 0;
        while (i < n) {
            if (starts[i] < ends[j]) { rooms++; i++; mx = max(mx, rooms); }
            else { rooms--; j++; }
        }
        return mx;
    }
};
''',

    # gold-45 : 회전하는 큐 최소 연산
    "gold-45": r'''#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    deque<int> dq;
    for (int i = 1; i <= n; i++) dq.push_back(i);
    int count = 0;
    for (int k = 0; k < m; k++) {
        int t;
        scanf("%d", &t);
        // 현재 큐에서 t 의 위치(idx) 탐색
        int idx = 0;
        for (size_t p = 0; p < dq.size(); p++) if (dq[p] == t) { idx = (int)p; break; }
        int half = (int)dq.size() / 2;
        if (idx <= half) {
            for (int i = 0; i < idx; i++) { dq.push_back(dq.front()); dq.pop_front(); count++; }
        } else {
            for (int i = 0; i < (int)dq.size() - idx; i++) { dq.push_front(dq.back()); dq.pop_back(); count++; }
        }
        dq.pop_front();
    }
    printf("%d\n", count);
    return 0;
}
''',

    # gold-46 : 뱀 게임 시뮬레이션
    "gold-46": r'''#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k;
    scanf("%d", &n);
    scanf("%d", &k);
    set<long long> apple;
    for (int i = 0; i < k; i++) {
        int r, c;
        scanf("%d %d", &r, &c);
        apple.insert((long long)r * 1000 + c);
    }
    int l;
    scanf("%d", &l);
    vector<int> mt(l);
    vector<char> mc(l);
    for (int i = 0; i < l; i++) {
        char ch;
        scanf("%d %c", &mt[i], &ch);
        mc[i] = ch;
    }
    int dr[] = {0, 1, 0, -1}, dc[] = {1, 0, -1, 0};
    int d = 0;
    deque<pair<int,int>> snake;
    snake.push_front({1, 1});
    set<long long> body;
    body.insert(1001LL);
    int time = 0, mi = 0;
    while (true) {
        time++;
        auto head = snake.front();
        int nr = head.first + dr[d], nc = head.second + dc[d];
        long long key = (long long)nr * 1000 + nc;
        if (nr < 1 || nr > n || nc < 1 || nc > n || body.count(key)) break;
        snake.push_front({nr, nc});
        body.insert(key);
        if (apple.count(key)) apple.erase(key);
        else {
            auto t = snake.back(); snake.pop_back();
            body.erase((long long)t.first * 1000 + t.second);
        }
        if (mi < l && mt[mi] == time) {
            d = mc[mi] == 'D' ? (d + 1) % 4 : (d + 3) % 4;
            mi++;
        }
    }
    printf("%d\n", time);
    return 0;
}
''',

    # gold-47 : 최소 비용 경로
    "gold-47": r'''#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    scanf("%d", &n);
    scanf("%d", &m);
    vector<vector<pair<int,int>>> g(n + 1);  // {정점, 가중치}
    for (int i = 0; i < m; i++) {
        int u, v, w;
        scanf("%d %d %d", &u, &v, &w);
        g[u].push_back({v, w});
    }
    int s, e;
    scanf("%d %d", &s, &e);
    const long long INF = LLONG_MAX / 4;
    vector<long long> dist(n + 1, INF);
    dist[s] = 0;
    priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<>> pq;
    pq.push({0, s});
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue;
        for (auto& [v, w] : g[u]) {
            long long nd = d + w;
            if (nd < dist[v]) { dist[v] = nd; pq.push({nd, v}); }
        }
    }
    printf("%lld\n", dist[e]);
    return 0;
}
''',

    # gold-48 : 외판원 순회 최소 비용 - 함수 구현형: 참고용 C++ 정답
    "gold-48": r'''#include <bits/stdc++.h>
using namespace std;

// 함수 구현형: 참고용 C++ 정답
struct Solution {
    int solution(vector<vector<int>> dist) {
        int n = dist.size();
        const int INF = INT_MAX / 4;
        vector<vector<int>> dp(1 << n, vector<int>(n, INF));
        dp[1][0] = 0;
        for (int mask = 0; mask < (1 << n); mask++) {
            for (int u = 0; u < n; u++) {
                if (dp[mask][u] == INF || (mask >> u & 1) == 0) continue;
                for (int v = 0; v < n; v++) {
                    if ((mask >> v & 1) == 1 || dist[u][v] == 0) continue;
                    int nm = mask | (1 << v);
                    if (dp[nm][v] > dp[mask][u] + dist[u][v]) dp[nm][v] = dp[mask][u] + dist[u][v];
                }
            }
        }
        int full = (1 << n) - 1, ans = INF;
        for (int u = 0; u < n; u++) {
            if (dist[u][0] == 0) continue;
            ans = min(ans, dp[full][u] + dist[u][0]);
        }
        return ans == INF ? -1 : ans;
    }
};
''',

    # gold-49 : 카드 합치기 최소 비용 - 함수 구현형: 참고용 C++ 정답
    "gold-49": r'''#include <bits/stdc++.h>
using namespace std;

// 함수 구현형: 참고용 C++ 정답
struct Solution {
    long long solution(vector<int> cards) {
        if (cards.size() <= 1) return 0;
        priority_queue<long long, vector<long long>, greater<>> pq;
        for (int c : cards) pq.push((long long)c);
        long long total = 0;
        while (pq.size() > 1) {
            long long a = pq.top(); pq.pop();
            long long b = pq.top(); pq.pop();
            long long s = a + b;
            total += s;
            pq.push(s);
        }
        return total;
    }
};
''',

    # gold-50 : 요세푸스 순열
    "gold-50": r'''#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    vector<int> list;
    for (int i = 1; i <= n; i++) list.push_back(i);
    string out = "<";
    int idx = 0;
    while (!list.empty()) {
        idx = (idx + k - 1) % (int)list.size();
        out += to_string(list[idx]);
        list.erase(list.begin() + idx);
        if (!list.empty()) out += ", ";
    }
    out += ">";
    printf("%s\n", out.c_str());
    return 0;
}
''',
}
