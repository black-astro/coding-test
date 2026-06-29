"""C++ 고급 문법 (코딩테스트 STL/문법 핵심 8꼭지)."""

from engine.models import Lesson

LESSONS = [

    Lesson(
        id="cpp-adv-01",
        lang="cpp", level="고급",
        title="우선순위 큐(priority_queue) — 최소/최대 힙",
        summary="기본 최대 힙 · greater 로 최소 힙",
        explanation=(
            "priority_queue 는 내부적으로 힙으로 구현되어 top() 으로 항상 최댓값을 O(1) 에 본다.\n"
            "기본 선언 priority_queue<int> 는 최대 힙이다.\n"
            "최소 힙은 priority_queue<int, vector<int>, greater<int>> 로 비교자를 바꿔 만든다.\n"
            "push/pop 은 O(log n) 이며, 다익스트라·우선순위 처리에 필수다."
        ),
        usage="다익스트라 최단경로, K번째 큰 수, 작업 스케줄링 등 '항상 최대/최소를 빠르게' 꺼내야 할 때.",
        cons="중간 원소 조회·임의 삭제가 불가능하다. 그런 연산이 필요하면 set/multiset 를 쓴다.",
        code=(
            "#include <bits/stdc++.h>\n"
            "using namespace std;\n"
            "\n"
            "int main() {\n"
            "    // 최대 힙 (기본)\n"
            "    priority_queue<int> maxHeap;\n"
            "    for (int x : {3, 1, 4, 1, 5, 9}) maxHeap.push(x);\n"
            "    cout << \"최댓값: \" << maxHeap.top() << \"\\n\";   // 9\n"
            "\n"
            "    // 최소 힙\n"
            "    priority_queue<int, vector<int>, greater<int>> minHeap;\n"
            "    for (int x : {3, 1, 4, 1, 5, 9}) minHeap.push(x);\n"
            "    cout << \"최솟값: \" << minHeap.top() << \"\\n\";   // 1\n"
            "\n"
            "    // 최소 힙에서 꺼내면 오름차순\n"
            "    cout << \"오름차순: \";\n"
            "    while (!minHeap.empty()) {\n"
            "        cout << minHeap.top() << ' ';\n"
            "        minHeap.pop();\n"
            "    }\n"
            "    cout << \"\\n\";\n"
            "    return 0;\n"
            "}\n"
        ),
    ),

    Lesson(
        id="cpp-adv-02",
        lang="cpp", level="고급",
        title="deque · stack · queue",
        summary="양끝 덱 · LIFO 스택 · FIFO 큐",
        explanation=(
            "deque 는 앞뒤 양쪽에서 O(1) 로 삽입·삭제가 되는 양방향 큐다.\n"
            "stack 은 LIFO(후입선출)로 push/pop/top 을 제공한다.\n"
            "queue 는 FIFO(선입선출)로 push/pop/front/back 을 제공한다.\n"
            "stack 과 queue 는 기본적으로 deque 를 어댑터로 감싸 만든 구조다."
        ),
        usage="BFS 는 queue, DFS·괄호검사·후위표기는 stack, 슬라이딩 윈도우 최댓값은 deque 가 정석이다.",
        cons="stack/queue 는 중간 원소 접근이 안 된다. deque 는 인덱스 접근은 되지만 중간 삽입은 느리다.",
        code=(
            "#include <bits/stdc++.h>\n"
            "using namespace std;\n"
            "\n"
            "int main() {\n"
            "    deque<int> dq;\n"
            "    dq.push_back(2);\n"
            "    dq.push_front(1);\n"
            "    dq.push_back(3);\n"
            "    cout << \"덱 앞/뒤: \" << dq.front() << ' ' << dq.back() << \"\\n\"; // 1 3\n"
            "\n"
            "    stack<int> st;\n"
            "    st.push(10); st.push(20); st.push(30);\n"
            "    cout << \"스택 top: \" << st.top() << \"\\n\";  // 30 (마지막에 넣은 것)\n"
            "\n"
            "    queue<int> q;\n"
            "    q.push(10); q.push(20); q.push(30);\n"
            "    cout << \"큐 front: \" << q.front() << \"\\n\"; // 10 (처음에 넣은 것)\n"
            "    return 0;\n"
            "}\n"
        ),
    ),

    Lesson(
        id="cpp-adv-03",
        lang="cpp", level="고급",
        title="람다와 함수 객체",
        summary="[](){}  · 캡처 · 커스텀 정렬",
        explanation=(
            "람다는 [캡처](매개변수){ 본문 } 형태로 이름 없는 함수를 즉석에서 만든다.\n"
            "[] 는 캡처 없음, [&] 는 참조 캡처, [=] 는 값 복사 캡처, [x] 는 x만 값 캡처다.\n"
            "sort 의 세 번째 인자나 for_each 등 알고리즘의 비교자/동작으로 자주 넘긴다.\n"
            "함수 객체(functor)는 operator() 를 가진 구조체로, 람다와 같은 역할을 한다."
        ),
        usage="정렬 기준을 즉석에서 지정하거나, 알고리즘에 동작을 인자로 넘길 때 코드가 간결해진다.",
        cons="캡처를 [&] 로 무심코 쓰면 수명이 끝난 변수를 참조해 버그가 날 수 있어 캡처 범위를 명확히 해야 한다.",
        code=(
            "#include <bits/stdc++.h>\n"
            "using namespace std;\n"
            "\n"
            "int main() {\n"
            "    vector<int> v = {5, 2, 8, 1, 9, 3};\n"
            "\n"
            "    // 내림차순 정렬 (람다 비교자)\n"
            "    sort(v.begin(), v.end(), [](int a, int b) {\n"
            "        return a > b;\n"
            "    });\n"
            "    cout << \"내림차순: \";\n"
            "    for (int x : v) cout << x << ' ';\n"
            "    cout << \"\\n\";\n"
            "\n"
            "    // 값 캡처: 기준값보다 큰 원소 개수 세기\n"
            "    int 기준 = 4;\n"
            "    int cnt = count_if(v.begin(), v.end(), [기준](int x) {\n"
            "        return x > 기준;\n"
            "    });\n"
            "    cout << 기준 << \"보다 큰 원소 수: \" << cnt << \"\\n\"; // 3\n"
            "    return 0;\n"
            "}\n"
        ),
    ),

    Lesson(
        id="cpp-adv-04",
        lang="cpp", level="고급",
        title="이터레이터와 알고리즘 — lower_bound · upper_bound · accumulate",
        summary="이분 탐색 위치 · 구간 합",
        explanation=(
            "lower_bound 는 정렬된 범위에서 'x 이상'이 처음 나오는 위치(이터레이터)를 O(log n)에 찾는다.\n"
            "upper_bound 는 'x 초과'가 처음 나오는 위치를 찾는다. 두 위치의 차이가 x의 개수다.\n"
            "위치를 인덱스로 바꾸려면 it - v.begin() 처럼 begin 을 빼면 된다.\n"
            "accumulate(begin, end, 초기값) 은 구간의 누적합(또는 사용자 연산)을 계산한다."
        ),
        usage="정렬된 배열에서 특정 값의 개수·삽입 위치를 빠르게 구하거나, 합/곱 누적을 한 줄로 처리할 때.",
        cons="lower_bound/upper_bound 는 범위가 반드시 정렬돼 있어야 정확하다. 정렬이 깨지면 결과가 틀린다.",
        code=(
            "#include <bits/stdc++.h>\n"
            "using namespace std;\n"
            "\n"
            "int main() {\n"
            "    vector<int> v = {1, 2, 2, 2, 4, 5, 7};  // 정렬된 상태\n"
            "\n"
            "    auto lo = lower_bound(v.begin(), v.end(), 2); // 2 이상 첫 위치\n"
            "    auto hi = upper_bound(v.begin(), v.end(), 2); // 2 초과 첫 위치\n"
            "    cout << \"2의 시작 인덱스: \" << (lo - v.begin()) << \"\\n\"; // 1\n"
            "    cout << \"2의 개수: \" << (hi - lo) << \"\\n\";              // 3\n"
            "\n"
            "    int sum = accumulate(v.begin(), v.end(), 0);\n"
            "    cout << \"전체 합: \" << sum << \"\\n\";   // 23\n"
            "    return 0;\n"
            "}\n"
        ),
    ),

    Lesson(
        id="cpp-adv-05",
        lang="cpp", level="고급",
        title="비트 연산과 비트마스킹",
        summary="& | ^ ~ << >> · 부분집합 표현",
        explanation=(
            "비트 연산자: AND(&), OR(|), XOR(^), NOT(~), 왼쪽시프트(<<), 오른쪽시프트(>>).\n"
            "i번째 비트 켜기 mask |= (1<<i), 끄기 mask &= ~(1<<i), 확인 mask & (1<<i).\n"
            "비트마스킹으로 n개 원소의 부분집합을 0~(2^n - 1) 의 정수 하나로 표현할 수 있다.\n"
            "__builtin_popcount(x) 는 켜진 비트(1) 개수를 빠르게 센다."
        ),
        usage="집합 DP(외판원 TSP 등), 상태 압축, 부분집합 전체 탐색에서 메모리·속도를 크게 아낀다.",
        cons="가독성이 떨어지고 우선순위 실수가 잦다. (1<<i) 처럼 괄호를 꼭 씌우고, n이 크면 2^n 폭발에 주의.",
        code=(
            "#include <bits/stdc++.h>\n"
            "using namespace std;\n"
            "\n"
            "int main() {\n"
            "    int mask = 0;\n"
            "    mask |= (1 << 1);   // 1번 비트 켜기\n"
            "    mask |= (1 << 3);   // 3번 비트 켜기\n"
            "    cout << \"mask = \" << mask << \"\\n\";              // 10 (2진수 1010)\n"
            "    cout << \"1번 비트 켜짐? \" << ((mask & (1 << 1)) ? 1 : 0) << \"\\n\"; // 1\n"
            "    cout << \"켜진 비트 수: \" << __builtin_popcount(mask) << \"\\n\";     // 2\n"
            "\n"
            "    // {A,B,C} 3원소의 모든 부분집합 출력\n"
            "    string item[3] = {\"A\", \"B\", \"C\"};\n"
            "    for (int s = 0; s < (1 << 3); s++) {\n"
            "        cout << '{';\n"
            "        for (int i = 0; i < 3; i++)\n"
            "            if (s & (1 << i)) cout << item[i];\n"
            "        cout << \"} \";\n"
            "    }\n"
            "    cout << \"\\n\";\n"
            "    return 0;\n"
            "}\n"
        ),
    ),

    Lesson(
        id="cpp-adv-06",
        lang="cpp", level="고급",
        title="빠른 입출력 — ios_base::sync_with_stdio",
        summary="C 스트림 동기화 해제 · cin.tie 해제",
        explanation=(
            "기본적으로 cin/cout 은 C 의 scanf/printf 와 동기화되어 있어 느리다.\n"
            "ios_base::sync_with_stdio(false); 로 동기화를 끊으면 cin/cout 이 훨씬 빨라진다.\n"
            "cin.tie(NULL); 은 cin 전 cout 자동 flush 를 막아 입출력이 섞이는 비용을 없앤다.\n"
            "개행은 endl 대신 '\\n' 을 쓰는 게 좋다(endl 은 매번 flush 하여 느리다)."
        ),
        usage="입력이 수십만 줄 이상인 백준 문제에서 시간초과를 피하는 거의 필수 관용구.",
        cons="동기화를 끄면 C 입출력(scanf/printf)과 섞어 쓰면 안 된다. main 시작부에 한 번만 설정한다.",
        code=(
            "#include <bits/stdc++.h>\n"
            "using namespace std;\n"
            "\n"
            "int main() {\n"
            "    ios_base::sync_with_stdio(false);\n"
            "    cin.tie(NULL);\n"
            "\n"
            "    // 데모: 입력 대신 고정값으로 빠른 출력 시연\n"
            "    int n = 5;\n"
            "    long long sum = 0;\n"
            "    for (int i = 1; i <= n; i++) {\n"
            "        sum += i;\n"
            "        cout << i << (i < n ? ' ' : '\\n');  // endl 대신 '\\n'\n"
            "    }\n"
            "    cout << \"합: \" << sum << \"\\n\";   // 15\n"
            "    return 0;\n"
            "}\n"
        ),
    ),

    Lesson(
        id="cpp-adv-07",
        lang="cpp", level="고급",
        title="multiset · multimap",
        summary="중복 허용 정렬 컨테이너",
        explanation=(
            "multiset 은 중복을 허용하는 정렬된 집합으로, 삽입·삭제·탐색이 O(log n) 이다.\n"
            "원소를 넣으면 자동으로 정렬되어 begin() 이 최솟값, rbegin() 이 최댓값을 가리킨다.\n"
            "주의: erase(값) 은 같은 값을 '전부' 지운다. 하나만 지우려면 erase(find(값)) 를 쓴다.\n"
            "multimap 은 같은 키에 여러 값을 저장할 수 있는 정렬된 맵이다."
        ),
        usage="정렬 상태를 유지하면서 중복값을 다루거나, 최솟/최댓값을 계속 꺼내며 임의 삭제도 필요할 때.",
        cons="해시(unordered_*)보다 상수가 크고 메모리도 더 쓴다. 단순 조회만 필요하면 unordered 계열이 빠르다.",
        code=(
            "#include <bits/stdc++.h>\n"
            "using namespace std;\n"
            "\n"
            "int main() {\n"
            "    multiset<int> ms;\n"
            "    for (int x : {5, 1, 3, 1, 5, 1}) ms.insert(x);\n"
            "\n"
            "    cout << \"정렬+중복: \";\n"
            "    for (int x : ms) cout << x << ' ';   // 1 1 1 3 5 5\n"
            "    cout << \"\\n\";\n"
            "    cout << \"1의 개수: \" << ms.count(1) << \"\\n\";   // 3\n"
            "    cout << \"최솟값: \" << *ms.begin() << \"\\n\";      // 1\n"
            "\n"
            "    ms.erase(ms.find(1));   // 1을 '하나만' 삭제\n"
            "    cout << \"하나 삭제 후 1의 개수: \" << ms.count(1) << \"\\n\"; // 2\n"
            "\n"
            "    multimap<string, int> mm;\n"
            "    mm.insert({\"kim\", 90});\n"
            "    mm.insert({\"kim\", 85});\n"
            "    cout << \"kim 키 개수: \" << mm.count(\"kim\") << \"\\n\"; // 2\n"
            "    return 0;\n"
            "}\n"
        ),
    ),

    Lesson(
        id="cpp-adv-08",
        lang="cpp", level="고급",
        title="auto · 범위 기반 for · 구조적 바인딩",
        summary="타입 추론 · for(x : v) · auto [a,b]",
        explanation=(
            "auto 는 초기값으로부터 타입을 자동 추론해 긴 타입 이름을 줄여 준다.\n"
            "범위 기반 for( for (auto x : v) )는 컨테이너를 인덱스 없이 순회한다.\n"
            "원소를 수정하거나 복사 비용을 줄이려면 참조로 받는다: for (auto& x : v).\n"
            "구조적 바인딩 auto [a, b] = pair; 는 pair/tuple/구조체를 한 번에 분해한다(C++17)."
        ),
        usage="map 순회 시 auto& [key, val], 이터레이터 타입 생략 등에서 코드가 짧고 명확해진다.",
        cons="auto 는 의도한 타입과 다르게 추론될 수 있어(예: 참조가 복사로) 성능·동작 의도를 분명히 해야 한다.",
        code=(
            "#include <bits/stdc++.h>\n"
            "using namespace std;\n"
            "\n"
            "int main() {\n"
            "    vector<int> v = {10, 20, 30};\n"
            "\n"
            "    // 범위 기반 for + 참조로 값 수정\n"
            "    for (auto& x : v) x += 1;\n"
            "    cout << \"수정 후: \";\n"
            "    for (auto x : v) cout << x << ' ';   // 11 21 31\n"
            "    cout << \"\\n\";\n"
            "\n"
            "    // map 순회 + 구조적 바인딩\n"
            "    map<string, int> score = {{\"kim\", 90}, {\"lee\", 80}};\n"
            "    for (const auto& [name, point] : score)\n"
            "        cout << name << \": \" << point << \"\\n\";\n"
            "\n"
            "    // pair 분해\n"
            "    auto [a, b] = make_pair(1, 2);\n"
            "    cout << \"a+b = \" << a + b << \"\\n\";   // 3\n"
            "    return 0;\n"
            "}\n"
        ),
    ),
]
