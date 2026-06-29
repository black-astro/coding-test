"""유형 보강 배치 — DP / 비트마스킹 / 분할 정복 / 누적합.

같은 유형을 쉬운 랭크와 어려운 랭크로 나누어 배치한다.
- 1D DP        : Silver(gd-01) + Gold(gd-02)
- 2D 격자 DP   : Silver(gd-03) + Gold(gd-04)
- 배낭         : Silver(gd-05) + Gold(gd-06)
- 비트마스킹   : Silver 기초(gd-07) + Gold DP(gd-08)
- 누적합       : Silver 1D(gd-09) + Gold 2D(gd-10)
- 분할 정복    : Gold(gd-11)
- 구간 DP      : Platinum(gd-12)

gd-01 ~ gd-12.
"""

from engine.models import Problem

PROBLEMS = [

    # ------------------------------------------------------------------
    # 1D DP — Silver
    Problem(
        id="gd-01",
        rank="Silver",
        tier="S3",
        category="DP",
        title="계단 오르기 경우의 수",
        style="대기업",
        topic="1차원 DP",
        type="func",
        func_name="solution",
        description=(
            "한 번에 한 칸 또는 두 칸씩 계단을 오를 수 있다. 총 n개의 계단을 오르는 "
            "서로 다른 방법의 수를 구하세요. n이 0이면 오를 계단이 없으므로 방법은 1가지(가만히 있기)로 본다."
        ),
        input_desc="n : int (0 ≤ n ≤ 40)",
        output_desc="n개의 계단을 오르는 서로 다른 방법의 수",
        examples=[
            {"args": [5], "output": 8},
            {"args": [1], "output": 1},
        ],
        hints=[
            "마지막 한 걸음은 '한 칸 올라왔거나' '두 칸 올라온' 두 경우뿐입니다. 그 직전 상태의 방법 수를 더하면 됩니다.",
            "dp[i] = i번째 계단까지 오르는 방법의 수. dp[i] = dp[i-1] + dp[i-2] (피보나치 형태).",
            "dp[0]=1, dp[1]=1; for i in 2..n: dp[i]=dp[i-1]+dp[i-2]; 답은 dp[n].",
        ],
        testcases=[
            {"args": [5], "expected": 8},
            {"args": [1], "expected": 1},
            {"args": [0], "expected": 1},
            {"args": [2], "expected": 2},
            {"args": [3], "expected": 3},
            {"args": [10], "expected": 89},
        ],
        reference_py=(
            "def solution(n):\n"
            "    dp = [0] * (n + 2)\n"
            "    dp[0] = 1\n"
            "    dp[1] = 1\n"
            "    for i in range(2, n + 1):\n"
            "        dp[i] = dp[i - 1] + dp[i - 2]\n"
            "    return dp[n]\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public long solution(int n) {\n"
            "        long[] dp = new long[n + 2];\n"
            "        dp[0] = 1; dp[1] = 1;\n"
            "        for (int i = 2; i <= n; i++) dp[i] = dp[i - 1] + dp[i - 2];\n"
            "        return dp[n];\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp="",
        template_py=(
            "# 계단 오르기 경우의 수 (1차원 DP)\n"
            "def solution(n):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    # ------------------------------------------------------------------
    # 1D DP — Gold
    Problem(
        id="gd-02",
        rank="Gold",
        tier="G5",
        category="DP",
        title="포도주 시식 최대량",
        style="백준",
        topic="1차원 DP",
        type="stdin",
        description=(
            "일렬로 놓인 포도주 잔이 있다. 각 잔에는 정해진 양의 포도주가 담겨 있다. "
            "잔을 선택해 마시되, 연속으로 놓인 세 잔을 모두 마실 수는 없다(연속 두 잔까지는 가능). "
            "마실 수 있는 포도주 양의 최댓값을 구하시오."
        ),
        input_desc=(
            "첫째 줄에 포도주 잔의 개수 N (1 ≤ N ≤ 10000). "
            "다음 N개의 줄에 각 잔에 담긴 포도주의 양(0 이상의 정수)이 한 줄에 하나씩 주어진다."
        ),
        output_desc="마실 수 있는 포도주 양의 최댓값을 한 줄에 출력한다.",
        examples=[
            {"input": "6\n6\n10\n13\n9\n8\n1\n", "output": "33\n"},
            {"input": "3\n1\n2\n3\n", "output": "5\n"},
        ],
        hints=[
            "현재 잔을 '안 마시는 경우'와 '마시는 경우'를 나누되, 마실 때는 직전 두 잔을 연속으로 마셨는지가 중요합니다.",
            "dp[i] = i번째 잔까지 봤을 때의 최대량. i번째를 마신다면 직전(i-1)만 마시거나, 직전을 건너뛰고 i를 마시는 식으로 경우를 나눕니다.",
            "dp[i] = max(dp[i-1], dp[i-2]+a[i], dp[i-3]+a[i-1]+a[i]). 경계(i<3)는 직접 처리하고 답은 dp[N-1].",
        ],
        testcases=[
            {"input": "6\n6\n10\n13\n9\n8\n1\n", "output": "33\n"},
            {"input": "3\n1\n2\n3\n", "output": "5\n"},
            {"input": "1\n100\n", "output": "100\n"},
            {"input": "2\n100\n100\n", "output": "200\n"},
            {"input": "3\n1\n1\n1\n", "output": "2\n"},
        ],
        reference_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "n = int(input())\n"
            "a = [int(input()) for _ in range(n)]\n"
            "dp = [0] * n\n"
            "dp[0] = a[0]\n"
            "if n >= 2:\n"
            "    dp[1] = a[0] + a[1]\n"
            "if n >= 3:\n"
            "    dp[2] = max(a[2] + a[1], a[2] + a[0], dp[1])\n"
            "for i in range(3, n):\n"
            "    dp[i] = max(dp[i - 1], dp[i - 2] + a[i], dp[i - 3] + a[i - 1] + a[i])\n"
            "print(dp[n - 1])\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        int n = Integer.parseInt(br.readLine().trim());\n"
            "        int[] a = new int[n];\n"
            "        for (int i = 0; i < n; i++) a[i] = Integer.parseInt(br.readLine().trim());\n"
            "        int[] dp = new int[n];\n"
            "        dp[0] = a[0];\n"
            "        if (n >= 2) dp[1] = a[0] + a[1];\n"
            "        if (n >= 3) dp[2] = Math.max(a[2] + a[1], Math.max(a[2] + a[0], dp[1]));\n"
            "        for (int i = 3; i < n; i++)\n"
            "            dp[i] = Math.max(dp[i - 1], Math.max(dp[i - 2] + a[i], dp[i - 3] + a[i - 1] + a[i]));\n"
            "        System.out.println(dp[n - 1]);\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp="",
        template_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "# 포도주 시식 : 연속 3잔 금지, 최대량 (1차원 DP)\n"
            "n = int(input())\n"
            "# ...\n"
        ),
    ),

    # ------------------------------------------------------------------
    # 2D 격자 DP — Silver
    Problem(
        id="gd-03",
        rank="Silver",
        tier="S2",
        category="DP",
        title="격자 경로의 수",
        style="대기업",
        topic="2차원 격자 DP",
        type="func",
        func_name="solution",
        description=(
            "n행 m열의 격자가 있다. 왼쪽 위 칸 (1,1)에서 출발해 오른쪽 또는 아래로만 한 칸씩 이동하여 "
            "오른쪽 아래 칸 (n,m)까지 가는 서로 다른 경로의 수를 구하세요."
        ),
        input_desc="n : 행 수, m : 열 수 (1 ≤ n, m ≤ 30)",
        output_desc="(1,1)에서 (n,m)까지 가는 서로 다른 경로의 수",
        examples=[
            {"args": [3, 3], "output": 6},
            {"args": [2, 2], "output": 2},
        ],
        hints=[
            "어떤 칸에 도달하는 방법은 '바로 위 칸에서 내려오는 경우'와 '바로 왼쪽 칸에서 오는 경우'의 합입니다.",
            "dp[i][j] = (i,j)까지 가는 경로 수. 첫 행과 첫 열은 모두 1(직진뿐)로 둡니다.",
            "dp[i][j] = dp[i-1][j] + dp[i][j-1]. 답은 dp[n-1][m-1] (0-based).",
        ],
        testcases=[
            {"args": [3, 3], "expected": 6},
            {"args": [2, 2], "expected": 2},
            {"args": [1, 1], "expected": 1},
            {"args": [1, 5], "expected": 1},
            {"args": [2, 3], "expected": 3},
            {"args": [3, 7], "expected": 28},
        ],
        reference_py=(
            "def solution(n, m):\n"
            "    dp = [[1] * m for _ in range(n)]\n"
            "    for i in range(1, n):\n"
            "        for j in range(1, m):\n"
            "            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]\n"
            "    return dp[n - 1][m - 1]\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public long solution(int n, int m) {\n"
            "        long[][] dp = new long[n][m];\n"
            "        for (int i = 0; i < n; i++) dp[i][0] = 1;\n"
            "        for (int j = 0; j < m; j++) dp[0][j] = 1;\n"
            "        for (int i = 1; i < n; i++)\n"
            "            for (int j = 1; j < m; j++)\n"
            "                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];\n"
            "        return dp[n - 1][m - 1];\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp="",
        template_py=(
            "# 격자 경로의 수 (2차원 격자 DP)\n"
            "def solution(n, m):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    # ------------------------------------------------------------------
    # 2D 격자 DP — Gold
    Problem(
        id="gd-04",
        rank="Gold",
        tier="G4",
        category="DP",
        title="장애물 격자 최대 점수 경로",
        style="해외대기업",
        topic="2차원 격자 DP",
        type="func",
        func_name="solution",
        description=(
            "n x m 격자의 각 칸에는 점수가 적혀 있다. 단, 값이 -1인 칸은 벽이라 지나갈 수 없다. "
            "왼쪽 위 (0,0)에서 출발해 오른쪽 또는 아래로만 이동하여 오른쪽 아래 (n-1,m-1)까지 갈 때 "
            "지나온 칸의 점수 합을 최대로 하는 값을 구하세요. 도달이 불가능하면 -1을 반환합니다."
        ),
        input_desc="grid : n x m 정수 격자 (칸 값은 점수, -1은 벽)",
        output_desc="최대 점수 합. 도달 불가능하면 -1",
        examples=[
            {"args": [[[1, 3, 1], [1, 5, 1], [4, 2, 1]]], "output": 12},
            {"args": [[[1, -1], [1, 1]]], "output": 3},
        ],
        hints=[
            "어떤 칸의 최대 점수는 '위 칸까지의 최대'와 '왼쪽 칸까지의 최대' 중 큰 값에 현재 점수를 더한 것입니다.",
            "도달 불가능을 표현하려면 -무한대 같은 sentinel을 쓰세요. 벽 칸이나 양쪽 모두 막힌 칸은 도달 불가로 둡니다.",
            "dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j], 단 들어온 경로가 하나라도 유효할 때만. 마지막 칸이 -무한대면 -1.",
        ],
        testcases=[
            {"args": [[[1, 3, 1], [1, 5, 1], [4, 2, 1]]], "expected": 12},
            {"args": [[[1, -1], [1, 1]]], "expected": 3},
            {"args": [[[5]]], "expected": 5},
            {"args": [[[1, -1], [-1, 1]]], "expected": -1},
            {"args": [[[0, 0, 0], [0, 0, 0]]], "expected": 0},
            {"args": [[[2, 2, 2], [2, -1, 2], [2, 2, 2]]], "expected": 10},
        ],
        reference_py=(
            "def solution(grid):\n"
            "    n = len(grid)\n"
            "    m = len(grid[0])\n"
            "    NEG = float('-inf')\n"
            "    dp = [[NEG] * m for _ in range(n)]\n"
            "    if grid[0][0] == -1:\n"
            "        return -1\n"
            "    dp[0][0] = grid[0][0]\n"
            "    for i in range(n):\n"
            "        for j in range(m):\n"
            "            if grid[i][j] == -1 or (i == 0 and j == 0):\n"
            "                continue\n"
            "            best = NEG\n"
            "            if i > 0 and dp[i - 1][j] != NEG:\n"
            "                best = max(best, dp[i - 1][j])\n"
            "            if j > 0 and dp[i][j - 1] != NEG:\n"
            "                best = max(best, dp[i][j - 1])\n"
            "            if best != NEG:\n"
            "                dp[i][j] = best + grid[i][j]\n"
            "    return dp[n - 1][m - 1] if dp[n - 1][m - 1] != NEG else -1\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int[][] grid) {\n"
            "        int n = grid.length, m = grid[0].length;\n"
            "        final int NEG = Integer.MIN_VALUE;\n"
            "        int[][] dp = new int[n][m];\n"
            "        for (int[] row : dp) java.util.Arrays.fill(row, NEG);\n"
            "        if (grid[0][0] == -1) return -1;\n"
            "        dp[0][0] = grid[0][0];\n"
            "        for (int i = 0; i < n; i++)\n"
            "            for (int j = 0; j < m; j++) {\n"
            "                if (grid[i][j] == -1 || (i == 0 && j == 0)) continue;\n"
            "                int best = NEG;\n"
            "                if (i > 0 && dp[i - 1][j] != NEG) best = Math.max(best, dp[i - 1][j]);\n"
            "                if (j > 0 && dp[i][j - 1] != NEG) best = Math.max(best, dp[i][j - 1]);\n"
            "                if (best != NEG) dp[i][j] = best + grid[i][j];\n"
            "            }\n"
            "        return dp[n - 1][m - 1] != NEG ? dp[n - 1][m - 1] : -1;\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp="",
        template_py=(
            "# 장애물 격자 최대 점수 경로 (2차원 격자 DP)\n"
            "def solution(grid):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    # ------------------------------------------------------------------
    # 배낭 — Silver
    Problem(
        id="gd-05",
        rank="Silver",
        tier="S1",
        category="DP",
        title="부분집합 합 만들기",
        style="대기업",
        topic="배낭(부분집합 합)",
        type="func",
        func_name="solution",
        description=(
            "음이 아닌 정수 리스트 nums 와 목표값 target 이 주어진다. nums 의 원소 중 일부(또는 전부, "
            "또는 아무것도 안 고름)를 골라 그 합이 정확히 target 이 되게 할 수 있으면 True, "
            "불가능하면 False 를 반환하세요."
        ),
        input_desc="nums : 음이 아닌 정수 리스트, target : 음이 아닌 정수 (0 ≤ target ≤ 10000)",
        output_desc="합이 정확히 target 인 부분집합이 존재하면 True, 아니면 False",
        examples=[
            {"args": [[3, 34, 4, 12, 5, 2], 9], "output": True},
            {"args": [[1, 2, 5], 4], "output": False},
        ],
        hints=[
            "각 원소를 '쓴다/안 쓴다'로 나누면, 만들 수 있는 합의 집합이 점점 커집니다. 어떤 합이 가능한지 표로 관리하세요.",
            "1차원 배낭 DP를 쓰세요. possible[s] = 합 s를 만들 수 있는가. 처음엔 possible[0]만 True.",
            "각 x마다 s를 target부터 x까지 '내려가며' possible[s] |= possible[s-x]. 답은 possible[target].",
        ],
        testcases=[
            {"args": [[3, 34, 4, 12, 5, 2], 9], "expected": True},
            {"args": [[1, 2, 5], 4], "expected": False},
            {"args": [[], 0], "expected": True},
            {"args": [[2, 4], 0], "expected": True},
            {"args": [[5], 3], "expected": False},
            {"args": [[1, 1, 1], 2], "expected": True},
        ],
        reference_py=(
            "def solution(nums, target):\n"
            "    possible = [False] * (target + 1)\n"
            "    possible[0] = True\n"
            "    for x in nums:\n"
            "        if x > target:\n"
            "            continue\n"
            "        for s in range(target, x - 1, -1):\n"
            "            if possible[s - x]:\n"
            "                possible[s] = True\n"
            "    return possible[target]\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public boolean solution(int[] nums, int target) {\n"
            "        boolean[] possible = new boolean[target + 1];\n"
            "        possible[0] = true;\n"
            "        for (int x : nums) {\n"
            "            if (x > target) continue;\n"
            "            for (int s = target; s >= x; s--)\n"
            "                if (possible[s - x]) possible[s] = true;\n"
            "        }\n"
            "        return possible[target];\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp="",
        template_py=(
            "# 부분집합 합 만들기 (배낭 / 부분집합 합 DP)\n"
            "def solution(nums, target):\n"
            "    answer = False\n"
            "    return answer\n"
        ),
    ),

    # ------------------------------------------------------------------
    # 배낭 — Gold
    Problem(
        id="gd-06",
        rank="Gold",
        tier="G3",
        category="DP",
        title="동전 교환 최소 개수",
        style="백준",
        topic="배낭(무한 배낭)",
        type="stdin",
        description=(
            "서로 다른 종류의 동전이 있고 각 동전은 무한히 사용할 수 있다. 동전들을 조합해 "
            "금액 K를 정확히 만들 때 필요한 동전 개수의 최솟값을 구하시오. 만들 수 없으면 -1을 출력한다."
        ),
        input_desc=(
            "첫째 줄에 동전 종류 수 N과 목표 금액 K (1 ≤ N ≤ 100, 0 ≤ K ≤ 100000). "
            "둘째 줄에 N개의 동전 가치가 공백으로 주어진다(각 1 이상)."
        ),
        output_desc="금액 K를 만드는 데 필요한 최소 동전 개수. 불가능하면 -1.",
        examples=[
            {"input": "3 11\n1 2 5\n", "output": "3\n"},
            {"input": "1 3\n2\n", "output": "-1\n"},
        ],
        hints=[
            "금액 a를 만드는 최소 개수는, 어떤 동전 c를 마지막에 한 개 쓴다고 가정하면 (a-c를 만드는 최소 개수)+1 입니다.",
            "무한 배낭 DP를 쓰세요. dp[a] = 금액 a를 만드는 최소 동전 수. 동전을 무한히 쓰므로 a를 '작은 쪽부터' 키우며 갱신합니다.",
            "dp[0]=0, 나머지는 무한대. 각 동전 c마다 a를 c..K로 올리며 dp[a]=min(dp[a], dp[a-c]+1). 답은 dp[K] (무한대면 -1).",
        ],
        testcases=[
            {"input": "3 11\n1 2 5\n", "output": "3\n"},
            {"input": "1 3\n2\n", "output": "-1\n"},
            {"input": "3 0\n1 2 5\n", "output": "0\n"},
            {"input": "2 6\n1 3\n", "output": "2\n"},
            {"input": "3 27\n1 5 10\n", "output": "5\n"},
        ],
        reference_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "n, k = map(int, input().split())\n"
            "coins = list(map(int, input().split()))\n"
            "INF = float('inf')\n"
            "dp = [0] + [INF] * k\n"
            "for c in coins:\n"
            "    for a in range(c, k + 1):\n"
            "        if dp[a - c] + 1 < dp[a]:\n"
            "            dp[a] = dp[a - c] + 1\n"
            "print(dp[k] if dp[k] != INF else -1)\n"
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
            "        int[] coins = new int[n];\n"
            "        st = new StringTokenizer(br.readLine());\n"
            "        for (int i = 0; i < n; i++) coins[i] = Integer.parseInt(st.nextToken());\n"
            "        final int INF = 1 << 29;\n"
            "        int[] dp = new int[k + 1];\n"
            "        Arrays.fill(dp, INF);\n"
            "        dp[0] = 0;\n"
            "        for (int c : coins)\n"
            "            for (int a = c; a <= k; a++)\n"
            "                if (dp[a - c] + 1 < dp[a]) dp[a] = dp[a - c] + 1;\n"
            "        System.out.println(dp[k] != INF ? dp[k] : -1);\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp="",
        template_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "# 동전 교환 : 금액 K를 만드는 최소 동전 수 (무한 배낭)\n"
            "n, k = map(int, input().split())\n"
            "# ...\n"
        ),
    ),

    # ------------------------------------------------------------------
    # 비트마스킹 기초 — Silver
    Problem(
        id="gd-07",
        rank="Silver",
        tier="S2",
        category="비트마스킹",
        title="부분집합 합 개수 세기",
        style="대기업",
        topic="비트마스킹 기초",
        type="func",
        func_name="solution",
        description=(
            "정수 리스트 nums 와 목표값 target 이 주어진다. nums 의 모든 부분집합(공집합 포함)을 "
            "비트마스크로 하나씩 만들어 보며, 원소들의 합이 정확히 target 이 되는 부분집합의 개수를 구하세요. "
            "(같은 인덱스 조합이면 값이 같아도 서로 다른 부분집합으로 셉니다)"
        ),
        input_desc="nums : 정수 리스트 (0 ≤ len ≤ 18), target : 정수",
        output_desc="원소 합이 target 인 부분집합의 개수",
        examples=[
            {"args": [[1, 2, 3, 4], 5], "output": 2},
            {"args": [[1, 1, 1], 2], "output": 3},
        ],
        hints=[
            "원소가 n개면 부분집합은 2^n개입니다. 0부터 2^n-1까지의 정수 하나가 부분집합 하나에 대응합니다.",
            "정수 mask의 i번째 비트가 1이면 'i번째 원소를 포함'한다고 보세요. mask & (1<<i) 로 포함 여부를 확인합니다.",
            "for mask in range(1<<n): 비트가 켜진 원소들의 합을 구하고, target과 같으면 카운트. 답은 그 카운트.",
        ],
        testcases=[
            {"args": [[1, 2, 3, 4], 5], "expected": 2},
            {"args": [[1, 1, 1], 2], "expected": 3},
            {"args": [[], 0], "expected": 1},
            {"args": [[5], 5], "expected": 1},
            {"args": [[1, 2, 3], 6], "expected": 1},
            {"args": [[2, 4, 6], 5], "expected": 0},
        ],
        reference_py=(
            "def solution(nums, target):\n"
            "    n = len(nums)\n"
            "    count = 0\n"
            "    for mask in range(1 << n):\n"
            "        s = 0\n"
            "        for i in range(n):\n"
            "            if mask & (1 << i):\n"
            "                s += nums[i]\n"
            "        if s == target:\n"
            "            count += 1\n"
            "    return count\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int[] nums, int target) {\n"
            "        int n = nums.length, count = 0;\n"
            "        for (int mask = 0; mask < (1 << n); mask++) {\n"
            "            int s = 0;\n"
            "            for (int i = 0; i < n; i++)\n"
            "                if ((mask & (1 << i)) != 0) s += nums[i];\n"
            "            if (s == target) count++;\n"
            "        }\n"
            "        return count;\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp="",
        template_py=(
            "# 부분집합 합 개수 세기 (비트마스킹 기초)\n"
            "def solution(nums, target):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    # ------------------------------------------------------------------
    # 비트마스킹 DP — Gold
    Problem(
        id="gd-08",
        rank="Gold",
        tier="G2",
        category="비트마스킹",
        title="작업 배정 최소 비용",
        style="해외대기업",
        topic="비트마스킹 DP",
        type="func",
        func_name="solution",
        description=(
            "N명의 작업자와 N개의 작업이 있다. cost[i][j] 는 i번 작업자가 j번 작업을 맡을 때 드는 비용이다. "
            "각 작업자는 정확히 하나의 작업을, 각 작업은 정확히 한 명에게 배정된다. 전체 비용 합을 "
            "최소로 하는 값을 구하세요. (1 ≤ N ≤ 18)"
        ),
        input_desc="cost : N x N 비용 행렬",
        output_desc="모든 작업자에게 작업을 하나씩 배정했을 때 비용 합의 최솟값",
        examples=[
            {"args": [[[9, 2, 7, 8], [6, 4, 3, 7], [5, 8, 1, 8], [7, 6, 9, 4]]], "output": 13},
            {"args": [[[3, 2], [1, 4]]], "output": 3},
        ],
        hints=[
            "작업자 0부터 순서대로 작업을 배정한다고 하면, '지금까지 어떤 작업들이 이미 쓰였는지'만 알면 됩니다.",
            "비트마스킹 DP를 쓰세요. mask의 켜진 비트 = 이미 배정된 작업 집합. 그 켜진 비트 수가 곧 지금 배정할 작업자 번호입니다.",
            "dp[mask] = 그 작업 집합을 쓰도록 배정한 최소 비용. i=popcount(mask); for j not in mask: dp[mask|1<<j]=min(.., dp[mask]+cost[i][j]). 답은 dp[(1<<N)-1].",
        ],
        testcases=[
            {"args": [[[9, 2, 7, 8], [6, 4, 3, 7], [5, 8, 1, 8], [7, 6, 9, 4]]], "expected": 13},
            {"args": [[[3, 2], [1, 4]]], "expected": 3},
            {"args": [[[42]]], "expected": 42},
            {"args": [[[10, 20, 30], [40, 50, 60], [70, 80, 90]]], "expected": 150},
            {"args": [[[1, 1], [1, 1]]], "expected": 2},
        ],
        reference_py=(
            "def solution(cost):\n"
            "    n = len(cost)\n"
            "    INF = float('inf')\n"
            "    dp = [INF] * (1 << n)\n"
            "    dp[0] = 0\n"
            "    for mask in range(1 << n):\n"
            "        if dp[mask] == INF:\n"
            "            continue\n"
            "        i = bin(mask).count('1')\n"
            "        if i >= n:\n"
            "            continue\n"
            "        for j in range(n):\n"
            "            if not (mask & (1 << j)):\n"
            "                nm = mask | (1 << j)\n"
            "                v = dp[mask] + cost[i][j]\n"
            "                if v < dp[nm]:\n"
            "                    dp[nm] = v\n"
            "    return dp[(1 << n) - 1]\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int[][] cost) {\n"
            "        int n = cost.length;\n"
            "        final int INF = 1 << 29;\n"
            "        int[] dp = new int[1 << n];\n"
            "        java.util.Arrays.fill(dp, INF);\n"
            "        dp[0] = 0;\n"
            "        for (int mask = 0; mask < (1 << n); mask++) {\n"
            "            if (dp[mask] == INF) continue;\n"
            "            int i = Integer.bitCount(mask);\n"
            "            if (i >= n) continue;\n"
            "            for (int j = 0; j < n; j++) {\n"
            "                if ((mask & (1 << j)) != 0) continue;\n"
            "                int nm = mask | (1 << j);\n"
            "                int v = dp[mask] + cost[i][j];\n"
            "                if (v < dp[nm]) dp[nm] = v;\n"
            "            }\n"
            "        }\n"
            "        return dp[(1 << n) - 1];\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp="",
        template_py=(
            "# 작업 배정 최소 비용 (비트마스킹 DP)\n"
            "def solution(cost):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    # ------------------------------------------------------------------
    # 누적합 1D — Silver
    Problem(
        id="gd-09",
        rank="Silver",
        tier="S3",
        category="누적합",
        title="구간 합 질의",
        style="백준",
        topic="1차원 누적합",
        type="stdin",
        description=(
            "정수 N개로 이루어진 수열이 있고, 여러 개의 질의가 주어진다. 각 질의는 두 정수 i, j (i ≤ j)로 "
            "이루어지며, i번째 수부터 j번째 수까지의 합을 구해 출력해야 한다(인덱스는 1부터 시작)."
        ),
        input_desc=(
            "첫째 줄에 수의 개수 N과 질의 수 Q (1 ≤ N, Q ≤ 100000). "
            "둘째 줄에 N개의 정수. 이어서 Q개의 줄에 각각 i j가 주어진다."
        ),
        output_desc="각 질의에 대한 구간 합을 한 줄에 하나씩 출력한다.",
        examples=[
            {"input": "5 3\n1 2 3 4 5\n1 3\n2 4\n1 5\n", "output": "6\n9\n15\n"},
            {"input": "4 2\n10 20 30 40\n2 2\n1 4\n", "output": "20\n100\n"},
        ],
        hints=[
            "질의마다 구간을 직접 더하면 느립니다. 누적합을 한 번 만들어 두면 각 질의를 뺄셈 한 번으로 처리할 수 있습니다.",
            "pre[k] = 앞에서부터 k개의 합. 그러면 i..j 구간 합은 pre[j] - pre[i-1] 입니다.",
            "pre[0]=0; for k in 1..N: pre[k]=pre[k-1]+a[k-1]. 각 질의는 pre[j]-pre[i-1].",
        ],
        testcases=[
            {"input": "5 3\n1 2 3 4 5\n1 3\n2 4\n1 5\n", "output": "6\n9\n15\n"},
            {"input": "4 2\n10 20 30 40\n2 2\n1 4\n", "output": "20\n100\n"},
            {"input": "1 1\n7\n1 1\n", "output": "7\n"},
            {"input": "3 1\n-1 -2 -3\n1 3\n", "output": "-6\n"},
            {"input": "5 2\n5 5 5 5 5\n3 3\n2 5\n", "output": "5\n20\n"},
        ],
        reference_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "n, q = map(int, input().split())\n"
            "a = list(map(int, input().split()))\n"
            "pre = [0] * (n + 1)\n"
            "for k in range(1, n + 1):\n"
            "    pre[k] = pre[k - 1] + a[k - 1]\n"
            "out = []\n"
            "for _ in range(q):\n"
            "    i, j = map(int, input().split())\n"
            "    out.append(str(pre[j] - pre[i - 1]))\n"
            "print('\\n'.join(out))\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int n = Integer.parseInt(st.nextToken());\n"
            "        int q = Integer.parseInt(st.nextToken());\n"
            "        long[] pre = new long[n + 1];\n"
            "        st = new StringTokenizer(br.readLine());\n"
            "        for (int k = 1; k <= n; k++)\n"
            "            pre[k] = pre[k - 1] + Long.parseLong(st.nextToken());\n"
            "        StringBuilder sb = new StringBuilder();\n"
            "        for (int t = 0; t < q; t++) {\n"
            "            st = new StringTokenizer(br.readLine());\n"
            "            int i = Integer.parseInt(st.nextToken());\n"
            "            int j = Integer.parseInt(st.nextToken());\n"
            "            sb.append(pre[j] - pre[i - 1]).append('\\n');\n"
            "        }\n"
            "        System.out.print(sb);\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp="",
        template_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "# 구간 합 질의 (1차원 누적합)\n"
            "n, q = map(int, input().split())\n"
            "# ...\n"
        ),
    ),

    # ------------------------------------------------------------------
    # 2D 누적합 — Gold
    Problem(
        id="gd-10",
        rank="Gold",
        tier="G3",
        category="누적합",
        title="부분 행렬 합 질의",
        style="백준",
        topic="2차원 누적합",
        type="stdin",
        description=(
            "N x M 크기의 정수 행렬이 주어지고 여러 질의가 들어온다. 각 질의는 네 정수 "
            "r1, c1, r2, c2 로 이루어지며, (r1,c1)을 왼쪽 위, (r2,c2)를 오른쪽 아래로 하는 "
            "직사각형 영역에 포함된 모든 원소의 합을 출력한다(행·열 인덱스는 1부터)."
        ),
        input_desc=(
            "첫째 줄에 N M (1 ≤ N, M ≤ 1000). 다음 N개의 줄에 M개씩 정수. "
            "그 다음 줄에 질의 수 Q. 이어서 Q개의 줄에 r1 c1 r2 c2."
        ),
        output_desc="각 질의에 대한 부분 행렬 합을 한 줄에 하나씩 출력한다.",
        examples=[
            {"input": "3 3\n1 2 3\n4 5 6\n7 8 9\n2\n1 1 2 2\n2 2 3 3\n", "output": "12\n28\n"},
            {"input": "2 2\n1 1\n1 1\n1\n1 1 2 2\n", "output": "4\n"},
        ],
        hints=[
            "1차원 누적합을 2차원으로 확장합니다. pre[i][j] = (1,1)부터 (i,j)까지 직사각형 영역의 합.",
            "pre[i][j] = a[i][j] + pre[i-1][j] + pre[i][j-1] - pre[i-1][j-1] (겹치는 부분을 한 번 빼줌).",
            "질의 합 = pre[r2][c2] - pre[r1-1][c2] - pre[r2][c1-1] + pre[r1-1][c1-1] (포함-배제).",
        ],
        testcases=[
            {"input": "3 3\n1 2 3\n4 5 6\n7 8 9\n2\n1 1 2 2\n2 2 3 3\n", "output": "12\n28\n"},
            {"input": "2 2\n1 1\n1 1\n1\n1 1 2 2\n", "output": "4\n"},
            {"input": "3 3\n1 2 3\n4 5 6\n7 8 9\n1\n1 1 3 3\n", "output": "45\n"},
            {"input": "1 1\n5\n1\n1 1 1 1\n", "output": "5\n"},
            {"input": "3 3\n1 2 3\n4 5 6\n7 8 9\n1\n2 2 2 2\n", "output": "5\n"},
        ],
        reference_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "n, m = map(int, input().split())\n"
            "g = [list(map(int, input().split())) for _ in range(n)]\n"
            "pre = [[0] * (m + 1) for _ in range(n + 1)]\n"
            "for i in range(1, n + 1):\n"
            "    for j in range(1, m + 1):\n"
            "        pre[i][j] = g[i - 1][j - 1] + pre[i - 1][j] + pre[i][j - 1] - pre[i - 1][j - 1]\n"
            "q = int(input())\n"
            "out = []\n"
            "for _ in range(q):\n"
            "    r1, c1, r2, c2 = map(int, input().split())\n"
            "    s = pre[r2][c2] - pre[r1 - 1][c2] - pre[r2][c1 - 1] + pre[r1 - 1][c1 - 1]\n"
            "    out.append(str(s))\n"
            "print('\\n'.join(out))\n"
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
            "        long[][] pre = new long[n + 1][m + 1];\n"
            "        for (int i = 1; i <= n; i++) {\n"
            "            st = new StringTokenizer(br.readLine());\n"
            "            for (int j = 1; j <= m; j++) {\n"
            "                long v = Long.parseLong(st.nextToken());\n"
            "                pre[i][j] = v + pre[i - 1][j] + pre[i][j - 1] - pre[i - 1][j - 1];\n"
            "            }\n"
            "        }\n"
            "        int q = Integer.parseInt(br.readLine().trim());\n"
            "        StringBuilder sb = new StringBuilder();\n"
            "        for (int t = 0; t < q; t++) {\n"
            "            st = new StringTokenizer(br.readLine());\n"
            "            int r1 = Integer.parseInt(st.nextToken());\n"
            "            int c1 = Integer.parseInt(st.nextToken());\n"
            "            int r2 = Integer.parseInt(st.nextToken());\n"
            "            int c2 = Integer.parseInt(st.nextToken());\n"
            "            long s = pre[r2][c2] - pre[r1 - 1][c2] - pre[r2][c1 - 1] + pre[r1 - 1][c1 - 1];\n"
            "            sb.append(s).append('\\n');\n"
            "        }\n"
            "        System.out.print(sb);\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp="",
        template_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "# 부분 행렬 합 질의 (2차원 누적합)\n"
            "n, m = map(int, input().split())\n"
            "# ...\n"
        ),
    ),

    # ------------------------------------------------------------------
    # 분할 정복 — Gold
    Problem(
        id="gd-11",
        rank="Gold",
        tier="G4",
        category="분할정복",
        title="거듭제곱 나머지 (분할 정복)",
        style="백준",
        topic="분할 정복",
        type="func",
        func_name="solution",
        description=(
            "정수 a, b, m 이 주어진다. a 의 b 제곱을 m 으로 나눈 나머지, 즉 (a^b) mod m 을 구하세요. "
            "b 가 매우 클 수 있으므로 지수를 절반씩 나누는 분할 정복(빠른 거듭제곱)으로 계산해야 한다."
        ),
        input_desc="a : 밑 (a ≥ 0), b : 지수 (b ≥ 0), m : 나누는 수 (m ≥ 1)",
        output_desc="(a^b) mod m 의 값",
        examples=[
            {"args": [2, 10, 1000], "output": 24},
            {"args": [10, 11, 1000000007], "output": 999999307},
        ],
        hints=[
            "a^b 를 b번 곱하면 b가 클 때 너무 느립니다. b를 절반으로 나누는 성질 a^b = (a^(b/2))^2 을 이용하세요.",
            "분할 정복으로 power(b)를 구합니다. b가 짝수면 (power(b/2))^2, 홀수면 거기에 a를 한 번 더 곱합니다. 매 단계 mod 를 취하세요.",
            "power(e): if e==0 return 1%m; h=power(e//2); h=h*h%m; if e가 홀수: h=h*(a%m)%m; return h.",
        ],
        testcases=[
            {"args": [2, 10, 1000], "expected": 24},
            {"args": [10, 11, 1000000007], "expected": 999999307},
            {"args": [3, 0, 100], "expected": 1},
            {"args": [2, 1, 5], "expected": 2},
            {"args": [7, 2, 10], "expected": 9},
            {"args": [123, 456, 1000], "expected": 561},
        ],
        reference_py=(
            "def solution(a, b, m):\n"
            "    def power(e):\n"
            "        if e == 0:\n"
            "            return 1 % m\n"
            "        h = power(e // 2)\n"
            "        h = h * h % m\n"
            "        if e % 2 == 1:\n"
            "            h = h * (a % m) % m\n"
            "        return h\n"
            "    return power(b)\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    long m;\n"
            "    long a;\n"
            "    public long solution(long a, long b, long m) {\n"
            "        this.a = a; this.m = m;\n"
            "        return power(b);\n"
            "    }\n"
            "    long power(long e) {\n"
            "        if (e == 0) return 1 % m;\n"
            "        long h = power(e / 2);\n"
            "        h = h * h % m;\n"
            "        if (e % 2 == 1) h = h * (a % m) % m;\n"
            "        return h;\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp="",
        template_py=(
            "# 거듭제곱 나머지 : (a^b) mod m (분할 정복)\n"
            "def solution(a, b, m):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    # ------------------------------------------------------------------
    # 구간 DP — Platinum
    Problem(
        id="gd-12",
        rank="Platinum",
        tier="P5",
        category="DP",
        title="풍선 터뜨리기 최대 점수",
        style="해외대기업",
        topic="구간 DP",
        type="func",
        func_name="solution",
        description=(
            "일렬로 놓인 풍선이 있고 각 풍선에는 숫자가 적혀 있다. 풍선 i를 터뜨리면 "
            "(왼쪽 인접 풍선 숫자) x (i 숫자) x (오른쪽 인접 풍선 숫자) 만큼 점수를 얻는다. "
            "터지면 그 자리는 사라지고 양옆이 새로 인접해진다. 배열 밖은 숫자 1로 친다. "
            "모든 풍선을 터뜨려 얻는 점수 합의 최댓값을 구하세요."
        ),
        input_desc="nums : 풍선에 적힌 정수 리스트 (0 ≤ len ≤ 300, 각 원소는 0 이상)",
        output_desc="모든 풍선을 터뜨려 얻을 수 있는 점수 합의 최댓값",
        examples=[
            {"args": [[3, 1, 5, 8]], "output": 167},
            {"args": [[1, 5]], "output": 10},
        ],
        hints=[
            "어떤 풍선을 '먼저' 터뜨릴지 정하면 양옆 상태가 얽혀 어렵습니다. 대신 구간 안에서 '마지막에' 터지는 풍선을 기준으로 나눠 보세요.",
            "양 끝에 1을 덧붙인 배열에서 구간 DP를 쓰세요. dp[l][r] = 양 끝 l, r은 남겨둔 채 (l,r) 사이를 모두 터뜨릴 때의 최대 점수.",
            "dp[l][r] = max over k in (l,r) ( a[l]*a[k]*a[r] + dp[l][k] + dp[k][r] ). k가 그 구간에서 마지막에 터지는 풍선. 답은 dp[0][n-1].",
        ],
        testcases=[
            {"args": [[3, 1, 5, 8]], "expected": 167},
            {"args": [[1, 5]], "expected": 10},
            {"args": [[5]], "expected": 5},
            {"args": [[7]], "expected": 7},
            {"args": [[1, 2, 3]], "expected": 12},
            {"args": [[]], "expected": 0},
        ],
        reference_py=(
            "def solution(nums):\n"
            "    a = [1] + list(nums) + [1]\n"
            "    n = len(a)\n"
            "    dp = [[0] * n for _ in range(n)]\n"
            "    for length in range(2, n):\n"
            "        for left in range(0, n - length):\n"
            "            right = left + length\n"
            "            best = 0\n"
            "            for k in range(left + 1, right):\n"
            "                v = a[left] * a[k] * a[right] + dp[left][k] + dp[k][right]\n"
            "                if v > best:\n"
            "                    best = v\n"
            "            dp[left][right] = best\n"
            "    return dp[0][n - 1]\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int[] nums) {\n"
            "        int n = nums.length + 2;\n"
            "        int[] a = new int[n];\n"
            "        a[0] = 1; a[n - 1] = 1;\n"
            "        for (int i = 0; i < nums.length; i++) a[i + 1] = nums[i];\n"
            "        int[][] dp = new int[n][n];\n"
            "        for (int len = 2; len < n; len++)\n"
            "            for (int left = 0; left + len < n; left++) {\n"
            "                int right = left + len, best = 0;\n"
            "                for (int k = left + 1; k < right; k++) {\n"
            "                    int v = a[left] * a[k] * a[right] + dp[left][k] + dp[k][right];\n"
            "                    if (v > best) best = v;\n"
            "                }\n"
            "                dp[left][right] = best;\n"
            "            }\n"
            "        return dp[0][n - 1];\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp="",
        template_py=(
            "# 풍선 터뜨리기 최대 점수 (구간 DP)\n"
            "def solution(nums):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

]
