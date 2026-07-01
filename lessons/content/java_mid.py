"""Java 중급 문법 (컬렉션 · 제네릭 · 객체지향 · 예외 · 문자열 · 정렬)."""

from engine.models import Lesson

LESSONS = [

    Lesson(
        id="java-mid-01",
        lang="java", level="중급",
        title="List와 ArrayList",
        summary="가변 배열 · add/get/size · for-each",
        explanation=(
            "[개요]\n"
            "List는 순서가 있는 값의 모음을 다루는 컬렉션 인터페이스이며, 추가·삭제·조회가 가능하고 삽입 순서가 유지된다.\n"
            "ArrayList는 List의 대표 구현체로, 저장 요소 수에 따라 내부 배열 크기가 자동으로 확장된다.\n"
            "\n"
            "[핵심 개념]\n"
            "• 일반 배열(int[] arr)은 생성 시 크기를 고정해야 한다(예: int[] arr = new int[5]는 5칸으로 고정).\n"
            "• ArrayList는 크기가 자동으로 늘어나므로 요소를 계속 추가할 수 있다.\n"
            "• 요소 개수를 미리 알 수 없는 경우 ArrayList를 사용한다.\n"
            "\n"
            "[코드 분석]\n"
            "• import java.util.*;                          → 컬렉션 라이브러리를 불러온다. 이 선언이 없으면 ArrayList, List 등을 사용할 수 없다.\n"
            "• List<String> fruits = new ArrayList<>();     → String만 담을 수 있는 리스트를 생성한다. List<String>은 인터페이스(설계도), new ArrayList<>()는 구현체(실제 객체)이다. <String>은 저장 가능한 타입을 String으로 제한하는 표시이다. 인터페이스 타입으로 선언하면 이후 LinkedList 등으로 교체할 때 이 줄만 수정하면 된다.\n"
            "• fruits.add(\"사과\");                          → 리스트 끝에 \"사과\"를 추가한다.\n"
            "• fruits.add(\"바나나\");                        → \"바나나\"를 추가한다. 리스트는 [사과, 바나나]가 된다.\n"
            "• fruits.add(\"포도\");                          → \"포도\"를 추가한다. 최종 상태는 [사과, 바나나, 포도]이다.\n"
            "• System.out.println(\"개수: \" + fruits.size()); → size()는 리스트의 항목 수를 반환한다. 현재 3개이므로 \"개수: 3\"이 출력된다.\n"
            "• System.out.println(\"첫번째: \" + fruits.get(0)); → get(0)은 0번 위치의 항목을 반환한다. Java의 인덱스는 0부터 시작하므로 0=사과, 1=바나나, 2=포도이며 첫 번째 요소는 get(0)이다.\n"
            "• for (String f : fruits) {                    → fruits의 모든 항목을 하나씩 f에 담아 반복한다(사과 → 바나나 → 포도). 이 구문을 for-each 문이라 한다.\n"
            "• System.out.println(\"과일 = \" + f);           → 현재 반복 중인 항목 f를 출력한다.\n"
            "\n"
            "[유의 사항]\n"
            "• get(인덱스)에서 범위를 벗어나면 IndexOutOfBoundsException이 발생한다(예: 항목이 3개인데 fruits.get(5) 호출).\n"
            "• List<String>으로 선언했다면 숫자 등 다른 타입은 넣을 수 없으며, 시도 시 컴파일 오류가 발생한다.\n"
            "• 유효한 인덱스 범위는 0 이상 size()-1 이하이다."
        ),
        usage="크기가 변하는 목록을 다룰 때 기본으로 사용한다. 인덱스 조회가 빠르다(O(1)).",
        cons="중간 삽입/삭제는 뒤 요소를 모두 옮겨야 해서 O(n)으로 느리다. 그런 연산이 잦으면 LinkedList 고려.",
        code=(
            "import java.util.*;\n"
            "\n"
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        List<String> fruits = new ArrayList<>();\n"
            "        fruits.add(\"사과\");\n"
            "        fruits.add(\"바나나\");\n"
            "        fruits.add(\"포도\");\n"
            "        System.out.println(\"개수: \" + fruits.size());\n"
            "        System.out.println(\"첫번째: \" + fruits.get(0));\n"
            "        for (String f : fruits) {\n"
            "            System.out.println(\"과일 = \" + f);\n"
            "        }\n"
            "    }\n"
            "}\n"
        ),
    ),

    Lesson(
        id="java-mid-02",
        lang="java", level="중급",
        title="Map과 HashMap",
        summary="키-값 저장 · put/get · getOrDefault",
        explanation=(
            "[개요]\n"
            "Map은 키(key)와 값(value)의 쌍을 저장하는 자료구조이다. 사전에서 단어(키)로 뜻(값)을 찾는 구조와 동일하다.\n"
            "예를 들어 \"사과\" → 3, \"배\" → 2와 같이 단어별 등장 횟수를 기록하는 데 적합하다.\n"
            "\n"
            "[핵심 개념]\n"
            "• HashMap은 Map의 가장 흔한 구현체이다.\n"
            "• 해시(hash) 기법으로 값을 저장하므로 조회 속도가 매우 빠르다(평균 O(1)).\n"
            "\n"
            "[코드 분석]\n"
            "• Map<String, Integer> count = new HashMap<>();   → 키는 String, 값은 Integer인 HashMap을 생성한다. 즉 '단어 → 개수'를 기록하는 사전이다.\n"
            "• String[] words = {\"사과\", \"배\", \"사과\", \"사과\", \"배\"};  → 단어 배열이며, 사과가 3번, 배가 2번 포함되어 있다.\n"
            "• for (String w : words) {                        → 배열의 단어를 하나씩 w에 담아 반복한다.\n"
            "• count.put(w, count.getOrDefault(w, 0) + 1);    → 빈도수 집계의 핵심 로직이다. 다음 순서로 동작한다.\n"
            "  1) count.getOrDefault(w, 0) → 현재 w의 카운트를 가져오되, Map에 없으면 기본값 0을 반환한다.\n"
            "  2) ... + 1 → 이번 등장을 반영해 1을 더한다.\n"
            "  3) count.put(w, ...) → 계산된 값을 Map에 저장한다.\n"
            "  결과적으로 '사과'는 첫 등장 시 0+1=1, 두 번째 1+1=2, 세 번째 2+1=3이 된다.\n"
            "• System.out.println(\"사과 = \" + count.get(\"사과\")); → get(\"사과\")로 \"사과\" 키의 값을 조회한다. 결과는 3이다.\n"
            "• System.out.println(\"배 = \" + count.get(\"배\"));     → \"배\"는 2번 등장했으므로 2가 반환된다.\n"
            "• System.out.println(\"전체 = \" + count);              → Map 전체를 출력하면 {사과=3, 배=2} 형태로 표시된다.\n"
            "\n"
            "[유의 사항]\n"
            "• 존재하지 않는 키를 get하면 null이 반환된다. 이를 그대로 사용하면 NullPointerException이 발생할 수 있으므로 getOrDefault(키, 기본값) 사용이 안전하다.\n"
            "• HashMap은 저장 순서를 보장하지 않으므로 출력 순서가 삽입 순서와 다를 수 있다.\n"
            "• 삽입 순서를 유지하려면 LinkedHashMap을 사용한다."
        ),
        usage="단어 빈도수 세기, 이름→점수 매핑 등 키로 값을 빠르게 찾아야 할 때 쓴다.",
        cons="저장 순서가 보장되지 않는다. 순서가 필요하면 LinkedHashMap, 정렬이 필요하면 TreeMap 을 쓴다.",
        code=(
            "import java.util.*;\n"
            "\n"
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        Map<String, Integer> count = new HashMap<>();\n"
            "        String[] words = {\"사과\", \"배\", \"사과\", \"사과\", \"배\"};\n"
            "        for (String w : words) {\n"
            "            count.put(w, count.getOrDefault(w, 0) + 1);\n"
            "        }\n"
            "        System.out.println(\"사과 = \" + count.get(\"사과\"));\n"
            "        System.out.println(\"배 = \" + count.get(\"배\"));\n"
            "        System.out.println(\"전체 = \" + count);\n"
            "    }\n"
            "}\n"
        ),
    ),

    Lesson(
        id="java-mid-03",
        lang="java", level="중급",
        title="Set과 HashSet",
        summary="중복 제거 · contains · 집합",
        explanation=(
            "[개요]\n"
            "Set은 중복을 허용하지 않는 컬렉션이다. 이미 존재하는 값을 추가해도 반영되지 않는다.\n"
            "\n"
            "[핵심 개념]\n"
            "주요 활용 상황은 다음과 같다.\n"
            "• 특정 값을 이미 본 적이 있는지 빠르게 확인할 때\n"
            "• 배열에서 중복을 제거할 때\n"
            "• 방문한 좌표를 기록하여 방문 여부를 확인할 때(BFS/DFS에서 자주 사용)\n"
            "HashSet은 Set의 대표 구현체로, 해시 기법으로 동작하여 포함 여부 확인(contains)이 매우 빠르다(평균 O(1)). 반면 ArrayList의 contains는 처음부터 끝까지 탐색하므로 O(n)이다.\n"
            "\n"
            "[코드 분석]\n"
            "• int[] data = {1, 2, 2, 3, 3, 3, 4};  → 중복이 포함된 정수 배열이다(2는 두 번, 3은 세 번).\n"
            "• Set<Integer> set = new HashSet<>();   → Integer를 담는 HashSet을 생성한다. 기본형 int는 제네릭에 사용할 수 없으므로 래퍼 클래스 Integer를 사용한다.\n"
            "• for (int x : data) {                 → 배열의 값을 하나씩 x에 담아 반복한다.\n"
            "• set.add(x);                          → x를 Set에 추가한다. 이미 존재하는 값이면 무시되며 오류는 발생하지 않는다. 진행 과정은 다음과 같다.\n"
            "    1 추가 → {1}\n"
            "    2 추가 → {1, 2}\n"
            "    2 재추가 → {1, 2} (변화 없음)\n"
            "    3 추가 → {1, 2, 3}\n"
            "    3 재추가 → {1, 2, 3} (변화 없음)\n"
            "    3 재추가 → {1, 2, 3} (변화 없음)\n"
            "    4 추가 → {1, 2, 3, 4}\n"
            "• System.out.println(\"고유 개수: \" + set.size());       → 고유한 값의 개수를 반환한다. 결과는 4(1,2,3,4)이다.\n"
            "• System.out.println(\"3 포함? \" + set.contains(3));    → 3이 Set에 있으면 true, 없으면 false를 반환한다. 결과는 true이다.\n"
            "• System.out.println(\"9 포함? \" + set.contains(9));    → 9는 배열에 없었으므로 Set에도 없다. 결과는 false이다.\n"
            "\n"
            "[활용 패턴]\n"
            "• 배열/리스트에서 중복 제거:\n"
            "  List<Integer> list = Arrays.asList(1, 2, 2, 3);\n"
            "  Set<Integer> unique = new HashSet<>(list);  // {1, 2, 3}\n"
            "\n"
            "[유의 사항]\n"
            "• HashSet은 저장 순서를 보장하지 않아 출력 순서가 삽입 순서와 다를 수 있다.\n"
            "• 삽입 순서를 유지하려면 LinkedHashSet을, 정렬된 순서를 유지하려면 TreeSet을 사용한다.\n"
            "• 기본형 int 대신 Integer를 사용한다. 자동 박싱이 일어나지만 명시적으로 사용하는 것이 안전하다."
        ),
        usage="중복 제거, '이미 본 적 있는지' 빠른 확인, 방문 체크 등에 쓴다(평균 O(1)).",
        cons="저장 순서가 보장되지 않는다. 삽입 순서 유지가 필요하면 LinkedHashSet 을 사용한다.",
        code=(
            "import java.util.*;\n"
            "\n"
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        int[] data = {1, 2, 2, 3, 3, 3, 4};\n"
            "        Set<Integer> set = new HashSet<>();\n"
            "        for (int x : data) {\n"
            "            set.add(x);\n"
            "        }\n"
            "        System.out.println(\"고유 개수: \" + set.size());\n"
            "        System.out.println(\"3 포함? \" + set.contains(3));\n"
            "        System.out.println(\"9 포함? \" + set.contains(9));\n"
            "    }\n"
            "}\n"
        ),
    ),

    Lesson(
        id="java-mid-04",
        lang="java", level="중급",
        title="제네릭(Generics)",
        summary="타입 매개변수 <T> · 타입 안전",
        explanation=(
            "[개요]\n"
            "제네릭은 클래스나 메서드가 다룰 타입을 매개변수로 지정하여, 여러 타입에 재사용 가능하면서도 타입 안전성을 확보하는 기법이다. 컨테이너에 타입 라벨을 부여하여 꺼낼 때 해당 타입임을 보장하는 것과 같다.\n"
            "\n"
            "[핵심 개념]\n"
            "• 제네릭을 사용하지 않는 방식은 Object로 저장 후 강제 형변환이 필요하며, 실수 시 ClassCastException이 발생한다.\n"
            "  Object value = \"안녕\";\n"
            "  String s = (String) value;  // 강제 형변환 필요\n"
            "• 제네릭을 사용하면 형변환 없이 타입이 보장된다.\n"
            "  Box<String> box = new Box<>();\n"
            "  box.set(\"안녕\");\n"
            "  String s = box.get();  // 형변환 불필요, 컴파일러가 String임을 인지\n"
            "\n"
            "[코드 분석]\n"
            "• static class Box<T> {              → <T>는 타입 매개변수이다. T는 이름일 뿐이며 사용 시 실제 타입으로 치환된다. Box<String>이면 T가 String, Box<Integer>면 T가 Integer가 된다. 관례상 T(Type), E(Element), K(Key), V(Value)를 사용한다.\n"
            "• private T value;                   → T 타입의 value 필드를 선언한다. 구체적 타입은 사용 시점에 결정된다.\n"
            "• public void set(T v) { this.value = v; }  → T 타입의 값 v를 받아 저장한다. Box<String>이면 String을, Box<Integer>면 Integer를 받는다.\n"
            "• public T get() { return value; }   → 저장된 값을 T 타입으로 반환한다. 조회 시 형변환이 불필요하다.\n"
            "• Box<String> s = new Box<>();       → 이 시점에 T가 String으로 확정되어 문자열 전용 상자가 된다.\n"
            "• s.set(\"안녕\");                      → 문자열 \"안녕\"을 저장한다. T=String이므로 String만 허용되며, 숫자를 넣으면 컴파일 오류가 발생한다.\n"
            "• System.out.println(\"문자열 상자: \" + s.get());  → 조회 시 String 타입이 보장되므로 별도 캐스팅이 불필요하다.\n"
            "• Box<Integer> n = new Box<>();      → T가 Integer로 확정되어 정수 전용 상자가 된다.\n"
            "• n.set(42);                         → 정수 42를 저장한다. int 42가 Integer 42로 자동 박싱된다.\n"
            "• System.out.println(\"정수 상자: \" + n.get());    → 42가 출력된다.\n"
            "\n"
            "[제네릭 사용의 이점]\n"
            "1. 타입 안전: 잘못된 타입은 실행 전 컴파일 단계에서 오류로 검출된다.\n"
            "2. 형변환 불필요: 조회 시 (String) 등의 캐스팅이 필요 없다.\n"
            "3. 코드 재사용: Box<String>, Box<Integer>, Box<Dog> 등을 동일한 Box 클래스로 처리한다.\n"
            "\n"
            "[유의 사항]\n"
            "• 기본형(int, double, char 등)은 제네릭에 직접 사용할 수 없으며, 래퍼 클래스(Integer, Double, Character 등)를 사용해야 한다(Box<int>는 오류, Box<Integer>는 정상).\n"
            "• 값의 저장·조회 시 자동 박싱/언박싱(int ↔ Integer 변환)이 발생하여 약간의 성능 오버헤드가 있다."
        ),
        usage="여러 타입에 재사용 가능한 자료구조/유틸을 만들 때, 형변환 없이 타입 안전을 얻고 싶을 때 쓴다.",
        cons="기본형(int 등)은 직접 못 쓰고 래퍼(Integer)로 박싱돼 약간의 오버헤드가 있다. 과하면 코드가 복잡해진다.",
        code=(
            "public class Main {\n"
            "    static class Box<T> {\n"
            "        private T value;\n"
            "        public void set(T v) { this.value = v; }\n"
            "        public T get() { return value; }\n"
            "    }\n"
            "\n"
            "    public static void main(String[] args) {\n"
            "        Box<String> s = new Box<>();\n"
            "        s.set(\"안녕\");\n"
            "        System.out.println(\"문자열 상자: \" + s.get());\n"
            "        Box<Integer> n = new Box<>();\n"
            "        n.set(42);\n"
            "        System.out.println(\"정수 상자: \" + n.get());\n"
            "    }\n"
            "}\n"
        ),
    ),

    Lesson(
        id="java-mid-05",
        lang="java", level="중급",
        title="클래스 · 상속 · 인터페이스",
        summary="extends · implements · 오버라이딩",
        explanation=(
            "[개요]\n"
            "클래스는 객체를 생성하기 위한 설계도이며, 하나의 클래스로 여러 객체를 생성할 수 있다.\n"
            "상속(extends)과 인터페이스(interface)는 객체지향의 핵심 재사용·추상화 수단이다.\n"
            "\n"
            "[핵심 개념]\n"
            "• 상속(extends): 부모 클래스의 필드와 메서드를 자식 클래스가 물려받는 것이다. 자식은 부모의 모든 멤버를 사용할 수 있으며, 필요한 부분만 재정의한다.\n"
            "• 인터페이스(interface): 구현 클래스가 반드시 제공해야 하는 메서드를 규정하는 약속이다. 예를 들어 Animal 인터페이스에 sound() 메서드가 있으면, Animal을 구현한 모든 클래스는 sound()를 반드시 구현해야 한다.\n"
            "\n"
            "[코드 분석]\n"
            "• interface Animal {                  → Animal 인터페이스를 선언한다. '동물은 소리를 낼 수 있어야 한다'는 규약이다.\n"
            "• String sound();                     → 구현부 없이 메서드 선언만 존재한다. 기능의 존재만 규정하며, 실제 동작은 각 구현 클래스가 정의한다.\n"
            "• static class Dog implements Animal { → Dog 클래스가 Animal 인터페이스를 구현한다. implements는 해당 규약을 준수하겠다는 선언이며, Dog는 sound()를 반드시 구현해야 한다(미구현 시 컴파일 오류).\n"
            "• public String sound() { return \"멍멍\"; }  → Dog의 sound()를 구현한다. 반환값은 \"멍멍\"이다.\n"
            "• static class Puppy extends Dog {    → Puppy 클래스가 Dog 클래스를 상속한다. Puppy는 Dog의 모든 멤버를 물려받되, 소리는 다르게 정의한다.\n"
            "• @Override                           → 부모(Dog)의 sound() 메서드를 재정의한다는 선언이다. 필수는 아니지만, 메서드 이름 오기 등 실수를 컴파일 단계에서 방지한다.\n"
            "• public String sound() { return \"왈왈\"; }  → Puppy의 sound()를 재정의한다. 반환값은 \"왈왈\"이다.\n"
            "• Animal a = new Dog();               → Dog 객체를 Animal 타입으로 참조한다. Dog가 Animal을 구현했으므로 가능하다.\n"
            "• Animal b = new Puppy();             → Puppy 객체도 Animal 타입으로 참조할 수 있다. Puppy는 Dog를 상속하고 Dog는 Animal을 구현했기 때문이다.\n"
            "• System.out.println(\"개: \" + a.sound());     → a는 Dog이므로 sound()가 \"멍멍\"을 반환한다.\n"
            "• System.out.println(\"강아지: \" + b.sound());  → b는 Puppy이므로 재정의된 sound()가 \"왈왈\"을 반환한다. 동일한 Animal 타입이지만 실제 동작이 달라지는 것이 다형성이다.\n"
            "\n"
            "[핵심 차이]\n"
            "• extends: 부모의 멤버를 물려받는다. 단일 상속만 가능하다.\n"
            "• implements: 규약을 준수한다. 다중 구현이 가능하다.\n"
            "\n"
            "[유의 사항]\n"
            "• Java는 클래스 상속(extends)을 하나만 허용한다(class A extends B, C는 오류).\n"
            "• 인터페이스는 여러 개 구현할 수 있다(class A implements B, C, D는 정상).\n"
            "• 상속 계층이 지나치게 깊어지면(Dog → Puppy → BabyPuppy → ...) 코드 파악이 어려워진다."
        ),
        usage="공통 동작을 부모로 묶어 코드 중복을 줄이고, 인터페이스로 구현을 교체 가능하게 설계할 때 쓴다.",
        cons="상속이 깊어지면 결합도가 높아져 유지보수가 어렵다. 단순 기능 공유는 상속보다 조합이 나을 때가 많다.",
        code=(
            "public class Main {\n"
            "    interface Animal {\n"
            "        String sound();\n"
            "    }\n"
            "    static class Dog implements Animal {\n"
            "        public String sound() { return \"멍멍\"; }\n"
            "    }\n"
            "    static class Puppy extends Dog {\n"
            "        @Override public String sound() { return \"왈왈\"; }\n"
            "    }\n"
            "\n"
            "    public static void main(String[] args) {\n"
            "        Animal a = new Dog();\n"
            "        Animal b = new Puppy();\n"
            "        System.out.println(\"개: \" + a.sound());\n"
            "        System.out.println(\"강아지: \" + b.sound());\n"
            "    }\n"
            "}\n"
        ),
    ),

    Lesson(
        id="java-mid-06",
        lang="java", level="중급",
        title="예외 처리(try/catch)",
        summary="try-catch-finally · 예외 던지기",
        explanation=(
            "[개요]\n"
            "예외(Exception)는 프로그램 실행 중 발생하는 예상치 못한 오류이다. try/catch/finally 구조로 이를 처리한다.\n"
            "• try: 오류 발생 가능성이 있는 코드를 실행한다.\n"
            "• catch: 예외가 발생하면 이를 잡아 처리한다.\n"
            "• finally: 성공·실패와 무관하게 항상 실행하며, 자원 정리 등에 사용한다.\n"
            "\n"
            "[핵심 개념]\n"
            "예외 처리가 없으면 오류 발생 시 프로그램이 즉시 종료되지만, 예외를 처리하면 오류를 잡아 안내 메시지를 제공하고 실행을 이어갈 수 있다.\n"
            "자주 발생하는 예외 종류는 다음과 같다.\n"
            "• ArrayIndexOutOfBoundsException → 배열 범위 초과(크기 3인데 arr[5] 접근)\n"
            "• NumberFormatException          → 문자를 숫자로 변환 실패(\"abc\"를 int로 변환 시도)\n"
            "• NullPointerException           → null인 변수를 사용할 때\n"
            "• ArithmeticException            → 0으로 나누기\n"
            "\n"
            "[코드 분석]\n"
            "• int[] arr = {10, 20, 30};       → 크기 3인 배열로, 유효 인덱스는 0, 1, 2이다.\n"
            "• try {                           → 이후 블록의 코드를 실행하되, 오류 발생 가능성을 감안한다는 의미이다.\n"
            "• System.out.println(arr[5]);     → 인덱스 5는 존재하지 않으므로 예외가 발생한다. 예외 발생 시 이후 try 블록 코드는 실행되지 않고 catch 블록으로 이동한다.\n"
            "• } catch (ArrayIndexOutOfBoundsException e) {  → 배열 범위 초과 예외를 처리한다. e는 예외 객체이며 e.getMessage()로 오류 메시지를 확인할 수 있다.\n"
            "• System.out.println(\"잘못된 인덱스 접근입니다\");  → 오류 발생 시 안내 메시지를 출력한다. 프로그램은 종료되지 않고 실행을 계속한다.\n"
            "• } finally {                    → try·catch 실행 여부와 무관하게 항상 실행되는 블록으로, 파일 닫기·DB 연결 종료 등 정리 작업에 사용한다.\n"
            "• System.out.println(\"처리 완료\");  → 성공·실패와 관계없이 항상 출력된다.\n"
            "• int x = Integer.parseInt(\"abc\");  → \"abc\"는 정수로 변환할 수 없으므로 NumberFormatException이 발생한다.\n"
            "• } catch (NumberFormatException e) {  → 문자→숫자 변환 실패 예외를 처리한다.\n"
            "• System.out.println(\"숫자가 아닙니다\");  → 변환 실패 시 안내 메시지를 출력한다.\n"
            "\n"
            "[실행 흐름]\n"
            "1) arr[5] 접근 시도 → 예외 발생\n"
            "2) catch 블록 이동 → '잘못된 인덱스 접근입니다' 출력\n"
            "3) finally 블록 실행 → '처리 완료' 출력\n"
            "4) 다음 try 블록 진행\n"
            "5) Integer.parseInt(\"abc\") 실패 → 예외 발생\n"
            "6) 두 번째 catch 블록 → '숫자가 아닙니다' 출력\n"
            "\n"
            "[유의 사항]\n"
            "• 빈 catch 블록은 사용하지 않는다. catch (Exception e) { }는 예외를 은폐하여 버그를 숨긴다.\n"
            "• catch 블록이 여러 개이면 위에서부터 순서대로 검사하므로, 더 구체적인 예외를 위에 배치해야 한다.\n"
            "• Exception 하나로 모든 예외를 잡을 수 있으나, 구체적인 오류 종류를 구분할 수 없다."
        ),
        usage="파일/네트워크/형변환처럼 실패 가능성이 있는 작업에서 프로그램이 죽지 않게 안전하게 처리할 때 쓴다.",
        cons="예외를 제어 흐름으로 남용하면 느리고 가독성이 나빠진다. 빈 catch 로 삼키면 버그를 숨기게 된다.",
        code=(
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        int[] arr = {10, 20, 30};\n"
            "        try {\n"
            "            System.out.println(\"값: \" + arr[5]);\n"
            "        } catch (ArrayIndexOutOfBoundsException e) {\n"
            "            System.out.println(\"잘못된 인덱스 접근입니다\");\n"
            "        } finally {\n"
            "            System.out.println(\"처리 완료\");\n"
            "        }\n"
            "        try {\n"
            "            int x = Integer.parseInt(\"abc\");\n"
            "            System.out.println(x);\n"
            "        } catch (NumberFormatException e) {\n"
            "            System.out.println(\"숫자가 아닙니다\");\n"
            "        }\n"
            "    }\n"
            "}\n"
        ),
    ),

    Lesson(
        id="java-mid-07",
        lang="java", level="중급",
        title="StringBuilder",
        summary="가변 문자열 · append · 빠른 문자열 조립",
        explanation=(
            "[개요]\n"
            "Java의 String은 불변(immutable)이므로, 한 번 생성된 String 객체의 내용은 변경되지 않는다. 따라서 String을 반복해서 이어붙이면 매번 새로운 객체가 생성되어 비효율적이다.\n"
            "StringBuilder는 가변 문자열 버퍼로, 내용을 덧붙이거나 삭제할 때 새 객체를 만들지 않고 동일한 버퍼를 재사용하며, 마지막에 toString()으로 완성된 String을 얻는다.\n"
            "\n"
            "[핵심 개념]\n"
            "• 반복문에서 String으로 1000번 이어붙이면 다수의 임시 객체가 생성되어 낭비가 크다.\n"
            "• 성능 비교(반복문에서 10,000번 이어붙이기):\n"
            "  - String 사용: 약 130ms (실전에서 TLE 유발 가능)\n"
            "  - StringBuilder 사용: 약 1ms (100배 이상 빠름)\n"
            "\n"
            "[코드 분석]\n"
            "• StringBuilder sb = new StringBuilder();  → 빈 문자열 버퍼를 생성한다.\n"
            "• for (int i = 1; i <= 5; i++) {           → 1부터 5까지 반복한다.\n"
            "• sb.append(i);                            → 버퍼에 i를 덧붙인다(i=1이면 \"1\", i=2이면 \"1-2\" 등).\n"
            "• if (i < 5) sb.append(\"-\");              → i가 5보다 작을 때만 구분자 \"-\"를 붙여, 마지막 값 뒤에는 구분자가 붙지 않게 한다. 진행 과정은 다음과 같다.\n"
            "    1 → \"1-\"\n"
            "    2 → \"1-2-\"\n"
            "    3 → \"1-2-3-\"\n"
            "    4 → \"1-2-3-4-\"\n"
            "    5 → \"1-2-3-4-5\" (마지막에는 구분자 없음)\n"
            "• System.out.println(\"조립 결과: \" + sb.toString());  → toString()으로 최종 String으로 변환한다. 결과는 \"1-2-3-4-5\"이다. println에 sb를 직접 전달해도 자동으로 toString()이 호출된다.\n"
            "• sb.append(\" 끝\");                        → 기존 내용 뒤에 \" 끝\"을 덧붙인다. 버퍼는 \"1-2-3-4-5 끝\"이 된다.\n"
            "• System.out.println(\"길이: \" + sb.length());  → 현재 버퍼의 문자 수를 반환한다. \"1-2-3-4-5 끝\"은 12글자이다.\n"
            "• System.out.println(\"뒤집기: \" + sb.reverse());  → 버퍼 내용을 뒤집는다. \"1-2-3-4-5 끝\" → \"끝 5-4-3-2-1\". 회문(팰린드롬) 판별에 활용된다.\n"
            "\n"
            "[주요 메서드]\n"
            "• sb.append(x)    → 뒤에 붙이기(x는 String, int, char, boolean 등 가능)\n"
            "• sb.insert(i, x) → i번 위치에 x 삽입\n"
            "• sb.delete(s, e) → s번부터 e번 전까지 삭제\n"
            "• sb.reverse()    → 전체 뒤집기\n"
            "• sb.length()     → 현재 길이\n"
            "• sb.charAt(i)    → i번 위치 문자 조회\n"
            "• sb.toString()   → 최종 String으로 변환\n"
            "\n"
            "[유의 사항]\n"
            "• 멀티스레드 환경에서 여러 스레드가 동일한 StringBuilder를 동시에 사용하면 데이터가 손상될 수 있다. 이 경우 동기화를 지원하는 StringBuffer를 사용한다. 코딩테스트는 대부분 단일 스레드이므로 StringBuilder로 충분하다.\n"
            "• new StringBuilder(1000)처럼 초기 용량을 지정하면 메모리 재할당이 줄어 성능이 향상된다."
        ),
        usage="반복문에서 문자열을 많이 이어 붙일 때, 대량 출력을 모아 한 번에 출력할 때 필수로 쓴다.",
        cons="단발성 짧은 연결에는 오히려 번거롭다. 멀티스레드 공유 시에는 StringBuffer 가 안전하다.",
        code=(
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        StringBuilder sb = new StringBuilder();\n"
            "        for (int i = 1; i <= 5; i++) {\n"
            "            sb.append(i);\n"
            "            if (i < 5) sb.append(\"-\");\n"
            "        }\n"
            "        System.out.println(\"조립 결과: \" + sb.toString());\n"
            "        sb.append(\" 끝\");\n"
            "        System.out.println(\"길이: \" + sb.length());\n"
            "        System.out.println(\"뒤집기: \" + sb.reverse());\n"
            "    }\n"
            "}\n"
        ),
    ),

    Lesson(
        id="java-mid-08",
        lang="java", level="중급",
        title="Comparator와 정렬",
        summary="Collections.sort · Arrays.sort · 람다 비교자",
        explanation=(
            "[개요]\n"
            "정렬은 데이터를 특정 기준에 따라 순서대로 나열하는 연산이다. 기본 오름차순 외에 사용자 정의 기준으로 정렬하려면 Comparator를 사용한다.\n"
            "예를 들어 기본 정렬은 제목 가나다순, 페이지 수 내림차순은 Comparator 사용, 두께가 같으면 제목순으로 하는 복합 기준은 Comparator 체이닝으로 구현한다.\n"
            "\n"
            "[핵심 개념]\n"
            "Comparator는 두 값 a, b를 받아 정수를 반환하며, 반환값의 부호로 순서를 결정한다.\n"
            "• 반환값이 음수: a가 b보다 앞에 온다(a < b)\n"
            "• 반환값이 0: a와 b의 순서는 무관하다(a == b)\n"
            "• 반환값이 양수: b가 a보다 앞에 온다(a > b)\n"
            "따라서 오름차순은 (a, b) -> a - b, 내림차순은 (a, b) -> b - a로 표현한다.\n"
            "\n"
            "[코드 분석]\n"
            "• Integer[] nums = {5, 2, 8, 1};                    → 정수 배열이다. Comparator는 기본형(int)을 다루지 못하므로 int[]가 아닌 래퍼 타입 Integer[]를 사용한다.\n"
            "• Arrays.sort(nums, (a, b) -> b - a);              → nums 배열을 람다 (a, b) -> b - a 기준으로 정렬한다. a=5, b=8이면 b-a=3(양수)이므로 8이 앞으로, a=8, b=5이면 b-a=-3(음수)이므로 8이 앞으로 이동하여 내림차순이 된다. 결과는 [8, 5, 2, 1]이다.\n"
            "• System.out.println(\"내림차순: \" + Arrays.toString(nums));  → 배열을 [8, 5, 2, 1] 형태로 출력한다. 배열은 println에 직접 넣으면 [I@1b6d3586 같은 형태로 출력되므로 Arrays.toString()을 사용한다.\n"
            "• List<String> words = new ArrayList<>(Arrays.asList(\"가나다\", \"가\", \"가나\"));  → 문자열 리스트를 생성한다. Arrays.asList로 배열을 리스트로 변환하고, new ArrayList<>()로 감싸야 크기 변경이 가능하다.\n"
            "• Collections.sort(words, Comparator.comparingInt(String::length));  → 단어를 길이(글자 수) 오름차순으로 정렬한다. Comparator.comparingInt(String::length)는 각 단어의 length() 값을 기준으로 비교하며, \"가\"(1글자), \"가나\"(2글자), \"가나다\"(3글자) 순으로 정렬된다.\n"
            "• System.out.println(\"길이순: \" + words);           → [가, 가나, 가나다]가 출력된다.\n"
            "\n"
            "[자주 쓰는 Comparator 패턴]\n"
            "• 오름차순(기본):\n"
            "  Arrays.sort(nums);\n"
            "  Collections.sort(list);\n"
            "• 내림차순:\n"
            "  Arrays.sort(nums, (a, b) -> b - a);\n"
            "  Collections.sort(list, Collections.reverseOrder());\n"
            "• 문자열 길이 오름차순:\n"
            "  Collections.sort(list, Comparator.comparingInt(String::length));\n"
            "• 점수 내림차순(2차원 배열):\n"
            "  Arrays.sort(students, (a, b) -> b[1] - a[1]);\n"
            "• 복합 정렬(점수 내림차순, 같으면 이름 오름차순):\n"
            "  list.sort(Comparator.comparingInt(Student::getScore).reversed()\n"
            "      .thenComparing(Student::getName));\n"
            "\n"
            "[유의 사항]\n"
            "• (a, b) -> a - b 패턴은 오버플로우 위험이 있다. a = Integer.MIN_VALUE, b = 1이면 a - b가 오버플로우된다. 안전한 방법은 Integer.compare(a, b) 또는 (a, b) -> Integer.compare(a, b)를 사용하는 것이다.\n"
            "• int[](기본형 배열)에는 Comparator를 직접 사용할 수 없으므로 Integer[]로 변환하거나 다른 방법을 사용한다.\n"
            "• 비교자 로직이 일관성을 잃으면(a>b인데 b>a로도 판단되는 등) 예외가 발생하거나 정렬이 잘못될 수 있다."
        ),
        usage="문자열 길이순, 점수 내림차순 등 사용자 정의 기준으로 정렬할 때 쓴다.",
        cons="비교자 로직이 일관성(대소 관계 모순)을 깨면 예외가 나거나 잘못 정렬된다. 복잡하면 가독성이 떨어진다.",
        code=(
            "import java.util.*;\n"
            "\n"
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        Integer[] nums = {5, 2, 8, 1};\n"
            "        Arrays.sort(nums, (a, b) -> b - a);   // 내림차순\n"
            "        System.out.println(\"내림차순: \" + Arrays.toString(nums));\n"
            "\n"
            "        List<String> words = new ArrayList<>(Arrays.asList(\"가나다\", \"가\", \"가나\"));\n"
            "        Collections.sort(words, Comparator.comparingInt(String::length));\n"
            "        System.out.println(\"길이순: \" + words);\n"
            "    }\n"
            "}\n"
        ),
    ),
]
