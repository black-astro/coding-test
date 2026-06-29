"""골드 랭크 추가 배치 A — DP 집중 (gold-06 ~ gold-20).

1D DP(계단/포도주/삼각형/카데인/타일링), 2D DP(편집거리/RGB/정사각형/격자경로/LCS/회문),
배낭 변형(부분집합 합), 동전 경우의 수, 최대 곱 부분배열, 이친수 등 15문제.
"""

from engine.models import Problem

RANK = "Gold"

PROBLEMS = [

    Problem(
        id="gold-06",
        rank="Gold",
        title="계단 오르기 최대 점수",
        style="백준",
        topic="DP",
        type="stdin",
        description=(
            "계단에는 각 칸마다 점수가 적혀 있다. 한 번에 한 칸 또는 두 칸씩 오를 수 있으나, "
            "연속한 세 칸을 모두 밟을 수는 없다. 또한 마지막 칸은 반드시 밟아야 한다. "
            "시작 지점(첫 칸 아래)에서 출발해 마지막 칸까지 올라갈 때 밟은 칸들의 점수 합의 "
            "최댓값을 구하시오."
        ),
        input_desc="첫째 줄 계단 수 N (1 ≤ N ≤ 300), 다음 N개의 줄에 각 칸의 점수(정수).",
        output_desc="밟은 칸 점수 합의 최댓값.",
        examples=[
            {"input": "6\n10\n20\n15\n25\n10\n20\n", "output": "75\n"},
            {"input": "2\n10\n20\n", "output": "30\n"},
        ],
        hints=[
            "마지막 칸은 무조건 밟으므로, '연속 세 칸 금지' 규칙 때문에 직전 칸을 밟았는지 여부로 상태가 갈립니다.",
            "1차원 DP. dp[i] = i번째 칸을 밟고 거기까지 얻는 최대 점수. i칸은 (i-2)칸에서 한 번에 오거나, (i-3)칸에서 (i-1)칸을 거쳐 옵니다.",
            "dp[i] = max(dp[i-2], dp[i-3]+s[i-1]) + s[i] 형태로 채우고, 초기값 dp[0], dp[1], dp[2]를 따로 처리한 뒤 dp[N-1]을 출력.",
        ],
        testcases=[
            {"input": "6\n10\n20\n15\n25\n10\n20\n", "output": "75\n"},
            {"input": "2\n10\n20\n", "output": "30\n"},
            {"input": "1\n5\n", "output": "5\n"},
            {"input": "3\n10\n20\n15\n", "output": "35\n"},
            {"input": "4\n1\n2\n3\n4\n", "output": "8\n"},
        ],
        reference_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "n = int(input())\n"
            "s = [int(input()) for _ in range(n)]\n"
            "dp = [0] * n\n"
            "dp[0] = s[0]\n"
            "if n >= 2:\n"
            "    dp[1] = s[0] + s[1]\n"
            "if n >= 3:\n"
            "    dp[2] = max(s[0] + s[2], s[1] + s[2])\n"
            "for i in range(3, n):\n"
            "    dp[i] = max(dp[i - 2] + s[i], dp[i - 3] + s[i - 1] + s[i])\n"
            "print(dp[n - 1])\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        int n = Integer.parseInt(br.readLine().trim());\n"
            "        int[] s = new int[n];\n"
            "        for (int i = 0; i < n; i++) s[i] = Integer.parseInt(br.readLine().trim());\n"
            "        int[] dp = new int[n];\n"
            "        dp[0] = s[0];\n"
            "        if (n >= 2) dp[1] = s[0] + s[1];\n"
            "        if (n >= 3) dp[2] = Math.max(s[0] + s[2], s[1] + s[2]);\n"
            "        for (int i = 3; i < n; i++)\n"
            "            dp[i] = Math.max(dp[i - 2] + s[i], dp[i - 3] + s[i - 1] + s[i]);\n"
            "        System.out.println(dp[n - 1]);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "# 계단 오르기 : 밟은 칸 점수 합의 최댓값 (DP)\n"
            "n = int(input())\n"
            "s = [int(input()) for _ in range(n)]\n"
            "# ...\n"
        ),
    ),

    Problem(
        id="gold-07",
        rank="Gold",
        title="포도주 시식 최대량",
        style="백준",
        topic="DP",
        type="stdin",
        description=(
            "일렬로 놓인 포도주 잔이 있다. 잔을 선택하면 그 안의 포도주를 모두 마신다. "
            "단, 연속으로 놓인 세 잔을 모두 마실 수는 없다(건너뛰는 것은 자유). "
            "마실 수 있는 포도주 양의 최댓값을 구하시오. 계단 오르기와 달리 마지막 잔을 "
            "꼭 마실 필요는 없다."
        ),
        input_desc="첫째 줄 포도주 잔 수 N (1 ≤ N ≤ 10000), 다음 N개의 줄에 각 잔의 양(정수).",
        output_desc="마실 수 있는 포도주 양의 최댓값.",
        examples=[
            {"input": "6\n6\n10\n13\n9\n8\n1\n", "output": "33\n"},
            {"input": "3\n6\n10\n13\n", "output": "23\n"},
        ],
        hints=[
            "마지막 잔을 꼭 마시지 않아도 되므로, 각 칸에서 '마신다 / 마시지 않는다'를 모두 고려한 누적 최댓값이 필요합니다.",
            "1차원 DP. dp[i] = i번째 잔까지 봤을 때 마실 수 있는 최대량. i를 마시지 않거나, i만 마시거나, i-1과 i를 마시는 세 경우를 비교합니다.",
            "dp[i] = max(dp[i-1], dp[i-2]+w[i], dp[i-3]+w[i-1]+w[i]) 로 채우고 dp[N-1]을 출력.",
        ],
        testcases=[
            {"input": "6\n6\n10\n13\n9\n8\n1\n", "output": "33\n"},
            {"input": "3\n6\n10\n13\n", "output": "23\n"},
            {"input": "1\n6\n", "output": "6\n"},
            {"input": "2\n6\n10\n", "output": "16\n"},
            {"input": "4\n1\n2\n3\n4\n", "output": "8\n"},
        ],
        reference_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "n = int(input())\n"
            "w = [int(input()) for _ in range(n)]\n"
            "dp = [0] * n\n"
            "dp[0] = w[0]\n"
            "if n >= 2:\n"
            "    dp[1] = w[0] + w[1]\n"
            "if n >= 3:\n"
            "    dp[2] = max(dp[1], w[0] + w[2], w[1] + w[2])\n"
            "for i in range(3, n):\n"
            "    dp[i] = max(dp[i - 1], dp[i - 2] + w[i], dp[i - 3] + w[i - 1] + w[i])\n"
            "print(dp[n - 1])\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        int n = Integer.parseInt(br.readLine().trim());\n"
            "        int[] w = new int[n];\n"
            "        for (int i = 0; i < n; i++) w[i] = Integer.parseInt(br.readLine().trim());\n"
            "        int[] dp = new int[n];\n"
            "        dp[0] = w[0];\n"
            "        if (n >= 2) dp[1] = w[0] + w[1];\n"
            "        if (n >= 3) dp[2] = Math.max(dp[1], Math.max(w[0] + w[2], w[1] + w[2]));\n"
            "        for (int i = 3; i < n; i++)\n"
            "            dp[i] = Math.max(dp[i - 1], Math.max(dp[i - 2] + w[i], dp[i - 3] + w[i - 1] + w[i]));\n"
            "        System.out.println(dp[n - 1]);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "# 포도주 시식 : 최대량 (DP)\n"
            "n = int(input())\n"
            "w = [int(input()) for _ in range(n)]\n"
            "# ...\n"
        ),
    ),

    Problem(
        id="gold-08",
        rank="Gold",
        title="정수 삼각형 최대 경로",
        style="백준",
        topic="DP",
        type="stdin",
        description=(
            "맨 위 칸에서 시작해 아래로 내려가며 합을 최대로 만드는 경로를 찾는다. "
            "아래로 내려갈 때는 바로 아래 칸 또는 바로 아래 오른쪽 칸으로만 이동할 수 있다. "
            "거쳐 간 칸에 적힌 수들의 합의 최댓값을 구하시오."
        ),
        input_desc="첫째 줄 삼각형 크기 N (1 ≤ N ≤ 500), 다음 N개의 줄에 i번째 줄은 i개의 정수.",
        output_desc="맨 위에서 맨 아래까지 경로 합의 최댓값.",
        examples=[
            {"input": "5\n7\n3 8\n8 1 0\n2 7 4 4\n4 5 2 6 5\n", "output": "30\n"},
            {"input": "3\n1\n2 3\n4 5 6\n", "output": "10\n"},
        ],
        hints=[
            "위에서 아래로 모든 경로를 다 시도하면 지수 시간입니다. 아래쪽 결과를 알면 위쪽 칸의 최선이 결정됩니다.",
            "2차원 DP를 아래에서 위로 채웁니다. 각 칸에는 그 칸에서 바닥까지 갈 수 있는 최대 합을 누적합니다.",
            "맨 아랫줄부터 위로 올라오며 tri[i][j] += max(tri[i+1][j], tri[i+1][j+1]). 최종 tri[0][0]이 답.",
        ],
        testcases=[
            {"input": "5\n7\n3 8\n8 1 0\n2 7 4 4\n4 5 2 6 5\n", "output": "30\n"},
            {"input": "3\n1\n2 3\n4 5 6\n", "output": "10\n"},
            {"input": "1\n5\n", "output": "5\n"},
            {"input": "2\n1\n2 3\n", "output": "4\n"},
        ],
        reference_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "n = int(input())\n"
            "tri = [list(map(int, input().split())) for _ in range(n)]\n"
            "for i in range(n - 2, -1, -1):\n"
            "    for j in range(i + 1):\n"
            "        tri[i][j] += max(tri[i + 1][j], tri[i + 1][j + 1])\n"
            "print(tri[0][0])\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        int n = Integer.parseInt(br.readLine().trim());\n"
            "        int[][] tri = new int[n][];\n"
            "        for (int i = 0; i < n; i++) {\n"
            "            StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "            tri[i] = new int[i + 1];\n"
            "            for (int j = 0; j <= i; j++) tri[i][j] = Integer.parseInt(st.nextToken());\n"
            "        }\n"
            "        for (int i = n - 2; i >= 0; i--)\n"
            "            for (int j = 0; j <= i; j++)\n"
            "                tri[i][j] += Math.max(tri[i + 1][j], tri[i + 1][j + 1]);\n"
            "        System.out.println(tri[0][0]);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "# 정수 삼각형 : 경로 합 최댓값 (DP)\n"
            "n = int(input())\n"
            "tri = [list(map(int, input().split())) for _ in range(n)]\n"
            "# ...\n"
        ),
    ),

    Problem(
        id="gold-09",
        rank="Gold",
        title="연속 부분 수열 최대 합",
        style="해외대기업",
        topic="DP",
        type="func",
        func_name="solution",
        description=(
            "정수 배열 nums(음수 포함)가 주어진다. 연속한 부분 수열 중 원소 합이 가장 큰 값을 "
            "구하세요. 부분 수열은 비어 있을 수 없으며 최소 한 개의 원소를 포함합니다. "
            "예) [-2,1,-3,4,-1,2,1,-5,4] 의 최대 합은 부분 수열 [4,-1,2,1]에서 6입니다."
        ),
        input_desc="nums : 정수 리스트 (1 ≤ len ≤ 100000)",
        output_desc="연속 부분 수열 합의 최댓값(정수)",
        examples=[
            {"args": [[-2, 1, -3, 4, -1, 2, 1, -5, 4]], "output": 6},
            {"args": [[5, 4, -1, 7, 8]], "output": 23},
        ],
        hints=[
            "지금 보고 있는 원소에서 끝나는 연속합의 최댓값만 추적하면, 전체 최댓값을 한 번의 순회로 구할 수 있습니다.",
            "카데인(Kadane) 알고리즘. cur = 현재 원소로 끝나는 최대 연속합, best = 지금까지의 전체 최댓값.",
            "cur = max(x, cur + x); best = max(best, cur) 를 모든 x에 대해 갱신. 초기값은 nums[0].",
        ],
        testcases=[
            {"args": [[-2, 1, -3, 4, -1, 2, 1, -5, 4]], "expected": 6},
            {"args": [[5, 4, -1, 7, 8]], "expected": 23},
            {"args": [[5]], "expected": 5},
            {"args": [[-1, -2, -3]], "expected": -1},
            {"args": [[1, 2, 3, 4]], "expected": 10},
            {"args": [[-2, -1]], "expected": -1},
        ],
        reference_py=(
            "def solution(nums):\n"
            "    cur = best = nums[0]\n"
            "    for x in nums[1:]:\n"
            "        cur = max(x, cur + x)\n"
            "        best = max(best, cur)\n"
            "    return best\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int[] nums) {\n"
            "        int cur = nums[0], best = nums[0];\n"
            "        for (int i = 1; i < nums.length; i++) {\n"
            "            cur = Math.max(nums[i], cur + nums[i]);\n"
            "            best = Math.max(best, cur);\n"
            "        }\n"
            "        return best;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 연속 부분 수열 최대 합 (카데인)\n"
            "def solution(nums):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="gold-10",
        rank="Gold",
        title="2 x n 타일 채우기",
        style="백준",
        topic="DP",
        type="stdin",
        description=(
            "2×n 크기의 직사각형을 1×2, 2×1 타일로 빈틈없이 겹치지 않게 채우는 방법의 수를 "
            "구하시오. 경우의 수가 매우 커질 수 있으므로 10007로 나눈 나머지를 출력한다."
        ),
        input_desc="첫째 줄에 정수 n (1 ≤ n ≤ 1000).",
        output_desc="채우는 방법의 수를 10007로 나눈 나머지.",
        examples=[
            {"input": "2\n", "output": "2\n"},
            {"input": "9\n", "output": "55\n"},
        ],
        hints=[
            "가장 오른쪽 부분을 어떻게 마무리하는지 생각해 보세요. 세로 타일 1개로 끝내거나 가로 타일 2개로 끝내는 두 경우뿐입니다.",
            "1차원 DP이며 점화식이 피보나치 형태입니다. dp[i] = i 폭을 채우는 방법의 수.",
            "dp[1]=1, dp[2]=2, dp[i] = (dp[i-1] + dp[i-2]) % 10007 로 채워 dp[n]을 출력.",
        ],
        testcases=[
            {"input": "1\n", "output": "1\n"},
            {"input": "2\n", "output": "2\n"},
            {"input": "3\n", "output": "3\n"},
            {"input": "9\n", "output": "55\n"},
            {"input": "20\n", "output": "939\n"},
        ],
        reference_py=(
            "import sys\n"
            "n = int(sys.stdin.readline())\n"
            "MOD = 10007\n"
            "dp = [0] * (n + 1)\n"
            "dp[1] = 1\n"
            "if n >= 2:\n"
            "    dp[2] = 2\n"
            "for i in range(3, n + 1):\n"
            "    dp[i] = (dp[i - 1] + dp[i - 2]) % MOD\n"
            "print(dp[n])\n"
        ),
        reference_java=(
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        int n = Integer.parseInt(br.readLine().trim());\n"
            "        int MOD = 10007;\n"
            "        int[] dp = new int[n + 1];\n"
            "        dp[1] = 1;\n"
            "        if (n >= 2) dp[2] = 2;\n"
            "        for (int i = 3; i <= n; i++) dp[i] = (dp[i - 1] + dp[i - 2]) % MOD;\n"
            "        System.out.println(dp[n]);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "# 2 x n 타일링 방법의 수 (mod 10007)\n"
            "n = int(sys.stdin.readline())\n"
            "# ...\n"
        ),
    ),

    Problem(
        id="gold-11",
        rank="Gold",
        title="편집 거리 최소 연산",
        style="대기업",
        topic="DP",
        type="func",
        func_name="solution",
        description=(
            "문자열 a를 문자열 b로 바꾸는 데 필요한 최소 연산 횟수를 구하세요. 사용할 수 있는 "
            "연산은 (1) 문자 하나 삽입, (2) 문자 하나 삭제, (3) 문자 하나 교체 세 가지이며 "
            "각 연산의 비용은 1입니다."
        ),
        input_desc="a : 문자열, b : 문자열 (0 ≤ 길이 ≤ 1000)",
        output_desc="a를 b로 만드는 최소 연산 횟수(정수)",
        examples=[
            {"args": ["horse", "ros"], "output": 3},
            {"args": ["intention", "execution"], "output": 5},
        ],
        hints=[
            "a의 앞 i글자를 b의 앞 j글자로 바꾸는 부분 문제로 쪼개면, 마지막 글자를 어떻게 처리하느냐로 경우가 나뉩니다.",
            "2차원 DP. dp[i][j] = a[:i] 를 b[:j] 로 바꾸는 최소 비용. 마지막 글자가 같으면 그대로, 다르면 삽입/삭제/교체 중 최소.",
            "같으면 dp[i][j]=dp[i-1][j-1], 다르면 1+min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]). 경계는 dp[i][0]=i, dp[0][j]=j.",
        ],
        testcases=[
            {"args": ["horse", "ros"], "expected": 3},
            {"args": ["intention", "execution"], "expected": 5},
            {"args": ["", "abc"], "expected": 3},
            {"args": ["abc", ""], "expected": 3},
            {"args": ["abc", "abc"], "expected": 0},
            {"args": ["sunday", "saturday"], "expected": 3},
        ],
        reference_py=(
            "def solution(a, b):\n"
            "    m, n = len(a), len(b)\n"
            "    dp = [[0] * (n + 1) for _ in range(m + 1)]\n"
            "    for i in range(m + 1):\n"
            "        dp[i][0] = i\n"
            "    for j in range(n + 1):\n"
            "        dp[0][j] = j\n"
            "    for i in range(1, m + 1):\n"
            "        for j in range(1, n + 1):\n"
            "            if a[i - 1] == b[j - 1]:\n"
            "                dp[i][j] = dp[i - 1][j - 1]\n"
            "            else:\n"
            "                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])\n"
            "    return dp[m][n]\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(String a, String b) {\n"
            "        int m = a.length(), n = b.length();\n"
            "        int[][] dp = new int[m + 1][n + 1];\n"
            "        for (int i = 0; i <= m; i++) dp[i][0] = i;\n"
            "        for (int j = 0; j <= n; j++) dp[0][j] = j;\n"
            "        for (int i = 1; i <= m; i++)\n"
            "            for (int j = 1; j <= n; j++) {\n"
            "                if (a.charAt(i - 1) == b.charAt(j - 1)) dp[i][j] = dp[i - 1][j - 1];\n"
            "                else dp[i][j] = 1 + Math.min(dp[i - 1][j - 1], Math.min(dp[i - 1][j], dp[i][j - 1]));\n"
            "            }\n"
            "        return dp[m][n];\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 편집 거리 : 최소 연산 횟수 (2D DP)\n"
            "def solution(a, b):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="gold-12",
        rank="Gold",
        title="RGB 집 색칠 비용",
        style="프로그래머스",
        topic="DP",
        type="func",
        func_name="solution",
        description=(
            "일렬로 늘어선 집들을 빨강(R)·초록(G)·파랑(B) 중 하나로 칠한다. costs[i] = [r, g, b] 는 "
            "i번째 집을 각 색으로 칠하는 비용이다. 단, 이웃한 두 집은 서로 다른 색이어야 한다. "
            "모든 집을 칠하는 데 드는 최소 비용을 구하세요."
        ),
        input_desc="costs : 각 원소가 [r, g, b] 비용인 2차원 리스트 (1 ≤ 집 수 ≤ 1000)",
        output_desc="모든 집을 칠하는 최소 비용(정수)",
        examples=[
            {"args": [[[26, 40, 83], [49, 60, 57], [13, 89, 99]]], "output": 96},
            {"args": [[[1, 100, 100]]], "output": 1},
        ],
        hints=[
            "i번째 집의 색은 i-1번째 집의 색에만 영향을 받습니다. 직전 집을 각 색으로 칠했을 때의 누적 최소 비용을 들고 가세요.",
            "2차원 DP. dp[i][c] = i번째 집을 색 c로 칠했을 때 0~i번째까지의 최소 비용.",
            "dp[i][R]=costs[i][R]+min(dp[i-1][G],dp[i-1][B]) 처럼 자신과 다른 두 색의 최솟값을 더해 채우고, 마지막 줄의 최솟값을 반환.",
        ],
        testcases=[
            {"args": [[[26, 40, 83], [49, 60, 57], [13, 89, 99]]], "expected": 96},
            {"args": [[[1, 100, 100]]], "expected": 1},
            {"args": [[[1, 2, 3], [1, 2, 3]]], "expected": 3},
            {"args": [[[7, 3, 5], [4, 6, 8], [2, 9, 1]]], "expected": 8},
        ],
        reference_py=(
            "def solution(costs):\n"
            "    prev = costs[0][:]\n"
            "    for i in range(1, len(costs)):\n"
            "        cur = [0, 0, 0]\n"
            "        cur[0] = costs[i][0] + min(prev[1], prev[2])\n"
            "        cur[1] = costs[i][1] + min(prev[0], prev[2])\n"
            "        cur[2] = costs[i][2] + min(prev[0], prev[1])\n"
            "        prev = cur\n"
            "    return min(prev)\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int[][] costs) {\n"
            "        int[] prev = costs[0].clone();\n"
            "        for (int i = 1; i < costs.length; i++) {\n"
            "            int[] cur = new int[3];\n"
            "            cur[0] = costs[i][0] + Math.min(prev[1], prev[2]);\n"
            "            cur[1] = costs[i][1] + Math.min(prev[0], prev[2]);\n"
            "            cur[2] = costs[i][2] + Math.min(prev[0], prev[1]);\n"
            "            prev = cur;\n"
            "        }\n"
            "        return Math.min(prev[0], Math.min(prev[1], prev[2]));\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# RGB 거리 : 최소 색칠 비용 (DP)\n"
            "def solution(costs):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="gold-13",
        rank="Gold",
        title="가장 큰 정사각형 넓이",
        style="해외대기업",
        topic="DP",
        type="func",
        func_name="solution",
        description=(
            "0과 1로 이루어진 2차원 행렬 matrix가 주어진다. 1로만 채워진 가장 큰 정사각형을 찾아 "
            "그 넓이(한 변 길이의 제곱)를 반환하세요. 1이 하나도 없으면 0을 반환합니다."
        ),
        input_desc="matrix : 각 원소가 0 또는 1(int)인 2차원 리스트",
        output_desc="1로만 이루어진 가장 큰 정사각형의 넓이(정수)",
        examples=[
            {"args": [[[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]], "output": 4},
            {"args": [[[0, 1], [1, 0]]], "output": 1},
        ],
        hints=[
            "어떤 칸을 정사각형의 오른쪽 아래 꼭짓점이라고 보면, 그 칸까지 만들 수 있는 정사각형 변의 길이가 정해집니다.",
            "2차원 DP. dp[i][j] = (i, j)를 우하단 꼭짓점으로 하는 가장 큰 정사각형의 변 길이.",
            "matrix[i][j]==1 이면 dp[i][j]=min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1. 최대 변 길이의 제곱이 답.",
        ],
        testcases=[
            {"args": [[[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]], "expected": 4},
            {"args": [[[0, 1], [1, 0]]], "expected": 1},
            {"args": [[[0]]], "expected": 0},
            {"args": [[[1]]], "expected": 1},
            {"args": [[[1, 1], [1, 1]]], "expected": 4},
            {"args": [[[0, 0], [0, 0]]], "expected": 0},
        ],
        reference_py=(
            "def solution(matrix):\n"
            "    if not matrix or not matrix[0]:\n"
            "        return 0\n"
            "    m, n = len(matrix), len(matrix[0])\n"
            "    dp = [[0] * n for _ in range(m)]\n"
            "    best = 0\n"
            "    for i in range(m):\n"
            "        for j in range(n):\n"
            "            if matrix[i][j] == 1:\n"
            "                if i == 0 or j == 0:\n"
            "                    dp[i][j] = 1\n"
            "                else:\n"
            "                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1\n"
            "                if dp[i][j] > best:\n"
            "                    best = dp[i][j]\n"
            "    return best * best\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int[][] matrix) {\n"
            "        if (matrix.length == 0 || matrix[0].length == 0) return 0;\n"
            "        int m = matrix.length, n = matrix[0].length, best = 0;\n"
            "        int[][] dp = new int[m][n];\n"
            "        for (int i = 0; i < m; i++)\n"
            "            for (int j = 0; j < n; j++)\n"
            "                if (matrix[i][j] == 1) {\n"
            "                    if (i == 0 || j == 0) dp[i][j] = 1;\n"
            "                    else dp[i][j] = Math.min(dp[i - 1][j], Math.min(dp[i][j - 1], dp[i - 1][j - 1])) + 1;\n"
            "                    best = Math.max(best, dp[i][j]);\n"
            "                }\n"
            "        return best * best;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 가장 큰 정사각형 넓이 (2D DP)\n"
            "def solution(matrix):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="gold-14",
        rank="Gold",
        title="장애물 격자 경로 수",
        style="프로그래머스",
        topic="DP",
        type="func",
        func_name="solution",
        description=(
            "로봇이 격자의 왼쪽 위 칸에서 출발해 오른쪽 아래 칸까지 이동한다. 한 번에 오른쪽 또는 "
            "아래로만 한 칸씩 갈 수 있다. grid의 값이 0이면 빈 칸, 1이면 장애물이라 지날 수 없다. "
            "출발점에서 도착점까지 가는 서로 다른 경로의 수를 구하세요."
        ),
        input_desc="grid : 각 원소가 0(빈 칸) 또는 1(장애물)인 2차원 리스트",
        output_desc="왼쪽 위에서 오른쪽 아래까지 가는 경로의 수(정수)",
        examples=[
            {"args": [[[0, 0, 0], [0, 1, 0], [0, 0, 0]]], "output": 2},
            {"args": [[[0, 1], [0, 0]]], "output": 1},
        ],
        hints=[
            "어떤 칸에 도달하는 경로 수는 그 칸의 위쪽 칸과 왼쪽 칸으로 들어오는 경로 수의 합입니다.",
            "2차원 DP. dp[i][j] = (i, j)에 도달하는 경로 수. 장애물 칸은 0으로 둡니다.",
            "grid[i][j]==1 이면 dp[i][j]=0, 아니면 dp[i][j]=dp[i-1][j]+dp[i][j-1] (경계는 한쪽만). 시작칸이 장애물이면 답은 0.",
        ],
        testcases=[
            {"args": [[[0, 0, 0], [0, 1, 0], [0, 0, 0]]], "expected": 2},
            {"args": [[[0, 1], [0, 0]]], "expected": 1},
            {"args": [[[0]]], "expected": 1},
            {"args": [[[1]]], "expected": 0},
            {"args": [[[0, 0, 0], [0, 0, 0], [0, 0, 0]]], "expected": 6},
        ],
        reference_py=(
            "def solution(grid):\n"
            "    m, n = len(grid), len(grid[0])\n"
            "    dp = [[0] * n for _ in range(m)]\n"
            "    for i in range(m):\n"
            "        for j in range(n):\n"
            "            if grid[i][j] == 1:\n"
            "                dp[i][j] = 0\n"
            "            elif i == 0 and j == 0:\n"
            "                dp[i][j] = 1\n"
            "            else:\n"
            "                up = dp[i - 1][j] if i > 0 else 0\n"
            "                left = dp[i][j - 1] if j > 0 else 0\n"
            "                dp[i][j] = up + left\n"
            "    return dp[m - 1][n - 1]\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int[][] grid) {\n"
            "        int m = grid.length, n = grid[0].length;\n"
            "        int[][] dp = new int[m][n];\n"
            "        for (int i = 0; i < m; i++)\n"
            "            for (int j = 0; j < n; j++) {\n"
            "                if (grid[i][j] == 1) dp[i][j] = 0;\n"
            "                else if (i == 0 && j == 0) dp[i][j] = 1;\n"
            "                else {\n"
            "                    int up = i > 0 ? dp[i - 1][j] : 0;\n"
            "                    int left = j > 0 ? dp[i][j - 1] : 0;\n"
            "                    dp[i][j] = up + left;\n"
            "                }\n"
            "            }\n"
            "        return dp[m - 1][n - 1];\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 장애물 격자 경로 수 (2D DP)\n"
            "def solution(grid):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="gold-15",
        rank="Gold",
        title="부분집합 합 존재 판별",
        style="대기업",
        topic="DP",
        type="func",
        func_name="solution",
        description=(
            "음이 아닌 정수 리스트 nums가 있다. 이 중 일부 원소(0개 이상)를 골라 합이 정확히 "
            "target이 되도록 만들 수 있으면 True, 불가능하면 False를 반환하세요. (배낭 변형 — "
            "부분집합 합 판별)"
        ),
        input_desc="nums : 음이 아닌 정수 리스트, target : 음이 아닌 정수",
        output_desc="합이 target인 부분집합이 존재하면 True, 없으면 False",
        examples=[
            {"args": [[3, 34, 4, 12, 5, 2], 9], "output": True},
            {"args": [[3, 34, 4, 12, 5, 2], 30], "output": False},
        ],
        hints=[
            "각 원소를 '고른다 / 안 고른다'로 나누는 0/1 배낭과 같은 구조입니다. 다만 가치가 아니라 특정 합의 도달 가능 여부만 추적합니다.",
            "1차원 불리언 DP. dp[s] = 합 s를 만들 수 있으면 True. 각 원소마다 큰 합부터 갱신합니다.",
            "dp[0]=True; for x in nums: for s in range(target, x-1, -1): if dp[s-x]: dp[s]=True. 답은 dp[target].",
        ],
        testcases=[
            {"args": [[3, 34, 4, 12, 5, 2], 9], "expected": True},
            {"args": [[3, 34, 4, 12, 5, 2], 30], "expected": False},
            {"args": [[1, 2, 3], 0], "expected": True},
            {"args": [[1, 5, 11, 5], 11], "expected": True},
            {"args": [[2, 4, 6], 5], "expected": False},
            {"args": [[], 0], "expected": True},
        ],
        reference_py=(
            "def solution(nums, target):\n"
            "    if target < 0:\n"
            "        return False\n"
            "    dp = [False] * (target + 1)\n"
            "    dp[0] = True\n"
            "    for x in nums:\n"
            "        for s in range(target, x - 1, -1):\n"
            "            if dp[s - x]:\n"
            "                dp[s] = True\n"
            "    return dp[target]\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public boolean solution(int[] nums, int target) {\n"
            "        if (target < 0) return false;\n"
            "        boolean[] dp = new boolean[target + 1];\n"
            "        dp[0] = true;\n"
            "        for (int x : nums)\n"
            "            for (int s = target; s >= x; s--)\n"
            "                if (dp[s - x]) dp[s] = true;\n"
            "        return dp[target];\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 부분집합 합 존재 판별 (배낭 변형)\n"
            "def solution(nums, target):\n"
            "    answer = False\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="gold-16",
        rank="Gold",
        title="동전 조합 경우의 수",
        style="백준",
        topic="DP",
        type="stdin",
        description=(
            "n가지 종류의 동전이 있고 각 동전을 원하는 만큼 사용할 수 있다. 이 동전들을 사용해 "
            "그 가치의 합이 k가 되는 경우의 수를 구하시오. 동전을 사용하는 순서는 구분하지 않는다. "
            "(예: 1원+2원과 2원+1원은 같은 경우)"
        ),
        input_desc="첫째 줄 동전 종류 수 n과 목표 금액 k (1 ≤ n ≤ 100, 1 ≤ k ≤ 10000), 다음 n개의 줄에 각 동전의 가치.",
        output_desc="합이 k가 되는 경우의 수.",
        examples=[
            {"input": "3 10\n1\n2\n5\n", "output": "10\n"},
            {"input": "2 4\n1\n2\n", "output": "3\n"},
        ],
        hints=[
            "순서를 구분하지 않으려면 동전을 한 종류씩 차례로 도입하면서 누적해야 같은 조합을 중복으로 세지 않습니다.",
            "1차원 DP. dp[j] = 금액 j를 만드는 경우의 수. 동전마다 작은 금액부터 갱신(무한 개 사용 가능한 배낭).",
            "dp[0]=1; for c in coins: for j in range(c, k+1): dp[j]+=dp[j-c]. 답은 dp[k].",
        ],
        testcases=[
            {"input": "3 10\n1\n2\n5\n", "output": "10\n"},
            {"input": "1 5\n1\n", "output": "1\n"},
            {"input": "2 5\n2\n5\n", "output": "1\n"},
            {"input": "1 5\n3\n", "output": "0\n"},
            {"input": "2 4\n1\n2\n", "output": "3\n"},
        ],
        reference_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "n, k = map(int, input().split())\n"
            "coins = [int(input()) for _ in range(n)]\n"
            "dp = [0] * (k + 1)\n"
            "dp[0] = 1\n"
            "for c in coins:\n"
            "    for j in range(c, k + 1):\n"
            "        dp[j] += dp[j - c]\n"
            "print(dp[k])\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int n = Integer.parseInt(st.nextToken()), k = Integer.parseInt(st.nextToken());\n"
            "        int[] coins = new int[n];\n"
            "        for (int i = 0; i < n; i++) coins[i] = Integer.parseInt(br.readLine().trim());\n"
            "        int[] dp = new int[k + 1];\n"
            "        dp[0] = 1;\n"
            "        for (int c : coins)\n"
            "            for (int j = c; j <= k; j++)\n"
            "                dp[j] += dp[j - c];\n"
            "        System.out.println(dp[k]);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "# 동전 조합 경우의 수 (DP)\n"
            "n, k = map(int, input().split())\n"
            "coins = [int(input()) for _ in range(n)]\n"
            "# ...\n"
        ),
    ),

    Problem(
        id="gold-17",
        rank="Gold",
        title="최장 공통 부분 수열 길이",
        style="해외대기업",
        topic="DP",
        type="func",
        func_name="solution",
        description=(
            "두 문자열 a, b가 주어진다. 두 문자열 모두에서 (연속이 아니어도 되지만) 순서를 지켜 "
            "공통으로 뽑을 수 있는 가장 긴 부분 수열의 길이를 구하세요. 예) \"ACAYKP\"와 "
            "\"CAPCAK\"의 최장 공통 부분 수열은 \"ACAK\"로 길이 4입니다."
        ),
        input_desc="a : 문자열, b : 문자열 (0 ≤ 길이 ≤ 1000)",
        output_desc="최장 공통 부분 수열의 길이(정수)",
        examples=[
            {"args": ["ACAYKP", "CAPCAK"], "output": 4},
            {"args": ["abcde", "ace"], "output": 3},
        ],
        hints=[
            "두 문자열의 앞부분끼리 비교하는 부분 문제로 나눕니다. 끝 글자가 같은지 다른지에 따라 경우가 갈립니다.",
            "2차원 DP. dp[i][j] = a[:i]와 b[:j]의 최장 공통 부분 수열 길이.",
            "a[i-1]==b[j-1] 이면 dp[i][j]=dp[i-1][j-1]+1, 아니면 max(dp[i-1][j], dp[i][j-1]). 답은 dp[len(a)][len(b)].",
        ],
        testcases=[
            {"args": ["ACAYKP", "CAPCAK"], "expected": 4},
            {"args": ["abcde", "ace"], "expected": 3},
            {"args": ["abc", "def"], "expected": 0},
            {"args": ["", "abc"], "expected": 0},
            {"args": ["abc", "abc"], "expected": 3},
        ],
        reference_py=(
            "def solution(a, b):\n"
            "    m, n = len(a), len(b)\n"
            "    dp = [[0] * (n + 1) for _ in range(m + 1)]\n"
            "    for i in range(1, m + 1):\n"
            "        for j in range(1, n + 1):\n"
            "            if a[i - 1] == b[j - 1]:\n"
            "                dp[i][j] = dp[i - 1][j - 1] + 1\n"
            "            else:\n"
            "                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])\n"
            "    return dp[m][n]\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(String a, String b) {\n"
            "        int m = a.length(), n = b.length();\n"
            "        int[][] dp = new int[m + 1][n + 1];\n"
            "        for (int i = 1; i <= m; i++)\n"
            "            for (int j = 1; j <= n; j++) {\n"
            "                if (a.charAt(i - 1) == b.charAt(j - 1)) dp[i][j] = dp[i - 1][j - 1] + 1;\n"
            "                else dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);\n"
            "            }\n"
            "        return dp[m][n];\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 최장 공통 부분 수열 길이 (LCS, 2D DP)\n"
            "def solution(a, b):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="gold-18",
        rank="Gold",
        title="연속 부분 수열 최대 곱",
        style="해외대기업",
        topic="DP",
        type="func",
        func_name="solution",
        description=(
            "정수 배열 nums(음수·0 포함)가 주어진다. 연속한 부분 수열 중 원소들의 곱이 가장 큰 값을 "
            "구하세요. 부분 수열은 최소 한 개의 원소를 포함합니다. 음수가 두 번 곱해지면 양수가 "
            "되므로 최댓값뿐 아니라 최솟값도 함께 추적해야 합니다."
        ),
        input_desc="nums : 정수 리스트 (1 ≤ len ≤ 20000)",
        output_desc="연속 부분 수열 곱의 최댓값(정수)",
        examples=[
            {"args": [[2, 3, -2, 4]], "output": 6},
            {"args": [[-2, 3, -4]], "output": 24},
        ],
        hints=[
            "합과 달리 곱에서는 음수를 만나면 최대와 최소가 뒤바뀝니다. 그래서 현재 원소로 끝나는 최댓값과 최솟값을 동시에 들고 가야 합니다.",
            "변형 카데인. cur_max, cur_min 두 값을 유지하고 음수를 만나면 둘을 바꿔 곱합니다.",
            "각 x마다 후보 {x, cur_max*x, cur_min*x} 중 cur_max=최댓값, cur_min=최솟값으로 갱신하고 정답에 cur_max를 반영.",
        ],
        testcases=[
            {"args": [[2, 3, -2, 4]], "expected": 6},
            {"args": [[-2, 3, -4]], "expected": 24},
            {"args": [[-2, 0, -1]], "expected": 0},
            {"args": [[2]], "expected": 2},
            {"args": [[-3]], "expected": -3},
            {"args": [[0, 2]], "expected": 2},
        ],
        reference_py=(
            "def solution(nums):\n"
            "    cur_max = cur_min = ans = nums[0]\n"
            "    for x in nums[1:]:\n"
            "        cands = (x, cur_max * x, cur_min * x)\n"
            "        cur_max = max(cands)\n"
            "        cur_min = min(cands)\n"
            "        ans = max(ans, cur_max)\n"
            "    return ans\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int[] nums) {\n"
            "        int curMax = nums[0], curMin = nums[0], ans = nums[0];\n"
            "        for (int i = 1; i < nums.length; i++) {\n"
            "            int x = nums[i];\n"
            "            int a = x, b = curMax * x, c = curMin * x;\n"
            "            curMax = Math.max(a, Math.max(b, c));\n"
            "            curMin = Math.min(a, Math.min(b, c));\n"
            "            ans = Math.max(ans, curMax);\n"
            "        }\n"
            "        return ans;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 연속 부분 수열 최대 곱 (변형 카데인)\n"
            "def solution(nums):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="gold-19",
        rank="Gold",
        title="이친수 개수 세기",
        style="백준",
        topic="DP",
        type="stdin",
        description=(
            "0과 1로 이루어진 수를 이진수라 한다. 다음 두 조건을 만족하는 이진수를 '이친수'라 한다. "
            "(1) 0으로 시작하지 않는다. (2) 1이 두 번 연속해서 나타나지 않는다(즉 11을 포함하지 않는다). "
            "N자리 이친수의 개수를 구하시오. 결과가 매우 클 수 있다."
        ),
        input_desc="첫째 줄에 정수 N (1 ≤ N ≤ 90).",
        output_desc="N자리 이친수의 개수.",
        examples=[
            {"input": "3\n", "output": "2\n"},
            {"input": "1\n", "output": "1\n"},
        ],
        hints=[
            "각 자리에 0이 오는 경우와 1이 오는 경우로 나누되, 1 다음에는 1이 올 수 없다는 제약을 상태에 담아야 합니다.",
            "마지막 자리가 0으로 끝나는 개수와 1로 끝나는 개수를 따로 관리하는 DP를 씁니다.",
            "zero, one = 0, 1 에서 시작해 매 자리마다 (zero, one) = (zero + one, zero) 로 갱신하고, 마지막에 zero + one 을 출력. (값이 크니 64비트/큰 정수 사용)",
        ],
        testcases=[
            {"input": "1\n", "output": "1\n"},
            {"input": "2\n", "output": "1\n"},
            {"input": "3\n", "output": "2\n"},
            {"input": "5\n", "output": "5\n"},
            {"input": "90\n", "output": "2880067194370816120\n"},
        ],
        reference_py=(
            "import sys\n"
            "n = int(sys.stdin.readline())\n"
            "zero, one = 0, 1\n"
            "for _ in range(n - 1):\n"
            "    zero, one = zero + one, zero\n"
            "print(zero + one)\n"
        ),
        reference_java=(
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        int n = Integer.parseInt(br.readLine().trim());\n"
            "        long zero = 0, one = 1;\n"
            "        for (int i = 0; i < n - 1; i++) {\n"
            "            long nz = zero + one, no = zero;\n"
            "            zero = nz; one = no;\n"
            "        }\n"
            "        System.out.println(zero + one);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "# 이친수 개수 (DP)\n"
            "n = int(sys.stdin.readline())\n"
            "# ...\n"
        ),
    ),

    Problem(
        id="gold-20",
        rank="Gold",
        title="최장 회문 부분 수열",
        style="해외대기업",
        topic="DP",
        type="func",
        func_name="solution",
        description=(
            "문자열 s가 주어진다. s에서 (연속이 아니어도 되지만) 순서를 지켜 뽑아 만들 수 있는 "
            "가장 긴 '회문(앞뒤로 읽어도 같은 문자열)' 부분 수열의 길이를 구하세요. 예) "
            "\"bbbab\"의 최장 회문 부분 수열은 \"bbbb\"로 길이 4입니다."
        ),
        input_desc="s : 문자열 (0 ≤ 길이 ≤ 1000)",
        output_desc="최장 회문 부분 수열의 길이(정수)",
        examples=[
            {"args": ["bbbab"], "output": 4},
            {"args": ["cbbd"], "output": 2},
        ],
        hints=[
            "구간 [i, j]를 부분 문제로 보고, 양 끝 글자가 같은지 다른지에 따라 안쪽 구간의 답을 이용합니다.",
            "구간 DP. dp[i][j] = s[i..j] 구간의 최장 회문 부분 수열 길이. 구간 길이를 늘려가며 채웁니다.",
            "s[i]==s[j] 이면 dp[i][j]=dp[i+1][j-1]+2, 아니면 max(dp[i+1][j], dp[i][j-1]). 길이 1 구간은 1로 초기화하고 dp[0][n-1] 반환.",
        ],
        testcases=[
            {"args": ["bbbab"], "expected": 4},
            {"args": ["cbbd"], "expected": 2},
            {"args": ["a"], "expected": 1},
            {"args": [""], "expected": 0},
            {"args": ["abcba"], "expected": 5},
            {"args": ["agbdba"], "expected": 5},
        ],
        reference_py=(
            "def solution(s):\n"
            "    n = len(s)\n"
            "    if n == 0:\n"
            "        return 0\n"
            "    dp = [[0] * n for _ in range(n)]\n"
            "    for i in range(n):\n"
            "        dp[i][i] = 1\n"
            "    for length in range(2, n + 1):\n"
            "        for i in range(n - length + 1):\n"
            "            j = i + length - 1\n"
            "            if s[i] == s[j]:\n"
            "                dp[i][j] = (dp[i + 1][j - 1] if length > 2 else 0) + 2\n"
            "            else:\n"
            "                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])\n"
            "    return dp[0][n - 1]\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(String s) {\n"
            "        int n = s.length();\n"
            "        if (n == 0) return 0;\n"
            "        int[][] dp = new int[n][n];\n"
            "        for (int i = 0; i < n; i++) dp[i][i] = 1;\n"
            "        for (int len = 2; len <= n; len++)\n"
            "            for (int i = 0; i + len - 1 < n; i++) {\n"
            "                int j = i + len - 1;\n"
            "                if (s.charAt(i) == s.charAt(j))\n"
            "                    dp[i][j] = (len > 2 ? dp[i + 1][j - 1] : 0) + 2;\n"
            "                else dp[i][j] = Math.max(dp[i + 1][j], dp[i][j - 1]);\n"
            "            }\n"
            "        return dp[0][n - 1];\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 최장 회문 부분 수열 길이 (구간 DP)\n"
            "def solution(s):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

]
