"""실버 50문제 C++ 정답 코드 맵.

검증된 Java/Python 정답을 C++17 기준으로 번역한 것이다.
- stdin 문제: 완전한 int main() (빠른 입출력 적용)
- func 문제: 동등 C++ 함수 (참고용)
"""

CPP = {
    "silver-01": r'''#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    sort(a.begin(), a.end());          // 오름차순 정렬
    for (int x : a) cout << x << '\n';  // 한 줄에 하나씩 출력
    return 0;
}
''',

    "silver-02": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
bool solution(string s) {
    int cnt = 0;
    for (char c : s) {
        cnt += (c == '(') ? 1 : -1;  // 여는 괄호 +1, 닫는 괄호 -1
        if (cnt < 0) return false;   // 닫는 괄호가 더 많으면 실패
    }
    return cnt == 0;                 // 모두 짝이 맞아야 VPS
}
''',

    "silver-03": r'''#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    unordered_set<int> s;
    for (int i = 0; i < n; i++) { int x; cin >> x; s.insert(x); }
    int m;
    cin >> m;
    string out;
    for (int i = 0; i < m; i++) {
        int x; cin >> x;
        out += (s.count(x) ? "1" : "0");  // 집합에 존재하면 1
        if (i < m - 1) out += ' ';
    }
    cout << out << '\n';
    return 0;
}
''',

    "silver-04": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
int solution(vector<int> coins, int amount) {
    sort(coins.rbegin(), coins.rend());  // 큰 동전부터 사용 (그리디)
    int cnt = 0;
    for (int c : coins) {
        cnt += amount / c;
        amount %= c;
    }
    return amount == 0 ? cnt : -1;        // 거슬러줄 수 없으면 -1
}
''',

    "silver-05": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
vector<int> solution(vector<int> nums, vector<vector<int>> queries) {
    int n = nums.size();
    vector<long long> p(n + 1, 0);          // 누적합 (오버플로 방지 long long)
    for (int k = 0; k < n; k++) p[k + 1] = p[k] + nums[k];
    vector<int> ans;
    for (auto& q : queries) {
        int i = q[0], j = q[1];             // 1-indexed 구간 [i, j]
        ans.push_back((int)(p[j] - p[i - 1]));
    }
    return ans;
}
''',

    "silver-06": r'''#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<pair<int, string>> m(n);
    for (int i = 0; i < n; i++) cin >> m[i].first >> m[i].second;
    // 나이 오름차순, 동일 나이는 가입 순서 유지(안정 정렬)
    stable_sort(m.begin(), m.end(),
        [](const pair<int, string>& a, const pair<int, string>& b) {
            return a.first < b.first;
        });
    string out;
    for (auto& p : m) {
        out += to_string(p.first);
        out += ' ';
        out += p.second;
        out += '\n';
    }
    cout << out;
    return 0;
}
''',

    "silver-07": r'''#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<pair<int, int>> p(n);
    for (int i = 0; i < n; i++) cin >> p[i].first >> p[i].second;
    sort(p.begin(), p.end());  // (x, y) 사전순 정렬
    string out;
    for (auto& q : p) {
        out += to_string(q.first);
        out += ' ';
        out += to_string(q.second);
        out += '\n';
    }
    cout << out;
    return 0;
}
''',

    "silver-08": r'''#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<string> v(n);
    for (int i = 0; i < n; i++) cin >> v[i];
    // 길이 우선, 같으면 사전순
    sort(v.begin(), v.end(), [](const string& a, const string& b) {
        if (a.size() != b.size()) return a.size() < b.size();
        return a < b;
    });
    v.erase(unique(v.begin(), v.end()), v.end());  // 중복 제거
    string out;
    for (auto& w : v) { out += w; out += '\n'; }
    cout << out;
    return 0;
}
''',

    "silver-09": r'''#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long m;
    cin >> n >> m;
    vector<int> t(n);
    long long hi = 0;
    for (int i = 0; i < n; i++) { cin >> t[i]; hi = max(hi, (long long)t[i]); }
    long long lo = 0, ans = 0;
    while (lo <= hi) {                       // 절단기 높이 이분 탐색
        long long mid = (lo + hi) / 2, got = 0;
        for (int x : t) if (x > mid) got += x - mid;
        if (got >= m) { ans = mid; lo = mid + 1; }  // 충분하면 더 높게
        else hi = mid - 1;
    }
    cout << ans << '\n';
    return 0;
}
''',

    "silver-10": r'''#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int k;
    long long n;
    cin >> k >> n;
    vector<long long> a(k);
    long long hi = 1;
    for (int i = 0; i < k; i++) { cin >> a[i]; hi = max(hi, a[i]); }
    long long lo = 1, ans = 0;
    while (lo <= hi) {                        // 랜선 길이 이분 탐색
        long long mid = (lo + hi) / 2, cnt = 0;
        for (long long x : a) cnt += x / mid;
        if (cnt >= n) { ans = mid; lo = mid + 1; }  // 충분하면 더 길게
        else hi = mid - 1;
    }
    cout << ans << '\n';
    return 0;
}
''',

    "silver-11": r'''#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    vector<int> s(arr);
    sort(s.begin(), s.end());
    s.erase(unique(s.begin(), s.end()), s.end());  // 정렬 + 중복 제거
    string out;
    for (int i = 0; i < n; i++) {
        // 압축된 좌표값 = 정렬 배열에서의 인덱스
        int r = lower_bound(s.begin(), s.end(), arr[i]) - s.begin();
        out += to_string(r);
        if (i < n - 1) out += ' ';
    }
    cout << out << '\n';
    return 0;
}
''',

    "silver-12": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> ans;
    for (auto& cmd : commands) {
        int i = cmd[0], j = cmd[1], k = cmd[2];
        vector<int> sub(array.begin() + i - 1, array.begin() + j);  // [i, j] 구간
        sort(sub.begin(), sub.end());
        ans.push_back(sub[k - 1]);  // k번째 수
    }
    return ans;
}
''',

    "silver-13": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
// students: (이름, 점수) 목록
vector<string> solution(vector<pair<string, int>> students) {
    sort(students.begin(), students.end(),
        [](const pair<string, int>& a, const pair<string, int>& b) {
            if (a.second != b.second) return a.second > b.second;  // 점수 내림차순
            return a.first < b.first;                              // 동점은 이름순
        });
    vector<string> ans;
    for (auto& s : students) ans.push_back(s.first);
    return ans;
}
''',

    "silver-14": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
int solution(vector<int> arr, int x) {
    int lo = 0, hi = arr.size();
    while (lo < hi) {                 // lower_bound 직접 구현
        int mid = (lo + hi) / 2;
        if (arr[mid] < x) lo = mid + 1;
        else hi = mid;
    }
    return lo;  // x가 삽입될 위치
}
''',

    "silver-15": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
vector<vector<int>> solution(vector<vector<int>> points, int k) {
    sort(points.begin(), points.end(),
        [](const vector<int>& a, const vector<int>& b) {
            long long da = (long long)a[0]*a[0] + (long long)a[1]*a[1];  // 원점 거리 제곱
            long long db = (long long)b[0]*b[0] + (long long)b[1]*b[1];
            if (da != db) return da < db;
            if (a[0] != b[0]) return a[0] < b[0];
            return a[1] < b[1];
        });
    return vector<vector<int>>(points.begin(), points.begin() + k);  // 가까운 k개
}
''',

    "silver-16": r'''#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> req(n);
    int hi = 0;
    for (int i = 0; i < n; i++) { cin >> req[i]; hi = max(hi, req[i]); }
    long long m;
    cin >> m;
    int lo = 0, ans = 0;
    while (lo <= hi) {                    // 상한액 이분 탐색
        int mid = (lo + hi) / 2;
        long long total = 0;
        for (int x : req) total += min(x, mid);  // 상한을 넘는 요청은 상한만 배정
        if (total <= m) { ans = mid; lo = mid + 1; }  // 예산 내면 더 크게
        else hi = mid - 1;
    }
    cout << ans << '\n';
    return 0;
}
''',

    "silver-17": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
int solution(vector<int> arr, int x) {
    // upper_bound - lower_bound = x의 개수
    auto lo = lower_bound(arr.begin(), arr.end(), x);
    auto hi = upper_bound(arr.begin(), arr.end(), x);
    return (int)(hi - lo);
}
''',

    "silver-18": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
vector<string> solution(vector<string> words) {
    sort(words.begin(), words.end(), [](const string& a, const string& b) {
        if (a.size() != b.size()) return a.size() > b.size();  // 길이 내림차순
        return a < b;                                          // 같으면 사전순
    });
    return words;
}
''',

    "silver-19": r'''#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    sort(arr.begin(), arr.end());
    cout << arr[n / 2] << '\n';  // 정렬 후 중앙값
    return 0;
}
''',

    "silver-20": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
vector<int> solution(vector<int> scores) {
    vector<int> ordered(scores);
    sort(ordered.rbegin(), ordered.rend());  // 내림차순
    unordered_map<int, int> rank;
    for (int i = 0; i < (int)ordered.size(); i++)
        if (!rank.count(ordered[i])) rank[ordered[i]] = i + 1;  // 동점은 같은 순위
    vector<int> ans;
    for (int s : scores) ans.push_back(rank[s]);
    return ans;
}
''',

    "silver-21": r'''#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    string s;
    cin >> s;
    int open = 0;        // 현재 열린 괄호(쇠막대기) 개수
    long long ans = 0;
    for (int i = 0; i < (int)s.size(); i++) {
        if (s[i] == '(') open++;
        else {
            open--;
            if (s[i - 1] == '(') ans += open;  // 레이저: 잘리는 막대 수
            else ans += 1;                     // 막대 끝: 토막 +1
        }
    }
    cout << ans << '\n';
    return 0;
}
''',

    "silver-22": r'''#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    string expr;
    cin >> expr;
    vector<int> stk;
    for (char c : expr) {
        if (isdigit((unsigned char)c)) stk.push_back(c - '0');
        else {
            int b = stk.back(); stk.pop_back();
            int a = stk.back(); stk.pop_back();
            if (c == '+') stk.push_back(a + b);
            else if (c == '-') stk.push_back(a - b);
            else stk.push_back(a * b);
        }
    }
    cout << stk.back() << '\n';  // 후위 표기식 계산 결과
    return 0;
}
''',

    "silver-23": r'''#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> h(n + 1);
    for (int i = 1; i <= n; i++) cin >> h[i];
    vector<pair<int, int>> stk;  // (높이, 인덱스) 단조 스택
    string out;
    for (int i = 1; i <= n; i++) {
        while (!stk.empty() && stk.back().first < h[i]) stk.pop_back();
        out += to_string(stk.empty() ? 0 : stk.back().second);  // 수신 탑
        if (i < n) out += ' ';
        stk.push_back({h[i], i});
    }
    cout << out << '\n';
    return 0;
}
''',

    "silver-24": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
vector<int> solution(vector<int> nums) {
    int n = nums.size();
    vector<int> ans(n, -1);
    vector<int> stk;  // 아직 오큰수를 못 찾은 인덱스들
    for (int i = 0; i < n; i++) {
        while (!stk.empty() && nums[stk.back()] < nums[i]) {
            ans[stk.back()] = nums[i];  // 현재 값이 오큰수
            stk.pop_back();
        }
        stk.push_back(i);
    }
    return ans;
}
''',

    "silver-25": r'''#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    cin >> n >> k;
    deque<int> q;
    for (int i = 1; i <= n; i++) q.push_back(i);
    string out = "<";
    bool first = true;
    while (!q.empty()) {
        for (int i = 0; i < k - 1; i++) {  // k-1번 회전
            q.push_back(q.front());
            q.pop_front();
        }
        if (!first) out += ", ";
        out += to_string(q.front());       // k번째 사람 제거
        q.pop_front();
        first = false;
    }
    out += ">";
    cout << out << '\n';
    return 0;
}
''',

    "silver-26": r'''#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    deque<int> q;
    for (int i = 1; i <= n; i++) q.push_back(i);
    while (q.size() > 1) {
        q.pop_front();              // 맨 위 카드 버림
        q.push_back(q.front());     // 다음 카드를 맨 아래로
        q.pop_front();
    }
    cout << q.front() << '\n';      // 마지막 남은 카드
    return 0;
}
''',

    "silver-27": r'''#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    deque<int> q;
    for (int i = 1; i <= n; i++) q.push_back(i);
    int cnt = 0;
    for (int j = 0; j < m; j++) {
        int t;
        cin >> t;
        int idx = 0;  // 현재 큐에서 목표 원소의 위치
        for (int i = 0; i < (int)q.size(); i++)
            if (q[i] == t) { idx = i; break; }
        int L = q.size();
        if (idx <= L / 2) {              // 왼쪽 회전이 더 가까움
            cnt += idx;
            for (int i = 0; i < idx; i++) { q.push_back(q.front()); q.pop_front(); }
        } else {                         // 오른쪽 회전이 더 가까움
            cnt += L - idx;
            for (int i = 0; i < L - idx; i++) { q.push_front(q.back()); q.pop_back(); }
        }
        q.pop_front();                   // 목표 원소 뽑기
    }
    cout << cnt << '\n';
    return 0;
}
''',

    "silver-28": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
bool solution(string s) {
    int l = 0, r = (int)s.size() - 1;  // 양쪽 끝에서 비교 (덱과 동일 원리)
    while (l < r) {
        if (s[l] != s[r]) return false;
        l++;
        r--;
    }
    return true;
}
''',

    "silver-29": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
int solution(vector<int> nums) {
    map<int, int> c;
    for (int x : nums) c[x]++;          // 빈도 계산
    int best = 0;
    for (auto& e : c) best = max(best, e.second);  // 최대 빈도
    int ans = INT_MAX;
    for (auto& e : c) if (e.second == best) ans = min(ans, e.first);  // 그중 최솟값
    return ans;
}
''',

    "silver-30": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
vector<int> solution(vector<int> nums) {
    unordered_set<int> seen;
    vector<int> res;
    for (int x : nums)
        if (seen.insert(x).second) res.push_back(x);  // 처음 본 값만 추가(순서 유지)
    return res;
}
''',

    "silver-31": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
vector<int> solution(vector<int> a, vector<int> b) {
    unordered_set<int> sa(a.begin(), a.end());
    set<int> inter;                        // 정렬된 교집합
    for (int x : b) if (sa.count(x)) inter.insert(x);
    return vector<int>(inter.begin(), inter.end());
}
''',

    "silver-32": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
vector<int> solution(vector<int> nums, int target) {
    unordered_map<int, int> seen;  // 값 -> 인덱스
    for (int i = 0; i < (int)nums.size(); i++) {
        if (seen.count(target - nums[i]))
            return {seen[target - nums[i]], i};  // 합이 target인 두 인덱스
        seen[nums[i]] = i;
    }
    return {};
}
''',

    "silver-33": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
vector<int> solution(vector<int> nums, int k) {
    sort(nums.begin(), nums.end());                       // 오름차순 정렬
    return vector<int>(nums.begin(), nums.begin() + k);   // 가장 작은 k개
}
''',

    "silver-34": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
int solution(vector<int> nums, int k) {
    sort(nums.begin(), nums.end());
    return nums[nums.size() - k];  // 뒤에서 k번째 = k번째 큰 수
}
''',

    "silver-35": r'''#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    // (절댓값, 원래값) 최소 힙: 절댓값이 같으면 작은 값 먼저
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    string out;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        if (x == 0) {
            if (pq.empty()) out += "0";
            else { out += to_string(pq.top().second); pq.pop(); }
            out += '\n';
        } else {
            pq.push({abs(x), x});
        }
    }
    cout << out;
    return 0;
}
''',

    "silver-36": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
int solution(vector<vector<int>> meetings) {
    sort(meetings.begin(), meetings.end(), [](const vector<int>& a, const vector<int>& b) {
        if (a[1] != b[1]) return a[1] < b[1];  // 종료 시각 오름차순
        return a[0] < b[0];                    // 같으면 시작 시각순
    });
    int cnt = 0, last = -1;
    for (auto& m : meetings) {
        if (m[0] >= last) { cnt++; last = m[1]; }  // 겹치지 않으면 선택
    }
    return cnt;
}
''',

    "silver-37": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
int solution(vector<int> coins, int amount) {
    int m = *min_element(coins.begin(), coins.end());  // 가장 작은 단위
    if (amount % m != 0) return -1;                    // 나눠떨어지지 않으면 불가
    return amount / m;                                 // 최대 개수
}
''',

    "silver-38": r'''#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    int coins[] = {50000, 10000, 5000, 1000, 500, 100, 50, 10};
    int cnt = 0;
    for (int c : coins) { cnt += n / c; n %= c; }  // 큰 단위부터 그리디
    cout << cnt << '\n';
    return 0;
}
''',

    "silver-39": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
int solution(vector<int> nums, int target) {
    int left = 0, s = 0, cnt = 0;
    for (int right = 0; right < (int)nums.size(); right++) {  // 투 포인터
        s += nums[right];
        while (s > target) { s -= nums[left]; left++; }       // 합이 크면 왼쪽 축소
        if (s == target) cnt++;
    }
    return cnt;
}
''',

    "silver-40": r'''#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, s;
    cin >> n >> s;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    int left = 0, cur = 0, best = n + 1;
    for (int right = 0; right < n; right++) {  // 슬라이딩 윈도우
        cur += a[right];
        while (cur >= s) {                     // 조건 만족 시 길이 갱신 후 축소
            best = min(best, right - left + 1);
            cur -= a[left++];
        }
    }
    cout << (best <= n ? best : 0) << '\n';    // 불가능하면 0
    return 0;
}
''',

    "silver-41": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
int solution(vector<int> cards, int m) {
    int n = cards.size(), best = 0;
    for (int i = 0; i < n; i++)               // 세 장 조합 완전 탐색
        for (int j = i + 1; j < n; j++)
            for (int k = j + 1; k < n; k++) {
                int s = cards[i] + cards[j] + cards[k];
                if (s <= m && s > best) best = s;  // m 이하 중 최대 합
            }
    return best;
}
''',

    "silver-42": r'''#include <bits/stdc++.h>
using namespace std;
vector<string> board;
// (r, c)에서 시작하는 8x8 영역을 다시 칠하는 최소 횟수
int cost(int r, int c) {
    int cnt = 0;
    for (int i = 0; i < 8; i++)
        for (int j = 0; j < 8; j++) {
            char exp = ((i + j) % 2 == 0) ? 'W' : 'B';  // 좌상단이 흰색 기준
            if (board[r + i][c + j] != exp) cnt++;
        }
    return min(cnt, 64 - cnt);  // 흰색 기준 / 검은색 기준 중 작은 값
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    board.resize(n);
    for (int i = 0; i < n; i++) cin >> board[i];
    int best = 64;
    for (int r = 0; r <= n - 8; r++)
        for (int c = 0; c <= m - 8; c++)
            best = min(best, cost(r, c));
    cout << best << '\n';
    return 0;
}
''',

    "silver-43": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
long long gcd_(long long a, long long b) { return b == 0 ? a : gcd_(b, a % b); }
vector<long long> solution(long long a, long long b) {
    long long g = gcd_(a, b);
    return {g, a * b / g};  // {최대공약수, 최소공배수}
}
''',

    "silver-44": r'''#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int m, n;
    cin >> m >> n;
    vector<bool> sieve(n + 1, true);  // 에라토스테네스의 체
    if (n >= 0) sieve[0] = false;
    if (n >= 1) sieve[1] = false;
    for (int i = 2; (long long)i * i <= n; i++)
        if (sieve[i])
            for (int j = i * i; j <= n; j += i) sieve[j] = false;
    string out;
    for (int i = max(m, 2); i <= n; i++)
        if (sieve[i]) { out += to_string(i); out += '\n'; }
    cout << out;
    return 0;
}
''',

    "silver-45": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
long long solution(int n, int r) {
    long long result = 1;
    r = min(r, n - r);                    // 대칭성 이용
    for (int i = 0; i < r; i++) {
        result = result * (n - i) / (i + 1);  // 곱하고 나누어 오버플로 완화
    }
    return result;
}
''',

    "silver-46": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
string solution(int n, int b) {
    if (n == 0) return "0";
    string digits = "0123456789ABCDEF";
    string res;
    while (n > 0) {
        res = digits[n % b] + res;  // 나머지를 앞에 붙임
        n /= b;
    }
    return res;
}
''',

    "silver-47": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
long long solution(int n) {
    if (n == 0) return 0;
    return 2 * solution(n - 1) + 1;  // 하노이 탑 점화식
}
''',

    "silver-48": r'''#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    long long a = 0, b = 1;
    for (int i = 0; i < n; i++) {  // F(n) 반복 계산
        long long t = a + b;
        a = b;
        b = t;
    }
    cout << a << '\n';
    return 0;
}
''',

    "silver-49": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
bool solution(vector<int> nums, int target) {
    int l = 0, r = (int)nums.size() - 1;  // 정렬된 배열 양끝 투 포인터
    while (l < r) {
        int s = nums[l] + nums[r];
        if (s == target) return true;
        else if (s < target) l++;
        else r--;
    }
    return false;
}
''',

    "silver-50": r'''#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    long long n;
    cin >> n;
    long long cnt = 0, p = 5;
    while (p <= n) { cnt += n / p; p *= 5; }  // n!에 포함된 5의 개수
    cout << cnt << '\n';
    return 0;
}
''',
}
