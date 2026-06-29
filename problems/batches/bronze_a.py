"""브론즈 추가 배치 A — 사칙연산 / 조건문 / 절댓값·부호 / 단위·시간 변환 등 입문~기초 15문제.

bronze-06 ~ bronze-20.
"""

from engine.models import Problem

RANK = "Bronze"

PROBLEMS = [

    Problem(
        id="bronze-06",
        rank="Bronze",
        title="사칙연산 한 번에",
        style="백준",
        topic="사칙연산",
        type="stdin",
        description="두 정수 A와 B가 주어질 때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 차례대로 한 줄씩 출력하시오.",
        input_desc="첫째 줄에 A와 B가 공백으로 구분되어 주어진다. (0 < A, B < 10000)",
        output_desc="첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B(정수 나눗셈의 몫), 다섯째 줄에 A%B를 출력한다.",
        examples=[
            {"input": "7 3\n", "output": "10\n4\n21\n2\n1\n"},
            {"input": "10 5\n", "output": "15\n5\n50\n2\n0\n"},
        ],
        hints=[
            "두 수를 받은 뒤 다섯 가지 연산 결과를 순서대로 출력하면 됩니다.",
            "정수 나눗셈의 몫은 // 연산자, 나머지는 % 연산자를 사용합니다.",
            "a, b = map(int, input().split()) 후 print(a+b); print(a-b); print(a*b); print(a//b); print(a%b) 입니다.",
        ],
        testcases=[
            {"input": "7 3\n", "output": "10\n4\n21\n2\n1\n"},
            {"input": "10 5\n", "output": "15\n5\n50\n2\n0\n"},
            {"input": "1 1\n", "output": "2\n0\n1\n1\n0\n"},
            {"input": "9999 1\n", "output": "10000\n9998\n9999\n9999\n0\n"},
            {"input": "5 7\n", "output": "12\n-2\n35\n0\n5\n"},
        ],
        reference_py=(
            "a, b = map(int, input().split())\n"
            "print(a + b)\n"
            "print(a - b)\n"
            "print(a * b)\n"
            "print(a // b)\n"
            "print(a % b)\n"
        ),
        reference_java=(
            "import java.util.Scanner;\n"
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        Scanner sc = new Scanner(System.in);\n"
            "        int a = sc.nextInt(), b = sc.nextInt();\n"
            "        System.out.println(a + b);\n"
            "        System.out.println(a - b);\n"
            "        System.out.println(a * b);\n"
            "        System.out.println(a / b);\n"
            "        System.out.println(a % b);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 사칙연산 한 번에 : 합, 차, 곱, 몫, 나머지를 한 줄씩 출력하세요.\n"
            "a, b = map(int, input().split())\n"
            "# print(...)\n"
        ),
    ),

    Problem(
        id="bronze-07",
        rank="Bronze",
        title="몫과 나머지",
        style="프로그래머스",
        topic="몫과 나머지",
        type="func",
        func_name="solution",
        description="두 정수 a, b가 주어질 때 a를 b로 나눈 몫과 나머지를 [몫, 나머지] 형태의 리스트로 반환하는 함수 solution을 완성하세요.",
        input_desc="a : int (1 ≤ a ≤ 100000), b : int (1 ≤ b ≤ 100000)",
        output_desc="[a를 b로 나눈 몫, a를 b로 나눈 나머지] 형태의 정수 리스트",
        examples=[
            {"args": [17, 5], "output": [3, 2]},
            {"args": [10, 2], "output": [5, 0]},
        ],
        hints=[
            "몫과 나머지를 각각 구해 리스트 하나에 담아 반환하면 됩니다.",
            "몫은 a // b, 나머지는 a % b 로 구할 수 있습니다.",
            "return [a // b, a % b] 한 줄이면 됩니다.",
        ],
        testcases=[
            {"args": [17, 5], "expected": [3, 2]},
            {"args": [10, 2], "expected": [5, 0]},
            {"args": [1, 100], "expected": [0, 1]},
            {"args": [100000, 7], "expected": [14285, 5]},
            {"args": [9, 9], "expected": [1, 0]},
        ],
        reference_py=(
            "def solution(a, b):\n"
            "    return [a // b, a % b]\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int[] solution(int a, int b) {\n"
            "        return new int[]{a / b, a % b};\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 몫과 나머지를 [몫, 나머지] 리스트로 반환하세요.\n"
            "def solution(a, b):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="bronze-08",
        rank="Bronze",
        title="점수로 학점 매기기",
        style="대기업",
        topic="조건문",
        type="stdin",
        description=(
            "한 학생의 점수가 주어질 때, 다음 기준에 따라 학점을 출력하시오.\n"
            "90점 이상이면 A, 80점 이상이면 B, 70점 이상이면 C, 60점 이상이면 D, 그 미만이면 F."
        ),
        input_desc="첫째 줄에 정수 점수 score가 주어진다. (0 ≤ score ≤ 100)",
        output_desc="해당하는 학점(A, B, C, D, F 중 하나)을 출력한다.",
        examples=[
            {"input": "95\n", "output": "A\n"},
            {"input": "73\n", "output": "C\n"},
        ],
        hints=[
            "점수 구간별로 학점이 정해져 있으니 큰 구간부터 차례로 따져 보세요.",
            "if / elif / else 로 90, 80, 70, 60 경계를 위에서부터 검사하면 깔끔합니다.",
            "if score>=90: print('A') elif score>=80: print('B') elif score>=70: print('C') elif score>=60: print('D') else: print('F')",
        ],
        testcases=[
            {"input": "95\n", "output": "A\n"},
            {"input": "73\n", "output": "C\n"},
            {"input": "90\n", "output": "A\n"},
            {"input": "60\n", "output": "D\n"},
            {"input": "59\n", "output": "F\n"},
            {"input": "0\n", "output": "F\n"},
            {"input": "100\n", "output": "A\n"},
        ],
        reference_py=(
            "score = int(input())\n"
            "if score >= 90:\n"
            "    print('A')\n"
            "elif score >= 80:\n"
            "    print('B')\n"
            "elif score >= 70:\n"
            "    print('C')\n"
            "elif score >= 60:\n"
            "    print('D')\n"
            "else:\n"
            "    print('F')\n"
        ),
        reference_java=(
            "import java.util.Scanner;\n"
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        int score = new Scanner(System.in).nextInt();\n"
            "        String grade;\n"
            "        if (score >= 90) grade = \"A\";\n"
            "        else if (score >= 80) grade = \"B\";\n"
            "        else if (score >= 70) grade = \"C\";\n"
            "        else if (score >= 60) grade = \"D\";\n"
            "        else grade = \"F\";\n"
            "        System.out.println(grade);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 점수를 받아 학점(A~F)을 출력하세요.\n"
            "score = int(input())\n"
            "# if ...\n"
        ),
    ),

    Problem(
        id="bronze-09",
        rank="Bronze",
        title="윤년 판별",
        style="백준",
        topic="조건문",
        type="stdin",
        description=(
            "연도 year가 주어질 때 윤년이면 1, 평년이면 0을 출력하시오.\n"
            "윤년은 4로 나누어떨어지면서 100으로 나누어떨어지지 않거나, 400으로 나누어떨어지는 해이다."
        ),
        input_desc="첫째 줄에 연도 year가 주어진다. (1 ≤ year ≤ 4000)",
        output_desc="윤년이면 1, 평년이면 0을 출력한다.",
        examples=[
            {"input": "2000\n", "output": "1\n"},
            {"input": "1900\n", "output": "0\n"},
        ],
        hints=[
            "윤년 규칙을 그대로 조건식으로 옮기면 됩니다. '4의 배수이면서 100의 배수가 아님' 또는 '400의 배수'.",
            "나누어떨어지는지는 % 연산자로 확인하고, and / or 로 두 조건을 묶습니다.",
            "leap = (year%4==0 and year%100!=0) or (year%400==0); print(1 if leap else 0)",
        ],
        testcases=[
            {"input": "2000\n", "output": "1\n"},
            {"input": "1900\n", "output": "0\n"},
            {"input": "2024\n", "output": "1\n"},
            {"input": "2023\n", "output": "0\n"},
            {"input": "2100\n", "output": "0\n"},
            {"input": "4\n", "output": "1\n"},
            {"input": "1\n", "output": "0\n"},
        ],
        reference_py=(
            "year = int(input())\n"
            "leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)\n"
            "print(1 if leap else 0)\n"
        ),
        reference_java=(
            "import java.util.Scanner;\n"
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        int year = new Scanner(System.in).nextInt();\n"
            "        boolean leap = (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);\n"
            "        System.out.println(leap ? 1 : 0);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 윤년이면 1, 평년이면 0을 출력하세요.\n"
            "year = int(input())\n"
            "# print(...)\n"
        ),
    ),

    Problem(
        id="bronze-10",
        rank="Bronze",
        title="사분면 고르기",
        style="백준",
        topic="조건문",
        type="stdin",
        description=(
            "좌표평면 위의 점 (x, y)가 어느 사분면에 속하는지 출력하시오.\n"
            "x>0, y>0이면 1사분면, x<0, y>0이면 2사분면, x<0, y<0이면 3사분면, x>0, y<0이면 4사분면이다.\n"
            "x와 y는 모두 0이 아니다."
        ),
        input_desc="첫째 줄에 x, 둘째 줄에 y가 주어진다. (-1000 ≤ x, y ≤ 1000, x≠0, y≠0)",
        output_desc="점이 속한 사분면의 번호(1, 2, 3, 4 중 하나)를 출력한다.",
        examples=[
            {"input": "12\n5\n", "output": "1\n"},
            {"input": "9\n-13\n", "output": "4\n"},
        ],
        hints=[
            "x의 부호와 y의 부호 조합으로 사분면이 결정됩니다.",
            "x>0인지, y>0인지를 각각 판단한 뒤 네 경우로 나누는 if문을 작성하세요.",
            "if x>0: print(1 if y>0 else 4) else: print(2 if y>0 else 3)",
        ],
        testcases=[
            {"input": "12\n5\n", "output": "1\n"},
            {"input": "9\n-13\n", "output": "4\n"},
            {"input": "-5\n8\n", "output": "2\n"},
            {"input": "-7\n-3\n", "output": "3\n"},
            {"input": "1\n1\n", "output": "1\n"},
            {"input": "-1\n-1\n", "output": "3\n"},
        ],
        reference_py=(
            "x = int(input())\n"
            "y = int(input())\n"
            "if x > 0:\n"
            "    print(1 if y > 0 else 4)\n"
            "else:\n"
            "    print(2 if y > 0 else 3)\n"
        ),
        reference_java=(
            "import java.util.Scanner;\n"
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        Scanner sc = new Scanner(System.in);\n"
            "        int x = sc.nextInt(), y = sc.nextInt();\n"
            "        if (x > 0) System.out.println(y > 0 ? 1 : 4);\n"
            "        else System.out.println(y > 0 ? 2 : 3);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 점 (x, y)가 속한 사분면 번호를 출력하세요.\n"
            "x = int(input())\n"
            "y = int(input())\n"
            "# print(...)\n"
        ),
    ),

    Problem(
        id="bronze-11",
        rank="Bronze",
        title="세 수 중 최댓값",
        style="해외대기업",
        topic="조건문",
        type="func",
        func_name="solution",
        description="세 정수 a, b, c가 주어질 때 그 중 가장 큰 값을 반환하는 함수 solution을 완성하세요.",
        input_desc="a, b, c : int (-100000 ≤ a, b, c ≤ 100000)",
        output_desc="세 값 중 가장 큰 정수",
        examples=[
            {"args": [3, 7, 5], "output": 7},
            {"args": [-1, -5, -2], "output": -1},
        ],
        hints=[
            "세 값을 비교해 가장 큰 것을 고르면 됩니다.",
            "파이썬 내장 함수 max는 여러 인자를 받아 그 중 최댓값을 돌려줍니다.",
            "return max(a, b, c) 한 줄이면 됩니다.",
        ],
        testcases=[
            {"args": [3, 7, 5], "expected": 7},
            {"args": [-1, -5, -2], "expected": -1},
            {"args": [10, 10, 10], "expected": 10},
            {"args": [100000, 0, -100000], "expected": 100000},
            {"args": [4, 9, 9], "expected": 9},
        ],
        reference_py=(
            "def solution(a, b, c):\n"
            "    return max(a, b, c)\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int a, int b, int c) {\n"
            "        return Math.max(a, Math.max(b, c));\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 세 수 중 가장 큰 값을 반환하세요.\n"
            "def solution(a, b, c):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="bronze-12",
        rank="Bronze",
        title="절댓값 구하기",
        style="프로그래머스",
        topic="절댓값",
        type="func",
        func_name="solution",
        description=(
            "정수 n이 주어질 때 n의 절댓값을 반환하는 함수 solution을 완성하세요.\n"
            "절댓값은 음수면 부호를 없앤 값, 0 이상이면 그대로의 값입니다. (내장 abs 사용 금지를 가정하고 직접 구현해도 됩니다.)"
        ),
        input_desc="n : int (-1000000 ≤ n ≤ 1000000)",
        output_desc="n의 절댓값(0 이상의 정수)",
        examples=[
            {"args": [-7], "output": 7},
            {"args": [5], "output": 5},
        ],
        hints=[
            "n이 음수일 때만 부호를 바꿔 주면 됩니다.",
            "조건문으로 n<0인지 확인하고, 그렇다면 -n을 반환하세요.",
            "return -n if n < 0 else n (또는 return abs(n))",
        ],
        testcases=[
            {"args": [-7], "expected": 7},
            {"args": [5], "expected": 5},
            {"args": [0], "expected": 0},
            {"args": [-1000000], "expected": 1000000},
            {"args": [1000000], "expected": 1000000},
        ],
        reference_py=(
            "def solution(n):\n"
            "    return -n if n < 0 else n\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int n) {\n"
            "        return n < 0 ? -n : n;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# n의 절댓값을 반환하세요.\n"
            "def solution(n):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="bronze-13",
        rank="Bronze",
        title="부호 판별",
        style="대기업",
        topic="부호 판별",
        type="func",
        func_name="solution",
        description=(
            "정수 n이 주어질 때 양수면 1, 0이면 0, 음수면 -1을 반환하는 함수 solution을 완성하세요."
        ),
        input_desc="n : int (-1000000 ≤ n ≤ 1000000)",
        output_desc="n이 양수면 1, 0이면 0, 음수면 -1",
        examples=[
            {"args": [42], "output": 1},
            {"args": [-3], "output": -1},
        ],
        hints=[
            "값이 0보다 큰지, 작은지, 같은지 세 경우로 나눠 생각하세요.",
            "if / elif / else 로 n > 0, n < 0, 나머지(0)를 구분하면 됩니다.",
            "if n > 0: return 1 elif n < 0: return -1 else: return 0",
        ],
        testcases=[
            {"args": [42], "expected": 1},
            {"args": [-3], "expected": -1},
            {"args": [0], "expected": 0},
            {"args": [1000000], "expected": 1},
            {"args": [-1000000], "expected": -1},
        ],
        reference_py=(
            "def solution(n):\n"
            "    if n > 0:\n"
            "        return 1\n"
            "    elif n < 0:\n"
            "        return -1\n"
            "    else:\n"
            "        return 0\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int n) {\n"
            "        if (n > 0) return 1;\n"
            "        else if (n < 0) return -1;\n"
            "        else return 0;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 양수면 1, 0이면 0, 음수면 -1을 반환하세요.\n"
            "def solution(n):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="bronze-14",
        rank="Bronze",
        title="두 수 교환",
        style="백준",
        topic="변수 교환",
        type="stdin",
        description=(
            "두 정수 A와 B가 주어질 때, 두 값을 서로 바꿔서 출력하시오.\n"
            "즉 입력으로 A B가 들어오면 B A 순서로 출력한다."
        ),
        input_desc="첫째 줄에 A와 B가 공백으로 구분되어 주어진다. (-10000 ≤ A, B ≤ 10000)",
        output_desc="B와 A를 공백으로 구분하여 한 줄에 출력한다.",
        examples=[
            {"input": "3 8\n", "output": "8 3\n"},
            {"input": "-2 5\n", "output": "5 -2\n"},
        ],
        hints=[
            "출력 순서만 바꾸면 되는 문제입니다.",
            "파이썬에서는 a, b = b, a 처럼 한 줄로 두 변수를 교환할 수 있습니다.",
            "a, b = map(int, input().split()); a, b = b, a; print(a, b)",
        ],
        testcases=[
            {"input": "3 8\n", "output": "8 3\n"},
            {"input": "-2 5\n", "output": "5 -2\n"},
            {"input": "0 0\n", "output": "0 0\n"},
            {"input": "10000 -10000\n", "output": "-10000 10000\n"},
            {"input": "7 7\n", "output": "7 7\n"},
        ],
        reference_py=(
            "a, b = map(int, input().split())\n"
            "a, b = b, a\n"
            "print(a, b)\n"
        ),
        reference_java=(
            "import java.util.Scanner;\n"
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        Scanner sc = new Scanner(System.in);\n"
            "        int a = sc.nextInt(), b = sc.nextInt();\n"
            "        int t = a; a = b; b = t;\n"
            "        System.out.println(a + \" \" + b);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 두 수를 서로 바꿔 출력하세요.\n"
            "a, b = map(int, input().split())\n"
            "# print(...)\n"
        ),
    ),

    Problem(
        id="bronze-15",
        rank="Bronze",
        title="초를 시분초로",
        style="해외대기업",
        topic="시간 변환",
        type="func",
        func_name="solution",
        description=(
            "총 시간을 나타내는 초 단위 정수 total이 주어질 때, 이를 시(h), 분(m), 초(s)로 변환하여 "
            "[시, 분, 초] 형태의 리스트로 반환하는 함수 solution을 완성하세요.\n"
            "1분은 60초, 1시간은 3600초입니다."
        ),
        input_desc="total : int (0 ≤ total ≤ 1000000), 초 단위 시간",
        output_desc="[시, 분, 초] 형태의 정수 리스트 (분과 초는 0~59 범위)",
        examples=[
            {"args": [3661], "output": [1, 1, 1]},
            {"args": [59], "output": [0, 0, 59]},
        ],
        hints=[
            "전체 초를 3600으로, 그 다음 60으로 나눠가며 단위를 떼어내면 됩니다.",
            "몫(//)과 나머지(%)를 활용하세요. 시 = total // 3600, 남은 초 = total % 3600.",
            "h = total//3600; m = (total%3600)//60; s = total%60; return [h, m, s]",
        ],
        testcases=[
            {"args": [3661], "expected": [1, 1, 1]},
            {"args": [59], "expected": [0, 0, 59]},
            {"args": [0], "expected": [0, 0, 0]},
            {"args": [3600], "expected": [1, 0, 0]},
            {"args": [7325], "expected": [2, 2, 5]},
            {"args": [86399], "expected": [23, 59, 59]},
        ],
        reference_py=(
            "def solution(total):\n"
            "    h = total // 3600\n"
            "    m = (total % 3600) // 60\n"
            "    s = total % 60\n"
            "    return [h, m, s]\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int[] solution(int total) {\n"
            "        int h = total / 3600;\n"
            "        int m = (total % 3600) / 60;\n"
            "        int s = total % 60;\n"
            "        return new int[]{h, m, s};\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 초 단위 시간을 [시, 분, 초] 리스트로 변환하세요.\n"
            "def solution(total):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="bronze-16",
        rank="Bronze",
        title="킬로미터를 미터로",
        style="프로그래머스",
        topic="단위 변환",
        type="func",
        func_name="solution",
        description=(
            "거리를 킬로미터(km)와 추가 미터(m)로 나타낸 두 정수 km, m이 주어질 때, "
            "전체 거리를 미터 단위 정수로 환산해 반환하는 함수 solution을 완성하세요.\n"
            "1킬로미터는 1000미터입니다."
        ),
        input_desc="km : int (0 ≤ km ≤ 100000), m : int (0 ≤ m ≤ 100000)",
        output_desc="전체 거리(미터 단위 정수)",
        examples=[
            {"args": [2, 300], "output": 2300},
            {"args": [0, 500], "output": 500},
        ],
        hints=[
            "킬로미터를 미터로 바꾼 뒤 추가 미터를 더하면 됩니다.",
            "1km = 1000m 이므로 km에 1000을 곱한 값에 m을 더하세요.",
            "return km * 1000 + m 한 줄이면 됩니다.",
        ],
        testcases=[
            {"args": [2, 300], "expected": 2300},
            {"args": [0, 500], "expected": 500},
            {"args": [0, 0], "expected": 0},
            {"args": [100000, 100000], "expected": 100100000},
            {"args": [5, 0], "expected": 5000},
        ],
        reference_py=(
            "def solution(km, m):\n"
            "    return km * 1000 + m\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int km, int m) {\n"
            "        return km * 1000 + m;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# km와 m를 받아 전체 거리를 미터 단위로 반환하세요.\n"
            "def solution(km, m):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="bronze-17",
        rank="Bronze",
        title="이름표 출력",
        style="백준",
        topic="입출력 포맷팅",
        type="stdin",
        description=(
            "이름 name과 나이 age가 주어질 때, \"name(age세)\" 형식으로 한 줄에 출력하시오.\n"
            "예를 들어 name이 Kim, age가 20이면 Kim(20세) 를 출력한다."
        ),
        input_desc="첫째 줄에 이름 name(공백 없는 문자열), 둘째 줄에 정수 나이 age가 주어진다. (0 ≤ age ≤ 150)",
        output_desc="\"name(age세)\" 형식의 문자열을 한 줄에 출력한다.",
        examples=[
            {"input": "Kim\n20\n", "output": "Kim(20세)\n"},
            {"input": "Lee\n7\n", "output": "Lee(7세)\n"},
        ],
        hints=[
            "이름과 나이를 정해진 형식의 한 문자열로 합쳐서 출력하면 됩니다.",
            "f-string을 쓰면 f\"{name}({age}세)\" 처럼 값을 끼워 넣을 수 있습니다.",
            "name = input(); age = input(); print(f\"{name}({age}세)\")",
        ],
        testcases=[
            {"input": "Kim\n20\n", "output": "Kim(20세)\n"},
            {"input": "Lee\n7\n", "output": "Lee(7세)\n"},
            {"input": "Park\n0\n", "output": "Park(0세)\n"},
            {"input": "Choi\n150\n", "output": "Choi(150세)\n"},
            {"input": "a\n99\n", "output": "a(99세)\n"},
        ],
        reference_py=(
            "name = input().strip()\n"
            "age = input().strip()\n"
            "print(f\"{name}({age}세)\")\n"
        ),
        reference_java=(
            "import java.util.Scanner;\n"
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        Scanner sc = new Scanner(System.in);\n"
            "        String name = sc.next();\n"
            "        int age = sc.nextInt();\n"
            "        System.out.println(name + \"(\" + age + \"세)\");\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 이름과 나이를 받아 \"name(age세)\" 형식으로 출력하세요.\n"
            "name = input().strip()\n"
            "age = input().strip()\n"
            "# print(...)\n"
        ),
    ),

    Problem(
        id="bronze-18",
        rank="Bronze",
        title="두 수 비교하기",
        style="백준",
        topic="비교 연산",
        type="stdin",
        description=(
            "두 정수 A와 B가 주어질 때, 다음을 출력하시오.\n"
            "A가 B보다 크면 '>', A가 B보다 작으면 '<', 둘이 같으면 '==' 를 출력한다."
        ),
        input_desc="첫째 줄에 A와 B가 공백으로 구분되어 주어진다. (-10000 ≤ A, B ≤ 10000)",
        output_desc="A와 B의 관계에 따라 '>', '<', '==' 중 하나를 출력한다.",
        examples=[
            {"input": "1 2\n", "output": "<\n"},
            {"input": "5 5\n", "output": "==\n"},
        ],
        hints=[
            "A와 B의 대소 관계는 세 가지(크다/작다/같다)뿐입니다.",
            "if / elif / else 로 A > B, A < B, 나머지(같음)를 구분하세요.",
            "if a > b: print('>') elif a < b: print('<') else: print('==')",
        ],
        testcases=[
            {"input": "1 2\n", "output": "<\n"},
            {"input": "5 5\n", "output": "==\n"},
            {"input": "10 3\n", "output": ">\n"},
            {"input": "-5 -5\n", "output": "==\n"},
            {"input": "-10000 10000\n", "output": "<\n"},
            {"input": "0 -1\n", "output": ">\n"},
        ],
        reference_py=(
            "a, b = map(int, input().split())\n"
            "if a > b:\n"
            "    print('>')\n"
            "elif a < b:\n"
            "    print('<')\n"
            "else:\n"
            "    print('==')\n"
        ),
        reference_java=(
            "import java.util.Scanner;\n"
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        Scanner sc = new Scanner(System.in);\n"
            "        int a = sc.nextInt(), b = sc.nextInt();\n"
            "        if (a > b) System.out.println(\">\");\n"
            "        else if (a < b) System.out.println(\"<\");\n"
            "        else System.out.println(\"==\");\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 두 수를 비교해 '>', '<', '==' 중 하나를 출력하세요.\n"
            "a, b = map(int, input().split())\n"
            "# if ...\n"
        ),
    ),

    Problem(
        id="bronze-19",
        rank="Bronze",
        title="세 과목 평균",
        style="대기업",
        topic="사칙연산",
        type="func",
        func_name="solution",
        description=(
            "세 과목 점수 a, b, c가 주어질 때 세 점수의 평균을 정수(소수점 이하 버림)로 반환하는 함수 solution을 완성하세요."
        ),
        input_desc="a, b, c : int (0 ≤ a, b, c ≤ 100)",
        output_desc="세 점수 평균의 정수 부분(소수점 이하 버림)",
        examples=[
            {"args": [90, 80, 70], "output": 80},
            {"args": [100, 100, 99], "output": 99},
        ],
        hints=[
            "세 점수를 더한 뒤 3으로 나누면 평균입니다. 소수점 이하는 버려야 합니다.",
            "합을 구한 뒤 정수 나눗셈 // 3 을 쓰면 소수점 이하가 자동으로 버려집니다.",
            "return (a + b + c) // 3 한 줄이면 됩니다.",
        ],
        testcases=[
            {"args": [90, 80, 70], "expected": 80},
            {"args": [100, 100, 99], "expected": 99},
            {"args": [0, 0, 0], "expected": 0},
            {"args": [100, 100, 100], "expected": 100},
            {"args": [50, 51, 52], "expected": 51},
            {"args": [1, 1, 2], "expected": 1},
        ],
        reference_py=(
            "def solution(a, b, c):\n"
            "    return (a + b + c) // 3\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int a, int b, int c) {\n"
            "        return (a + b + c) / 3;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 세 점수의 평균(소수점 이하 버림)을 반환하세요.\n"
            "def solution(a, b, c):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="bronze-20",
        rank="Bronze",
        title="거스름돈 동전 개수",
        style="해외대기업",
        topic="몫과 나머지",
        type="stdin",
        description=(
            "거스름돈 금액 N원이 주어질 때, 500원, 100원, 50원, 10원짜리 동전을 사용하여 "
            "동전의 개수가 최소가 되도록 거슬러 줄 때 필요한 동전의 총 개수를 출력하시오.\n"
            "N은 항상 10으로 나누어떨어진다."
        ),
        input_desc="첫째 줄에 거스름돈 금액 N이 주어진다. (0 ≤ N ≤ 1000000, N은 10의 배수)",
        output_desc="필요한 동전의 최소 총 개수를 출력한다.",
        examples=[
            {"input": "660\n", "output": "4\n"},
            {"input": "1000\n", "output": "2\n"},
        ],
        hints=[
            "큰 단위 동전부터 최대한 많이 사용하는 것이 동전 개수를 최소로 만드는 방법입니다.",
            "각 동전 금액으로 나눈 몫(//)이 그 동전의 개수이고, 나머지(%)를 다음 동전으로 넘기면 됩니다.",
            "for coin in [500,100,50,10]: count += N//coin; N %= coin 후 count 출력.",
        ],
        testcases=[
            {"input": "660\n", "output": "4\n"},
            {"input": "1000\n", "output": "2\n"},
            {"input": "0\n", "output": "0\n"},
            {"input": "10\n", "output": "1\n"},
            {"input": "1000000\n", "output": "2000\n"},
            {"input": "1230\n", "output": "7\n"},
        ],
        reference_py=(
            "n = int(input())\n"
            "count = 0\n"
            "for coin in (500, 100, 50, 10):\n"
            "    count += n // coin\n"
            "    n %= coin\n"
            "print(count)\n"
        ),
        reference_java=(
            "import java.util.Scanner;\n"
            "public class Main {\n"
            "    public static void main(String[] args) {\n"
            "        int n = new Scanner(System.in).nextInt();\n"
            "        int[] coins = {500, 100, 50, 10};\n"
            "        int count = 0;\n"
            "        for (int coin : coins) {\n"
            "            count += n / coin;\n"
            "            n %= coin;\n"
            "        }\n"
            "        System.out.println(count);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 500/100/50/10원 동전으로 거슬러 줄 때 최소 동전 개수를 출력하세요.\n"
            "n = int(input())\n"
            "# ...\n"
        ),
    ),

]
