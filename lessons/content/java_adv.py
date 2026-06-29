"""Java 고급 문법 (스트림/람다/자료구조/제네릭/비트/입출력/Optional)."""

from engine.models import Lesson

LESSONS = [

    Lesson(
        id="java-adv-01",
        lang="java", level="고급",
        title="스트림 API (stream/map/filter/collect)",
        summary="컬렉션을 선언적으로 가공 · 중간연산/최종연산",
        explanation=(
            "스트림은 컬렉션의 원소를 함수형 파이프라인으로 가공하는 도구다.\n"
            "stream() 으로 스트림을 만들고, filter(조건)/map(변환) 같은 중간 연산을 이어 붙인다.\n"
            "collect(Collectors.toList())/sum()/count() 같은 최종 연산이 실행되어야 비로소 계산된다(지연 평가).\n"
            "for 루프 없이 '무엇을 할지'만 기술해 가독성이 높아진다."
        ),
        usage="데이터 필터링/변환/집계를 한 줄로 표현할 때. 코딩테스트보다는 실무 가독성에 강점.",
        cons="단순 반복엔 일반 for 보다 느리고 디버깅이 까다롭다. 대량 원소 박싱 비용도 주의.",
        code=(
            "import java.util.*;\n"
            "import java.util.stream.*;\n"
            "\n"
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        List<Integer> nums = Arrays.asList(1, 2, 3, 4, 5, 6);\n"
            "        // 짝수만 골라 제곱한 뒤 리스트로 수집\n"
            "        List<Integer> result = nums.stream()\n"
            "                .filter(n -> n % 2 == 0)\n"
            "                .map(n -> n * n)\n"
            "                .collect(Collectors.toList());\n"
            "        System.out.println(\"짝수의 제곱: \" + result);\n"
            "\n"
            "        int sum = nums.stream().filter(n -> n > 3).mapToInt(Integer::intValue).sum();\n"
            "        System.out.println(\"3 초과 합계: \" + sum);\n"
            "\n"
            "        List<String> names = Arrays.asList(\"kim\", \"lee\", \"park\");\n"
            "        String joined = names.stream().map(String::toUpperCase).collect(Collectors.joining(\", \"));\n"
            "        System.out.println(\"대문자 연결: \" + joined);\n"
            "    }\n"
            "}\n"
        ),
    ),

    Lesson(
        id="java-adv-02",
        lang="java", level="고급",
        title="람다와 함수형 인터페이스",
        summary="익명 함수 · Function/Predicate/Supplier/Consumer",
        explanation=(
            "람다 (인자) -> 식 은 추상 메서드가 하나뿐인 함수형 인터페이스의 구현을 간결하게 표현한다.\n"
            "자주 쓰는 표준 함수형 인터페이스: Function<T,R>(변환), Predicate<T>(참/거짓),\n"
            "Supplier<T>(공급), Consumer<T>(소비), BiFunction<T,U,R>(두 입력).\n"
            "메서드 참조 Math::abs 처럼 람다를 더 짧게 쓸 수도 있다."
        ),
        usage="콜백, 정렬 비교자(Comparator), 스트림 연산 등에 동작 자체를 인자로 넘길 때.",
        cons="과하게 중첩하면 가독성이 떨어진다. 체크 예외를 던지는 코드는 람다에서 다루기 번거롭다.",
        code=(
            "import java.util.function.*;\n"
            "\n"
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        Function<Integer, Integer> square = x -> x * x;\n"
            "        Predicate<Integer> isEven = x -> x % 2 == 0;\n"
            "        Supplier<String> hello = () -> \"안녕하세요\";\n"
            "        Consumer<String> printer = s -> System.out.println(\"출력: \" + s);\n"
            "        BiFunction<Integer, Integer, Integer> add = (a, b) -> a + b;\n"
            "\n"
            "        System.out.println(\"제곱(5): \" + square.apply(5));\n"
            "        System.out.println(\"4는 짝수? \" + isEven.test(4));\n"
            "        System.out.println(\"공급: \" + hello.get());\n"
            "        printer.accept(hello.get());\n"
            "        System.out.println(\"덧셈(3,7): \" + add.apply(3, 7));\n"
            "\n"
            "        // 함수 합성: andThen\n"
            "        Function<Integer, Integer> squarePlusOne = square.andThen(x -> x + 1);\n"
            "        System.out.println(\"제곱+1(4): \" + squarePlusOne.apply(4));\n"
            "    }\n"
            "}\n"
        ),
    ),

    Lesson(
        id="java-adv-03",
        lang="java", level="고급",
        title="우선순위 큐 (PriorityQueue)",
        summary="힙 기반 · 최소/최대 힙 · O(log n) 삽입/삭제",
        explanation=(
            "PriorityQueue 는 이진 힙으로 구현된 큐로, 항상 우선순위가 가장 높은 원소가 먼저 나온다.\n"
            "기본은 최소 힙(작은 값 우선). poll() 로 꺼내고 peek() 로 확인한다.\n"
            "최대 힙은 Collections.reverseOrder() 나 비교자(Comparator)를 생성자에 넘겨 만든다.\n"
            "삽입/삭제가 O(log n) 이라 다익스트라, top-K 문제에 자주 쓰인다."
        ),
        usage="다익스트라 최단경로, 작업 스케줄링, K번째 최소/최대 값 추적 등.",
        cons="중간 원소 임의 접근/검색은 O(n)으로 느리다. 정렬된 전체 순회는 보장되지 않는다.",
        code=(
            "import java.util.*;\n"
            "\n"
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        // 최소 힙\n"
            "        PriorityQueue<Integer> minHeap = new PriorityQueue<>();\n"
            "        for (int v : new int[]{5, 1, 8, 3, 2}) minHeap.offer(v);\n"
            "        StringBuilder sb = new StringBuilder(\"최소힙 꺼내기: \");\n"
            "        while (!minHeap.isEmpty()) sb.append(minHeap.poll()).append(' ');\n"
            "        System.out.println(sb.toString().trim());\n"
            "\n"
            "        // 최대 힙\n"
            "        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());\n"
            "        for (int v : new int[]{5, 1, 8, 3, 2}) maxHeap.offer(v);\n"
            "        System.out.println(\"최댓값(peek): \" + maxHeap.peek());\n"
            "\n"
            "        // 문자열 길이 기준 우선순위\n"
            "        PriorityQueue<String> byLen = new PriorityQueue<>(Comparator.comparingInt(String::length));\n"
            "        byLen.add(\"가나다\"); byLen.add(\"가\"); byLen.add(\"가나\");\n"
            "        System.out.println(\"가장 짧은 단어: \" + byLen.poll());\n"
            "    }\n"
            "}\n"
        ),
    ),

    Lesson(
        id="java-adv-04",
        lang="java", level="고급",
        title="ArrayDeque (스택/큐)",
        summary="양쪽 끝 O(1) · Stack/LinkedList 대체",
        explanation=(
            "ArrayDeque 는 양방향 큐(deque)로, 앞뒤 모두 O(1) 삽입/삭제가 가능한 배열 기반 자료구조다.\n"
            "스택으로 쓸 때: push/pop/peek (뒤쪽 사용). 큐로 쓸 때: offer/poll (뒤에 넣고 앞에서 꺼냄).\n"
            "구식 Stack 클래스나 LinkedList 보다 빠르고 권장된다.\n"
            "단, null 원소는 허용하지 않는다."
        ),
        usage="DFS의 명시적 스택, BFS 큐, 슬라이딩 윈도우 최댓값(단조 덱) 등.",
        cons="null 저장 불가. 인덱스 임의 접근은 지원하지 않아 중간 조회엔 부적합.",
        code=(
            "import java.util.*;\n"
            "\n"
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        // 스택처럼 사용\n"
            "        Deque<Integer> stack = new ArrayDeque<>();\n"
            "        stack.push(1); stack.push(2); stack.push(3);\n"
            "        System.out.println(\"스택 top: \" + stack.peek());\n"
            "        System.out.print(\"스택 pop 순서: \");\n"
            "        while (!stack.isEmpty()) System.out.print(stack.pop() + \" \");\n"
            "        System.out.println();\n"
            "\n"
            "        // 큐처럼 사용\n"
            "        Deque<String> queue = new ArrayDeque<>();\n"
            "        queue.offer(\"A\"); queue.offer(\"B\"); queue.offer(\"C\");\n"
            "        System.out.print(\"큐 poll 순서: \");\n"
            "        while (!queue.isEmpty()) System.out.print(queue.poll() + \" \");\n"
            "        System.out.println();\n"
            "\n"
            "        // 양끝 활용\n"
            "        Deque<Integer> dq = new ArrayDeque<>();\n"
            "        dq.offerFirst(10); dq.offerLast(20); dq.offerFirst(5);\n"
            "        System.out.println(\"앞: \" + dq.peekFirst() + \", 뒤: \" + dq.peekLast());\n"
            "    }\n"
            "}\n"
        ),
    ),

    Lesson(
        id="java-adv-05",
        lang="java", level="고급",
        title="제네릭 와일드카드 (? extends / ? super)",
        summary="PECS · 읽기는 extends, 쓰기는 super",
        explanation=(
            "와일드카드 ? 는 '어떤 타입인지 모르지만 상관없다'는 의미의 제네릭 타입이다.\n"
            "List<? extends Number> 는 Number 의 하위 타입 리스트 → 원소를 꺼내 읽기(Producer)에 적합.\n"
            "List<? super Integer> 는 Integer 의 상위 타입 리스트 → 원소를 넣기(Consumer)에 적합.\n"
            "이 규칙을 PECS(Producer Extends, Consumer Super)라 부른다."
        ),
        usage="여러 타입을 받는 유연한 유틸 메서드 작성 시. 컬렉션 복사/합산 함수 등.",
        cons="? extends 컬렉션엔 (null 외) 값을 넣을 수 없고, ? super 에서 꺼내면 Object 로만 받는다.",
        code=(
            "import java.util.*;\n"
            "\n"
            "public class Main {\n"
            "    // 생산자: extends 로 읽어서 합산\n"
            "    static double sum(List<? extends Number> list) {\n"
            "        double total = 0;\n"
            "        for (Number n : list) total += n.doubleValue();\n"
            "        return total;\n"
            "    }\n"
            "    // 소비자: super 로 Integer 들을 채워 넣기\n"
            "    static void fill(List<? super Integer> list) {\n"
            "        for (int i = 1; i <= 3; i++) list.add(i);\n"
            "    }\n"
            "    public static void main(String[] args) {\n"
            "        List<Integer> ints = Arrays.asList(1, 2, 3);\n"
            "        List<Double> dbls = Arrays.asList(1.5, 2.5);\n"
            "        System.out.println(\"정수 합: \" + sum(ints));\n"
            "        System.out.println(\"실수 합: \" + sum(dbls));\n"
            "\n"
            "        List<Number> bucket = new ArrayList<>();\n"
            "        fill(bucket);\n"
            "        System.out.println(\"채워진 리스트: \" + bucket);\n"
            "    }\n"
            "}\n"
        ),
    ),

    Lesson(
        id="java-adv-06",
        lang="java", level="고급",
        title="비트 연산과 마스킹",
        summary="& | ^ ~ << >> · 비트마스크 집합",
        explanation=(
            "정수를 2진수 비트들의 모음으로 다루는 연산이다. & (AND), | (OR), ^ (XOR), ~ (NOT),\n"
            "<< / >> (시프트)가 기본이다.\n"
            "i번째 비트 켜기: x | (1<<i), 끄기: x & ~(1<<i), 확인: (x>>i)&1, 토글: x ^ (1<<i).\n"
            "Integer.bitCount(x) 로 켜진 비트 수를 세고, 비트마스크로 부분집합을 정수 하나로 표현한다."
        ),
        usage="부분집합 완전탐색(2^n), 비트마스크 DP, 플래그 집합, 빠른 곱셈/나눗셈(시프트).",
        cons="가독성이 낮아 실수하기 쉽고, 음수/오버플로 처리에 주의해야 한다(부호 비트).",
        code=(
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        int a = 0b1100, b = 0b1010;  // 12, 10\n"
            "        System.out.println(\"AND: \" + (a & b));   // 8\n"
            "        System.out.println(\"OR : \" + (a | b));   // 14\n"
            "        System.out.println(\"XOR: \" + (a ^ b));   // 6\n"
            "        System.out.println(\"왼쪽 시프트 3<<2: \" + (3 << 2));  // 12\n"
            "\n"
            "        int set = 0;\n"
            "        set |= (1 << 1);   // 1번 원소 추가\n"
            "        set |= (1 << 3);   // 3번 원소 추가\n"
            "        System.out.println(\"3번 포함? \" + (((set >> 3) & 1) == 1));\n"
            "        set &= ~(1 << 1);  // 1번 원소 제거\n"
            "        System.out.println(\"1번 포함? \" + (((set >> 1) & 1) == 1));\n"
            "        System.out.println(\"켜진 비트 수: \" + Integer.bitCount(0b10110));  // 3\n"
            "\n"
            "        // {1,2,3} 의 모든 부분집합 개수 출력\n"
            "        int n = 3, cnt = 0;\n"
            "        for (int mask = 0; mask < (1 << n); mask++) cnt++;\n"
            "        System.out.println(\"부분집합 개수: \" + cnt);  // 8\n"
            "    }\n"
            "}\n"
        ),
    ),

    Lesson(
        id="java-adv-07",
        lang="java", level="고급",
        title="입출력 최적화 (BufferedReader + StringBuilder)",
        summary="대량 입력은 버퍼링 · 출력은 모아서 한 번에",
        explanation=(
            "Scanner 와 매 줄 println 은 대량 데이터에서 느려 시간 초과의 원인이 된다.\n"
            "입력은 BufferedReader(new InputStreamReader(System.in)) 로 한 줄씩 읽고\n"
            "StringTokenizer/split 으로 토큰을 나누는 것이 빠르다.\n"
            "출력은 StringBuilder 에 모아 마지막에 한 번만 출력(System.out.print)하면 I/O 횟수가 줄어 빠르다."
        ),
        usage="백준 등 입력이 수십만 줄인 문제. 출력 줄 수가 많을 때 특히 효과적.",
        cons="코드가 길어지고 IOException 처리가 필요하다. 입력이 작으면 체감 차이는 거의 없다.",
        code=(
            "import java.io.*;\n"
            "import java.util.*;\n"
            "\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        // 데모: System.in 대신 고정 문자열을 같은 방식으로 처리\n"
            "        String input = \"3\\n10 20\\n5 7\\n100 1\\n\";\n"
            "        BufferedReader br = new BufferedReader(new StringReader(input));\n"
            "        StringBuilder sb = new StringBuilder();\n"
            "\n"
            "        int n = Integer.parseInt(br.readLine().trim());\n"
            "        for (int i = 0; i < n; i++) {\n"
            "            StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "            int x = Integer.parseInt(st.nextToken());\n"
            "            int y = Integer.parseInt(st.nextToken());\n"
            "            sb.append(x + y).append('\\n');   // 출력은 모아서\n"
            "        }\n"
            "        System.out.print(sb);   // 마지막에 한 번만 출력\n"
            "    }\n"
            "}\n"
        ),
    ),

    Lesson(
        id="java-adv-08",
        lang="java", level="고급",
        title="Optional과 제네릭 메서드",
        summary="null 안전 처리 · 타입 매개변수 <T> 메서드",
        explanation=(
            "Optional<T> 는 값이 있을 수도/없을 수도 있음을 명시해 NullPointerException 을 예방한다.\n"
            "of/ofNullable 로 만들고, isPresent/orElse/map 으로 안전하게 다룬다.\n"
            "제네릭 메서드는 반환형 앞에 <T> 를 두어 호출마다 타입이 정해지는 메서드다.\n"
            "두 기능을 조합하면 타입에 독립적이면서 null 안전한 유틸을 만들 수 있다."
        ),
        usage="조회 결과가 없을 수 있는 메서드의 반환형, 타입 무관한 공통 알고리즘(최댓값 등) 작성.",
        cons="Optional 을 필드/매개변수로 남발하면 오히려 복잡해진다. 반환형 용도로 쓰는 것이 권장된다.",
        code=(
            "import java.util.*;\n"
            "\n"
            "public class Main {\n"
            "    // 제네릭 메서드: 리스트의 최댓값을 Optional 로 반환\n"
            "    static <T extends Comparable<T>> Optional<T> maxOf(List<T> list) {\n"
            "        if (list.isEmpty()) return Optional.empty();\n"
            "        T best = list.get(0);\n"
            "        for (T x : list) if (x.compareTo(best) > 0) best = x;\n"
            "        return Optional.of(best);\n"
            "    }\n"
            "    public static void main(String[] args) {\n"
            "        List<Integer> nums = Arrays.asList(3, 9, 1, 7);\n"
            "        Optional<Integer> m = maxOf(nums);\n"
            "        System.out.println(\"최댓값: \" + m.orElse(-1));\n"
            "\n"
            "        List<String> empty = new ArrayList<>();\n"
            "        System.out.println(\"빈 리스트 최댓값: \" + maxOf(empty).orElse(\"없음\"));\n"
            "\n"
            "        String name = null;\n"
            "        String shown = Optional.ofNullable(name).map(String::toUpperCase).orElse(\"손님\");\n"
            "        System.out.println(\"이름: \" + shown);\n"
            "    }\n"
            "}\n"
        ),
    ),
]
