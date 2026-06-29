"""실버 랭크 — 정렬 / 이분탐색 / 스택 / 그리디 기초 / 누적합.

목표 50문제. 현재 시드 5문제.
"""

from engine.models import Problem

PROBLEMS = [

    Problem(
        id="silver-01",
        rank="Silver",
        title="수 정렬하기",
        style="백준",
        topic="정렬",
        type="stdin",
        description="N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.",
        input_desc="첫째 줄에 N(1 ≤ N ≤ 1000), 다음 N개의 줄에 정수가 하나씩 주어진다.",
        output_desc="오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.",
        examples=[
            {"input": "5\n5\n2\n3\n4\n1\n", "output": "1\n2\n3\n4\n5\n"},
        ],
        hints=[
            "수를 N개 읽어 리스트에 담은 뒤 정렬하면 됩니다.",
            "리스트에는 .sort() 메서드가, 내장에는 sorted() 가 있습니다. 출력은 한 줄에 하나씩.",
            "arr = [int(input()) for _ in range(n)]; arr.sort(); 후 for x in arr: print(x)",
        ],
        testcases=[
            {"input": "5\n5\n2\n3\n4\n1\n", "output": "1\n2\n3\n4\n5\n"},
            {"input": "3\n-1\n0\n-5\n", "output": "-5\n-1\n0\n"},
            {"input": "1\n7\n", "output": "7\n"},
        ],
        reference_py=(
            "n = int(input())\n"
            "arr = [int(input()) for _ in range(n)]\n"
            "for x in sorted(arr):\n"
            "    print(x)\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        int n = Integer.parseInt(br.readLine());\n"
            "        int[] a = new int[n];\n"
            "        for (int i = 0; i < n; i++) a[i] = Integer.parseInt(br.readLine());\n"
            "        Arrays.sort(a);\n"
            "        StringBuilder sb = new StringBuilder();\n"
            "        for (int x : a) sb.append(x).append('\\n');\n"
            "        System.out.print(sb);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 수 정렬하기 : N개를 읽어 오름차순 출력\n"
            "n = int(input())\n"
            "# arr = ...\n"
        ),
    ),

    Problem(
        id="silver-02",
        rank="Silver",
        title="괄호 검사 (VPS)",
        style="백준",
        topic="스택",
        type="func",
        func_name="solution",
        description=(
            "'(' 와 ')' 로만 이루어진 문자열이 올바른 괄호 문자열(VPS)인지 검사한다. "
            "여는 괄호와 닫는 괄호의 짝이 모두 맞으면 True, 아니면 False 를 반환하세요."
        ),
        input_desc="s : '(' 와 ')' 로 이루어진 문자열 (0 ≤ len(s) ≤ 50)",
        output_desc="올바른 괄호면 True, 아니면 False",
        examples=[
            {"args": ["(())()"], "output": True},
            {"args": ["(()("], "output": False},
        ],
        hints=[
            "왼쪽부터 읽으면서 '열려 있는 괄호 개수'를 세어 보세요. 닫는 괄호가 더 많아지면 안 됩니다.",
            "스택(또는 카운터)을 쓰세요. '(' 면 +1, ')' 면 -1. 중간에 음수가 되면 실패, 끝에 0이 아니어도 실패.",
            "cnt=0; for c in s: cnt += 1 if c=='(' else -1; if cnt<0: return False  → 끝나고 return cnt==0",
        ],
        testcases=[
            {"args": ["(())()"], "expected": True},
            {"args": ["(()("], "expected": False},
            {"args": [")("], "expected": False},
            {"args": [""], "expected": True},
            {"args": ["((()))"], "expected": True},
        ],
        reference_py=(
            "def solution(s):\n"
            "    cnt = 0\n"
            "    for c in s:\n"
            "        cnt += 1 if c == '(' else -1\n"
            "        if cnt < 0:\n"
            "            return False\n"
            "    return cnt == 0\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public boolean solution(String s) {\n"
            "        int cnt = 0;\n"
            "        for (char c : s.toCharArray()) {\n"
            "            cnt += (c == '(') ? 1 : -1;\n"
            "            if (cnt < 0) return false;\n"
            "        }\n"
            "        return cnt == 0;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 올바른 괄호 문자열이면 True, 아니면 False\n"
            "def solution(s):\n"
            "    answer = True\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="silver-03",
        rank="Silver",
        title="숫자 찾기 (이분 탐색)",
        style="백준",
        topic="이분탐색",
        type="stdin",
        description=(
            "정렬되지 않은 N개의 정수 배열 A가 있다. M개의 정수가 주어지면, "
            "각 정수가 A 안에 존재하면 1, 없으면 0을 공백으로 구분해 출력하시오."
        ),
        input_desc=(
            "첫째 줄 N, 둘째 줄 A의 원소 N개, 셋째 줄 M, 넷째 줄 확인할 정수 M개. "
            "(1 ≤ N, M ≤ 100000)"
        ),
        output_desc="M개의 정수 각각에 대해 존재 여부(1/0)를 공백으로 구분해 한 줄에 출력한다.",
        examples=[
            {"input": "5\n4 1 5 2 3\n5\n1 3 7 9 5\n", "output": "1 1 0 0 1\n"},
        ],
        hints=[
            "M개를 각각 선형 탐색하면 N*M이라 느릴 수 있습니다. A를 한 번 정렬하면 무엇을 쓸 수 있을까요?",
            "정렬 후 이분 탐색(bisect) 또는 set 을 활용하면 빠르게 존재 여부를 확인할 수 있습니다.",
            "S = set(A); print(' '.join('1' if x in S else '0' for x in queries)) — set 의 in 은 평균 O(1).",
        ],
        testcases=[
            {"input": "5\n4 1 5 2 3\n5\n1 3 7 9 5\n", "output": "1 1 0 0 1\n"},
            {"input": "1\n10\n3\n10 11 10\n", "output": "1 0 1\n"},
        ],
        reference_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "n = int(input())\n"
            "A = set(map(int, input().split()))\n"
            "m = int(input())\n"
            "q = map(int, input().split())\n"
            "print(' '.join('1' if x in A else '0' for x in q))\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        br.readLine();\n"
            "        HashSet<Integer> set = new HashSet<>();\n"
            "        for (String t : br.readLine().split(\" \")) set.add(Integer.parseInt(t));\n"
            "        br.readLine();\n"
            "        StringBuilder sb = new StringBuilder();\n"
            "        for (String t : br.readLine().split(\" \"))\n"
            "            sb.append(set.contains(Integer.parseInt(t)) ? 1 : 0).append(' ');\n"
            "        System.out.println(sb.toString().trim());\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "# 숫자 찾기 : A에 존재하면 1, 아니면 0\n"
            "n = int(input())\n"
            "# ...\n"
        ),
    ),

    Problem(
        id="silver-04",
        rank="Silver",
        title="동전 거스름돈 (그리디)",
        style="대기업",
        topic="그리디",
        type="func",
        func_name="solution",
        description=(
            "거스름돈 amount원을 동전으로 거슬러 줄 때, 사용하는 동전 개수의 최솟값을 구하세요. "
            "동전 종류 coins 는 서로 배수 관계라 큰 동전부터 쓰는 그리디가 최적입니다."
        ),
        input_desc="coins : 동전 단위 리스트(예: [500,100,50,10]), amount : 거슬러 줄 금액",
        output_desc="필요한 최소 동전 개수 (정확히 거슬러 줄 수 없으면 -1)",
        examples=[
            {"args": [[500, 100, 50, 10], 1260], "output": 6},
            {"args": [[500, 100, 50, 10], 33], "output": -1},
        ],
        hints=[
            "큰 단위 동전부터 최대한 많이 쓰는 게 개수를 줄이는 길입니다.",
            "동전을 내림차순으로 정렬한 뒤, 각 동전에 대해 amount // coin 개를 쓰고 amount %= coin 하세요.",
            "for c in sorted(coins, reverse=True): cnt += amount//c; amount %= c. 끝에 amount>0 이면 -1, 아니면 cnt.",
        ],
        testcases=[
            {"args": [[500, 100, 50, 10], 1260], "expected": 6},
            {"args": [[500, 100, 50, 10], 33], "expected": -1},
            {"args": [[500, 100, 50, 10], 0], "expected": 0},
            {"args": [[1000, 500, 100], 1600], "expected": 3},
        ],
        reference_py=(
            "def solution(coins, amount):\n"
            "    cnt = 0\n"
            "    for c in sorted(coins, reverse=True):\n"
            "        cnt += amount // c\n"
            "        amount %= c\n"
            "    return cnt if amount == 0 else -1\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int solution(int[] coins, int amount) {\n"
            "        Integer[] c = Arrays.stream(coins).boxed().toArray(Integer[]::new);\n"
            "        Arrays.sort(c, Collections.reverseOrder());\n"
            "        int cnt = 0;\n"
            "        for (int v : c) { cnt += amount / v; amount %= v; }\n"
            "        return amount == 0 ? cnt : -1;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 최소 동전 개수 (불가능하면 -1)\n"
            "def solution(coins, amount):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="silver-05",
        rank="Silver",
        title="구간 합 구하기 (누적합)",
        style="백준",
        topic="누적합",
        type="func",
        func_name="solution",
        description=(
            "수열 nums 와 질의 목록 queries 가 주어진다. 각 질의 (i, j) 는 1-based 로 "
            "i번째부터 j번째까지의 합을 의미한다. 각 질의의 답을 리스트로 반환하세요. "
            "질의가 많으므로 매번 더하지 말고 누적합을 이용하세요."
        ),
        input_desc="nums : 정수 리스트, queries : [(i, j), ...] (1 ≤ i ≤ j ≤ len(nums))",
        output_desc="각 질의에 대한 구간 합 리스트",
        examples=[
            {"args": [[5, 4, 3, 2, 1], [[1, 3], [2, 4], [5, 5]]], "output": [12, 9, 1]},
        ],
        hints=[
            "질의마다 sum(nums[i-1:j]) 하면 질의가 많을 때 느립니다. 미리 계산해 둘 값은 없을까요?",
            "누적합 배열 prefix 를 만드세요. prefix[k] = nums[0..k-1] 의 합. 그러면 구간합 = prefix[j]-prefix[i-1].",
            "prefix=[0]; for x in nums: prefix.append(prefix[-1]+x). 답은 prefix[j]-prefix[i-1].",
        ],
        testcases=[
            {"args": [[5, 4, 3, 2, 1], [[1, 3], [2, 4], [5, 5]]], "expected": [12, 9, 1]},
            {"args": [[1, 2, 3, 4, 5], [[1, 5]]], "expected": [15]},
            {"args": [[10], [[1, 1]]], "expected": [10]},
        ],
        reference_py=(
            "def solution(nums, queries):\n"
            "    prefix = [0]\n"
            "    for x in nums:\n"
            "        prefix.append(prefix[-1] + x)\n"
            "    return [prefix[j] - prefix[i - 1] for i, j in queries]\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int[] solution(int[] nums, int[][] queries) {\n"
            "        int n = nums.length;\n"
            "        long[] p = new long[n + 1];\n"
            "        for (int k = 0; k < n; k++) p[k + 1] = p[k] + nums[k];\n"
            "        int[] ans = new int[queries.length];\n"
            "        for (int q = 0; q < queries.length; q++) {\n"
            "            int i = queries[q][0], j = queries[q][1];\n"
            "            ans[q] = (int)(p[j] - p[i - 1]);\n"
            "        }\n"
            "        return ans;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 누적합으로 각 질의의 구간합을 리스트로 반환\n"
            "def solution(nums, queries):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

]
