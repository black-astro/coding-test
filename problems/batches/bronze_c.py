"""브론즈 추가 배치 C — 문자열 기초 / 리스트 기초 / 간단 수학 / 아스키 코드.

bronze-36 ~ bronze-50 (15문제). base 및 다른 배치와 주제 중복 없음.
"""

from engine.models import Problem

RANK = "Bronze"

PROBLEMS = [

    Problem(
        id="bronze-36",
        rank="Bronze",
        title="모두 대문자로",
        style="프로그래머스",
        topic="문자열",
        type="func",
        func_name="solution",
        description="영어 알파벳으로 이루어진 문자열 s가 주어집니다. s에 포함된 모든 영어 소문자를 대문자로 바꾼 문자열을 반환하는 함수 solution을 완성하세요.",
        input_desc="s : str (1 ≤ len(s) ≤ 1000)",
        output_desc="모든 문자가 대문자로 바뀐 문자열",
        examples=[
            {"args": ["hello"], "output": "HELLO"},
            {"args": ["Python3"], "output": "PYTHON3"},
        ],
        hints=[
            "문자열을 한 글자씩 바꿀 수도 있지만, 문자열에는 통째로 대소문자를 바꾸는 편리한 기능이 있습니다.",
            "파이썬 문자열 메서드 중 upper() 를 사용하면 됩니다.",
            "return s.upper() 한 줄이면 끝납니다.",
        ],
        testcases=[
            {"args": ["hello"], "expected": "HELLO"},
            {"args": ["Python3"], "expected": "PYTHON3"},
            {"args": ["ABC"], "expected": "ABC"},
            {"args": ["a"], "expected": "A"},
            {"args": ["mix123Case"], "expected": "MIX123CASE"},
        ],
        reference_py=(
            "def solution(s):\n"
            "    return s.upper()\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public String solution(String s) {\n"
            "        return s.toUpperCase();\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 문자열 s의 모든 문자를 대문자로 바꿔 반환하세요.\n"
            "def solution(s):\n"
            "    answer = \"\"\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="bronze-37",
        rank="Bronze",
        title="특정 문자 개수 세기",
        style="백준",
        topic="문자열",
        type="stdin",
        description="문자열 S와 문자 C가 주어졌을 때, 문자열 S 안에 문자 C가 몇 번 나타나는지 세어 출력하시오.",
        input_desc="첫째 줄에 문자열 S(공백 없는 1 ≤ 길이 ≤ 1000), 둘째 줄에 찾을 문자 C가 주어진다.",
        output_desc="S에 포함된 C의 개수를 출력한다.",
        examples=[
            {"input": "banana\na\n", "output": "3\n"},
            {"input": "mississippi\ns\n", "output": "4\n"},
        ],
        hints=[
            "문자열을 처음부터 끝까지 보면서 C와 같은 글자를 만날 때마다 세면 됩니다.",
            "직접 반복하지 않아도, 문자열 메서드 count() 가 특정 부분 문자열의 개수를 바로 알려줍니다.",
            "s = input(); c = input() 으로 받은 뒤 print(s.count(c)) 하면 됩니다.",
        ],
        testcases=[
            {"input": "banana\na\n", "output": "3\n"},
            {"input": "mississippi\ns\n", "output": "4\n"},
            {"input": "abc\nz\n", "output": "0\n"},
            {"input": "aaaa\na\n", "output": "4\n"},
            {"input": "x\nx\n", "output": "1\n"},
        ],
        reference_py=(
            "s = input()\n"
            "c = input()\n"
            "print(s.count(c))\n"
        ),
        reference_java=(
            "import java.util.Scanner;\n"
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        Scanner sc = new Scanner(System.in);\n"
            "        String s = sc.next();\n"
            "        char c = sc.next().charAt(0);\n"
            "        int cnt = 0;\n"
            "        for (int i = 0; i < s.length(); i++)\n"
            "            if (s.charAt(i) == c) cnt++;\n"
            "        System.out.println(cnt);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 문자열 S에서 문자 C의 개수를 세어 출력하세요.\n"
            "s = input()\n"
            "c = input()\n"
            "# print(...)\n"
        ),
    ),

    Problem(
        id="bronze-38",
        rank="Bronze",
        title="모음의 개수",
        style="대기업",
        topic="문자열",
        type="func",
        func_name="solution",
        description="영어 소문자로 이루어진 문자열 s가 주어집니다. s에 포함된 모음(a, e, i, o, u)의 총 개수를 반환하는 함수 solution을 완성하세요.",
        input_desc="s : str (1 ≤ len(s) ≤ 1000, 영어 소문자만)",
        output_desc="모음의 개수 (int)",
        examples=[
            {"args": ["apple"], "output": 2},
            {"args": ["rhythm"], "output": 0},
        ],
        hints=[
            "문자열을 한 글자씩 확인하면서, 그 글자가 모음인지 판단하면 됩니다.",
            "모음들을 'aeiou' 같은 문자열에 모아두고, 각 글자가 그 안에 들어있는지(in) 검사하세요.",
            "return sum(1 for ch in s if ch in 'aeiou') 처럼 모음일 때만 더하면 됩니다.",
        ],
        testcases=[
            {"args": ["apple"], "expected": 2},
            {"args": ["rhythm"], "expected": 0},
            {"args": ["aeiou"], "expected": 5},
            {"args": ["banana"], "expected": 3},
            {"args": ["b"], "expected": 0},
        ],
        reference_py=(
            "def solution(s):\n"
            "    return sum(1 for ch in s if ch in 'aeiou')\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(String s) {\n"
            "        int cnt = 0;\n"
            "        for (int i = 0; i < s.length(); i++)\n"
            "            if (\"aeiou\".indexOf(s.charAt(i)) >= 0) cnt++;\n"
            "        return cnt;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 문자열 s에 들어있는 모음(a,e,i,o,u)의 개수를 반환하세요.\n"
            "def solution(s):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="bronze-39",
        rank="Bronze",
        title="문자 바꾸기",
        style="프로그래머스",
        topic="문자열",
        type="func",
        func_name="solution",
        description="문자열 s와 두 문자 a, b가 주어집니다. s에 등장하는 모든 문자 a를 문자 b로 바꾼 새 문자열을 반환하는 함수 solution을 완성하세요.",
        input_desc="s : str, a : str(길이 1), b : str(길이 1)",
        output_desc="a가 모두 b로 치환된 문자열",
        examples=[
            {"args": ["banana", "a", "o"], "output": "bonono"},
            {"args": ["hello", "l", "L"], "output": "heLLo"},
        ],
        hints=[
            "문자열에서 특정 글자를 다른 글자로 한꺼번에 바꾸는 작업입니다.",
            "파이썬 문자열 메서드 replace(찾을값, 바꿀값) 를 쓰면 모든 등장 위치가 한 번에 바뀝니다.",
            "return s.replace(a, b) 한 줄이면 됩니다.",
        ],
        testcases=[
            {"args": ["banana", "a", "o"], "expected": "bonono"},
            {"args": ["hello", "l", "L"], "expected": "heLLo"},
            {"args": ["aaaa", "a", "b"], "expected": "bbbb"},
            {"args": ["abc", "z", "x"], "expected": "abc"},
            {"args": ["mississippi", "s", "S"], "expected": "miSSiSSippi"},
        ],
        reference_py=(
            "def solution(s, a, b):\n"
            "    return s.replace(a, b)\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public String solution(String s, String a, String b) {\n"
            "        return s.replace(a, b);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 문자열 s의 모든 a를 b로 바꿔 반환하세요.\n"
            "def solution(s, a, b):\n"
            "    answer = \"\"\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="bronze-40",
        rank="Bronze",
        title="앞뒤 공백 지우기",
        style="해외대기업",
        topic="문자열",
        type="stdin",
        description="한 줄의 문자열이 주어진다. 이 문자열의 앞과 뒤에 붙어있는 공백을 모두 제거한 결과를 출력하시오. (문자열 중간의 공백은 그대로 둔다.)",
        input_desc="첫째 줄에 앞뒤로 공백이 포함될 수 있는 문자열이 주어진다. 문자열 가운데에는 공백이 있을 수 있다.",
        output_desc="앞뒤 공백을 제거한 문자열을 출력한다.",
        examples=[
            {"input": "   hello   \n", "output": "hello\n"},
            {"input": "  코딩 테스트  \n", "output": "코딩 테스트\n"},
        ],
        hints=[
            "문자열의 시작 부분과 끝 부분에 있는 공백만 떼어내면 됩니다. 가운데 공백은 건드리지 않습니다.",
            "파이썬 문자열 메서드 strip() 은 양쪽 끝의 공백을 제거해 줍니다.",
            "s = input() 으로 한 줄을 받고 print(s.strip()) 하면 됩니다.",
        ],
        testcases=[
            {"input": "   hello   \n", "output": "hello\n"},
            {"input": "  코딩 테스트  \n", "output": "코딩 테스트\n"},
            {"input": "nospace\n", "output": "nospace\n"},
            {"input": "     a b c     \n", "output": "a b c\n"},
            {"input": "   x\n", "output": "x\n"},
        ],
        reference_py=(
            "s = input()\n"
            "print(s.strip())\n"
        ),
        reference_java=(
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        String s = br.readLine();\n"
            "        System.out.println(s.trim());\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 입력 문자열의 앞뒤 공백을 제거해 출력하세요.\n"
            "s = input()\n"
            "# print(...)\n"
        ),
    ),

    Problem(
        id="bronze-41",
        rank="Bronze",
        title="리스트 원소의 합",
        style="백준",
        topic="리스트",
        type="func",
        func_name="solution",
        description="정수들이 담긴 리스트 numbers가 주어집니다. 리스트에 들어있는 모든 원소의 합을 반환하는 함수 solution을 완성하세요. 빈 리스트의 합은 0입니다.",
        input_desc="numbers : list[int] (0 ≤ len(numbers) ≤ 1000)",
        output_desc="모든 원소의 합 (int)",
        examples=[
            {"args": [[1, 2, 3, 4]], "output": 10},
            {"args": [[-5, 5, 10]], "output": 10},
        ],
        hints=[
            "리스트의 원소들을 하나씩 더해 나가는 문제입니다.",
            "직접 반복문으로 더해도 되지만, 파이썬 내장 함수 sum() 이 리스트의 합을 바로 구해 줍니다.",
            "return sum(numbers) 한 줄이면 됩니다. (빈 리스트는 sum 이 0을 돌려줍니다.)",
        ],
        testcases=[
            {"args": [[1, 2, 3, 4]], "expected": 10},
            {"args": [[-5, 5, 10]], "expected": 10},
            {"args": [[]], "expected": 0},
            {"args": [[100]], "expected": 100},
            {"args": [[0, 0, 0]], "expected": 0},
        ],
        reference_py=(
            "def solution(numbers):\n"
            "    return sum(numbers)\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int[] numbers) {\n"
            "        int total = 0;\n"
            "        for (int x : numbers) total += x;\n"
            "        return total;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 리스트 numbers의 모든 원소의 합을 반환하세요.\n"
            "def solution(numbers):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="bronze-42",
        rank="Bronze",
        title="리스트 거꾸로",
        style="프로그래머스",
        topic="리스트",
        type="func",
        func_name="solution",
        description="정수 리스트 arr가 주어집니다. arr의 원소 순서를 거꾸로 뒤집은 새 리스트를 반환하는 함수 solution을 완성하세요.",
        input_desc="arr : list[int] (1 ≤ len(arr) ≤ 1000)",
        output_desc="원소 순서가 거꾸로 된 리스트",
        examples=[
            {"args": [[1, 2, 3]], "output": [3, 2, 1]},
            {"args": [[5, 4, 3, 2, 1]], "output": [1, 2, 3, 4, 5]},
        ],
        hints=[
            "리스트도 문자열처럼 슬라이싱이 가능합니다. 순서를 뒤집는 방법을 떠올려 보세요.",
            "슬라이싱 step에 -1을 주는 arr[::-1] 을 사용하면 뒤집힌 새 리스트가 만들어집니다.",
            "return arr[::-1] 한 줄이면 됩니다.",
        ],
        testcases=[
            {"args": [[1, 2, 3]], "expected": [3, 2, 1]},
            {"args": [[5, 4, 3, 2, 1]], "expected": [1, 2, 3, 4, 5]},
            {"args": [[7]], "expected": [7]},
            {"args": [[1, 1, 2]], "expected": [2, 1, 1]},
            {"args": [[-1, 0, 1]], "expected": [1, 0, -1]},
        ],
        reference_py=(
            "def solution(arr):\n"
            "    return arr[::-1]\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int[] solution(int[] arr) {\n"
            "        int n = arr.length;\n"
            "        int[] r = new int[n];\n"
            "        for (int i = 0; i < n; i++) r[i] = arr[n - 1 - i];\n"
            "        return r;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 리스트 arr를 거꾸로 뒤집어 반환하세요.\n"
            "def solution(arr):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="bronze-43",
        rank="Bronze",
        title="값의 위치 찾기",
        style="대기업",
        topic="리스트",
        type="func",
        func_name="solution",
        description="정수 리스트 arr와 정수 target이 주어집니다. arr에서 target이 처음으로 나타나는 위치(0부터 시작하는 인덱스)를 반환하세요. target이 리스트에 없으면 -1을 반환하는 함수 solution을 완성하세요.",
        input_desc="arr : list[int], target : int",
        output_desc="target이 처음 등장하는 인덱스, 없으면 -1 (int)",
        examples=[
            {"args": [[10, 20, 30, 40], 30], "output": 2},
            {"args": [[1, 2, 3], 9], "output": -1},
        ],
        hints=[
            "리스트를 앞에서부터 살펴보며 target과 같은 값을 처음 만나는 위치를 찾으면 됩니다.",
            "리스트 메서드 index() 는 값의 위치를 알려주지만 없을 때 오류가 납니다. 먼저 in 으로 존재 여부를 검사하세요.",
            "return arr.index(target) if target in arr else -1 처럼 작성하면 됩니다.",
        ],
        testcases=[
            {"args": [[10, 20, 30, 40], 30], "expected": 2},
            {"args": [[1, 2, 3], 9], "expected": -1},
            {"args": [[5, 5, 5], 5], "expected": 0},
            {"args": [[7], 7], "expected": 0},
            {"args": [[2, 4, 6, 8], 8], "expected": 3},
        ],
        reference_py=(
            "def solution(arr, target):\n"
            "    return arr.index(target) if target in arr else -1\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int[] arr, int target) {\n"
            "        for (int i = 0; i < arr.length; i++)\n"
            "            if (arr[i] == target) return i;\n"
            "        return -1;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# arr에서 target이 처음 나타나는 인덱스를, 없으면 -1을 반환하세요.\n"
            "def solution(arr, target):\n"
            "    answer = -1\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="bronze-44",
        rank="Bronze",
        title="소수인지 판별하기",
        style="백준",
        topic="수학",
        type="stdin",
        description="자연수 N이 주어졌을 때, N이 소수이면 \"소수\"를, 소수가 아니면 \"합성수\"를 출력하시오. (1은 소수가 아니다.)",
        input_desc="첫째 줄에 자연수 N(1 ≤ N ≤ 100000)이 주어진다.",
        output_desc="N이 소수이면 \"소수\", 아니면 \"합성수\"를 출력한다.",
        examples=[
            {"input": "7\n", "output": "소수\n"},
            {"input": "10\n", "output": "합성수\n"},
        ],
        hints=[
            "소수는 1과 자기 자신 외에 약수가 없는 2 이상의 수입니다. 2부터 나눠떨어지는 수가 있는지 확인해 보세요.",
            "2부터 N의 제곱근까지만 나눠 보면 충분합니다. 하나라도 나눠떨어지면 소수가 아닙니다.",
            "n<2 면 합성수, 아니면 i가 2부터 int(n**0.5)까지 n%i==0 이 한 번이라도 있으면 합성수, 끝까지 없으면 소수입니다.",
        ],
        testcases=[
            {"input": "7\n", "output": "소수\n"},
            {"input": "10\n", "output": "합성수\n"},
            {"input": "1\n", "output": "합성수\n"},
            {"input": "2\n", "output": "소수\n"},
            {"input": "97\n", "output": "소수\n"},
            {"input": "100000\n", "output": "합성수\n"},
        ],
        reference_py=(
            "n = int(input())\n"
            "if n < 2:\n"
            "    print('합성수')\n"
            "else:\n"
            "    is_prime = True\n"
            "    i = 2\n"
            "    while i * i <= n:\n"
            "        if n % i == 0:\n"
            "            is_prime = False\n"
            "            break\n"
            "        i += 1\n"
            "    print('소수' if is_prime else '합성수')\n"
        ),
        reference_java=(
            "import java.util.Scanner;\n"
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        int n = new Scanner(System.in).nextInt();\n"
            "        boolean prime = n >= 2;\n"
            "        for (int i = 2; (long) i * i <= n; i++) {\n"
            "            if (n % i == 0) { prime = false; break; }\n"
            "        }\n"
            "        System.out.println(prime ? \"소수\" : \"합성수\");\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# N이 소수이면 '소수', 아니면 '합성수'를 출력하세요.\n"
            "n = int(input())\n"
            "# ...\n"
        ),
    ),

    Problem(
        id="bronze-45",
        rank="Bronze",
        title="약수의 개수",
        style="해외대기업",
        topic="수학",
        type="func",
        func_name="solution",
        description="자연수 n이 주어집니다. n의 약수(n을 나누어떨어지게 하는 1 이상의 정수)의 개수를 반환하는 함수 solution을 완성하세요.",
        input_desc="n : int (1 ≤ n ≤ 100000)",
        output_desc="n의 약수의 개수 (int)",
        examples=[
            {"args": [6], "output": 4},
            {"args": [7], "output": 2},
        ],
        hints=[
            "1부터 n까지의 수 중에서 n을 나누어떨어지게 하는 수가 몇 개인지 세면 됩니다.",
            "i가 1부터 n까지 돌 때 n % i == 0 인 i의 개수를 세면 그것이 약수의 개수입니다.",
            "return sum(1 for i in range(1, n + 1) if n % i == 0) 으로 셀 수 있습니다.",
        ],
        testcases=[
            {"args": [6], "expected": 4},
            {"args": [7], "expected": 2},
            {"args": [1], "expected": 1},
            {"args": [12], "expected": 6},
            {"args": [16], "expected": 5},
        ],
        reference_py=(
            "def solution(n):\n"
            "    return sum(1 for i in range(1, n + 1) if n % i == 0)\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int n) {\n"
            "        int cnt = 0;\n"
            "        for (int i = 1; i <= n; i++)\n"
            "            if (n % i == 0) cnt++;\n"
            "        return cnt;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# n의 약수의 개수를 반환하세요.\n"
            "def solution(n):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="bronze-46",
        rank="Bronze",
        title="이진수로 바꾸기",
        style="프로그래머스",
        topic="수학",
        type="func",
        func_name="solution",
        description="0 이상의 정수 n이 주어집니다. n을 2진수로 나타낸 문자열을 반환하는 함수 solution을 완성하세요. (앞에 0b 같은 접두어 없이 0과 1로만 이루어진 문자열입니다. n이 0이면 \"0\"입니다.)",
        input_desc="n : int (0 ≤ n ≤ 1000000)",
        output_desc="n의 2진수 표현 문자열",
        examples=[
            {"args": [5], "output": "101"},
            {"args": [10], "output": "1010"},
        ],
        hints=[
            "10진수를 2진수로 바꾸는 문제입니다. 직접 2로 나눈 나머지를 거꾸로 모아도 되지만, 더 쉬운 방법이 있습니다.",
            "내장 함수 bin(n) 은 '0b101' 형태를 주고, format(n, 'b') 는 접두어 없는 2진수 문자열을 바로 줍니다.",
            "return format(n, 'b') 한 줄이면 됩니다. (또는 bin(n)[2:])",
        ],
        testcases=[
            {"args": [5], "expected": "101"},
            {"args": [10], "expected": "1010"},
            {"args": [0], "expected": "0"},
            {"args": [1], "expected": "1"},
            {"args": [255], "expected": "11111111"},
        ],
        reference_py=(
            "def solution(n):\n"
            "    return format(n, 'b')\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public String solution(int n) {\n"
            "        return Integer.toBinaryString(n);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# n을 접두어 없는 2진수 문자열로 바꿔 반환하세요.\n"
            "def solution(n):\n"
            "    answer = \"\"\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="bronze-47",
        rank="Bronze",
        title="아스키 코드 값",
        style="백준",
        topic="아스키코드",
        type="stdin",
        description="알파벳 대문자 또는 소문자 하나가 입력으로 주어진다. 그 문자의 아스키(ASCII) 코드 값을 출력하시오.",
        input_desc="첫째 줄에 알파벳 한 글자가 주어진다.",
        output_desc="입력된 문자의 아스키 코드 값을 출력한다.",
        examples=[
            {"input": "A\n", "output": "65\n"},
            {"input": "a\n", "output": "97\n"},
        ],
        hints=[
            "문자를 그에 대응하는 숫자 코드로 바꾸는 작업입니다. 파이썬에 그런 변환 함수가 있습니다.",
            "내장 함수 ord(문자) 는 한 글자의 아스키 코드 값을 정수로 돌려줍니다.",
            "c = input() 으로 받은 뒤 print(ord(c)) 하면 됩니다.",
        ],
        testcases=[
            {"input": "A\n", "output": "65\n"},
            {"input": "a\n", "output": "97\n"},
            {"input": "Z\n", "output": "90\n"},
            {"input": "z\n", "output": "122\n"},
            {"input": "0\n", "output": "48\n"},
        ],
        reference_py=(
            "c = input()\n"
            "print(ord(c))\n"
        ),
        reference_java=(
            "import java.util.Scanner;\n"
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        char c = new Scanner(System.in).next().charAt(0);\n"
            "        System.out.println((int) c);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 입력된 한 글자의 아스키 코드 값을 출력하세요.\n"
            "c = input()\n"
            "# print(...)\n"
        ),
    ),

    Problem(
        id="bronze-48",
        rank="Bronze",
        title="모두 소문자로",
        style="대기업",
        topic="문자열",
        type="func",
        func_name="solution",
        description="영어 알파벳과 숫자로 이루어진 문자열 s가 주어집니다. s에 포함된 모든 영어 대문자를 소문자로 바꾼 문자열을 반환하는 함수 solution을 완성하세요.",
        input_desc="s : str (1 ≤ len(s) ≤ 1000)",
        output_desc="모든 문자가 소문자로 바뀐 문자열",
        examples=[
            {"args": ["HELLO"], "output": "hello"},
            {"args": ["Python3"], "output": "python3"},
        ],
        hints=[
            "문자열 전체의 대문자를 소문자로 바꾸는 작업입니다.",
            "파이썬 문자열 메서드 lower() 를 사용하면 됩니다.",
            "return s.lower() 한 줄이면 끝납니다.",
        ],
        testcases=[
            {"args": ["HELLO"], "expected": "hello"},
            {"args": ["Python3"], "expected": "python3"},
            {"args": ["abc"], "expected": "abc"},
            {"args": ["A"], "expected": "a"},
            {"args": ["MiX123CaSe"], "expected": "mix123case"},
        ],
        reference_py=(
            "def solution(s):\n"
            "    return s.lower()\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public String solution(String s) {\n"
            "        return s.toLowerCase();\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 문자열 s의 모든 문자를 소문자로 바꿔 반환하세요.\n"
            "def solution(s):\n"
            "    answer = \"\"\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="bronze-49",
        rank="Bronze",
        title="특정 문자 모두 지우기",
        style="해외대기업",
        topic="문자열",
        type="func",
        func_name="solution",
        description="문자열 s와 문자 c가 주어집니다. s에서 문자 c를 모두 제거한 문자열을 반환하는 함수 solution을 완성하세요.",
        input_desc="s : str, c : str(길이 1)",
        output_desc="문자 c가 모두 제거된 문자열",
        examples=[
            {"args": ["banana", "a"], "output": "bnn"},
            {"args": ["hello world", " "], "output": "helloworld"},
        ],
        hints=[
            "특정 글자를 '아무것도 아닌 것'으로 바꾼다고 생각하면 제거와 같습니다.",
            "문자열 메서드 replace(c, '') 처럼 빈 문자열로 치환하면 그 글자가 사라집니다.",
            "return s.replace(c, '') 한 줄이면 됩니다.",
        ],
        testcases=[
            {"args": ["banana", "a"], "expected": "bnn"},
            {"args": ["hello world", " "], "expected": "helloworld"},
            {"args": ["aaaa", "a"], "expected": ""},
            {"args": ["abc", "z"], "expected": "abc"},
            {"args": ["mississippi", "s"], "expected": "miiippi"},
        ],
        reference_py=(
            "def solution(s, c):\n"
            "    return s.replace(c, '')\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public String solution(String s, String c) {\n"
            "        return s.replace(c, \"\");\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 문자열 s에서 문자 c를 모두 제거해 반환하세요.\n"
            "def solution(s, c):\n"
            "    answer = \"\"\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="bronze-50",
        rank="Bronze",
        title="값의 등장 횟수",
        style="백준",
        topic="리스트",
        type="stdin",
        description="N개의 정수와 찾을 값 K가 주어진다. N개의 정수 중에서 K와 같은 값이 몇 번 등장하는지 세어 출력하시오.",
        input_desc="첫째 줄에 N(1 ≤ N ≤ 1000), 둘째 줄에 N개의 정수가 공백으로, 셋째 줄에 찾을 값 K가 주어진다.",
        output_desc="N개의 정수 중 K의 등장 횟수를 출력한다.",
        examples=[
            {"input": "5\n1 2 2 3 2\n2\n", "output": "3\n"},
            {"input": "4\n5 6 7 8\n9\n", "output": "0\n"},
        ],
        hints=[
            "여러 정수를 리스트로 받은 다음, 그 안에서 K와 같은 값의 개수를 세면 됩니다.",
            "리스트로 받은 뒤 리스트 메서드 count(K) 를 쓰면 K의 개수를 바로 알 수 있습니다.",
            "arr = list(map(int, input().split())) 로 받고 k = int(input()) 후 print(arr.count(k)) 하면 됩니다. (N은 받기만 하면 됨)",
        ],
        testcases=[
            {"input": "5\n1 2 2 3 2\n2\n", "output": "3\n"},
            {"input": "4\n5 6 7 8\n9\n", "output": "0\n"},
            {"input": "3\n7 7 7\n7\n", "output": "3\n"},
            {"input": "1\n42\n42\n", "output": "1\n"},
            {"input": "6\n-1 -1 0 1 -1 2\n-1\n", "output": "3\n"},
        ],
        reference_py=(
            "n = int(input())\n"
            "arr = list(map(int, input().split()))\n"
            "k = int(input())\n"
            "print(arr.count(k))\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        Scanner sc = new Scanner(System.in);\n"
            "        int n = sc.nextInt();\n"
            "        int[] arr = new int[n];\n"
            "        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();\n"
            "        int k = sc.nextInt(), cnt = 0;\n"
            "        for (int x : arr) if (x == k) cnt++;\n"
            "        System.out.println(cnt);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# N개의 정수 중 K의 등장 횟수를 세어 출력하세요.\n"
            "n = int(input())\n"
            "arr = list(map(int, input().split()))\n"
            "k = int(input())\n"
            "# print(...)\n"
        ),
    ),

]
