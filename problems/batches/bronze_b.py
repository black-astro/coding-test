"""브론즈 배치 B — 반복문 / 약수·배수 / 구구단 / 누적합 / 자릿수 등 기초 반복.

bronze-21 ~ bronze-35 (15문제). base 및 다른 배치와 주제 중복 없음.
"""

from engine.models import Problem

RANK = "Bronze"

PROBLEMS = [

    Problem(
        id="bronze-21",
        rank="Bronze",
        title="정수 N개의 합",
        style="백준",
        topic="반복문",
        type="stdin",
        description="N개의 정수가 주어졌을 때, 모든 수의 합을 출력하시오.",
        input_desc="첫째 줄에 N(1 ≤ N ≤ 1000), 둘째 줄에 N개의 정수가 공백으로 주어진다. (-1000 ≤ 각 수 ≤ 1000)",
        output_desc="N개 정수의 합을 출력한다.",
        examples=[
            {"input": "5\n1 2 3 4 5\n", "output": "15\n"},
            {"input": "3\n10 -5 7\n", "output": "12\n"},
        ],
        hints=[
            "둘째 줄의 여러 수를 하나씩 더해 나가야 합니다. 먼저 수들을 리스트로 받아 보세요.",
            "list(map(int, input().split())) 로 받은 뒤, 합을 담을 변수를 0으로 두고 반복문으로 누적하면 됩니다.",
            "total = 0; for x in arr: total += x; print(total) — 또는 print(sum(arr)) 한 줄로도 됩니다.",
        ],
        testcases=[
            {"input": "5\n1 2 3 4 5\n", "output": "15\n"},
            {"input": "3\n10 -5 7\n", "output": "12\n"},
            {"input": "1\n42\n", "output": "42\n"},
            {"input": "4\n-1 -2 -3 -4\n", "output": "-10\n"},
            {"input": "2\n0 0\n", "output": "0\n"},
        ],
        reference_py=(
            "n = int(input())\n"
            "arr = list(map(int, input().split()))\n"
            "total = 0\n"
            "for x in arr:\n"
            "    total += x\n"
            "print(total)\n"
        ),
        reference_java=(
            "import java.util.Scanner;\n"
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        Scanner sc = new Scanner(System.in);\n"
            "        int n = sc.nextInt();\n"
            "        int total = 0;\n"
            "        for (int i = 0; i < n; i++) total += sc.nextInt();\n"
            "        System.out.println(total);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 정수 N개의 합을 구하세요.\n"
            "n = int(input())\n"
            "arr = list(map(int, input().split()))\n"
            "# print(...)\n"
        ),
    ),

    Problem(
        id="bronze-22",
        rank="Bronze",
        title="점수 평균",
        style="프로그래머스",
        topic="반복문",
        type="func",
        func_name="solution",
        description="여러 학생의 점수가 담긴 리스트 scores가 주어질 때, 점수의 평균을 소수점 이하를 버린 정수로 반환하는 함수 solution을 완성하세요.",
        input_desc="scores : List[int] (1 ≤ len(scores) ≤ 1000, 0 ≤ 각 점수 ≤ 100)",
        output_desc="평균(소수점 이하 버림) : int",
        examples=[
            {"args": [[90, 80, 70]], "output": 80},
            {"args": [[100, 50]], "output": 75},
        ],
        hints=[
            "평균은 (모든 점수의 합) 을 (점수의 개수) 로 나눈 값입니다. 먼저 합과 개수를 구해 보세요.",
            "sum(scores) 와 len(scores) 를 이용하되, 소수점을 버리려면 일반 나눗셈(/) 대신 몫 연산(//)을 씁니다.",
            "return sum(scores) // len(scores) 한 줄이면 됩니다.",
        ],
        testcases=[
            {"args": [[90, 80, 70]], "expected": 80},
            {"args": [[100, 50]], "expected": 75},
            {"args": [[100]], "expected": 100},
            {"args": [[50, 55]], "expected": 52},
            {"args": [[0, 0, 0, 0]], "expected": 0},
        ],
        reference_py=(
            "def solution(scores):\n"
            "    total = 0\n"
            "    for s in scores:\n"
            "        total += s\n"
            "    return total // len(scores)\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int[] scores) {\n"
            "        int total = 0;\n"
            "        for (int s : scores) total += s;\n"
            "        return total / scores.length;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 점수의 평균(소수점 이하 버림)을 반환하세요.\n"
            "def solution(scores):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="bronze-23",
        rank="Bronze",
        title="짝수의 개수",
        style="대기업",
        topic="반복문",
        type="stdin",
        description="N개의 정수가 주어졌을 때, 그 중 짝수가 몇 개인지 세어 출력하시오.",
        input_desc="첫째 줄에 N(1 ≤ N ≤ 1000), 둘째 줄에 N개의 정수가 공백으로 주어진다.",
        output_desc="짝수의 개수를 출력한다.",
        examples=[
            {"input": "5\n1 2 3 4 5\n", "output": "2\n"},
            {"input": "4\n2 4 6 8\n", "output": "4\n"},
        ],
        hints=[
            "수를 하나씩 보면서 그 수가 짝수일 때만 세어야 합니다. 세는 변수를 따로 두세요.",
            "어떤 수가 짝수인지는 그 수를 2로 나눈 나머지(% 2)가 0인지로 알 수 있습니다.",
            "cnt = 0; for x in arr: if x % 2 == 0: cnt += 1; print(cnt) 입니다.",
        ],
        testcases=[
            {"input": "5\n1 2 3 4 5\n", "output": "2\n"},
            {"input": "4\n2 4 6 8\n", "output": "4\n"},
            {"input": "3\n1 3 5\n", "output": "0\n"},
            {"input": "1\n0\n", "output": "1\n"},
            {"input": "6\n-2 -1 0 1 2 3\n", "output": "3\n"},
        ],
        reference_py=(
            "n = int(input())\n"
            "arr = list(map(int, input().split()))\n"
            "cnt = 0\n"
            "for x in arr:\n"
            "    if x % 2 == 0:\n"
            "        cnt += 1\n"
            "print(cnt)\n"
        ),
        reference_java=(
            "import java.util.Scanner;\n"
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        Scanner sc = new Scanner(System.in);\n"
            "        int n = sc.nextInt();\n"
            "        int cnt = 0;\n"
            "        for (int i = 0; i < n; i++) {\n"
            "            if (sc.nextInt() % 2 == 0) cnt++;\n"
            "        }\n"
            "        System.out.println(cnt);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 짝수의 개수를 세어 출력하세요.\n"
            "n = int(input())\n"
            "arr = list(map(int, input().split()))\n"
            "# print(...)\n"
        ),
    ),

    Problem(
        id="bronze-24",
        rank="Bronze",
        title="약수의 개수",
        style="백준",
        topic="약수",
        type="stdin",
        description="자연수 N의 약수가 모두 몇 개인지 출력하시오. 약수란 N을 나누어떨어지게 하는 수이다.",
        input_desc="첫째 줄에 자연수 N(1 ≤ N ≤ 10000)이 주어진다.",
        output_desc="N의 약수의 개수를 출력한다.",
        examples=[
            {"input": "6\n", "output": "4\n"},
            {"input": "7\n", "output": "2\n"},
        ],
        hints=[
            "1부터 N까지의 수를 차례로 확인하면서, N을 나누어떨어지게 하는 수가 약수입니다.",
            "i가 N의 약수인지는 N % i == 0 으로 판별합니다. range(1, N+1) 을 반복하며 세어 보세요.",
            "cnt = 0; for i in range(1, N+1): if N % i == 0: cnt += 1; print(cnt) 입니다.",
        ],
        testcases=[
            {"input": "6\n", "output": "4\n"},
            {"input": "7\n", "output": "2\n"},
            {"input": "1\n", "output": "1\n"},
            {"input": "12\n", "output": "6\n"},
            {"input": "100\n", "output": "9\n"},
        ],
        reference_py=(
            "n = int(input())\n"
            "cnt = 0\n"
            "for i in range(1, n + 1):\n"
            "    if n % i == 0:\n"
            "        cnt += 1\n"
            "print(cnt)\n"
        ),
        reference_java=(
            "import java.util.Scanner;\n"
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        int n = new Scanner(System.in).nextInt();\n"
            "        int cnt = 0;\n"
            "        for (int i = 1; i <= n; i++) {\n"
            "            if (n % i == 0) cnt++;\n"
            "        }\n"
            "        System.out.println(cnt);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# N의 약수의 개수를 출력하세요.\n"
            "n = int(input())\n"
            "# for ...\n"
        ),
    ),

    Problem(
        id="bronze-25",
        rank="Bronze",
        title="3 또는 5의 배수 합",
        style="해외대기업",
        topic="배수",
        type="func",
        func_name="solution",
        description="자연수 n이 주어질 때, 1 이상 n 이하의 자연수 중 3의 배수이거나 5의 배수인 모든 수의 합을 반환하는 함수 solution을 완성하세요.",
        input_desc="n : int (1 ≤ n ≤ 100000)",
        output_desc="3 또는 5의 배수의 총합 : int",
        examples=[
            {"args": [10], "output": 33},
            {"args": [5], "output": 8},
        ],
        hints=[
            "1부터 n까지의 수를 하나씩 보면서, 조건에 맞는 수만 더해 나가면 됩니다.",
            "어떤 수가 3의 배수이거나 5의 배수인지는 (x % 3 == 0) 또는 (x % 5 == 0) 으로 판별합니다.",
            "return sum(x for x in range(1, n+1) if x % 3 == 0 or x % 5 == 0) 입니다.",
        ],
        testcases=[
            {"args": [10], "expected": 33},
            {"args": [5], "expected": 8},
            {"args": [1], "expected": 0},
            {"args": [15], "expected": 60},
            {"args": [2], "expected": 0},
        ],
        reference_py=(
            "def solution(n):\n"
            "    total = 0\n"
            "    for x in range(1, n + 1):\n"
            "        if x % 3 == 0 or x % 5 == 0:\n"
            "            total += x\n"
            "    return total\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int n) {\n"
            "        int total = 0;\n"
            "        for (int x = 1; x <= n; x++) {\n"
            "            if (x % 3 == 0 || x % 5 == 0) total += x;\n"
            "        }\n"
            "        return total;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 1..n 중 3 또는 5의 배수의 합을 반환하세요.\n"
            "def solution(n):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="bronze-26",
        rank="Bronze",
        title="최대공약수 구하기",
        style="프로그래머스",
        topic="공약수",
        type="func",
        func_name="solution",
        description="두 자연수 a와 b가 주어질 때, 두 수의 최대공약수(두 수를 모두 나누어떨어지게 하는 가장 큰 수)를 반환하는 함수 solution을 완성하세요.",
        input_desc="a, b : int (1 ≤ a, b ≤ 10000)",
        output_desc="a와 b의 최대공약수 : int",
        examples=[
            {"args": [12, 18], "output": 6},
            {"args": [5, 7], "output": 1},
        ],
        hints=[
            "두 수를 모두 나누어떨어지게 하는 수 중에서 가장 큰 값을 찾으면 됩니다.",
            "1부터 min(a, b)까지 반복하면서 a % i == 0 이고 b % i == 0 인 i를 찾고, 그 중 가장 큰 값을 기록하세요.",
            "answer = 1; for i in range(1, min(a,b)+1): if a%i==0 and b%i==0: answer = i; return answer 입니다.",
        ],
        testcases=[
            {"args": [12, 18], "expected": 6},
            {"args": [5, 7], "expected": 1},
            {"args": [10, 10], "expected": 10},
            {"args": [100, 80], "expected": 20},
            {"args": [1, 9999], "expected": 1},
        ],
        reference_py=(
            "def solution(a, b):\n"
            "    answer = 1\n"
            "    for i in range(1, min(a, b) + 1):\n"
            "        if a % i == 0 and b % i == 0:\n"
            "            answer = i\n"
            "    return answer\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int a, int b) {\n"
            "        int answer = 1;\n"
            "        int m = Math.min(a, b);\n"
            "        for (int i = 1; i <= m; i++) {\n"
            "            if (a % i == 0 && b % i == 0) answer = i;\n"
            "        }\n"
            "        return answer;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 두 수 a, b의 최대공약수를 반환하세요.\n"
            "def solution(a, b):\n"
            "    answer = 1\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="bronze-27",
        rank="Bronze",
        title="최소공배수 구하기",
        style="백준",
        topic="최소공배수",
        type="stdin",
        description="두 자연수 A와 B가 주어질 때, 두 수의 최소공배수(A의 배수이면서 B의 배수인 가장 작은 자연수)를 출력하시오.",
        input_desc="첫째 줄에 두 자연수 A와 B가 공백으로 주어진다. (1 ≤ A, B ≤ 1000)",
        output_desc="A와 B의 최소공배수를 출력한다.",
        examples=[
            {"input": "2 3\n", "output": "6\n"},
            {"input": "4 6\n", "output": "12\n"},
        ],
        hints=[
            "두 수의 배수를 작은 것부터 차례로 만들어 보며, 둘 다의 배수가 되는 첫 수를 찾으면 됩니다.",
            "1부터 차례로 늘려가며 i가 A의 배수(i % A == 0)이고 B의 배수(i % B == 0)인 첫 i를 while 문으로 찾을 수 있습니다.",
            "i = 1; while i % a != 0 or i % b != 0: i += 1; print(i) 입니다. (혹은 a*b를 최대공약수로 나눠도 됩니다.)",
        ],
        testcases=[
            {"input": "2 3\n", "output": "6\n"},
            {"input": "4 6\n", "output": "12\n"},
            {"input": "5 5\n", "output": "5\n"},
            {"input": "7 1\n", "output": "7\n"},
            {"input": "12 8\n", "output": "24\n"},
        ],
        reference_py=(
            "a, b = map(int, input().split())\n"
            "i = 1\n"
            "while i % a != 0 or i % b != 0:\n"
            "    i += 1\n"
            "print(i)\n"
        ),
        reference_java=(
            "import java.util.Scanner;\n"
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        Scanner sc = new Scanner(System.in);\n"
            "        int a = sc.nextInt(), b = sc.nextInt();\n"
            "        int i = 1;\n"
            "        while (i % a != 0 || i % b != 0) i++;\n"
            "        System.out.println(i);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 두 수 A, B의 최소공배수를 출력하세요.\n"
            "a, b = map(int, input().split())\n"
            "# while ...\n"
        ),
    ),

    Problem(
        id="bronze-28",
        rank="Bronze",
        title="구구단 출력",
        style="백준",
        topic="구구단",
        type="stdin",
        description="N을 입력받아 N단의 구구단을 출력하는 프로그램을 작성하시오. 출력 형식은 'N * i = N*i' 이다.",
        input_desc="첫째 줄에 N(1 ≤ N ≤ 9)이 주어진다.",
        output_desc="N * 1 = ? 부터 N * 9 = ? 까지 9줄을 출력한다.",
        examples=[
            {"input": "2\n", "output": "2 * 1 = 2\n2 * 2 = 4\n2 * 3 = 6\n2 * 4 = 8\n2 * 5 = 10\n2 * 6 = 12\n2 * 7 = 14\n2 * 8 = 16\n2 * 9 = 18\n"},
            {"input": "5\n", "output": "5 * 1 = 5\n5 * 2 = 10\n5 * 3 = 15\n5 * 4 = 20\n5 * 5 = 25\n5 * 6 = 30\n5 * 7 = 35\n5 * 8 = 40\n5 * 9 = 45\n"},
        ],
        hints=[
            "곱하는 수 i를 1부터 9까지 바꿔 가며 한 줄씩 출력하면 됩니다.",
            "for i in range(1, 10) 반복문 안에서 N과 i, 그리고 N*i 를 형식에 맞게 출력하세요.",
            "for i in range(1, 10): print(f\"{n} * {i} = {n*i}\") 입니다. 띄어쓰기까지 정확히 맞추세요.",
        ],
        testcases=[
            {"input": "2\n", "output": "2 * 1 = 2\n2 * 2 = 4\n2 * 3 = 6\n2 * 4 = 8\n2 * 5 = 10\n2 * 6 = 12\n2 * 7 = 14\n2 * 8 = 16\n2 * 9 = 18\n"},
            {"input": "5\n", "output": "5 * 1 = 5\n5 * 2 = 10\n5 * 3 = 15\n5 * 4 = 20\n5 * 5 = 25\n5 * 6 = 30\n5 * 7 = 35\n5 * 8 = 40\n5 * 9 = 45\n"},
            {"input": "1\n", "output": "1 * 1 = 1\n1 * 2 = 2\n1 * 3 = 3\n1 * 4 = 4\n1 * 5 = 5\n1 * 6 = 6\n1 * 7 = 7\n1 * 8 = 8\n1 * 9 = 9\n"},
            {"input": "9\n", "output": "9 * 1 = 9\n9 * 2 = 18\n9 * 3 = 27\n9 * 4 = 36\n9 * 5 = 45\n9 * 6 = 54\n9 * 7 = 63\n9 * 8 = 72\n9 * 9 = 81\n"},
        ],
        reference_py=(
            "n = int(input())\n"
            "for i in range(1, 10):\n"
            "    print(f\"{n} * {i} = {n * i}\")\n"
        ),
        reference_java=(
            "import java.util.Scanner;\n"
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        int n = new Scanner(System.in).nextInt();\n"
            "        for (int i = 1; i <= 9; i++) {\n"
            "            System.out.println(n + \" * \" + i + \" = \" + (n * i));\n"
            "        }\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# N단의 구구단을 'N * i = N*i' 형식으로 출력하세요.\n"
            "n = int(input())\n"
            "# for ...\n"
        ),
    ),

    Problem(
        id="bronze-29",
        rank="Bronze",
        title="곱셈표 만들기",
        style="대기업",
        topic="곱셈표",
        type="func",
        func_name="solution",
        description="자연수 n이 주어질 때, i행 j열의 값이 i*j인 n×n 곱셈표를 2차원 리스트로 반환하는 함수 solution을 완성하세요. (i, j는 1부터 n까지)",
        input_desc="n : int (1 ≤ n ≤ 20)",
        output_desc="각 행이 리스트인 2차원 리스트 (List[List[int]])",
        examples=[
            {"args": [2], "output": [[1, 2], [2, 4]]},
            {"args": [3], "output": [[1, 2, 3], [2, 4, 6], [3, 6, 9]]},
        ],
        hints=[
            "행(i)과 열(j)을 각각 1부터 n까지 돌리는 이중 반복문이 필요합니다.",
            "바깥 반복으로 한 행을 만들고, 안쪽 반복으로 i*j 값을 그 행 리스트에 차곡차곡 추가한 뒤 전체 표에 넣으세요.",
            "table = []; for i in range(1,n+1): row = [i*j for j in range(1,n+1)]; table.append(row); return table 입니다.",
        ],
        testcases=[
            {"args": [2], "expected": [[1, 2], [2, 4]]},
            {"args": [3], "expected": [[1, 2, 3], [2, 4, 6], [3, 6, 9]]},
            {"args": [1], "expected": [[1]]},
            {"args": [4], "expected": [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]]},
        ],
        reference_py=(
            "def solution(n):\n"
            "    table = []\n"
            "    for i in range(1, n + 1):\n"
            "        row = []\n"
            "        for j in range(1, n + 1):\n"
            "            row.append(i * j)\n"
            "        table.append(row)\n"
            "    return table\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int[][] solution(int n) {\n"
            "        int[][] table = new int[n][n];\n"
            "        for (int i = 1; i <= n; i++) {\n"
            "            for (int j = 1; j <= n; j++) {\n"
            "                table[i - 1][j - 1] = i * j;\n"
            "            }\n"
            "        }\n"
            "        return table;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# i행 j열 값이 i*j인 n x n 곱셈표를 2차원 리스트로 반환하세요.\n"
            "def solution(n):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="bronze-30",
        rank="Bronze",
        title="누적합 배열",
        style="프로그래머스",
        topic="누적합",
        type="func",
        func_name="solution",
        description="정수 리스트 arr이 주어질 때, i번째 원소가 arr[0]부터 arr[i]까지의 합인 누적합 리스트를 반환하는 함수 solution을 완성하세요.",
        input_desc="arr : List[int] (1 ≤ len(arr) ≤ 1000)",
        output_desc="누적합이 담긴 리스트 (List[int])",
        examples=[
            {"args": [[1, 2, 3]], "output": [1, 3, 6]},
            {"args": [[5]], "output": [5]},
        ],
        hints=[
            "앞에서부터 더해 온 합을 기억하면서, 현재 원소를 더한 값을 결과에 차례로 넣으면 됩니다.",
            "running = 0 같은 누적 변수를 두고, 원소를 하나씩 더한 뒤 그 값을 결과 리스트에 append 하세요.",
            "res = []; s = 0; for x in arr: s += x; res.append(s); return res 입니다.",
        ],
        testcases=[
            {"args": [[1, 2, 3]], "expected": [1, 3, 6]},
            {"args": [[5]], "expected": [5]},
            {"args": [[1, 1, 1, 1]], "expected": [1, 2, 3, 4]},
            {"args": [[-1, 2, -3]], "expected": [-1, 1, -2]},
            {"args": [[10, 0, 0, 5]], "expected": [10, 10, 10, 15]},
        ],
        reference_py=(
            "def solution(arr):\n"
            "    res = []\n"
            "    s = 0\n"
            "    for x in arr:\n"
            "        s += x\n"
            "        res.append(s)\n"
            "    return res\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int[] solution(int[] arr) {\n"
            "        int[] res = new int[arr.length];\n"
            "        int s = 0;\n"
            "        for (int i = 0; i < arr.length; i++) {\n"
            "            s += arr[i];\n"
            "            res[i] = s;\n"
            "        }\n"
            "        return res;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 앞에서부터의 누적합 리스트를 반환하세요.\n"
            "def solution(arr):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="bronze-31",
        rank="Bronze",
        title="숫자 삼각형",
        style="해외대기업",
        topic="반복문",
        type="stdin",
        description="N이 주어졌을 때, 첫째 줄에는 1, 둘째 줄에는 1 2, ..., N번째 줄에는 1부터 N까지를 공백으로 구분해 출력하시오.",
        input_desc="첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.",
        output_desc="i번째 줄에 1부터 i까지의 수를 공백으로 구분해 출력한다.",
        examples=[
            {"input": "3\n", "output": "1\n1 2\n1 2 3\n"},
            {"input": "1\n", "output": "1\n"},
        ],
        hints=[
            "i번째 줄에는 1부터 i까지의 수가 들어갑니다. 줄마다 출력할 수의 개수가 달라진다는 점에 주목하세요.",
            "바깥 for i in range(1, N+1) 안에서, 안쪽으로 1부터 i까지의 수를 모아 공백으로 이어 붙여 출력하세요.",
            "for i in range(1, N+1): print(' '.join(str(j) for j in range(1, i+1))) 입니다.",
        ],
        testcases=[
            {"input": "3\n", "output": "1\n1 2\n1 2 3\n"},
            {"input": "1\n", "output": "1\n"},
            {"input": "4\n", "output": "1\n1 2\n1 2 3\n1 2 3 4\n"},
            {"input": "5\n", "output": "1\n1 2\n1 2 3\n1 2 3 4\n1 2 3 4 5\n"},
        ],
        reference_py=(
            "n = int(input())\n"
            "for i in range(1, n + 1):\n"
            "    print(' '.join(str(j) for j in range(1, i + 1)))\n"
        ),
        reference_java=(
            "import java.util.Scanner;\n"
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        int n = new Scanner(System.in).nextInt();\n"
            "        StringBuilder sb = new StringBuilder();\n"
            "        for (int i = 1; i <= n; i++) {\n"
            "            for (int j = 1; j <= i; j++) {\n"
            "                if (j > 1) sb.append(' ');\n"
            "                sb.append(j);\n"
            "            }\n"
            "            sb.append('\\n');\n"
            "        }\n"
            "        System.out.print(sb);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# i번째 줄에 1부터 i까지를 공백으로 구분해 출력하세요.\n"
            "n = int(input())\n"
            "# for ...\n"
        ),
    ),

    Problem(
        id="bronze-32",
        rank="Bronze",
        title="1부터 N까지의 합",
        style="대기업",
        topic="반복문",
        type="stdin",
        description="자연수 N이 주어졌을 때, 1부터 N까지의 모든 자연수의 합을 출력하시오.",
        input_desc="첫째 줄에 자연수 N(1 ≤ N ≤ 100000)이 주어진다.",
        output_desc="1부터 N까지의 합을 출력한다.",
        examples=[
            {"input": "10\n", "output": "55\n"},
            {"input": "1\n", "output": "1\n"},
        ],
        hints=[
            "1, 2, 3, ... , N 을 차례로 더해 나가면 됩니다. 합을 담을 변수를 0으로 시작하세요.",
            "for i in range(1, N+1) 반복문 안에서 합 변수에 i를 더해 가면 됩니다.",
            "total = 0; for i in range(1, N+1): total += i; print(total) 입니다. (N*(N+1)//2 로도 가능)",
        ],
        testcases=[
            {"input": "10\n", "output": "55\n"},
            {"input": "1\n", "output": "1\n"},
            {"input": "100\n", "output": "5050\n"},
            {"input": "3\n", "output": "6\n"},
            {"input": "100000\n", "output": "5000050000\n"},
        ],
        reference_py=(
            "n = int(input())\n"
            "total = 0\n"
            "for i in range(1, n + 1):\n"
            "    total += i\n"
            "print(total)\n"
        ),
        reference_java=(
            "import java.util.Scanner;\n"
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        int n = new Scanner(System.in).nextInt();\n"
            "        long total = 0;\n"
            "        for (int i = 1; i <= n; i++) total += i;\n"
            "        System.out.println(total);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 1부터 N까지의 합을 출력하세요.\n"
            "n = int(input())\n"
            "# for ...\n"
        ),
    ),

    Problem(
        id="bronze-33",
        rank="Bronze",
        title="팩토리얼 계산",
        style="프로그래머스",
        topic="팩토리얼",
        type="func",
        func_name="solution",
        description="0 이상의 정수 n이 주어질 때, n 팩토리얼(n!) 값을 반환하는 함수 solution을 완성하세요. n!은 1부터 n까지의 모든 자연수의 곱이며, 0! = 1입니다.",
        input_desc="n : int (0 ≤ n ≤ 12)",
        output_desc="n! 값 : int",
        examples=[
            {"args": [5], "output": 120},
            {"args": [0], "output": 1},
        ],
        hints=[
            "팩토리얼은 1부터 n까지의 수를 모두 곱한 값입니다. 곱을 누적할 변수를 1로 시작하세요.",
            "result를 1로 두고, for i in range(1, n+1) 반복으로 result에 i를 곱해 나가면 됩니다. (0!은 곱이 없으므로 1)",
            "result = 1; for i in range(1, n+1): result *= i; return result 입니다.",
        ],
        testcases=[
            {"args": [5], "expected": 120},
            {"args": [0], "expected": 1},
            {"args": [1], "expected": 1},
            {"args": [10], "expected": 3628800},
            {"args": [12], "expected": 479001600},
        ],
        reference_py=(
            "def solution(n):\n"
            "    result = 1\n"
            "    for i in range(1, n + 1):\n"
            "        result *= i\n"
            "    return result\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public long solution(int n) {\n"
            "        long result = 1;\n"
            "        for (int i = 1; i <= n; i++) result *= i;\n"
            "        return result;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# n 팩토리얼(n!)을 반환하세요. (0! = 1)\n"
            "def solution(n):\n"
            "    answer = 1\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="bronze-34",
        rank="Bronze",
        title="자릿수의 합",
        style="해외대기업",
        topic="자릿수 합",
        type="func",
        func_name="solution",
        description="0 이상의 정수 n이 주어질 때, n을 이루는 각 자리 숫자의 합을 반환하는 함수 solution을 완성하세요. 예를 들어 123의 자릿수 합은 1+2+3=6입니다.",
        input_desc="n : int (0 ≤ n ≤ 1000000000)",
        output_desc="각 자리 숫자의 합 : int",
        examples=[
            {"args": [123], "output": 6},
            {"args": [9999], "output": 36},
        ],
        hints=[
            "각 자리 숫자를 하나씩 떼어내어 더해야 합니다. 숫자를 문자열로 바꾸면 자리마다 접근하기 쉽습니다.",
            "str(n) 으로 바꾼 뒤 각 문자 c를 int(c)로 바꿔 더하거나, n % 10 으로 끝자리를 떼고 n //= 10 으로 줄여 가도 됩니다.",
            "return sum(int(c) for c in str(n)) 한 줄이면 됩니다.",
        ],
        testcases=[
            {"args": [123], "expected": 6},
            {"args": [9999], "expected": 36},
            {"args": [0], "expected": 0},
            {"args": [1000], "expected": 1},
            {"args": [1000000000], "expected": 1},
        ],
        reference_py=(
            "def solution(n):\n"
            "    total = 0\n"
            "    for c in str(n):\n"
            "        total += int(c)\n"
            "    return total\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(long n) {\n"
            "        int total = 0;\n"
            "        if (n == 0) return 0;\n"
            "        while (n > 0) {\n"
            "            total += (int)(n % 10);\n"
            "            n /= 10;\n"
            "        }\n"
            "        return total;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# n의 각 자리 숫자의 합을 반환하세요.\n"
            "def solution(n):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="bronze-35",
        rank="Bronze",
        title="카운트다운 출력",
        style="백준",
        topic="반복문",
        type="stdin",
        description="자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 거꾸로 출력하시오.",
        input_desc="첫째 줄에 자연수 N(1 ≤ N ≤ 1000)이 주어진다.",
        output_desc="N부터 1까지 한 줄에 한 수씩 출력한다.",
        examples=[
            {"input": "5\n", "output": "5\n4\n3\n2\n1\n"},
            {"input": "1\n", "output": "1\n"},
        ],
        hints=[
            "N에서 시작해 1씩 줄여 가며 1이 될 때까지 출력하면 됩니다.",
            "while 문으로 변수를 N부터 시작해 출력하고 1씩 빼거나, range(N, 0, -1) 로 거꾸로 반복할 수 있습니다.",
            "i = n; while i >= 1: print(i); i -= 1 — 또는 for i in range(n, 0, -1): print(i) 입니다.",
        ],
        testcases=[
            {"input": "5\n", "output": "5\n4\n3\n2\n1\n"},
            {"input": "1\n", "output": "1\n"},
            {"input": "3\n", "output": "3\n2\n1\n"},
            {"input": "10\n", "output": "10\n9\n8\n7\n6\n5\n4\n3\n2\n1\n"},
        ],
        reference_py=(
            "n = int(input())\n"
            "i = n\n"
            "while i >= 1:\n"
            "    print(i)\n"
            "    i -= 1\n"
        ),
        reference_java=(
            "import java.util.Scanner;\n"
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        int n = new Scanner(System.in).nextInt();\n"
            "        StringBuilder sb = new StringBuilder();\n"
            "        for (int i = n; i >= 1; i--) sb.append(i).append('\\n');\n"
            "        System.out.print(sb);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# N부터 1까지 한 줄에 하나씩 거꾸로 출력하세요.\n"
            "n = int(input())\n"
            "# while ...\n"
        ),
    ),

]
