"""Bronze 50문제 C++ 정답 코드.

검증된 Java/Python 정답을 C++(g++ -std=c++17)로 번역한 것.
- type=="stdin": 표준입력/표준출력 완전한 int main() 프로그램.
- type=="func":  프로그래머스식 함수 구현형(참고용).
"""

CPP = {
    "bronze-01": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    int a, b;
    cin >> a >> b;      // 두 정수 입력
    cout << a + b << "\n";  // 합 출력
    return 0;
}
''',
    "bronze-02": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin >> n;
    string sb;
    for (int i = 1; i <= n; i++) {   // i번째 줄에 별 i개
        for (int j = 0; j < i; j++) sb += '*';
        sb += '\n';
    }
    cout << sb;
    return 0;
}
''',
    "bronze-03": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
string solution(int num){
    return num % 2 == 0 ? "Even" : "Odd";   // 짝수면 Even, 홀수면 Odd
}
''',
    "bronze-04": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin >> n;
    int best = INT_MIN;
    for (int i = 0; i < n; i++) {
        int x; cin >> x;
        best = max(best, x);   // 최댓값 갱신
    }
    cout << best << "\n";
    return 0;
}
''',
    "bronze-05": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
string solution(string s){
    reverse(s.begin(), s.end());   // 문자열 뒤집기
    return s;
}
''',
    "bronze-06": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    int a, b;
    cin >> a >> b;
    cout << a + b << "\n";   // 합
    cout << a - b << "\n";   // 차
    cout << a * b << "\n";   // 곱
    cout << a / b << "\n";   // 몫
    cout << a % b << "\n";   // 나머지
    return 0;
}
''',
    "bronze-07": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
vector<int> solution(int a, int b){
    return {a / b, a % b};   // {몫, 나머지}
}
''',
    "bronze-08": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    int score;
    cin >> score;
    string grade;
    if (score >= 90) grade = "A";
    else if (score >= 80) grade = "B";
    else if (score >= 70) grade = "C";
    else if (score >= 60) grade = "D";
    else grade = "F";
    cout << grade << "\n";
    return 0;
}
''',
    "bronze-09": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    int year;
    cin >> year;
    // 4의 배수이고 100의 배수가 아니거나, 400의 배수면 윤년
    bool leap = (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
    cout << (leap ? 1 : 0) << "\n";
    return 0;
}
''',
    "bronze-10": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    int x, y;
    cin >> x >> y;
    if (x > 0) cout << (y > 0 ? 1 : 4) << "\n";   // 오른쪽: 1사분면/4사분면
    else cout << (y > 0 ? 2 : 3) << "\n";          // 왼쪽: 2사분면/3사분면
    return 0;
}
''',
    "bronze-11": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
int solution(int a, int b, int c){
    return max(a, max(b, c));   // 세 수 중 최댓값
}
''',
    "bronze-12": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
int solution(int n){
    return n < 0 ? -n : n;   // 음수면 부호 반전
}
''',
    "bronze-13": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
int solution(int n){
    if (n > 0) return 1;        // 양수
    else if (n < 0) return -1;  // 음수
    else return 0;              // 0
}
''',
    "bronze-14": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    int a, b;
    cin >> a >> b;
    int t = a; a = b; b = t;   // 두 수 교환
    cout << a << " " << b << "\n";
    return 0;
}
''',
    "bronze-15": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
vector<int> solution(int total){
    int h = total / 3600;          // 시
    int m = (total % 3600) / 60;   // 분
    int s = total % 60;            // 초
    return {h, m, s};
}
''',
    "bronze-16": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
int solution(int km, int m){
    return km * 1000 + m;   // km를 m로 변환 후 합산
}
''',
    "bronze-17": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    string name;
    int age;
    cin >> name >> age;
    cout << name << "(" << age << "세)" << "\n";   // 이름(나이세)
    return 0;
}
''',
    "bronze-18": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    int a, b;
    cin >> a >> b;
    if (a > b) cout << ">" << "\n";
    else if (a < b) cout << "<" << "\n";
    else cout << "==" << "\n";
    return 0;
}
''',
    "bronze-19": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
int solution(int a, int b, int c){
    return (a + b + c) / 3;   // 세 과목 평균(정수 나눗셈)
}
''',
    "bronze-20": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin >> n;
    int coins[] = {500, 100, 50, 10};
    int count = 0;
    for (int coin : coins) {   // 큰 동전부터 그리디로 사용
        count += n / coin;
        n %= coin;
    }
    cout << count << "\n";
    return 0;
}
''',
    "bronze-21": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin >> n;
    int total = 0;
    for (int i = 0; i < n; i++) {
        int x; cin >> x;
        total += x;   // 누적 합
    }
    cout << total << "\n";
    return 0;
}
''',
    "bronze-22": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
int solution(vector<int> scores){
    int total = 0;
    for (int s : scores) total += s;
    return total / (int)scores.size();   // 평균(정수 나눗셈)
}
''',
    "bronze-23": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin >> n;
    int cnt = 0;
    for (int i = 0; i < n; i++) {
        int x; cin >> x;
        if (x % 2 == 0) cnt++;   // 짝수 카운트
    }
    cout << cnt << "\n";
    return 0;
}
''',
    "bronze-24": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin >> n;
    int cnt = 0;
    for (int i = 1; i <= n; i++) {
        if (n % i == 0) cnt++;   // 약수 카운트
    }
    cout << cnt << "\n";
    return 0;
}
''',
    "bronze-25": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
int solution(int n){
    int total = 0;
    for (int x = 1; x <= n; x++) {
        if (x % 3 == 0 || x % 5 == 0) total += x;   // 3 또는 5의 배수 합
    }
    return total;
}
''',
    "bronze-26": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
int solution(int a, int b){
    int answer = 1;
    int m = min(a, b);
    for (int i = 1; i <= m; i++) {
        if (a % i == 0 && b % i == 0) answer = i;   // 공약수 중 최댓값
    }
    return answer;
}
''',
    "bronze-27": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    int a, b;
    cin >> a >> b;
    int i = 1;
    while (i % a != 0 || i % b != 0) i++;   // a,b 모두로 나눠지는 최소 수
    cout << i << "\n";
    return 0;
}
''',
    "bronze-28": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin >> n;
    for (int i = 1; i <= 9; i++) {
        cout << n << " * " << i << " = " << (n * i) << "\n";   // 구구단 한 줄씩
    }
    return 0;
}
''',
    "bronze-29": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
vector<vector<int>> solution(int n){
    vector<vector<int>> table(n, vector<int>(n));
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            table[i - 1][j - 1] = i * j;   // 곱셈표 채우기
        }
    }
    return table;
}
''',
    "bronze-30": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
vector<int> solution(vector<int> arr){
    vector<int> res(arr.size());
    int s = 0;
    for (size_t i = 0; i < arr.size(); i++) {
        s += arr[i];   // 누적합
        res[i] = s;
    }
    return res;
}
''',
    "bronze-31": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin >> n;
    string sb;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            if (j > 1) sb += ' ';   // 숫자 사이 공백
            sb += to_string(j);
        }
        sb += '\n';
    }
    cout << sb;
    return 0;
}
''',
    "bronze-32": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin >> n;
    long long total = 0;   // 오버플로 방지
    for (int i = 1; i <= n; i++) total += i;
    cout << total << "\n";
    return 0;
}
''',
    "bronze-33": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
long long solution(int n){
    long long result = 1;
    for (int i = 1; i <= n; i++) result *= i;   // n!
    return result;
}
''',
    "bronze-34": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
int solution(long long n){
    int total = 0;
    if (n == 0) return 0;
    while (n > 0) {
        total += (int)(n % 10);   // 마지막 자리 더하기
        n /= 10;
    }
    return total;
}
''',
    "bronze-35": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin >> n;
    string sb;
    for (int i = n; i >= 1; i--) {   // n부터 1까지 카운트다운
        sb += to_string(i);
        sb += '\n';
    }
    cout << sb;
    return 0;
}
''',
    "bronze-36": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
string solution(string s){
    transform(s.begin(), s.end(), s.begin(), ::toupper);   // 모두 대문자로
    return s;
}
''',
    "bronze-37": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    string s;
    char c;
    cin >> s >> c;   // 문자열과 찾을 문자
    int cnt = 0;
    for (size_t i = 0; i < s.length(); i++)
        if (s[i] == c) cnt++;
    cout << cnt << "\n";
    return 0;
}
''',
    "bronze-38": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
int solution(string s){
    int cnt = 0;
    string vowels = "aeiou";
    for (size_t i = 0; i < s.length(); i++)
        if (vowels.find(s[i]) != string::npos) cnt++;   // 모음이면 카운트
    return cnt;
}
''',
    "bronze-39": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
string solution(string s, string a, string b){
    // s 안의 모든 a를 b로 치환
    if (a.empty()) return s;
    string res;
    size_t pos = 0;
    while (pos < s.length()) {
        if (s.compare(pos, a.length(), a) == 0) {
            res += b;
            pos += a.length();
        } else {
            res += s[pos];
            pos++;
        }
    }
    return res;
}
''',
    "bronze-40": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    string s;
    getline(cin, s);
    // 앞뒤 공백 제거
    size_t start = s.find_first_not_of(" \t\r\n");
    size_t end = s.find_last_not_of(" \t\r\n");
    if (start == string::npos) cout << "\n";
    else cout << s.substr(start, end - start + 1) << "\n";
    return 0;
}
''',
    "bronze-41": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
int solution(vector<int> numbers){
    int total = 0;
    for (int x : numbers) total += x;   // 원소 합
    return total;
}
''',
    "bronze-42": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
vector<int> solution(vector<int> arr){
    int n = (int)arr.size();
    vector<int> r(n);
    for (int i = 0; i < n; i++) r[i] = arr[n - 1 - i];   // 거꾸로 복사
    return r;
}
''',
    "bronze-43": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
int solution(vector<int> arr, int target){
    for (int i = 0; i < (int)arr.size(); i++)
        if (arr[i] == target) return i;   // 처음 발견한 위치
    return -1;
}
''',
    "bronze-44": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin >> n;
    bool prime = n >= 2;
    for (int i = 2; (long long) i * i <= n; i++) {   // 제곱근까지 검사
        if (n % i == 0) { prime = false; break; }
    }
    cout << (prime ? "소수" : "합성수") << "\n";
    return 0;
}
''',
    "bronze-45": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
int solution(int n){
    int cnt = 0;
    for (int i = 1; i <= n; i++)
        if (n % i == 0) cnt++;   // 약수 카운트
    return cnt;
}
''',
    "bronze-46": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
string solution(int n){
    if (n == 0) return "0";
    string res;
    while (n > 0) {           // 2로 나눈 나머지를 역순으로
        res += char('0' + (n % 2));
        n /= 2;
    }
    reverse(res.begin(), res.end());
    return res;
}
''',
    "bronze-47": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    char c;
    cin >> c;
    cout << (int) c << "\n";   // 아스키 코드 값
    return 0;
}
''',
    "bronze-48": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
string solution(string s){
    transform(s.begin(), s.end(), s.begin(), ::tolower);   // 모두 소문자로
    return s;
}
''',
    "bronze-49": r'''// 함수 구현형: 참고용 C++ 정답
#include <bits/stdc++.h>
using namespace std;
string solution(string s, string c){
    // s 안의 모든 c를 제거(빈 문자열로 치환)
    if (c.empty()) return s;
    string res;
    size_t pos = 0;
    while (pos < s.length()) {
        if (s.compare(pos, c.length(), c) == 0) {
            pos += c.length();
        } else {
            res += s[pos];
            pos++;
        }
    }
    return res;
}
''',
    "bronze-50": r'''#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    int k, cnt = 0;
    cin >> k;
    for (int x : arr) if (x == k) cnt++;   // k의 등장 횟수
    cout << cnt << "\n";
    return 0;
}
''',
}
