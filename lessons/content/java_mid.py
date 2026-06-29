"""Java 중급 문법 (컬렉션 · 제네릭 · 객체지향 · 예외 · 문자열 · 정렬)."""

from engine.models import Lesson

LESSONS = [

    Lesson(
        id="java-mid-01",
        lang="java", level="중급",
        title="List와 ArrayList",
        summary="가변 배열 · add/get/size · for-each",
        explanation=(
            "List 는 순서가 있는 컬렉션 인터페이스이고, 가장 많이 쓰는 구현체가 ArrayList 다.\n"
            "List<String> list = new ArrayList<>(); 처럼 인터페이스 타입으로 선언하는 것이 관례다.\n"
            "add 로 추가, get(i) 로 조회, size() 로 크기를 얻고 for-each 로 순회한다."
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
            "Map 은 키-값 쌍을 저장하는 자료구조이며 HashMap 이 대표 구현체다(평균 O(1) 조회).\n"
            "put(키, 값) 으로 넣고 get(키) 로 꺼낸다. 없는 키를 get 하면 null 이 반환된다.\n"
            "getOrDefault(키, 기본값) 을 쓰면 키가 없을 때 기본값을 돌려줘 빈도수 세기에 편리하다."
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
            "Set 은 중복을 허용하지 않는 컬렉션이고 HashSet 이 대표 구현체다.\n"
            "add 로 추가하되 이미 있는 값은 무시되며, contains(값) 으로 포함 여부를 빠르게 확인한다.\n"
            "리스트의 중복을 제거하려면 new HashSet<>(list) 처럼 생성자에 넘기면 된다."
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
            "제네릭은 클래스나 메서드가 다룰 타입을 <T> 같은 타입 매개변수로 일반화하는 기능이다.\n"
            "컬렉션의 List<String> 처럼 어떤 타입을 담을지 컴파일 시점에 못 박아 형변환 실수를 막는다.\n"
            "직접 만들 때는 class Box<T> 처럼 선언하고 T 를 필드/메서드 타입으로 사용한다."
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
            "클래스는 데이터(필드)와 동작(메서드)을 묶은 설계도다. extends 로 부모 클래스를 상속한다.\n"
            "인터페이스는 '무엇을 할 수 있는가'를 규정한 약속이며 implements 로 구현한다.\n"
            "자식은 부모/인터페이스의 메서드를 @Override 로 재정의해 다형성을 구현한다."
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
            "실행 중 발생할 수 있는 오류를 예외로 다룬다. 위험한 코드를 try 블록에 넣는다.\n"
            "예외가 나면 catch 블록이 받아 처리하고, finally 블록은 성공/실패와 무관하게 항상 실행된다.\n"
            "여러 예외는 catch 를 여러 개 두거나 상위 타입(Exception)으로 한 번에 받을 수 있다."
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
            "String 은 불변(immutable)이라 + 로 이어 붙일 때마다 새 객체가 만들어져 반복이 많으면 느리다.\n"
            "StringBuilder 는 내부 버퍼를 가진 가변 문자열로 append 로 효율적으로 이어 붙인다.\n"
            "조립이 끝나면 toString() 으로 최종 String 을 얻는다. insert/reverse 등도 제공한다."
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
            "기본 정렬은 Collections.sort(list) / Arrays.sort(arr) 로 오름차순 정렬한다.\n"
            "기준을 바꾸려면 Comparator 를 넘긴다. 람다 (a, b) -> ... 로 간단히 비교자를 만든다.\n"
            "Comparator.comparing / reverseOrder 등으로 정렬 기준을 선언적으로 조합할 수 있다."
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
