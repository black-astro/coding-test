"""플래티넘 랭크 — 고급 DP / 최단경로 / 위상정렬 / 세그먼트 트리 / 조합 DP.

목표 50문제. 현재 시드 5문제.
"""

from engine.models import Problem

PROBLEMS = [

    Problem(
        id="platinum-01",
        rank="Platinum",
        title="가장 긴 공통 부분 수열 (LCS)",
        style="백준",
        topic="DP",
        type="func",
        func_name="solution",
        description=(
            "두 문자열 a, b 가 주어졌을 때, 두 문자열에 공통으로 들어 있는 부분 수열 중 "
            "가장 긴 것의 길이를 구하세요. (연속이 아니어도 되며 순서는 유지)"
        ),
        input_desc="a, b : 문자열 (1 ≤ len ≤ 1000)",
        output_desc="가장 긴 공통 부분 수열의 길이",
        examples=[
            {"args": ["ACAYKP", "CAPCAK"], "output": 4},   # ACAK
        ],
        hints=[
            "두 문자열을 앞에서부터 비교하며 표(2차원 DP)를 채우는 전형적인 문제입니다.",
            "dp[i][j] = a[:i] 와 b[:j] 의 LCS 길이. a[i-1]==b[j-1] 이면 대각선+1, 아니면 위/왼쪽 중 큰 값.",
            "a[i-1]==b[j-1]: dp[i][j]=dp[i-1][j-1]+1 / else: dp[i][j]=max(dp[i-1][j], dp[i][j-1]). 답은 dp[len(a)][len(b)].",
        ],
        testcases=[
            {"args": ["ACAYKP", "CAPCAK"], "expected": 4},
            {"args": ["ABCBDAB", "BDCAB"], "expected": 4},
            {"args": ["abc", "abc"], "expected": 3},
            {"args": ["abc", "xyz"], "expected": 0},
        ],
        reference_py=(
            "def solution(a, b):\n"
            "    n, m = len(a), len(b)\n"
            "    dp = [[0] * (m + 1) for _ in range(n + 1)]\n"
            "    for i in range(1, n + 1):\n"
            "        for j in range(1, m + 1):\n"
            "            if a[i - 1] == b[j - 1]:\n"
            "                dp[i][j] = dp[i - 1][j - 1] + 1\n"
            "            else:\n"
            "                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])\n"
            "    return dp[n][m]\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(String a, String b) {\n"
            "        int n = a.length(), m = b.length();\n"
            "        int[][] dp = new int[n + 1][m + 1];\n"
            "        for (int i = 1; i <= n; i++)\n"
            "            for (int j = 1; j <= m; j++)\n"
            "                if (a.charAt(i-1) == b.charAt(j-1)) dp[i][j] = dp[i-1][j-1] + 1;\n"
            "                else dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);\n"
            "        return dp[n][m];\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# LCS : 가장 긴 공통 부분 수열의 길이\n"
            "def solution(a, b):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="platinum-02",
        rank="Platinum",
        title="최단 경로 (다익스트라)",
        style="백준",
        topic="다익스트라",
        type="stdin",
        description=(
            "방향 가중치 그래프에서 시작 정점으로부터 모든 정점까지의 최단 거리를 구하시오. "
            "도달할 수 없는 정점은 INF 로 출력한다. 모든 간선 가중치는 양수이다."
        ),
        input_desc=(
            "첫째 줄에 V E start (정점 수, 간선 수, 시작 정점, 정점 번호는 1..V). "
            "다음 E개의 줄에 u v w (u에서 v로 가는 가중치 w 간선)."
        ),
        output_desc="1번 정점부터 V번 정점까지, 시작점으로부터의 최단 거리를 한 줄에 하나씩 출력. 도달 불가는 INF.",
        examples=[
            {
                "input": "5 6 1\n1 2 2\n1 3 3\n2 3 1\n2 4 5\n3 4 1\n4 5 2\n",
                "output": "0\n2\n3\n4\n6\n",
            },
        ],
        hints=[
            "가중치가 있는 그래프의 한 점 → 모든 점 최단거리입니다. 가까운 정점부터 확정해 나가는 방식을 떠올리세요.",
            "우선순위 큐(heapq)를 이용한 다익스트라를 쓰세요. dist[start]=0 에서 시작해 더 짧은 거리를 발견할 때만 갱신.",
            "heap=[(0,start)]; pop한 거리가 dist보다 크면 skip; 인접 (v,w)에 대해 nd=d+w<dist[v]면 갱신·push. 마지막에 INF는 'INF' 출력.",
        ],
        testcases=[
            {
                "input": "5 6 1\n1 2 2\n1 3 3\n2 3 1\n2 4 5\n3 4 1\n4 5 2\n",
                "output": "0\n2\n3\n4\n6\n",
            },
            {
                "input": "3 1 1\n1 2 4\n",
                "output": "0\n4\nINF\n",
            },
        ],
        reference_py=(
            "import sys, heapq\n"
            "input = sys.stdin.readline\n"
            "INF = float('inf')\n"
            "v, e, start = map(int, input().split())\n"
            "graph = [[] for _ in range(v + 1)]\n"
            "for _ in range(e):\n"
            "    a, b, w = map(int, input().split())\n"
            "    graph[a].append((b, w))\n"
            "dist = [INF] * (v + 1)\n"
            "dist[start] = 0\n"
            "pq = [(0, start)]\n"
            "while pq:\n"
            "    d, u = heapq.heappop(pq)\n"
            "    if d > dist[u]:\n"
            "        continue\n"
            "    for nxt, w in graph[u]:\n"
            "        nd = d + w\n"
            "        if nd < dist[nxt]:\n"
            "            dist[nxt] = nd\n"
            "            heapq.heappush(pq, (nd, nxt))\n"
            "out = []\n"
            "for i in range(1, v + 1):\n"
            "    out.append('INF' if dist[i] == INF else str(dist[i]))\n"
            "print('\\n'.join(out))\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int v = Integer.parseInt(st.nextToken());\n"
            "        int e = Integer.parseInt(st.nextToken());\n"
            "        int start = Integer.parseInt(st.nextToken());\n"
            "        List<int[]>[] g = new List[v + 1];\n"
            "        for (int i = 1; i <= v; i++) g[i] = new ArrayList<>();\n"
            "        for (int i = 0; i < e; i++) {\n"
            "            st = new StringTokenizer(br.readLine());\n"
            "            int a = Integer.parseInt(st.nextToken());\n"
            "            int b = Integer.parseInt(st.nextToken());\n"
            "            int w = Integer.parseInt(st.nextToken());\n"
            "            g[a].add(new int[]{b, w});\n"
            "        }\n"
            "        long[] dist = new long[v + 1];\n"
            "        Arrays.fill(dist, Long.MAX_VALUE);\n"
            "        dist[start] = 0;\n"
            "        PriorityQueue<long[]> pq = new PriorityQueue<>((x, y) -> Long.compare(x[0], y[0]));\n"
            "        pq.add(new long[]{0, start});\n"
            "        while (!pq.isEmpty()) {\n"
            "            long[] c = pq.poll();\n"
            "            long d = c[0]; int u = (int) c[1];\n"
            "            if (d > dist[u]) continue;\n"
            "            for (int[] nx : g[u]) {\n"
            "                long nd = d + nx[1];\n"
            "                if (nd < dist[nx[0]]) { dist[nx[0]] = nd; pq.add(new long[]{nd, nx[0]}); }\n"
            "            }\n"
            "        }\n"
            "        StringBuilder sb = new StringBuilder();\n"
            "        for (int i = 1; i <= v; i++)\n"
            "            sb.append(dist[i] == Long.MAX_VALUE ? \"INF\" : dist[i]).append('\\n');\n"
            "        System.out.print(sb);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys, heapq\n"
            "input = sys.stdin.readline\n"
            "# 다익스트라 최단경로\n"
            "v, e, start = map(int, input().split())\n"
            "# ...\n"
        ),
    ),

    Problem(
        id="platinum-03",
        rank="Platinum",
        title="줄 세우기 (위상 정렬)",
        style="백준",
        topic="위상정렬",
        type="stdin",
        description=(
            "N명의 학생을 키 순서로 줄 세운다. 일부 학생 쌍에 대해서만 '누가 더 앞(작은 키)' 인지 "
            "비교 결과가 주어진다. 가능한 줄 세우기 중 하나를 출력하시오. "
            "답이 여러 개면 앞에 오는 번호가 작은 것을 우선한다."
        ),
        input_desc=(
            "첫째 줄 N M (학생 수, 비교 횟수). 다음 M개의 줄에 a b (a가 b보다 앞에 서야 함). "
            "정점 번호는 1..N."
        ),
        output_desc="조건을 만족하는 줄 세우기 결과를 한 줄에 공백으로 구분해 출력.",
        examples=[
            {"input": "3 2\n1 3\n2 3\n", "output": "1 2 3\n"},
            {"input": "4 2\n4 2\n3 1\n", "output": "3 1 4 2\n"},
        ],
        hints=[
            "'A는 B보다 앞' 이라는 선후 관계 → 방향 그래프에서 순서를 정하는 문제입니다.",
            "위상 정렬을 쓰세요. 진입차수(indegree)가 0인 정점부터 차례로 빼내며 줄을 만듭니다.",
            "indegree 0인 정점들을 '최소 힙'에 넣고, 작은 번호부터 pop·출력하며 인접 정점의 indegree를 줄여 0이 되면 push.",
        ],
        testcases=[
            {"input": "3 2\n1 3\n2 3\n", "output": "1 2 3\n"},
            {"input": "4 2\n4 2\n3 1\n", "output": "3 1 4 2\n"},
            {"input": "3 0\n", "output": "1 2 3\n"},
        ],
        reference_py=(
            "import sys, heapq\n"
            "input = sys.stdin.readline\n"
            "n, m = map(int, input().split())\n"
            "graph = [[] for _ in range(n + 1)]\n"
            "indeg = [0] * (n + 1)\n"
            "for _ in range(m):\n"
            "    a, b = map(int, input().split())\n"
            "    graph[a].append(b)\n"
            "    indeg[b] += 1\n"
            "heap = [i for i in range(1, n + 1) if indeg[i] == 0]\n"
            "heapq.heapify(heap)\n"
            "order = []\n"
            "while heap:\n"
            "    u = heapq.heappop(heap)\n"
            "    order.append(u)\n"
            "    for nxt in graph[u]:\n"
            "        indeg[nxt] -= 1\n"
            "        if indeg[nxt] == 0:\n"
            "            heapq.heappush(heap, nxt)\n"
            "print(' '.join(map(str, order)))\n"
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
            "        List<Integer>[] g = new List[n + 1];\n"
            "        for (int i = 1; i <= n; i++) g[i] = new ArrayList<>();\n"
            "        int[] indeg = new int[n + 1];\n"
            "        for (int i = 0; i < m; i++) {\n"
            "            st = new StringTokenizer(br.readLine());\n"
            "            int a = Integer.parseInt(st.nextToken());\n"
            "            int b = Integer.parseInt(st.nextToken());\n"
            "            g[a].add(b); indeg[b]++;\n"
            "        }\n"
            "        PriorityQueue<Integer> pq = new PriorityQueue<>();\n"
            "        for (int i = 1; i <= n; i++) if (indeg[i] == 0) pq.add(i);\n"
            "        StringBuilder sb = new StringBuilder();\n"
            "        while (!pq.isEmpty()) {\n"
            "            int u = pq.poll();\n"
            "            sb.append(u).append(' ');\n"
            "            for (int nx : g[u]) if (--indeg[nx] == 0) pq.add(nx);\n"
            "        }\n"
            "        System.out.println(sb.toString().trim());\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys, heapq\n"
            "input = sys.stdin.readline\n"
            "# 줄 세우기 (위상 정렬, 작은 번호 우선)\n"
            "n, m = map(int, input().split())\n"
            "# ...\n"
        ),
    ),

    Problem(
        id="platinum-04",
        rank="Platinum",
        title="구간 합과 갱신 (세그먼트 트리)",
        style="백준",
        topic="세그먼트트리",
        type="func",
        func_name="solution",
        description=(
            "초기 배열 arr 와 질의 목록 queries 가 주어진다. 각 질의는 다음 두 종류다.\n"
            "  - ['U', i, x] : arr 의 i번째(1-based) 값을 x 로 바꾼다.\n"
            "  - ['Q', l, r] : l번째부터 r번째까지의 구간 합을 답한다.\n"
            "모든 'Q' 질의의 답을 순서대로 리스트로 반환하세요. "
            "갱신과 질의가 섞여 많이 들어오므로 세그먼트 트리가 적합합니다."
        ),
        input_desc="arr : 정수 리스트, queries : ['U',i,x] / ['Q',l,r] 의 리스트 (1-based 인덱스)",
        output_desc="'Q' 질의들의 답을 순서대로 담은 리스트",
        examples=[
            {
                "args": [[1, 2, 3, 4, 5], [["Q", 1, 3], ["U", 2, 10], ["Q", 1, 3], ["Q", 4, 5]]],
                "output": [6, 14, 9],
            },
        ],
        hints=[
            "값이 계속 바뀌므로 누적합은 매번 다시 만들어야 해 비효율적입니다. 갱신·질의 둘 다 빠른 구조가 필요합니다.",
            "세그먼트 트리를 쓰세요. 리프는 원소, 내부 노드는 자식 구간의 합. 갱신·질의 모두 O(log n).",
            "tree 크기 2*size. update(i,x): 리프 갱신 후 부모로 올라가며 tree[p]=tree[2p]+tree[2p+1]. query(l,r): 표준 반복 세그트리 합.",
        ],
        testcases=[
            {
                "args": [[1, 2, 3, 4, 5], [["Q", 1, 3], ["U", 2, 10], ["Q", 1, 3], ["Q", 4, 5]]],
                "expected": [6, 14, 9],
            },
            {
                "args": [[5, 5, 5], [["Q", 1, 3], ["U", 1, 0], ["Q", 1, 1]]],
                "expected": [15, 0],
            },
            {
                "args": [[10], [["Q", 1, 1], ["U", 1, 7], ["Q", 1, 1]]],
                "expected": [10, 7],
            },
        ],
        reference_py=(
            "def solution(arr, queries):\n"
            "    n = len(arr)\n"
            "    size = 1\n"
            "    while size < n:\n"
            "        size *= 2\n"
            "    tree = [0] * (2 * size)\n"
            "    for i in range(n):\n"
            "        tree[size + i] = arr[i]\n"
            "    for p in range(size - 1, 0, -1):\n"
            "        tree[p] = tree[2 * p] + tree[2 * p + 1]\n"
            "    def update(idx, val):\n"
            "        p = size + idx\n"
            "        tree[p] = val\n"
            "        p //= 2\n"
            "        while p:\n"
            "            tree[p] = tree[2 * p] + tree[2 * p + 1]\n"
            "            p //= 2\n"
            "    def query(l, r):\n"
            "        res = 0\n"
            "        l += size\n"
            "        r += size + 1\n"
            "        while l < r:\n"
            "            if l & 1:\n"
            "                res += tree[l]\n"
            "                l += 1\n"
            "            if r & 1:\n"
            "                r -= 1\n"
            "                res += tree[r]\n"
            "            l //= 2\n"
            "            r //= 2\n"
            "        return res\n"
            "    out = []\n"
            "    for q in queries:\n"
            "        if q[0] == 'U':\n"
            "            update(q[1] - 1, q[2])\n"
            "        else:\n"
            "            out.append(query(q[1] - 1, q[2] - 1))\n"
            "    return out\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    long[] tree; int size;\n"
            "    public int[] solution(int[] arr, Object[][] queries) {\n"
            "        int n = arr.length; size = 1;\n"
            "        while (size < n) size *= 2;\n"
            "        tree = new long[2 * size];\n"
            "        for (int i = 0; i < n; i++) tree[size + i] = arr[i];\n"
            "        for (int p = size - 1; p >= 1; p--) tree[p] = tree[2*p] + tree[2*p+1];\n"
            "        List<Integer> out = new ArrayList<>();\n"
            "        for (Object[] q : queries) {\n"
            "            if (q[0].equals(\"U\")) update((int)q[1] - 1, (int)q[2]);\n"
            "            else out.add((int) query((int)q[1] - 1, (int)q[2] - 1));\n"
            "        }\n"
            "        return out.stream().mapToInt(Integer::intValue).toArray();\n"
            "    }\n"
            "    void update(int idx, long val) {\n"
            "        int p = size + idx; tree[p] = val; p /= 2;\n"
            "        while (p >= 1) { tree[p] = tree[2*p] + tree[2*p+1]; p /= 2; }\n"
            "    }\n"
            "    long query(int l, int r) {\n"
            "        long res = 0; l += size; r += size + 1;\n"
            "        while (l < r) {\n"
            "            if ((l & 1) == 1) res += tree[l++];\n"
            "            if ((r & 1) == 1) res += tree[--r];\n"
            "            l /= 2; r /= 2;\n"
            "        }\n"
            "        return res;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 세그먼트 트리 : 갱신(U)과 구간합 질의(Q) 처리, Q들의 답 리스트 반환\n"
            "def solution(arr, queries):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="platinum-05",
        rank="Platinum",
        title="동전 2 (최소 동전 개수, 무한 개)",
        style="백준",
        topic="DP",
        type="func",
        func_name="solution",
        description=(
            "n가지 종류의 동전이 있고 각 동전은 무한히 사용할 수 있다. 가치의 합이 정확히 "
            "target 이 되도록 할 때 필요한 동전 개수의 최솟값을 구하세요. "
            "만들 수 없으면 -1 을 반환합니다. (그리디로는 풀 수 없는 일반 화폐)"
        ),
        input_desc="coins : 동전 가치 리스트, target : 목표 금액",
        output_desc="target 을 만드는 최소 동전 개수 (불가능하면 -1)",
        examples=[
            {"args": [[1, 5, 12], 15], "output": 3},   # 5+5+5
        ],
        hints=[
            "동전을 큰 것부터 쓰는 그리디는 [1,5,12], 15 에서 틀립니다(12+1+1+1=4개 vs 5+5+5=3개). DP가 필요합니다.",
            "dp[k] = 금액 k를 만드는 최소 동전 수. 각 동전 c에 대해 dp[k] = min(dp[k], dp[k-c]+1) (완전 배낭).",
            "dp=[INF]*(target+1); dp[0]=0; for c in coins: for k in range(c, target+1): dp[k]=min(dp[k], dp[k-c]+1). 답은 dp[target] (INF면 -1).",
        ],
        testcases=[
            {"args": [[1, 5, 12], 15], "expected": 3},
            {"args": [[2], 3], "expected": -1},
            {"args": [[1, 5, 12], 0], "expected": 0},
            {"args": [[3, 7], 13], "expected": 3},
            {"args": [[1, 2, 5], 11], "expected": 3},
        ],
        reference_py=(
            "def solution(coins, target):\n"
            "    INF = float('inf')\n"
            "    dp = [INF] * (target + 1)\n"
            "    dp[0] = 0\n"
            "    for c in coins:\n"
            "        for k in range(c, target + 1):\n"
            "            if dp[k - c] + 1 < dp[k]:\n"
            "                dp[k] = dp[k - c] + 1\n"
            "    return dp[target] if dp[target] != INF else -1\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int solution(int[] coins, int target) {\n"
            "        int INF = 1 << 29;\n"
            "        int[] dp = new int[target + 1];\n"
            "        Arrays.fill(dp, INF);\n"
            "        dp[0] = 0;\n"
            "        for (int c : coins)\n"
            "            for (int k = c; k <= target; k++)\n"
            "                dp[k] = Math.min(dp[k], dp[k - c] + 1);\n"
            "        return dp[target] == INF ? -1 : dp[target];\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 동전 2 : 최소 동전 개수 (무한 사용, 불가능하면 -1)\n"
            "def solution(coins, target):\n"
            "    answer = -1\n"
            "    return answer\n"
        ),
    ),

]
