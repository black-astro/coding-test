"""브론즈 랭크 — 기본 입출력 / 조건문 / 반복문 / 간단한 구현.

목표 50문제. 현재 시드 5문제. (Problem 을 더 append 하면 확장된다.)
"""

from engine.models import Problem

PROBLEMS = [

    Problem(
        id="bronze-01",
        rank="Bronze",
        title="A+B",
        style="백준",
        topic="입출력",
        type="stdin",
        description="두 정수 A와 B를 입력받아 A+B를 출력하는 프로그램을 작성하시오.",
        input_desc="첫째 줄에 A와 B가 공백으로 구분되어 주어진다. (0 < A, B < 10)",
        output_desc="첫째 줄에 A+B를 출력한다.",
        examples=[
            {"input": "1 2\n", "output": "3\n"},
            {"input": "9 8\n", "output": "17\n"},
        ],
        hints=[
            "한 줄에 두 수가 공백으로 들어옵니다. 입력을 어떻게 두 개로 나눌지 생각해 보세요.",
            "input().split() 으로 문자열을 나눈 뒤, 각각을 int() 로 변환하면 됩니다.",
            "a, b = map(int, input().split()) 로 받고 print(a + b) 하면 끝입니다.",
        ],
        testcases=[
            {"input": "1 2\n", "output": "3\n"},
            {"input": "9 8\n", "output": "17\n"},
            {"input": "5 5\n", "output": "10\n"},
            {"input": "1 1\n", "output": "2\n"},
        ],
        reference_py=(
            "a, b = map(int, input().split())\n"
            "print(a + b)\n"
        ),
        reference_java=(
            "import java.util.Scanner;\n"
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        Scanner sc = new Scanner(System.in);\n"
            "        int a = sc.nextInt(), b = sc.nextInt();\n"
            "        System.out.println(a + b);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# A+B : 두 정수를 입력받아 합을 출력하세요.\n"
            "a, b = map(int, input().split())\n"
            "# print(...)\n"
        ),
    ),

    Problem(
        id="bronze-02",
        rank="Bronze",
        title="별 찍기",
        style="백준",
        topic="반복문",
        type="stdin",
        description="N이 주어졌을 때, 첫째 줄에 별 1개, 둘째 줄에 별 2개, ..., N번째 줄에 별 N개를 찍는 문제이다.",
        input_desc="첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.",
        output_desc="첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.",
        examples=[
            {"input": "3\n", "output": "*\n**\n***\n"},
            {"input": "5\n", "output": "*\n**\n***\n****\n*****\n"},
        ],
        hints=[
            "줄 번호 i가 1부터 N까지 갈 때, 그 줄에 찍히는 별의 개수와 i의 관계를 찾아보세요.",
            "for i in range(1, N+1) 반복문 안에서 '*' * i 처럼 문자열을 곱하면 별을 만들 수 있습니다.",
            "for i in range(1, N+1): print('*' * i) — i번째 줄에 별 i개입니다.",
        ],
        testcases=[
            {"input": "3\n", "output": "*\n**\n***\n"},
            {"input": "1\n", "output": "*\n"},
            {"input": "5\n", "output": "*\n**\n***\n****\n*****\n"},
        ],
        reference_py=(
            "n = int(input())\n"
            "for i in range(1, n + 1):\n"
            "    print('*' * i)\n"
        ),
        reference_java=(
            "import java.util.Scanner;\n"
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        int n = new Scanner(System.in).nextInt();\n"
            "        StringBuilder sb = new StringBuilder();\n"
            "        for (int i = 1; i <= n; i++) {\n"
            "            for (int j = 0; j < i; j++) sb.append('*');\n"
            "            sb.append('\\n');\n"
            "        }\n"
            "        System.out.print(sb);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 별 찍기 : N줄에 걸쳐 별을 1개씩 늘려가며 출력하세요.\n"
            "n = int(input())\n"
            "# for ...\n"
        ),
    ),

    Problem(
        id="bronze-03",
        rank="Bronze",
        title="짝수와 홀수",
        style="프로그래머스",
        topic="조건문",
        type="func",
        func_name="solution",
        description="정수 num이 짝수일 경우 \"Even\"을, 홀수인 경우 \"Odd\"를 반환하는 함수 solution을 완성하세요.",
        input_desc="num : int (0 ≤ num ≤ 10000)",
        output_desc="\"Even\" 또는 \"Odd\" 문자열",
        examples=[
            {"args": [3], "output": "Odd"},
            {"args": [4], "output": "Even"},
        ],
        hints=[
            "어떤 수가 짝수인지 홀수인지는 2로 나눈 나머지로 알 수 있습니다.",
            "num % 2 의 값이 0이면 짝수, 1이면 홀수입니다.",
            "return \"Even\" if num % 2 == 0 else \"Odd\" 한 줄이면 됩니다.",
        ],
        testcases=[
            {"args": [3], "expected": "Odd"},
            {"args": [4], "expected": "Even"},
            {"args": [0], "expected": "Even"},
            {"args": [9999], "expected": "Odd"},
        ],
        reference_py=(
            "def solution(num):\n"
            "    return \"Even\" if num % 2 == 0 else \"Odd\"\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public String solution(int num) {\n"
            "        return num % 2 == 0 ? \"Even\" : \"Odd\";\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 짝수면 \"Even\", 홀수면 \"Odd\" 를 반환하세요.\n"
            "def solution(num):\n"
            "    answer = \"\"\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="bronze-04",
        rank="Bronze",
        title="최댓값 찾기",
        style="백준",
        topic="구현",
        type="stdin",
        description="N개의 정수가 주어졌을 때, 그 중 가장 큰 값을 출력하시오.",
        input_desc="첫째 줄에 N(1 ≤ N ≤ 1000), 둘째 줄에 N개의 정수가 공백으로 주어진다.",
        output_desc="가장 큰 값을 출력한다.",
        examples=[
            {"input": "5\n3 1 9 2 7\n", "output": "9\n"},
            {"input": "3\n-1 -5 -2\n", "output": "-1\n"},
        ],
        hints=[
            "둘째 줄의 여러 수를 리스트로 받는 것부터 시작하세요.",
            "list(map(int, input().split())) 로 받은 뒤, 가장 큰 값을 구하는 내장 함수를 떠올려 보세요.",
            "arr = list(map(int, input().split())) 후 print(max(arr)) 입니다. (N은 받기만 하면 됨)",
        ],
        testcases=[
            {"input": "5\n3 1 9 2 7\n", "output": "9\n"},
            {"input": "3\n-1 -5 -2\n", "output": "-1\n"},
            {"input": "1\n42\n", "output": "42\n"},
            {"input": "4\n7 7 7 7\n", "output": "7\n"},
        ],
        reference_py=(
            "n = int(input())\n"
            "arr = list(map(int, input().split()))\n"
            "print(max(arr))\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        Scanner sc = new Scanner(System.in);\n"
            "        int n = sc.nextInt(), best = Integer.MIN_VALUE;\n"
            "        for (int i = 0; i < n; i++) best = Math.max(best, sc.nextInt());\n"
            "        System.out.println(best);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 최댓값 찾기\n"
            "n = int(input())\n"
            "arr = list(map(int, input().split()))\n"
            "# print(...)\n"
        ),
    ),

    Problem(
        id="bronze-05",
        rank="Bronze",
        title="문자열 뒤집기",
        style="프로그래머스",
        topic="문자열",
        type="func",
        func_name="solution",
        description="문자열 s가 주어지면 s를 거꾸로 뒤집은 문자열을 반환하는 함수 solution을 완성하세요.",
        input_desc="s : str (1 ≤ len(s) ≤ 1000)",
        output_desc="뒤집힌 문자열",
        examples=[
            {"args": ["hello"], "output": "olleh"},
            {"args": ["Python"], "output": "nohtyP"},
        ],
        hints=[
            "문자열도 시퀀스라서 인덱싱/슬라이싱이 됩니다.",
            "파이썬 슬라이싱에는 '거꾸로'를 의미하는 step 값이 있습니다. s[::-1] 을 떠올려 보세요.",
            "return s[::-1] 한 줄로 끝납니다.",
        ],
        testcases=[
            {"args": ["hello"], "expected": "olleh"},
            {"args": ["Python"], "expected": "nohtyP"},
            {"args": ["a"], "expected": "a"},
            {"args": ["12345"], "expected": "54321"},
        ],
        reference_py=(
            "def solution(s):\n"
            "    return s[::-1]\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public String solution(String s) {\n"
            "        return new StringBuilder(s).reverse().toString();\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 문자열을 거꾸로 뒤집어 반환하세요.\n"
            "def solution(s):\n"
            "    answer = \"\"\n"
            "    return answer\n"
        ),
    ),

]
