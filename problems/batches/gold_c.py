"""골드 랭크 추가 배치 C — 최단경로 / 유니온-파인드 / 비트마스크 / 그리디 / 시뮬레이션.

gold-36 ~ gold-50 (15문제).
"""

from engine.models import Problem

RANK = "Gold"

PROBLEMS = [

    Problem(
        id="gold-36",
        rank="Gold",
        title="다익스트라 최단 거리",
        style="백준",
        topic="다익스트라",
        type="stdin",
        description=(
            "방향 그래프가 주어진다. 시작 정점 S에서 각 정점까지 가는 최단 거리를 "
            "구하세요. 간선의 가중치는 모두 양수이며, 도달할 수 없는 정점은 INF로 "
            "출력합니다."
        ),
        input_desc=(
            "첫째 줄에 정점 수 N과 간선 수 M. 둘째 줄에 시작 정점 S. "
            "이어 M개의 줄에 'u v w' (정점 u에서 v로 가는 가중치 w의 방향 간선). "
            "정점 번호는 1부터 N까지이다."
        ),
        output_desc="1번 정점부터 N번 정점까지 각각의 최단 거리를 한 줄에 하나씩 출력. 도달 불가는 INF.",
        examples=[
            {"input": "5 6\n1\n1 2 2\n1 3 3\n2 3 4\n2 4 5\n3 4 6\n4 5 1\n", "output": "0\n2\n3\n7\n8\n"},
            {"input": "3 2\n1\n1 2 5\n2 3 2\n", "output": "0\n5\n7\n"},
        ],
        hints=[
            "이미 확정된 최단 거리 중 '가장 가까운' 정점부터 처리하면, 그 정점의 거리는 더 줄어들 수 없습니다.",
            "우선순위 큐(최소 힙)를 사용하는 다익스트라 알고리즘을 적용하세요. (거리, 정점)을 힙에 넣고 꺼냅니다.",
            "dist[S]=0; 힙에서 (d,u)를 꺼내 d>dist[u]면 skip; 인접 v에 대해 d+w<dist[v]면 갱신 후 push.",
        ],
        testcases=[
            {"input": "5 6\n1\n1 2 2\n1 3 3\n2 3 4\n2 4 5\n3 4 6\n4 5 1\n", "output": "0\n2\n3\n7\n8\n"},
            {"input": "3 2\n1\n1 2 5\n2 3 2\n", "output": "0\n5\n7\n"},
            {"input": "2 0\n2\n", "output": "INF\n0\n"},
            {"input": "4 4\n1\n1 2 1\n2 3 1\n3 4 1\n1 4 10\n", "output": "0\n1\n2\n3\n"},
            {"input": "1 0\n1\n", "output": "0\n"},
        ],
        reference_py=(
            "import sys, heapq\n"
            "input = sys.stdin.readline\n"
            "def main():\n"
            "    n, m = map(int, input().split())\n"
            "    s = int(input())\n"
            "    graph = [[] for _ in range(n + 1)]\n"
            "    for _ in range(m):\n"
            "        u, v, w = map(int, input().split())\n"
            "        graph[u].append((v, w))\n"
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
            "    out = []\n"
            "    for i in range(1, n + 1):\n"
            "        out.append('INF' if dist[i] == INF else str(dist[i]))\n"
            "    print('\\n'.join(out))\n"
            "main()\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());\n"
            "        int s = Integer.parseInt(br.readLine().trim());\n"
            "        List<int[]>[] g = new List[n + 1];\n"
            "        for (int i = 0; i <= n; i++) g[i] = new ArrayList<>();\n"
            "        for (int i = 0; i < m; i++) {\n"
            "            st = new StringTokenizer(br.readLine());\n"
            "            int u = Integer.parseInt(st.nextToken());\n"
            "            int v = Integer.parseInt(st.nextToken());\n"
            "            int w = Integer.parseInt(st.nextToken());\n"
            "            g[u].add(new int[]{v, w});\n"
            "        }\n"
            "        long INF = Long.MAX_VALUE / 4;\n"
            "        long[] dist = new long[n + 1];\n"
            "        Arrays.fill(dist, INF);\n"
            "        dist[s] = 0;\n"
            "        PriorityQueue<long[]> pq = new PriorityQueue<>((a, b) -> Long.compare(a[0], b[0]));\n"
            "        pq.add(new long[]{0, s});\n"
            "        while (!pq.isEmpty()) {\n"
            "            long[] c = pq.poll();\n"
            "            long d = c[0]; int u = (int) c[1];\n"
            "            if (d > dist[u]) continue;\n"
            "            for (int[] e : g[u]) {\n"
            "                long nd = d + e[1];\n"
            "                if (nd < dist[e[0]]) { dist[e[0]] = nd; pq.add(new long[]{nd, e[0]}); }\n"
            "            }\n"
            "        }\n"
            "        StringBuilder sb = new StringBuilder();\n"
            "        for (int i = 1; i <= n; i++) sb.append(dist[i] == INF ? \"INF\" : dist[i]).append('\\n');\n"
            "        System.out.print(sb);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys, heapq\n"
            "input = sys.stdin.readline\n"
            "# 다익스트라 최단 거리\n"
            "def main():\n"
            "    n, m = map(int, input().split())\n"
            "    s = int(input())\n"
            "    # ...\n"
            "main()\n"
        ),
    ),

    Problem(
        id="gold-37",
        rank="Gold",
        title="플로이드-워셜 모든 쌍 최단 거리",
        style="백준",
        topic="플로이드워셜",
        type="stdin",
        description=(
            "방향 그래프에서 모든 정점 쌍 (i, j)에 대해 i에서 j로 가는 최단 거리를 "
            "구하세요. 같은 정점 쌍은 거리 0, 도달할 수 없는 쌍도 0으로 출력합니다. "
            "두 정점 사이에 여러 간선이 있으면 가장 작은 가중치를 사용합니다."
        ),
        input_desc=(
            "첫째 줄에 정점 수 N과 간선 수 M. 이어 M개의 줄에 'u v w' "
            "(정점 u에서 v로 가는 가중치 w의 방향 간선). 정점 번호는 1부터 N까지이다."
        ),
        output_desc="N개의 줄에 걸쳐 i행 j열이 i에서 j까지의 최단 거리인 N×N 행렬을 공백으로 구분해 출력.",
        examples=[
            {"input": "3 4\n1 2 3\n2 3 4\n1 3 10\n3 1 2\n", "output": "0 3 7\n6 0 4\n2 5 0\n"},
            {"input": "2 1\n1 2 5\n", "output": "0 5\n0 0\n"},
        ],
        hints=[
            "정점 k를 '경유지'로 허용했을 때 i→j 거리가 줄어드는지 모든 i, j에 대해 갱신하는 것을 생각하세요.",
            "플로이드-워셜 알고리즘입니다. k, i, j 삼중 반복으로 dist[i][j]를 최소화합니다.",
            "for k: for i: for j: if dist[i][k]+dist[k][j]<dist[i][j]: dist[i][j]=dist[i][k]+dist[k][j]. 초기 dist[i][i]=0, 나머지 INF.",
        ],
        testcases=[
            {"input": "3 4\n1 2 3\n2 3 4\n1 3 10\n3 1 2\n", "output": "0 3 7\n6 0 4\n2 5 0\n"},
            {"input": "2 1\n1 2 5\n", "output": "0 5\n0 0\n"},
            {"input": "1 0\n", "output": "0\n"},
            {"input": "4 5\n1 2 1\n2 3 1\n3 4 1\n1 4 100\n4 1 1\n", "output": "0 1 2 3\n3 0 1 2\n2 3 0 1\n1 2 3 0\n"},
        ],
        reference_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "def main():\n"
            "    n, m = map(int, input().split())\n"
            "    INF = float('inf')\n"
            "    dist = [[INF] * (n + 1) for _ in range(n + 1)]\n"
            "    for i in range(1, n + 1):\n"
            "        dist[i][i] = 0\n"
            "    for _ in range(m):\n"
            "        u, v, w = map(int, input().split())\n"
            "        if w < dist[u][v]:\n"
            "            dist[u][v] = w\n"
            "    for k in range(1, n + 1):\n"
            "        for i in range(1, n + 1):\n"
            "            for j in range(1, n + 1):\n"
            "                if dist[i][k] + dist[k][j] < dist[i][j]:\n"
            "                    dist[i][j] = dist[i][k] + dist[k][j]\n"
            "    out = []\n"
            "    for i in range(1, n + 1):\n"
            "        row = [str(0 if dist[i][j] == INF else dist[i][j]) for j in range(1, n + 1)]\n"
            "        out.append(' '.join(row))\n"
            "    print('\\n'.join(out))\n"
            "main()\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());\n"
            "        long INF = Long.MAX_VALUE / 4;\n"
            "        long[][] d = new long[n + 1][n + 1];\n"
            "        for (long[] r : d) Arrays.fill(r, INF);\n"
            "        for (int i = 1; i <= n; i++) d[i][i] = 0;\n"
            "        for (int e = 0; e < m; e++) {\n"
            "            st = new StringTokenizer(br.readLine());\n"
            "            int u = Integer.parseInt(st.nextToken());\n"
            "            int v = Integer.parseInt(st.nextToken());\n"
            "            int w = Integer.parseInt(st.nextToken());\n"
            "            if (w < d[u][v]) d[u][v] = w;\n"
            "        }\n"
            "        for (int k = 1; k <= n; k++)\n"
            "            for (int i = 1; i <= n; i++)\n"
            "                for (int j = 1; j <= n; j++)\n"
            "                    if (d[i][k] + d[k][j] < d[i][j]) d[i][j] = d[i][k] + d[k][j];\n"
            "        StringBuilder sb = new StringBuilder();\n"
            "        for (int i = 1; i <= n; i++) {\n"
            "            for (int j = 1; j <= n; j++) {\n"
            "                sb.append(d[i][j] == INF ? 0 : d[i][j]);\n"
            "                if (j < n) sb.append(' ');\n"
            "            }\n"
            "            sb.append('\\n');\n"
            "        }\n"
            "        System.out.print(sb);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "# 플로이드-워셜 모든 쌍 최단 거리\n"
            "def main():\n"
            "    n, m = map(int, input().split())\n"
            "    # ...\n"
            "main()\n"
        ),
    ),

    Problem(
        id="gold-38",
        rank="Gold",
        title="무방향 그래프 사이클 판별",
        style="해외대기업",
        topic="유니온파인드",
        type="func",
        func_name="solution",
        description=(
            "정점 번호가 1부터 n까지인 무방향 그래프가 간선 목록 edges로 주어진다. "
            "이 그래프에 사이클이 하나라도 존재하면 True, 없으면 False를 반환하세요. "
            "(두 정점을 잇는 간선이 두 번 이상 주어지면 그 자체로 사이클로 본다.)"
        ),
        input_desc="n : 정점 수, edges : [u, v] 형태의 무방향 간선 리스트",
        output_desc="사이클이 존재하면 True, 아니면 False",
        examples=[
            {"args": [3, [[1, 2], [2, 3], [1, 3]]], "output": True},
            {"args": [3, [[1, 2], [2, 3]]], "output": False},
        ],
        hints=[
            "간선을 하나씩 추가하면서, 두 정점이 '이미 같은 그룹'이면 그 간선이 사이클을 만든다는 사실을 이용하세요.",
            "유니온-파인드(분리 집합)를 사용하세요. find로 두 정점의 루트를 찾고, 같으면 사이클입니다.",
            "for u,v in edges: if find(u)==find(v): return True; else union(u,v). 끝까지 같지 않으면 return False.",
        ],
        testcases=[
            {"args": [3, [[1, 2], [2, 3], [1, 3]]], "expected": True},
            {"args": [3, [[1, 2], [2, 3]]], "expected": False},
            {"args": [4, [[1, 2], [3, 4]]], "expected": False},
            {"args": [2, [[1, 2], [1, 2]]], "expected": True},
            {"args": [1, []], "expected": False},
        ],
        reference_py=(
            "def solution(n, edges):\n"
            "    parent = list(range(n + 1))\n"
            "    def find(x):\n"
            "        while parent[x] != x:\n"
            "            parent[x] = parent[parent[x]]\n"
            "            x = parent[x]\n"
            "        return x\n"
            "    for u, v in edges:\n"
            "        ru, rv = find(u), find(v)\n"
            "        if ru == rv:\n"
            "            return True\n"
            "        parent[ru] = rv\n"
            "    return False\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    int[] parent;\n"
            "    int find(int x) {\n"
            "        while (parent[x] != x) { parent[x] = parent[parent[x]]; x = parent[x]; }\n"
            "        return x;\n"
            "    }\n"
            "    public boolean solution(int n, int[][] edges) {\n"
            "        parent = new int[n + 1];\n"
            "        for (int i = 0; i <= n; i++) parent[i] = i;\n"
            "        for (int[] e : edges) {\n"
            "            int ru = find(e[0]), rv = find(e[1]);\n"
            "            if (ru == rv) return true;\n"
            "            parent[ru] = rv;\n"
            "        }\n"
            "        return false;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 무방향 그래프 사이클 판별 (유니온-파인드)\n"
            "def solution(n, edges):\n"
            "    answer = False\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="gold-39",
        rank="Gold",
        title="친구 네트워크 크기",
        style="프로그래머스",
        topic="유니온파인드",
        type="func",
        func_name="solution",
        description=(
            "두 사람의 이름 쌍이 시간 순서대로 operations에 주어진다. 각 쌍이 등장할 때마다 "
            "두 사람은 친구가 되며, 친구의 친구도 모두 같은 네트워크에 속한다. 각 쌍이 "
            "처리된 직후 그 두 사람이 속한 친구 네트워크의 인원 수를 순서대로 모은 "
            "리스트를 반환하세요."
        ),
        input_desc="operations : [이름A, 이름B] 형태(문자열)의 친구 관계 리스트",
        output_desc="각 관계 처리 직후 해당 네트워크의 인원 수를 담은 정수 리스트",
        examples=[
            {"args": [[["Fehead", "Mund"], ["Mund", "Sahur"], ["Sahur", "Mund"]]], "output": [2, 3, 3]},
            {"args": [[["a", "b"], ["c", "d"], ["b", "c"]]], "output": [2, 2, 4]},
        ],
        hints=[
            "사람을 처음 볼 때마다 새 그룹(크기 1)으로 만들고, 친구가 되면 두 그룹을 합칩니다.",
            "유니온-파인드에 그룹 크기 배열을 함께 관리하세요. union 시 합쳐진 루트의 크기를 더합니다.",
            "이름을 사전으로 관리; 처음 보면 parent[x]=x,size[x]=1; union(a,b)에서 size[새루트]+=size[옛루트]; 답은 size[find(a)].",
        ],
        testcases=[
            {"args": [[["Fehead", "Mund"], ["Mund", "Sahur"], ["Sahur", "Mund"]]], "expected": [2, 3, 3]},
            {"args": [[["a", "b"], ["c", "d"], ["b", "c"]]], "expected": [2, 2, 4]},
            {"args": [[["x", "y"]]], "expected": [2]},
            {"args": [[["p", "q"], ["p", "q"], ["q", "p"]]], "expected": [2, 2, 2]},
            {"args": [[["a", "b"], ["b", "c"], ["d", "e"], ["c", "d"]]], "expected": [2, 3, 2, 5]},
        ],
        reference_py=(
            "def solution(operations):\n"
            "    parent = {}\n"
            "    size = {}\n"
            "    def add(x):\n"
            "        if x not in parent:\n"
            "            parent[x] = x\n"
            "            size[x] = 1\n"
            "    def find(x):\n"
            "        while parent[x] != x:\n"
            "            parent[x] = parent[parent[x]]\n"
            "            x = parent[x]\n"
            "        return x\n"
            "    res = []\n"
            "    for a, b in operations:\n"
            "        add(a)\n"
            "        add(b)\n"
            "        ra, rb = find(a), find(b)\n"
            "        if ra != rb:\n"
            "            parent[ra] = rb\n"
            "            size[rb] += size[ra]\n"
            "        res.append(size[find(a)])\n"
            "    return res\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    Map<String, String> parent = new HashMap<>();\n"
            "    Map<String, Integer> size = new HashMap<>();\n"
            "    void add(String x) { if (!parent.containsKey(x)) { parent.put(x, x); size.put(x, 1); } }\n"
            "    String find(String x) {\n"
            "        while (!parent.get(x).equals(x)) { parent.put(x, parent.get(parent.get(x))); x = parent.get(x); }\n"
            "        return x;\n"
            "    }\n"
            "    public int[] solution(String[][] operations) {\n"
            "        int[] res = new int[operations.length];\n"
            "        for (int i = 0; i < operations.length; i++) {\n"
            "            String a = operations[i][0], b = operations[i][1];\n"
            "            add(a); add(b);\n"
            "            String ra = find(a), rb = find(b);\n"
            "            if (!ra.equals(rb)) { parent.put(ra, rb); size.put(rb, size.get(rb) + size.get(ra)); }\n"
            "            res[i] = size.get(find(a));\n"
            "        }\n"
            "        return res;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 친구 네트워크 크기 (유니온-파인드 + 크기 관리)\n"
            "def solution(operations):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="gold-40",
        rank="Gold",
        title="연결 그래프 판별",
        style="대기업",
        topic="유니온파인드",
        type="func",
        func_name="solution",
        description=(
            "정점 번호가 1부터 n까지인 무방향 그래프가 간선 목록 edges로 주어진다. "
            "모든 정점이 하나의 덩어리로 연결되어 있으면(임의의 두 정점 사이에 경로가 "
            "존재하면) True, 그렇지 않으면 False를 반환하세요."
        ),
        input_desc="n : 정점 수, edges : [u, v] 형태의 무방향 간선 리스트",
        output_desc="그래프가 하나로 연결되어 있으면 True, 아니면 False",
        examples=[
            {"args": [4, [[1, 2], [2, 3], [3, 4]]], "output": True},
            {"args": [4, [[1, 2], [3, 4]]], "output": False},
        ],
        hints=[
            "모든 간선으로 정점들을 합쳤을 때 남는 '서로 다른 그룹'이 하나뿐이면 연결된 그래프입니다.",
            "유니온-파인드로 모든 간선을 union한 뒤, 모든 정점의 루트가 단 하나인지 확인하세요.",
            "for u,v in edges: union(u,v); roots={find(i) for i in 1..n}; return len(roots)==1.",
        ],
        testcases=[
            {"args": [4, [[1, 2], [2, 3], [3, 4]]], "expected": True},
            {"args": [4, [[1, 2], [3, 4]]], "expected": False},
            {"args": [1, []], "expected": True},
            {"args": [3, [[1, 2], [2, 3], [1, 3]]], "expected": True},
            {"args": [5, [[1, 2], [2, 3], [4, 5]]], "expected": False},
        ],
        reference_py=(
            "def solution(n, edges):\n"
            "    parent = list(range(n + 1))\n"
            "    def find(x):\n"
            "        while parent[x] != x:\n"
            "            parent[x] = parent[parent[x]]\n"
            "            x = parent[x]\n"
            "        return x\n"
            "    for u, v in edges:\n"
            "        parent[find(u)] = find(v)\n"
            "    roots = {find(i) for i in range(1, n + 1)}\n"
            "    return len(roots) == 1\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    int[] parent;\n"
            "    int find(int x) {\n"
            "        while (parent[x] != x) { parent[x] = parent[parent[x]]; x = parent[x]; }\n"
            "        return x;\n"
            "    }\n"
            "    public boolean solution(int n, int[][] edges) {\n"
            "        parent = new int[n + 1];\n"
            "        for (int i = 0; i <= n; i++) parent[i] = i;\n"
            "        for (int[] e : edges) parent[find(e[0])] = find(e[1]);\n"
            "        Set<Integer> roots = new HashSet<>();\n"
            "        for (int i = 1; i <= n; i++) roots.add(find(i));\n"
            "        return roots.size() == 1;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 연결 그래프 판별 (유니온-파인드)\n"
            "def solution(n, edges):\n"
            "    answer = False\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="gold-41",
        rank="Gold",
        title="부분집합 합 개수 (비트마스크)",
        style="해외대기업",
        topic="비트마스크",
        type="func",
        func_name="solution",
        description=(
            "정수 배열 nums의 모든 '공집합이 아닌 부분집합' 중에서, 원소들의 합이 "
            "target과 정확히 일치하는 부분집합이 몇 개인지 세어 반환하세요. "
            "배열의 길이는 20 이하입니다."
        ),
        input_desc="nums : 정수 리스트(길이 ≤ 20), target : 목표 합",
        output_desc="합이 target인 공집합이 아닌 부분집합의 개수",
        examples=[
            {"args": [[1, 2, 3, 4, 5], 5], "output": 3},
            {"args": [[2, 2, 2], 4], "output": 3},
        ],
        hints=[
            "원소가 n개면 부분집합은 2^n개입니다. 각 부분집합을 0/1 선택의 조합으로 표현할 수 있습니다.",
            "비트마스크로 1부터 2^n-1까지 순회하면서, 켜진 비트에 해당하는 원소만 더해 합을 구하세요.",
            "for mask in range(1, 1<<n): s=sum(nums[i] for i in range(n) if mask>>i&1); if s==target: cnt+=1.",
        ],
        testcases=[
            {"args": [[1, 2, 3, 4, 5], 5], "expected": 3},
            {"args": [[2, 2, 2], 4], "expected": 3},
            {"args": [[1, 1, 1, 1], 2], "expected": 6},
            {"args": [[5], 5], "expected": 1},
            {"args": [[1, 2, 3], 7], "expected": 0},
        ],
        reference_py=(
            "def solution(nums, target):\n"
            "    n = len(nums)\n"
            "    cnt = 0\n"
            "    for mask in range(1, 1 << n):\n"
            "        s = 0\n"
            "        for i in range(n):\n"
            "            if mask >> i & 1:\n"
            "                s += nums[i]\n"
            "        if s == target:\n"
            "            cnt += 1\n"
            "    return cnt\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int[] nums, int target) {\n"
            "        int n = nums.length, cnt = 0;\n"
            "        for (int mask = 1; mask < (1 << n); mask++) {\n"
            "            long s = 0;\n"
            "            for (int i = 0; i < n; i++) if ((mask >> i & 1) == 1) s += nums[i];\n"
            "            if (s == target) cnt++;\n"
            "        }\n"
            "        return cnt;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 부분집합 합 개수 (비트마스크 부분집합 순회)\n"
            "def solution(nums, target):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="gold-42",
        rank="Gold",
        title="회의실 배정 최대 개수",
        style="백준",
        topic="그리디",
        type="func",
        func_name="solution",
        description=(
            "하나의 회의실에 대해 여러 회의의 (시작 시각, 종료 시각) 목록이 주어진다. "
            "회의는 한 번 시작하면 중간에 멈출 수 없고, 한 회의가 끝나는 시각에 다른 "
            "회의가 시작해도 된다. 회의실을 사용할 수 있는 회의의 최대 개수를 반환하세요."
        ),
        input_desc="meetings : [시작, 종료] 형태의 회의 리스트",
        output_desc="겹치지 않게 배정할 수 있는 최대 회의 개수",
        examples=[
            {"args": [[[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]], "output": 4},
            {"args": [[[1, 2], [2, 3], [3, 4]]], "output": 3},
        ],
        hints=[
            "가능한 한 빨리 끝나는 회의를 먼저 선택할수록 남는 시간이 많아져 더 많은 회의를 넣을 수 있습니다.",
            "종료 시각 기준으로 오름차순 정렬한 뒤, 직전에 선택한 회의의 종료 시각 이후에 시작하는 회의를 탐욕적으로 고릅니다.",
            "정렬 키=(종료, 시작); end=-inf; for s,e: if s>=end: cnt+=1; end=e. 답은 cnt.",
        ],
        testcases=[
            {"args": [[[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]], "expected": 4},
            {"args": [[[1, 2], [2, 3], [3, 4]]], "expected": 3},
            {"args": [[[1, 5], [2, 3]]], "expected": 1},
            {"args": [[[0, 1]]], "expected": 1},
            {"args": [[[1, 3], [1, 3], [1, 3]]], "expected": 1},
        ],
        reference_py=(
            "def solution(meetings):\n"
            "    ms = sorted(meetings, key=lambda x: (x[1], x[0]))\n"
            "    cnt = 0\n"
            "    end = float('-inf')\n"
            "    for s, e in ms:\n"
            "        if s >= end:\n"
            "            cnt += 1\n"
            "            end = e\n"
            "    return cnt\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int solution(int[][] meetings) {\n"
            "        Arrays.sort(meetings, (a, b) -> a[1] != b[1] ? a[1] - b[1] : a[0] - b[0]);\n"
            "        int cnt = 0;\n"
            "        long end = Long.MIN_VALUE;\n"
            "        for (int[] m : meetings) {\n"
            "            if (m[0] >= end) { cnt++; end = m[1]; }\n"
            "        }\n"
            "        return cnt;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 회의실 배정 최대 개수 (그리디)\n"
            "def solution(meetings):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="gold-43",
        rank="Gold",
        title="LRU 캐시 실행 시간",
        style="프로그래머스",
        topic="그리디",
        type="func",
        func_name="solution",
        description=(
            "크기 cache_size인 캐시가 LRU(가장 오래 사용되지 않은 항목 교체) 정책으로 "
            "동작한다. 요청 도시 이름들이 순서대로 requests에 주어질 때, 캐시에 있으면 "
            "(캐시 히트) 1, 없으면(캐시 미스) 5의 시간이 든다. 도시 이름은 대소문자를 "
            "구분하지 않는다. 전체 요청을 처리하는 데 걸리는 총 실행 시간을 반환하세요."
        ),
        input_desc="cache_size : 캐시 크기(0 이상), requests : 도시 이름 문자열 리스트",
        output_desc="전체 요청 처리에 걸리는 총 실행 시간",
        examples=[
            {"args": [3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]], "output": 50},
            {"args": [2, ["A", "A", "A"]], "output": 7},
        ],
        hints=[
            "캐시 크기가 0이면 항상 미스이므로 요청 수 × 5가 됩니다. 먼저 이 경계를 처리하세요.",
            "최근 사용 순서를 유지해야 하므로 큐(또는 순서 있는 자료구조)로 LRU를 구현합니다. 도시 이름은 소문자로 통일하세요.",
            "히트면 해당 항목을 맨 뒤로 옮기고 +1; 미스면 가득 찼을 때 맨 앞 제거 후 맨 뒤 삽입하고 +5.",
        ],
        testcases=[
            {"args": [3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]], "expected": 50},
            {"args": [2, ["A", "A", "A"]], "expected": 7},
            {"args": [0, ["a", "b"]], "expected": 10},
            {"args": [2, ["a", "b", "c", "a"]], "expected": 20},
            {"args": [2, ["a", "b", "a", "c", "a"]], "expected": 17},
        ],
        reference_py=(
            "from collections import deque\n"
            "def solution(cache_size, requests):\n"
            "    if cache_size == 0:\n"
            "        return len(requests) * 5\n"
            "    cache = deque()\n"
            "    time = 0\n"
            "    for c in requests:\n"
            "        c = c.lower()\n"
            "        if c in cache:\n"
            "            cache.remove(c)\n"
            "            cache.append(c)\n"
            "            time += 1\n"
            "        else:\n"
            "            if len(cache) >= cache_size:\n"
            "                cache.popleft()\n"
            "            cache.append(c)\n"
            "            time += 5\n"
            "    return time\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int solution(int cacheSize, String[] requests) {\n"
            "        if (cacheSize == 0) return requests.length * 5;\n"
            "        LinkedList<String> cache = new LinkedList<>();\n"
            "        int time = 0;\n"
            "        for (String raw : requests) {\n"
            "            String c = raw.toLowerCase();\n"
            "            if (cache.contains(c)) { cache.remove(c); cache.addLast(c); time += 1; }\n"
            "            else {\n"
            "                if (cache.size() >= cacheSize) cache.removeFirst();\n"
            "                cache.addLast(c); time += 5;\n"
            "            }\n"
            "        }\n"
            "        return time;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# LRU 캐시 실행 시간\n"
            "def solution(cache_size, requests):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="gold-44",
        rank="Gold",
        title="강의실 최소 개수",
        style="해외대기업",
        topic="그리디",
        type="func",
        func_name="solution",
        description=(
            "여러 강의의 (시작 시각, 종료 시각) 목록이 주어진다. 한 강의는 [시작, 종료) "
            "구간 동안 강의실 하나를 사용하며, 한 강의가 종료하는 시각에 같은 강의실에서 "
            "다른 강의가 시작할 수 있다. 모든 강의를 진행하기 위해 필요한 강의실의 최소 "
            "개수를 반환하세요."
        ),
        input_desc="lectures : [시작, 종료] 형태의 강의 리스트",
        output_desc="모든 강의를 수용하는 데 필요한 강의실의 최소 개수",
        examples=[
            {"args": [[[1, 3], [2, 4], [3, 5]]], "output": 2},
            {"args": [[[0, 10], [1, 2], [3, 4]]], "output": 2},
        ],
        hints=[
            "어느 한 시점에 '동시에 진행 중'인 강의가 가장 많은 수가 곧 필요한 강의실 수입니다.",
            "시작 시각과 종료 시각을 각각 정렬한 뒤, 두 포인터로 훑으며 현재 진행 중인 강의 수의 최댓값을 구합니다.",
            "starts/ends 정렬; i=j=0; while i<n: if starts[i]<ends[j]: rooms+=1,i+=1,mx 갱신 else rooms-=1,j+=1.",
        ],
        testcases=[
            {"args": [[[1, 3], [2, 4], [3, 5]]], "expected": 2},
            {"args": [[[0, 10], [1, 2], [3, 4]]], "expected": 2},
            {"args": [[[1, 2], [2, 3], [3, 4]]], "expected": 1},
            {"args": [[[0, 5]]], "expected": 1},
            {"args": [[[1, 4], [2, 3], [3, 6], [5, 7], [0, 8]]], "expected": 3},
        ],
        reference_py=(
            "def solution(lectures):\n"
            "    starts = sorted(s for s, e in lectures)\n"
            "    ends = sorted(e for s, e in lectures)\n"
            "    n = len(lectures)\n"
            "    rooms = 0\n"
            "    mx = 0\n"
            "    i = j = 0\n"
            "    while i < n:\n"
            "        if starts[i] < ends[j]:\n"
            "            rooms += 1\n"
            "            i += 1\n"
            "            if rooms > mx:\n"
            "                mx = rooms\n"
            "        else:\n"
            "            rooms -= 1\n"
            "            j += 1\n"
            "    return mx\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int solution(int[][] lectures) {\n"
            "        int n = lectures.length;\n"
            "        int[] starts = new int[n], ends = new int[n];\n"
            "        for (int i = 0; i < n; i++) { starts[i] = lectures[i][0]; ends[i] = lectures[i][1]; }\n"
            "        Arrays.sort(starts);\n"
            "        Arrays.sort(ends);\n"
            "        int rooms = 0, mx = 0, i = 0, j = 0;\n"
            "        while (i < n) {\n"
            "            if (starts[i] < ends[j]) { rooms++; i++; mx = Math.max(mx, rooms); }\n"
            "            else { rooms--; j++; }\n"
            "        }\n"
            "        return mx;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 강의실 최소 개수 (그리디 / 스위핑)\n"
            "def solution(lectures):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="gold-45",
        rank="Gold",
        title="회전하는 큐 최소 연산",
        style="백준",
        topic="시뮬레이션",
        type="stdin",
        description=(
            "1번부터 N번까지의 원소가 차례로 들어 있는 양방향 큐가 있다. 항상 큐의 맨 "
            "앞 원소를 뽑아낼 수 있고, 그 외에 (1) 왼쪽으로 한 칸 회전(맨 앞을 맨 뒤로), "
            "(2) 오른쪽으로 한 칸 회전(맨 뒤를 맨 앞으로) 연산을 쓸 수 있다. 주어진 위치의 "
            "원소들을 순서대로 모두 뽑아내는 데 필요한 회전 연산의 최소 횟수를 구하세요."
        ),
        input_desc=(
            "첫째 줄에 큐 크기 N과 뽑아낼 원소의 개수 M. 둘째 줄에 뽑아낼 원소 M개의 "
            "번호가 순서대로 주어진다."
        ),
        output_desc="모든 원소를 뽑아내기 위한 회전 연산의 최소 총 횟수.",
        examples=[
            {"input": "10 3\n1 2 3\n", "output": "0\n"},
            {"input": "10 3\n2 9 5\n", "output": "8\n"},
        ],
        hints=[
            "뽑을 원소가 현재 큐에서 앞쪽 절반에 있으면 왼쪽 회전이, 뒤쪽 절반에 있으면 오른쪽 회전이 더 짧습니다.",
            "덱(deque)으로 직접 시뮬레이션하세요. 매번 목표 원소의 현재 인덱스를 찾아 더 가까운 방향으로 회전합니다.",
            "idx=dq.index(t); 앞쪽이면 idx번 popleft→append, 뒤쪽이면 len-idx번 pop→appendleft, 회전 수 누적 후 popleft로 제거.",
        ],
        testcases=[
            {"input": "10 3\n1 2 3\n", "output": "0\n"},
            {"input": "10 3\n2 9 5\n", "output": "8\n"},
            {"input": "32 6\n27 16 30 11 6 23\n", "output": "59\n"},
            {"input": "5 1\n5\n", "output": "1\n"},
            {"input": "1 1\n1\n", "output": "0\n"},
        ],
        reference_py=(
            "import sys\n"
            "from collections import deque\n"
            "input = sys.stdin.readline\n"
            "def main():\n"
            "    n, m = map(int, input().split())\n"
            "    targets = list(map(int, input().split()))\n"
            "    dq = deque(range(1, n + 1))\n"
            "    count = 0\n"
            "    for t in targets:\n"
            "        idx = dq.index(t)\n"
            "        half = len(dq) // 2\n"
            "        if idx <= half:\n"
            "            for _ in range(idx):\n"
            "                dq.append(dq.popleft())\n"
            "                count += 1\n"
            "        else:\n"
            "            for _ in range(len(dq) - idx):\n"
            "                dq.appendleft(dq.pop())\n"
            "                count += 1\n"
            "        dq.popleft()\n"
            "    print(count)\n"
            "main()\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());\n"
            "        Deque<Integer> dq = new ArrayDeque<>();\n"
            "        for (int i = 1; i <= n; i++) dq.addLast(i);\n"
            "        st = new StringTokenizer(br.readLine());\n"
            "        int count = 0;\n"
            "        for (int k = 0; k < m; k++) {\n"
            "            int t = Integer.parseInt(st.nextToken());\n"
            "            List<Integer> cur = new ArrayList<>(dq);\n"
            "            int idx = cur.indexOf(t);\n"
            "            int half = dq.size() / 2;\n"
            "            if (idx <= half) {\n"
            "                for (int i = 0; i < idx; i++) { dq.addLast(dq.pollFirst()); count++; }\n"
            "            } else {\n"
            "                for (int i = 0; i < dq.size() - idx; i++) { dq.addFirst(dq.pollLast()); count++; }\n"
            "            }\n"
            "            dq.pollFirst();\n"
            "        }\n"
            "        System.out.println(count);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "from collections import deque\n"
            "input = sys.stdin.readline\n"
            "# 회전하는 큐 최소 연산\n"
            "def main():\n"
            "    n, m = map(int, input().split())\n"
            "    # ...\n"
            "main()\n"
        ),
    ),

    Problem(
        id="gold-46",
        rank="Gold",
        title="뱀 게임 시뮬레이션",
        style="대기업",
        topic="시뮬레이션",
        type="stdin",
        description=(
            "N×N 보드의 (1,1)에서 길이 1의 뱀이 오른쪽을 향해 시작한다. 매 초마다 뱀은 "
            "머리를 향한 방향으로 한 칸 이동한다. 이동한 칸에 사과가 있으면 사과를 먹고 "
            "꼬리는 그대로 두어 길이가 1 늘고, 사과가 없으면 꼬리 칸을 비워 길이를 유지한다. "
            "벽이나 자기 몸에 부딪히면 게임이 끝난다. 또한 정해진 시각마다 머리 방향을 "
            "왼쪽(L) 또는 오른쪽(D)으로 90도 회전한다. 게임이 끝나는 시각(초)을 구하세요."
        ),
        input_desc=(
            "첫째 줄 보드 크기 N. 둘째 줄 사과 수 K. 이어 K개의 줄에 사과의 행 열 좌표. "
            "다음 줄 방향 전환 횟수 L. 이어 L개의 줄에 'X C' (X초가 지난 직후 방향 C 회전, "
            "C는 L 또는 D). 좌표는 1부터 시작한다."
        ),
        output_desc="게임이 종료되는 시각(초)을 출력.",
        examples=[
            {"input": "6\n3\n3 4\n2 5\n5 3\n3\n3 D\n15 L\n17 D\n", "output": "9\n"},
            {"input": "10\n4\n1 2\n1 3\n1 4\n1 5\n4\n8 D\n10 D\n11 D\n13 L\n", "output": "21\n"},
        ],
        hints=[
            "뱀의 몸을 좌표들의 순서 있는 목록(덱)으로 관리하면 머리 추가와 꼬리 제거를 쉽게 처리할 수 있습니다.",
            "방향을 (오른쪽, 아래, 왼쪽, 위) 순환으로 두고, D는 +1, L은 -1로 회전하는 시뮬레이션입니다.",
            "매 초: 머리 전진 → 벽/몸 충돌이면 종료; 사과면 머리만 추가, 아니면 꼬리 pop; 해당 시각이면 방향 회전.",
        ],
        testcases=[
            {"input": "6\n3\n3 4\n2 5\n5 3\n3\n3 D\n15 L\n17 D\n", "output": "9\n"},
            {"input": "10\n4\n1 2\n1 3\n1 4\n1 5\n4\n8 D\n10 D\n11 D\n13 L\n", "output": "21\n"},
            {"input": "5\n0\n2\n5 D\n8 L\n", "output": "5\n"},
            {"input": "4\n1\n1 2\n1\n2 D\n", "output": "6\n"},
        ],
        reference_py=(
            "import sys\n"
            "from collections import deque\n"
            "input = sys.stdin.readline\n"
            "def main():\n"
            "    n = int(input())\n"
            "    k = int(input())\n"
            "    apple = set()\n"
            "    for _ in range(k):\n"
            "        r, c = map(int, input().split())\n"
            "        apple.add((r, c))\n"
            "    l = int(input())\n"
            "    moves = []\n"
            "    for _ in range(l):\n"
            "        x, ch = input().split()\n"
            "        moves.append((int(x), ch))\n"
            "    dr = [0, 1, 0, -1]\n"
            "    dc = [1, 0, -1, 0]\n"
            "    d = 0\n"
            "    snake = deque([(1, 1)])\n"
            "    body = {(1, 1)}\n"
            "    time = 0\n"
            "    mi = 0\n"
            "    while True:\n"
            "        time += 1\n"
            "        hr, hc = snake[0]\n"
            "        nr, nc = hr + dr[d], hc + dc[d]\n"
            "        if not (1 <= nr <= n and 1 <= nc <= n) or (nr, nc) in body:\n"
            "            break\n"
            "        snake.appendleft((nr, nc))\n"
            "        body.add((nr, nc))\n"
            "        if (nr, nc) in apple:\n"
            "            apple.discard((nr, nc))\n"
            "        else:\n"
            "            tr, tc = snake.pop()\n"
            "            body.discard((tr, tc))\n"
            "        if mi < len(moves) and moves[mi][0] == time:\n"
            "            if moves[mi][1] == 'D':\n"
            "                d = (d + 1) % 4\n"
            "            else:\n"
            "                d = (d - 1) % 4\n"
            "            mi += 1\n"
            "    print(time)\n"
            "main()\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        int n = Integer.parseInt(br.readLine().trim());\n"
            "        int k = Integer.parseInt(br.readLine().trim());\n"
            "        Set<Long> apple = new HashSet<>();\n"
            "        for (int i = 0; i < k; i++) {\n"
            "            StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "            int r = Integer.parseInt(st.nextToken()), c = Integer.parseInt(st.nextToken());\n"
            "            apple.add((long) r * 1000 + c);\n"
            "        }\n"
            "        int l = Integer.parseInt(br.readLine().trim());\n"
            "        int[] mt = new int[l]; char[] mc = new char[l];\n"
            "        for (int i = 0; i < l; i++) {\n"
            "            StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "            mt[i] = Integer.parseInt(st.nextToken()); mc[i] = st.nextToken().charAt(0);\n"
            "        }\n"
            "        int[] dr = {0, 1, 0, -1}, dc = {1, 0, -1, 0};\n"
            "        int d = 0;\n"
            "        Deque<int[]> snake = new ArrayDeque<>();\n"
            "        snake.addFirst(new int[]{1, 1});\n"
            "        Set<Long> body = new HashSet<>();\n"
            "        body.add(1001L);\n"
            "        int time = 0, mi = 0;\n"
            "        while (true) {\n"
            "            time++;\n"
            "            int[] head = snake.peekFirst();\n"
            "            int nr = head[0] + dr[d], nc = head[1] + dc[d];\n"
            "            long key = (long) nr * 1000 + nc;\n"
            "            if (nr < 1 || nr > n || nc < 1 || nc > n || body.contains(key)) break;\n"
            "            snake.addFirst(new int[]{nr, nc});\n"
            "            body.add(key);\n"
            "            if (apple.contains(key)) apple.remove(key);\n"
            "            else { int[] t = snake.pollLast(); body.remove((long) t[0] * 1000 + t[1]); }\n"
            "            if (mi < l && mt[mi] == time) {\n"
            "                d = mc[mi] == 'D' ? (d + 1) % 4 : (d + 3) % 4;\n"
            "                mi++;\n"
            "            }\n"
            "        }\n"
            "        System.out.println(time);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "from collections import deque\n"
            "input = sys.stdin.readline\n"
            "# 뱀 게임 시뮬레이션\n"
            "def main():\n"
            "    n = int(input())\n"
            "    # ...\n"
            "main()\n"
        ),
    ),

    Problem(
        id="gold-47",
        rank="Gold",
        title="최소 비용 경로",
        style="백준",
        topic="다익스트라",
        type="stdin",
        description=(
            "N개의 도시와 도시 사이를 잇는 단방향 버스 노선이 주어진다. 각 노선은 비용을 "
            "가진다. 출발 도시 S에서 도착 도시 E까지 가는 데 드는 최소 비용을 구하세요. "
            "S에서 E로 가는 경로는 항상 존재한다."
        ),
        input_desc=(
            "첫째 줄 도시 수 N. 둘째 줄 노선 수 M. 이어 M개의 줄에 'u v w' "
            "(도시 u에서 v로 가는 비용 w의 단방향 노선). 마지막 줄에 출발 도시 S와 "
            "도착 도시 E. 도시 번호는 1부터 N까지이다."
        ),
        output_desc="S에서 E까지의 최소 비용.",
        examples=[
            {"input": "5\n6\n1 2 2\n1 3 3\n2 3 4\n2 4 5\n3 4 6\n4 5 1\n1 5\n", "output": "8\n"},
            {"input": "3\n3\n1 2 5\n2 3 2\n1 3 10\n1 3\n", "output": "7\n"},
        ],
        hints=[
            "단일 출발점에서 가중치가 양수인 그래프의 최단 비용 문제입니다. 가까운 정점부터 확정하면 됩니다.",
            "우선순위 큐를 사용하는 다익스트라로 S에서 모든 정점까지 최소 비용을 구한 뒤 E의 값을 출력하세요.",
            "dist[S]=0; 힙에서 (d,u) 꺼내 d>dist[u]면 skip; 인접 v에 d+w<dist[v]면 갱신·push; 답은 dist[E].",
        ],
        testcases=[
            {"input": "5\n6\n1 2 2\n1 3 3\n2 3 4\n2 4 5\n3 4 6\n4 5 1\n1 5\n", "output": "8\n"},
            {"input": "3\n3\n1 2 5\n2 3 2\n1 3 10\n1 3\n", "output": "7\n"},
            {"input": "2\n1\n1 2 7\n1 2\n", "output": "7\n"},
            {"input": "4\n4\n1 2 1\n2 3 1\n3 4 1\n1 4 100\n1 4\n", "output": "3\n"},
        ],
        reference_py=(
            "import sys, heapq\n"
            "input = sys.stdin.readline\n"
            "def main():\n"
            "    n = int(input())\n"
            "    m = int(input())\n"
            "    graph = [[] for _ in range(n + 1)]\n"
            "    for _ in range(m):\n"
            "        u, v, w = map(int, input().split())\n"
            "        graph[u].append((v, w))\n"
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
            "    print(dist[e])\n"
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
            "        List<int[]>[] g = new List[n + 1];\n"
            "        for (int i = 0; i <= n; i++) g[i] = new ArrayList<>();\n"
            "        for (int i = 0; i < m; i++) {\n"
            "            StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "            int u = Integer.parseInt(st.nextToken());\n"
            "            int v = Integer.parseInt(st.nextToken());\n"
            "            int w = Integer.parseInt(st.nextToken());\n"
            "            g[u].add(new int[]{v, w});\n"
            "        }\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int s = Integer.parseInt(st.nextToken()), e = Integer.parseInt(st.nextToken());\n"
            "        long INF = Long.MAX_VALUE / 4;\n"
            "        long[] dist = new long[n + 1];\n"
            "        Arrays.fill(dist, INF);\n"
            "        dist[s] = 0;\n"
            "        PriorityQueue<long[]> pq = new PriorityQueue<>((a, b) -> Long.compare(a[0], b[0]));\n"
            "        pq.add(new long[]{0, s});\n"
            "        while (!pq.isEmpty()) {\n"
            "            long[] c = pq.poll();\n"
            "            long d = c[0]; int u = (int) c[1];\n"
            "            if (d > dist[u]) continue;\n"
            "            for (int[] ed : g[u]) {\n"
            "                long nd = d + ed[1];\n"
            "                if (nd < dist[ed[0]]) { dist[ed[0]] = nd; pq.add(new long[]{nd, ed[0]}); }\n"
            "            }\n"
            "        }\n"
            "        System.out.println(dist[e]);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys, heapq\n"
            "input = sys.stdin.readline\n"
            "# 최소 비용 경로 (다익스트라)\n"
            "def main():\n"
            "    n = int(input())\n"
            "    m = int(input())\n"
            "    # ...\n"
            "main()\n"
        ),
    ),

    Problem(
        id="gold-48",
        rank="Gold",
        title="외판원 순회 최소 비용",
        style="해외대기업",
        topic="비트마스크",
        type="func",
        func_name="solution",
        description=(
            "도시가 0번부터 n-1번까지 있고, dist[i][j]는 도시 i에서 j로 가는 비용이다. "
            "dist[i][j]가 0이면 i에서 j로 가는 길이 없음을 뜻한다(i=j인 대각선 제외). "
            "한 도시에서 출발해 모든 도시를 정확히 한 번씩 방문하고 출발 도시로 돌아오는 "
            "순회의 최소 비용을 반환하세요. 유효한 순회가 없으면 -1을 반환합니다. "
            "도시 수 n은 12 이하입니다."
        ),
        input_desc="dist : n×n 비용 행렬(0은 길 없음을 의미)",
        output_desc="모든 도시를 한 번씩 방문하고 돌아오는 최소 비용(없으면 -1)",
        examples=[
            {"args": [[[0, 10, 15, 20], [5, 0, 9, 10], [6, 13, 0, 12], [8, 8, 9, 0]]], "output": 35},
            {"args": [[[0, 1, 1], [1, 0, 1], [1, 1, 0]]], "output": 3},
        ],
        hints=[
            "어떤 도시들을 이미 방문했는지를 비트마스크로 표현하면 상태 수가 2^n으로 줄어듭니다.",
            "비트마스크 DP를 사용하세요. dp[visited][last] = visited 집합을 방문하고 현재 last에 있을 때의 최소 비용.",
            "dp[1<<0][0]=0; 전이 dp[mask|1<<v][v]=min(..., dp[mask][u]+dist[u][v]); 답은 min(dp[full][u]+dist[u][0]).",
        ],
        testcases=[
            {"args": [[[0, 10, 15, 20], [5, 0, 9, 10], [6, 13, 0, 12], [8, 8, 9, 0]]], "expected": 35},
            {"args": [[[0, 1, 1], [1, 0, 1], [1, 1, 0]]], "expected": 3},
            {"args": [[[0, 5], [5, 0]]], "expected": 10},
            {"args": [[[0, 1, 10, 10], [10, 0, 1, 10], [10, 10, 0, 1], [1, 10, 10, 0]]], "expected": 4},
            {"args": [[[0, 0], [5, 0]]], "expected": -1},
        ],
        reference_py=(
            "def solution(dist):\n"
            "    n = len(dist)\n"
            "    INF = float('inf')\n"
            "    dp = [[INF] * n for _ in range(1 << n)]\n"
            "    dp[1][0] = 0\n"
            "    for mask in range(1 << n):\n"
            "        for u in range(n):\n"
            "            if dp[mask][u] == INF:\n"
            "                continue\n"
            "            if not mask >> u & 1:\n"
            "                continue\n"
            "            for v in range(n):\n"
            "                if mask >> v & 1:\n"
            "                    continue\n"
            "                if dist[u][v] == 0:\n"
            "                    continue\n"
            "                nm = mask | 1 << v\n"
            "                if dp[nm][v] > dp[mask][u] + dist[u][v]:\n"
            "                    dp[nm][v] = dp[mask][u] + dist[u][v]\n"
            "    full = (1 << n) - 1\n"
            "    ans = INF\n"
            "    for u in range(n):\n"
            "        if dist[u][0] == 0:\n"
            "            continue\n"
            "        if dp[full][u] + dist[u][0] < ans:\n"
            "            ans = dp[full][u] + dist[u][0]\n"
            "    return ans if ans != INF else -1\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int[][] dist) {\n"
            "        int n = dist.length;\n"
            "        final int INF = Integer.MAX_VALUE / 4;\n"
            "        int[][] dp = new int[1 << n][n];\n"
            "        for (int[] r : dp) java.util.Arrays.fill(r, INF);\n"
            "        dp[1][0] = 0;\n"
            "        for (int mask = 0; mask < (1 << n); mask++) {\n"
            "            for (int u = 0; u < n; u++) {\n"
            "                if (dp[mask][u] == INF || (mask >> u & 1) == 0) continue;\n"
            "                for (int v = 0; v < n; v++) {\n"
            "                    if ((mask >> v & 1) == 1 || dist[u][v] == 0) continue;\n"
            "                    int nm = mask | (1 << v);\n"
            "                    if (dp[nm][v] > dp[mask][u] + dist[u][v]) dp[nm][v] = dp[mask][u] + dist[u][v];\n"
            "                }\n"
            "            }\n"
            "        }\n"
            "        int full = (1 << n) - 1, ans = INF;\n"
            "        for (int u = 0; u < n; u++) {\n"
            "            if (dist[u][0] == 0) continue;\n"
            "            ans = Math.min(ans, dp[full][u] + dist[u][0]);\n"
            "        }\n"
            "        return ans == INF ? -1 : ans;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 외판원 순회 최소 비용 (비트마스크 DP)\n"
            "def solution(dist):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="gold-49",
        rank="Gold",
        title="카드 합치기 최소 비용",
        style="대기업",
        topic="그리디",
        type="func",
        func_name="solution",
        description=(
            "여러 묶음의 카드가 있고 각 묶음의 카드 수가 cards에 주어진다. 두 묶음을 "
            "합칠 때는 두 묶음의 카드 수의 합만큼 비교가 필요해 그만큼의 비용이 든다. "
            "모든 묶음을 하나로 합칠 때 드는 비용의 최솟값을 반환하세요."
        ),
        input_desc="cards : 각 묶음의 카드 수를 담은 정수 리스트",
        output_desc="모든 묶음을 하나로 합치는 최소 비용",
        examples=[
            {"args": [[10, 20, 40]], "output": 100},
            {"args": [[10, 20, 30, 40]], "output": 190},
        ],
        hints=[
            "한 번 합쳐진 묶음은 이후 합칠 때마다 비용에 다시 더해집니다. 작은 묶음을 먼저 합칠수록 유리합니다.",
            "최소 힙(우선순위 큐)을 사용해 항상 가장 작은 두 묶음을 꺼내 합치고 다시 넣으세요.",
            "heapify(cards); while len>1: a=pop,b=pop; s=a+b; total+=s; push(s). 답은 total.",
        ],
        testcases=[
            {"args": [[10, 20, 40]], "expected": 100},
            {"args": [[10, 20, 30, 40]], "expected": 190},
            {"args": [[5]], "expected": 0},
            {"args": [[1, 1, 1, 1]], "expected": 8},
            {"args": [[1, 2, 3, 4, 5]], "expected": 33},
        ],
        reference_py=(
            "import heapq\n"
            "def solution(cards):\n"
            "    if len(cards) <= 1:\n"
            "        return 0\n"
            "    h = list(cards)\n"
            "    heapq.heapify(h)\n"
            "    total = 0\n"
            "    while len(h) > 1:\n"
            "        a = heapq.heappop(h)\n"
            "        b = heapq.heappop(h)\n"
            "        s = a + b\n"
            "        total += s\n"
            "        heapq.heappush(h, s)\n"
            "    return total\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public long solution(int[] cards) {\n"
            "        if (cards.length <= 1) return 0;\n"
            "        PriorityQueue<Long> pq = new PriorityQueue<>();\n"
            "        for (int c : cards) pq.add((long) c);\n"
            "        long total = 0;\n"
            "        while (pq.size() > 1) {\n"
            "            long s = pq.poll() + pq.poll();\n"
            "            total += s;\n"
            "            pq.add(s);\n"
            "        }\n"
            "        return total;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 카드 합치기 최소 비용 (그리디 + 최소 힙)\n"
            "def solution(cards):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="gold-50",
        rank="Gold",
        title="요세푸스 순열",
        style="백준",
        topic="시뮬레이션",
        type="stdin",
        description=(
            "1번부터 N번까지 N명이 원을 이루어 앉아 있다. 양의 정수 K에 대해, 순서대로 "
            "K번째 사람을 원에서 제거한다. 제거된 사람 다음부터 다시 세어 K번째 사람을 "
            "제거하는 과정을 모두가 제거될 때까지 반복한다. 제거되는 순서를 나열한 "
            "(N, K)-요세푸스 순열을 구하세요."
        ),
        input_desc="첫째 줄에 N과 K가 공백으로 구분되어 주어진다.",
        output_desc="요세푸스 순열을 '<a, b, ...>' 형식으로 한 줄에 출력.",
        examples=[
            {"input": "7 3\n", "output": "<3, 6, 2, 7, 5, 1, 4>\n"},
            {"input": "5 2\n", "output": "<2, 4, 1, 5, 3>\n"},
        ],
        hints=[
            "원을 도는 과정을 그대로 흉내 내면 됩니다. 제거 위치를 매번 K칸 전진한 지점으로 계산하세요.",
            "덱(또는 리스트)으로 시뮬레이션하거나, 현재 인덱스를 (idx+K-1) % 남은인원 으로 갱신하며 제거합니다.",
            "idx=0; while 남으면: idx=(idx+K-1)%len; res.append(제거값); del dq[idx]. 마지막에 '<'+', '.join+'>'.",
        ],
        testcases=[
            {"input": "7 3\n", "output": "<3, 6, 2, 7, 5, 1, 4>\n"},
            {"input": "5 2\n", "output": "<2, 4, 1, 5, 3>\n"},
            {"input": "1 1\n", "output": "<1>\n"},
            {"input": "10 1\n", "output": "<1, 2, 3, 4, 5, 6, 7, 8, 9, 10>\n"},
        ],
        reference_py=(
            "import sys\n"
            "from collections import deque\n"
            "input = sys.stdin.readline\n"
            "def main():\n"
            "    n, k = map(int, input().split())\n"
            "    dq = deque(range(1, n + 1))\n"
            "    res = []\n"
            "    idx = 0\n"
            "    while dq:\n"
            "        idx = (idx + k - 1) % len(dq)\n"
            "        res.append(str(dq[idx]))\n"
            "        del dq[idx]\n"
            "    print('<' + ', '.join(res) + '>')\n"
            "main()\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int n = Integer.parseInt(st.nextToken()), k = Integer.parseInt(st.nextToken());\n"
            "        List<Integer> list = new ArrayList<>();\n"
            "        for (int i = 1; i <= n; i++) list.add(i);\n"
            "        StringBuilder sb = new StringBuilder(\"<\");\n"
            "        int idx = 0;\n"
            "        while (!list.isEmpty()) {\n"
            "            idx = (idx + k - 1) % list.size();\n"
            "            sb.append(list.remove(idx));\n"
            "            if (!list.isEmpty()) sb.append(\", \");\n"
            "        }\n"
            "        sb.append('>');\n"
            "        System.out.println(sb);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "from collections import deque\n"
            "input = sys.stdin.readline\n"
            "# 요세푸스 순열\n"
            "def main():\n"
            "    n, k = map(int, input().split())\n"
            "    # ...\n"
            "main()\n"
        ),
    ),

]
