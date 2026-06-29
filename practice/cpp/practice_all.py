"""유형별 실전 51문제 C++ 정답 코드 맵.

검증된 Java/Python 정답을 C++(g++ -std=c++17)로 정확히 번역한 것.
stdin 문제는 완전한 int main(), func 문제는 동등한 C++ 함수로 제공한다.
"""

CPP = {

# ============================ 구현/시뮬레이션 ============================

"impl-01": r'''
#include <bits/stdc++.h>
using namespace std;
int main() {
    int R, C;
    cin >> R >> C;
    vector<string> grid(R);
    for (int i = 0; i < R; i++) cin >> grid[i];
    int r, c; string sd;
    cin >> r >> c >> sd;
    string cmds; cin >> cmds;
    string dirs = "NESW";
    int dr[] = {-1, 0, 1, 0};
    int dc[] = {0, 1, 0, -1};
    int d = (int) dirs.find(sd[0]);   // 시작 방향 인덱스
    for (char ch : cmds) {
        if (ch == 'L') d = (d + 3) % 4;        // 좌회전
        else if (ch == 'R') d = (d + 1) % 4;   // 우회전
        else if (ch == 'F') {                  // 전진
            int nr = r + dr[d], nc = c + dc[d];
            if (nr >= 1 && nr <= R && nc >= 1 && nc <= C && grid[nr - 1][nc - 1] != '#') {
                r = nr; c = nc;
            }
        }
    }
    cout << r << " " << c << " " << dirs[d] << "\n";
    return 0;
}
''',

"impl-02": r'''
// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<vector<int>> solution(vector<vector<int>> board, int k) {
        k %= 4;
        vector<vector<int>> b = board;
        for (int t = 0; t < k; t++) {
            int R = b.size(), C = b[0].size();
            vector<vector<int>> nb(C, vector<int>(R));   // 시계방향 90도 회전
            for (int i = 0; i < R; i++)
                for (int j = 0; j < C; j++)
                    nb[j][R - 1 - i] = b[i][j];
            b = nb;
        }
        return b;
    }
};
''',

"impl-03": r'''
#include <bits/stdc++.h>
using namespace std;
int main() {
    int R, C;
    cin >> R >> C;
    vector<string> g(R);
    for (int i = 0; i < R; i++) cin >> g[i];
    int total = 0;
    int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};
    while (true) {
        vector<vector<char>> visited(R, vector<char>(C, 0));
        vector<vector<char>> mark(R, vector<char>(C, 0));
        int removed = 0;
        for (int i = 0; i < R; i++) for (int j = 0; j < C; j++) {
            if (g[i][j] == '.' || visited[i][j]) continue;
            char color = g[i][j];
            vector<pair<int,int>> comp;
            queue<pair<int,int>> dq;
            dq.push({i, j}); visited[i][j] = 1;
            while (!dq.empty()) {                        // 같은 색 연결요소 탐색
                auto c = dq.front(); dq.pop();
                comp.push_back(c);
                for (int d = 0; d < 4; d++) {
                    int nx = c.first + dx[d], ny = c.second + dy[d];
                    if (nx >= 0 && nx < R && ny >= 0 && ny < C && !visited[nx][ny] && g[nx][ny] == color) {
                        visited[nx][ny] = 1; dq.push({nx, ny});
                    }
                }
            }
            if ((int) comp.size() >= 3)
                for (auto &c : comp) mark[c.first][c.second] = 1;
        }
        for (int i = 0; i < R; i++) for (int j = 0; j < C; j++)
            if (mark[i][j]) { g[i][j] = '.'; removed++; }
        if (removed == 0) break;
        total += removed;
        for (int col = 0; col < C; col++) {              // 중력 적용 (아래로 떨어짐)
            vector<char> st;
            for (int row = 0; row < R; row++) if (g[row][col] != '.') st.push_back(g[row][col]);
            int p = (int) st.size() - 1;
            for (int row = R - 1; row >= 0; row--) g[row][col] = (p >= 0) ? st[p--] : '.';
        }
    }
    cout << total << "\n";
    return 0;
}
''',

"impl-04": r'''
// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<int> solution(vector<int> fees, vector<string> records) {
        int baseT = fees[0], baseF = fees[1], unitT = fees[2], unitF = fees[3];
        unordered_map<string, int> inTime;
        map<string, int> total;   // 차량번호 오름차순 정렬 보장
        for (auto &rec : records) {
            stringstream ss(rec);
            string t, num, act;
            ss >> t >> num >> act;
            int h = stoi(t.substr(0, 2)), m = stoi(t.substr(3, 2));
            int minutes = h * 60 + m;
            if (act == "IN") {
                inTime[num] = minutes;
            } else {
                total[num] += minutes - inTime[num];
                inTime.erase(num);
            }
        }
        for (auto &e : inTime)   // 출차 기록 없는 차량은 23:59 출차 처리
            total[e.first] += 23 * 60 + 59 - e.second;
        vector<int> answer;
        for (auto &e : total) {
            int dur = e.second;
            int fee = baseF;
            if (dur > baseT)
                fee += (int) ceil((dur - baseT) / (double) unitT) * unitF;
            answer.push_back(fee);
        }
        return answer;
    }
};
''',

"impl-05": r'''
// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int solution(string s) {
        int n = s.size();
        int best = n;
        for (int unit = 1; unit <= n / 2; unit++) {        // 압축 단위 길이
            int comp = 0, cnt = 1;
            string prev = s.substr(0, min(unit, n));
            for (int i = unit; i < n; i += unit) {
                string cur = s.substr(i, min(unit, n - i));
                if (cur == prev) {
                    cnt++;
                } else {
                    comp += (cnt > 1 ? (int) to_string(cnt).size() : 0) + (int) prev.size();
                    prev = cur;
                    cnt = 1;
                }
            }
            comp += (cnt > 1 ? (int) to_string(cnt).size() : 0) + (int) prev.size();
            best = min(best, comp);
        }
        return best;
    }
};
''',

# ============================ DFS/BFS ============================

"bfs-01": r'''
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, m;
    cin >> n >> m;
    vector<string> g(n);
    for (int i = 0; i < n; i++) cin >> g[i];
    vector<vector<char>> vis(n, vector<char>(m, 0));
    int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};
    int cnt = 0;
    for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) {
        if (g[i][j] == '1' && !vis[i][j]) {
            cnt++;
            vis[i][j] = 1;
            queue<pair<int,int>> q;
            q.push({i, j});
            while (!q.empty()) {                  // 하나의 섬 BFS
                auto c = q.front(); q.pop();
                for (int d = 0; d < 4; d++) {
                    int nx = c.first + dx[d], ny = c.second + dy[d];
                    if (nx >= 0 && nx < n && ny >= 0 && ny < m && g[nx][ny] == '1' && !vis[nx][ny]) {
                        vis[nx][ny] = 1;
                        q.push({nx, ny});
                    }
                }
            }
        }
    }
    cout << cnt << "\n";
    return 0;
}
''',

"bfs-02": r'''
// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int solution(int n, vector<vector<int>> computers) {
        vector<char> visited(n, 0);
        int cnt = 0;
        for (int s = 0; s < n; s++) {
            if (!visited[s]) {
                cnt++;
                vector<int> stk;
                stk.push_back(s);
                visited[s] = 1;
                while (!stk.empty()) {            // DFS 로 연결요소 탐색
                    int x = stk.back(); stk.pop_back();
                    for (int y = 0; y < n; y++)
                        if (computers[x][y] == 1 && !visited[y]) {
                            visited[y] = 1;
                            stk.push_back(y);
                        }
                }
            }
        }
        return cnt;
    }
};
''',

"bfs-03": r'''
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, m;
    cin >> n >> m;
    vector<string> g(n);
    for (int i = 0; i < n; i++) cin >> g[i];
    vector<vector<int>> dist(n, vector<int>(m, 0));
    dist[0][0] = 1;
    queue<pair<int,int>> q;
    q.push({0, 0});
    int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};
    while (!q.empty()) {
        auto c = q.front(); q.pop();
        for (int d = 0; d < 4; d++) {
            int nx = c.first + dx[d], ny = c.second + dy[d];
            if (nx >= 0 && nx < n && ny >= 0 && ny < m && g[nx][ny] == '1' && dist[nx][ny] == 0) {
                dist[nx][ny] = dist[c.first][c.second] + 1;
                q.push({nx, ny});
            }
        }
    }
    int ans = dist[n - 1][m - 1];
    cout << (ans != 0 ? ans : -1) << "\n";
    return 0;
}
''',

"bfs-04": r'''
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> g(n, vector<int>(m));
    vector<vector<int>> dist(n, vector<int>(m, -1));
    for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) cin >> g[i][j];
    queue<pair<int,int>> q;
    for (int i = 0; i < n; i++) for (int j = 0; j < m; j++)
        if (g[i][j] == 2) { dist[i][j] = 0; q.push({i, j}); }   // 다중 시작점
    int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};
    while (!q.empty()) {
        auto c = q.front(); q.pop();
        for (int d = 0; d < 4; d++) {
            int nx = c.first + dx[d], ny = c.second + dy[d];
            if (nx >= 0 && nx < n && ny >= 0 && ny < m && g[nx][ny] == 1 && dist[nx][ny] == -1) {
                dist[nx][ny] = dist[c.first][c.second] + 1;
                q.push({nx, ny});
            }
        }
    }
    int ans = 0; bool ok = true;
    for (int i = 0; i < n; i++) for (int j = 0; j < m; j++)
        if (g[i][j] == 1) {
            if (dist[i][j] == -1) ok = false;
            else ans = max(ans, dist[i][j]);
        }
    cout << (ok ? ans : -1) << "\n";
    return 0;
}
''',

"bfs-05": r'''
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, m;
    cin >> n >> m;
    vector<string> g(n);
    for (int i = 0; i < n; i++) cin >> g[i];
    // dist[x][y][b] : (x,y) 도달, b=벽을 부쉈는지 여부(0/1)
    vector<vector<array<int,2>>> dist(n, vector<array<int,2>>(m, {-1, -1}));
    dist[0][0][0] = 1;
    queue<array<int,3>> q;
    q.push({0, 0, 0});
    int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};
    int ans = -1;
    while (!q.empty()) {
        auto c = q.front(); q.pop();
        int x = c[0], y = c[1], b = c[2];
        if (x == n - 1 && y == m - 1) { ans = dist[x][y][b]; break; }
        for (int d = 0; d < 4; d++) {
            int nx = x + dx[d], ny = y + dy[d];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (g[nx][ny] == '0' && dist[nx][ny][b] == -1) {
                dist[nx][ny][b] = dist[x][y][b] + 1;
                q.push({nx, ny, b});
            } else if (g[nx][ny] == '1' && b == 0 && dist[nx][ny][1] == -1) {
                dist[nx][ny][1] = dist[x][y][0] + 1;   // 벽 한 번 부수기
                q.push({nx, ny, 1});
            }
        }
    }
    cout << ans << "\n";
    return 0;
}
''',

# ============================ 완전탐색/백트래킹 ============================

"bruteforce-01": r'''
#include <bits/stdc++.h>
using namespace std;
int n, m;
vector<int> pick;
string out;
void rec(int depth, int start) {
    if (depth == m) {                      // M개 선택 완료
        for (int i = 0; i < m; i++) {
            out += to_string(pick[i]);
            if (i < m - 1) out += ' ';
        }
        out += '\n';
        return;
    }
    for (int v = start; v <= n; v++) {     // 오름차순 조합
        pick[depth] = v;
        rec(depth + 1, v + 1);
    }
}
int main() {
    cin >> n >> m;
    pick.assign(m, 0);
    rec(0, 1);
    cout << out;
    return 0;
}
''',

"bruteforce-02": r'''
// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int solution(vector<int> menu, int budget) {
        int n = menu.size(), best = -1;
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                for (int k = j + 1; k < n; k++) {     // 3개 조합 완전탐색
                    int sum = menu[i] + menu[j] + menu[k];
                    int mn = min(menu[i], min(menu[j], menu[k]));
                    int pay = sum - mn;               // 가장 싼 것 무료
                    if (pay <= budget && pay > best) best = pay;
                }
        return best;
    }
};
''',

"bruteforce-03": r'''
// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int solution(vector<vector<string>> relation) {
        int rows = relation.size(), cols = relation[0].size();
        vector<int> candidates;
        for (int mask = 1; mask < (1 << cols); mask++) {
            bool superset = false;                  // 이미 후보키의 상위집합이면 제외(최소성)
            for (int c : candidates) if ((mask & c) == c) { superset = true; break; }
            if (superset) continue;
            unordered_set<string> seen;
            bool uniq = true;
            for (int r = 0; r < rows; r++) {        // 유일성 검사
                string key;
                for (int c = 0; c < cols; c++)
                    if (mask & (1 << c)) { key += relation[r][c]; key += '#'; }
                if (!seen.insert(key).second) { uniq = false; break; }
            }
            if (uniq) candidates.push_back(mask);
        }
        return (int) candidates.size();
    }
};
''',

"bruteforce-04": r'''
#include <bits/stdc++.h>
using namespace std;
int n;
long long cnt = 0;
vector<int> perm;
vector<char> used;
bool isPrime(int x) {
    if (x < 2) return false;
    for (long long i = 2; i * i <= x; i++) if (x % i == 0) return false;
    return true;
}
void rec(int depth) {
    if (depth == n) { cnt++; return; }
    for (int v = 1; v <= n; v++) {
        if (used[v]) continue;
        if (depth > 0 && !isPrime(perm[depth - 1] + v)) continue;   // 이웃 합이 소수여야
        used[v] = 1;
        perm[depth] = v;
        rec(depth + 1);
        used[v] = 0;
    }
}
int main() {
    cin >> n;
    perm.assign(n, 0);
    used.assign(n + 1, 0);
    rec(0);
    cout << cnt << "\n";
    return 0;
}
''',

# ============================ 정렬 ============================

"sort-01": r'''
// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
class Solution {
    pair<string,int> key(const string &f) {
        int i = 0;
        string head;
        while (i < (int) f.size() && !isdigit((unsigned char) f[i])) head += f[i++];
        string num;
        while (i < (int) f.size() && isdigit((unsigned char) f[i]) && (int) num.size() < 5) num += f[i++];
        for (auto &ch : head) ch = tolower((unsigned char) ch);
        return {head, stoi(num)};
    }
public:
    vector<string> solution(vector<string> files) {
        vector<string> arr = files;
        stable_sort(arr.begin(), arr.end(), [&](const string &a, const string &b) {
            auto ka = key(a), kb = key(b);
            if (ka.first != kb.first) return ka.first < kb.first;   // HEAD 사전순
            return ka.second < kb.second;                          // NUMBER 수치순
        });
        return arr;
    }
};
''',

"sort-02": r'''
// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<string> solution(vector<string> logs) {
        vector<string> letters, digits;
        for (auto &lg : logs) {
            int sp = lg.find(' ');
            string rest = lg.substr(sp + 1);
            if (isdigit((unsigned char) rest[0])) digits.push_back(lg);   // 숫자 로그
            else letters.push_back(lg);                                   // 문자 로그
        }
        stable_sort(letters.begin(), letters.end(), [](const string &a, const string &b) {
            string ra = a.substr(a.find(' ') + 1), rb = b.substr(b.find(' ') + 1);
            if (ra != rb) return ra < rb;                  // 내용 우선
            return a.substr(0, a.find(' ')) < b.substr(0, b.find(' '));  // 식별자 비교
        });
        vector<string> res = letters;
        for (auto &d : digits) res.push_back(d);           // 숫자 로그는 원래 순서 유지
        return res;
    }
};
''',

"sort-03": r'''
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    cin >> n;
    vector<array<string,4>> arr(n);    // name, kor, eng, math (문자열로 보관)
    for (int i = 0; i < n; i++)
        cin >> arr[i][0] >> arr[i][1] >> arr[i][2] >> arr[i][3];
    stable_sort(arr.begin(), arr.end(), [](const array<string,4> &a, const array<string,4> &b) {
        int ka = stoi(a[1]), kb = stoi(b[1]);
        if (ka != kb) return ka > kb;                  // 국어 내림차순
        int ea = stoi(a[2]), eb = stoi(b[2]);
        if (ea != eb) return ea < eb;                  // 영어 오름차순
        int ma = stoi(a[3]), mb = stoi(b[3]);
        if (ma != mb) return ma > mb;                  // 수학 내림차순
        return a[0] < b[0];                            // 이름 사전순
    });
    string out;
    for (auto &s : arr) { out += s[0]; out += '\n'; }
    cout << out;
    return 0;
}
''',

"sort-04": r'''
// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<string> solution(vector<string> words, string order) {
        int idx[128] = {0};
        for (int i = 0; i < (int) order.size(); i++) idx[(int) order[i]] = i;
        vector<string> arr = words;
        stable_sort(arr.begin(), arr.end(), [&](const string &a, const string &b) {
            int n = min(a.size(), b.size());
            for (int i = 0; i < n; i++) {
                int ca = idx[(int) a[i]], cb = idx[(int) b[i]];
                if (ca != cb) return ca < cb;          // 외계어 사전순 비교
            }
            return a.size() < b.size();                // 접두사가 먼저
        });
        return arr;
    }
};
''',

# ============================ 해시 ============================

"hash-01": r'''
// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    string solution(vector<string> participant, vector<string> completion) {
        unordered_map<string, int> mp;
        for (auto &p : participant) mp[p]++;
        for (auto &c : completion) mp[c]--;
        for (auto &e : mp)
            if (e.second > 0) return e.first;   // 완주하지 못한 1명
        return "";
    }
};
''',

"hash-02": r'''
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    cin >> n;
    unordered_map<int, int> mp;
    for (int i = 0; i < n; i++) {
        int v; cin >> v;
        mp[v]++;
    }
    int best = 0, bestCnt = -1;
    for (auto &e : mp) {
        int v = e.first, c = e.second;
        if (c > bestCnt || (c == bestCnt && v < best)) { best = v; bestCnt = c; }  // 최빈값, 동률시 작은 수
    }
    cout << best << "\n";
    return 0;
}
''',

"hash-03": r'''
// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    bool solution(vector<string> phoneBook) {
        sort(phoneBook.begin(), phoneBook.end());        // 정렬하면 접두어는 바로 앞에 위치
        for (int i = 0; i + 1 < (int) phoneBook.size(); i++)
            if (phoneBook[i + 1].compare(0, phoneBook[i].size(), phoneBook[i]) == 0)
                return false;
        return true;
    }
};
''',

"hash-04": r'''
// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int solution(vector<vector<string>> clothes) {
        unordered_map<string, int> mp;
        for (auto &c : clothes) mp[c[1]]++;     // 종류별 개수
        long long answer = 1;
        for (auto &e : mp) answer *= (e.second + 1);   // 각 종류 (개수+1), 안 입는 경우 포함
        return (int)(answer - 1);               // 모두 안 입는 경우 제외
    }
};
''',

# ============================ 투포인터/누적합 ============================

"twopointer-01": r'''
// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int solution(vector<int> nums, int target) {
        int left = 0, cur = 0, cnt = 0;
        for (int right = 0; right < (int) nums.size(); right++) {
            cur += nums[right];
            while (cur > target && left <= right) cur -= nums[left++];   // 합이 넘으면 왼쪽 축소
            if (cur == target) cnt++;
        }
        return cnt;
    }
};
''',

"twopointer-02": r'''
// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int solution(vector<int> nums, int target) {
        int left = 0, cur = 0, best = INT_MAX;
        for (int right = 0; right < (int) nums.size(); right++) {
            cur += nums[right];
            while (cur >= target) {                       // 조건 만족하는 동안 최소 길이 갱신
                best = min(best, right - left + 1);
                cur -= nums[left++];
            }
        }
        return best == INT_MAX ? 0 : best;
    }
};
''',

"twopointer-03": r'''
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    vector<long long> prefix(n + 1, 0);
    for (int k = 1; k <= n; k++) {
        long long v; cin >> v;
        prefix[k] = prefix[k - 1] + v;        // 누적합
    }
    string out;
    for (int t = 0; t < q; t++) {
        int i, j; cin >> i >> j;
        out += to_string(prefix[j] - prefix[i - 1]);
        out += '\n';
    }
    cout << out;
    return 0;
}
''',

"twopointer-04": r'''
// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int solution(vector<int> nums, int k) {
        unordered_map<int, int> count;
        int left = 0, distinct = 0, best = 0;
        for (int right = 0; right < (int) nums.size(); right++) {
            if (count[nums[right]] == 0) distinct++;
            count[nums[right]]++;
            while (distinct > k) {                    // 서로 다른 원소가 k개 초과면 축소
                count[nums[left]]--;
                if (count[nums[left]] == 0) distinct--;
                left++;
            }
            best = max(best, right - left + 1);
        }
        return best;
    }
};
''',

# ============================ 이분탐색 ============================

"binsearch-01": r'''
// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    long long solution(int n, vector<int> times) {
        long long lo = 1, hi = 0;
        for (int t : times) hi = max(hi, (long long) t * n);
        while (lo < hi) {                          // 정답(시간)에 대한 이분탐색
            long long mid = (lo + hi) / 2;
            long long done = 0;
            for (int t : times) done += mid / t;   // mid 시간 동안 처리 가능 인원
            if (done >= n) hi = mid; else lo = mid + 1;
        }
        return lo;
    }
};
''',

"binsearch-02": r'''
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    cin >> n;
    vector<int> req(n);
    int maxReq = 0; long long sum = 0;
    for (int i = 0; i < n; i++) {
        cin >> req[i];
        maxReq = max(maxReq, req[i]); sum += req[i];
    }
    long long m;
    cin >> m;
    if (sum <= m) { cout << maxReq << "\n"; return 0; }   // 전부 배정 가능
    int lo = 0, hi = maxReq;
    while (lo < hi) {                               // 상한선에 대한 이분탐색
        int mid = (lo + hi + 1) / 2;
        long long total = 0;
        for (int r : req) total += min(r, mid);
        if (total <= m) lo = mid; else hi = mid - 1;
    }
    cout << lo << "\n";
    return 0;
}
''',

"binsearch-03": r'''
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n; long long m;
    cin >> n >> m;
    vector<int> trees(n);
    int mx = 0;
    for (int i = 0; i < n; i++) { cin >> trees[i]; mx = max(mx, trees[i]); }
    int lo = 0, hi = mx;
    while (lo < hi) {                               // 절단기 높이에 대한 이분탐색
        int mid = (int)(((long long) lo + hi + 1) / 2);
        long long total = 0;
        for (int t : trees) if (t > mid) total += t - mid;
        if (total >= m) lo = mid; else hi = mid - 1;
    }
    cout << lo << "\n";
    return 0;
}
''',

"binsearch-04": r'''
// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int solution(vector<int> houses, int c) {
        sort(houses.begin(), houses.end());
        int lo = 1, hi = houses.back() - houses[0], answer = 0;
        while (lo <= hi) {                          // 최소 인접거리에 대한 이분탐색
            int mid = (lo + hi) / 2;
            int cnt = 1, last = houses[0];
            for (int i = 1; i < (int) houses.size(); i++)
                if (houses[i] - last >= mid) { cnt++; last = houses[i]; }
            if (cnt >= c) { answer = mid; lo = mid + 1; }   // 더 큰 거리 시도
            else hi = mid - 1;
        }
        return answer;
    }
};
''',

# ============================ 그리디 ============================

"greedy-01": r'''
// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int solution(vector<int> people, int limit) {
        sort(people.begin(), people.end());
        int l = 0, r = (int) people.size() - 1, boats = 0;
        while (l <= r) {                            // 가장 가벼운+무거운 사람 짝짓기
            if (people[l] + people[r] <= limit) l++;
            r--;
            boats++;
        }
        return boats;
    }
};
''',

"greedy-02": r'''
// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int solution(int n, vector<int> lost, vector<int> reserve) {
        set<int> lostSet(lost.begin(), lost.end());
        set<int> resSet(reserve.begin(), reserve.end());
        vector<int> both;
        for (int x : lostSet) if (resSet.count(x)) both.push_back(x);  // 도난+여벌 동시
        for (int x : both) { lostSet.erase(x); resSet.erase(x); }
        int answer = n - (int) lostSet.size();
        for (int r : resSet) {                      // 작은 번호부터 앞->뒤 순서로 빌려줌
            if (lostSet.count(r - 1)) { lostSet.erase(r - 1); answer++; }
            else if (lostSet.count(r + 1)) { lostSet.erase(r + 1); answer++; }
        }
        return answer;
    }
};
''',

"greedy-03": r'''
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    cin >> n;
    vector<pair<int,int>> r(n);   // (start, end)
    for (int i = 0; i < n; i++) cin >> r[i].first >> r[i].second;
    sort(r.begin(), r.end(), [](const pair<int,int> &a, const pair<int,int> &b) {
        return a.second < b.second;               // 끝점 기준 정렬
    });
    int cnt = 0, last = -30001;
    for (auto &c : r)
        if (c.first > last) { cnt++; last = c.second; }   // 겹치지 않으면 카메라 설치
    cout << cnt << "\n";
    return 0;
}
''',

"greedy-04": r'''
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    cin >> n;
    vector<pair<long long,long long>> m(n);   // (start, end)
    for (int i = 0; i < n; i++) cin >> m[i].first >> m[i].second;
    sort(m.begin(), m.end(), [](const pair<long long,long long> &a, const pair<long long,long long> &b) {
        if (a.second != b.second) return a.second < b.second;   // 끝나는 시간 우선
        return a.first < b.first;
    });
    int cnt = 0; long long end = 0;
    for (auto &c : m)
        if (c.first >= end) { cnt++; end = c.second; }   // 이전 회의와 안 겹치면 선택
    cout << cnt << "\n";
    return 0;
}
''',

# ============================ DP ============================

"dp-01": r'''
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    cin >> n;
    vector<vector<int>> tri(n);
    for (int i = 0; i < n; i++) {
        tri[i].resize(i + 1);
        for (int j = 0; j <= i; j++) cin >> tri[i][j];
    }
    for (int i = 1; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            if (j == 0) tri[i][j] += tri[i - 1][0];
            else if (j == i) tri[i][j] += tri[i - 1][i - 1];
            else tri[i][j] += max(tri[i - 1][j - 1], tri[i - 1][j]);   // 위 두 칸 중 큰 값
        }
    }
    int ans = 0;
    for (int v : tri[n - 1]) ans = max(ans, v);
    cout << ans << "\n";
    return 0;
}
''',

"dp-02": r'''
// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int solution(int m, int n, vector<vector<int>> puddles) {
        const long long MOD = 1000000007;
        set<pair<int,int>> puddle;
        for (auto &p : puddles) puddle.insert({p[1], p[0]});   // (y, x)
        vector<vector<long long>> dp(n + 1, vector<long long>(m + 1, 0));
        dp[1][1] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (i == 1 && j == 1) continue;
                if (puddle.count({i, j})) { dp[i][j] = 0; continue; }  // 물 웅덩이
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD;        // 위+왼쪽
            }
        }
        return (int) dp[n][m];
    }
};
''',

"dp-03": r'''
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    cin >> n;
    vector<int> a(n), b(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < n; i++) cin >> b[i];
    vector<array<int,3>> dp(n);   // 0: 안뗌, 1: 위 스티커, 2: 아래 스티커
    dp[0] = {0, a[0], b[0]};
    for (int i = 1; i < n; i++) {
        dp[i][0] = max({dp[i - 1][0], dp[i - 1][1], dp[i - 1][2]});
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + a[i];   // 위는 이전 위 못붙임
        dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + b[i];
    }
    cout << max({dp[n - 1][0], dp[n - 1][1], dp[n - 1][2]}) << "\n";
    return 0;
}
''',

"dp-04": r'''
// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
class Solution {
    int rob(const vector<int> &a, int lo, int hi) {
        int prev = 0, cur = 0;
        for (int i = lo; i <= hi; i++) {
            int t = max(cur, prev + a[i]);   // 인접한 집은 못 털기
            prev = cur; cur = t;
        }
        return cur;
    }
public:
    int solution(vector<int> money) {
        int n = money.size();
        if (n == 1) return money[0];
        // 원형이므로 첫 집/마지막 집 중 하나만 포함하는 두 경우로 분리
        return max(rob(money, 0, n - 2), rob(money, 1, n - 1));
    }
};
''',

"dp-05": r'''
// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int solution(vector<int> nums) {
        vector<int> tails;   // tails[i]: 길이 i+1 증가수열의 최소 끝값
        for (int x : nums) {
            auto it = lower_bound(tails.begin(), tails.end(), x);
            if (it == tails.end()) tails.push_back(x);
            else *it = x;
        }
        return (int) tails.size();
    }
};
''',

# ============================ 다익스트라/최단경로 ============================

"dijkstra-01": r'''
// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int solution(int N, vector<vector<int>> road, int K) {
        const long long INF = LLONG_MAX;
        vector<vector<pair<int,long long>>> g(N + 1);
        for (auto &r : road) {
            g[r[0]].push_back({r[1], r[2]});
            g[r[1]].push_back({r[0], r[2]});
        }
        vector<long long> dist(N + 1, INF);
        dist[1] = 0;
        priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<>> pq;
        pq.push({0, 1});
        while (!pq.empty()) {
            auto [d, u] = pq.top(); pq.pop();
            if (d > dist[u]) continue;
            for (auto &nx : g[u]) {
                long long nd = d + nx.second;
                if (nd < dist[nx.first]) { dist[nx.first] = nd; pq.push({nd, nx.first}); }
            }
        }
        int cnt = 0;
        for (int i = 1; i <= N; i++) if (dist[i] <= K) cnt++;   // K 이하 마을 수
        return cnt;
    }
};
''',

"dijkstra-02": r'''
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<pair<int,long long>>> g(n + 1);
    for (int i = 0; i < m; i++) {
        int a, b; long long c;
        cin >> a >> b >> c;
        g[a].push_back({b, c});       // 단방향 간선
    }
    int s, e;
    cin >> s >> e;
    vector<long long> dist(n + 1, LLONG_MAX);
    dist[s] = 0;
    priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<>> pq;
    pq.push({0, s});
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue;
        for (auto &nx : g[u]) {
            long long nd = d + nx.second;
            if (nd < dist[nx.first]) { dist[nx.first] = nd; pq.push({nd, nx.first}); }
        }
    }
    cout << (dist[e] == LLONG_MAX ? -1 : dist[e]) << "\n";
    return 0;
}
''',

"dijkstra-03": r'''
// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int solution(int n, int s, int a, int b, vector<vector<int>> fares) {
        const long long INF = LLONG_MAX / 4;
        vector<vector<long long>> dist(n + 1, vector<long long>(n + 1, INF));
        for (int i = 1; i <= n; i++) dist[i][i] = 0;
        for (auto &f : fares) {
            dist[f[0]][f[1]] = min(dist[f[0]][f[1]], (long long) f[2]);
            dist[f[1]][f[0]] = min(dist[f[1]][f[0]], (long long) f[2]);
        }
        for (int k = 1; k <= n; k++)                 // 플로이드-워셜
            for (int i = 1; i <= n; i++)
                for (int j = 1; j <= n; j++)
                    if (dist[i][k] + dist[k][j] < dist[i][j])
                        dist[i][j] = dist[i][k] + dist[k][j];
        long long ans = INF;
        for (int k = 1; k <= n; k++)                 // k 까지 합승 후 분리
            ans = min(ans, dist[s][k] + dist[k][a] + dist[k][b]);
        return (int) ans;
    }
};
''',

# ============================ 유니온파인드 ============================

"union-01": r'''
// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
class Solution {
    vector<int> parent;
    int find(int x) {
        while (parent[x] != x) { parent[x] = parent[parent[x]]; x = parent[x]; }
        return x;
    }
    void uni(int a, int b) {
        int ra = find(a), rb = find(b);
        if (ra != rb) parent[ra] = rb;
    }
public:
    int solution(int n, vector<vector<int>> computers) {
        parent.resize(n);
        for (int i = 0; i < n; i++) parent[i] = i;
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                if (computers[i][j] == 1) uni(i, j);
        set<int> roots;
        for (int i = 0; i < n; i++) roots.insert(find(i));   // 서로 다른 루트 = 그룹 수
        return (int) roots.size();
    }
};
''',

"union-02": r'''
#include <bits/stdc++.h>
using namespace std;
vector<int> parent;
int find(int x) {
    while (parent[x] != x) { parent[x] = parent[parent[x]]; x = parent[x]; }
    return x;
}
int main() {
    int v, e;
    cin >> v >> e;
    vector<array<int,3>> edges(e);   // (cost, a, b)
    for (int i = 0; i < e; i++) {
        int a, b, c;
        cin >> a >> b >> c;          // 입력: 정점 a b 비용 c
        edges[i] = {c, a, b};
    }
    sort(edges.begin(), edges.end(), [](const array<int,3> &x, const array<int,3> &y) {
        return x[0] < y[0];          // 비용 오름차순 (크루스칼)
    });
    parent.resize(v + 1);
    for (int i = 0; i <= v; i++) parent[i] = i;
    long long total = 0; int used = 0;
    for (auto &ed : edges) {
        int ra = find(ed[1]), rb = find(ed[2]);
        if (ra != rb) { parent[ra] = rb; total += ed[0]; if (++used == v - 1) break; }
    }
    cout << total << "\n";
    return 0;
}
''',

"union-03": r'''
// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
class Solution {
    vector<int> parent, sz;
    int find(int x) {
        while (parent[x] != x) { parent[x] = parent[parent[x]]; x = parent[x]; }
        return x;
    }
    void uni(int a, int b) {
        int ra = find(a), rb = find(b);
        if (ra != rb) { parent[ra] = rb; sz[rb] += sz[ra]; }   // 그룹 크기 합치기
    }
public:
    int solution(int n, vector<vector<int>> relations) {
        parent.resize(n + 1); sz.assign(n + 1, 1);
        for (int i = 0; i <= n; i++) parent[i] = i;
        for (auto &r : relations) uni(r[0], r[1]);
        int best = 0;
        for (int i = 1; i <= n; i++) best = max(best, sz[find(i)]);   // 가장 큰 그룹
        return best;
    }
};
''',

# ============================ 힙/우선순위큐 ============================

"heap-01": r'''
// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int solution(vector<int> scoville, int K) {
        priority_queue<long long, vector<long long>, greater<>> pq;   // 최소 힙
        for (int s : scoville) pq.push((long long) s);
        int count = 0;
        while (pq.size() > 1 && pq.top() < K) {
            long long a = pq.top(); pq.pop();
            long long b = pq.top(); pq.pop();
            pq.push(a + b * 2);            // 가장 안 매운 두 음식 섞기
            count++;
        }
        return pq.top() >= K ? count : -1;
    }
};
''',

"heap-02": r'''
#include <bits/stdc++.h>
using namespace std;
int main() {
    int t;
    cin >> t;
    // (값, 삽입인덱스) 쌍. 지연 삭제용 alive 배열 사용
    priority_queue<pair<long long,long long>, vector<pair<long long,long long>>, greater<>> minh;
    priority_queue<pair<long long,long long>> maxh;
    vector<char> alive(t, 0);
    long long nxt = 0; int size = 0;
    for (int i = 0; i < t; i++) {
        string op; long long num;
        cin >> op >> num;
        if (op == "I") {
            minh.push({num, nxt});
            maxh.push({num, nxt});
            alive[nxt] = 1; nxt++; size++;
        } else {
            if (size == 0) continue;
            if (num == 1) {               // 최댓값 삭제
                while (!maxh.empty() && !alive[maxh.top().second]) maxh.pop();
                alive[maxh.top().second] = 0; maxh.pop(); size--;
            } else {                      // 최솟값 삭제
                while (!minh.empty() && !alive[minh.top().second]) minh.pop();
                alive[minh.top().second] = 0; minh.pop(); size--;
            }
        }
    }
    while (!minh.empty() && !alive[minh.top().second]) minh.pop();
    while (!maxh.empty() && !alive[maxh.top().second]) maxh.pop();
    if (size == 0 || minh.empty() || maxh.empty()) cout << "EMPTY" << "\n";
    else cout << maxh.top().first << " " << minh.top().first << "\n";
    return 0;
}
''',

"heap-03": r'''
// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    long long solution(vector<int> cards) {
        if (cards.size() <= 1) return 0;
        priority_queue<long long, vector<long long>, greater<>> pq;   // 최소 힙
        for (int c : cards) pq.push((long long) c);
        long long total = 0;
        while (pq.size() > 1) {           // 가장 작은 두 묶음을 계속 합치기
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

# ============================ 세그먼트트리 ============================

"segtree-01": r'''
// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
class Solution {
    vector<long long> tree;
    int sz;
    void update(int idx, long long val) {
        int p = sz + idx; tree[p] = val; p /= 2;
        while (p >= 1) { tree[p] = tree[2 * p] + tree[2 * p + 1]; p /= 2; }
    }
    long long query(int l, int r) {       // [l, r] 구간 합
        long long res = 0; l += sz; r += sz + 1;
        while (l < r) {
            if (l & 1) res += tree[l++];
            if (r & 1) res += tree[--r];
            l /= 2; r /= 2;
        }
        return res;
    }
public:
    vector<int> solution(vector<int> sales, vector<vector<int>> queries) {
        int n = sales.size(); sz = 1;
        while (sz < n) sz *= 2;
        tree.assign(2 * sz, 0);
        for (int i = 0; i < n; i++) tree[sz + i] = sales[i];
        for (int p = sz - 1; p >= 1; p--) tree[p] = tree[2 * p] + tree[2 * p + 1];
        vector<int> out;
        for (auto &q : queries) {
            if (q[0] == 1) update(q[1] - 1, q[2]);            // 갱신
            else out.push_back((int) query(q[1] - 1, q[2] - 1));  // 구간 합 질의
        }
        return out;
    }
};
''',

"segtree-02": r'''
#include <bits/stdc++.h>
using namespace std;
vector<long long> tree;
int sz;
const long long NEG = LLONG_MIN;
void update(int idx, long long val) {
    int p = sz + idx; tree[p] = val; p /= 2;
    while (p >= 1) { tree[p] = max(tree[2 * p], tree[2 * p + 1]); p /= 2; }
}
long long query(int l, int r) {           // [l, r] 구간 최댓값
    long long res = NEG; l += sz; r += sz + 1;
    while (l < r) {
        if (l & 1) res = max(res, tree[l++]);
        if (r & 1) res = max(res, tree[--r]);
        l /= 2; r /= 2;
    }
    return res;
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    sz = 1;
    while (sz < n) sz *= 2;
    tree.assign(2 * sz, NEG);
    for (int i = 0; i < n; i++) cin >> tree[sz + i];
    for (int p = sz - 1; p >= 1; p--) tree[p] = max(tree[2 * p], tree[2 * p + 1]);
    string out;
    for (int i = 0; i < q; i++) {
        int type, a, b;
        cin >> type >> a >> b;
        if (type == 1) update(a - 1, b);
        else { out += to_string(query(a - 1, b - 1)); out += '\n'; }
    }
    cout << out;
    return 0;
}
''',

"segtree-03": r'''
// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
// 질의 표현: op="U"(갱신) 또는 "Q"(구간 최솟값 질의)
struct Query { string op; int a, b; };
class Solution {
    vector<long long> tree;
    int sz;
    static const long long INF = LLONG_MAX;
    void update(int idx, long long val) {
        int p = sz + idx; tree[p] = val; p /= 2;
        while (p >= 1) { tree[p] = min(tree[2 * p], tree[2 * p + 1]); p /= 2; }
    }
    long long query(int l, int r) {       // [l, r] 구간 최솟값
        long long res = INF; l += sz; r += sz + 1;
        while (l < r) {
            if (l & 1) res = min(res, tree[l++]);
            if (r & 1) res = min(res, tree[--r]);
            l /= 2; r /= 2;
        }
        return res;
    }
public:
    vector<int> solution(vector<int> arr, vector<Query> queries) {
        int n = arr.size(); sz = 1;
        while (sz < n) sz *= 2;
        tree.assign(2 * sz, INF);
        for (int i = 0; i < n; i++) tree[sz + i] = arr[i];
        for (int p = sz - 1; p >= 1; p--) tree[p] = min(tree[2 * p], tree[2 * p + 1]);
        vector<int> out;
        for (auto &q : queries) {
            if (q.op == "U") update(q.a - 1, q.b);
            else out.push_back((int) query(q.a - 1, q.b - 1));
        }
        return out;
    }
};
''',

}
