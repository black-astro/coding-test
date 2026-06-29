"""플래티넘 추가 배치 A — 고급 DP 15문제.

구간 DP(파일 합치기·행렬 곱셈 순서·팰린드롬), 트리 DP(독립집합),
비트마스크 DP(외판원 순회·집합 분할), 자릿수 DP, 슬라이딩/누적 DP 등.

platinum-06 ~ platinum-20.
"""

from engine.models import Problem

RANK = "Platinum"

PROBLEMS = [

    # ------------------------------------------------------------------
    Problem(
        id="platinum-06",
        rank="Platinum",
        title="파일 합치기 (구간 DP)",
        style="백준",
        topic="구간DP",
        type="stdin",
        description=(
            "N개의 파일이 한 줄로 놓여 있다. 인접한 두 파일을 합치면 두 파일 크기의 합만큼 비용이 들고, "
            "합쳐진 결과는 다시 하나의 파일이 된다. 모든 파일을 하나로 합칠 때 드는 비용의 최솟값을 구하시오. "
            "(반드시 인접한 파일끼리만 합칠 수 있다)"
        ),
        input_desc="첫째 줄에 파일 개수 N (1 ≤ N ≤ 100). 둘째 줄에 각 파일의 크기 N개가 공백으로 주어진다.",
        output_desc="모든 파일을 하나로 합치는 데 드는 최소 비용을 한 줄에 출력한다.",
        examples=[
            {"input": "4\n40 30 30 50\n", "output": "300\n"},
            {"input": "3\n10 20 30\n", "output": "90\n"},
        ],
        hints=[
            "어떤 순서로 합치느냐에 따라 비용이 달라집니다. 구간 [i..j]를 하나로 합치는 최소 비용을 작은 구간부터 채워 보세요.",
            "구간 DP를 쓰세요. dp[i][j] = i번째부터 j번째 파일을 하나로 합치는 최소 비용. 구간 합은 누적합으로 미리 구합니다.",
            "dp[i][j] = min over k in [i,j-1] ( dp[i][k] + dp[k+1][j] ) + (i..j 구간 합). 길이 1 구간은 0, 답은 dp[0][N-1].",
        ],
        testcases=[
            {"input": "4\n40 30 30 50\n", "output": "300\n"},
            {"input": "3\n10 20 30\n", "output": "90\n"},
            {"input": "1\n5\n", "output": "0\n"},
            {"input": "2\n5 5\n", "output": "10\n"},
            {"input": "5\n10 20 30 40 50\n", "output": "330\n"},
        ],
        reference_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "n = int(input())\n"
            "a = list(map(int, input().split()))\n"
            "pre = [0] * (n + 1)\n"
            "for i in range(n):\n"
            "    pre[i + 1] = pre[i] + a[i]\n"
            "INF = float('inf')\n"
            "dp = [[0] * n for _ in range(n)]\n"
            "for length in range(2, n + 1):\n"
            "    for i in range(0, n - length + 1):\n"
            "        j = i + length - 1\n"
            "        dp[i][j] = INF\n"
            "        s = pre[j + 1] - pre[i]\n"
            "        for k in range(i, j):\n"
            "            cost = dp[i][k] + dp[k + 1][j] + s\n"
            "            if cost < dp[i][j]:\n"
            "                dp[i][j] = cost\n"
            "print(dp[0][n - 1])\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        int n = Integer.parseInt(br.readLine().trim());\n"
            "        int[] a = new int[n];\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        for (int i = 0; i < n; i++) a[i] = Integer.parseInt(st.nextToken());\n"
            "        int[] pre = new int[n + 1];\n"
            "        for (int i = 0; i < n; i++) pre[i + 1] = pre[i] + a[i];\n"
            "        int[][] dp = new int[n][n];\n"
            "        for (int len = 2; len <= n; len++)\n"
            "            for (int i = 0; i + len - 1 < n; i++) {\n"
            "                int j = i + len - 1; dp[i][j] = Integer.MAX_VALUE;\n"
            "                int s = pre[j + 1] - pre[i];\n"
            "                for (int k = i; k < j; k++)\n"
            "                    dp[i][j] = Math.min(dp[i][j], dp[i][k] + dp[k + 1][j] + s);\n"
            "            }\n"
            "        System.out.println(dp[0][n - 1]);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "# 파일 합치기 : 구간 DP로 최소 합치기 비용\n"
            "n = int(input())\n"
            "a = list(map(int, input().split()))\n"
            "# ...\n"
        ),
    ),

    # ------------------------------------------------------------------
    Problem(
        id="platinum-07",
        rank="Platinum",
        title="행렬 곱셈 순서 (체인)",
        style="해외대기업",
        topic="구간DP",
        type="func",
        func_name="solution",
        description=(
            "여러 개의 행렬을 곱할 때, 곱하는 순서(괄호 묶는 방법)에 따라 필요한 곱셈 연산 횟수가 달라진다. "
            "행렬 차원 배열 p 가 주어진다. i번째 행렬의 크기는 p[i-1] x p[i] 이며 행렬은 총 len(p)-1개다. "
            "모든 행렬을 곱하는 데 필요한 스칼라 곱셈 횟수의 최솟값을 구하세요."
        ),
        input_desc="p : 차원 리스트 (길이 ≥ 2). 행렬 개수는 len(p)-1, i번째 행렬 크기는 p[i-1] x p[i].",
        output_desc="모든 행렬을 곱하는 데 필요한 최소 스칼라 곱셈 횟수",
        examples=[
            {"args": [[10, 30, 5, 60]], "output": 4500},
            {"args": [[30, 35, 15, 5, 10, 20, 25]], "output": 15125},
        ],
        hints=[
            "두 행렬 (a x b) x (b x c) 를 곱하면 a*b*c 번의 곱셈이 듭니다. 어디를 마지막에 곱할지(분할점)를 정하는 문제입니다.",
            "구간 DP를 쓰세요. dp[i][j] = i번째부터 j번째 행렬까지 곱하는 최소 비용. 마지막 곱을 k에서 끊습니다.",
            "dp[i][j] = min over k in [i,j-1] ( dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j] ). 행렬 1개면 0, 답은 dp[1][m].",
        ],
        testcases=[
            {"args": [[10, 30, 5, 60]], "expected": 4500},
            {"args": [[30, 35, 15, 5, 10, 20, 25]], "expected": 15125},
            {"args": [[5, 10, 3]], "expected": 150},
            {"args": [[2, 3]], "expected": 0},
            {"args": [[40, 20, 30, 10, 30]], "expected": 26000},
        ],
        reference_py=(
            "def solution(p):\n"
            "    m = len(p) - 1\n"
            "    if m <= 1:\n"
            "        return 0\n"
            "    INF = float('inf')\n"
            "    dp = [[0] * (m + 1) for _ in range(m + 1)]\n"
            "    for length in range(2, m + 1):\n"
            "        for i in range(1, m - length + 2):\n"
            "            j = i + length - 1\n"
            "            dp[i][j] = INF\n"
            "            for k in range(i, j):\n"
            "                cost = dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j]\n"
            "                if cost < dp[i][j]:\n"
            "                    dp[i][j] = cost\n"
            "    return dp[1][m]\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int[] p) {\n"
            "        int m = p.length - 1;\n"
            "        if (m <= 1) return 0;\n"
            "        int[][] dp = new int[m + 1][m + 1];\n"
            "        for (int len = 2; len <= m; len++)\n"
            "            for (int i = 1; i + len - 1 <= m; i++) {\n"
            "                int j = i + len - 1; dp[i][j] = Integer.MAX_VALUE;\n"
            "                for (int k = i; k < j; k++)\n"
            "                    dp[i][j] = Math.min(dp[i][j], dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j]);\n"
            "            }\n"
            "        return dp[1][m];\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 행렬 곱셈 순서 : 최소 스칼라 곱셈 횟수\n"
            "def solution(p):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    # ------------------------------------------------------------------
    Problem(
        id="platinum-08",
        rank="Platinum",
        title="트리의 최대 가중 독립 집합",
        style="대기업",
        topic="트리DP",
        type="func",
        func_name="solution",
        description=(
            "N개의 정점(1번부터 N번)으로 이루어진 트리가 있다. 각 정점에는 가중치가 있다. "
            "서로 인접한(간선으로 직접 연결된) 두 정점을 동시에 고를 수 없을 때, 고른 정점들의 가중치 합이 "
            "최대가 되도록 하는 값을 구하세요. (최대 독립 집합의 가중치 합)"
        ),
        input_desc=(
            "n : 정점 수, edges : [u, v] 간선 리스트 (트리, 1-based), "
            "weights : 길이 n 리스트 (weights[i] 는 i+1번 정점의 가중치)"
        ),
        output_desc="인접하지 않게 정점을 골랐을 때 가중치 합의 최댓값",
        examples=[
            {"args": [5, [[1, 2], [1, 3], [2, 4], [2, 5]], [10, 20, 30, 40, 50]], "output": 120},
            {"args": [3, [[1, 2], [2, 3]], [1, 10, 1]], "output": 10},
        ],
        hints=[
            "각 정점에서 '이 정점을 고른 경우'와 '고르지 않은 경우' 두 가지 상태를 자식들로부터 모아 올라가면 됩니다.",
            "트리 DP를 쓰세요. dp[v][1] = v를 고름, dp[v][0] = v를 안 고름. 루트(1번)에서 DFS로 후위 계산합니다.",
            "dp[v][1] = w[v] + sum(dp[child][0]); dp[v][0] = sum(max(dp[child][0], dp[child][1])). 답은 max(dp[root][0], dp[root][1]).",
        ],
        testcases=[
            {"args": [5, [[1, 2], [1, 3], [2, 4], [2, 5]], [10, 20, 30, 40, 50]], "expected": 120},
            {"args": [3, [[1, 2], [2, 3]], [1, 10, 1]], "expected": 10},
            {"args": [1, [], [5]], "expected": 5},
            {"args": [2, [[1, 2]], [1, 2]], "expected": 2},
            {"args": [4, [[1, 2], [1, 3], [1, 4]], [1, 5, 5, 5]], "expected": 15},
        ],
        reference_py=(
            "import sys\n"
            "def solution(n, edges, weights):\n"
            "    sys.setrecursionlimit(100000)\n"
            "    adj = [[] for _ in range(n + 1)]\n"
            "    for u, v in edges:\n"
            "        adj[u].append(v)\n"
            "        adj[v].append(u)\n"
            "    w = [0] + list(weights)\n"
            "    dp0 = [0] * (n + 1)\n"
            "    dp1 = [0] * (n + 1)\n"
            "    visited = [False] * (n + 1)\n"
            "    def dfs(u):\n"
            "        visited[u] = True\n"
            "        dp1[u] = w[u]\n"
            "        dp0[u] = 0\n"
            "        for nx in adj[u]:\n"
            "            if not visited[nx]:\n"
            "                dfs(nx)\n"
            "                dp1[u] += dp0[nx]\n"
            "                dp0[u] += max(dp0[nx], dp1[nx])\n"
            "    dfs(1)\n"
            "    return max(dp0[1], dp1[1])\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    List<Integer>[] adj; int[] w; long[] dp0, dp1; boolean[] vis;\n"
            "    public long solution(int n, int[][] edges, int[] weights) {\n"
            "        adj = new List[n + 1];\n"
            "        for (int i = 1; i <= n; i++) adj[i] = new ArrayList<>();\n"
            "        for (int[] e : edges) { adj[e[0]].add(e[1]); adj[e[1]].add(e[0]); }\n"
            "        w = new int[n + 1];\n"
            "        for (int i = 0; i < n; i++) w[i + 1] = weights[i];\n"
            "        dp0 = new long[n + 1]; dp1 = new long[n + 1]; vis = new boolean[n + 1];\n"
            "        dfs(1);\n"
            "        return Math.max(dp0[1], dp1[1]);\n"
            "    }\n"
            "    void dfs(int u) {\n"
            "        vis[u] = true; dp1[u] = w[u]; dp0[u] = 0;\n"
            "        for (int nx : adj[u]) if (!vis[nx]) {\n"
            "            dfs(nx); dp1[u] += dp0[nx]; dp0[u] += Math.max(dp0[nx], dp1[nx]);\n"
            "        }\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "# 트리 DP : 최대 가중 독립 집합\n"
            "def solution(n, edges, weights):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    # ------------------------------------------------------------------
    Problem(
        id="platinum-09",
        rank="Platinum",
        title="외판원 순회 (비트마스크 TSP)",
        style="해외대기업",
        topic="비트마스크DP",
        type="func",
        func_name="solution",
        description=(
            "N개의 도시가 있고 dist[i][j] 는 도시 i에서 j로 가는 비용이다. 0번 도시에서 출발해 모든 도시를 "
            "정확히 한 번씩 방문하고 다시 0번 도시로 돌아오는 여행 경로의 최소 비용을 구하세요. "
            "(N ≤ 10 의 작은 그래프, 완전 그래프로 가정한다)"
        ),
        input_desc="dist : N x N 비용 행렬 (dist[i][i] = 0, 1 ≤ N ≤ 10)",
        output_desc="모든 도시를 한 번씩 방문하고 출발 도시로 돌아오는 최소 비용",
        examples=[
            {"args": [[[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]], "output": 80},
            {"args": [[[0, 5], [5, 0]]], "output": 10},
        ],
        hints=[
            "방문한 도시 집합과 현재 위치만 알면 남은 결정이 똑같아집니다. '집합'을 정수 비트로 표현해 보세요.",
            "비트마스크 DP를 쓰세요. dp[mask][u] = 0에서 출발해 mask 집합을 방문했고 현재 u에 있을 때의 최소 비용.",
            "dp[mask|(1<<v)][v] = min(..., dp[mask][u] + dist[u][v]). 시작 dp[1][0]=0, 답은 min(dp[full][u]+dist[u][0]).",
        ],
        testcases=[
            {"args": [[[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]], "expected": 80},
            {"args": [[[0, 5], [5, 0]]], "expected": 10},
            {"args": [[[0]]], "expected": 0},
            {"args": [[[0, 10, 15], [10, 0, 20], [15, 20, 0]]], "expected": 45},
            {"args": [[[0, 1, 10, 10], [10, 0, 1, 10], [10, 10, 0, 1], [1, 10, 10, 0]]], "expected": 4},
        ],
        reference_py=(
            "def solution(dist):\n"
            "    n = len(dist)\n"
            "    if n == 1:\n"
            "        return 0\n"
            "    INF = float('inf')\n"
            "    dp = [[INF] * n for _ in range(1 << n)]\n"
            "    dp[1][0] = 0\n"
            "    for mask in range(1 << n):\n"
            "        for u in range(n):\n"
            "            if dp[mask][u] == INF:\n"
            "                continue\n"
            "            if not (mask & (1 << u)):\n"
            "                continue\n"
            "            for v in range(n):\n"
            "                if mask & (1 << v):\n"
            "                    continue\n"
            "                nm = mask | (1 << v)\n"
            "                nd = dp[mask][u] + dist[u][v]\n"
            "                if nd < dp[nm][v]:\n"
            "                    dp[nm][v] = nd\n"
            "    full = (1 << n) - 1\n"
            "    ans = INF\n"
            "    for u in range(n):\n"
            "        if dp[full][u] != INF:\n"
            "            ans = min(ans, dp[full][u] + dist[u][0])\n"
            "    return ans\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int[][] dist) {\n"
            "        int n = dist.length;\n"
            "        if (n == 1) return 0;\n"
            "        int INF = 1 << 29;\n"
            "        int[][] dp = new int[1 << n][n];\n"
            "        for (int[] row : dp) java.util.Arrays.fill(row, INF);\n"
            "        dp[1][0] = 0;\n"
            "        for (int mask = 0; mask < (1 << n); mask++)\n"
            "            for (int u = 0; u < n; u++) {\n"
            "                if (dp[mask][u] == INF || (mask & (1 << u)) == 0) continue;\n"
            "                for (int v = 0; v < n; v++) {\n"
            "                    if ((mask & (1 << v)) != 0) continue;\n"
            "                    int nm = mask | (1 << v);\n"
            "                    dp[nm][v] = Math.min(dp[nm][v], dp[mask][u] + dist[u][v]);\n"
            "                }\n"
            "            }\n"
            "        int full = (1 << n) - 1, ans = INF;\n"
            "        for (int u = 0; u < n; u++)\n"
            "            if (dp[full][u] != INF) ans = Math.min(ans, dp[full][u] + dist[u][0]);\n"
            "        return ans;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 외판원 순회 : 비트마스크 DP\n"
            "def solution(dist):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    # ------------------------------------------------------------------
    Problem(
        id="platinum-10",
        rank="Platinum",
        title="두 그룹 최소 차이 분할",
        style="프로그래머스",
        topic="부분집합DP",
        type="func",
        func_name="solution",
        description=(
            "양의 정수 리스트 nums 가 주어진다. 모든 원소를 두 그룹으로 나눌 때 두 그룹의 합의 차이가 "
            "최소가 되도록 하고, 그 최소 차이를 구하세요. (한 그룹이 비어도 된다)"
        ),
        input_desc="nums : 양의 정수 리스트",
        output_desc="두 그룹으로 나눴을 때 가능한 합의 차이의 최솟값",
        examples=[
            {"args": [[1, 6, 11, 5]], "output": 1},
            {"args": [[3, 1, 4, 2, 2]], "output": 0},
        ],
        hints=[
            "전체 합이 정해져 있으므로, 한 그룹의 합 s 가 정해지면 다른 그룹은 (전체-s)입니다. 차이는 |전체 - 2s|.",
            "부분집합 합 DP를 쓰세요. 어떤 부분집합으로 만들 수 있는 합들을 불리언 배열로 표시합니다.",
            "possible[0]=True, 각 x에 대해 s를 큰 값부터 내려가며 possible[s] |= possible[s-x]. 답은 min(|total-2s|) over possible[s].",
        ],
        testcases=[
            {"args": [[1, 6, 11, 5]], "expected": 1},
            {"args": [[3, 1, 4, 2, 2]], "expected": 0},
            {"args": [[10]], "expected": 10},
            {"args": [[4, 4]], "expected": 0},
            {"args": [[1, 2, 3, 9]], "expected": 3},
        ],
        reference_py=(
            "def solution(nums):\n"
            "    total = sum(nums)\n"
            "    possible = [False] * (total + 1)\n"
            "    possible[0] = True\n"
            "    for x in nums:\n"
            "        for s in range(total, x - 1, -1):\n"
            "            if possible[s - x]:\n"
            "                possible[s] = True\n"
            "    best = total\n"
            "    for s in range(total + 1):\n"
            "        if possible[s]:\n"
            "            d = abs(total - 2 * s)\n"
            "            if d < best:\n"
            "                best = d\n"
            "    return best\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int[] nums) {\n"
            "        int total = 0;\n"
            "        for (int x : nums) total += x;\n"
            "        boolean[] possible = new boolean[total + 1];\n"
            "        possible[0] = true;\n"
            "        for (int x : nums)\n"
            "            for (int s = total; s >= x; s--)\n"
            "                if (possible[s - x]) possible[s] = true;\n"
            "        int best = total;\n"
            "        for (int s = 0; s <= total; s++)\n"
            "            if (possible[s]) best = Math.min(best, Math.abs(total - 2 * s));\n"
            "        return best;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 두 그룹 최소 차이 분할 : 부분집합 합 DP\n"
            "def solution(nums):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    # ------------------------------------------------------------------
    Problem(
        id="platinum-11",
        rank="Platinum",
        title="자릿수 합이 같은 수 세기 (자릿수 DP)",
        style="대기업",
        topic="자릿수DP",
        type="func",
        func_name="solution",
        description=(
            "1 이상 N 이하의 정수 중에서, 각 자리 숫자의 합이 정확히 S 가 되는 수의 개수를 구하세요. "
            "N 이 매우 커질 수 있으므로 각 자리를 차례로 결정하는 자릿수 DP로 풀어야 합니다."
        ),
        input_desc="N : 상한 (N ≥ 0), S : 목표 자릿수 합 (S ≥ 0)",
        output_desc="1 이상 N 이하 정수 중 자릿수 합이 S 인 것의 개수",
        examples=[
            {"args": [20, 2], "output": 3},
            {"args": [100, 1], "output": 3},
        ],
        hints=[
            "1부터 N까지 직접 세면 N이 크면 불가능합니다. 가장 높은 자리부터 한 자리씩 정하며 세어 보세요.",
            "자릿수 DP를 쓰세요. 상태 = (현재 자리 위치, 지금까지 N과 같은 접두사인지(tight), 지금까지 자릿수 합).",
            "각 자리에서 tight면 0..N의 그 자리까지, 아니면 0..9를 고릅니다. 0..N 중 합 S인 개수를 센 뒤 S==0이면 0(숫자)을 제외.",
        ],
        testcases=[
            {"args": [20, 2], "expected": 3},
            {"args": [100, 1], "expected": 3},
            {"args": [9, 5], "expected": 1},
            {"args": [11, 2], "expected": 2},
            {"args": [0, 0], "expected": 0},
        ],
        reference_py=(
            "from functools import lru_cache\n"
            "def solution(N, S):\n"
            "    if N < 1:\n"
            "        return 0\n"
            "    digits = list(map(int, str(N)))\n"
            "    L = len(digits)\n"
            "    @lru_cache(None)\n"
            "    def go(pos, tight, s):\n"
            "        if s > S:\n"
            "            return 0\n"
            "        if pos == L:\n"
            "            return 1 if s == S else 0\n"
            "        limit = digits[pos] if tight else 9\n"
            "        total = 0\n"
            "        for d in range(limit + 1):\n"
            "            total += go(pos + 1, tight and d == limit, s + d)\n"
            "        return total\n"
            "    res = go(0, True, 0)\n"
            "    if S == 0:\n"
            "        res -= 1\n"
            "    return res\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    int[] digits; int L; int S; Integer[][][] memo;\n"
            "    public int solution(int N, int S) {\n"
            "        if (N < 1) return 0;\n"
            "        String s = Integer.toString(N);\n"
            "        L = s.length(); this.S = S;\n"
            "        digits = new int[L];\n"
            "        for (int i = 0; i < L; i++) digits[i] = s.charAt(i) - '0';\n"
            "        memo = new Integer[L + 1][2][S + 2];\n"
            "        int res = go(0, 1, 0);\n"
            "        if (S == 0) res -= 1;\n"
            "        return res;\n"
            "    }\n"
            "    int go(int pos, int tight, int sum) {\n"
            "        if (sum > S) return 0;\n"
            "        if (pos == L) return sum == S ? 1 : 0;\n"
            "        if (memo[pos][tight][sum] != null) return memo[pos][tight][sum];\n"
            "        int limit = tight == 1 ? digits[pos] : 9, total = 0;\n"
            "        for (int d = 0; d <= limit; d++)\n"
            "            total += go(pos + 1, (tight == 1 && d == limit) ? 1 : 0, sum + d);\n"
            "        return memo[pos][tight][sum] = total;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 자릿수 DP : 1..N 중 자릿수 합이 S인 수의 개수\n"
            "def solution(N, S):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    # ------------------------------------------------------------------
    Problem(
        id="platinum-12",
        rank="Platinum",
        title="최장 팰린드롬 부분 수열",
        style="해외대기업",
        topic="구간DP",
        type="func",
        func_name="solution",
        description=(
            "문자열 s 가 주어질 때, s 의 부분 수열(연속이 아니어도 되며 순서는 유지) 중 앞뒤가 똑같은 "
            "팰린드롬이면서 가장 긴 것의 길이를 구하세요."
        ),
        input_desc="s : 문자열 (1 ≤ len ≤ 1000)",
        output_desc="가장 긴 팰린드롬 부분 수열의 길이",
        examples=[
            {"args": ["bbbab"], "output": 4},
            {"args": ["agbdba"], "output": 5},
        ],
        hints=[
            "양 끝 문자가 같으면 그 두 글자를 팰린드롬 바깥에 붙일 수 있습니다. 구간의 양 끝을 보며 안쪽으로 좁혀 보세요.",
            "구간 DP를 쓰세요. dp[i][j] = 부분 문자열 s[i..j] 안의 최장 팰린드롬 부분 수열 길이.",
            "s[i]==s[j]: dp[i][j]=dp[i+1][j-1]+2, 아니면 dp[i][j]=max(dp[i+1][j], dp[i][j-1]). dp[i][i]=1, 답은 dp[0][n-1].",
        ],
        testcases=[
            {"args": ["bbbab"], "expected": 4},
            {"args": ["agbdba"], "expected": 5},
            {"args": ["cbbd"], "expected": 2},
            {"args": ["a"], "expected": 1},
            {"args": ["abcde"], "expected": 1},
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
            "        for i in range(0, n - length + 1):\n"
            "            j = i + length - 1\n"
            "            if s[i] == s[j]:\n"
            "                dp[i][j] = dp[i + 1][j - 1] + 2\n"
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
            "                if (s.charAt(i) == s.charAt(j)) dp[i][j] = dp[i + 1][j - 1] + 2;\n"
            "                else dp[i][j] = Math.max(dp[i + 1][j], dp[i][j - 1]);\n"
            "            }\n"
            "        return dp[0][n - 1];\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 최장 팰린드롬 부분 수열의 길이\n"
            "def solution(s):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    # ------------------------------------------------------------------
    Problem(
        id="platinum-13",
        rank="Platinum",
        title="연속 부분 수열 최대 합",
        style="프로그래머스",
        topic="누적DP",
        type="func",
        func_name="solution",
        description=(
            "정수 리스트 nums 가 주어진다. 적어도 하나 이상의 원소를 포함하는 연속한 부분 수열 중 "
            "원소들의 합이 최대가 되는 값을 구하세요. (음수만 있을 수도 있다)"
        ),
        input_desc="nums : 정수 리스트 (길이 ≥ 1, 음수 포함 가능)",
        output_desc="연속 부분 수열의 합 중 최댓값",
        examples=[
            {"args": [[-2, 1, -3, 4, -1, 2, 1, -5, 4]], "output": 6},
            {"args": [[-5, -2, -3]], "output": -2},
        ],
        hints=[
            "각 위치에서 '이 위치를 끝으로 하는 최대 연속 합'을 알면, 전체 답은 그 값들 중 최댓값입니다.",
            "누적(카데인) DP를 쓰세요. cur = 현재 원소로 끝나는 최대 합, best = 지금까지의 최댓값.",
            "cur = max(x, cur + x), best = max(best, cur) 를 왼쪽부터 갱신. 초기값은 첫 원소로 두어 빈 수열을 배제.",
        ],
        testcases=[
            {"args": [[-2, 1, -3, 4, -1, 2, 1, -5, 4]], "expected": 6},
            {"args": [[-5, -2, -3]], "expected": -2},
            {"args": [[1, 2, 3]], "expected": 6},
            {"args": [[5]], "expected": 5},
            {"args": [[-1, -1, -1]], "expected": -1},
        ],
        reference_py=(
            "def solution(nums):\n"
            "    best = cur = nums[0]\n"
            "    for x in nums[1:]:\n"
            "        cur = max(x, cur + x)\n"
            "        if cur > best:\n"
            "            best = cur\n"
            "    return best\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int[] nums) {\n"
            "        int best = nums[0], cur = nums[0];\n"
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

    # ------------------------------------------------------------------
    Problem(
        id="platinum-14",
        rank="Platinum",
        title="슬라이딩 윈도우 최댓값",
        style="프로그래머스",
        topic="슬라이딩DP",
        type="func",
        func_name="solution",
        description=(
            "정수 리스트 nums 와 윈도우 크기 k 가 주어진다. 왼쪽부터 크기 k의 윈도우를 한 칸씩 옮길 때, "
            "각 윈도우 안의 최댓값을 순서대로 리스트로 반환하세요."
        ),
        input_desc="nums : 정수 리스트, k : 윈도우 크기 (1 ≤ k ≤ len(nums))",
        output_desc="각 윈도우의 최댓값을 순서대로 담은 리스트",
        examples=[
            {"args": [[1, 3, -1, -3, 5, 3, 6, 7], 3], "output": [3, 3, 5, 5, 6, 7]},
            {"args": [[4, 3, 2, 1, 5], 2], "output": [4, 3, 2, 5]},
        ],
        hints=[
            "윈도우가 한 칸 옮겨질 때마다 전부 다시 최댓값을 구하면 느립니다. 후보를 줄 세워 관리해 보세요.",
            "단조 감소 덱(deque)을 쓰세요. 인덱스를 저장하되, 새 값보다 작은 뒤쪽 값들은 다시 최댓값이 될 수 없으므로 제거합니다.",
            "각 i에서 뒤쪽이 nums[i] 이하면 pop, i를 push. 앞이 윈도우를 벗어나면(i-k 이하) popleft. i>=k-1이면 nums[덱앞]을 결과에 추가.",
        ],
        testcases=[
            {"args": [[1, 3, -1, -3, 5, 3, 6, 7], 3], "expected": [3, 3, 5, 5, 6, 7]},
            {"args": [[4, 3, 2, 1, 5], 2], "expected": [4, 3, 2, 5]},
            {"args": [[1], 1], "expected": [1]},
            {"args": [[9, 8, 7, 6], 2], "expected": [9, 8, 7]},
            {"args": [[1, 2, 3, 4], 4], "expected": [4]},
        ],
        reference_py=(
            "from collections import deque\n"
            "def solution(nums, k):\n"
            "    dq = deque()\n"
            "    res = []\n"
            "    for i, x in enumerate(nums):\n"
            "        while dq and nums[dq[-1]] <= x:\n"
            "            dq.pop()\n"
            "        dq.append(i)\n"
            "        if dq[0] <= i - k:\n"
            "            dq.popleft()\n"
            "        if i >= k - 1:\n"
            "            res.append(nums[dq[0]])\n"
            "    return res\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int[] solution(int[] nums, int k) {\n"
            "        Deque<Integer> dq = new ArrayDeque<>();\n"
            "        int n = nums.length;\n"
            "        int[] res = new int[n - k + 1]; int idx = 0;\n"
            "        for (int i = 0; i < n; i++) {\n"
            "            while (!dq.isEmpty() && nums[dq.peekLast()] <= nums[i]) dq.pollLast();\n"
            "            dq.addLast(i);\n"
            "            if (dq.peekFirst() <= i - k) dq.pollFirst();\n"
            "            if (i >= k - 1) res[idx++] = nums[dq.peekFirst()];\n"
            "        }\n"
            "        return res;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "from collections import deque\n"
            "# 슬라이딩 윈도우 최댓값 : 각 윈도우의 최댓값 리스트\n"
            "def solution(nums, k):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

    # ------------------------------------------------------------------
    Problem(
        id="platinum-15",
        rank="Platinum",
        title="팰린드롬 분할 최소 횟수",
        style="해외대기업",
        topic="구간DP",
        type="func",
        func_name="solution",
        description=(
            "문자열 s 를 몇 개의 조각으로 나누어 모든 조각이 팰린드롬이 되게 하려고 한다. "
            "필요한 자르기 횟수(컷)의 최솟값을 구하세요. 이미 전체가 팰린드롬이면 0이다."
        ),
        input_desc="s : 문자열 (1 ≤ len ≤ 1000)",
        output_desc="모든 조각이 팰린드롬이 되도록 나누는 데 필요한 최소 컷 수",
        examples=[
            {"args": ["aab"], "output": 1},
            {"args": ["abccba"], "output": 0},
        ],
        hints=[
            "앞에서부터 s[:i]를 팰린드롬 조각들로 나누는 최소 컷을 차례로 구하면 됩니다.",
            "구간 DP로 팰린드롬 여부 표 pal[i][j] 를 먼저 만들고, 1차원 DP cut[i] 를 채웁니다.",
            "cut[i] = min over j ( cut[j-1] + 1 ), 단 s[j..i]가 팰린드롬. s[0..i] 자체가 팰린드롬이면 cut[i]=0. 답은 cut[n-1].",
        ],
        testcases=[
            {"args": ["aab"], "expected": 1},
            {"args": ["abccba"], "expected": 0},
            {"args": ["a"], "expected": 0},
            {"args": ["ab"], "expected": 1},
            {"args": ["aabb"], "expected": 1},
        ],
        reference_py=(
            "def solution(s):\n"
            "    n = len(s)\n"
            "    if n <= 1:\n"
            "        return 0\n"
            "    pal = [[False] * n for _ in range(n)]\n"
            "    for i in range(n):\n"
            "        pal[i][i] = True\n"
            "    for length in range(2, n + 1):\n"
            "        for i in range(0, n - length + 1):\n"
            "            j = i + length - 1\n"
            "            if s[i] == s[j]:\n"
            "                if length == 2:\n"
            "                    pal[i][j] = True\n"
            "                else:\n"
            "                    pal[i][j] = pal[i + 1][j - 1]\n"
            "    INF = float('inf')\n"
            "    cut = [0] * n\n"
            "    for i in range(n):\n"
            "        if pal[0][i]:\n"
            "            cut[i] = 0\n"
            "        else:\n"
            "            best = INF\n"
            "            for j in range(1, i + 1):\n"
            "                if pal[j][i] and cut[j - 1] + 1 < best:\n"
            "                    best = cut[j - 1] + 1\n"
            "            cut[i] = best\n"
            "    return cut[n - 1]\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(String s) {\n"
            "        int n = s.length();\n"
            "        if (n <= 1) return 0;\n"
            "        boolean[][] pal = new boolean[n][n];\n"
            "        for (int i = 0; i < n; i++) pal[i][i] = true;\n"
            "        for (int len = 2; len <= n; len++)\n"
            "            for (int i = 0; i + len - 1 < n; i++) {\n"
            "                int j = i + len - 1;\n"
            "                if (s.charAt(i) == s.charAt(j))\n"
            "                    pal[i][j] = (len == 2) || pal[i + 1][j - 1];\n"
            "            }\n"
            "        int INF = 1 << 29;\n"
            "        int[] cut = new int[n];\n"
            "        for (int i = 0; i < n; i++) {\n"
            "            if (pal[0][i]) { cut[i] = 0; continue; }\n"
            "            int best = INF;\n"
            "            for (int j = 1; j <= i; j++)\n"
            "                if (pal[j][i]) best = Math.min(best, cut[j - 1] + 1);\n"
            "            cut[i] = best;\n"
            "        }\n"
            "        return cut[n - 1];\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 팰린드롬 분할 최소 컷 수\n"
            "def solution(s):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    # ------------------------------------------------------------------
    Problem(
        id="platinum-16",
        rank="Platinum",
        title="가장 긴 증가하는 부분 수열 (LIS)",
        style="백준",
        topic="DP",
        type="stdin",
        description=(
            "수열이 주어졌을 때, 엄격히 증가하는 부분 수열(연속이 아니어도 되며 순서는 유지) 중 "
            "가장 긴 것의 길이를 구하시오."
        ),
        input_desc="첫째 줄에 수열의 길이 N (1 ≤ N ≤ 100000). 둘째 줄에 N개의 정수가 공백으로 주어진다.",
        output_desc="가장 긴 증가하는 부분 수열의 길이를 한 줄에 출력한다.",
        examples=[
            {"input": "6\n10 20 10 30 20 50\n", "output": "4\n"},
            {"input": "3\n3 2 1\n", "output": "1\n"},
        ],
        hints=[
            "각 길이의 증가 수열을 만들 때 '마지막 원소가 가장 작은' 것을 유지하면 더 길게 이어 붙이기 유리합니다.",
            "이분 탐색(bisect)을 이용한 O(N log N) LIS를 쓰세요. tails 배열에 각 길이의 가능한 최소 끝값을 둡니다.",
            "각 x에 대해 tails에서 x가 들어갈 위치를 bisect_left로 찾아, 끝이면 append 아니면 그 자리를 x로 교체. 답은 len(tails).",
        ],
        testcases=[
            {"input": "6\n10 20 10 30 20 50\n", "output": "4\n"},
            {"input": "3\n3 2 1\n", "output": "1\n"},
            {"input": "3\n1 2 3\n", "output": "3\n"},
            {"input": "1\n5\n", "output": "1\n"},
            {"input": "3\n2 2 2\n", "output": "1\n"},
        ],
        reference_py=(
            "import sys, bisect\n"
            "input = sys.stdin.readline\n"
            "n = int(input())\n"
            "a = list(map(int, input().split()))\n"
            "tails = []\n"
            "for x in a:\n"
            "    pos = bisect.bisect_left(tails, x)\n"
            "    if pos == len(tails):\n"
            "        tails.append(x)\n"
            "    else:\n"
            "        tails[pos] = x\n"
            "print(len(tails))\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        int n = Integer.parseInt(br.readLine().trim());\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int[] tails = new int[n]; int size = 0;\n"
            "        for (int i = 0; i < n; i++) {\n"
            "            int x = Integer.parseInt(st.nextToken());\n"
            "            int lo = 0, hi = size;\n"
            "            while (lo < hi) { int m = (lo + hi) / 2; if (tails[m] < x) lo = m + 1; else hi = m; }\n"
            "            tails[lo] = x;\n"
            "            if (lo == size) size++;\n"
            "        }\n"
            "        System.out.println(size);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys, bisect\n"
            "input = sys.stdin.readline\n"
            "# LIS : 가장 긴 증가하는 부분 수열의 길이\n"
            "n = int(input())\n"
            "a = list(map(int, input().split()))\n"
            "# ...\n"
        ),
    ),

    # ------------------------------------------------------------------
    Problem(
        id="platinum-17",
        rank="Platinum",
        title="편집 거리",
        style="해외대기업",
        topic="DP",
        type="func",
        func_name="solution",
        description=(
            "문자열 a 를 문자열 b 로 바꾸려고 한다. 한 번의 연산으로 문자 하나를 삽입/삭제/교체할 수 있다. "
            "a 를 b 로 만드는 데 필요한 최소 연산 횟수(편집 거리)를 구하세요."
        ),
        input_desc="a, b : 문자열 (0 ≤ len ≤ 1000)",
        output_desc="a 를 b 로 만드는 최소 편집 연산 횟수",
        examples=[
            {"args": ["horse", "ros"], "output": 3},
            {"args": ["intention", "execution"], "output": 5},
        ],
        hints=[
            "두 문자열의 접두사끼리 맞춰 나가는 표를 채우는 전형적인 2차원 DP입니다.",
            "dp[i][j] = a의 앞 i글자를 b의 앞 j글자로 바꾸는 최소 비용. 빈 문자열로의 변환을 경계로 둡니다.",
            "a[i-1]==b[j-1]면 dp[i][j]=dp[i-1][j-1], 아니면 1 + min(삭제 dp[i-1][j], 삽입 dp[i][j-1], 교체 dp[i-1][j-1]).",
        ],
        testcases=[
            {"args": ["horse", "ros"], "expected": 3},
            {"args": ["intention", "execution"], "expected": 5},
            {"args": ["", "abc"], "expected": 3},
            {"args": ["abc", "abc"], "expected": 0},
            {"args": ["abc", "abd"], "expected": 1},
        ],
        reference_py=(
            "def solution(a, b):\n"
            "    n, m = len(a), len(b)\n"
            "    dp = [[0] * (m + 1) for _ in range(n + 1)]\n"
            "    for i in range(n + 1):\n"
            "        dp[i][0] = i\n"
            "    for j in range(m + 1):\n"
            "        dp[0][j] = j\n"
            "    for i in range(1, n + 1):\n"
            "        for j in range(1, m + 1):\n"
            "            if a[i - 1] == b[j - 1]:\n"
            "                dp[i][j] = dp[i - 1][j - 1]\n"
            "            else:\n"
            "                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])\n"
            "    return dp[n][m]\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(String a, String b) {\n"
            "        int n = a.length(), m = b.length();\n"
            "        int[][] dp = new int[n + 1][m + 1];\n"
            "        for (int i = 0; i <= n; i++) dp[i][0] = i;\n"
            "        for (int j = 0; j <= m; j++) dp[0][j] = j;\n"
            "        for (int i = 1; i <= n; i++)\n"
            "            for (int j = 1; j <= m; j++)\n"
            "                if (a.charAt(i - 1) == b.charAt(j - 1)) dp[i][j] = dp[i - 1][j - 1];\n"
            "                else dp[i][j] = 1 + Math.min(dp[i - 1][j], Math.min(dp[i][j - 1], dp[i - 1][j - 1]));\n"
            "        return dp[n][m];\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 편집 거리 : a를 b로 만드는 최소 연산 횟수\n"
            "def solution(a, b):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    # ------------------------------------------------------------------
    Problem(
        id="platinum-18",
        rank="Platinum",
        title="정수 삼각형 최대 경로",
        style="백준",
        topic="DP",
        type="stdin",
        description=(
            "삼각형 모양으로 수가 쌓여 있다. 맨 위에서 시작해 아래로 내려가며 수를 더한다. "
            "한 칸 아래로 내려갈 때는 바로 아래의 왼쪽 또는 오른쪽 대각선 칸으로만 이동할 수 있다. "
            "맨 아래까지 내려오면서 더한 합의 최댓값을 구하시오."
        ),
        input_desc=(
            "첫째 줄에 삼각형의 높이 N (1 ≤ N ≤ 500). 다음 N개의 줄에 i번째 줄에는 i개의 정수가 주어진다."
        ),
        output_desc="맨 위에서 맨 아래까지 내려오며 더한 합의 최댓값을 한 줄에 출력한다.",
        examples=[
            {"input": "5\n7\n3 8\n8 1 0\n2 7 4 4\n4 5 2 6 5\n", "output": "30\n"},
            {"input": "3\n1\n2 3\n4 5 6\n", "output": "10\n"},
        ],
        hints=[
            "위에서 내려오며 각 칸까지의 '최대 누적합'을 기록하면 됩니다. 한 칸은 바로 위 두 칸 중 하나에서만 옵니다.",
            "경로 DP를 쓰세요. tri[i][j] 에 '그 칸까지 도달하는 최대 합'을 더해 갱신합니다.",
            "tri[i][j] += max(tri[i-1][j-1], tri[i-1][j]) (양 끝은 한쪽만). 답은 마지막 줄의 최댓값.",
        ],
        testcases=[
            {"input": "5\n7\n3 8\n8 1 0\n2 7 4 4\n4 5 2 6 5\n", "output": "30\n"},
            {"input": "3\n1\n2 3\n4 5 6\n", "output": "10\n"},
            {"input": "1\n5\n", "output": "5\n"},
            {"input": "2\n1\n2 3\n", "output": "4\n"},
            {"input": "3\n7\n3 8\n8 1 0\n", "output": "18\n"},
        ],
        reference_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "n = int(input())\n"
            "tri = [list(map(int, input().split())) for _ in range(n)]\n"
            "for i in range(1, n):\n"
            "    for j in range(i + 1):\n"
            "        if j == 0:\n"
            "            tri[i][j] += tri[i - 1][0]\n"
            "        elif j == i:\n"
            "            tri[i][j] += tri[i - 1][i - 1]\n"
            "        else:\n"
            "            tri[i][j] += max(tri[i - 1][j - 1], tri[i - 1][j])\n"
            "print(max(tri[n - 1]))\n"
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
            "            tri[i] = new int[i + 1];\n"
            "            StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "            for (int j = 0; j <= i; j++) tri[i][j] = Integer.parseInt(st.nextToken());\n"
            "        }\n"
            "        for (int i = 1; i < n; i++)\n"
            "            for (int j = 0; j <= i; j++) {\n"
            "                if (j == 0) tri[i][j] += tri[i - 1][0];\n"
            "                else if (j == i) tri[i][j] += tri[i - 1][i - 1];\n"
            "                else tri[i][j] += Math.max(tri[i - 1][j - 1], tri[i - 1][j]);\n"
            "            }\n"
            "        int ans = 0;\n"
            "        for (int v : tri[n - 1]) ans = Math.max(ans, v);\n"
            "        System.out.println(ans);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "# 정수 삼각형 : 최대 경로 합\n"
            "n = int(input())\n"
            "# ...\n"
        ),
    ),

    # ------------------------------------------------------------------
    Problem(
        id="platinum-19",
        rank="Platinum",
        title="원형 배열 도둑질",
        style="해외대기업",
        topic="DP",
        type="func",
        func_name="solution",
        description=(
            "집들이 원형으로 배치되어 있고 각 집에는 money[i] 만큼의 돈이 있다. 인접한 두 집을 연속으로 "
            "털면 경보가 울린다. 첫 집과 마지막 집도 서로 인접하다. 경보 없이 털 수 있는 최대 금액을 구하세요."
        ),
        input_desc="money : 각 집의 금액 리스트 (길이 ≥ 1, 0 이상의 정수)",
        output_desc="인접하지 않게 털었을 때 얻을 수 있는 최대 금액",
        examples=[
            {"args": [[2, 3, 2]], "output": 3},
            {"args": [[1, 2, 3, 1]], "output": 4},
        ],
        hints=[
            "원형이라 첫 집과 마지막 집을 동시에 털 수 없다는 점만 빼면 일자형 도둑질과 같습니다.",
            "1차원 DP를 두 번 적용하세요. '첫 집을 제외한 구간'과 '마지막 집을 제외한 구간' 각각의 최댓값을 비교합니다.",
            "rob(arr): prev,cur=0,0; 각 x마다 prev,cur=cur,max(cur,prev+x). 답은 max(rob(money[:-1]), rob(money[1:])), 단 길이 1이면 money[0].",
        ],
        testcases=[
            {"args": [[2, 3, 2]], "expected": 3},
            {"args": [[1, 2, 3, 1]], "expected": 4},
            {"args": [[5]], "expected": 5},
            {"args": [[1, 2]], "expected": 2},
            {"args": [[200, 3, 140, 20, 10]], "expected": 340},
        ],
        reference_py=(
            "def solution(money):\n"
            "    n = len(money)\n"
            "    if n == 1:\n"
            "        return money[0]\n"
            "    def rob_linear(arr):\n"
            "        prev = cur = 0\n"
            "        for x in arr:\n"
            "            prev, cur = cur, max(cur, prev + x)\n"
            "        return cur\n"
            "    return max(rob_linear(money[:-1]), rob_linear(money[1:]))\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int[] money) {\n"
            "        int n = money.length;\n"
            "        if (n == 1) return money[0];\n"
            "        return Math.max(robLinear(money, 0, n - 1), robLinear(money, 1, n));\n"
            "    }\n"
            "    int robLinear(int[] a, int lo, int hi) {\n"
            "        int prev = 0, cur = 0;\n"
            "        for (int i = lo; i < hi; i++) {\n"
            "            int t = Math.max(cur, prev + a[i]);\n"
            "            prev = cur; cur = t;\n"
            "        }\n"
            "        return cur;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 원형 배열 도둑질 : 인접 불가, 첫/마지막도 인접\n"
            "def solution(money):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    # ------------------------------------------------------------------
    Problem(
        id="platinum-20",
        rank="Platinum",
        title="0/1 배낭 채우기",
        style="백준",
        topic="DP",
        type="stdin",
        description=(
            "N개의 물건이 있고 각 물건은 무게 W와 가치 V를 가진다. 각 물건은 0개 또는 1개만 담을 수 있다. "
            "배낭이 견딜 수 있는 무게가 K일 때, 무게 합이 K를 넘지 않으면서 담은 가치 합의 최댓값을 구하시오."
        ),
        input_desc=(
            "첫째 줄에 물건 수 N과 버틸 수 있는 무게 K (1 ≤ N ≤ 100, 0 ≤ K ≤ 100000). "
            "다음 N개의 줄에 각 물건의 무게 W와 가치 V가 주어진다."
        ),
        output_desc="담을 수 있는 물건들의 가치 합의 최댓값을 한 줄에 출력한다.",
        examples=[
            {"input": "4 7\n6 13\n4 8\n3 6\n5 12\n", "output": "14\n"},
            {"input": "3 5\n1 6\n2 10\n3 12\n", "output": "22\n"},
        ],
        hints=[
            "각 물건을 '담는다/안 담는다' 두 선택만 있습니다. 남은 무게 한도별 최대 가치를 갱신해 나가세요.",
            "0/1 배낭 DP를 쓰세요. dp[c] = 무게 한도 c에서의 최대 가치. 각 물건마다 한 번씩만 쓰도록 갱신 방향에 주의합니다.",
            "각 물건 (w, v)에 대해 c를 K부터 w까지 내려가며 dp[c] = max(dp[c], dp[c-w]+v). 답은 dp[K].",
        ],
        testcases=[
            {"input": "4 7\n6 13\n4 8\n3 6\n5 12\n", "output": "14\n"},
            {"input": "3 5\n1 6\n2 10\n3 12\n", "output": "22\n"},
            {"input": "1 0\n5 10\n", "output": "0\n"},
            {"input": "1 4\n5 10\n", "output": "0\n"},
            {"input": "3 4\n2 3\n2 3\n2 3\n", "output": "6\n"},
        ],
        reference_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "n, k = map(int, input().split())\n"
            "dp = [0] * (k + 1)\n"
            "for _ in range(n):\n"
            "    w, v = map(int, input().split())\n"
            "    for c in range(k, w - 1, -1):\n"
            "        if dp[c - w] + v > dp[c]:\n"
            "            dp[c] = dp[c - w] + v\n"
            "print(dp[k])\n"
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
            "        int[] dp = new int[k + 1];\n"
            "        for (int i = 0; i < n; i++) {\n"
            "            st = new StringTokenizer(br.readLine());\n"
            "            int w = Integer.parseInt(st.nextToken());\n"
            "            int v = Integer.parseInt(st.nextToken());\n"
            "            for (int c = k; c >= w; c--) dp[c] = Math.max(dp[c], dp[c - w] + v);\n"
            "        }\n"
            "        System.out.println(dp[k]);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "# 0/1 배낭 : 무게 한도 K에서 최대 가치\n"
            "n, k = map(int, input().split())\n"
            "# ...\n"
        ),
    ),

]
