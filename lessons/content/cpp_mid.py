"""C++ 중급 문법 (스타터 — 더 많은 항목은 추가 가능)."""

from engine.models import Lesson

LESSONS = [

    Lesson(
        id="cpp-mid-01",
        lang="cpp", level="중급",
        title="vector 심화 (정렬과 이터레이터)",
        summary="sort · begin/end · 범위 기반 for",
        explanation=(
            "━━ vector 심화 (정렬과 이터레이터) 이란? ━━\n"
            "\n"
            "vector 는 C++ 의 '자동으로 늘어나는 배열'이에요.\n"
            "일반 배열(int arr[5])은 크기를 미리 정해야 하지만,\n"
            "vector 는 원소를 넣을수록 자동으로 공간이 늘어나요.\n"
            "마치 고무줄 필통처럼, 연필을 계속 넣어도 알아서 늘어나는 거예요!\n"
            "\n"
            "정렬이란, 숫자들을 크기 순서대로 늘어놓는 작업이에요.\n"
            "sort() 함수가 그 역할을 해줘요.\n"
            "\n"
            "이터레이터(iterator) 는 '배열을 가리키는 손가락'이라고 생각하세요.\n"
            "begin() 은 첫 번째 원소를 가리키고,\n"
            "end() 는 마지막 원소 바로 다음을 가리켜요.\n"
            "rbegin() / rend() 는 반대 방향(뒤에서 앞)으로 순회할 때 써요.\n"
            "\n"
            "코드 한 줄씩 읽기:\n"
            "  #include <bits/stdc++.h>              →  C++ 표준 라이브러리를 한 번에 모두 불러와요\n"
            "  using namespace std;                  →  std:: 를 매번 안 써도 되게 해줘요\n"
            "  vector<int> v = {5, 2, 9, 1, 7};     →  정수를 담는 vector 를 만들고 초기값 5,2,9,1,7 을 넣어요\n"
            "  v.push_back(3);                       →  vector 끝에 3 을 추가해요. 이제 v = {5,2,9,1,7,3}\n"
            "  sort(v.begin(), v.end());             →  v 의 처음부터 끝까지 오름차순(작은 수→큰 수)으로 정렬해요\n"
            "  for (int x : v) cout << x << ' ';    →  v 의 모든 원소를 하나씩 x 에 담아 출력해요 (범위 기반 for)\n"
            "  cout << '\\n';                        →  줄바꿈 문자를 출력해요\n"
            "  for (auto it = v.rbegin(); it != v.rend(); ++it)  →  역방향 이터레이터로 뒤에서 앞으로 순회해요\n"
            "      cout << *it << ' ';              →  *it 는 이터레이터가 가리키는 원소의 값이에요 (별표=값 꺼내기)\n"
            "  cout << \"크기: \" << v.size()         →  v 에 원소가 몇 개인지 출력해요\n"
            "\n"
            "주의할 점:\n"
            "  - v[100] 처럼 범위를 벗어난 인덱스로 접근하면 프로그램이 그냥 죽어요 (오류 메시지도 안 나옴!)\n"
            "  - push_back 을 반복하면 내부적으로 메모리 재할당이 일어나고, 이때 기존 이터레이터가 무효화될 수 있어요\n"
            "  - sort() 는 기본적으로 오름차순이에요. 내림차순은 sort(v.begin(), v.end(), greater<int>()) 를 써요\n"
            "  - 범위 기반 for (for (int x : v)) 는 인덱스가 필요 없을 때 가장 간결하고 실수도 적어요"
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
            "━━ pair 와 tuple 이란? ━━\n"
            "\n"
            "pair 는 두 가지 값을 하나로 묶어 다니는 '쌍둥이 보관함'이에요.\n"
            "예를 들어, 학생의 (이름, 점수) 또는 좌표의 (x, y) 를 하나로 묶어 들고 다닐 수 있어요.\n"
            "마치 신발 한 켤레처럼, 왼쪽(.first)과 오른쪽(.second) 이 항상 같이 다니는 거예요!\n"
            "\n"
            "tuple 은 pair 의 확장판으로, 세 개 이상의 값도 묶을 수 있어요.\n"
            "(이름, 점수, 학번) 처럼 세 가지를 같이 들고 다닐 때 쓰는 '삼단 서랍장'이에요.\n"
            "\n"
            "왜 pair 를 쓰냐고요?\n"
            "다익스트라 알고리즘에서 (거리, 정점) 을 함께 관리하거나,\n"
            "좌표 (x, y) 를 하나의 단위로 정렬할 때 매우 유용해요.\n"
            "pair 끼리 비교하면 .first 를 먼저 비교하고, 같으면 .second 를 비교해요.\n"
            "\n"
            "코드 한 줄씩 읽기:\n"
            "  pair<int, string> p = {1, \"사과\"};    →  숫자 1 과 문자 \"사과\" 를 한 묶음으로 만들어요\n"
            "  cout << p.first << ' ' << p.second   →  p.first 는 1, p.second 는 \"사과\" 를 출력해요\n"
            "  vector<pair<int,int>> v = {{3,1}, {1,2}, {1,1}};  →  pair 들을 원소로 가지는 vector 를 만들어요\n"
            "  sort(v.begin(), v.end());             →  pair 정렬: .first 먼저 비교, 같으면 .second 비교해요\n"
            "  for (auto& [a, b] : v)                →  C++17 구조적 바인딩! pair 를 a, b 로 자동 분해해요\n"
            "      cout << '(' << a << ',' << b << \") \";  →  각 pair 를 (1,1) 형식으로 출력해요\n"
            "  tuple<int, string, double> t = {10, \"점수\", 99.5};  →  세 가지 값을 tuple 로 묶어요\n"
            "  int id; string name; double score;   →  tuple 을 분해해서 받을 변수들을 선언해요\n"
            "  tie(id, name, score) = t;            →  tuple 을 id, name, score 변수로 한 번에 분해해요\n"
            "  cout << id << ' ' << name << ' ' << score  →  분해된 값들을 각각 출력해요\n"
            "\n"
            "주의할 점:\n"
            "  - pair 는 .first, .second 두 개만 가능해요. 세 개 이상이면 tuple 을 써야 해요\n"
            "  - 정렬 시 pair 는 자동으로 사전식 비교(.first 우선)를 해요. 이걸 이용해 다중 기준 정렬이 가능해요\n"
            "  - auto& [a, b] 구조적 바인딩은 C++17 이상에서만 작동해요 (대부분의 코딩테스트 환경은 지원)\n"
            "  - get<0>(t), get<1>(t) 로도 tuple 원소에 접근할 수 있어요"
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
            "━━ map 과 unordered_map 이란? ━━\n"
            "\n"
            "map 은 '정렬된 사전'이에요.\n"
            "단어(키)를 넣으면 뜻(값)이 바로 나오는 국어사전처럼,\n"
            "\"사과\" 라는 키를 넣으면 1000(가격)이 나오는 거예요.\n"
            "그리고 국어사전처럼 키가 항상 알파벳/가나다 순으로 자동 정렬되어 있어요.\n"
            "내부적으로 균형 이진트리 구조라서 조회·삽입이 O(log n) 이에요.\n"
            "\n"
            "unordered_map 은 '뒤죽박죽이지만 초고속 사전'이에요.\n"
            "정렬은 없지만 찾는 속도가 훨씬 빠른 게 장점이에요 (평균 O(1)).\n"
            "해시 함수를 이용해 바로 원하는 위치로 점프하는 마법 사전 같은 거예요!\n"
            "\n"
            "코드 한 줄씩 읽기:\n"
            "  map<string, int> cnt;                →  문자열을 키, 정수를 값으로 하는 정렬된 map 을 만들어요\n"
            "  string s = \"banana\";                →  \"banana\" 라는 문자열을 s 에 저장해요\n"
            "  for (char c : s) cnt[string(1, c)]++;  →  각 글자 하나를 키로 해서 등장 횟수를 세요\n"
            "                                           없는 키를 cnt[key] 로 쓰면 자동으로 0에서 시작해요!\n"
            "  for (auto& [k, v] : cnt)             →  map 의 모든 키-값 쌍을 k, v 로 꺼내 순회해요\n"
            "      cout << k << \": \" << v          →  \"a: 3\" 처럼 각 글자와 등장 횟수를 출력해요\n"
            "  unordered_map<string, int> price;    →  해시 기반 map (빠르지만 순서 없음)\n"
            "  price[\"사과\"] = 1000;               →  \"사과\" 키에 1000 을 저장해요\n"
            "  price[\"바나나\"] = 1500;             →  \"바나나\" 키에 1500 을 저장해요\n"
            "  if (price.count(\"사과\"))            →  \"사과\" 키가 map 에 있는지 확인해요 (있으면 1, 없으면 0)\n"
            "      cout << price[\"사과\"]           →  있을 때만 값을 꺼내요 → 1000\n"
            "\n"
            "주의할 점:\n"
            "  - map[key] 를 읽기만 해도 해당 키가 없으면 기본값(0 또는 빈 문자열)으로 자동 생성돼요!\n"
            "    그래서 존재 여부를 먼저 확인할 때는 반드시 count(key) 나 find(key) 를 써야 해요\n"
            "  - map 은 O(log n), unordered_map 은 평균 O(1) 이에요. 데이터가 많으면 속도 차이가 커요\n"
            "  - 빈도수 세기 문제에서 map[글자]++ 패턴은 매우 자주 쓰이는 필수 패턴이에요!\n"
            "  - 키 순서(알파벳 순, 숫자 순)가 필요하면 map, 속도만 중요하면 unordered_map 을 골라요"
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
            "━━ set 과 unordered_set 이란? ━━\n"
            "\n"
            "set 은 '중복 없는 정렬된 바구니'예요.\n"
            "같은 사과를 여러 번 넣어도 바구니 안에는 사과 한 개만 있어요!\n"
            "그리고 꺼낼 때는 항상 크기 순서대로 나와요 (자동 정렬).\n"
            "내부적으로 균형 이진트리라서 삽입·조회가 O(log n) 이에요.\n"
            "\n"
            "unordered_set 은 '중복 없는 뒤죽박죽 바구니'예요.\n"
            "set 과 마찬가지로 중복을 제거하지만, 순서는 보장하지 않아요.\n"
            "대신 '이 원소가 있나요?' 를 해시 기반으로 평균 O(1) 만에 확인할 수 있어요.\n"
            "\n"
            "왜 set 을 쓰냐고요?\n"
            "BFS/DFS 에서 방문한 곳을 기록할 때 이미 간 곳인지 확인하는 데 딱이에요.\n"
            "또는 입력에서 중복을 자동으로 제거하고 싶을 때도 매우 유용해요.\n"
            "\n"
            "코드 한 줄씩 읽기:\n"
            "  set<int> s;                         →  정수를 담는 set 을 만들어요 (자동 정렬 + 중복 제거)\n"
            "  for (int x : {5, 3, 5, 1, 3}) s.insert(x);  →  5,3,5,1,3 을 넣는데, 중복(5,3)은 하나만 남아요\n"
            "  for (int x : s) cout << x << ' ';  →  1 3 5 순으로 출력돼요 (set 이 자동 정렬해줬어요!)\n"
            "  s.count(3)                          →  3 이 set 안에 있으면 1, 없으면 0 을 반환해요\n"
            "  unordered_set<string> visited;      →  문자열을 담는 해시 기반 set 을 만들어요\n"
            "  visited.insert(\"A\");              →  \"A\" 를 visited 에 추가해요\n"
            "  visited.insert(\"B\");              →  \"B\" 를 visited 에 추가해요\n"
            "  visited.size()                      →  set 안에 원소가 몇 개인지 반환해요 → 2\n"
            "\n"
            "주의할 점:\n"
            "  - set 에서는 s[0] 같은 인덱스 접근이 안 돼요! 이터레이터나 범위 기반 for 로만 순회해요\n"
            "  - unordered_set 은 순서가 없어서, 출력하면 들어간 순서와 다르게 나올 수 있어요\n"
            "  - 중복 제거 + 정렬이 필요하면 set, 단순히 '있나 없나' 빠르게 확인만 하면 unordered_set 이 빨라요\n"
            "  - erase(값) 으로 특정 원소를 삭제할 수 있고, find(값) 으로 이터레이터를 얻을 수 있어요"
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
            "━━ 사용자 정의 비교자 (정렬 기준) 이란? ━━\n"
            "\n"
            "sort() 는 기본적으로 오름차순으로 정렬해요.\n"
            "그런데 '점수 높은 사람 먼저, 점수가 같으면 이름 가나다 순으로' 같은\n"
            "복잡한 기준이 필요할 때는 직접 비교 규칙을 만들어서 sort() 에 넘겨줘야 해요.\n"
            "\n"
            "이때 사용하는 게 '람다 함수(lambda)'예요.\n"
            "람다는 이름 없는 작은 함수로, 그 자리에서 바로 만들어 쓰는 일회용 규칙이에요.\n"
            "마치 '오늘만 적용되는 규칙표'를 즉석에서 만드는 거예요!\n"
            "\n"
            "비교자의 핵심 규칙:\n"
            "  → a 가 b 보다 앞에 와야 한다면 true 반환\n"
            "  → a 가 b 보다 뒤에 와야 한다면 false 반환\n"
            "  → 절대로 같을 때 true 를 반환하면 안 돼요 (엄격한 약한 순서 위반)\n"
            "\n"
            "코드 한 줄씩 읽기:\n"
            "  struct Student {                       →  Student 라는 데이터 묶음 타입을 정의해요\n"
            "      string name;                       →  이름을 담는 문자열 멤버\n"
            "      int score;                         →  점수를 담는 정수 멤버\n"
            "  };                                     →  구조체 정의 끝\n"
            "  vector<Student> v = {{\"김\",80},{\"이\",90},{\"박\",80}};  →  학생 3명을 vector 에 넣어요\n"
            "  sort(v.begin(), v.end(), [](const Student& a, const Student& b) {  →  sort 에 람다 비교자를 전달해요\n"
            "      if (a.score != b.score) return a.score > b.score;  →  점수가 다르면 높은 쪽이 앞 (내림차순)\n"
            "      return a.name < b.name;            →  점수가 같으면 이름 가나다 순 (오름차순)\n"
            "  });                                    →  람다와 sort 끝\n"
            "  for (auto& st : v)                    →  정렬된 학생 목록을 순회해요\n"
            "      cout << st.name << ' ' << st.score  →  이름과 점수를 출력해요\n"
            "\n"
            "주의할 점:\n"
            "  - 비교자에서 a.score >= b.score 처럼 등호(=)를 포함시키면 절대 안 돼요!\n"
            "    같은 값일 때 true 를 반환하면 'a 가 b 보다 앞이고 동시에 b 가 a 보다 앞' 이라는\n"
            "    모순이 생겨서 프로그램이 무한루프나 크래시를 일으켜요\n"
            "  - 람다 문법: [](인자1, 인자2){ return 조건; }  — 대괄호[]는 외부 변수 캡처 범위예요\n"
            "  - const Student& 로 받는 이유: 복사 없이 원본을 읽기 전용으로 참조해서 빠르게 처리해요\n"
            "  - 단순 내림차순만 필요하면 sort(v.begin(), v.end(), greater<int>()) 를 쓰면 더 간단해요"
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
            "━━ string 처리 (substr, stoi, to_string) 이란? ━━\n"
            "\n"
            "문자열 처리는 거의 모든 코딩테스트에서 등장하는 필수 기술이에요.\n"
            "C++ 의 string 은 파이썬과 달리 기능이 더 명시적으로 분리되어 있어요.\n"
            "\n"
            "핵심 기능 세 가지:\n"
            "  1. substr(pos, len)  →  문자열의 일부를 잘라내요\n"
            "     예: \"abc123def\" 에서 3번 위치부터 3글자 = \"123\"\n"
            "  2. stoi(\"42\")       →  문자열 \"42\" 를 숫자 42 로 변환해요 (string to integer)\n"
            "     비유: \"42\" 라고 적힌 메모를 보고 42 라는 숫자로 인식하는 것\n"
            "  3. to_string(42)    →  숫자 42 를 문자열 \"42\" 로 변환해요\n"
            "     비유: 계산기 결과 42 를 영수증에 \"42\" 로 프린트하는 것\n"
            "\n"
            "코드 한 줄씩 읽기:\n"
            "  string s = \"abc123def\";             →  \"abc123def\" 라는 문자열을 s 에 저장해요\n"
            "  s.size()                             →  문자열의 길이(글자 수)를 반환해요 → 9\n"
            "  s.substr(3, 3)                       →  s[3]부터 3글자를 잘라요\n"
            "                                           s[3]='1', s[4]='2', s[5]='3' → \"123\"\n"
            "  string num = \"42\"; int n = stoi(num);  →  문자열 \"42\" 를 정수 42 로 변환해요\n"
            "  n + 8                                →  이제 진짜 숫자라 덧셈이 돼요 → 50\n"
            "  int x = 2026; string t = to_string(x) + \"년\";  →  숫자 2026 → \"2026\" 으로 바꾼 뒤 \"년\" 을 이어 붙여요\n"
            "  cout << t                            →  \"2026년\" 이 출력돼요\n"
            "  size_t pos = s.find(\"123\");          →  \"123\" 이 s 의 몇 번째 인덱스에서 시작하는지 찾아요\n"
            "  if (pos != string::npos)             →  find 가 못 찾으면 string::npos 를 반환해요\n"
            "      cout << \"'123' 위치: \" << pos   →  찾았을 때만 위치를 출력해요 → 3\n"
            "\n"
            "주의할 점:\n"
            "  - stoi(\"abc\") 처럼 숫자가 아닌 문자열을 넣으면 invalid_argument 예외로 프로그램이 종료돼요\n"
            "  - substr(pos, len) 에서 pos + len 이 문자열 길이를 초과하면 out_of_range 예외가 발생해요\n"
            "  - string::npos 는 매우 큰 숫자(size_t 최댓값)예요. if (pos == -1) 로 비교하면 틀려요!\n"
            "  - C++ 에서 문자 'a' 와 문자열 \"a\" 는 완전히 달라요\n"
            "    작은따옴표는 char(문자 한 개), 큰따옴표는 string(문자열)이에요\n"
            "  - stoll 은 long long 크기의 큰 정수 변환, stod 는 실수(double) 변환에 써요"
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
            "━━ 구조체(struct)와 클래스(class) 이란? ━━\n"
            "\n"
            "struct 와 class 는 관련 있는 데이터들을 하나로 묶는 '설계도'예요.\n"
            "예를 들어, 사람을 표현할 때 이름·나이·키를 따로따로 변수로 만드는 대신\n"
            "Person 이라는 묶음(struct/class)으로 만들어 한 번에 관리하는 거예요.\n"
            "\n"
            "비유: 클래스는 '쿠키 틀', 객체는 '쿠키'예요.\n"
            "틀(클래스)로 모양을 정해두고, 틀을 이용해 실제 쿠키(객체)를 찍어내는 거예요!\n"
            "Rectangle r(4, 5); 는 '너비 4, 높이 5 인 직사각형 쿠키를 찍어냈다'는 뜻이에요.\n"
            "\n"
            "struct 와 class 의 차이는 딱 하나예요:\n"
            "  - struct: 기본적으로 모든 멤버가 public (외부에서 바로 접근 가능)\n"
            "  - class : 기본적으로 모든 멤버가 private (외부에서 직접 접근 불가)\n"
            "\n"
            "코드 한 줄씩 읽기:\n"
            "  class Rectangle {                        →  Rectangle(직사각형) 이라는 클래스를 정의해요\n"
            "  private:                                 →  아래 변수들은 클래스 외부에서 직접 접근 불가해요\n"
            "      int w, h;                            →  너비(w)와 높이(h)를 담는 멤버 변수예요\n"
            "  public:                                  →  아래 것들은 외부에서 접근 가능해요\n"
            "      Rectangle(int width, int height) : w(width), h(height) {}  →  생성자예요\n"
            "                                           : w(width) 는 '멤버 w 를 width 로 초기화'라는 뜻 (초기화 리스트)\n"
            "      int area() const { return w * h; }   →  넓이를 계산해 반환. const 는 멤버를 바꾸지 않는다는 표시\n"
            "      int perimeter() const { return 2*(w+h); }  →  둘레를 계산해 반환\n"
            "  struct Point { int x, y; };              →  Point(점) 구조체. struct 라 기본으로 public\n"
            "  Rectangle r(4, 5);                      →  너비 4, 높이 5 인 Rectangle 객체를 만들어요 (생성자 호출)\n"
            "  r.area()                                →  r 의 area() 메서드를 호출해요 → 4*5=20\n"
            "  r.perimeter()                           →  r 의 perimeter() 메서드를 호출해요 → 2*(4+5)=18\n"
            "  Point p = {2, 3};                       →  x=2, y=3 인 Point 를 만들어요\n"
            "  cout << p.x << ',' << p.y               →  '(' 2 ',' 3 ')' 를 출력해요\n"
            "\n"
            "주의할 점:\n"
            "  - class 에서 생성자를 정의하지 않으면 멤버 변수가 초기화되지 않아요 (쓰레기 값이 들어있을 수 있음!)\n"
            "  - private 멤버에 외부에서 직접 접근하면 컴파일 오류가 나요 (r.w = 10; 은 불가)\n"
            "  - 코딩테스트에서는 보통 struct 로 간단한 데이터 묶음을 만들고,\n"
            "    복잡한 캡슐화가 필요한 경우만 class 를 써요\n"
            "  - 생성자 초기화 리스트(: w(width)) 는 생성자 본체({ }) 안에서 대입하는 것보다 효율적이에요"
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
            "━━ 참조(&)와 포인터 기초 이란? ━━\n"
            "\n"
            "이 개념은 C++ 의 핵심이면서 초보자가 가장 헷갈려하는 부분이에요.\n"
            "천천히 비유와 함께 이해해봐요!\n"
            "\n"
            "[참조(&)] 는 변수의 '별명(별칭)'이에요.\n"
            "홍길동과 '길동이' 는 같은 사람을 가리키잖아요?\n"
            "int& r = a; 는 r 이 a 의 별명이에요. r 을 바꾸면 a 도 바뀌어요!\n"
            "같은 메모리 공간을 두 이름으로 부르는 거예요.\n"
            "\n"
            "[포인터(*)] 는 변수의 '주소(집 번지수)'를 저장하는 특별한 변수예요.\n"
            "a 가 집이라면, &a 는 그 집의 주소(예: '서울시 강남구 123번지')예요.\n"
            "int* p = &a; 는 'a 의 주소를 p 에 저장해요'\n"
            "*p 는 'p 가 가리키는 주소에 있는 값'이에요 (집에 들어가서 내용물 확인하기).\n"
            "\n"
            "왜 함수 매개변수로 참조(&)를 쓰냐고요?\n"
            "함수에 값을 전달할 때 기본적으로 복사가 일어나는데,\n"
            "큰 vector 를 매번 복사하면 매우 느리고 메모리도 많이 써요!\n"
            "참조(&)로 전달하면 복사 없이 원본을 직접 다루니까 훨씬 빠르고 효율적이에요.\n"
            "\n"
            "코드 한 줄씩 읽기:\n"
            "  void addOne(int& x) { x += 1; }    →  참조로 받으므로, 함수 안에서 x 를 바꾸면 원본도 바뀌어요\n"
            "  int a = 10;                         →  a 라는 정수 변수를 만들고 10 을 넣어요\n"
            "  int& ref = a;                       →  ref 는 a 의 별명(참조). ref 와 a 는 같은 메모리 공간\n"
            "  ref = 20;                           →  ref 를 20 으로 바꾸면, 같은 메모리의 a 도 20 이 돼요\n"
            "  cout << \"a = \" << a               →  출력: a = 20 (ref 를 바꿨는데 a 가 바뀐 것 확인!)\n"
            "  int* p = &a;                        →  p 는 포인터, &a 는 a 의 메모리 주소. p 에 주소를 저장해요\n"
            "  cout << \"*p = \" << *p             →  *p 는 역참조: p 가 가리키는 주소(=a)의 값 → 20\n"
            "  *p = 30;                            →  p 가 가리키는 곳(a)의 값을 30 으로 바꿔요\n"
            "  cout << \"a = \" << a               →  출력: a = 30 (*p 를 통해 a 가 바뀐 것 확인!)\n"
            "  addOne(a);                          →  a 를 참조로 넘기므로, 함수 안에서 a 가 직접 +1 돼요\n"
            "  cout << \"a = \" << a               →  출력: a = 31\n"
            "\n"
            "주의할 점:\n"
            "  - 참조는 선언과 동시에 반드시 초기화해야 해요: int& r;  ← 이렇게만 쓰면 컴파일 오류!\n"
            "  - 포인터는 nullptr(아무것도 가리키지 않음)인 상태에서 *p 를 하면 프로그램이 크래시돼요\n"
            "  - 포인터 선언(int* p)과 역참조(*p)는 같은 * 기호지만 전혀 다른 의미예요!\n"
            "    int* p   →  'p 는 포인터 변수다' (타입 선언)\n"
            "    *p = 30  →  'p 가 가리키는 곳의 값을 30 으로 바꿔라' (역참조·값 접근)\n"
            "  - 함수에서 큰 데이터를 수정 없이 전달할 때는 const int& 를 써서 복사도 막고 수정도 막아요\n"
            "  - 참조는 한 번 초기화하면 다른 변수를 가리킬 수 없어요 (포인터는 재배치 가능)"
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
