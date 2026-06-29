"""C++ 기초 문법 (스타터 — 더 많은 항목은 추가 가능)."""

from engine.models import Lesson

LESSONS = [

    Lesson(
        id="cpp-basic-01",
        lang="cpp", level="기초",
        title="변수와 기본 타입",
        summary="int / long long / double / char / bool",
        explanation=(
            "C++ 은 변수를 쓰기 전에 타입을 함께 선언하는 정적 타입 언어다.\n"
            "정수 int(보통 32비트), 더 큰 정수 long long(64비트), 실수 double,\n"
            "문자 char(작은따옴표 'A'), 참/거짓 bool(true/false) 이 기본 타입이다.\n"
            "boolalpha 를 켜면 bool 이 0/1 대신 true/false 로 출력된다."
        ),
        usage="값 저장의 기본. 큰 수가 나오는 문제(누적합, 곱)는 처음부터 long long 을 쓰면 안전하다.",
        cons="타입을 직접 골라야 하고, 범위를 넘으면(오버플로) 경고 없이 값이 망가진다. 초기화를 빠뜨리면 쓰레기값이 들어간다.",
        code=(
            "#include <bits/stdc++.h>\n"
            "using namespace std;\n"
            "\n"
            "int main() {\n"
            "    // 각 기본 타입을 고정값으로 선언해 본다\n"
            "    int a = 10;            // 정수 (보통 32비트)\n"
            "    long long big = 10000000000LL;  // 32비트 범위를 넘는 큰 정수\n"
            "    double d = 3.14;       // 실수\n"
            "    char c = 'A';          // 문자 하나\n"
            "    bool flag = true;      // 참/거짓\n"
            "\n"
            "    cout << \"a = \" << a << '\\n';\n"
            "    cout << \"big = \" << big << '\\n';\n"
            "    cout << \"d = \" << d << '\\n';\n"
            "    cout << \"c = \" << c << '\\n';\n"
            "    cout << boolalpha << \"flag = \" << flag << '\\n';  // true 로 출력\n"
            "    return 0;\n"
            "}\n"
        ),
    ),

    Lesson(
        id="cpp-basic-02",
        lang="cpp", level="기초",
        title="표준 입출력 cin / cout",
        summary="cin 으로 입력 · cout 으로 출력",
        explanation=(
            "표준 입력은 cin >> 변수, 표준 출력은 cout << 값 으로 한다.\n"
            ">> 는 공백/줄바꿈을 기준으로 값을 끊어 읽고, << 는 여러 값을 이어서 출력한다.\n"
            "줄바꿈은 '\\n' 또는 endl 을 쓴다(endl 은 버퍼를 비워서 약간 느리다).\n"
            "속도가 필요하면 main 맨 앞에 ios::sync_with_stdio(false); cin.tie(nullptr); 를 둔다."
        ),
        usage="모든 입출력의 기본. 백준 같은 표준입력 문제에서 cin 으로 받고 cout 으로 답을 낸다.",
        cons="cin >> 는 줄 단위가 아니라 공백 단위라 한 줄 전체(공백 포함)를 읽으려면 getline 을 따로 써야 한다.",
        code=(
            "#include <bits/stdc++.h>\n"
            "using namespace std;\n"
            "\n"
            "int main() {\n"
            "    // 표준입력 없이 데모하기 위해 cin 대신 고정값을 사용한다\n"
            "    int x = 3, y = 5;        // 원래라면 cin >> x >> y;\n"
            "    cout << \"두 수: \" << x << \" \" << y << '\\n';\n"
            "    cout << \"합: \" << (x + y) << '\\n';\n"
            "    cout << \"곱: \" << (x * y) << '\\n';\n"
            "\n"
            "    // 여러 값을 한 줄에 이어서 출력\n"
            "    cout << x << \" + \" << y << \" = \" << (x + y) << '\\n';\n"
            "    return 0;\n"
            "}\n"
        ),
    ),

    Lesson(
        id="cpp-basic-03",
        lang="cpp", level="기초",
        title="조건문과 반복문",
        summary="if / else · for · while",
        explanation=(
            "조건은 if / else if / else 로 분기한다. 조건식은 true/false 로 평가된다.\n"
            "반복은 for(초기식; 조건; 증감식) 와 while(조건) 두 가지가 기본이다.\n"
            "break 로 반복을 즉시 끝내고, continue 로 다음 회차로 건너뛴다.\n"
            "C++ 의 % 는 나머지 연산자라서 짝수/배수 판별에 자주 쓴다."
        ),
        usage="모든 흐름 제어의 기본. 합 구하기, 개수 세기, 조건 분기 등 거의 모든 문제에 등장한다.",
        cons="반복 조건이나 증감을 잘못 쓰면 무한 루프에 빠진다. 인덱스 범위를 넘으면 배열에서 오류가 난다.",
        code=(
            "#include <bits/stdc++.h>\n"
            "using namespace std;\n"
            "\n"
            "int main() {\n"
            "    // 1~10 중 짝수의 합을 구한다\n"
            "    int total = 0;\n"
            "    for (int i = 1; i <= 10; i++) {\n"
            "        if (i % 2 == 0) {      // 짝수만 더한다\n"
            "            total += i;\n"
            "        }\n"
            "    }\n"
            "    cout << \"짝수합: \" << total << '\\n';   // 30\n"
            "\n"
            "    // while 로 같은 수를 거꾸로 출력\n"
            "    int n = 5;\n"
            "    while (n > 0) {\n"
            "        cout << n << ' ';\n"
            "        n--;\n"
            "    }\n"
            "    cout << '\\n';   // 5 4 3 2 1\n"
            "    return 0;\n"
            "}\n"
        ),
    ),

    Lesson(
        id="cpp-basic-04",
        lang="cpp", level="기초",
        title="배열과 vector 기초",
        summary="고정 배열 · 가변 배열 vector",
        explanation=(
            "고정 크기 배열은 int arr[5]; 처럼 선언하며 크기를 바꿀 수 없다.\n"
            "vector<int> 는 크기를 자유롭게 늘릴 수 있는 가변 배열로, push_back 으로 추가한다.\n"
            "원소 개수는 v.size(), 접근은 v[i] 로 한다. 범위 기반 for(int x : v) 로 순회할 수 있다.\n"
            "정렬은 sort(v.begin(), v.end()) 처럼 <algorithm> 의 함수를 쓴다."
        ),
        usage="여러 값을 모아 다룰 때 기본. 입력 개수가 가변이면 vector 가 편하고 안전하다.",
        cons="고정 배열은 범위를 넘어 접근해도 막아주지 않아 위험하다. vector 도 v[i] 는 범위 검사를 하지 않는다.",
        code=(
            "#include <bits/stdc++.h>\n"
            "using namespace std;\n"
            "\n"
            "int main() {\n"
            "    // 고정 크기 배열\n"
            "    int arr[5] = {5, 2, 9, 1, 7};\n"
            "    int sum = 0;\n"
            "    for (int i = 0; i < 5; i++) sum += arr[i];\n"
            "    cout << \"배열 합: \" << sum << '\\n';   // 24\n"
            "\n"
            "    // 가변 배열 vector\n"
            "    vector<int> v;\n"
            "    v.push_back(3);\n"
            "    v.push_back(1);\n"
            "    v.push_back(2);\n"
            "    sort(v.begin(), v.end());   // 오름차순 정렬\n"
            "\n"
            "    cout << \"정렬된 vector:\";\n"
            "    for (int x : v) cout << ' ' << x;   // 1 2 3\n"
            "    cout << '\\n';\n"
            "    cout << \"크기: \" << v.size() << '\\n';\n"
            "    return 0;\n"
            "}\n"
        ),
    ),

    Lesson(
        id="cpp-basic-05",
        lang="cpp", level="기초",
        title="string 기초",
        summary="std::string · 연결 · 길이 · 부분 문자열",
        explanation=(
            "C++ 의 문자열은 std::string 을 쓴다. C 스타일 char 배열보다 안전하고 편하다.\n"
            "+ 로 이어붙이고, s.size()/s.length() 로 길이를 구한다. s[i] 로 한 글자에 접근한다.\n"
            "s.substr(시작, 길이) 로 부분 문자열을, s.find(\"...\") 로 위치를 찾는다.\n"
            "공백 포함 한 줄 입력은 getline(cin, s) 로 받는다(여기선 데모라 직접 대입)."
        ),
        usage="이름/문장 처리, 문자열 뒤집기, 부분 문자열 탐색 등 문자열 문제 전반에 쓴다.",
        cons="큰 문자열을 + 로 반복해서 이어붙이면 복사가 잦아 느려질 수 있다. += 나 reserve 로 최적화한다.",
        code=(
            "#include <bits/stdc++.h>\n"
            "using namespace std;\n"
            "\n"
            "int main() {\n"
            "    string a = \"Hello\";\n"
            "    string b = \"World\";\n"
            "    string c = a + \", \" + b + \"!\";   // 문자열 연결\n"
            "\n"
            "    cout << c << '\\n';                 // Hello, World!\n"
            "    cout << \"길이: \" << c.size() << '\\n';\n"
            "    cout << \"첫 글자: \" << c[0] << '\\n';\n"
            "    cout << \"부분: \" << c.substr(7, 5) << '\\n';   // World\n"
            "\n"
            "    // 문자열 뒤집기\n"
            "    string r = a;\n"
            "    reverse(r.begin(), r.end());\n"
            "    cout << \"뒤집기: \" << r << '\\n';   // olleH\n"
            "    return 0;\n"
            "}\n"
        ),
    ),

    Lesson(
        id="cpp-basic-06",
        lang="cpp", level="기초",
        title="형변환과 정수 오버플로",
        summary="int ↔ double · long long 으로 오버플로 방지",
        explanation=(
            "int 끼리 나누면 소수점이 버려진다(정수 나눗셈). 실수 결과가 필요하면 double 로 형변환한다.\n"
            "형변환은 (double)x 또는 static_cast<double>(x) 처럼 쓴다.\n"
            "int 는 약 ±21억까지만 담는다. 곱셈/누적합이 이를 넘으면 오버플로로 값이 망가진다.\n"
            "큰 결과가 예상되면 long long 을 쓰고, 곱셈 중간 계산도 long long 으로 올려야 한다."
        ),
        usage="평균 계산(실수 변환), 큰 수 곱/합 문제(long long)에서 정확한 답을 내기 위해 필수다.",
        cons="형변환을 빠뜨리면 조용히 틀린 답이 나온다(에러 없이). 어디서 int 곱이 일어나는지 늘 신경 써야 한다.",
        code=(
            "#include <bits/stdc++.h>\n"
            "using namespace std;\n"
            "\n"
            "int main() {\n"
            "    int a = 7, b = 2;\n"
            "    cout << \"정수 나눗셈: \" << (a / b) << '\\n';        // 3 (소수점 버림)\n"
            "    cout << \"실수 나눗셈: \" << ((double)a / b) << '\\n'; // 3.5\n"
            "\n"
            "    // 오버플로 예시\n"
            "    int x = 100000;\n"
            "    long long good = (long long)x * x;  // 먼저 long long 으로 올려 곱한다\n"
            "    cout << \"올바른 곱: \" << good << '\\n';   // 10000000000\n"
            "\n"
            "    // 큰 누적합도 long long 으로 안전하게\n"
            "    long long sum = 0;\n"
            "    for (int i = 1; i <= 1000000; i++) sum += i;\n"
            "    cout << \"1~100만 합: \" << sum << '\\n';   // 500000500000\n"
            "    return 0;\n"
            "}\n"
        ),
    ),

    Lesson(
        id="cpp-basic-07",
        lang="cpp", level="기초",
        title="연산자",
        summary="산술 · 비교 · 논리 · 복합대입",
        explanation=(
            "산술 연산자 + - * / % (나머지), 비교 연산자 == != < <= > >= 가 기본이다.\n"
            "논리 연산자 && (그리고), || (또는), ! (부정) 로 조건을 조합한다.\n"
            "복합 대입 += -= *= /= %= 로 자기 자신을 갱신하고, ++ -- 로 1씩 증감한다.\n"
            "삼항 연산자 조건 ? 참값 : 거짓값 으로 간단한 분기를 한 줄에 쓸 수 있다."
        ),
        usage="모든 계산과 조건 판단의 기본 도구. 짝수 판별, 최댓값 선택 등에 두루 쓴다.",
        cons="&& 와 ||, == 와 = 를 헷갈리면 미묘한 버그가 난다. 정수끼리의 / 는 나머지를 버린다는 점도 주의.",
        code=(
            "#include <bits/stdc++.h>\n"
            "using namespace std;\n"
            "\n"
            "int main() {\n"
            "    int a = 17, b = 5;\n"
            "    cout << \"a + b = \" << (a + b) << '\\n';   // 22\n"
            "    cout << \"a / b = \" << (a / b) << '\\n';   // 3\n"
            "    cout << \"a % b = \" << (a % b) << '\\n';    // 2\n"
            "\n"
            "    // 비교와 논리 (boolalpha 로 true/false 출력)\n"
            "    cout << boolalpha;\n"
            "    cout << \"a > b 그리고 b > 0: \" << (a > b && b > 0) << '\\n';  // true\n"
            "\n"
            "    // 삼항 연산자로 더 큰 값 고르기\n"
            "    int mx = (a > b) ? a : b;\n"
            "    cout << \"더 큰 값: \" << mx << '\\n';   // 17\n"
            "\n"
            "    // 복합 대입과 증감\n"
            "    int cnt = 0;\n"
            "    cnt += 10;\n"
            "    cnt++;\n"
            "    cout << \"cnt = \" << cnt << '\\n';   // 11\n"
            "    return 0;\n"
            "}\n"
        ),
    ),

    Lesson(
        id="cpp-basic-08",
        lang="cpp", level="기초",
        title="함수 정의",
        summary="반환형 · 매개변수 · 참조 전달",
        explanation=(
            "함수는 반환형 이름(매개변수) { ... } 형태로 정의한다. 반환값이 없으면 void 를 쓴다.\n"
            "함수는 main 보다 위에 정의하거나, 위쪽에 원형(프로토타입)을 선언해 두어야 호출할 수 있다.\n"
            "기본 전달은 값 복사(call by value)라 원본이 바뀌지 않는다.\n"
            "원본을 바꾸거나 큰 데이터를 복사 없이 넘기려면 참조(&) 로 전달한다."
        ),
        usage="반복되는 계산을 묶어 재사용한다. 코드가 짧고 명확해지며 디버깅이 쉬워진다.",
        cons="값 전달은 큰 객체에서 복사 비용이 크다(이럴 땐 const 참조 사용). 함수 호출 자체에도 약간의 비용이 있다.",
        code=(
            "#include <bits/stdc++.h>\n"
            "using namespace std;\n"
            "\n"
            "// 두 수의 합을 반환하는 함수\n"
            "int add(int a, int b) {\n"
            "    return a + b;\n"
            "}\n"
            "\n"
            "// 참조로 받아 원본 값을 직접 두 배로 만든다\n"
            "void doubleIt(int& x) {\n"
            "    x *= 2;\n"
            "}\n"
            "\n"
            "// 최댓값을 돌려주는 함수\n"
            "int maxOf(int a, int b) {\n"
            "    return (a > b) ? a : b;\n"
            "}\n"
            "\n"
            "int main() {\n"
            "    cout << \"add(3, 4) = \" << add(3, 4) << '\\n';   // 7\n"
            "    cout << \"maxOf(8, 5) = \" << maxOf(8, 5) << '\\n'; // 8\n"
            "\n"
            "    int n = 10;\n"
            "    doubleIt(n);          // 참조 전달이라 원본이 바뀐다\n"
            "    cout << \"n = \" << n << '\\n';   // 20\n"
            "    return 0;\n"
            "}\n"
        ),
    ),
]
