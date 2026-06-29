"""그래프 유형 묶음 — 같은 유형을 난이도별로 여러 랭크에 배치 (gg-01 ~ gg-12).

멀티소스 BFS(S/G), 위상정렬(S/G), 다익스트라(S/G), 플로이드-워셜(G),
유니온파인드(S/G), DFS·연결요소(S), 0-1 BFS(G), 백트래킹 경로(G) 총 12문제.
모든 문제의 정답 출력은 유일하게 결정되도록 설계했다.
"""

from engine.models import Problem

PROBLEMS = [

    # ────────────────────────── 멀티소스 BFS ──────────────────────────

    Problem(
        id="gg-01",
        rank="Silver",
        tier="S1",
        category="DFS/BFS",
        title="토마토 상자 익히기",
        style="백준",
        topic="멀티소스 BFS",
        type="stdin",
        description=(
            "R행 C열 격자 상자에 토마토가 들어 있다. 각 칸의 값이 1이면 익은 토마토, 0이면 "
            "안 익은 토마토다(빈 칸은 없다). 익은 토마토는 하루가 지나면 인접한 상하좌우 칸의 "
            "안 익은 토마토를 익게 만든다. 모든 토마토가 익을 때까지 걸리는 최소 일수를 구하시오. "
            "처음부터 모두 익어 있으면 0을 출력한다. (적어도 한 칸은 익은 토마토다.)"
        ),
        input_desc=(
            "첫째 줄에 행 수 R과 열 수 C (1 ≤ R, C ≤ 1000). 다음 R개의 줄에 각 줄마다 "
            "C개의 정수(0 또는 1)가 공백으로 주어진다."
        ),
        output_desc="모든 토마토가 익을 때까지 걸리는 최소 일수.",
        examples=[
            {"input": "3 3\n0 0 0\n0 1 0\n0 0 0\n", "output": "2\n"},
            {"input": "1 4\n1 0 0 0\n", "output": "3\n"},
        ],
        hints=[
            "한 칸씩 동시에 퍼져 나가는 과정이므로, 익은 토마토 전부를 동시에 출발점으로 삼는 너비 우선 탐색을 생각하세요.",
            "멀티소스 BFS: 처음 익은 토마토를 모두 큐에 넣고 거리(=날짜)를 0으로 둔 뒤, 인접 칸으로 +1씩 퍼뜨립니다. 답은 최대 거리값.",
            "dist 배열을 -1로 초기화하고 익은 칸은 0으로 두어 큐에 넣은 뒤 BFS, 갱신할 때마다 ans=max(ans, dist[nx][ny]). 마지막에 ans 출력.",
        ],
        testcases=[
            {"input": "3 3\n0 0 0\n0 1 0\n0 0 0\n", "output": "2\n"},
            {"input": "1 4\n1 0 0 0\n", "output": "3\n"},
            {"input": "2 2\n1 1\n1 1\n", "output": "0\n"},
            {"input": "1 1\n1\n", "output": "0\n"},
            {"input": "2 3\n1 0 0\n0 0 1\n", "output": "1\n"},
        ],
        reference_py=(
            "import sys\n"
            "from collections import deque\n"
            "input = sys.stdin.readline\n"
            "r, c = map(int, input().split())\n"
            "g = [list(map(int, input().split())) for _ in range(r)]\n"
            "dist = [[-1] * c for _ in range(r)]\n"
            "q = deque()\n"
            "for i in range(r):\n"
            "    for j in range(c):\n"
            "        if g[i][j] == 1:\n"
            "            dist[i][j] = 0\n"
            "            q.append((i, j))\n"
            "ans = 0\n"
            "while q:\n"
            "    x, y = q.popleft()\n"
            "    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):\n"
            "        nx, ny = x + dx, y + dy\n"
            "        if 0 <= nx < r and 0 <= ny < c and dist[nx][ny] == -1:\n"
            "            dist[nx][ny] = dist[x][y] + 1\n"
            "            if dist[nx][ny] > ans:\n"
            "                ans = dist[nx][ny]\n"
            "            q.append((nx, ny))\n"
            "print(ans)\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int r = Integer.parseInt(st.nextToken()), c = Integer.parseInt(st.nextToken());\n"
            "        int[][] g = new int[r][c];\n"
            "        int[][] dist = new int[r][c];\n"
            "        ArrayDeque<int[]> q = new ArrayDeque<>();\n"
            "        for (int i = 0; i < r; i++) {\n"
            "            st = new StringTokenizer(br.readLine());\n"
            "            for (int j = 0; j < c; j++) {\n"
            "                g[i][j] = Integer.parseInt(st.nextToken());\n"
            "                dist[i][j] = -1;\n"
            "                if (g[i][j] == 1) { dist[i][j] = 0; q.add(new int[]{i, j}); }\n"
            "            }\n"
            "        }\n"
            "        int ans = 0;\n"
            "        int[] dx = {1,-1,0,0}, dy = {0,0,1,-1};\n"
            "        while (!q.isEmpty()) {\n"
            "            int[] cur = q.poll();\n"
            "            for (int d = 0; d < 4; d++) {\n"
            "                int nx = cur[0]+dx[d], ny = cur[1]+dy[d];\n"
            "                if (nx>=0&&nx<r&&ny>=0&&ny<c&&dist[nx][ny]==-1) {\n"
            "                    dist[nx][ny] = dist[cur[0]][cur[1]] + 1;\n"
            "                    ans = Math.max(ans, dist[nx][ny]);\n"
            "                    q.add(new int[]{nx, ny});\n"
            "                }\n"
            "            }\n"
            "        }\n"
            "        System.out.println(ans);\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp="",
        template_py=(
            "import sys\n"
            "from collections import deque\n"
            "input = sys.stdin.readline\n"
            "# 토마토 상자 : 모두 익는 최소 일수 (멀티소스 BFS)\n"
            "r, c = map(int, input().split())\n"
            "# ...\n"
        ),
    ),

    Problem(
        id="gg-02",
        rank="Gold",
        tier="G5",
        category="DFS/BFS",
        title="토마토 창고 익히기",
        style="삼성",
        topic="멀티소스 BFS",
        type="stdin",
        description=(
            "R행 C열 창고 격자에 토마토가 칸마다 놓여 있다. 각 칸의 값은 1(익은 토마토), "
            "0(안 익은 토마토), -1(토마토가 없는 빈 칸) 중 하나다. 익은 토마토는 하루가 지나면 "
            "인접한 상하좌우의 안 익은 토마토를 익힌다. 빈 칸(-1)으로는 익음이 전파되지 않는다. "
            "모든 토마토가 익을 때까지의 최소 일수를 구하시오. 처음부터 모두 익어 있으면 0을, "
            "끝내 익지 못하는 토마토가 있으면 -1을 출력한다."
        ),
        input_desc=(
            "첫째 줄에 행 수 R과 열 수 C (1 ≤ R, C ≤ 1000). 다음 R개의 줄에 각 줄마다 "
            "C개의 정수(-1, 0, 1)가 공백으로 주어진다."
        ),
        output_desc="모든 토마토가 익는 최소 일수. 모두 익어 있으면 0, 불가능하면 -1.",
        examples=[
            {"input": "2 3\n0 0 0\n0 0 1\n", "output": "3\n"},
            {"input": "1 3\n1 -1 0\n", "output": "-1\n"},
        ],
        hints=[
            "익은 토마토가 여럿이므로 그것들을 동시에 출발점으로 두는 너비 우선 탐색이 자연스럽습니다. 빈 칸(-1)은 통과 불가입니다.",
            "멀티소스 BFS로 거리를 채운 뒤, 안 익은 토마토(0)인데 방문하지 못한 칸이 하나라도 있으면 -1을 답으로 합니다.",
            "dist를 -1로 두고 익은 칸만 0으로 큐에 넣어 g[nx][ny]==0 인 칸으로만 전파. 끝나고 0인데 dist==-1이면 실패, 아니면 최대 dist 출력.",
        ],
        testcases=[
            {"input": "2 3\n0 0 0\n0 0 1\n", "output": "3\n"},
            {"input": "1 3\n1 -1 0\n", "output": "-1\n"},
            {"input": "1 1\n1\n", "output": "0\n"},
            {"input": "1 1\n0\n", "output": "-1\n"},
            {"input": "2 2\n1 -1\n-1 0\n", "output": "-1\n"},
            {"input": "2 3\n1 1 1\n1 1 1\n", "output": "0\n"},
        ],
        reference_py=(
            "import sys\n"
            "from collections import deque\n"
            "input = sys.stdin.readline\n"
            "r, c = map(int, input().split())\n"
            "g = [list(map(int, input().split())) for _ in range(r)]\n"
            "dist = [[-1] * c for _ in range(r)]\n"
            "q = deque()\n"
            "for i in range(r):\n"
            "    for j in range(c):\n"
            "        if g[i][j] == 1:\n"
            "            dist[i][j] = 0\n"
            "            q.append((i, j))\n"
            "while q:\n"
            "    x, y = q.popleft()\n"
            "    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):\n"
            "        nx, ny = x + dx, y + dy\n"
            "        if 0 <= nx < r and 0 <= ny < c and g[nx][ny] == 0 and dist[nx][ny] == -1:\n"
            "            dist[nx][ny] = dist[x][y] + 1\n"
            "            q.append((nx, ny))\n"
            "ans = 0\n"
            "for i in range(r):\n"
            "    for j in range(c):\n"
            "        if g[i][j] == 0 and dist[i][j] == -1:\n"
            "            print(-1)\n"
            "            sys.exit(0)\n"
            "        if dist[i][j] > ans:\n"
            "            ans = dist[i][j]\n"
            "print(ans)\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int r = Integer.parseInt(st.nextToken()), c = Integer.parseInt(st.nextToken());\n"
            "        int[][] g = new int[r][c];\n"
            "        int[][] dist = new int[r][c];\n"
            "        ArrayDeque<int[]> q = new ArrayDeque<>();\n"
            "        for (int i = 0; i < r; i++) {\n"
            "            st = new StringTokenizer(br.readLine());\n"
            "            for (int j = 0; j < c; j++) {\n"
            "                g[i][j] = Integer.parseInt(st.nextToken());\n"
            "                dist[i][j] = -1;\n"
            "                if (g[i][j] == 1) { dist[i][j] = 0; q.add(new int[]{i, j}); }\n"
            "            }\n"
            "        }\n"
            "        int[] dx = {1,-1,0,0}, dy = {0,0,1,-1};\n"
            "        while (!q.isEmpty()) {\n"
            "            int[] cur = q.poll();\n"
            "            for (int d = 0; d < 4; d++) {\n"
            "                int nx = cur[0]+dx[d], ny = cur[1]+dy[d];\n"
            "                if (nx>=0&&nx<r&&ny>=0&&ny<c&&g[nx][ny]==0&&dist[nx][ny]==-1) {\n"
            "                    dist[nx][ny] = dist[cur[0]][cur[1]] + 1;\n"
            "                    q.add(new int[]{nx, ny});\n"
            "                }\n"
            "            }\n"
            "        }\n"
            "        int ans = 0;\n"
            "        for (int i = 0; i < r; i++)\n"
            "            for (int j = 0; j < c; j++) {\n"
            "                if (g[i][j] == 0 && dist[i][j] == -1) { System.out.println(-1); return; }\n"
            "                ans = Math.max(ans, dist[i][j]);\n"
            "            }\n"
            "        System.out.println(ans);\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp="",
        template_py=(
            "import sys\n"
            "from collections import deque\n"
            "input = sys.stdin.readline\n"
            "# 토마토 창고 : 최소 일수, 불가능하면 -1 (멀티소스 BFS)\n"
            "r, c = map(int, input().split())\n"
            "# ...\n"
        ),
    ),

    # ────────────────────────── 위상정렬 ──────────────────────────

    Problem(
        id="gg-03",
        rank="Silver",
        tier="S2",
        category="위상정렬",
        title="문제 풀이 순서 정하기",
        style="백준",
        topic="위상정렬",
        type="stdin",
        description=(
            "1번부터 N번까지 번호가 매겨진 문제가 있다. 'A를 풀어야 B를 풀 수 있다'는 선행 관계가 "
            "M개 주어진다. 모든 선행 관계를 지키면서 문제를 푸는 순서를 정하되, 여러 순서가 가능하면 "
            "되도록 번호가 작은 문제를 먼저 푸는 순서를 출력하시오. (선행 관계에 모순은 없다.)"
        ),
        input_desc=(
            "첫째 줄에 문제 수 N과 선행 관계 수 M (1 ≤ N ≤ 32000, 0 ≤ M ≤ 100000). "
            "다음 M개의 줄에 'A B' 형식으로, A를 푼 뒤에 B를 풀 수 있음을 뜻한다."
        ),
        output_desc="문제를 푸는 순서를 공백으로 구분해 한 줄에 출력한다.",
        examples=[
            {"input": "4 2\n4 2\n3 1\n", "output": "3 1 4 2\n"},
            {"input": "3 0\n", "output": "1 2 3\n"},
        ],
        hints=[
            "선행 관계는 방향 그래프입니다. 아직 풀어야 할 선행 문제가 없는(진입 차수 0) 문제부터 차례로 골라 나가야 합니다.",
            "위상 정렬(칸 알고리즘)을 쓰되, '작은 번호 우선' 조건 때문에 큐 대신 최소 힙(우선순위 큐)을 사용합니다.",
            "진입 차수 0인 정점을 힙에 넣고, 가장 작은 번호를 꺼내 결과에 추가한 뒤 그 정점이 가리키는 노드의 진입 차수를 줄여 0이 되면 힙에 넣기를 반복.",
        ],
        testcases=[
            {"input": "4 2\n4 2\n3 1\n", "output": "3 1 4 2\n"},
            {"input": "3 0\n", "output": "1 2 3\n"},
            {"input": "2 1\n2 1\n", "output": "2 1\n"},
            {"input": "1 0\n", "output": "1\n"},
            {"input": "5 4\n1 2\n1 3\n2 4\n3 4\n", "output": "1 2 3 4 5\n"},
        ],
        reference_py=(
            "import sys, heapq\n"
            "input = sys.stdin.readline\n"
            "n, m = map(int, input().split())\n"
            "adj = [[] for _ in range(n + 1)]\n"
            "indeg = [0] * (n + 1)\n"
            "for _ in range(m):\n"
            "    a, b = map(int, input().split())\n"
            "    adj[a].append(b)\n"
            "    indeg[b] += 1\n"
            "h = [i for i in range(1, n + 1) if indeg[i] == 0]\n"
            "heapq.heapify(h)\n"
            "res = []\n"
            "while h:\n"
            "    x = heapq.heappop(h)\n"
            "    res.append(x)\n"
            "    for y in adj[x]:\n"
            "        indeg[y] -= 1\n"
            "        if indeg[y] == 0:\n"
            "            heapq.heappush(h, y)\n"
            "print(' '.join(map(str, res)))\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());\n"
            "        List<List<Integer>> adj = new ArrayList<>();\n"
            "        for (int i = 0; i <= n; i++) adj.add(new ArrayList<>());\n"
            "        int[] indeg = new int[n + 1];\n"
            "        for (int i = 0; i < m; i++) {\n"
            "            st = new StringTokenizer(br.readLine());\n"
            "            int a = Integer.parseInt(st.nextToken()), b = Integer.parseInt(st.nextToken());\n"
            "            adj.get(a).add(b);\n"
            "            indeg[b]++;\n"
            "        }\n"
            "        PriorityQueue<Integer> pq = new PriorityQueue<>();\n"
            "        for (int i = 1; i <= n; i++) if (indeg[i] == 0) pq.add(i);\n"
            "        StringBuilder sb = new StringBuilder();\n"
            "        while (!pq.isEmpty()) {\n"
            "            int x = pq.poll();\n"
            "            sb.append(x).append(' ');\n"
            "            for (int y : adj.get(x)) if (--indeg[y] == 0) pq.add(y);\n"
            "        }\n"
            "        System.out.println(sb.toString().trim());\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp="",
        template_py=(
            "import sys, heapq\n"
            "input = sys.stdin.readline\n"
            "# 문제 풀이 순서 : 작은 번호 우선 위상정렬\n"
            "n, m = map(int, input().split())\n"
            "# ...\n"
        ),
    ),

    Problem(
        id="gg-04",
        rank="Gold",
        tier="G3",
        category="위상정렬",
        title="건물 건설 완료 시간",
        style="백준",
        topic="위상정렬",
        type="stdin",
        description=(
            "1번부터 N번까지의 건물을 짓는다. 각 건물은 짓는 데 걸리는 시간이 있고, 먼저 완성해야 하는 "
            "선행 건물 목록이 있다. 선행 건물이 모두 완성된 직후 그 건물의 건설을 시작할 수 있으며, "
            "여러 건물은 동시에 지을 수 있다. 각 건물이 완성되는 가장 빠른 시각을 구하시오."
        ),
        input_desc=(
            "첫째 줄에 건물 수 N (1 ≤ N ≤ 100000). 이어서 N개의 줄에 i번 건물 정보가 주어지는데, "
            "각 줄은 '건설 시간'으로 시작해 그 건물의 선행 건물 번호들이 나오고 -1로 끝난다."
        ),
        output_desc="1번부터 N번 건물까지, 각 건물이 완성되는 가장 빠른 시각을 한 줄에 하나씩 출력한다.",
        examples=[
            {"input": "4\n5 -1\n3 1 -1\n2 1 -1\n4 2 3 -1\n", "output": "5\n8\n7\n12\n"},
            {"input": "1\n7 -1\n", "output": "7\n"},
        ],
        hints=[
            "건물의 완성 시각은 자신의 건설 시간에, 모든 선행 건물 중 가장 늦게 끝나는 시각을 더한 값입니다.",
            "위상 정렬 순서대로 처리하면서 DP를 합니다. 선행 관계가 없는 건물부터 시작해 완성 시각을 확정해 나갑니다.",
            "진입 차수 0인 건물부터 처리. done[i] = time[i] + (선행들의 완성 시각 최댓값). 어떤 건물을 완성하면 그 건물에 의존하는 건물의 시작 가능 시각을 갱신하고 진입 차수를 줄여 0이 되면 큐에 추가.",
        ],
        testcases=[
            {"input": "4\n5 -1\n3 1 -1\n2 1 -1\n4 2 3 -1\n", "output": "5\n8\n7\n12\n"},
            {"input": "1\n7 -1\n", "output": "7\n"},
            {"input": "3\n1 -1\n2 1 -1\n3 2 -1\n", "output": "1\n3\n6\n"},
            {"input": "3\n5 -1\n3 -1\n8 -1\n", "output": "5\n3\n8\n"},
            {"input": "4\n2 -1\n3 1 -1\n5 1 -1\n1 2 3 -1\n", "output": "2\n5\n7\n8\n"},
        ],
        reference_py=(
            "import sys\n"
            "from collections import deque\n"
            "input = sys.stdin.readline\n"
            "n = int(input())\n"
            "time = [0] * (n + 1)\n"
            "adj = [[] for _ in range(n + 1)]\n"
            "indeg = [0] * (n + 1)\n"
            "for i in range(1, n + 1):\n"
            "    data = list(map(int, input().split()))\n"
            "    time[i] = data[0]\n"
            "    for p in data[1:-1]:\n"
            "        adj[p].append(i)\n"
            "        indeg[i] += 1\n"
            "dp = [0] * (n + 1)\n"
            "res = [0] * (n + 1)\n"
            "q = deque(i for i in range(1, n + 1) if indeg[i] == 0)\n"
            "while q:\n"
            "    x = q.popleft()\n"
            "    res[x] = dp[x] + time[x]\n"
            "    for y in adj[x]:\n"
            "        if res[x] > dp[y]:\n"
            "            dp[y] = res[x]\n"
            "        indeg[y] -= 1\n"
            "        if indeg[y] == 0:\n"
            "            q.append(y)\n"
            "print('\\n'.join(str(res[i]) for i in range(1, n + 1)))\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        int n = Integer.parseInt(br.readLine().trim());\n"
            "        int[] time = new int[n + 1];\n"
            "        List<List<Integer>> adj = new ArrayList<>();\n"
            "        for (int i = 0; i <= n; i++) adj.add(new ArrayList<>());\n"
            "        int[] indeg = new int[n + 1];\n"
            "        for (int i = 1; i <= n; i++) {\n"
            "            StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "            time[i] = Integer.parseInt(st.nextToken());\n"
            "            int v;\n"
            "            while ((v = Integer.parseInt(st.nextToken())) != -1) {\n"
            "                adj.get(v).add(i);\n"
            "                indeg[i]++;\n"
            "            }\n"
            "        }\n"
            "        int[] dp = new int[n + 1];\n"
            "        int[] res = new int[n + 1];\n"
            "        ArrayDeque<Integer> q = new ArrayDeque<>();\n"
            "        for (int i = 1; i <= n; i++) if (indeg[i] == 0) q.add(i);\n"
            "        while (!q.isEmpty()) {\n"
            "            int x = q.poll();\n"
            "            res[x] = dp[x] + time[x];\n"
            "            for (int y : adj.get(x)) {\n"
            "                if (res[x] > dp[y]) dp[y] = res[x];\n"
            "                if (--indeg[y] == 0) q.add(y);\n"
            "            }\n"
            "        }\n"
            "        StringBuilder sb = new StringBuilder();\n"
            "        for (int i = 1; i <= n; i++) sb.append(res[i]).append('\\n');\n"
            "        System.out.print(sb);\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp="",
        template_py=(
            "import sys\n"
            "from collections import deque\n"
            "input = sys.stdin.readline\n"
            "# 건물 건설 완료 시간 : 위상정렬 + DP\n"
            "n = int(input())\n"
            "# ...\n"
        ),
    ),

    # ────────────────────────── 다익스트라 / 최단경로 ──────────────────────────

    Problem(
        id="gg-05",
        rank="Silver",
        tier="S1",
        category="최단경로",
        title="작은 도시 최단 거리",
        style="프로그래머스",
        topic="다익스트라",
        type="func",
        func_name="solution",
        description=(
            "정점이 0번부터 n-1번까지 있는 방향 그래프가 있다. edges의 각 원소 [u, v, w]는 "
            "u에서 v로 가는 가중치 w(양의 정수)인 간선을 뜻한다. 시작 정점 start에서 각 정점까지의 "
            "최단 거리를 담은 리스트를 반환하세요. 시작 정점의 거리는 0이며, 도달할 수 없는 정점은 "
            "-1로 표시합니다. 반환 리스트의 i번째 원소는 정점 i까지의 최단 거리입니다."
        ),
        input_desc=(
            "n : 정점 수(int), edges : [u, v, w] 형태의 방향 간선 리스트, start : 시작 정점 번호(int)"
        ),
        output_desc="길이 n의 리스트. i번째 값은 start에서 정점 i까지의 최단 거리(도달 불가 시 -1).",
        examples=[
            {"args": [4, [[0, 1, 1], [0, 2, 4], [1, 2, 2], [2, 3, 1]], 0], "output": [0, 1, 3, 4]},
            {"args": [3, [[0, 1, 5]], 0], "output": [0, 5, -1]},
        ],
        hints=[
            "간선 가중치가 양수이므로, 가장 가까운 정점부터 거리를 확정해 나가는 방식이 잘 맞습니다.",
            "다익스트라 알고리즘을 쓰세요. (거리, 정점) 쌍을 최소 힙에 넣고, 더 짧은 경로를 찾을 때마다 거리를 갱신합니다.",
            "dist를 무한대로 두고 dist[start]=0, 힙에 (0,start). pop한 거리가 기록된 거리보다 크면 무시. 인접 v에 대해 d+w<dist[v]면 갱신·push. 마지막에 무한대는 -1로 바꿔 반환.",
        ],
        testcases=[
            {"args": [4, [[0, 1, 1], [0, 2, 4], [1, 2, 2], [2, 3, 1]], 0], "expected": [0, 1, 3, 4]},
            {"args": [3, [[0, 1, 5]], 0], "expected": [0, 5, -1]},
            {"args": [1, [], 0], "expected": [0]},
            {"args": [3, [[2, 0, 3], [0, 1, 2]], 2], "expected": [3, 5, 0]},
            {"args": [4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 10]], 0], "expected": [0, 1, 2, 3]},
        ],
        reference_py=(
            "import heapq\n"
            "def solution(n, edges, start):\n"
            "    adj = [[] for _ in range(n)]\n"
            "    for u, v, w in edges:\n"
            "        adj[u].append((v, w))\n"
            "    INF = float('inf')\n"
            "    dist = [INF] * n\n"
            "    dist[start] = 0\n"
            "    pq = [(0, start)]\n"
            "    while pq:\n"
            "        d, u = heapq.heappop(pq)\n"
            "        if d > dist[u]:\n"
            "            continue\n"
            "        for v, w in adj[u]:\n"
            "            nd = d + w\n"
            "            if nd < dist[v]:\n"
            "                dist[v] = nd\n"
            "                heapq.heappush(pq, (nd, v))\n"
            "    return [d if d != INF else -1 for d in dist]\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int[] solution(int n, int[][] edges, int start) {\n"
            "        List<int[]>[] adj = new List[n];\n"
            "        for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();\n"
            "        for (int[] e : edges) adj[e[0]].add(new int[]{e[1], e[2]});\n"
            "        long INF = Long.MAX_VALUE / 4;\n"
            "        long[] dist = new long[n];\n"
            "        Arrays.fill(dist, INF);\n"
            "        dist[start] = 0;\n"
            "        PriorityQueue<long[]> pq = new PriorityQueue<>((a, b) -> Long.compare(a[0], b[0]));\n"
            "        pq.add(new long[]{0, start});\n"
            "        while (!pq.isEmpty()) {\n"
            "            long[] cur = pq.poll();\n"
            "            long d = cur[0]; int u = (int) cur[1];\n"
            "            if (d > dist[u]) continue;\n"
            "            for (int[] e : adj[u]) {\n"
            "                long nd = d + e[1];\n"
            "                if (nd < dist[e[0]]) { dist[e[0]] = nd; pq.add(new long[]{nd, e[0]}); }\n"
            "            }\n"
            "        }\n"
            "        int[] res = new int[n];\n"
            "        for (int i = 0; i < n; i++) res[i] = (dist[i] == INF) ? -1 : (int) dist[i];\n"
            "        return res;\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp="",
        template_py=(
            "import heapq\n"
            "# 작은 도시 최단 거리 : 다익스트라, 도달 불가는 -1\n"
            "def solution(n, edges, start):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="gg-06",
        rank="Gold",
        tier="G5",
        category="최단경로",
        title="최단 경로 거리 출력",
        style="백준",
        topic="다익스트라",
        type="stdin",
        description=(
            "정점 V개, 간선 E개로 이루어진 방향 그래프가 있다. 모든 간선의 가중치는 양수다. "
            "시작 정점 K에서 다른 모든 정점까지의 최단 경로 거리를 구하시오. 시작 정점 자신까지의 "
            "거리는 0이며, 경로가 존재하지 않으면 INF를 출력한다."
        ),
        input_desc=(
            "첫째 줄에 정점 수 V와 간선 수 E (1 ≤ V ≤ 20000, 0 ≤ E ≤ 300000). 둘째 줄에 시작 정점 "
            "번호 K. 다음 E개의 줄에 'u v w' 형식으로 u에서 v로 가는 가중치 w(1 ≤ w ≤ 10)인 간선이 주어진다."
        ),
        output_desc="1번 정점부터 V번 정점까지 각 정점까지의 최단 거리를 한 줄에 하나씩 출력한다. 도달 불가면 INF.",
        examples=[
            {"input": "5 6\n1\n5 1 1\n1 2 2\n1 3 3\n2 3 4\n2 4 5\n3 4 6\n", "output": "0\n2\n3\n7\nINF\n"},
            {"input": "2 1\n1\n1 2 10\n", "output": "0\n10\n"},
        ],
        hints=[
            "가중치가 모두 양수인 단일 출발점 최단 경로 문제입니다. 가장 가까운 정점부터 거리를 확정해 나갑니다.",
            "다익스트라 알고리즘을 우선순위 큐(최소 힙)로 구현하세요. 간선 수가 많으므로 입력을 빠르게 읽어야 합니다.",
            "dist를 무한대로 초기화, dist[K]=0, 힙에 (0,K). pop한 거리가 dist보다 크면 스킵. 인접 정점에 대해 갱신·push. 출력 시 무한대는 'INF'로.",
        ],
        testcases=[
            {"input": "5 6\n1\n5 1 1\n1 2 2\n1 3 3\n2 3 4\n2 4 5\n3 4 6\n", "output": "0\n2\n3\n7\nINF\n"},
            {"input": "1 0\n1\n", "output": "0\n"},
            {"input": "2 1\n1\n1 2 10\n", "output": "0\n10\n"},
            {"input": "3 2\n2\n1 2 5\n2 3 1\n", "output": "INF\n0\n1\n"},
            {"input": "4 4\n1\n1 2 1\n1 3 5\n2 3 1\n3 4 2\n", "output": "0\n1\n2\n4\n"},
        ],
        reference_py=(
            "import sys, heapq\n"
            "input = sys.stdin.readline\n"
            "v, e = map(int, input().split())\n"
            "k = int(input())\n"
            "adj = [[] for _ in range(v + 1)]\n"
            "for _ in range(e):\n"
            "    a, b, w = map(int, input().split())\n"
            "    adj[a].append((b, w))\n"
            "INF = float('inf')\n"
            "dist = [INF] * (v + 1)\n"
            "dist[k] = 0\n"
            "pq = [(0, k)]\n"
            "while pq:\n"
            "    d, u = heapq.heappop(pq)\n"
            "    if d > dist[u]:\n"
            "        continue\n"
            "    for nv, w in adj[u]:\n"
            "        nd = d + w\n"
            "        if nd < dist[nv]:\n"
            "            dist[nv] = nd\n"
            "            heapq.heappush(pq, (nd, nv))\n"
            "out = []\n"
            "for i in range(1, v + 1):\n"
            "    out.append(str(dist[i]) if dist[i] != INF else 'INF')\n"
            "print('\\n'.join(out))\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int v = Integer.parseInt(st.nextToken()), e = Integer.parseInt(st.nextToken());\n"
            "        int k = Integer.parseInt(br.readLine().trim());\n"
            "        List<int[]>[] adj = new List[v + 1];\n"
            "        for (int i = 0; i <= v; i++) adj[i] = new ArrayList<>();\n"
            "        for (int i = 0; i < e; i++) {\n"
            "            st = new StringTokenizer(br.readLine());\n"
            "            int a = Integer.parseInt(st.nextToken());\n"
            "            int b = Integer.parseInt(st.nextToken());\n"
            "            int w = Integer.parseInt(st.nextToken());\n"
            "            adj[a].add(new int[]{b, w});\n"
            "        }\n"
            "        final long INF = Long.MAX_VALUE / 4;\n"
            "        long[] dist = new long[v + 1];\n"
            "        Arrays.fill(dist, INF);\n"
            "        dist[k] = 0;\n"
            "        PriorityQueue<long[]> pq = new PriorityQueue<>((x, y) -> Long.compare(x[0], y[0]));\n"
            "        pq.add(new long[]{0, k});\n"
            "        while (!pq.isEmpty()) {\n"
            "            long[] cur = pq.poll();\n"
            "            long d = cur[0]; int u = (int) cur[1];\n"
            "            if (d > dist[u]) continue;\n"
            "            for (int[] ed : adj[u]) {\n"
            "                long nd = d + ed[1];\n"
            "                if (nd < dist[ed[0]]) { dist[ed[0]] = nd; pq.add(new long[]{nd, ed[0]}); }\n"
            "            }\n"
            "        }\n"
            "        StringBuilder sb = new StringBuilder();\n"
            "        for (int i = 1; i <= v; i++) sb.append(dist[i] == INF ? \"INF\" : String.valueOf(dist[i])).append('\\n');\n"
            "        System.out.print(sb);\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp="",
        template_py=(
            "import sys, heapq\n"
            "input = sys.stdin.readline\n"
            "# 최단 경로 거리 출력 : 다익스트라, 도달 불가는 INF\n"
            "v, e = map(int, input().split())\n"
            "# ...\n"
        ),
    ),

    # ────────────────────────── 플로이드-워셜 ──────────────────────────

    Problem(
        id="gg-07",
        rank="Gold",
        tier="G4",
        category="최단경로",
        title="모든 도시 간 최단 거리",
        style="백준",
        topic="플로이드-워셜",
        type="stdin",
        description=(
            "N개의 도시와 도시 사이를 잇는 단방향 도로 M개가 있다. 각 도로에는 양의 비용이 있다. "
            "모든 도시 쌍 (i, j)에 대해 i에서 j로 가는 최소 비용을 구하시오. 같은 두 도시를 잇는 "
            "도로가 여럿일 수 있으며, 이때는 가장 작은 비용만 의미가 있다."
        ),
        input_desc=(
            "첫째 줄에 도시 수 N (1 ≤ N ≤ 100). 둘째 줄에 도로 수 M (0 ≤ M ≤ 10000). 다음 M개의 줄에 "
            "'a b c' 형식으로 도시 a에서 b로 가는 비용 c(1 ≤ c ≤ 100000)인 도로가 주어진다."
        ),
        output_desc=(
            "N개의 줄에 걸쳐 i행 j열에 i에서 j로 가는 최소 비용을 공백으로 구분해 출력한다. "
            "i에서 j로 갈 수 없거나 i와 j가 같으면 0을 출력한다."
        ),
        examples=[
            {"input": "3\n4\n1 2 2\n1 3 9\n2 3 3\n3 1 1\n", "output": "0 2 5\n4 0 3\n1 3 0\n"},
            {"input": "2\n1\n1 2 7\n", "output": "0 7\n0 0\n"},
        ],
        hints=[
            "정점 수가 작고 모든 쌍의 최단 거리가 필요합니다. 거쳐 가는 중간 정점을 하나씩 늘려 가며 거리를 갱신하는 방법이 알맞습니다.",
            "플로이드-워셜 알고리즘을 쓰세요. d[i][j]를 직접 간선으로 초기화하고, 중간 정점 k를 모든 i, j에 대해 시도합니다.",
            "d[i][k]+d[k][j] < d[i][j] 이면 갱신(삼중 반복, k가 가장 바깥). 자기 자신은 0, 도달 불가는 무한대로 두고 출력 시 무한대를 0으로.",
        ],
        testcases=[
            {"input": "3\n4\n1 2 2\n1 3 9\n2 3 3\n3 1 1\n", "output": "0 2 5\n4 0 3\n1 3 0\n"},
            {"input": "1\n0\n", "output": "0\n"},
            {"input": "2\n1\n1 2 7\n", "output": "0 7\n0 0\n"},
            {"input": "2\n2\n1 2 3\n2 1 4\n", "output": "0 3\n4 0\n"},
            {"input": "3\n2\n1 2 1\n2 3 1\n", "output": "0 1 2\n0 0 1\n0 0 0\n"},
        ],
        reference_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "n = int(input())\n"
            "m = int(input())\n"
            "INF = float('inf')\n"
            "d = [[INF] * (n + 1) for _ in range(n + 1)]\n"
            "for i in range(1, n + 1):\n"
            "    d[i][i] = 0\n"
            "for _ in range(m):\n"
            "    a, b, c = map(int, input().split())\n"
            "    if c < d[a][b]:\n"
            "        d[a][b] = c\n"
            "for k in range(1, n + 1):\n"
            "    for i in range(1, n + 1):\n"
            "        if d[i][k] == INF:\n"
            "            continue\n"
            "        for j in range(1, n + 1):\n"
            "            if d[i][k] + d[k][j] < d[i][j]:\n"
            "                d[i][j] = d[i][k] + d[k][j]\n"
            "out = []\n"
            "for i in range(1, n + 1):\n"
            "    row = ['0' if d[i][j] == INF else str(d[i][j]) for j in range(1, n + 1)]\n"
            "    out.append(' '.join(row))\n"
            "print('\\n'.join(out))\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        int n = Integer.parseInt(br.readLine().trim());\n"
            "        int m = Integer.parseInt(br.readLine().trim());\n"
            "        final long INF = Long.MAX_VALUE / 4;\n"
            "        long[][] d = new long[n + 1][n + 1];\n"
            "        for (long[] row : d) Arrays.fill(row, INF);\n"
            "        for (int i = 1; i <= n; i++) d[i][i] = 0;\n"
            "        for (int i = 0; i < m; i++) {\n"
            "            StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "            int a = Integer.parseInt(st.nextToken());\n"
            "            int b = Integer.parseInt(st.nextToken());\n"
            "            long c = Long.parseLong(st.nextToken());\n"
            "            if (c < d[a][b]) d[a][b] = c;\n"
            "        }\n"
            "        for (int k = 1; k <= n; k++)\n"
            "            for (int i = 1; i <= n; i++) {\n"
            "                if (d[i][k] == INF) continue;\n"
            "                for (int j = 1; j <= n; j++)\n"
            "                    if (d[i][k] + d[k][j] < d[i][j]) d[i][j] = d[i][k] + d[k][j];\n"
            "            }\n"
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
        reference_cpp="",
        template_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "# 모든 도시 간 최단 거리 : 플로이드-워셜\n"
            "n = int(input())\n"
            "m = int(input())\n"
            "# ...\n"
        ),
    ),

    # ────────────────────────── 유니온 파인드 ──────────────────────────

    Problem(
        id="gg-08",
        rank="Silver",
        tier="S2",
        category="유니온파인드",
        title="네트워크 묶음 개수",
        style="프로그래머스",
        topic="유니온파인드",
        type="func",
        func_name="solution",
        description=(
            "컴퓨터가 0번부터 n-1번까지 n대 있다. edges의 각 원소 [a, b]는 컴퓨터 a와 b가 직접 "
            "연결되어 있음을 뜻한다(양방향). 직접 또는 간접으로 연결된 컴퓨터들은 하나의 네트워크를 "
            "이룬다. 전체 네트워크의 개수를 반환하세요."
        ),
        input_desc="n : 컴퓨터 수(int), edges : [a, b] 형태의 연결 정보 리스트(중복 가능)",
        output_desc="서로 분리된 네트워크의 개수(정수)",
        examples=[
            {"args": [5, [[0, 1], [1, 2], [3, 4]]], "output": 2},
            {"args": [3, []], "output": 3},
        ],
        hints=[
            "연결된 컴퓨터들을 같은 그룹으로 묶고, 최종적으로 서로 다른 그룹이 몇 개인지 세면 됩니다.",
            "유니온 파인드(분리 집합)를 쓰세요. 각 간선마다 두 컴퓨터를 같은 집합으로 합치고, 마지막에 서로 다른 루트의 개수를 셉니다.",
            "parent를 0..n-1로 초기화하고 find/union 구현. 모든 간선에 union(a,b). 답은 len(set(find(i) for i in range(n))).",
        ],
        testcases=[
            {"args": [5, [[0, 1], [1, 2], [3, 4]]], "expected": 2},
            {"args": [3, []], "expected": 3},
            {"args": [1, []], "expected": 1},
            {"args": [4, [[0, 1], [1, 2], [2, 3]]], "expected": 1},
            {"args": [4, [[0, 1], [0, 1], [2, 3]]], "expected": 2},
            {"args": [6, [[0, 1], [2, 3], [4, 5]]], "expected": 3},
        ],
        reference_py=(
            "def solution(n, edges):\n"
            "    parent = list(range(n))\n"
            "    def find(x):\n"
            "        while parent[x] != x:\n"
            "            parent[x] = parent[parent[x]]\n"
            "            x = parent[x]\n"
            "        return x\n"
            "    for a, b in edges:\n"
            "        ra, rb = find(a), find(b)\n"
            "        if ra != rb:\n"
            "            parent[ra] = rb\n"
            "    return len(set(find(i) for i in range(n)))\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    int[] parent;\n"
            "    int find(int x) {\n"
            "        while (parent[x] != x) { parent[x] = parent[parent[x]]; x = parent[x]; }\n"
            "        return x;\n"
            "    }\n"
            "    public int solution(int n, int[][] edges) {\n"
            "        parent = new int[n];\n"
            "        for (int i = 0; i < n; i++) parent[i] = i;\n"
            "        for (int[] e : edges) {\n"
            "            int ra = find(e[0]), rb = find(e[1]);\n"
            "            if (ra != rb) parent[ra] = rb;\n"
            "        }\n"
            "        Set<Integer> roots = new HashSet<>();\n"
            "        for (int i = 0; i < n; i++) roots.add(find(i));\n"
            "        return roots.size();\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp="",
        template_py=(
            "# 네트워크 묶음 개수 : 유니온 파인드\n"
            "def solution(n, edges):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="gg-09",
        rank="Gold",
        tier="G4",
        category="유니온파인드",
        title="최소 연결 비용",
        style="백준",
        topic="유니온파인드",
        type="stdin",
        description=(
            "정점 V개와 가중치가 있는 양방향 간선 E개로 이루어진 연결 그래프가 있다. 모든 정점이 "
            "서로 연결되도록 간선의 일부를 골라 남기되, 고른 간선들의 가중치 합이 최소가 되도록 하라. "
            "이 최소 합(최소 신장 트리의 가중치)을 구하시오. (그래프는 항상 연결되어 있다.)"
        ),
        input_desc=(
            "첫째 줄에 정점 수 V와 간선 수 E (1 ≤ V ≤ 10000, 0 ≤ E ≤ 100000). 다음 E개의 줄에 "
            "'a b w' 형식으로 정점 a와 b를 잇는 가중치 w(정수)인 간선이 주어진다."
        ),
        output_desc="최소 신장 트리를 이루는 간선들의 가중치 합.",
        examples=[
            {"input": "3 3\n1 2 1\n2 3 2\n1 3 3\n", "output": "3\n"},
            {"input": "2 1\n1 2 5\n", "output": "5\n"},
        ],
        hints=[
            "모든 정점을 잇되 비용을 최소로 하는 간선 집합 = 최소 신장 트리(MST)입니다.",
            "크루스칼 알고리즘을 쓰세요. 간선을 가중치 오름차순으로 정렬한 뒤, 사이클을 만들지 않는 간선만 차례로 선택합니다. 사이클 판별에 유니온 파인드를 씁니다.",
            "간선을 (w, a, b)로 정렬, find(a)!=find(b)일 때만 union하고 w를 누적. V-1개의 간선을 고르면 끝. 누적합을 출력.",
        ],
        testcases=[
            {"input": "3 3\n1 2 1\n2 3 2\n1 3 3\n", "output": "3\n"},
            {"input": "2 1\n1 2 5\n", "output": "5\n"},
            {"input": "1 0\n", "output": "0\n"},
            {"input": "4 5\n1 2 1\n2 3 2\n3 4 3\n1 4 4\n2 4 5\n", "output": "6\n"},
            {"input": "4 4\n1 2 3\n2 3 3\n3 4 3\n1 2 1\n", "output": "7\n"},
        ],
        reference_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "v, e = map(int, input().split())\n"
            "edges = []\n"
            "for _ in range(e):\n"
            "    a, b, w = map(int, input().split())\n"
            "    edges.append((w, a, b))\n"
            "edges.sort()\n"
            "parent = list(range(v + 1))\n"
            "def find(x):\n"
            "    while parent[x] != x:\n"
            "        parent[x] = parent[parent[x]]\n"
            "        x = parent[x]\n"
            "    return x\n"
            "total = 0\n"
            "for w, a, b in edges:\n"
            "    ra, rb = find(a), find(b)\n"
            "    if ra != rb:\n"
            "        parent[ra] = rb\n"
            "        total += w\n"
            "print(total)\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    static int[] parent;\n"
            "    static int find(int x) {\n"
            "        while (parent[x] != x) { parent[x] = parent[parent[x]]; x = parent[x]; }\n"
            "        return x;\n"
            "    }\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int v = Integer.parseInt(st.nextToken()), e = Integer.parseInt(st.nextToken());\n"
            "        int[][] edges = new int[e][3];\n"
            "        for (int i = 0; i < e; i++) {\n"
            "            st = new StringTokenizer(br.readLine());\n"
            "            edges[i][1] = Integer.parseInt(st.nextToken());\n"
            "            edges[i][2] = Integer.parseInt(st.nextToken());\n"
            "            edges[i][0] = Integer.parseInt(st.nextToken());\n"
            "        }\n"
            "        Arrays.sort(edges, (p, q) -> Integer.compare(p[0], q[0]));\n"
            "        parent = new int[v + 1];\n"
            "        for (int i = 0; i <= v; i++) parent[i] = i;\n"
            "        long total = 0;\n"
            "        for (int[] ed : edges) {\n"
            "            int ra = find(ed[1]), rb = find(ed[2]);\n"
            "            if (ra != rb) { parent[ra] = rb; total += ed[0]; }\n"
            "        }\n"
            "        System.out.println(total);\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp="",
        template_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "# 최소 연결 비용 : 크루스칼 MST (유니온 파인드)\n"
            "v, e = map(int, input().split())\n"
            "# ...\n"
        ),
    ),

    # ────────────────────────── DFS / 연결 요소 ──────────────────────────

    Problem(
        id="gg-10",
        rank="Silver",
        tier="S2",
        category="DFS/BFS",
        title="연결 요소의 개수 세기",
        style="백준",
        topic="DFS",
        type="stdin",
        description=(
            "정점 N개와 간선 M개로 이루어진 방향 없는 그래프가 있다. 이 그래프의 연결 요소(서로 "
            "연결된 정점들의 최대 덩어리)의 개수를 구하시오."
        ),
        input_desc=(
            "첫째 줄에 정점 수 N과 간선 수 M (1 ≤ N ≤ 1000, 0 ≤ M ≤ N*(N-1)/2). 다음 M개의 줄에 "
            "'u v' 형식으로 정점 u와 v를 잇는 간선이 주어진다. (자기 간선·중복 간선은 없다.)"
        ),
        output_desc="연결 요소의 개수.",
        examples=[
            {"input": "6 5\n1 2\n2 5\n5 1\n3 4\n4 6\n", "output": "2\n"},
            {"input": "6 8\n1 2\n2 5\n5 1\n3 4\n4 6\n5 4\n2 4\n2 3\n", "output": "1\n"},
        ],
        hints=[
            "아직 방문하지 않은 정점에서 탐색을 시작할 때마다 새로운 덩어리를 하나 발견한 셈입니다.",
            "DFS(또는 BFS)로 한 정점에서 시작해 도달 가능한 모든 정점을 방문 처리하세요. 방문 안 한 정점에서 탐색을 시작한 횟수가 곧 연결 요소 개수입니다.",
            "for s in 1..N: if not visited[s]: cnt+=1; 스택/재귀로 s가 속한 덩어리를 모두 방문. 마지막에 cnt 출력. (재귀 깊이가 깊을 수 있어 반복 DFS 권장.)",
        ],
        testcases=[
            {"input": "6 5\n1 2\n2 5\n5 1\n3 4\n4 6\n", "output": "2\n"},
            {"input": "6 8\n1 2\n2 5\n5 1\n3 4\n4 6\n5 4\n2 4\n2 3\n", "output": "1\n"},
            {"input": "1 0\n", "output": "1\n"},
            {"input": "3 0\n", "output": "3\n"},
            {"input": "5 2\n1 2\n3 4\n", "output": "3\n"},
            {"input": "4 4\n1 2\n2 3\n3 4\n4 1\n", "output": "1\n"},
        ],
        reference_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "n, m = map(int, input().split())\n"
            "adj = [[] for _ in range(n + 1)]\n"
            "for _ in range(m):\n"
            "    u, v = map(int, input().split())\n"
            "    adj[u].append(v)\n"
            "    adj[v].append(u)\n"
            "visited = [False] * (n + 1)\n"
            "cnt = 0\n"
            "for s in range(1, n + 1):\n"
            "    if not visited[s]:\n"
            "        cnt += 1\n"
            "        stack = [s]\n"
            "        visited[s] = True\n"
            "        while stack:\n"
            "            x = stack.pop()\n"
            "            for y in adj[x]:\n"
            "                if not visited[y]:\n"
            "                    visited[y] = True\n"
            "                    stack.append(y)\n"
            "print(cnt)\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());\n"
            "        List<List<Integer>> adj = new ArrayList<>();\n"
            "        for (int i = 0; i <= n; i++) adj.add(new ArrayList<>());\n"
            "        for (int i = 0; i < m; i++) {\n"
            "            st = new StringTokenizer(br.readLine());\n"
            "            int u = Integer.parseInt(st.nextToken()), v = Integer.parseInt(st.nextToken());\n"
            "            adj.get(u).add(v);\n"
            "            adj.get(v).add(u);\n"
            "        }\n"
            "        boolean[] visited = new boolean[n + 1];\n"
            "        int cnt = 0;\n"
            "        for (int s = 1; s <= n; s++) {\n"
            "            if (!visited[s]) {\n"
            "                cnt++;\n"
            "                Deque<Integer> stack = new ArrayDeque<>();\n"
            "                stack.push(s);\n"
            "                visited[s] = true;\n"
            "                while (!stack.isEmpty()) {\n"
            "                    int x = stack.pop();\n"
            "                    for (int y : adj.get(x)) if (!visited[y]) { visited[y] = true; stack.push(y); }\n"
            "                }\n"
            "            }\n"
            "        }\n"
            "        System.out.println(cnt);\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp="",
        template_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "# 연결 요소의 개수 : DFS\n"
            "n, m = map(int, input().split())\n"
            "# ...\n"
        ),
    ),

    # ────────────────────────── 0-1 BFS ──────────────────────────

    Problem(
        id="gg-11",
        rank="Gold",
        tier="G4",
        category="0-1 BFS",
        title="벽 최소로 부수고 이동하기",
        style="삼성",
        topic="0-1 BFS",
        type="stdin",
        description=(
            "R행 C열 격자가 있다. 각 칸은 0(빈 칸)이거나 1(벽)이다. 왼쪽 위 칸 (0,0)에서 출발해 "
            "오른쪽 아래 칸 (R-1,C-1)까지 상하좌우로 이동한다. 빈 칸으로 들어가는 데는 비용이 없고, "
            "벽이 있는 칸으로 들어가려면 그 벽을 부수어야 하며 비용 1이 든다. 도착 칸까지 가는 데 "
            "부수어야 하는 벽의 최소 개수를 구하시오. 시작 칸은 항상 빈 칸이며 도착은 항상 가능하다."
        ),
        input_desc=(
            "첫째 줄에 행 수 R과 열 수 C (1 ≤ R, C ≤ 1000). 다음 R개의 줄에 길이 C의 문자열(0/1)이 주어진다."
        ),
        output_desc="시작 칸에서 도착 칸까지 가는 데 부수어야 하는 벽의 최소 개수.",
        examples=[
            {"input": "3 3\n010\n010\n000\n", "output": "0\n"},
            {"input": "3 3\n011\n111\n110\n", "output": "3\n"},
        ],
        hints=[
            "이동 비용이 0(빈 칸) 또는 1(벽)인 그래프에서의 최단 비용 문제입니다. 일반 BFS로는 비용 차이를 다루기 어렵습니다.",
            "0-1 BFS를 쓰세요. 일반 큐 대신 덱(deque)을 사용해, 비용 0 이동은 앞쪽에, 비용 1 이동은 뒤쪽에 넣어 항상 비용이 작은 칸부터 꺼냅니다.",
            "dist를 무한대로 초기화, dist[0][0]=0. 칸을 꺼내 인접 칸의 비용 w(벽이면 1, 아니면 0)에 대해 dist+w<이웃이면 갱신하고 w==0이면 appendleft, w==1이면 append. 마지막 dist[R-1][C-1] 출력.",
        ],
        testcases=[
            {"input": "3 3\n010\n010\n000\n", "output": "0\n"},
            {"input": "3 3\n011\n111\n110\n", "output": "3\n"},
            {"input": "1 1\n0\n", "output": "0\n"},
            {"input": "1 5\n01010\n", "output": "2\n"},
            {"input": "2 2\n01\n10\n", "output": "1\n"},
            {"input": "3 3\n000\n111\n000\n", "output": "1\n"},
        ],
        reference_py=(
            "import sys\n"
            "from collections import deque\n"
            "input = sys.stdin.readline\n"
            "r, c = map(int, input().split())\n"
            "g = [input().strip() for _ in range(r)]\n"
            "INF = float('inf')\n"
            "dist = [[INF] * c for _ in range(r)]\n"
            "dist[0][0] = 0\n"
            "dq = deque([(0, 0)])\n"
            "while dq:\n"
            "    x, y = dq.popleft()\n"
            "    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):\n"
            "        nx, ny = x + dx, y + dy\n"
            "        if 0 <= nx < r and 0 <= ny < c:\n"
            "            w = 1 if g[nx][ny] == '1' else 0\n"
            "            if dist[x][y] + w < dist[nx][ny]:\n"
            "                dist[nx][ny] = dist[x][y] + w\n"
            "                if w == 0:\n"
            "                    dq.appendleft((nx, ny))\n"
            "                else:\n"
            "                    dq.append((nx, ny))\n"
            "print(dist[r - 1][c - 1])\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int r = Integer.parseInt(st.nextToken()), c = Integer.parseInt(st.nextToken());\n"
            "        char[][] g = new char[r][];\n"
            "        for (int i = 0; i < r; i++) g[i] = br.readLine().trim().toCharArray();\n"
            "        final int INF = Integer.MAX_VALUE / 4;\n"
            "        int[][] dist = new int[r][c];\n"
            "        for (int[] row : dist) Arrays.fill(row, INF);\n"
            "        dist[0][0] = 0;\n"
            "        ArrayDeque<int[]> dq = new ArrayDeque<>();\n"
            "        dq.add(new int[]{0, 0});\n"
            "        int[] dx = {1,-1,0,0}, dy = {0,0,1,-1};\n"
            "        while (!dq.isEmpty()) {\n"
            "            int[] cur = dq.pollFirst();\n"
            "            int x = cur[0], y = cur[1];\n"
            "            for (int d = 0; d < 4; d++) {\n"
            "                int nx = x+dx[d], ny = y+dy[d];\n"
            "                if (nx>=0&&nx<r&&ny>=0&&ny<c) {\n"
            "                    int w = g[nx][ny] == '1' ? 1 : 0;\n"
            "                    if (dist[x][y] + w < dist[nx][ny]) {\n"
            "                        dist[nx][ny] = dist[x][y] + w;\n"
            "                        if (w == 0) dq.addFirst(new int[]{nx, ny});\n"
            "                        else dq.addLast(new int[]{nx, ny});\n"
            "                    }\n"
            "                }\n"
            "            }\n"
            "        }\n"
            "        System.out.println(dist[r-1][c-1]);\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp="",
        template_py=(
            "import sys\n"
            "from collections import deque\n"
            "input = sys.stdin.readline\n"
            "# 벽 최소로 부수고 이동 : 0-1 BFS\n"
            "r, c = map(int, input().split())\n"
            "# ...\n"
        ),
    ),

    # ────────────────────────── 백트래킹 (그래프 경로) ──────────────────────────

    Problem(
        id="gg-12",
        rank="Gold",
        tier="G4",
        category="백트래킹",
        title="서로 다른 경로의 수",
        style="카카오",
        topic="백트래킹",
        type="func",
        func_name="solution",
        description=(
            "정점이 0번부터 n-1번까지 있는 방향 그래프가 있다. edges의 각 원소 [u, v]는 u에서 v로 "
            "가는 방향 간선이다. start에서 end까지 가는 '단순 경로'(같은 정점을 두 번 지나지 않는 경로)의 "
            "개수를 반환하세요. start와 end가 같으면 아무 정점도 거치지 않는 경로 1개로 셉니다."
        ),
        input_desc=(
            "n : 정점 수(int), edges : [u, v] 형태의 방향 간선 리스트, start : 시작 정점, end : 도착 정점"
        ),
        output_desc="start에서 end까지의 서로 다른 단순 경로의 개수(정수)",
        examples=[
            {"args": [4, [[0, 1], [0, 2], [1, 3], [2, 3]], 0, 3], "output": 2},
            {"args": [3, [[0, 1], [1, 2], [0, 2]], 0, 2], "output": 2},
        ],
        hints=[
            "모든 경로를 직접 만들어 보되, 같은 정점을 다시 밟지 않도록 방문 표시를 관리해야 합니다.",
            "백트래킹(DFS)으로 경로를 확장하세요. 현재 정점을 방문 처리하고 인접 정점으로 들어갔다가, 돌아올 때 방문 표시를 해제(복구)합니다.",
            "visited[start]=True 후 dfs(start). dfs에서 u==end면 카운트+1 후 반환, 아니면 방문 안 한 인접 v마다 visited[v]=True; dfs(v); visited[v]=False. 누적 카운트 반환.",
        ],
        testcases=[
            {"args": [4, [[0, 1], [0, 2], [1, 3], [2, 3]], 0, 3], "expected": 2},
            {"args": [3, [[0, 1], [1, 2], [0, 2]], 0, 2], "expected": 2},
            {"args": [2, [[0, 1]], 0, 1], "expected": 1},
            {"args": [2, [], 0, 1], "expected": 0},
            {"args": [3, [[0, 1], [1, 2]], 0, 0], "expected": 1},
            {"args": [4, [[0, 1], [0, 2], [1, 2], [2, 3], [1, 3]], 0, 3], "expected": 3},
        ],
        reference_py=(
            "def solution(n, edges, start, end):\n"
            "    adj = [[] for _ in range(n)]\n"
            "    for u, v in edges:\n"
            "        adj[u].append(v)\n"
            "    visited = [False] * n\n"
            "    cnt = 0\n"
            "    def dfs(u):\n"
            "        nonlocal cnt\n"
            "        if u == end:\n"
            "            cnt += 1\n"
            "            return\n"
            "        for v in adj[u]:\n"
            "            if not visited[v]:\n"
            "                visited[v] = True\n"
            "                dfs(v)\n"
            "                visited[v] = False\n"
            "    visited[start] = True\n"
            "    dfs(start)\n"
            "    return cnt\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    List<List<Integer>> adj;\n"
            "    boolean[] visited;\n"
            "    int end, cnt;\n"
            "    void dfs(int u) {\n"
            "        if (u == end) { cnt++; return; }\n"
            "        for (int v : adj.get(u)) {\n"
            "            if (!visited[v]) { visited[v] = true; dfs(v); visited[v] = false; }\n"
            "        }\n"
            "    }\n"
            "    public int solution(int n, int[][] edges, int start, int end) {\n"
            "        adj = new ArrayList<>();\n"
            "        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());\n"
            "        for (int[] e : edges) adj.get(e[0]).add(e[1]);\n"
            "        visited = new boolean[n];\n"
            "        this.end = end; this.cnt = 0;\n"
            "        visited[start] = true;\n"
            "        dfs(start);\n"
            "        return cnt;\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp="",
        template_py=(
            "# 서로 다른 단순 경로의 수 : 백트래킹\n"
            "def solution(n, edges, start, end):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

]
