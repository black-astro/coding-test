"""C++ 기초 문법 (스타터 — 더 많은 항목은 추가 가능)."""

from engine.models import Lesson

LESSONS = [

    Lesson(
        id="cpp-basic-01",
        lang="cpp", level="기초",
        title="변수와 기본 타입",
        summary="int / long long / double / char / bool",
        explanation=(
            "[개요]\n"
            "변수(variable)는 값을 저장하는, 이름이 부여된 메모리 공간이다. 컴퓨터 메모리의 특정 영역에 이름을 붙여 값을 저장하고 참조한다.\n"
            "\n"
            "[핵심 개념]\n"
            "C++은 정적 타입 언어로, 변수를 선언할 때 저장할 값의 종류(타입, 자료형)를 반드시 명시해야 한다. 담을 값의 종류에 따라 타입을 선택한다.\n"
            "\n"
            "기본 타입 종류:\n"
            "• int        — 정수 타입. -약 21억 ~ +약 21억 범위(32비트)\n"
            "• long long  — 더 큰 정수 타입. 약 ±922경 범위(64비트)\n"
            "• double     — 실수(소수) 타입. 3.14, -2.71 등을 저장\n"
            "• char       — 문자 하나를 저장하는 타입. 'A', '0', '!' 등 단일 문자\n"
            "• bool       — 참/거짓 두 값만 저장하는 타입. true(참) 또는 false(거짓)\n"
            "\n"
            "[코드 분석]\n"
            "• #include <bits/stdc++.h>             → C++ 표준 라이브러리 전체를 포함한다. 이 한 줄로 cout, cin 등을 사용할 수 있다.\n"
            "• using namespace std;                 → std 네임스페이스를 생략 가능하게 한다. 없으면 std::cout처럼 명시해야 한다.\n"
            "• int a = 10;                          → 정수 변수 a를 선언하고 10으로 초기화한다.\n"
            "• long long big = 10000000000LL;       → long long 변수 big을 선언하고 100억으로 초기화한다. 접미사 LL을 붙여야 long long 리터럴로 인식된다.\n"
            "• double d = 3.14;                     → 실수 변수 d를 선언하고 3.14로 초기화한다.\n"
            "• char c = 'A';                        → 문자 변수 c를 선언하고 'A'로 초기화한다. 문자는 작은따옴표('')로 감싼다.\n"
            "• bool flag = true;                    → 불리언 변수 flag를 선언하고 true로 초기화한다.\n"
            "• cout << \"a = \" << a << '\\n';         → 화면에 \"a = 10\"을 출력하고 줄을 바꾼다.\n"
            "• cout << boolalpha << \"flag = \" << flag << '\\n';  → boolalpha 조작자를 사용하면 bool 값이 0/1이 아닌 true/false로 출력된다.\n"
            "\n"
            "[유의 사항]\n"
            "• int로 선언한 변수에 약 21억을 초과하는 값을 저장하면 경고 없이 잘못된 값이 된다(오버플로).\n"
            "• 변수를 초기화하지 않으면 쓰레기값(garbage value)이 들어간다. 반드시 초기화한다.\n"
            "• char 값은 작은따옴표(''), string 값은 큰따옴표(\"\")로 감싼다."
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
            "[개요]\n"
            "cin과 cout은 프로그램이 표준 입출력을 처리하는 스트림이다. cin은 키보드(표준 입력)로부터 값을 읽어오고, cout은 화면(표준 출력)에 값을 출력한다.\n"
            "\n"
            "[핵심 개념]\n"
            "스트림 연산자:\n"
            "• >> (추출 연산자) — 입력을 읽어 변수에 저장한다.\n"
            "• << (삽입 연산자) — 값을 출력 스트림으로 내보낸다.\n"
            "\n"
            "줄바꿈 방법:\n"
            "• '\\n' — 줄바꿈만 수행한다. 코딩 테스트에서 권장된다.\n"
            "• endl  — 줄바꿈과 버퍼 비우기를 함께 수행한다. 속도가 느려 대량 출력에는 권장되지 않는다.\n"
            "\n"
            "[코드 분석]\n"
            "• ios::sync_with_stdio(false);         → C++ 스트림과 C 표준 입출력의 동기화를 해제하여 입출력 속도를 높인다. 대량 입력 문제에서 필수다.\n"
            "• cin.tie(nullptr);                    → cin과 cout의 강제 연결을 해제하여 속도를 높인다. 위 설정과 함께 사용한다.\n"
            "• cin >> x >> y;                       → 표준 입력에서 값 두 개를 읽어 x와 y에 저장한다. 공백 또는 줄바꿈으로 구분된다.\n"
            "• cout << \"두 수: \" << x << \" \" << y << '\\n';  → \"두 수: 3 5\" 형태로 출력하고 줄을 바꾼다.\n"
            "• cout << \"합: \" << (x + y) << '\\n';   → x와 y의 합을 출력한다.\n"
            "• cout << x << \" + \" << y << \" = \" << (x + y) << '\\n';  → \"3 + 5 = 8\" 형태로 출력한다.\n"
            "\n"
            "[유의 사항]\n"
            "• cin >>는 공백과 줄바꿈을 기준으로 값을 구분하여 읽는다.\n"
            "• 공백이 포함된 한 줄 전체를 읽으려면 cin >>가 아니라 getline(cin, s)를 사용한다.\n"
            "• 속도가 문제가 되는 경우 main 최상단에 ios::sync_with_stdio(false); cin.tie(nullptr);를 배치한다.\n"
            "• endl은 버퍼를 비우므로 느리다. 대신 '\\n'을 사용하는 것이 효율적이다."
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
            "[개요]\n"
            "조건문(if/else)은 조건의 참/거짓에 따라 실행 흐름을 분기하는 제어 구조이다. 반복문(for/while)은 동일한 코드 블록을 여러 번 반복 실행하는 제어 구조이다.\n"
            "\n"
            "[핵심 개념]\n"
            "조건문 if / else if / else:\n"
            "• if (조건)        — 조건이 참이면 해당 블록을 실행한다.\n"
            "• else if (조건2)  — 앞선 조건이 거짓이고 조건2가 참이면 해당 블록을 실행한다.\n"
            "• else             — 모든 조건이 거짓이면 해당 블록을 실행한다.\n"
            "\n"
            "반복문 for:\n"
            "• 형식: for (시작; 계속조건; 변화) { 반복할 내용 }\n"
            "• 예: for (int i = 1; i <= 10; i++) — i를 1로 시작하여 i가 10 이하인 동안 매 반복마다 i를 1씩 증가시킨다.\n"
            "\n"
            "반복문 while:\n"
            "• 형식: while (조건) { 반복할 내용 }\n"
            "• 조건이 참인 동안 반복하며, 조건이 거짓이 되면 종료한다.\n"
            "\n"
            "[코드 분석]\n"
            "• int total = 0;                  → 합계를 저장할 변수 total을 0으로 초기화한다(초기화하지 않으면 쓰레기값이 된다).\n"
            "• for (int i = 1; i <= 10; i++) { → i를 1부터 10까지 1씩 증가시키며 총 10회 반복한다.\n"
            "• if (i % 2 == 0) {               → i를 2로 나눈 나머지가 0이면 짝수이다. %는 나머지 연산자이다.\n"
            "• total += i;                     → total = total + i와 같다. 짝수일 때만 total에 누적한다.\n"
            "• cout << \"짝수합: \" << total;     → 결과 30을 출력한다(2+4+6+8+10=30).\n"
            "• int n = 5;                      → 변수 n을 5로 초기화한다.\n"
            "• while (n > 0) {                 → n이 0보다 큰 동안 반복한다.\n"
            "• cout << n << ' ';               → 현재 n 값과 공백을 출력한다.\n"
            "• n--;                            → n = n - 1과 같다. n을 1 감소시킨다.\n"
            "• }                               → n이 0이 되면 조건이 거짓이 되어 반복을 종료한다.\n"
            "\n"
            "[유의 사항]\n"
            "• while 내부에서 조건 변수를 변경하지 않으면 무한 루프가 발생한다. 반드시 탈출 조건을 마련한다.\n"
            "• for의 인덱스 i는 배열 인덱스가 0부터 시작하므로 통상 0부터 시작한다.\n"
            "• break는 반복을 즉시 완전히 종료한다.\n"
            "• continue는 현재 회차를 건너뛰고 다음 회차로 진행한다.\n"
            "• 비교 시 ==를 =로 잘못 쓰면 비교가 아닌 대입이 되어 버그가 발생한다."
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
            "[개요]\n"
            "배열(array)은 동일한 타입의 값 여러 개를 연속된 메모리에 저장하는 자료 구조이며, 선언 시 크기가 고정되어 이후 변경할 수 없다. vector는 크기를 동적으로 조절할 수 있는 가변 배열이다.\n"
            "\n"
            "[핵심 개념]\n"
            "• 배열은 크기가 고정되지만, vector는 push_back()으로 원소를 추가하며 크기를 늘릴 수 있다.\n"
            "• 코딩 테스트에서는 입력 개수가 사전에 정해지지 않는 경우가 많아 vector를 자주 사용한다.\n"
            "\n"
            "인덱스(index):\n"
            "• 배열과 vector의 각 원소는 0부터 시작하는 번호로 접근한다.\n"
            "• 크기가 5인 배열은 인덱스 0, 1, 2, 3, 4를 가진다(인덱스 5는 존재하지 않는다).\n"
            "\n"
            "[코드 분석]\n"
            "• int arr[5] = {5, 2, 9, 1, 7};        → 크기 5의 정수 배열을 선언하고 5개 값으로 초기화한다.\n"
            "• int sum = 0;                          → 합계 변수 sum을 0으로 초기화한다.\n"
            "• for (int i = 0; i < 5; i++) sum += arr[i];  → i를 0부터 4까지 변화시키며 arr[0]부터 arr[4]까지 누적한다.\n"
            "• cout << \"배열 합: \" << sum << '\\n';    → 합계 24를 출력한다(5+2+9+1+7=24).\n"
            "• vector<int> v;                        → 정수를 담는 빈 vector를 선언한다. <int>는 원소 타입을 의미한다.\n"
            "• v.push_back(3);                       → vector의 끝에 3을 추가한다.\n"
            "• v.push_back(1);                       → vector에 1을 추가한다.\n"
            "• v.push_back(2);                       → vector에 2를 추가한다. 현재 v = [3, 1, 2].\n"
            "• sort(v.begin(), v.end());             → v를 처음부터 끝까지 오름차순으로 정렬한다. 정렬 후 v = [1, 2, 3].\n"
            "• for (int x : v) cout << ' ' << x;    → v의 각 원소를 x에 담아 순회하며 출력한다(범위 기반 for).\n"
            "• cout << \"크기: \" << v.size() << '\\n'; → vector의 원소 개수 3을 출력한다.\n"
            "\n"
            "[유의 사항]\n"
            "• 배열 인덱스는 0부터 시작한다. arr[5] 선언 시 arr[0]~arr[4]만 유효하며, arr[5] 접근은 범위 초과 오류이다.\n"
            "• vector.size()의 반환 타입은 부호 없는 정수(size_t)이다. int와 비교할 때 (int)v.size()로 형변환하면 안전하다.\n"
            "• sort() 사용에는 #include <algorithm>이 필요하다(bits/stdc++.h로 일괄 해결 가능).\n"
            "• vector는 = 로 복사할 수 있다: vector<int> v2 = v;"
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
            "[개요]\n"
            "string은 여러 문자의 연속, 즉 문자열을 저장하는 타입이다. \"Hello\", \"나는 학생입니다\", \"12345\"와 같은 문자 시퀀스를 다룬다.\n"
            "\n"
            "[핵심 개념]\n"
            "• char는 문자 하나를, string은 여러 문자로 이루어진 문자열을 저장한다.\n"
            "• C 스타일의 char[] 배열도 있으나 string이 더 편리하고 안전하다. + 로 연결하고, 길이를 쉽게 구하며, == 로 비교할 수 있다.\n"
            "\n"
            "[코드 분석]\n"
            "• string a = \"Hello\";                       → 문자열 변수 a를 \"Hello\"로 초기화한다.\n"
            "• string b = \"World\";                       → 문자열 변수 b를 \"World\"로 초기화한다.\n"
            "• string c = a + \", \" + b + \"!\";           → 문자열을 + 로 연결한다. c = \"Hello, World!\".\n"
            "• cout << c << '\\n';                        → c 전체를 출력한다.\n"
            "• cout << \"길이: \" << c.size() << '\\n';     → c의 문자 개수 13을 출력한다. length()도 동일하다.\n"
            "• cout << \"첫 글자: \" << c[0] << '\\n';       → c[0]은 첫 번째 문자 'H'이다. 인덱스는 0부터 시작한다.\n"
            "• cout << c.substr(7, 5) << '\\n';           → 인덱스 7부터 5글자를 추출한다. \"World\"를 출력한다.\n"
            "• string r = a;                              → r에 a의 내용을 복사한다(r = \"Hello\").\n"
            "• reverse(r.begin(), r.end());               → r의 내용을 역순으로 뒤집는다. r = \"olleH\".\n"
            "• cout << \"뒤집기: \" << r << '\\n';           → 뒤집힌 결과 \"olleH\"를 출력한다.\n"
            "\n"
            "[자주 쓰는 string 기능]\n"
            "• s.size() / s.length()    — 문자 개수를 반환한다.\n"
            "• s[i]                     — i번째 문자에 접근한다(0부터 시작).\n"
            "• s.substr(시작, 길이)     — 시작 인덱스부터 지정 길이만큼 추출하여 반환한다.\n"
            "• s.substr(시작)           — 시작 인덱스부터 끝까지 반환한다.\n"
            "• s.find(\"찾을것\")         — 처음 등장하는 인덱스를 반환한다. 없으면 string::npos.\n"
            "• s += \"추가\";            — 문자열 뒤에 덧붙인다.\n"
            "• reverse(s.begin(), s.end());  — 문자열을 뒤집는다.\n"
            "\n"
            "[유의 사항]\n"
            "• string은 큰따옴표(\"\"), char는 작은따옴표('')를 사용한다. 'Hello'는 오류이다.\n"
            "• s[i] 접근 시 범위를 넘으면 위험하다. 안전하게 쓰려면 s.at(i)를 사용한다(범위 초과 시 예외 발생).\n"
            "• 공백이 포함된 한 줄 전체를 읽으려면 getline(cin, s)를 사용한다.\n"
            "• 큰 문자열을 반복적으로 + 로 연결하면 느려진다. += 나 stringstream을 활용한다."
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
            "[개요]\n"
            "형변환(Type Casting)은 한 타입의 값을 다른 타입으로 변환하는 것이다. 정수 오버플로(Integer Overflow)는 변수 타입이 표현할 수 있는 범위를 초과하여 값이 손상되는 현상이다.\n"
            "\n"
            "[형변환]\n"
            "가장 중요한 사례는 정수 나눗셈이다: 정수 ÷ 정수 = 정수(소수점 절삭).\n"
            "• 7 / 2 → 3 (3.5가 아님)\n"
            "• 두 피연산자가 모두 int이면 결과도 int이기 때문이다.\n"
            "• 실수 결과가 필요하면 적어도 한 쪽을 double로 변환해야 한다.\n"
            "\n"
            "형변환 방법:\n"
            "• (double)x              — x를 double로 변환한다(C 스타일, 간결).\n"
            "• static_cast<double>(x) — C++ 스타일. 더 안전하고 명확하다.\n"
            "\n"
            "[정수 오버플로]\n"
            "• int의 최대값: 약 21억(2,147,483,647)\n"
            "• 이를 초과하면 경고 없이 음수나 잘못된 값이 된다.\n"
            "• long long의 최대값: 약 922경(9,223,372,036,854,775,807)\n"
            "\n"
            "[코드 분석]\n"
            "• int a = 7, b = 2;                       → a를 7, b를 2로 초기화한다.\n"
            "• cout << (a / b) << '\\n';                → int ÷ int = int이므로 3이 출력된다(0.5 절삭).\n"
            "• cout << ((double)a / b) << '\\n';        → a를 double로 변환한 후 나누면 3.5가 출력된다.\n"
            "• int x = 100000;                         → x를 100000으로 초기화한다.\n"
            "• long long good = (long long)x * x;      → x를 먼저 long long으로 승격한 뒤 곱한다. 결과는 100억.\n"
            "• (long long good = x * x; 인 경우)        → int끼리 곱해 오버플로가 먼저 발생한다(위험).\n"
            "• long long sum = 0;                      → 합계를 long long으로 선언한다(누적 시 int 범위를 초과할 수 있음).\n"
            "• for (int i = 1; i <= 1000000; i++) sum += i;  → 1부터 100만까지 누적한다.\n"
            "• cout << sum << '\\n';                    → 결과 500,000,500,000을 출력한다.\n"
            "\n"
            "[유의 사항]\n"
            "• 오버플로는 오류 메시지 없이 발생하므로, 잘못된 답의 원인을 찾기 어렵다.\n"
            "• 곱셈 중간에도 오버플로가 발생한다. int x = 100000일 때 x * x는 이미 int 범위를 초과한다.\n"
            "• long long에 큰 리터럴을 직접 쓸 때는 숫자 뒤에 LL을 붙인다: 10000000000LL(생략 시 int로 처리됨).\n"
            "• 평균 계산 시 (a + b) / 2 는 a+b가 오버플로될 수 있으므로 long long으로 먼저 변환한다."
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
            "[개요]\n"
            "연산자(operator)는 값들 사이에서 계산이나 비교를 수행하는 기호이다. C++은 산술, 비교, 논리, 복합 대입, 삼항 등 다양한 연산자를 제공한다.\n"
            "\n"
            "[산술 연산자]\n"
            "• +   — 더하기. 5 + 3 = 8\n"
            "• -   — 빼기.   5 - 3 = 2\n"
            "• *   — 곱하기. 5 * 3 = 15\n"
            "• /   — 나누기. 5 / 2 = 2 (정수 나눗셈은 소수점 절삭)\n"
            "• %   — 나머지. 17 % 5 = 2\n"
            "\n"
            "[비교 연산자] — 두 값을 비교하여 true/false를 반환한다.\n"
            "• ==  — 같으면 true.           a == b\n"
            "• !=  — 다르면 true.           a != b\n"
            "• <   — 왼쪽이 작으면 true\n"
            "• <=  — 왼쪽이 작거나 같으면 true\n"
            "• >   — 왼쪽이 크면 true\n"
            "• >=  — 왼쪽이 크거나 같으면 true\n"
            "\n"
            "[논리 연산자] — 조건들을 조합한다.\n"
            "• &&  — 논리곱(AND). 양쪽 모두 true여야 true이다.\n"
            "• ||  — 논리합(OR).  하나라도 true이면 true이다.\n"
            "• !   — 부정(NOT). true를 false로, false를 true로 바꾼다.\n"
            "\n"
            "[복합 대입 연산자] — 계산과 대입을 동시에 수행한다.\n"
            "• +=  — a += 5 는 a = a + 5 와 같다.\n"
            "• -=  — a -= 3 는 a = a - 3 과 같다.\n"
            "• *=  — a *= 2 는 a = a * 2 와 같다.\n"
            "• ++  — a++ 는 a = a + 1 과 같다(1 증가).\n"
            "• --  — a-- 는 a = a - 1 과 같다(1 감소).\n"
            "\n"
            "[삼항 연산자] — if/else를 한 줄로 표현한다.\n"
            "• 형식: 조건 ? 참일때값 : 거짓일때값\n"
            "• (a > b) ? a : b — a가 b보다 크면 a, 아니면 b를 반환한다(더 큰 값 선택).\n"
            "\n"
            "[코드 분석]\n"
            "• int a = 17, b = 5;                            → a를 17, b를 5로 초기화한다.\n"
            "• cout << \"a + b = \" << (a + b) << '\\n';       → 17 + 5 = 22를 출력한다.\n"
            "• cout << \"a / b = \" << (a / b) << '\\n';       → 정수 나눗셈이므로 17 ÷ 5 = 3을 출력한다.\n"
            "• cout << \"a % b = \" << (a % b) << '\\n';       → 17을 5로 나눈 나머지 2를 출력한다.\n"
            "• cout << (a > b && b > 0) << '\\n';            → 17>5가 true이고 5>0도 true이므로 true이다.\n"
            "• int mx = (a > b) ? a : b;                     → a(17)가 b(5)보다 크므로 mx = 17이 된다.\n"
            "• int cnt = 0;                                   → cnt를 0으로 초기화한다.\n"
            "• cnt += 10;                                     → cnt = 0 + 10 = 10.\n"
            "• cnt++;                                         → cnt = 10 + 1 = 11.\n"
            "• cout << \"cnt = \" << cnt << '\\n';             → 11을 출력한다.\n"
            "\n"
            "[유의 사항]\n"
            "• ==와 =를 혼동하지 않는다. if (a = 5)는 비교가 아닌 대입이다. 조건은 if (a == 5)로 써야 한다.\n"
            "• &&는 양쪽 모두 true여야 true이고, ||는 하나만 true여도 true이다.\n"
            "• % 나머지 연산은 짝수/홀수 판별(i%2==0), 배수 판별(i%3==0), 자릿수 추출 등에 자주 사용된다.\n"
            "• 정수끼리의 / 나눗셈은 소수점이 절삭된다. 실수 결과가 필요하면 (double)로 형변환한다."
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
            "[개요]\n"
            "함수(function)는 특정 작업을 수행하는 코드 묶음에 이름을 부여한 것이다. 한 번 정의하면 이름으로 반복 호출하여 사용할 수 있다.\n"
            "\n"
            "[함수를 사용하는 이유]\n"
            "1. 재사용: 동일한 코드를 반복 작성하지 않고 함수 호출로 대체한다.\n"
            "2. 가독성: 코드가 짧고 명확해진다.\n"
            "3. 유지보수: 수정이 필요할 때 함수 한 곳만 고치면 된다.\n"
            "\n"
            "[함수의 구조]\n"
            "  반환형 함수이름(매개변수) {\n"
            "      // 실행할 코드\n"
            "      return 반환값;\n"
            "  }\n"
            "• 반환형: 함수가 반환하는 값의 타입(int, double, string 등). 반환값이 없으면 void를 사용한다.\n"
            "• 매개변수: 함수에 전달하는 입력값(없어도 된다).\n"
            "\n"
            "[값 전달 vs 참조 전달]\n"
            "• 값 전달(call by value): 변수의 복사본을 전달한다. 원본은 변경되지 않는다.\n"
            "• 참조 전달(call by reference): 원본 변수 자체를 전달한다. & 기호를 붙이며, 함수 내 변경이 원본에 반영된다.\n"
            "\n"
            "[코드 분석]\n"
            "• int add(int a, int b) {          → int를 반환하는 add 함수이다. 정수 a, b를 입력으로 받는다.\n"
            "• return a + b;                    → a + b의 결과를 반환한다. 호출한 곳으로 값이 돌아간다.\n"
            "• void doubleIt(int& x) {          → 반환값이 없는(void) 함수이다. &는 참조 전달을 의미한다.\n"
            "• x *= 2;                          → x를 두 배로 만든다. 참조이므로 원본 변수가 직접 변경된다.\n"
            "• int maxOf(int a, int b) {        → 두 int를 받아 더 큰 int를 반환하는 함수이다.\n"
            "• return (a > b) ? a : b;          → 삼항 연산자로 더 큰 값을 반환한다.\n"
            "• cout << add(3, 4) << '\\n';       → add(3, 4)가 7을 반환하여 7이 출력된다.\n"
            "• int n = 10;                      → n을 10으로 초기화한다.\n"
            "• doubleIt(n);                     → n을 참조로 전달하므로 함수 내에서 원본 n이 변경된다.\n"
            "• cout << \"n = \" << n << '\\n';    → 원본이 변경되어 n은 20이다.\n"
            "\n"
            "[유의 사항]\n"
            "• 함수를 main보다 아래에 정의하면 컴파일 오류가 발생한다. main 위에 정의하거나 앞에 선언(프로토타입)을 두어야 한다.\n"
            "  예: int add(int a, int b); 처럼 원형만 먼저 선언하면 정의는 main 아래에 두어도 된다.\n"
            "• 큰 vector나 string을 값으로 전달하면 복사 비용이 크다. const 참조(const vector<int>& v)로 전달하는 것이 효율적이다.\n"
            "• void 함수에서도 return;을 사용할 수 있다(값 없이). 조기 종료 시 유용하다."
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
