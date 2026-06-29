"""Java 기초 문법 (스타터 — 8개 항목)."""

from engine.models import Lesson

LESSONS = [

    Lesson(
        id="java-basic-01",
        lang="java", level="기초",
        title="변수와 기본 타입",
        summary="기본형(int/long/double/boolean/char) · 참조형 · 선언과 초기화",
        explanation=(
            "자바는 정적 타입 언어라 변수를 쓰기 전에 반드시 타입을 선언해야 한다.\n"
            "기본형(primitive)은 값 자체를 저장한다: 정수 int(4바이트)·long(8바이트),\n"
            "실수 double(8바이트)·float(4바이트), 참/거짓 boolean, 문자 하나 char 등이 있다.\n"
            "정수 리터럴이 int 범위를 넘으면 뒤에 L 을 붙여 long 으로 적는다(예: 10000000000L).\n"
            "실수 리터럴은 기본이 double 이며 float 에는 f 를 붙인다(예: 3.14f).\n"
            "참조형(String, 배열, 객체)은 실제 데이터의 주소(참조)를 담는다.\n"
            "지역 변수는 자동 초기화되지 않으므로 사용 전에 값을 반드시 대입해야 한다."
        ),
        usage="모든 데이터 저장의 출발점. 큰 수 계산엔 long, 정밀 소수엔 double 을 쓴다.",
        cons="기본형은 null 을 가질 수 없고, int 끼리 큰 수를 곱하면 오버플로가 날 수 있어 long 으로 승격해야 한다.",
        code=(
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        int age = 25;            // 정수\n"
            "        long big = 10000000000L; // int 범위를 넘는 큰 정수\n"
            "        double pi = 3.14;        // 실수(기본 double)\n"
            "        boolean ok = true;       // 참/거짓\n"
            "        char grade = 'A';        // 문자 하나\n"
            "        String name = \"홍길동\";   // 참조형 문자열\n"
            "\n"
            "        System.out.println(\"이름: \" + name + \", 나이: \" + age);\n"
            "        System.out.println(\"큰 수: \" + big);\n"
            "        System.out.println(\"원주율: \" + pi + \", 합격: \" + ok + \", 학점: \" + grade);\n"
            "\n"
            "        int max = Integer.MAX_VALUE; // int 가 담을 수 있는 최댓값\n"
            "        System.out.println(\"int 최댓값: \" + max);\n"
            "    }\n"
            "}\n"
        ),
    ),

    Lesson(
        id="java-basic-02",
        lang="java", level="기초",
        title="표준 출력과 형변환",
        summary="print/println/printf · 캐스팅 · parse · String.valueOf",
        explanation=(
            "표준 출력은 System.out 으로 한다. print 는 줄바꿈 없이, println 은 줄바꿈을 붙여 출력한다.\n"
            "printf 는 서식 지정 출력으로 %d(정수), %f(실수), %s(문자열), %n(줄바꿈)을 쓴다.\n"
            "형변환에는 두 종류가 있다.\n"
            "1) 자동 형변환: 작은 타입 → 큰 타입(int → double)은 그냥 대입하면 된다.\n"
            "2) 명시적 캐스팅: 큰 타입 → 작은 타입은 (int) 처럼 괄호로 강제하며 소수점은 버려진다.\n"
            "문자열↔숫자 변환은 Integer.parseInt(\"123\"), Double.parseDouble(\"3.14\") 로 하고,\n"
            "반대로 숫자→문자열은 String.valueOf(x) 또는 \"\" + x 로 만든다."
        ),
        usage="결과를 보기 좋게 찍을 때 printf, 입력 문자열을 숫자로 바꿀 때 parseInt 가 핵심.",
        cons="double → int 캐스팅은 반올림이 아니라 '버림'이라 의도와 다를 수 있다. parseInt 는 숫자가 아니면 예외를 던진다.",
        code=(
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        int a = 7, b = 2;\n"
            "        System.out.println(a + \" / \" + b + \" = \" + (a / b));   // 정수 나눗셈 → 3\n"
            "\n"
            "        double d = (double) a / b;   // 한쪽을 double 로 캐스팅 → 3.5\n"
            "        System.out.printf(\"실수 나눗셈: %.2f%n\", d);\n"
            "\n"
            "        double pi = 3.99;\n"
            "        int cut = (int) pi;          // 캐스팅은 버림 → 3\n"
            "        System.out.println(\"버림: \" + cut);\n"
            "\n"
            "        int parsed = Integer.parseInt(\"123\");  // 문자열 → 정수\n"
            "        String text = String.valueOf(456);      // 정수 → 문자열\n"
            "        System.out.println(\"parse 결과: \" + (parsed + 1));\n"
            "        System.out.println(\"valueOf 결과 길이: \" + text.length());\n"
            "    }\n"
            "}\n"
        ),
    ),

    Lesson(
        id="java-basic-03",
        lang="java", level="기초",
        title="조건문과 반복문",
        summary="if/else if/else · switch · for/while · break/continue",
        explanation=(
            "조건문은 if / else if / else 로 분기한다. 조건식은 반드시 boolean 이어야 한다.\n"
            "값이 정해진 여러 갈래는 switch 로 깔끔하게 쓸 수 있고, 각 case 끝에 break 가 없으면\n"
            "다음 case 로 흘러내려가니(fall-through) 주의한다.\n"
            "반복문은 세 가지가 있다.\n"
            "1) for: 초기화·조건·증감을 한 줄에 모아 횟수가 정해진 반복에 쓴다.\n"
            "2) while: 조건이 참인 동안 반복한다.\n"
            "3) do-while: 본문을 최소 한 번 실행한 뒤 조건을 검사한다.\n"
            "break 는 반복을 즉시 끝내고, continue 는 이번 회차만 건너뛰고 다음으로 넘어간다."
        ),
        usage="모든 흐름 제어의 기본. 횟수가 정해지면 for, 조건이 끝을 정하면 while 을 택한다.",
        cons="switch 의 break 누락 버그가 흔하다. 무한 while 은 종료 조건을 빠뜨리면 멈추지 않는다.",
        code=(
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        int score = 82;\n"
            "        if (score >= 90) System.out.println(\"A\");\n"
            "        else if (score >= 80) System.out.println(\"B\");\n"
            "        else System.out.println(\"C\");\n"
            "\n"
            "        int day = 3;\n"
            "        switch (day) {\n"
            "            case 1: System.out.println(\"월\"); break;\n"
            "            case 3: System.out.println(\"수\"); break;\n"
            "            default: System.out.println(\"기타\");\n"
            "        }\n"
            "\n"
            "        int sum = 0;\n"
            "        for (int i = 1; i <= 10; i++) {\n"
            "            if (i % 2 == 1) continue; // 홀수는 건너뜀\n"
            "            sum += i;                 // 짝수만 더함\n"
            "        }\n"
            "        System.out.println(\"1~10 짝수합: \" + sum); // 30\n"
            "\n"
            "        int n = 5, fact = 1;\n"
            "        while (n > 1) { fact *= n; n--; }\n"
            "        System.out.println(\"5! = \" + fact);       // 120\n"
            "    }\n"
            "}\n"
        ),
    ),

    Lesson(
        id="java-basic-04",
        lang="java", level="기초",
        title="배열(1차원/2차원)",
        summary="고정 길이 · new · length · 향상된 for · 2차원 배열",
        explanation=(
            "배열은 같은 타입의 값을 연속으로 모아 둔 고정 길이 자료구조다.\n"
            "선언과 생성은 int[] a = new int[5]; 처럼 하며, 생성 시 0(숫자)·false·null 로 자동 초기화된다.\n"
            "초기값을 바로 줄 때는 int[] a = {10, 20, 30}; 형태를 쓴다.\n"
            "인덱스는 0부터 시작하고, 길이는 a.length 로 얻는다(메서드가 아니라 필드라 괄호가 없다).\n"
            "원소만 순회하면 되는 경우 향상된 for( for (int x : a) )가 간결하다.\n"
            "2차원 배열은 '배열의 배열'이다. int[][] g = new int[2][3]; 은 2행 3열을 만들고\n"
            "g[i].length 로 각 행의 길이를 구한다. 행마다 길이가 다른 비정형 배열도 가능하다."
        ),
        usage="크기가 고정된 데이터, 격자/표 형태 데이터 처리에 적합. 인접 메모리라 접근이 빠르다.",
        cons="길이를 만든 뒤 바꿀 수 없다(크기 변경이 필요하면 ArrayList). 범위를 벗어나면 예외가 난다.",
        code=(
            "import java.util.Arrays;\n"
            "\n"
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        int[] a = {5, 2, 9, 1};\n"
            "        int sum = 0;\n"
            "        for (int x : a) sum += x;           // 향상된 for\n"
            "        System.out.println(\"길이: \" + a.length + \", 합: \" + sum);\n"
            "\n"
            "        Arrays.sort(a);                     // 오름차순 정렬\n"
            "        System.out.println(\"정렬: \" + Arrays.toString(a));\n"
            "\n"
            "        int[][] grid = {                    // 2x3 2차원 배열\n"
            "            {1, 2, 3},\n"
            "            {4, 5, 6}\n"
            "        };\n"
            "        for (int i = 0; i < grid.length; i++) {\n"
            "            for (int j = 0; j < grid[i].length; j++) {\n"
            "                System.out.print(grid[i][j] + \" \");\n"
            "            }\n"
            "            System.out.println();\n"
            "        }\n"
            "    }\n"
            "}\n"
        ),
    ),

    Lesson(
        id="java-basic-05",
        lang="java", level="기초",
        title="문자열(String)과 주요 메서드",
        summary="불변 · length/charAt/substring/indexOf · split · StringBuilder",
        explanation=(
            "String 은 문자들의 시퀀스이며 한 번 만들어지면 내용을 바꿀 수 없다(불변, immutable).\n"
            "그래서 + 로 이어 붙일 때마다 새 객체가 생긴다.\n"
            "자주 쓰는 메서드:\n"
            "- length(): 문자 개수\n"
            "- charAt(i): i번째 문자\n"
            "- substring(a, b): a부터 b 직전까지 잘라낸 부분 문자열\n"
            "- indexOf(s): s가 처음 나오는 위치(없으면 -1)\n"
            "- toUpperCase()/toLowerCase(): 대소문자 변환\n"
            "- split(정규식): 구분자로 쪼개 배열로 반환\n"
            "- equals(other): 내용 비교(== 는 참조 비교라 내용 비교엔 쓰면 안 된다)\n"
            "반복문에서 문자열을 많이 이어 붙일 때는 가변 버퍼인 StringBuilder 를 쓰면 훨씬 빠르다."
        ),
        usage="텍스트 파싱·가공의 기본. 입력 한 줄을 split 으로 토큰화하는 패턴이 매우 흔하다.",
        cons="불변이라 루프 안 + 연결은 비효율적이다(StringBuilder 권장). 내용 비교는 반드시 equals 로 한다.",
        code=(
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        String s = \"Hello, Java\";\n"
            "        System.out.println(\"길이: \" + s.length());\n"
            "        System.out.println(\"첫 글자: \" + s.charAt(0));\n"
            "        System.out.println(\"부분: \" + s.substring(7));      // Java\n"
            "        System.out.println(\"위치: \" + s.indexOf(\"Java\"));   // 7\n"
            "        System.out.println(\"대문자: \" + s.toUpperCase());\n"
            "\n"
            "        String line = \"3 5 7\";\n"
            "        String[] tokens = line.split(\" \");\n"
            "        int total = 0;\n"
            "        for (String t : tokens) total += Integer.parseInt(t);\n"
            "        System.out.println(\"토큰 합: \" + total);             // 15\n"
            "\n"
            "        StringBuilder sb = new StringBuilder();\n"
            "        for (int i = 1; i <= 3; i++) sb.append(i).append('-');\n"
            "        System.out.println(\"빌더: \" + sb.toString());        // 1-2-3-\n"
            "\n"
            "        System.out.println(\"내용 비교: \" + \"abc\".equals(\"abc\"));\n"
            "    }\n"
            "}\n"
        ),
    ),

    Lesson(
        id="java-basic-06",
        lang="java", level="기초",
        title="입력(Scanner vs BufferedReader)",
        summary="Scanner의 편의성 · BufferedReader의 속도 · 개념 비교",
        explanation=(
            "자바에서 표준 입력은 보통 두 가지 방법으로 읽는다.\n"
            "1) Scanner: new Scanner(System.in) 으로 만들고 nextInt(), next(), nextLine() 으로\n"
            "   타입별로 편하게 읽는다. 코드가 짧고 직관적이지만 내부 처리가 무거워 느린 편이다.\n"
            "2) BufferedReader: new BufferedReader(new InputStreamReader(System.in)) 로 만들고\n"
            "   readLine() 으로 한 줄을 통째로 읽는다. 문자열로만 주므로 숫자는 직접 parseInt 하거나\n"
            "   split(\" \") / StringTokenizer 로 토큰을 나눠야 한다. 버퍼를 써서 입력이 많을 때 훨씬 빠르다.\n"
            "정리: 입력량이 적고 간편함이 우선이면 Scanner, 대량 입력으로 속도가 중요하면 BufferedReader.\n"
            "아래 데모는 표준입력 대신 고정 문자열을 같은 방식(split + parse)으로 처리해 흐름만 보여준다."
        ),
        usage="코딩테스트에서 입력이 크면 BufferedReader 가 사실상 표준. 작은 입력엔 Scanner 가 편하다.",
        cons="Scanner 는 느리고 nextInt 와 nextLine 을 섞으면 개행 처리 함정이 있다. BufferedReader 는 IOException 처리와 파싱을 직접 해야 한다.",
        code=(
            "import java.io.BufferedReader;\n"
            "import java.io.IOException;\n"
            "import java.io.StringReader;\n"
            "import java.util.StringTokenizer;\n"
            "\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        // 표준입력 대신 고정 문자열로 데모(System.in 을 흉내 냄)\n"
            "        String input = \"3\\n10 20 30\\n\";\n"
            "        BufferedReader br = new BufferedReader(new StringReader(input));\n"
            "\n"
            "        int n = Integer.parseInt(br.readLine().trim()); // 첫 줄: 개수\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int sum = 0;\n"
            "        for (int i = 0; i < n; i++) {\n"
            "            sum += Integer.parseInt(st.nextToken());    // 토큰별 정수 파싱\n"
            "        }\n"
            "        System.out.println(\"개수: \" + n);\n"
            "        System.out.println(\"합계: \" + sum);            // 60\n"
            "\n"
            "        // 참고: 실제로는 new BufferedReader(new InputStreamReader(System.in)) 로 만든다.\n"
            "    }\n"
            "}\n"
        ),
    ),

    Lesson(
        id="java-basic-07",
        lang="java", level="기초",
        title="연산자와 형 승격",
        summary="산술/비교/논리/대입 · 정수 나눗셈 · 자동 타입 승격 규칙",
        explanation=(
            "연산자는 크게 네 부류다.\n"
            "- 산술: + - * / % (나머지). 정수끼리의 / 는 몫만 남기는 정수 나눗셈이다.\n"
            "- 비교: == != < <= > >= → 결과는 boolean.\n"
            "- 논리: && (그리고), || (또는), ! (부정). &&/|| 는 단축 평가(short-circuit)를 한다.\n"
            "- 대입: = 와 += -= *= /= %= 같은 복합 대입.\n"
            "형 승격(type promotion): 서로 다른 타입을 연산하면 작은 타입이 큰 타입으로 자동 변환된다.\n"
            "규칙은 byte/short/char → int → long → float → double 방향이다.\n"
            "그래서 int / int 는 int 이지만, int 와 double 을 섞으면 결과가 double 이 된다.\n"
            "또한 큰 int 끼리 곱하면 int 범위를 넘어 오버플로가 나므로, 한쪽을 long 으로 만들어 계산해야 한다."
        ),
        usage="수치 계산 전반의 기본. 평균·확률처럼 소수가 필요한 계산에선 형 승격을 의식해야 한다.",
        cons="정수 나눗셈으로 소수점이 사라지는 실수가 잦다. int 오버플로는 예외 없이 조용히 틀린 값을 낸다.",
        code=(
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        int a = 7, b = 3;\n"
            "        System.out.println(\"몫: \" + (a / b) + \", 나머지: \" + (a % b)); // 2, 1\n"
            "\n"
            "        double avg = (a + b) / 2.0;   // 2.0 때문에 double 로 승격\n"
            "        System.out.println(\"평균: \" + avg);                 // 5.0\n"
            "\n"
            "        boolean cond = (a > 5) && (b < 5);\n"
            "        System.out.println(\"논리 결과: \" + cond);            // true\n"
            "\n"
            "        int big = 100000;\n"
            "        long overflowSafe = (long) big * big;  // long 으로 승격해 오버플로 방지\n"
            "        System.out.println(\"안전한 곱: \" + overflowSafe);   // 10000000000\n"
            "        System.out.println(\"위험한 곱(int): \" + (big * big)); // 오버플로된 값\n"
            "    }\n"
            "}\n"
        ),
    ),

    Lesson(
        id="java-basic-08",
        lang="java", level="기초",
        title="메서드 정의와 호출",
        summary="static 메서드 · 매개변수/반환값 · 오버로딩 · 중첩 클래스",
        explanation=(
            "메서드는 기능을 묶어 이름 붙인 코드 블록으로, 입력(매개변수)을 받아 결과(반환값)를 돌려준다.\n"
            "형식은 [접근제어] static 반환타입 이름(매개변수목록) { ... return 값; } 이다.\n"
            "반환값이 없으면 반환타입을 void 로 쓴다.\n"
            "main 처럼 객체 없이 호출하는 메서드에는 static 을 붙이며, 같은 클래스의 다른 static 메서드를\n"
            "이름만으로 바로 호출할 수 있다.\n"
            "오버로딩(overloading): 이름이 같아도 매개변수의 개수나 타입이 다르면 별개의 메서드로 공존한다.\n"
            "자바에서 메서드는 클래스 안에만 존재한다. 여러 클래스가 필요하면 Main 안에 static 중첩\n"
            "클래스를 두어 정리할 수 있다(아래 Calculator 예시)."
        ),
        usage="중복 코드를 함수로 묶어 재사용한다. 오버로딩으로 비슷한 기능을 같은 이름으로 제공할 수 있다.",
        cons="static 메서드는 인스턴스 상태(필드)에 접근할 수 없다. 매개변수가 많아지면 호출 의미가 흐려진다.",
        code=(
            "public class Main {\n"
            "    // 정수 두 개의 합을 반환하는 static 메서드\n"
            "    static int add(int a, int b) {\n"
            "        return a + b;\n"
            "    }\n"
            "\n"
            "    // 오버로딩: 같은 이름, 매개변수 타입이 다름(실수 버전)\n"
            "    static double add(double a, double b) {\n"
            "        return a + b;\n"
            "    }\n"
            "\n"
            "    // 반환값이 없는 메서드(void)\n"
            "    static void greet(String name) {\n"
            "        System.out.println(name + \"님, 환영합니다.\");\n"
            "    }\n"
            "\n"
            "    // 여러 클래스가 필요하면 static 중첩 클래스로 정리\n"
            "    static class Calculator {\n"
            "        int multiply(int a, int b) { return a * b; }\n"
            "    }\n"
            "\n"
            "    public static void main(String[] args) {\n"
            "        System.out.println(\"정수 합: \" + add(3, 4));        // 7\n"
            "        System.out.println(\"실수 합: \" + add(1.5, 2.5));    // 4.0\n"
            "        greet(\"홍길동\");\n"
            "\n"
            "        Calculator calc = new Calculator();\n"
            "        System.out.println(\"곱: \" + calc.multiply(6, 7));   // 42\n"
            "    }\n"
            "}\n"
        ),
    ),
]
