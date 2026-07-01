"""C++ 중급 문법 (스타터 — 더 많은 항목은 추가 가능)."""

from engine.models import Lesson

LESSONS = [

    Lesson(
        id="cpp-mid-01",
        lang="cpp", level="중급",
        title="vector 심화 (정렬과 이터레이터)",
        summary="sort · begin/end · 범위 기반 for",
        explanation=(
            "[개요]\n"
            "vector 는 C++ 의 동적 배열로, 원소를 추가하면 내부 용량이 자동으로 확장된다.\n"
            "일반 배열(int arr[5])은 크기를 고정해야 하지만, vector 는 크기를 미리 정할 필요가 없다.\n"
            "\n"
            "[핵심 개념]\n"
            "• 정렬은 원소를 크기 순서대로 재배치하는 작업이며, sort() 함수가 이를 수행한다.\n"
            "• 이터레이터(iterator)는 컨테이너의 특정 위치를 가리키는 객체이다.\n"
            "  - begin() 은 첫 번째 원소를 가리킨다.\n"
            "  - end() 는 마지막 원소 바로 다음 위치를 가리킨다.\n"
            "  - rbegin() / rend() 는 역방향(뒤에서 앞) 순회에 사용한다.\n"
            "\n"
            "[코드 분석]\n"
            "  #include <bits/stdc++.h>              → C++ 표준 라이브러리를 일괄 포함한다.\n"
            "  using namespace std;                  → std:: 접두사를 생략할 수 있게 한다.\n"
            "  vector<int> v = {5, 2, 9, 1, 7};     → 정수 vector 를 생성하고 초기값 5,2,9,1,7 로 초기화한다.\n"
            "  v.push_back(3);                       → vector 끝에 3 을 추가한다. 결과: v = {5,2,9,1,7,3}.\n"
            "  sort(v.begin(), v.end());             → v 의 처음부터 끝까지 오름차순으로 정렬한다.\n"
            "  for (int x : v) cout << x << ' ';    → v 의 모든 원소를 x 에 담아 출력한다(범위 기반 for).\n"
            "  cout << '\\n';                        → 줄바꿈 문자를 출력한다.\n"
            "  for (auto it = v.rbegin(); it != v.rend(); ++it)  → 역방향 이터레이터로 뒤에서 앞으로 순회한다.\n"
            "      cout << *it << ' ';              → *it 는 이터레이터가 가리키는 원소의 값이다(역참조).\n"
            "  cout << \"크기: \" << v.size()         → v 의 원소 개수를 출력한다.\n"
            "\n"
            "[유의 사항]\n"
            "• v[100] 처럼 범위를 벗어난 인덱스로 접근하면 정의되지 않은 동작이 발생하며, 별도의 오류 메시지 없이 비정상 종료될 수 있다.\n"
            "• push_back 을 반복하면 내부 메모리 재할당이 발생하고, 이때 기존 이터레이터가 무효화될 수 있다.\n"
            "• sort() 는 기본적으로 오름차순이다. 내림차순은 sort(v.begin(), v.end(), greater<int>()) 를 사용한다.\n"
            "• 인덱스가 필요 없는 경우 범위 기반 for(for (int x : v))가 가장 간결하고 오류 가능성이 낮다."
        ),
        usage="대부분의 배열 처리에 사용. 정렬 후 이분탐색(lower_bound)과 함께 코딩테스트 단골.",
        cons="중간 삽입/삭제는 O(n)으로 느리다. 인덱스 무효화(재할당 시 이터레이터 무효화)에 주의.",
        code=(
            "#include <bits/stdc++.h>\n"
            "using namespace std;\n"
            "\n"
            "int main() {\n"
            "    vector<int> v = {5, 2, 9, 1, 7};\n"
            "    v.push_back(3);\n"
            "\n"
            "    sort(v.begin(), v.end());          // 오름차순 정렬\n"
            "    cout << \"정렬: \";\n"
            "    for (int x : v) cout << x << ' ';   // 범위 기반 for\n"
            "    cout << '\\n';\n"
            "\n"
            "    // 이터레이터로 순회\n"
            "    cout << \"역순: \";\n"
            "    for (auto it = v.rbegin(); it != v.rend(); ++it)\n"
            "        cout << *it << ' ';\n"
            "    cout << '\\n';\n"
            "\n"
            "    cout << \"크기: \" << v.size() << '\\n';\n"
            "    return 0;\n"
            "}\n"
        ),
    ),

    Lesson(
        id="cpp-mid-02",
        lang="cpp", level="중급",
        title="pair 와 tuple",
        summary="두 값 묶기 · first/second · tie",
        explanation=(
            "[개요]\n"
            "pair 는 두 개의 값을 하나의 단위로 묶는 컨테이너이다. 예를 들어 (이름, 점수) 또는 좌표 (x, y) 를 함께 관리할 수 있다.\n"
            "tuple 은 pair 의 확장으로, 세 개 이상의 값을 묶을 수 있다. 예: (이름, 점수, 학번).\n"
            "\n"
            "[핵심 개념]\n"
            "• pair 의 두 원소는 .first 와 .second 로 접근한다.\n"
            "• pair 활용 예: 다익스트라 알고리즘에서 (거리, 정점)을 함께 관리하거나, 좌표 (x, y)를 하나의 단위로 정렬한다.\n"
            "• pair 비교는 사전식으로 이루어진다. .first 를 먼저 비교하고, 같으면 .second 를 비교한다.\n"
            "\n"
            "[코드 분석]\n"
            "  pair<int, string> p = {1, \"사과\"};    → 정수 1 과 문자열 \"사과\" 를 하나의 pair 로 묶는다.\n"
            "  cout << p.first << ' ' << p.second   → p.first 는 1, p.second 는 \"사과\" 를 출력한다.\n"
            "  vector<pair<int,int>> v = {{3,1}, {1,2}, {1,1}};  → pair 를 원소로 가지는 vector 를 생성한다.\n"
            "  sort(v.begin(), v.end());             → pair 정렬: .first 를 먼저 비교하고 같으면 .second 를 비교한다.\n"
            "  for (auto& [a, b] : v)                → C++17 구조적 바인딩으로 pair 를 a, b 로 분해한다.\n"
            "      cout << '(' << a << ',' << b << \") \";  → 각 pair 를 (1,1) 형식으로 출력한다.\n"
            "  tuple<int, string, double> t = {10, \"점수\", 99.5};  → 세 값을 tuple 로 묶는다.\n"
            "  int id; string name; double score;   → tuple 을 분해해 받을 변수들을 선언한다.\n"
            "  tie(id, name, score) = t;            → tuple 을 id, name, score 변수로 한 번에 분해한다.\n"
            "  cout << id << ' ' << name << ' ' << score  → 분해된 값들을 각각 출력한다.\n"
            "\n"
            "[유의 사항]\n"
            "• pair 는 .first, .second 두 원소만 가진다. 세 개 이상이면 tuple 을 사용한다.\n"
            "• pair 는 정렬 시 자동으로 사전식 비교(.first 우선)를 수행하므로, 이를 이용해 다중 기준 정렬이 가능하다.\n"
            "• auto& [a, b] 구조적 바인딩은 C++17 이상에서 동작하며, 대부분의 코딩테스트 환경에서 지원한다.\n"
            "• get<0>(t), get<1>(t) 로도 tuple 원소에 접근할 수 있다."
        ),
        usage="좌표(x,y)나 (값,인덱스)를 묶어 정렬할 때 핵심. 다익스트라의 (거리,정점)에도 자주 사용.",
        cons="요소가 많아지면 .first/.second 가 가독성을 해친다. 의미가 분명하면 struct 가 더 명확하다.",
        code=(
            "#include <bits/stdc++.h>\n"
            "using namespace std;\n"
            "\n"
            "int main() {\n"
            "    pair<int, string> p = {1, \"사과\"};\n"
            "    cout << p.first << ' ' << p.second << '\\n';\n"
            "\n"
            "    vector<pair<int,int>> v = {{3,1}, {1,2}, {1,1}};\n"
            "    sort(v.begin(), v.end());      // first 우선, 같으면 second\n"
            "    for (auto& [a, b] : v)         // 구조적 바인딩\n"
            "        cout << '(' << a << ',' << b << \") \";\n"
            "    cout << '\\n';\n"
            "\n"
            "    tuple<int, string, double> t = {10, \"점수\", 99.5};\n"
            "    int id; string name; double score;\n"
            "    tie(id, name, score) = t;\n"
            "    cout << id << ' ' << name << ' ' << score << '\\n';\n"
            "    return 0;\n"
            "}\n"
        ),
    ),

    Lesson(
        id="cpp-mid-03",
        lang="cpp", level="중급",
        title="map 과 unordered_map",
        summary="키-값 저장 · 정렬맵 vs 해시맵",
        explanation=(
            "[개요]\n"
            "map 과 unordered_map 은 키(key)에 값(value)을 대응시켜 저장하는 연관 컨테이너이다.\n"
            "\n"
            "[핵심 개념]\n"
            "• map: 키가 항상 정렬된 상태로 유지되는 연관 컨테이너이다.\n"
            "  - 내부적으로 균형 이진트리 구조이며, 조회·삽입이 O(log n) 이다.\n"
            "• unordered_map: 정렬을 보장하지 않는 해시 기반 연관 컨테이너이다.\n"
            "  - 해시 함수로 위치를 계산해 접근하며, 평균 시간 복잡도는 O(1) 이다.\n"
            "\n"
            "[코드 분석]\n"
            "  map<string, int> cnt;                → 문자열을 키, 정수를 값으로 하는 정렬된 map 을 생성한다.\n"
            "  string s = \"banana\";                → 문자열 \"banana\" 를 s 에 저장한다.\n"
            "  for (char c : s) cnt[string(1, c)]++;  → 각 글자를 키로 하여 등장 횟수를 센다.\n"
            "                                           존재하지 않는 키를 cnt[key] 로 참조하면 값이 0 에서 시작한다.\n"
            "  for (auto& [k, v] : cnt)             → map 의 모든 키-값 쌍을 k, v 로 꺼내 순회한다.\n"
            "      cout << k << \": \" << v          → \"a: 3\" 형식으로 각 글자와 등장 횟수를 출력한다.\n"
            "  unordered_map<string, int> price;    → 해시 기반 map(빠르지만 순서 없음)을 생성한다.\n"
            "  price[\"사과\"] = 1000;               → \"사과\" 키에 1000 을 저장한다.\n"
            "  price[\"바나나\"] = 1500;             → \"바나나\" 키에 1500 을 저장한다.\n"
            "  if (price.count(\"사과\"))            → \"사과\" 키의 존재 여부를 확인한다(있으면 1, 없으면 0).\n"
            "      cout << price[\"사과\"]           → 존재할 때만 값을 조회한다 → 1000.\n"
            "\n"
            "[유의 사항]\n"
            "• map[key] 는 읽기만 해도 해당 키가 없으면 기본값(0 또는 빈 문자열)으로 원소를 자동 생성한다.\n"
            "  따라서 존재 여부만 확인할 때는 반드시 count(key) 또는 find(key) 를 사용해야 한다.\n"
            "• map 은 O(log n), unordered_map 은 평균 O(1) 이며, 데이터가 많을수록 속도 차이가 커진다.\n"
            "• 빈도수 계산 문제에서 map[글자]++ 패턴은 자주 사용되는 필수 패턴이다.\n"
            "• 키 순서(알파벳 순, 숫자 순)가 필요하면 map, 속도만 중요하면 unordered_map 을 선택한다."
        ),
        usage="빈도수 세기, 매핑, 캐싱에 사용. 키 순서가 필요하면 map, 속도만 필요하면 unordered_map.",
        cons="map[key] 는 없는 키를 읽기만 해도 원소를 만든다. unordered_map 은 최악 충돌 시 O(n)이 될 수 있다.",
        code=(
            "#include <bits/stdc++.h>\n"
            "using namespace std;\n"
            "\n"
            "int main() {\n"
            "    map<string, int> cnt;          // 키 정렬됨\n"
            "    string s = \"banana\";\n"
            "    for (char c : s) cnt[string(1, c)]++;\n"
            "    for (auto& [k, v] : cnt)\n"
            "        cout << k << \": \" << v << '\\n';\n"
            "\n"
            "    unordered_map<string, int> price;   // 해시맵\n"
            "    price[\"사과\"] = 1000;\n"
            "    price[\"바나나\"] = 1500;\n"
            "    if (price.count(\"사과\"))\n"
            "        cout << \"사과 가격: \" << price[\"사과\"] << '\\n';\n"
            "    return 0;\n"
            "}\n"
        ),
    ),

    Lesson(
        id="cpp-mid-04",
        lang="cpp", level="중급",
        title="set 과 unordered_set",
        summary="중복 없는 집합 · 정렬셋 vs 해시셋",
        explanation=(
            "[개요]\n"
            "set 과 unordered_set 은 중복을 허용하지 않는 집합 컨테이너이다. 동일한 값을 여러 번 삽입해도 하나만 저장된다.\n"
            "\n"
            "[핵심 개념]\n"
            "• set: 중복을 제거하며 원소를 항상 정렬된 상태로 유지한다.\n"
            "  - 내부적으로 균형 이진트리 구조이며, 삽입·조회가 O(log n) 이다.\n"
            "• unordered_set: 중복을 제거하되 순서를 보장하지 않는다.\n"
            "  - 원소 포함 여부를 해시 기반으로 평균 O(1) 에 확인할 수 있다.\n"
            "• 활용 예: BFS/DFS 에서 방문 여부 기록, 입력에서 중복 자동 제거.\n"
            "\n"
            "[코드 분석]\n"
            "  set<int> s;                         → 정수를 담는 set 을 생성한다(자동 정렬 + 중복 제거).\n"
            "  for (int x : {5, 3, 5, 1, 3}) s.insert(x);  → 5,3,5,1,3 을 삽입하며, 중복(5,3)은 하나만 남는다.\n"
            "  for (int x : s) cout << x << ' ';  → 자동 정렬 결과 1 3 5 순으로 출력된다.\n"
            "  s.count(3)                          → 3 이 set 에 있으면 1, 없으면 0 을 반환한다.\n"
            "  unordered_set<string> visited;      → 문자열을 담는 해시 기반 set 을 생성한다.\n"
            "  visited.insert(\"A\");              → \"A\" 를 visited 에 추가한다.\n"
            "  visited.insert(\"B\");              → \"B\" 를 visited 에 추가한다.\n"
            "  visited.size()                      → set 의 원소 개수를 반환한다 → 2.\n"
            "\n"
            "[유의 사항]\n"
            "• set 은 s[0] 같은 인덱스 접근을 지원하지 않는다. 이터레이터나 범위 기반 for 로만 순회한다.\n"
            "• unordered_set 은 순서를 보장하지 않으므로, 출력 순서가 삽입 순서와 다를 수 있다.\n"
            "• 중복 제거와 정렬이 모두 필요하면 set, 포함 여부만 빠르게 확인하면 unordered_set 이 유리하다.\n"
            "• erase(값) 으로 특정 원소를 삭제하고, find(값) 으로 이터레이터를 얻을 수 있다."
        ),
        usage="중복 제거, 방문 체크, 빠른 포함 여부 판정에 사용. 정렬된 순회가 필요하면 set.",
        cons="set 은 트리라 메모리/상수가 크다. unordered_set 은 순서 보장이 없어 출력 순서를 가정하면 안 된다.",
        code=(
            "#include <bits/stdc++.h>\n"
            "using namespace std;\n"
            "\n"
            "int main() {\n"
            "    set<int> s;                    // 자동 정렬 + 중복 제거\n"
            "    for (int x : {5, 3, 5, 1, 3}) s.insert(x);\n"
            "    cout << \"정렬된 원소: \";\n"
            "    for (int x : s) cout << x << ' ';   // 1 3 5\n"
            "    cout << '\\n';\n"
            "    cout << \"3 포함? \" << (s.count(3) ? \"예\" : \"아니오\") << '\\n';\n"
            "\n"
            "    unordered_set<string> visited;\n"
            "    visited.insert(\"A\");\n"
            "    visited.insert(\"B\");\n"
            "    cout << \"방문 수: \" << visited.size() << '\\n';\n"
            "    return 0;\n"
            "}\n"
        ),
    ),

    Lesson(
        id="cpp-mid-05",
        lang="cpp", level="중급",
        title="사용자 정의 비교자 (정렬 기준)",
        summary="sort + 람다 · 비교 구조체",
        explanation=(
            "[개요]\n"
            "sort() 는 기본적으로 오름차순 정렬을 수행한다. '점수 높은 순, 점수가 같으면 이름 오름차순' 같은 복합 기준이 필요하면 사용자 정의 비교자를 sort() 에 전달한다.\n"
            "\n"
            "[핵심 개념]\n"
            "• 람다 함수(lambda)는 이름 없이 그 자리에서 정의해 사용하는 함수이며, 비교자로 자주 활용된다.\n"
            "• 비교자의 규칙:\n"
            "  - a 가 b 보다 앞에 와야 하면 true 를 반환한다.\n"
            "  - a 가 b 보다 뒤에 와야 하면 false 를 반환한다.\n"
            "  - 두 값이 같을 때 true 를 반환하면 안 된다(엄격한 약한 순서 위반).\n"
            "\n"
            "[코드 분석]\n"
            "  struct Student {                       → Student 라는 데이터 묶음 타입을 정의한다.\n"
            "      string name;                       → 이름을 담는 문자열 멤버이다.\n"
            "      int score;                         → 점수를 담는 정수 멤버이다.\n"
            "  };                                     → 구조체 정의 종료.\n"
            "  vector<Student> v = {{\"김\",80},{\"이\",90},{\"박\",80}};  → 학생 3명을 vector 에 저장한다.\n"
            "  sort(v.begin(), v.end(), [](const Student& a, const Student& b) {  → sort 에 람다 비교자를 전달한다.\n"
            "      if (a.score != b.score) return a.score > b.score;  → 점수가 다르면 높은 쪽을 앞에 둔다(내림차순).\n"
            "      return a.name < b.name;            → 점수가 같으면 이름 오름차순으로 정렬한다.\n"
            "  });                                    → 람다와 sort 종료.\n"
            "  for (auto& st : v)                    → 정렬된 학생 목록을 순회한다.\n"
            "      cout << st.name << ' ' << st.score  → 이름과 점수를 출력한다.\n"
            "\n"
            "[유의 사항]\n"
            "• 비교자에서 a.score >= b.score 처럼 등호를 포함하면 안 된다. 같은 값에 대해 true 를 반환하면 'a 가 b 보다 앞이면서 동시에 b 가 a 보다 앞'이라는 모순이 생겨 무한루프나 크래시로 이어질 수 있다.\n"
            "• 람다 문법: [](인자1, 인자2){ return 조건; } — 대괄호 [] 는 외부 변수 캡처 범위이다.\n"
            "• const Student& 로 받으면 복사 없이 원본을 읽기 전용으로 참조하여 효율적으로 처리한다.\n"
            "• 단순 내림차순만 필요하면 sort(v.begin(), v.end(), greater<int>()) 가 더 간결하다."
        ),
        usage="여러 키 기준 정렬(점수 내림차순, 같으면 이름 오름차순) 등 실전 정렬에 필수.",
        cons="비교자가 엄격한 약한 순서(strict weak ordering)를 어기면(예: <= 사용) 런타임 오류가 날 수 있다.",
        code=(
            "#include <bits/stdc++.h>\n"
            "using namespace std;\n"
            "\n"
            "struct Student {\n"
            "    string name;\n"
            "    int score;\n"
            "};\n"
            "\n"
            "int main() {\n"
            "    vector<Student> v = {{\"김\", 80}, {\"이\", 90}, {\"박\", 80}};\n"
            "\n"
            "    // 점수 내림차순, 같으면 이름 오름차순\n"
            "    sort(v.begin(), v.end(), [](const Student& a, const Student& b) {\n"
            "        if (a.score != b.score) return a.score > b.score;\n"
            "        return a.name < b.name;\n"
            "    });\n"
            "\n"
            "    for (auto& st : v)\n"
            "        cout << st.name << ' ' << st.score << '\\n';\n"
            "    return 0;\n"
            "}\n"
        ),
    ),

    Lesson(
        id="cpp-mid-06",
        lang="cpp", level="중급",
        title="string 처리 (substr, stoi, to_string)",
        summary="부분 문자열 · 숫자 변환",
        explanation=(
            "[개요]\n"
            "문자열 처리는 대부분의 코딩테스트에서 요구되는 필수 기술이다. C++ 의 string 은 파이썬과 달리 기능이 명시적으로 분리되어 있다.\n"
            "\n"
            "[핵심 개념]\n"
            "• substr(pos, len): 문자열의 일부를 잘라낸다. 예: \"abc123def\" 에서 3번 위치부터 3글자는 \"123\" 이다.\n"
            "• stoi(\"42\"): 문자열 \"42\" 를 정수 42 로 변환한다(string to integer).\n"
            "• to_string(42): 정수 42 를 문자열 \"42\" 로 변환한다.\n"
            "\n"
            "[코드 분석]\n"
            "  string s = \"abc123def\";             → 문자열 \"abc123def\" 를 s 에 저장한다.\n"
            "  s.size()                             → 문자열의 길이를 반환한다 → 9.\n"
            "  s.substr(3, 3)                       → s[3]부터 3글자를 잘라낸다.\n"
            "                                           s[3]='1', s[4]='2', s[5]='3' → \"123\".\n"
            "  string num = \"42\"; int n = stoi(num);  → 문자열 \"42\" 를 정수 42 로 변환한다.\n"
            "  n + 8                                → 정수이므로 덧셈이 가능하다 → 50.\n"
            "  int x = 2026; string t = to_string(x) + \"년\";  → 정수 2026 을 \"2026\" 으로 변환한 뒤 \"년\" 을 이어 붙인다.\n"
            "  cout << t                            → \"2026년\" 을 출력한다.\n"
            "  size_t pos = s.find(\"123\");          → \"123\" 이 s 에서 시작하는 인덱스를 찾는다.\n"
            "  if (pos != string::npos)             → find 가 찾지 못하면 string::npos 를 반환한다.\n"
            "      cout << \"'123' 위치: \" << pos   → 찾았을 때만 위치를 출력한다 → 3.\n"
            "\n"
            "[유의 사항]\n"
            "• stoi(\"abc\") 처럼 숫자가 아닌 문자열을 전달하면 invalid_argument 예외가 발생해 프로그램이 종료된다.\n"
            "• substr(pos, len) 에서 pos 가 문자열 길이를 초과하면 out_of_range 예외가 발생한다.\n"
            "• string::npos 는 size_t 최댓값에 해당하는 매우 큰 값이다. if (pos == -1) 로 비교하면 잘못된 결과가 나온다.\n"
            "• 문자 'a'(작은따옴표, char)와 문자열 \"a\"(큰따옴표, string)는 서로 다른 타입이다.\n"
            "• stoll 은 long long 크기의 정수 변환, stod 는 실수(double) 변환에 사용한다."
        ),
        usage="입력 파싱, 토큰 분리, 숫자-문자열 변환에 필수. 문자열 처리 문제 전반에 사용.",
        cons="stoi 는 숫자가 아니면 예외(invalid_argument)를 던진다. substr 범위를 넘기면 out_of_range 발생.",
        code=(
            "#include <bits/stdc++.h>\n"
            "using namespace std;\n"
            "\n"
            "int main() {\n"
            "    string s = \"abc123def\";\n"
            "    cout << \"길이: \" << s.size() << '\\n';\n"
            "    cout << \"부분(3,3): \" << s.substr(3, 3) << '\\n';   // 123\n"
            "\n"
            "    string num = \"42\";\n"
            "    int n = stoi(num);\n"
            "    cout << \"숫자+8 = \" << (n + 8) << '\\n';            // 50\n"
            "\n"
            "    int x = 2026;\n"
            "    string t = to_string(x) + \"년\";\n"
            "    cout << t << '\\n';                                  // 2026년\n"
            "\n"
            "    size_t pos = s.find(\"123\");\n"
            "    if (pos != string::npos)\n"
            "        cout << \"'123' 위치: \" << pos << '\\n';         // 3\n"
            "    return 0;\n"
            "}\n"
        ),
    ),

    Lesson(
        id="cpp-mid-07",
        lang="cpp", level="중급",
        title="구조체(struct)와 클래스(class)",
        summary="멤버 변수 · 메서드 · 생성자",
        explanation=(
            "[개요]\n"
            "struct 와 class 는 관련 있는 데이터를 하나의 타입으로 묶는 사용자 정의 자료형이다. 예를 들어 사람의 이름·나이·키를 개별 변수 대신 Person 이라는 하나의 타입으로 관리할 수 있다.\n"
            "클래스는 객체를 생성하기 위한 설계도이며, 객체는 그 설계도로 만든 실체이다. Rectangle r(4, 5); 는 너비 4, 높이 5 인 Rectangle 객체를 생성한다는 의미이다.\n"
            "\n"
            "[핵심 개념]\n"
            "struct 와 class 의 유일한 차이는 기본 접근 지정자이다.\n"
            "• struct: 기본적으로 모든 멤버가 public(외부에서 직접 접근 가능)이다.\n"
            "• class: 기본적으로 모든 멤버가 private(외부에서 직접 접근 불가)이다.\n"
            "\n"
            "[코드 분석]\n"
            "  class Rectangle {                        → Rectangle 클래스를 정의한다.\n"
            "  private:                                 → 아래 멤버는 클래스 외부에서 직접 접근할 수 없다.\n"
            "      int w, h;                            → 너비(w)와 높이(h)를 담는 멤버 변수이다.\n"
            "  public:                                  → 아래 멤버는 외부에서 접근 가능하다.\n"
            "      Rectangle(int width, int height) : w(width), h(height) {}  → 생성자이다.\n"
            "                                           : w(width) 는 멤버 w 를 width 로 초기화한다는 의미이다(초기화 리스트).\n"
            "      int area() const { return w * h; }   → 넓이를 계산해 반환한다. const 는 멤버를 변경하지 않음을 표시한다.\n"
            "      int perimeter() const { return 2*(w+h); }  → 둘레를 계산해 반환한다.\n"
            "  struct Point { int x, y; };              → Point 구조체이다. struct 이므로 멤버가 기본 public 이다.\n"
            "  Rectangle r(4, 5);                      → 너비 4, 높이 5 인 Rectangle 객체를 생성한다(생성자 호출).\n"
            "  r.area()                                → r 의 area() 메서드를 호출한다 → 4*5=20.\n"
            "  r.perimeter()                           → r 의 perimeter() 메서드를 호출한다 → 2*(4+5)=18.\n"
            "  Point p = {2, 3};                       → x=2, y=3 인 Point 객체를 생성한다.\n"
            "  cout << p.x << ',' << p.y               → p 의 x, y 값을 출력한다.\n"
            "\n"
            "[유의 사항]\n"
            "• class 에서 생성자를 정의하지 않으면 멤버 변수가 초기화되지 않아 쓰레기 값이 들어갈 수 있다.\n"
            "• private 멤버에 외부에서 직접 접근하면 컴파일 오류가 발생한다(r.w = 10; 은 불가).\n"
            "• 코딩테스트에서는 보통 struct 로 단순한 데이터 묶음을 만들고, 복잡한 캡슐화가 필요할 때만 class 를 사용한다.\n"
            "• 생성자 초기화 리스트(: w(width))는 생성자 본체에서 대입하는 방식보다 효율적이다."
        ),
        usage="좌표/학생/노드 등 의미 있는 데이터 묶음 표현에 사용. 자료구조 구현의 기본 단위.",
        cons="단순 데이터 묶음에 과한 캡슐화는 불필요하다. C++ 에서는 상황에 맞게 struct/class 를 선택한다.",
        code=(
            "#include <bits/stdc++.h>\n"
            "using namespace std;\n"
            "\n"
            "class Rectangle {\n"
            "private:\n"
            "    int w, h;\n"
            "public:\n"
            "    Rectangle(int width, int height) : w(width), h(height) {}\n"
            "    int area() const { return w * h; }\n"
            "    int perimeter() const { return 2 * (w + h); }\n"
            "};\n"
            "\n"
            "struct Point {       // 기본 public\n"
            "    int x, y;\n"
            "};\n"
            "\n"
            "int main() {\n"
            "    Rectangle r(4, 5);\n"
            "    cout << \"넓이: \" << r.area() << '\\n';        // 20\n"
            "    cout << \"둘레: \" << r.perimeter() << '\\n';   // 18\n"
            "\n"
            "    Point p = {2, 3};\n"
            "    cout << \"점: (\" << p.x << ',' << p.y << \")\\n\";\n"
            "    return 0;\n"
            "}\n"
        ),
    ),

    Lesson(
        id="cpp-mid-08",
        lang="cpp", level="중급",
        title="참조(&)와 포인터 기초",
        summary="별칭 참조 · 주소와 역참조",
        explanation=(
            "[개요]\n"
            "참조와 포인터는 C++ 의 핵심 개념이며, 초보자가 혼동하기 쉬운 부분이다.\n"
            "\n"
            "[핵심 개념]\n"
            "• 참조(&): 기존 변수에 대한 별칭이다. int& r = a; 로 선언하면 r 은 a 와 같은 메모리 공간을 가리키므로, r 을 변경하면 a 도 변경된다.\n"
            "• 포인터(*): 변수의 메모리 주소를 저장하는 변수이다.\n"
            "  - &a 는 변수 a 의 주소이다.\n"
            "  - int* p = &a; 는 a 의 주소를 p 에 저장한다.\n"
            "  - *p 는 역참조로, p 가 가리키는 주소에 있는 값이다.\n"
            "• 함수 매개변수로 참조(&)를 사용하는 이유: 값 전달은 기본적으로 복사를 수반한다. 큰 vector 등을 매번 복사하면 성능과 메모리 측면에서 비효율적이므로, 참조로 전달하면 복사 없이 원본을 직접 다룰 수 있다.\n"
            "\n"
            "[코드 분석]\n"
            "  void addOne(int& x) { x += 1; }    → 참조로 받으므로 함수 안에서 x 를 변경하면 원본도 변경된다.\n"
            "  int a = 10;                         → 정수 변수 a 를 생성하고 10 으로 초기화한다.\n"
            "  int& ref = a;                       → ref 는 a 의 참조이며, 둘은 같은 메모리 공간을 가리킨다.\n"
            "  ref = 20;                           → ref 를 20 으로 변경하면 같은 메모리의 a 도 20 이 된다.\n"
            "  cout << \"a = \" << a               → 출력: a = 20 (ref 변경이 a 에 반영됨).\n"
            "  int* p = &a;                        → p 는 포인터이며, &a(a 의 주소)를 저장한다.\n"
            "  cout << \"*p = \" << *p             → *p 는 역참조로, p 가 가리키는 값(=a)이다 → 20.\n"
            "  *p = 30;                            → p 가 가리키는 곳(a)의 값을 30 으로 변경한다.\n"
            "  cout << \"a = \" << a               → 출력: a = 30 (*p 를 통한 변경이 a 에 반영됨).\n"
            "  addOne(a);                          → a 를 참조로 전달하므로 함수 안에서 a 가 직접 +1 된다.\n"
            "  cout << \"a = \" << a               → 출력: a = 31.\n"
            "\n"
            "[유의 사항]\n"
            "• 참조는 선언과 동시에 반드시 초기화해야 한다. int& r; 만 작성하면 컴파일 오류가 발생한다.\n"
            "• 포인터가 nullptr(아무것도 가리키지 않음) 상태에서 *p 로 역참조하면 프로그램이 크래시된다.\n"
            "• 포인터 선언(int* p)의 * 와 역참조(*p)의 * 는 기호는 같지만 의미가 다르다.\n"
            "  - int* p   → p 는 포인터 변수라는 타입 선언이다.\n"
            "  - *p = 30  → p 가 가리키는 곳의 값을 30 으로 변경하는 역참조·값 접근이다.\n"
            "• 함수에 큰 데이터를 수정 없이 전달할 때는 const int& 를 사용해 복사와 수정을 모두 방지한다.\n"
            "• 참조는 한 번 초기화하면 다른 변수를 가리킬 수 없다(포인터는 재배치 가능)."
        ),
        usage="큰 객체를 복사 없이 함수에 전달(const &)하거나, 함수에서 값을 수정해 돌려줄 때 사용.",
        cons="포인터는 nullptr/잘못된 주소 역참조 시 크래시가 난다. 참조는 초기화 후 다른 대상을 가리킬 수 없다.",
        code=(
            "#include <bits/stdc++.h>\n"
            "using namespace std;\n"
            "\n"
            "void addOne(int& x) { x += 1; }   // 참조 전달: 원본 수정\n"
            "\n"
            "int main() {\n"
            "    int a = 10;\n"
            "    int& ref = a;       // 참조: a 의 별칭\n"
            "    ref = 20;\n"
            "    cout << \"a = \" << a << '\\n';        // 20\n"
            "\n"
            "    int* p = &a;        // 포인터: a 의 주소\n"
            "    cout << \"*p = \" << *p << '\\n';      // 20\n"
            "    *p = 30;            // 역참조로 값 변경\n"
            "    cout << \"a = \" << a << '\\n';        // 30\n"
            "\n"
            "    addOne(a);\n"
            "    cout << \"a = \" << a << '\\n';        // 31\n"
            "    return 0;\n"
            "}\n"
        ),
    ),
]
