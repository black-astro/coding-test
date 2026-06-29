"""C++ 중급 문법 (스타터 — 더 많은 항목은 추가 가능)."""

from engine.models import Lesson

LESSONS = [

    Lesson(
        id="cpp-mid-01",
        lang="cpp", level="중급",
        title="vector 심화 (정렬과 이터레이터)",
        summary="sort · begin/end · 범위 기반 for",
        explanation=(
            "vector 는 가변 크기 배열로 push_back 으로 끝에 추가한다(평균 O(1)).\n"
            "정렬은 sort(v.begin(), v.end()) 로 기본 오름차순, 내림차순은 sort 뒤 reverse 또는 greater 사용.\n"
            "이터레이터 begin()/end() 로 순회하며, 범위 기반 for(auto x : v) 가 가장 간결하다."
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
            "pair<A,B> 는 두 값을 한 묶음으로 다루며 .first / .second 로 접근한다.\n"
            "make_pair 또는 {a, b} 로 생성하고, pair 끼리는 사전식 비교가 가능해 정렬 기준으로 쓰기 좋다.\n"
            "셋 이상은 tuple<...> 을 쓰고 get<i>(t) 로 꺼내거나 tie(a,b,c)=t 로 한 번에 분해한다."
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
            "map<K,V> 는 키가 자동 정렬되는 균형 이진트리(조회/삽입 O(log n)).\n"
            "unordered_map<K,V> 는 해시 기반으로 평균 O(1)이지만 순서가 없다.\n"
            "m[key] 로 접근하면 없을 때 기본값으로 자동 생성되며, count(key)/find(key) 로 존재 여부를 확인한다."
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
            "set<T> 는 중복을 허용하지 않고 원소가 자동 정렬되는 집합(삽입/조회 O(log n)).\n"
            "unordered_set<T> 는 해시 기반으로 평균 O(1)이지만 순서가 없다.\n"
            "insert 로 추가, count / find 로 존재 여부 확인, erase 로 제거한다."
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
            "sort 의 세 번째 인자로 비교 함수를 넘기면 원하는 기준으로 정렬할 수 있다.\n"
            "가장 간단한 방법은 람다 [](const T& a, const T& b){ return a < b; } 이다.\n"
            "비교자는 'a 가 b 보다 앞에 와야 하면 true' 를 반환해야 하며, 구조체 operator() 로도 정의한다."
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
            "string 은 += 로 이어붙이고 size()/length() 로 길이를 얻는다.\n"
            "substr(pos, len) 으로 부분 문자열을 자르고, find 로 위치를 찾는다(없으면 string::npos).\n"
            "stoi/stoll 로 문자열을 정수로, to_string 으로 숫자를 문자열로 변환한다."
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
            "struct 와 class 는 데이터(멤버 변수)와 동작(멤버 함수)을 묶는다.\n"
            "차이는 기본 접근 지정자뿐이다: struct 는 public, class 는 private 가 기본이다.\n"
            "생성자로 초기화하고, public 메서드를 통해 객체의 동작을 정의한다."
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
            "참조 int& r = a; 는 변수 a 의 별칭으로, r 을 바꾸면 a 도 바뀐다(재바인딩 불가).\n"
            "포인터 int* p = &a; 는 주소를 담으며 *p 로 값에 접근(역참조)한다.\n"
            "함수 인자를 참조(&)로 받으면 복사 없이 원본을 수정할 수 있어 효율적이다."
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
