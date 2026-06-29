"""유형별 실전 — 다익스트라 / 최단경로.

각 문제는 Problem 객체 하나로 표현된다.
"""

from engine.models import Problem

CATEGORY = "다익스트라/최단경로"

PROBLEMS = [

    Problem(
        id="dijkstra-01",
        rank="Gold",
        title="배달 가능 마을 수",
        style="카카오",
        topic="다익스트라",
        type="func",
        func_name="solution",
        description=(
            "음식점이 있는 1번 마을에서 출발해 음식을 배달한다. 마을은 1번부터 N번까지 있고, "
            "두 마을을 잇는 길은 양방향이며 통행 시간이 정해져 있다. 1번 마을에서 출발해 "
            "K 시간 이하로 배달이 가능한 마을의 개수를 구하세요. (출발 마을 1번 자신도 포함한다.)\n"
            "두 마을 사이에는 여러 개의 길이 있을 수 있으며, 그중 더 빠른 길을 택할 수 있다."
        ),
        input_desc=(
            "N : 마을 수 (1 ≤ N ≤ 50), "
            "road : 각 원소가 [a, b, c] 인 리스트 (a번과 b번 마을을 c 시간에 오갈 수 있다), "
            "K : 배달 가능 시간 상한"
        ),
        output_desc="1번 마을에서 K 시간 이하로 도달할 수 있는 마을의 개수 (1번 포함)",
        examples=[
            {
                "args": [5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3],
                "output": 4,
            },
            {
                "args": [6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4],
                "output": 4,
            },
        ],
        hints=[
            "1번 마을에서 다른 모든 마을까지의 '최소 통행 시간'을 먼저 구한 뒤, 그 값이 K 이하인 마을을 세면 됩니다.",
            "양수 가중치 그래프의 한 점 → 모든 점 최단거리이므로 우선순위 큐(heapq) 기반 다익스트라가 적합합니다. 중복 간선은 더 작은 가중치만 의미가 있습니다.",
            "dist[1]=0 으로 시작해 heap=[(0,1)]; pop한 거리가 dist[u]보다 크면 skip; 인접 (v,w)에 대해 d+w<dist[v]면 갱신·push. 마지막에 sum(1 for i if dist[i]<=K).",
        ],
        testcases=[
            {
                "args": [5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3],
                "expected": 4,
            },
            {
                "args": [6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4],
                "expected": 4,
            },
            {"args": [1, [], 0], "expected": 1},
            {"args": [4, [[1, 2, 5], [2, 3, 5]], 3], "expected": 1},
            {"args": [4, [[1, 2, 5], [2, 3, 5]], 100], "expected": 3},
        ],
        reference_py=(
            "import heapq\n"
            "\n"
            "def solution(N, road, K):\n"
            "    INF = float('inf')\n"
            "    graph = [[] for _ in range(N + 1)]\n"
            "    for a, b, c in road:\n"
            "        graph[a].append((b, c))\n"
            "        graph[b].append((a, c))\n"
            "    dist = [INF] * (N + 1)\n"
            "    dist[1] = 0\n"
            "    pq = [(0, 1)]\n"
            "    while pq:\n"
            "        d, u = heapq.heappop(pq)\n"
            "        if d > dist[u]:\n"
            "            continue\n"
            "        for v, w in graph[u]:\n"
            "            nd = d + w\n"
            "            if nd < dist[v]:\n"
            "                dist[v] = nd\n"
            "                heapq.heappush(pq, (nd, v))\n"
            "    return sum(1 for i in range(1, N + 1) if dist[i] <= K)\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int solution(int N, int[][] road, int K) {\n"
            "        long INF = Long.MAX_VALUE;\n"
            "        List<long[]>[] g = new List[N + 1];\n"
            "        for (int i = 1; i <= N; i++) g[i] = new ArrayList<>();\n"
            "        for (int[] r : road) {\n"
            "            g[r[0]].add(new long[]{r[1], r[2]});\n"
            "            g[r[1]].add(new long[]{r[0], r[2]});\n"
            "        }\n"
            "        long[] dist = new long[N + 1];\n"
            "        Arrays.fill(dist, INF);\n"
            "        dist[1] = 0;\n"
            "        PriorityQueue<long[]> pq = new PriorityQueue<>((x, y) -> Long.compare(x[0], y[0]));\n"
            "        pq.add(new long[]{0, 1});\n"
            "        while (!pq.isEmpty()) {\n"
            "            long[] c = pq.poll();\n"
            "            long d = c[0]; int u = (int) c[1];\n"
            "            if (d > dist[u]) continue;\n"
            "            for (long[] nx : g[u]) {\n"
            "                long nd = d + nx[1];\n"
            "                if (nd < dist[(int) nx[0]]) { dist[(int) nx[0]] = nd; pq.add(new long[]{nd, nx[0]}); }\n"
            "            }\n"
            "        }\n"
            "        int cnt = 0;\n"
            "        for (int i = 1; i <= N; i++) if (dist[i] <= K) cnt++;\n"
            "        return cnt;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import heapq\n"
            "# 배달 가능 마을 수 : 1번에서 K 시간 이하로 도달 가능한 마을 개수\n"
            "def solution(N, road, K):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="dijkstra-02",
        rank="Gold",
        title="최소 비용 경로",
        style="삼성",
        topic="최단경로",
        type="stdin",
        description=(
            "N개의 도시가 있고, 한 도시에서 다른 도시로 가는 단방향 도로들이 비용과 함께 주어진다. "
            "출발 도시에서 도착 도시까지 가는 데 드는 최소 비용을 구하시오. "
            "도착할 수 없으면 -1 을 출력한다. 모든 도로의 비용은 양수이다."
        ),
        input_desc=(
            "첫째 줄에 도시 수 N (1 ≤ N ≤ 1000). 둘째 줄에 도로 수 M. "
            "다음 M개의 줄에 a b c (a번 도시에서 b번 도시로 가는 비용 c 도로). "
            "마지막 줄에 출발 도시와 도착 도시 번호. 도시 번호는 1..N."
        ),
        output_desc="출발 도시에서 도착 도시까지의 최소 비용 (도달 불가면 -1).",
        examples=[
            {
                "input": "4\n5\n1 2 4\n1 3 1\n3 2 2\n2 4 5\n3 4 8\n1 4\n",
                "output": "8\n",
            },
            {
                "input": "5\n6\n1 2 2\n1 3 3\n2 3 1\n2 4 5\n3 4 1\n4 5 2\n1 5\n",
                "output": "6\n",
            },
        ],
        hints=[
            "한 출발점에서 한 도착점까지의 최소 비용입니다. 모든 비용이 양수이므로 가까운 도시부터 비용을 확정해 나갈 수 있습니다.",
            "우선순위 큐(heapq) 기반 다익스트라를 쓰세요. dist[start]=0 에서 시작해 더 짧은 비용을 발견할 때만 갱신합니다.",
            "heap=[(0,start)]; pop한 비용이 dist[u]보다 크면 skip; 인접 (v,w)에 대해 d+w<dist[v]면 갱신·push. dist[end]가 INF면 -1, 아니면 그 값 출력.",
        ],
        testcases=[
            {
                "input": "4\n5\n1 2 4\n1 3 1\n3 2 2\n2 4 5\n3 4 8\n1 4\n",
                "output": "8\n",
            },
            {
                "input": "5\n6\n1 2 2\n1 3 3\n2 3 1\n2 4 5\n3 4 1\n4 5 2\n1 5\n",
                "output": "6\n",
            },
            {
                "input": "3\n2\n1 2 5\n2 3 5\n2 2\n",
                "output": "0\n",
            },
            {
                "input": "3\n1\n1 2 3\n1 3\n",
                "output": "-1\n",
            },
        ],
        reference_py=(
            "import sys, heapq\n"
            "input = sys.stdin.readline\n"
            "\n"
            "def main():\n"
            "    n = int(input())\n"
            "    m = int(input())\n"
            "    graph = [[] for _ in range(n + 1)]\n"
            "    for _ in range(m):\n"
            "        a, b, c = map(int, input().split())\n"
            "        graph[a].append((b, c))\n"
            "    s, e = map(int, input().split())\n"
            "    INF = float('inf')\n"
            "    dist = [INF] * (n + 1)\n"
            "    dist[s] = 0\n"
            "    pq = [(0, s)]\n"
            "    while pq:\n"
            "        d, u = heapq.heappop(pq)\n"
            "        if d > dist[u]:\n"
            "            continue\n"
            "        for v, w in graph[u]:\n"
            "            nd = d + w\n"
            "            if nd < dist[v]:\n"
            "                dist[v] = nd\n"
            "                heapq.heappush(pq, (nd, v))\n"
            "    print(dist[e] if dist[e] != INF else -1)\n"
            "\n"
            "main()\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        int n = Integer.parseInt(br.readLine().trim());\n"
            "        int m = Integer.parseInt(br.readLine().trim());\n"
            "        List<long[]>[] g = new List[n + 1];\n"
            "        for (int i = 1; i <= n; i++) g[i] = new ArrayList<>();\n"
            "        for (int i = 0; i < m; i++) {\n"
            "            StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "            int a = Integer.parseInt(st.nextToken());\n"
            "            int b = Integer.parseInt(st.nextToken());\n"
            "            int c = Integer.parseInt(st.nextToken());\n"
            "            g[a].add(new long[]{b, c});\n"
            "        }\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int s = Integer.parseInt(st.nextToken());\n"
            "        int e = Integer.parseInt(st.nextToken());\n"
            "        long[] dist = new long[n + 1];\n"
            "        Arrays.fill(dist, Long.MAX_VALUE);\n"
            "        dist[s] = 0;\n"
            "        PriorityQueue<long[]> pq = new PriorityQueue<>((x, y) -> Long.compare(x[0], y[0]));\n"
            "        pq.add(new long[]{0, s});\n"
            "        while (!pq.isEmpty()) {\n"
            "            long[] c = pq.poll();\n"
            "            long d = c[0]; int u = (int) c[1];\n"
            "            if (d > dist[u]) continue;\n"
            "            for (long[] nx : g[u]) {\n"
            "                long nd = d + nx[1];\n"
            "                if (nd < dist[(int) nx[0]]) { dist[(int) nx[0]] = nd; pq.add(new long[]{nd, nx[0]}); }\n"
            "            }\n"
            "        }\n"
            "        System.out.println(dist[e] == Long.MAX_VALUE ? -1 : dist[e]);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys, heapq\n"
            "input = sys.stdin.readline\n"
            "# 최소 비용 경로 (단방향, 도달 불가면 -1)\n"
            "def main():\n"
            "    n = int(input())\n"
            "    # ...\n"
            "main()\n"
        ),
    ),

    Problem(
        id="dijkstra-03",
        rank="Platinum",
        title="합승 택시 최소 요금",
        style="카카오",
        topic="최단경로",
        type="func",
        func_name="solution",
        description=(
            "두 사람 A, B 가 출발 지점 s 에서 함께 택시를 타고 가다가, 어느 지점 k 에서 헤어져 "
            "각자 목적지 a, b 로 따로 이동한다. 지점 사이의 도로는 양방향이며 요금이 정해져 있다. "
            "함께 타는 구간(s→k)은 요금을 한 번만 내고, 헤어진 뒤(k→a, k→b)는 각자 낸다. "
            "두 사람의 요금 합이 최소가 되도록 할 때 그 최소 요금을 구하세요. "
            "(헤어지는 지점 k 는 s, a, b 자신을 포함해 어디든 될 수 있다.)"
        ),
        input_desc=(
            "n : 지점 수 (1 ≤ n ≤ 200), s : 출발 지점, a : A의 목적지, b : B의 목적지, "
            "fares : 각 원소가 [c, d, f] 인 리스트 (c와 d를 요금 f 에 양방향으로 오갈 수 있다). 지점 번호는 1..n."
        ),
        output_desc="두 사람이 내는 요금 합의 최솟값",
        examples=[
            {
                "args": [6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]],
                "output": 82,
            },
            {
                "args": [7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]],
                "output": 14,
            },
        ],
        hints=[
            "헤어지는 지점 k 를 하나로 고정하면 요금은 (s→k 최단) + (k→a 최단) + (k→b 최단) 입니다. 모든 k 후보 중 최솟값이 답입니다.",
            "모든 지점 쌍의 최단거리가 필요하므로 플로이드-워셜(또는 s, a, b 각각에서 다익스트라 3번)을 쓰면 됩니다. n 이 작아 O(n^3) 으로 충분합니다.",
            "dist[i][j] 를 플로이드로 채운 뒤 answer = min over k of dist[s][k]+dist[k][a]+dist[k][b]. (k=s 이면 함께 안 가는 경우, k=a/b 도 자동 포함)",
        ],
        testcases=[
            {
                "args": [6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]],
                "expected": 82,
            },
            {
                "args": [7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]],
                "expected": 14,
            },
            {
                "args": [6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]],
                "expected": 18,
            },
            {"args": [2, 1, 1, 1, [[1, 2, 5]]], "expected": 0},
            {"args": [3, 1, 2, 3, [[1, 2, 4], [1, 3, 7], [2, 3, 1]]], "expected": 5},
        ],
        reference_py=(
            "def solution(n, s, a, b, fares):\n"
            "    INF = float('inf')\n"
            "    dist = [[INF] * (n + 1) for _ in range(n + 1)]\n"
            "    for i in range(1, n + 1):\n"
            "        dist[i][i] = 0\n"
            "    for c, d, f in fares:\n"
            "        if f < dist[c][d]:\n"
            "            dist[c][d] = f\n"
            "            dist[d][c] = f\n"
            "    for k in range(1, n + 1):\n"
            "        for i in range(1, n + 1):\n"
            "            dik = dist[i][k]\n"
            "            if dik == INF:\n"
            "                continue\n"
            "            row = dist[i]\n"
            "            rowk = dist[k]\n"
            "            for j in range(1, n + 1):\n"
            "                nd = dik + rowk[j]\n"
            "                if nd < row[j]:\n"
            "                    row[j] = nd\n"
            "    ans = INF\n"
            "    for k in range(1, n + 1):\n"
            "        ans = min(ans, dist[s][k] + dist[k][a] + dist[k][b])\n"
            "    return ans\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int solution(int n, int s, int a, int b, int[][] fares) {\n"
            "        long INF = Long.MAX_VALUE / 4;\n"
            "        long[][] dist = new long[n + 1][n + 1];\n"
            "        for (long[] row : dist) Arrays.fill(row, INF);\n"
            "        for (int i = 1; i <= n; i++) dist[i][i] = 0;\n"
            "        for (int[] f : fares) {\n"
            "            dist[f[0]][f[1]] = Math.min(dist[f[0]][f[1]], f[2]);\n"
            "            dist[f[1]][f[0]] = Math.min(dist[f[1]][f[0]], f[2]);\n"
            "        }\n"
            "        for (int k = 1; k <= n; k++)\n"
            "            for (int i = 1; i <= n; i++)\n"
            "                for (int j = 1; j <= n; j++)\n"
            "                    if (dist[i][k] + dist[k][j] < dist[i][j])\n"
            "                        dist[i][j] = dist[i][k] + dist[k][j];\n"
            "        long ans = INF;\n"
            "        for (int k = 1; k <= n; k++)\n"
            "            ans = Math.min(ans, dist[s][k] + dist[k][a] + dist[k][b]);\n"
            "        return (int) ans;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 합승 택시 최소 요금 : (s->k)+(k->a)+(k->b) 의 최솟값\n"
            "def solution(n, s, a, b, fares):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

]
