"""실버 랭크 배치 B — 스택 / 큐·덱 / 해시 / 우선순위 큐 기초.

silver-21 ~ silver-35 (15문제). base 및 다른 배치와 주제 중복 금지.
"""

from engine.models import Problem

RANK = "Silver"

PROBLEMS = [

    # ============================ 스택 ============================
    Problem(
        id="silver-21",
        rank="Silver",
        title="쇠막대기 자르기",
        style="백준",
        topic="스택",
        type="stdin",
        description=(
            "여러 개의 쇠막대기가 레이저로 잘린다. 쇠막대기와 레이저는 괄호로 표현된다. "
            "마주 보는 두 개의 '(' 와 ')' 가 하나의 쇠막대기를 나타내고, 인접한 '(' 와 ')' "
            "즉 '()' 는 레이저를 나타낸다. 레이저는 모든 쇠막대기를 절단한다. "
            "잘린 쇠막대기 조각의 총 개수를 구하시오."
        ),
        input_desc=(
            "첫째 줄에 '(' 와 ')' 로만 이루어진 문자열이 주어진다. 길이는 짝수이고 "
            "2 이상 100000 이하이며, 항상 올바른 괄호 표현이다."
        ),
        output_desc="잘린 쇠막대기 조각의 총 개수를 출력한다.",
        examples=[
            {"input": "()(((()())(())()))(())\n", "output": "17\n"},
            {"input": "(())\n", "output": "2\n"},
        ],
        hints=[
            "여는 괄호를 만나면 아직 닫히지 않은 쇠막대기가 하나 늘어난다고 생각해 보세요. 닫는 괄호가 레이저인지 막대기 끝인지 구분이 필요합니다.",
            "스택을 사용하세요. 직전 문자가 '(' 인 ')' 는 레이저이고, 현재 스택에 쌓인 막대기 수만큼 조각이 늘어납니다. 직전 문자가 ')' 인 ')' 는 막대기의 오른쪽 끝이라 조각이 1 늘어납니다.",
            "for i,c in enumerate(s): '(' 면 push, ')' 면 pop 후 — s[i-1]=='(' 면 ans+=len(stack), 아니면 ans+=1.",
        ],
        testcases=[
            {"input": "()(((()())(())()))(())\n", "output": "17\n"},
            {"input": "(())\n", "output": "2\n"},
            {"input": "()()\n", "output": "0\n"},
            {"input": "((()()))\n", "output": "6\n"},
            {"input": "()\n", "output": "0\n"},
        ],
        reference_py=(
            "import sys\n"
            "s = sys.stdin.readline().strip()\n"
            "stack = []\n"
            "ans = 0\n"
            "for i, c in enumerate(s):\n"
            "    if c == '(':\n"
            "        stack.append(c)\n"
            "    else:\n"
            "        stack.pop()\n"
            "        if s[i - 1] == '(':\n"
            "            ans += len(stack)\n"
            "        else:\n"
            "            ans += 1\n"
            "print(ans)\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        String s = br.readLine().trim();\n"
            "        Deque<Character> stack = new ArrayDeque<>();\n"
            "        long ans = 0;\n"
            "        for (int i = 0; i < s.length(); i++) {\n"
            "            char c = s.charAt(i);\n"
            "            if (c == '(') stack.push(c);\n"
            "            else {\n"
            "                stack.pop();\n"
            "                if (s.charAt(i - 1) == '(') ans += stack.size();\n"
            "                else ans += 1;\n"
            "            }\n"
            "        }\n"
            "        System.out.println(ans);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "s = sys.stdin.readline().strip()\n"
            "# 스택으로 레이저와 막대기 끝을 구분하며 조각 수를 세어 보세요.\n"
            "stack = []\n"
            "ans = 0\n"
            "# ...\n"
            "print(ans)\n"
        ),
    ),

    Problem(
        id="silver-22",
        rank="Silver",
        title="후위 표기식 간단 계산",
        style="백준",
        topic="스택",
        type="stdin",
        description=(
            "피연산자가 모두 한 자리 숫자(0~9)인 후위 표기식이 주어진다. 연산자는 "
            "'+', '-', '*' 세 가지뿐이다. 이 식을 계산한 결과를 출력하시오. "
            "(나눗셈은 없으므로 결과는 항상 정수이다.)"
        ),
        input_desc=(
            "첫째 줄에 후위 표기식 문자열이 주어진다. 한 자리 숫자와 '+', '-', '*' 로만 "
            "이루어지며, 항상 올바른 후위 표기식이다. 길이는 1 이상 100 이하이다."
        ),
        output_desc="식을 계산한 결과(정수)를 출력한다.",
        examples=[
            {"input": "34+5*\n", "output": "35\n"},
            {"input": "23*4+\n", "output": "10\n"},
        ],
        hints=[
            "왼쪽부터 한 글자씩 읽으면서, 숫자는 어딘가에 보관해 두고 연산자를 만나면 보관해 둔 값 두 개를 꺼내 계산합니다.",
            "스택을 쓰세요. 숫자면 push, 연산자면 두 번 pop 한 뒤(먼저 꺼낸 것이 오른쪽 피연산자) 계산해서 다시 push 합니다.",
            "for c in expr: c.isdigit() 면 stack.append(int(c)); 아니면 b=stack.pop(); a=stack.pop(); '+'/'-'/'*' 에 맞춰 a?b 를 push. 마지막에 stack[0] 출력.",
        ],
        testcases=[
            {"input": "34+5*\n", "output": "35\n"},
            {"input": "23*4+\n", "output": "10\n"},
            {"input": "12+3+\n", "output": "6\n"},
            {"input": "52-\n", "output": "3\n"},
            {"input": "9\n", "output": "9\n"},
        ],
        reference_py=(
            "import sys\n"
            "expr = sys.stdin.readline().strip()\n"
            "stack = []\n"
            "for c in expr:\n"
            "    if c.isdigit():\n"
            "        stack.append(int(c))\n"
            "    else:\n"
            "        b = stack.pop()\n"
            "        a = stack.pop()\n"
            "        if c == '+':\n"
            "            stack.append(a + b)\n"
            "        elif c == '-':\n"
            "            stack.append(a - b)\n"
            "        else:\n"
            "            stack.append(a * b)\n"
            "print(stack[0])\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        String expr = br.readLine().trim();\n"
            "        Deque<Integer> stack = new ArrayDeque<>();\n"
            "        for (char c : expr.toCharArray()) {\n"
            "            if (Character.isDigit(c)) stack.push(c - '0');\n"
            "            else {\n"
            "                int b = stack.pop(), a = stack.pop();\n"
            "                if (c == '+') stack.push(a + b);\n"
            "                else if (c == '-') stack.push(a - b);\n"
            "                else stack.push(a * b);\n"
            "            }\n"
            "        }\n"
            "        System.out.println(stack.pop());\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "expr = sys.stdin.readline().strip()\n"
            "stack = []\n"
            "# 숫자는 push, 연산자는 두 번 pop 해서 계산\n"
            "# ...\n"
            "print(stack[0])\n"
        ),
    ),

    Problem(
        id="silver-23",
        rank="Silver",
        title="탑에서 쏜 레이저 수신",
        style="대기업",
        topic="스택",
        type="stdin",
        description=(
            "일렬로 늘어선 N개의 탑이 있다. 각 탑은 왼쪽으로 레이저 신호를 발사하고, "
            "신호는 자신보다 높은 탑 중 가장 가까운 탑에서 수신된다. 각 탑이 쏜 신호를 "
            "수신하는 탑의 번호를 구하시오. 어떤 탑도 수신하지 못하면 0이다."
        ),
        input_desc=(
            "첫째 줄에 탑의 수 N(1 ≤ N ≤ 100000), 둘째 줄에 탑의 높이가 왼쪽부터 "
            "공백으로 구분되어 주어진다. 높이는 1 이상 100000000 이하의 정수이다."
        ),
        output_desc="각 탑이 쏜 레이저를 수신하는 탑의 번호(1-based)를 공백으로 구분해 출력한다.",
        examples=[
            {"input": "5\n6 9 5 7 4\n", "output": "0 0 2 2 4\n"},
            {"input": "3\n3 2 1\n", "output": "0 1 2\n"},
        ],
        hints=[
            "각 탑마다 자기보다 왼쪽에 있으면서 더 높은 가장 가까운 탑을 찾아야 합니다. 모든 쌍을 비교하면 느립니다.",
            "스택에 (높이, 번호) 를 쌓되, 현재 탑보다 낮거나 같은 탑은 더 이상 누구의 수신탑도 될 수 없으니 pop 하세요. 남은 스택의 top 이 답입니다. (단조 스택)",
            "for i,h: while stack and stack[-1][0] < h: stack.pop(); ans = stack[-1][1] if stack else 0; stack.append((h,i)).",
        ],
        testcases=[
            {"input": "5\n6 9 5 7 4\n", "output": "0 0 2 2 4\n"},
            {"input": "3\n3 2 1\n", "output": "0 1 2\n"},
            {"input": "1\n10\n", "output": "0\n"},
            {"input": "4\n1 2 3 4\n", "output": "0 0 0 0\n"},
            {"input": "6\n1 5 2 4 3 6\n", "output": "0 0 2 2 4 0\n"},
        ],
        reference_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "n = int(input())\n"
            "heights = list(map(int, input().split()))\n"
            "stack = []\n"
            "ans = []\n"
            "for i, h in enumerate(heights, start=1):\n"
            "    while stack and stack[-1][0] < h:\n"
            "        stack.pop()\n"
            "    ans.append(stack[-1][1] if stack else 0)\n"
            "    stack.append((h, i))\n"
            "print(' '.join(map(str, ans)))\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        int n = Integer.parseInt(br.readLine().trim());\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int[] h = new int[n + 1];\n"
            "        for (int i = 1; i <= n; i++) h[i] = Integer.parseInt(st.nextToken());\n"
            "        Deque<int[]> stack = new ArrayDeque<>();\n"
            "        StringBuilder sb = new StringBuilder();\n"
            "        for (int i = 1; i <= n; i++) {\n"
            "            while (!stack.isEmpty() && stack.peek()[0] < h[i]) stack.pop();\n"
            "            sb.append(stack.isEmpty() ? 0 : stack.peek()[1]).append(' ');\n"
            "            stack.push(new int[]{h[i], i});\n"
            "        }\n"
            "        System.out.println(sb.toString().trim());\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "n = int(input())\n"
            "heights = list(map(int, input().split()))\n"
            "# 단조 스택으로 왼쪽의 가장 가까운 높은 탑 번호를 구하세요.\n"
            "# ...\n"
        ),
    ),

    Problem(
        id="silver-24",
        rank="Silver",
        title="오큰수 찾기",
        style="해외대기업",
        topic="스택",
        type="func",
        func_name="solution",
        description=(
            "정수 배열 nums 가 주어진다. 각 원소에 대해 오른쪽에 있으면서 그 원소보다 큰 "
            "수 중 가장 왼쪽(가장 가까운)에 있는 수를 '오큰수'라 한다. 각 원소의 오큰수를 "
            "구해 리스트로 반환하세요. 오큰수가 없으면 -1 로 채웁니다."
        ),
        input_desc="nums : 정수 리스트 (1 ≤ len(nums) ≤ 100000)",
        output_desc="각 원소의 오큰수를 담은 리스트 (없으면 -1)",
        examples=[
            {"args": [[3, 5, 2, 7]], "output": [5, 7, 7, -1]},
            {"args": [[9, 5, 4, 8]], "output": [-1, 8, 8, -1]},
        ],
        hints=[
            "각 원소마다 오른쪽을 끝까지 훑으면 O(N^2) 입니다. 아직 오큰수를 찾지 못한 원소들을 모아 두었다가 한꺼번에 처리하는 방법을 생각해 보세요.",
            "인덱스를 담는 스택을 쓰세요. 현재 수가 스택 top 위치의 수보다 크면, 그 위치의 오큰수가 바로 현재 수입니다. 조건을 만족하는 동안 pop 하며 채웁니다.",
            "ans=[-1]*n; stack=[]; for i in range(n): while stack and nums[stack[-1]]<nums[i]: ans[stack.pop()]=nums[i]; stack.append(i).",
        ],
        testcases=[
            {"args": [[3, 5, 2, 7]], "expected": [5, 7, 7, -1]},
            {"args": [[9, 5, 4, 8]], "expected": [-1, 8, 8, -1]},
            {"args": [[1, 2, 3, 4]], "expected": [2, 3, 4, -1]},
            {"args": [[5]], "expected": [-1]},
            {"args": [[3, 3, 3]], "expected": [-1, -1, -1]},
        ],
        reference_py=(
            "def solution(nums):\n"
            "    n = len(nums)\n"
            "    ans = [-1] * n\n"
            "    stack = []\n"
            "    for i in range(n):\n"
            "        while stack and nums[stack[-1]] < nums[i]:\n"
            "            ans[stack.pop()] = nums[i]\n"
            "        stack.append(i)\n"
            "    return ans\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int[] solution(int[] nums) {\n"
            "        int n = nums.length;\n"
            "        int[] ans = new int[n];\n"
            "        Arrays.fill(ans, -1);\n"
            "        Deque<Integer> stack = new ArrayDeque<>();\n"
            "        for (int i = 0; i < n; i++) {\n"
            "            while (!stack.isEmpty() && nums[stack.peek()] < nums[i])\n"
            "                ans[stack.pop()] = nums[i];\n"
            "            stack.push(i);\n"
            "        }\n"
            "        return ans;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 각 원소의 오큰수를 리스트로 반환 (없으면 -1)\n"
            "def solution(nums):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

    # ============================ 큐 · 덱 ============================
    Problem(
        id="silver-25",
        rank="Silver",
        title="요세푸스 순열",
        style="백준",
        topic="큐",
        type="stdin",
        description=(
            "1번부터 N번까지 N명이 원을 이루어 앉아 있다. 임의의 양의 정수 K가 주어질 때, "
            "1번부터 순서대로 K번째 사람을 차례로 제거한다. 한 사람이 제거되면 남은 사람들로 "
            "이루어진 원을 따라 이 과정을 반복한다. 제거되는 순서를 (N, K)-요세푸스 순열이라 "
            "한다. 이 순열을 출력하시오."
        ),
        input_desc="첫째 줄에 N과 K가 공백으로 주어진다. (1 ≤ K ≤ N ≤ 5000)",
        output_desc="요세푸스 순열을 예시 형식대로 출력한다. 예) <3, 6, 2, 7, 5, 1, 4>",
        examples=[
            {"input": "7 3\n", "output": "<3, 6, 2, 7, 5, 1, 4>\n"},
            {"input": "5 2\n", "output": "<2, 4, 1, 5, 3>\n"},
        ],
        hints=[
            "사람들을 원형으로 다루어야 합니다. 맨 앞 사람을 뒤로 보내는 동작을 반복하면 원을 회전시키는 효과가 납니다.",
            "덱(deque)을 쓰세요. K-1명을 앞에서 빼 뒤로 보낸 뒤, 그 다음 사람을 제거하면 됩니다. q.rotate(-(K-1)) 후 popleft() 가 깔끔합니다.",
            "from collections import deque; q=deque(range(1,n+1)); while q: q.rotate(-(k-1)); res.append(q.popleft()). 출력은 '<' + ', '.join(...) + '>'.",
        ],
        testcases=[
            {"input": "7 3\n", "output": "<3, 6, 2, 7, 5, 1, 4>\n"},
            {"input": "5 2\n", "output": "<2, 4, 1, 5, 3>\n"},
            {"input": "1 1\n", "output": "<1>\n"},
            {"input": "6 6\n", "output": "<6, 1, 3, 2, 5, 4>\n"},
        ],
        reference_py=(
            "import sys\n"
            "from collections import deque\n"
            "n, k = map(int, sys.stdin.readline().split())\n"
            "q = deque(range(1, n + 1))\n"
            "res = []\n"
            "while q:\n"
            "    q.rotate(-(k - 1))\n"
            "    res.append(q.popleft())\n"
            "print('<' + ', '.join(map(str, res)) + '>')\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int n = Integer.parseInt(st.nextToken());\n"
            "        int k = Integer.parseInt(st.nextToken());\n"
            "        ArrayDeque<Integer> q = new ArrayDeque<>();\n"
            "        for (int i = 1; i <= n; i++) q.addLast(i);\n"
            "        StringBuilder sb = new StringBuilder('<' + \"\");\n"
            "        boolean first = true;\n"
            "        while (!q.isEmpty()) {\n"
            "            for (int i = 0; i < k - 1; i++) q.addLast(q.pollFirst());\n"
            "            if (!first) sb.append(\", \");\n"
            "            sb.append(q.pollFirst());\n"
            "            first = false;\n"
            "        }\n"
            "        sb.append('>');\n"
            "        System.out.println(sb.toString());\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "from collections import deque\n"
            "n, k = map(int, sys.stdin.readline().split())\n"
            "q = deque(range(1, n + 1))\n"
            "# 덱을 회전시키며 K번째 사람을 차례로 제거하세요.\n"
            "# ...\n"
        ),
    ),

    Problem(
        id="silver-26",
        rank="Silver",
        title="카드 버리기 게임",
        style="백준",
        topic="큐",
        type="stdin",
        description=(
            "1번부터 N번까지 번호가 적힌 카드 N장이 위에서부터 1, 2, ..., N 순서로 쌓여 있다. "
            "이제 다음을 카드가 한 장 남을 때까지 반복한다: 맨 위 카드를 바닥에 버리고, 그 다음 "
            "맨 위 카드를 가장 아래로 옮긴다. 마지막에 남는 카드의 번호를 구하시오."
        ),
        input_desc="첫째 줄에 카드의 수 N이 주어진다. (1 ≤ N ≤ 500000)",
        output_desc="마지막에 남는 카드의 번호를 출력한다.",
        examples=[
            {"input": "6\n", "output": "4\n"},
            {"input": "7\n", "output": "6\n"},
        ],
        hints=[
            "맨 위에서 빼고, 또 빼서 맨 아래로 넣는 동작이 반복됩니다. 양쪽 끝에서 넣고 빼기 좋은 자료구조가 필요합니다.",
            "큐(또는 덱)를 쓰세요. popleft() 로 한 장 버리고, 다음 popleft() 한 장을 append() 로 맨 뒤에 넣습니다. 길이가 1이 될 때까지 반복.",
            "q=deque(range(1,n+1)); while len(q)>1: q.popleft(); q.append(q.popleft()). 답은 q[0].",
        ],
        testcases=[
            {"input": "6\n", "output": "4\n"},
            {"input": "7\n", "output": "6\n"},
            {"input": "1\n", "output": "1\n"},
            {"input": "2\n", "output": "2\n"},
            {"input": "4\n", "output": "4\n"},
        ],
        reference_py=(
            "import sys\n"
            "from collections import deque\n"
            "n = int(sys.stdin.readline())\n"
            "q = deque(range(1, n + 1))\n"
            "while len(q) > 1:\n"
            "    q.popleft()\n"
            "    q.append(q.popleft())\n"
            "print(q[0])\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        int n = Integer.parseInt(br.readLine().trim());\n"
            "        ArrayDeque<Integer> q = new ArrayDeque<>();\n"
            "        for (int i = 1; i <= n; i++) q.addLast(i);\n"
            "        while (q.size() > 1) {\n"
            "            q.pollFirst();\n"
            "            q.addLast(q.pollFirst());\n"
            "        }\n"
            "        System.out.println(q.peekFirst());\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "from collections import deque\n"
            "n = int(sys.stdin.readline())\n"
            "q = deque(range(1, n + 1))\n"
            "# 한 장 버리고 한 장은 맨 아래로 옮기기를 반복하세요.\n"
            "# ...\n"
        ),
    ),

    Problem(
        id="silver-27",
        rank="Silver",
        title="회전하는 큐 최소 이동",
        style="백준",
        topic="덱",
        type="stdin",
        description=(
            "1번부터 N번까지 N개의 원소가 양방향 순환 큐에 들어 있다. 가능한 연산은 세 가지다: "
            "(1) 첫 번째 원소를 뽑아낸다, (2) 왼쪽으로 한 칸 회전(맨 앞을 맨 뒤로), "
            "(3) 오른쪽으로 한 칸 회전(맨 뒤를 맨 앞으로). 뽑아내야 할 원소들의 위치가 순서대로 "
            "주어질 때, 모두 뽑기 위해 필요한 (2),(3) 연산의 최소 횟수를 구하시오."
        ),
        input_desc=(
            "첫째 줄에 큐 크기 N과 뽑을 원소 개수 M (1 ≤ M ≤ N ≤ 50). 둘째 줄에 뽑아야 할 "
            "원소들의 번호가 뽑는 순서대로 공백으로 주어진다."
        ),
        output_desc="필요한 회전 연산(2번, 3번)의 최소 횟수를 출력한다.",
        examples=[
            {"input": "10 3\n2 9 5\n", "output": "8\n"},
            {"input": "10 3\n1 2 3\n", "output": "0\n"},
        ],
        hints=[
            "현재 큐에서 목표 원소가 앞에서 몇 번째에 있는지 보세요. 왼쪽으로 가져오는 것과 오른쪽으로 가져오는 것 중 더 가까운 방향을 택해야 합니다.",
            "덱을 쓰세요. 목표의 인덱스 idx 와 길이 L 을 비교해, idx <= L/2 면 왼쪽 회전 idx 번, 아니면 오른쪽 회전 L-idx 번이 더 쌉니다. 회전 후 popleft 로 뽑습니다.",
            "idx=q.index(t); if idx<=len(q)//2: cnt+=idx; q.rotate(-idx) else: cnt+=len(q)-idx; q.rotate(len(q)-idx); q.popleft().",
        ],
        testcases=[
            {"input": "10 3\n2 9 5\n", "output": "8\n"},
            {"input": "10 3\n1 2 3\n", "output": "0\n"},
            {"input": "32 6\n27 16 30 11 6 23\n", "output": "59\n"},
            {"input": "1 1\n1\n", "output": "0\n"},
            {"input": "5 5\n5 4 3 2 1\n", "output": "4\n"},
        ],
        reference_py=(
            "import sys\n"
            "from collections import deque\n"
            "n, m = map(int, sys.stdin.readline().split())\n"
            "targets = list(map(int, sys.stdin.readline().split()))\n"
            "q = deque(range(1, n + 1))\n"
            "cnt = 0\n"
            "for t in targets:\n"
            "    idx = q.index(t)\n"
            "    if idx <= len(q) // 2:\n"
            "        cnt += idx\n"
            "        q.rotate(-idx)\n"
            "    else:\n"
            "        cnt += len(q) - idx\n"
            "        q.rotate(len(q) - idx)\n"
            "    q.popleft()\n"
            "print(cnt)\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int n = Integer.parseInt(st.nextToken());\n"
            "        int m = Integer.parseInt(st.nextToken());\n"
            "        ArrayList<Integer> q = new ArrayList<>();\n"
            "        for (int i = 1; i <= n; i++) q.add(i);\n"
            "        st = new StringTokenizer(br.readLine());\n"
            "        int cnt = 0;\n"
            "        for (int j = 0; j < m; j++) {\n"
            "            int t = Integer.parseInt(st.nextToken());\n"
            "            int idx = q.indexOf(t);\n"
            "            int L = q.size();\n"
            "            if (idx <= L / 2) cnt += idx; else cnt += L - idx;\n"
            "            q.remove(Integer.valueOf(t));\n"
            "            Collections.rotate(q, (idx <= L / 2) ? 0 : 0);\n"
            "            if (idx <= L / 2) { ArrayList<Integer> nq = new ArrayList<>(q.subList(idx, q.size())); nq.addAll(q.subList(0, idx)); q = nq; }\n"
            "            else { int r = (L - idx) % q.size(); if (q.size() > 0) { ArrayList<Integer> nq = new ArrayList<>(q.subList(q.size() - r, q.size())); nq.addAll(q.subList(0, q.size() - r)); q = nq; } }\n"
            "        }\n"
            "        System.out.println(cnt);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "from collections import deque\n"
            "n, m = map(int, sys.stdin.readline().split())\n"
            "targets = list(map(int, sys.stdin.readline().split()))\n"
            "q = deque(range(1, n + 1))\n"
            "# 더 가까운 방향으로 회전시키며 원소를 뽑고 횟수를 세세요.\n"
            "# ...\n"
        ),
    ),

    Problem(
        id="silver-28",
        rank="Silver",
        title="덱으로 회문 판별",
        style="해외대기업",
        topic="덱",
        type="func",
        func_name="solution",
        description=(
            "문자열 s 가 회문(palindrome)인지 판별하세요. 회문이란 앞에서 읽으나 뒤에서 "
            "읽으나 똑같은 문자열을 말합니다. 양쪽 끝에서 한 글자씩 꺼내 비교하는 방식을 "
            "사용하세요. 회문이면 True, 아니면 False 를 반환합니다."
        ),
        input_desc="s : 영문 소문자로 이루어진 문자열 (0 ≤ len(s) ≤ 100000)",
        output_desc="회문이면 True, 아니면 False",
        examples=[
            {"args": ["level"], "output": True},
            {"args": ["hello"], "output": False},
        ],
        hints=[
            "문자열의 양쪽 끝 문자를 동시에 비교하면 됩니다. 한 쌍이라도 다르면 회문이 아닙니다.",
            "덱(deque)에 문자를 모두 넣고, 길이가 1보다 큰 동안 popleft() 와 pop() 의 결과를 비교하세요.",
            "dq=deque(s); while len(dq)>1: if dq.popleft()!=dq.pop(): return False  → 끝까지 통과하면 return True.",
        ],
        testcases=[
            {"args": ["level"], "expected": True},
            {"args": ["hello"], "expected": False},
            {"args": [""], "expected": True},
            {"args": ["a"], "expected": True},
            {"args": ["abccba"], "expected": True},
            {"args": ["abca"], "expected": False},
        ],
        reference_py=(
            "from collections import deque\n"
            "def solution(s):\n"
            "    dq = deque(s)\n"
            "    while len(dq) > 1:\n"
            "        if dq.popleft() != dq.pop():\n"
            "            return False\n"
            "    return True\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public boolean solution(String s) {\n"
            "        Deque<Character> dq = new ArrayDeque<>();\n"
            "        for (char c : s.toCharArray()) dq.addLast(c);\n"
            "        while (dq.size() > 1) {\n"
            "            if (!dq.pollFirst().equals(dq.pollLast())) return false;\n"
            "        }\n"
            "        return true;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "from collections import deque\n"
            "# 회문이면 True, 아니면 False\n"
            "def solution(s):\n"
            "    answer = True\n"
            "    return answer\n"
        ),
    ),

    # ============================ 해시 ============================
    Problem(
        id="silver-29",
        rank="Silver",
        title="최빈값 구하기",
        style="프로그래머스",
        topic="해시",
        type="func",
        func_name="solution",
        description=(
            "정수 배열 nums 가 주어질 때, 가장 많이 등장한 값(최빈값)을 반환하세요. "
            "가장 많이 등장한 값이 여러 개라면 그중 가장 작은 값을 반환합니다."
        ),
        input_desc="nums : 정수 리스트 (1 ≤ len(nums) ≤ 100000)",
        output_desc="최빈값(동률이면 가장 작은 값)",
        examples=[
            {"args": [[1, 2, 2, 3, 3, 3]], "output": 3},
            {"args": [[1, 1, 2, 2]], "output": 1},
        ],
        hints=[
            "각 값이 몇 번 나왔는지 세어야 합니다. 값을 키로 하는 빈도 표를 만들면 좋겠죠.",
            "딕셔너리(또는 collections.Counter)로 빈도수를 세세요. 그다음 최대 빈도를 구하고, 그 빈도를 가진 값 중 최솟값을 고릅니다.",
            "c=Counter(nums); best=max(c.values()); return min(k for k,v in c.items() if v==best).",
        ],
        testcases=[
            {"args": [[1, 2, 2, 3, 3, 3]], "expected": 3},
            {"args": [[1, 1, 2, 2]], "expected": 1},
            {"args": [[5]], "expected": 5},
            {"args": [[4, 4, 4, 1, 1, 1]], "expected": 1},
            {"args": [[7, 7, 8]], "expected": 7},
        ],
        reference_py=(
            "from collections import Counter\n"
            "def solution(nums):\n"
            "    c = Counter(nums)\n"
            "    best = max(c.values())\n"
            "    return min(k for k, v in c.items() if v == best)\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int solution(int[] nums) {\n"
            "        HashMap<Integer, Integer> c = new HashMap<>();\n"
            "        for (int x : nums) c.merge(x, 1, Integer::sum);\n"
            "        int best = 0;\n"
            "        for (int v : c.values()) best = Math.max(best, v);\n"
            "        int ans = Integer.MAX_VALUE;\n"
            "        for (Map.Entry<Integer, Integer> e : c.entrySet())\n"
            "            if (e.getValue() == best) ans = Math.min(ans, e.getKey());\n"
            "        return ans;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "from collections import Counter\n"
            "# 최빈값(동률이면 가장 작은 값) 반환\n"
            "def solution(nums):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="silver-30",
        rank="Silver",
        title="순서 유지 중복 제거",
        style="대기업",
        topic="해시",
        type="func",
        func_name="solution",
        description=(
            "정수 배열 nums 에서 중복된 원소를 제거하되, 각 값이 처음 등장한 순서는 그대로 "
            "유지한 결과 리스트를 반환하세요. 정렬하면 안 되고 첫 등장 순서를 지켜야 합니다."
        ),
        input_desc="nums : 정수 리스트 (0 ≤ len(nums) ≤ 100000)",
        output_desc="중복을 제거하고 첫 등장 순서를 유지한 리스트",
        examples=[
            {"args": [[1, 1, 2, 3, 3, 3, 4]], "output": [1, 2, 3, 4]},
            {"args": [[4, 3, 2, 4, 1]], "output": [4, 3, 2, 1]},
        ],
        hints=[
            "이미 결과에 넣은 값인지 빠르게 확인할 수 있어야 합니다. 무엇을 보면 '이미 봤다'를 O(1)로 알 수 있을까요?",
            "셋(set)에 본 적 있는 값을 기록하세요. 처음 보는 값만 결과 리스트에 추가하고 셋에도 넣습니다.",
            "seen=set(); res=[]; for x in nums: if x not in seen: seen.add(x); res.append(x). return res.",
        ],
        testcases=[
            {"args": [[1, 1, 2, 3, 3, 3, 4]], "expected": [1, 2, 3, 4]},
            {"args": [[4, 3, 2, 4, 1]], "expected": [4, 3, 2, 1]},
            {"args": [[]], "expected": []},
            {"args": [[2, 2, 2, 2]], "expected": [2]},
            {"args": [[1, 3, 1, 3, 5]], "expected": [1, 3, 5]},
        ],
        reference_py=(
            "def solution(nums):\n"
            "    seen = set()\n"
            "    res = []\n"
            "    for x in nums:\n"
            "        if x not in seen:\n"
            "            seen.add(x)\n"
            "            res.append(x)\n"
            "    return res\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int[] solution(int[] nums) {\n"
            "        HashSet<Integer> seen = new HashSet<>();\n"
            "        ArrayList<Integer> res = new ArrayList<>();\n"
            "        for (int x : nums) if (seen.add(x)) res.add(x);\n"
            "        int[] out = new int[res.size()];\n"
            "        for (int i = 0; i < out.length; i++) out[i] = res.get(i);\n"
            "        return out;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 첫 등장 순서를 유지하며 중복 제거\n"
            "def solution(nums):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="silver-31",
        rank="Silver",
        title="두 배열의 교집합",
        style="해외대기업",
        topic="해시",
        type="func",
        func_name="solution",
        description=(
            "두 정수 배열 a 와 b 가 주어진다. 두 배열에 공통으로 등장하는 값들을 중복 없이 "
            "모아 오름차순으로 정렬한 리스트를 반환하세요."
        ),
        input_desc="a, b : 정수 리스트 (0 ≤ len(a), len(b) ≤ 100000)",
        output_desc="두 배열의 교집합을 오름차순으로 정렬한 리스트 (중복 없음)",
        examples=[
            {"args": [[1, 2, 2, 1], [2, 2]], "output": [2]},
            {"args": [[4, 9, 5], [9, 4, 9, 8, 4]], "output": [4, 9]},
        ],
        hints=[
            "한 배열의 원소를 빠르게 '있는지' 확인할 수 있으면, 다른 배열을 훑으며 공통 원소를 찾을 수 있습니다.",
            "두 배열을 각각 셋(set)으로 만든 뒤 교집합 연산(&)을 쓰면 공통 원소를 한 번에 얻습니다. 마지막에 정렬하세요.",
            "return sorted(set(a) & set(b)).",
        ],
        testcases=[
            {"args": [[1, 2, 2, 1], [2, 2]], "expected": [2]},
            {"args": [[4, 9, 5], [9, 4, 9, 8, 4]], "expected": [4, 9]},
            {"args": [[1, 2, 3], [4, 5, 6]], "expected": []},
            {"args": [[], [1, 2]], "expected": []},
            {"args": [[1, 1, 1], [1, 1]], "expected": [1]},
        ],
        reference_py=(
            "def solution(a, b):\n"
            "    return sorted(set(a) & set(b))\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int[] solution(int[] a, int[] b) {\n"
            "        HashSet<Integer> sa = new HashSet<>();\n"
            "        for (int x : a) sa.add(x);\n"
            "        TreeSet<Integer> inter = new TreeSet<>();\n"
            "        for (int x : b) if (sa.contains(x)) inter.add(x);\n"
            "        int[] out = new int[inter.size()];\n"
            "        int i = 0;\n"
            "        for (int x : inter) out[i++] = x;\n"
            "        return out;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 두 배열의 교집합을 오름차순 정렬해 반환\n"
            "def solution(a, b):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="silver-32",
        rank="Silver",
        title="두 수의 합 인덱스",
        style="해외대기업",
        topic="해시",
        type="func",
        func_name="solution",
        description=(
            "정수 배열 nums 와 목표값 target 이 주어진다. 더해서 target 이 되는 서로 다른 두 "
            "원소의 인덱스(0-based)를 [i, j] (i < j) 형태로 반환하세요. 정답은 정확히 하나만 "
            "존재한다고 가정합니다."
        ),
        input_desc="nums : 정수 리스트, target : 정수 (2 ≤ len(nums) ≤ 100000)",
        output_desc="합이 target 인 두 원소의 인덱스 [i, j] (i < j)",
        examples=[
            {"args": [[2, 7, 11, 15], 9], "output": [0, 1]},
            {"args": [[3, 2, 4], 6], "output": [1, 2]},
        ],
        hints=[
            "각 원소 x 에 대해 target - x 가 앞에 이미 나왔는지 알면 바로 답을 찾을 수 있습니다.",
            "딕셔너리에 '값 -> 인덱스' 를 기록하며 한 번만 훑으세요. 현재 값 x 에 대해 target-x 가 딕셔너리에 있으면 그 인덱스와 현재 인덱스가 답입니다.",
            "seen={}; for i,x in enumerate(nums): if target-x in seen: return [seen[target-x], i]; seen[x]=i.",
        ],
        testcases=[
            {"args": [[2, 7, 11, 15], 9], "expected": [0, 1]},
            {"args": [[3, 2, 4], 6], "expected": [1, 2]},
            {"args": [[3, 3], 6], "expected": [0, 1]},
            {"args": [[1, 5, 3, 7], 10], "expected": [2, 3]},
            {"args": [[0, 4, 3, 0], 0], "expected": [0, 3]},
        ],
        reference_py=(
            "def solution(nums, target):\n"
            "    seen = {}\n"
            "    for i, x in enumerate(nums):\n"
            "        if target - x in seen:\n"
            "            return [seen[target - x], i]\n"
            "        seen[x] = i\n"
            "    return []\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int[] solution(int[] nums, int target) {\n"
            "        HashMap<Integer, Integer> seen = new HashMap<>();\n"
            "        for (int i = 0; i < nums.length; i++) {\n"
            "            if (seen.containsKey(target - nums[i]))\n"
            "                return new int[]{seen.get(target - nums[i]), i};\n"
            "            seen.put(nums[i], i);\n"
            "        }\n"
            "        return new int[]{};\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 합이 target 인 두 원소의 인덱스 [i, j] (i < j) 반환\n"
            "def solution(nums, target):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

    # ============================ 우선순위 큐 ============================
    Problem(
        id="silver-33",
        rank="Silver",
        title="가장 작은 수 K개",
        style="프로그래머스",
        topic="우선순위큐",
        type="func",
        func_name="solution",
        description=(
            "정수 배열 nums 와 정수 k 가 주어진다. nums 에서 가장 작은 수 k개를 골라 "
            "오름차순으로 정렬한 리스트를 반환하세요. (1 ≤ k ≤ len(nums))"
        ),
        input_desc="nums : 정수 리스트, k : 골라낼 개수",
        output_desc="가장 작은 수 k개를 오름차순으로 담은 리스트",
        examples=[
            {"args": [[5, 1, 4, 2, 3], 3], "output": [1, 2, 3]},
            {"args": [[9, 8, 7], 2], "output": [7, 8]},
        ],
        hints=[
            "전체를 정렬해 앞에서 k개를 가져와도 되지만, 우선순위 큐(힙)를 쓰면 작은 값들을 효율적으로 뽑을 수 있습니다.",
            "최소 힙을 이용하세요. heapq 모듈의 nsmallest 를 쓰면 가장 작은 k개를 정렬된 상태로 바로 얻을 수 있습니다.",
            "import heapq; return heapq.nsmallest(k, nums).",
        ],
        testcases=[
            {"args": [[5, 1, 4, 2, 3], 3], "expected": [1, 2, 3]},
            {"args": [[9, 8, 7], 2], "expected": [7, 8]},
            {"args": [[3], 1], "expected": [3]},
            {"args": [[4, 4, 4, 1], 2], "expected": [1, 4]},
            {"args": [[10, 20, 30, 40], 4], "expected": [10, 20, 30, 40]},
        ],
        reference_py=(
            "import heapq\n"
            "def solution(nums, k):\n"
            "    return heapq.nsmallest(k, nums)\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int[] solution(int[] nums, int k) {\n"
            "        int[] copy = nums.clone();\n"
            "        Arrays.sort(copy);\n"
            "        int[] out = new int[k];\n"
            "        for (int i = 0; i < k; i++) out[i] = copy[i];\n"
            "        return out;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import heapq\n"
            "# 가장 작은 수 k개를 오름차순으로 반환\n"
            "def solution(nums, k):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="silver-34",
        rank="Silver",
        title="K번째 큰 수",
        style="해외대기업",
        topic="우선순위큐",
        type="func",
        func_name="solution",
        description=(
            "정수 배열 nums 와 정수 k 가 주어진다. 정렬했을 때 k번째로 큰 값을 반환하세요. "
            "(서로 다른 원소일 필요는 없으며, 중복을 포함해 순위를 셉니다.) "
            "예를 들어 [3,2,1,5,6,4] 에서 2번째 큰 수는 5 입니다."
        ),
        input_desc="nums : 정수 리스트, k : 순위 (1 ≤ k ≤ len(nums))",
        output_desc="k번째로 큰 값",
        examples=[
            {"args": [[3, 2, 1, 5, 6, 4], 2], "output": 5},
            {"args": [[3, 2, 3, 1, 2, 4, 5, 5, 6], 4], "output": 4},
        ],
        hints=[
            "전체를 내림차순으로 정렬하면 k번째 원소가 답입니다. 하지만 k가 작다면 큰 값 몇 개만 관리해도 됩니다.",
            "우선순위 큐(힙)를 활용하세요. heapq.nlargest 로 가장 큰 k개를 얻은 뒤 그 마지막 원소가 k번째 큰 수입니다.",
            "import heapq; return heapq.nlargest(k, nums)[-1].",
        ],
        testcases=[
            {"args": [[3, 2, 1, 5, 6, 4], 2], "expected": 5},
            {"args": [[3, 2, 3, 1, 2, 4, 5, 5, 6], 4], "expected": 4},
            {"args": [[1], 1], "expected": 1},
            {"args": [[7, 7, 7], 2], "expected": 7},
            {"args": [[5, 4, 3, 2, 1], 5], "expected": 1},
        ],
        reference_py=(
            "import heapq\n"
            "def solution(nums, k):\n"
            "    return heapq.nlargest(k, nums)[-1]\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int solution(int[] nums, int k) {\n"
            "        int[] copy = nums.clone();\n"
            "        Arrays.sort(copy);\n"
            "        return copy[copy.length - k];\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import heapq\n"
            "# k번째로 큰 값 반환\n"
            "def solution(nums, k):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="silver-35",
        rank="Silver",
        title="절댓값 힙",
        style="백준",
        topic="우선순위큐",
        type="stdin",
        description=(
            "다음 연산을 지원하는 절댓값 힙을 구현하시오. 정수 x 가 주어지면 x 를 배열에 "
            "추가하고, x 가 0이면 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 "
            "제거한다. 절댓값이 가장 작은 값이 여러 개일 때는 가장 작은 값을 먼저 제거한다. "
            "배열이 비어 있는데 0이 들어오면 0을 출력한다."
        ),
        input_desc=(
            "첫째 줄에 연산의 개수 N (1 ≤ N ≤ 100000). 다음 N개의 줄에 정수 x 가 하나씩 "
            "주어진다. (|x| < 2^31)"
        ),
        output_desc="입력에서 x 가 0인 경우마다 정해진 값을 한 줄에 하나씩 출력한다.",
        examples=[
            {"input": "5\n1\n-1\n0\n0\n0\n", "output": "-1\n1\n0\n"},
            {"input": "4\n3\n-3\n2\n0\n", "output": "2\n"},
        ],
        hints=[
            "절댓값이 작은 것을 먼저, 절댓값이 같으면 실제 값이 작은 것을 먼저 꺼내야 합니다. 무엇을 기준으로 우선순위를 정할지 생각해 보세요.",
            "(절댓값, 실제값) 튜플을 우선순위 큐(최소 힙)에 넣으세요. 튜플 비교는 첫 원소(절댓값) 우선, 같으면 둘째 원소(실제값) 순으로 비교되므로 조건이 정확히 맞습니다.",
            "heapq.heappush(heap, (abs(x), x)). 0이면 heap 이 비었으면 0, 아니면 heapq.heappop(heap)[1] 출력.",
        ],
        testcases=[
            {"input": "5\n1\n-1\n0\n0\n0\n", "output": "-1\n1\n0\n"},
            {"input": "4\n3\n-3\n2\n0\n", "output": "2\n"},
            {"input": "2\n0\n0\n", "output": "0\n0\n"},
            {"input": "3\n-5\n0\n0\n", "output": "-5\n0\n"},
            {
                "input": "18\n1\n-1\n0\n0\n0\n1\n1\n-1\n-1\n0\n0\n0\n0\n0\n0\n0\n0\n0\n",
                "output": "-1\n1\n0\n-1\n-1\n1\n1\n0\n0\n0\n0\n0\n",
            },
        ],
        reference_py=(
            "import sys, heapq\n"
            "input = sys.stdin.readline\n"
            "n = int(input())\n"
            "heap = []\n"
            "out = []\n"
            "for _ in range(n):\n"
            "    x = int(input())\n"
            "    if x == 0:\n"
            "        if heap:\n"
            "            out.append(str(heapq.heappop(heap)[1]))\n"
            "        else:\n"
            "            out.append('0')\n"
            "    else:\n"
            "        heapq.heappush(heap, (abs(x), x))\n"
            "print('\\n'.join(out))\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        int n = Integer.parseInt(br.readLine().trim());\n"
            "        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> {\n"
            "            int aa = Math.abs(a), bb = Math.abs(b);\n"
            "            if (aa != bb) return aa - bb;\n"
            "            return a - b;\n"
            "        });\n"
            "        StringBuilder sb = new StringBuilder();\n"
            "        for (int i = 0; i < n; i++) {\n"
            "            int x = Integer.parseInt(br.readLine().trim());\n"
            "            if (x == 0) sb.append(pq.isEmpty() ? 0 : pq.poll()).append('\\n');\n"
            "            else pq.add(x);\n"
            "        }\n"
            "        System.out.print(sb);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys, heapq\n"
            "input = sys.stdin.readline\n"
            "n = int(input())\n"
            "heap = []\n"
            "# (절댓값, 실제값) 튜플을 최소 힙에 넣어 관리하세요.\n"
            "# ...\n"
        ),
    ),

]
