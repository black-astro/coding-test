"""유형별 실전 — DFS/BFS.

대한민국 대기업 코딩테스트 실전형 문제 모음.
섬의 개수 / 네트워크 / 미로 최단거리 / 다중 시작 전파 / 상태 변화 탐색.
"""

from engine.models import Problem

CATEGORY = "DFS/BFS"

PROBLEMS = [

    # ──────────────────────────────────────────────────────────────
    Problem(
        id="bfs-01",
        rank="Silver",
        title="섬의 개수 세기",
        style="삼성",
        topic="플러드 필",
        type="stdin",
        category="DFS/BFS",
        description=(
            "N×M 크기의 지도가 주어진다. 1은 땅, 0은 바다이다. "
            "상하좌우로 연결된 1들의 덩어리 하나를 '섬' 한 개로 본다(대각선은 연결로 보지 않는다). "
            "지도에 존재하는 섬의 총 개수를 구하라.\n\n"
            "회사 위성 영상에서 육지 픽셀이 몇 개의 독립된 섬으로 나뉘는지 세는 상황을 떠올리면 된다. "
            "연결 요소(connected component)의 개수를 구하는 가장 기본적인 그래프 탐색 문제이다."
        ),
        input_desc=(
            "첫째 줄에 지도의 세로 길이 N과 가로 길이 M이 공백으로 주어진다 "
            "(1 ≤ N, M ≤ 100).\n"
            "다음 N개의 줄에 각각 길이 M인 0/1 문자열이 주어진다."
        ),
        output_desc="섬의 개수를 정수 한 줄로 출력한다.",
        examples=[
            {"input": "5 5\n11000\n11000\n00011\n00011\n00000\n", "output": "2\n"},
            {"input": "3 3\n101\n010\n101\n", "output": "5\n"},
        ],
        hints=[
            "1인 칸을 하나 발견할 때마다 거기서 출발해, 연결된 1들을 모두 방문 처리하면 그 한 덩어리가 섬 하나입니다. 새로 탐색을 시작한 횟수가 곧 섬의 개수입니다.",
            "BFS(또는 DFS)와 방문 배열을 사용하세요. 아직 방문하지 않은 1을 만나면 카운트를 1 늘리고, 그 칸에서 BFS로 같은 섬을 모두 방문 처리합니다.",
            "for i,j: if g[i][j]=='1' and not visited: cnt+=1; deque로 BFS 돌며 인접한 '1'을 visited=True. 4방향만 본다. 끝나면 cnt 출력.",
        ],
        testcases=[
            {"input": "5 5\n11000\n11000\n00011\n00011\n00000\n", "output": "2\n"},
            {"input": "3 3\n101\n010\n101\n", "output": "5\n"},
            {"input": "1 1\n0\n", "output": "0\n"},
            {"input": "1 1\n1\n", "output": "1\n"},
            {"input": "2 3\n111\n000\n", "output": "1\n"},
            {"input": "4 4\n1000\n0100\n0010\n0001\n", "output": "4\n"},
        ],
        reference_py=(
            "import sys\n"
            "from collections import deque\n"
            "input = sys.stdin.readline\n"
            "n, m = map(int, input().split())\n"
            "g = [input().strip() for _ in range(n)]\n"
            "visited = [[False] * m for _ in range(n)]\n"
            "cnt = 0\n"
            "for i in range(n):\n"
            "    for j in range(m):\n"
            "        if g[i][j] == '1' and not visited[i][j]:\n"
            "            cnt += 1\n"
            "            visited[i][j] = True\n"
            "            q = deque([(i, j)])\n"
            "            while q:\n"
            "                x, y = q.popleft()\n"
            "                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):\n"
            "                    nx, ny = x + dx, y + dy\n"
            "                    if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == '1' and not visited[nx][ny]:\n"
            "                        visited[nx][ny] = True\n"
            "                        q.append((nx, ny))\n"
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
            "        char[][] g = new char[n][];\n"
            "        for (int i = 0; i < n; i++) g[i] = br.readLine().toCharArray();\n"
            "        boolean[][] vis = new boolean[n][m];\n"
            "        int[] dx = {1,-1,0,0}, dy = {0,0,1,-1};\n"
            "        int cnt = 0;\n"
            "        for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) {\n"
            "            if (g[i][j] == '1' && !vis[i][j]) {\n"
            "                cnt++;\n"
            "                vis[i][j] = true;\n"
            "                ArrayDeque<int[]> q = new ArrayDeque<>();\n"
            "                q.add(new int[]{i, j});\n"
            "                while (!q.isEmpty()) {\n"
            "                    int[] c = q.poll();\n"
            "                    for (int d = 0; d < 4; d++) {\n"
            "                        int nx = c[0]+dx[d], ny = c[1]+dy[d];\n"
            "                        if (nx>=0&&nx<n&&ny>=0&&ny<m&&g[nx][ny]=='1'&&!vis[nx][ny]) {\n"
            "                            vis[nx][ny] = true;\n"
            "                            q.add(new int[]{nx, ny});\n"
            "                        }\n"
            "                    }\n"
            "                }\n"
            "            }\n"
            "        }\n"
            "        System.out.println(cnt);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "from collections import deque\n"
            "input = sys.stdin.readline\n"
            "# 섬의 개수 (연결 요소 개수)\n"
            "n, m = map(int, input().split())\n"
            "g = [input().strip() for _ in range(n)]\n"
            "# TODO: 방문 배열 + BFS 로 섬을 세보세요.\n"
        ),
    ),

    # ──────────────────────────────────────────────────────────────
    Problem(
        id="bfs-02",
        rank="Silver",
        title="네트워크 묶음 개수",
        style="카카오",
        topic="연결 요소",
        type="func",
        func_name="solution",
        category="DFS/BFS",
        description=(
            "컴퓨터의 개수 n과 연결 정보 computers가 주어진다. computers[i][j]가 1이면 "
            "컴퓨터 i와 j가 직접 연결되어 있다는 뜻이다. A가 B와 연결되고 B가 C와 연결되면 "
            "A와 C도 같은 네트워크로 본다(연결은 양방향이며 자기 자신 computers[i][i]는 항상 1).\n\n"
            "서로 다른 네트워크(연결 요소)가 몇 개인지 반환하라."
        ),
        input_desc="n : 컴퓨터 수 (1 ≤ n ≤ 200), computers : n×n 0/1 인접 행렬",
        output_desc="네트워크의 개수 (정수)",
        examples=[
            {"args": [3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]], "output": 2},
            {"args": [3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]], "output": 1},
        ],
        hints=[
            "한 컴퓨터에서 출발해 연결된 모든 컴퓨터를 방문 처리하면 그 한 덩어리가 네트워크 하나입니다. 아직 방문 안 된 컴퓨터에서 새로 탐색을 시작한 횟수를 세면 됩니다.",
            "방문 배열 visited를 두고, 0번부터 차례로 보며 미방문 컴퓨터에서 DFS/BFS를 시작할 때마다 카운트를 늘립니다.",
            "for s in range(n): if not visited[s]: cnt+=1; stack 으로 DFS, computers[x][y]==1 이고 미방문이면 visited[y]=True 후 push. 마지막에 cnt 반환.",
        ],
        testcases=[
            {"args": [3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]], "expected": 2},
            {"args": [3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]], "expected": 1},
            {"args": [1, [[1]]], "expected": 1},
            {"args": [4, [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]], "expected": 4},
            {"args": [5, [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 1]]], "expected": 3},
        ],
        reference_py=(
            "def solution(n, computers):\n"
            "    visited = [False] * n\n"
            "    cnt = 0\n"
            "    for s in range(n):\n"
            "        if not visited[s]:\n"
            "            cnt += 1\n"
            "            stack = [s]\n"
            "            visited[s] = True\n"
            "            while stack:\n"
            "                x = stack.pop()\n"
            "                for y in range(n):\n"
            "                    if computers[x][y] == 1 and not visited[y]:\n"
            "                        visited[y] = True\n"
            "                        stack.append(y)\n"
            "    return cnt\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int solution(int n, int[][] computers) {\n"
            "        boolean[] visited = new boolean[n];\n"
            "        int cnt = 0;\n"
            "        for (int s = 0; s < n; s++) {\n"
            "            if (!visited[s]) {\n"
            "                cnt++;\n"
            "                Deque<Integer> stack = new ArrayDeque<>();\n"
            "                stack.push(s);\n"
            "                visited[s] = true;\n"
            "                while (!stack.isEmpty()) {\n"
            "                    int x = stack.pop();\n"
            "                    for (int y = 0; y < n; y++)\n"
            "                        if (computers[x][y] == 1 && !visited[y]) {\n"
            "                            visited[y] = true;\n"
            "                            stack.push(y);\n"
            "                        }\n"
            "                }\n"
            "            }\n"
            "        }\n"
            "        return cnt;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 네트워크 개수 (연결 요소)\n"
            "def solution(n, computers):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    # ──────────────────────────────────────────────────────────────
    Problem(
        id="bfs-03",
        rank="Gold",
        title="미로의 최단 경로 칸수",
        style="소프티어",
        topic="BFS 최단거리",
        type="stdin",
        category="DFS/BFS",
        description=(
            "N×M 미로가 주어진다. 1은 지나갈 수 있는 길, 0은 벽이다. "
            "출발 칸 (1,1)에서 도착 칸 (N,M)까지 상하좌우로만 이동할 때, "
            "지나는 칸의 최소 개수(출발 칸과 도착 칸 모두 포함)를 구하라.\n\n"
            "도착 칸까지 갈 수 없으면 -1을 출력한다. 가중치 없는 격자에서의 최단 거리이므로 "
            "BFS로 한 칸씩 퍼뜨리며 거리를 채우면 가장 먼저 도착했을 때의 거리가 정답이다."
        ),
        input_desc=(
            "첫째 줄에 N과 M (1 ≤ N, M ≤ 100).\n"
            "다음 N개의 줄에 길이 M인 0/1 문자열. (1,1)과 (N,M)은 항상 1로 주어진다."
        ),
        output_desc="최단 경로의 칸 수. 도달 불가능하면 -1.",
        examples=[
            {"input": "4 6\n101111\n101010\n101011\n111011\n", "output": "15\n"},
            {"input": "3 3\n111\n011\n001\n", "output": "5\n"},
        ],
        hints=[
            "모든 이동 비용이 1로 같으므로, 출발점에서 BFS로 한 겹씩 퍼져나가면 어떤 칸에 처음 도달한 순간이 곧 그 칸까지의 최단 거리입니다.",
            "deque로 BFS를 돌리며 dist 배열에 거리를 기록하세요. 출발 칸 거리를 1로 두고, 인접한 길('1')이면서 아직 거리 0(미방문)인 칸에 현재 거리+1을 채웁니다.",
            "dist[0][0]=1; 인접한 g[nx][ny]=='1' and dist[nx][ny]==0 이면 dist[nx][ny]=dist[x][y]+1. 끝나면 dist[N-1][M-1]이 0이면 -1, 아니면 그 값 출력.",
        ],
        testcases=[
            {"input": "4 6\n101111\n101010\n101011\n111011\n", "output": "15\n"},
            {"input": "3 3\n111\n011\n001\n", "output": "5\n"},
            {"input": "2 2\n10\n01\n", "output": "-1\n"},
            {"input": "1 1\n1\n", "output": "1\n"},
            {"input": "1 5\n11111\n", "output": "5\n"},
        ],
        reference_py=(
            "import sys\n"
            "from collections import deque\n"
            "input = sys.stdin.readline\n"
            "n, m = map(int, input().split())\n"
            "g = [input().strip() for _ in range(n)]\n"
            "dist = [[0] * m for _ in range(n)]\n"
            "dist[0][0] = 1\n"
            "q = deque([(0, 0)])\n"
            "while q:\n"
            "    x, y = q.popleft()\n"
            "    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):\n"
            "        nx, ny = x + dx, y + dy\n"
            "        if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == '1' and dist[nx][ny] == 0:\n"
            "            dist[nx][ny] = dist[x][y] + 1\n"
            "            q.append((nx, ny))\n"
            "ans = dist[n - 1][m - 1]\n"
            "print(ans if ans != 0 else -1)\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());\n"
            "        char[][] g = new char[n][];\n"
            "        for (int i = 0; i < n; i++) g[i] = br.readLine().toCharArray();\n"
            "        int[][] dist = new int[n][m];\n"
            "        dist[0][0] = 1;\n"
            "        ArrayDeque<int[]> q = new ArrayDeque<>();\n"
            "        q.add(new int[]{0, 0});\n"
            "        int[] dx = {1,-1,0,0}, dy = {0,0,1,-1};\n"
            "        while (!q.isEmpty()) {\n"
            "            int[] c = q.poll();\n"
            "            for (int d = 0; d < 4; d++) {\n"
            "                int nx = c[0]+dx[d], ny = c[1]+dy[d];\n"
            "                if (nx>=0&&nx<n&&ny>=0&&ny<m&&g[nx][ny]=='1'&&dist[nx][ny]==0) {\n"
            "                    dist[nx][ny] = dist[c[0]][c[1]] + 1;\n"
            "                    q.add(new int[]{nx, ny});\n"
            "                }\n"
            "            }\n"
            "        }\n"
            "        int ans = dist[n-1][m-1];\n"
            "        System.out.println(ans != 0 ? ans : -1);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "from collections import deque\n"
            "input = sys.stdin.readline\n"
            "# 미로 최단 경로 칸수 (BFS)\n"
            "n, m = map(int, input().split())\n"
            "g = [input().strip() for _ in range(n)]\n"
            "# TODO: BFS 로 dist 채우고 도착칸 출력 (불가능하면 -1)\n"
        ),
    ),

    # ──────────────────────────────────────────────────────────────
    Problem(
        id="bfs-04",
        rank="Gold",
        title="전염병 전파 최소 일수",
        style="네이버",
        topic="다중 시작 BFS",
        type="stdin",
        category="DFS/BFS",
        description=(
            "N×M 격자에 도시 상태가 주어진다. 각 칸의 값은 2(감염된 도시), 1(아직 건강하지만 "
            "감염될 수 있는 도시), 0(통행이 막힌 차단 구역)이다. "
            "하루가 지날 때마다 감염된 도시는 상하좌우로 인접한 '건강한 도시(1)'를 감염시킨다. "
            "여러 감염원이 동시에 퍼지기 시작한다.\n\n"
            "모든 건강한 도시가 감염되기까지 걸리는 최소 일수를 구하라. "
            "끝까지 감염될 수 없는 건강한 도시가 하나라도 있으면 -1을, "
            "처음부터 건강한 도시가 하나도 없으면 0을 출력한다."
        ),
        input_desc=(
            "첫째 줄에 N과 M (1 ≤ N, M ≤ 100).\n"
            "다음 N개의 줄에 각 칸의 값(0/1/2)이 공백으로 구분되어 주어진다."
        ),
        output_desc="모든 건강한 도시가 감염되는 최소 일수. 불가능하면 -1, 건강한 도시가 없으면 0.",
        examples=[
            {"input": "3 3\n2 1 1\n1 1 1\n1 1 2\n", "output": "2\n"},
            {"input": "1 5\n2 1 1 1 1\n", "output": "4\n"},
        ],
        hints=[
            "감염원이 여러 개라도, 모든 감염원을 처음부터 큐에 함께 넣고 동시에 퍼뜨리면(다중 시작 BFS) 각 칸이 감염되는 '가장 빠른 날'을 한 번에 구할 수 있습니다.",
            "감염된 칸을 전부 거리 0으로 큐에 넣고 BFS를 돌려 dist를 채우세요. 정답은 감염 가능 칸들의 dist 중 최댓값입니다. 끝까지 dist가 미정(-1)인 1이 남으면 -1입니다.",
            "모든 2를 dist=0으로 큐에 push → BFS로 인접 1에 dist+1 전파. 마지막에 값이 1인 칸을 검사: 하나라도 미방문이면 -1, 아니면 max(dist) 출력(없으면 0).",
        ],
        testcases=[
            {"input": "3 3\n2 1 1\n1 1 1\n1 1 2\n", "output": "2\n"},
            {"input": "1 5\n2 1 1 1 1\n", "output": "4\n"},
            {"input": "3 3\n2 1 0\n0 0 0\n0 1 1\n", "output": "-1\n"},
            {"input": "2 2\n2 0\n0 2\n", "output": "0\n"},
            {"input": "1 1\n2\n", "output": "0\n"},
            {"input": "1 1\n1\n", "output": "-1\n"},
        ],
        reference_py=(
            "import sys\n"
            "from collections import deque\n"
            "data = sys.stdin.read().split()\n"
            "idx = 0\n"
            "n = int(data[idx]); idx += 1\n"
            "m = int(data[idx]); idx += 1\n"
            "g = []\n"
            "for _ in range(n):\n"
            "    row = [int(data[idx + j]) for j in range(m)]\n"
            "    idx += m\n"
            "    g.append(row)\n"
            "dist = [[-1] * m for _ in range(n)]\n"
            "q = deque()\n"
            "for i in range(n):\n"
            "    for j in range(m):\n"
            "        if g[i][j] == 2:\n"
            "            dist[i][j] = 0\n"
            "            q.append((i, j))\n"
            "while q:\n"
            "    x, y = q.popleft()\n"
            "    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):\n"
            "        nx, ny = x + dx, y + dy\n"
            "        if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == 1 and dist[nx][ny] == -1:\n"
            "            dist[nx][ny] = dist[x][y] + 1\n"
            "            q.append((nx, ny))\n"
            "ans = 0\n"
            "ok = True\n"
            "for i in range(n):\n"
            "    for j in range(m):\n"
            "        if g[i][j] == 1:\n"
            "            if dist[i][j] == -1:\n"
            "                ok = False\n"
            "            else:\n"
            "                ans = max(ans, dist[i][j])\n"
            "print(ans if ok else -1)\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        StreamTokenizer in = new StreamTokenizer(br);\n"
            "        in.nextToken(); int n = (int) in.nval;\n"
            "        in.nextToken(); int m = (int) in.nval;\n"
            "        int[][] g = new int[n][m];\n"
            "        int[][] dist = new int[n][m];\n"
            "        ArrayDeque<int[]> q = new ArrayDeque<>();\n"
            "        for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) {\n"
            "            in.nextToken(); g[i][j] = (int) in.nval; dist[i][j] = -1;\n"
            "        }\n"
            "        for (int i = 0; i < n; i++) for (int j = 0; j < m; j++)\n"
            "            if (g[i][j] == 2) { dist[i][j] = 0; q.add(new int[]{i, j}); }\n"
            "        int[] dx = {1,-1,0,0}, dy = {0,0,1,-1};\n"
            "        while (!q.isEmpty()) {\n"
            "            int[] c = q.poll();\n"
            "            for (int d = 0; d < 4; d++) {\n"
            "                int nx = c[0]+dx[d], ny = c[1]+dy[d];\n"
            "                if (nx>=0&&nx<n&&ny>=0&&ny<m&&g[nx][ny]==1&&dist[nx][ny]==-1) {\n"
            "                    dist[nx][ny] = dist[c[0]][c[1]] + 1;\n"
            "                    q.add(new int[]{nx, ny});\n"
            "                }\n"
            "            }\n"
            "        }\n"
            "        int ans = 0; boolean ok = true;\n"
            "        for (int i = 0; i < n; i++) for (int j = 0; j < m; j++)\n"
            "            if (g[i][j] == 1) {\n"
            "                if (dist[i][j] == -1) ok = false;\n"
            "                else ans = Math.max(ans, dist[i][j]);\n"
            "            }\n"
            "        System.out.println(ok ? ans : -1);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "from collections import deque\n"
            "# 전염병 전파 (다중 시작 BFS)\n"
            "data = sys.stdin.read().split()\n"
            "# TODO: 모든 감염원을 큐에 넣고 동시에 BFS\n"
        ),
    ),

    # ──────────────────────────────────────────────────────────────
    Problem(
        id="bfs-05",
        rank="Platinum",
        title="벽 한 번 부수고 탈출하기",
        style="라인",
        topic="상태 공간 BFS",
        type="stdin",
        category="DFS/BFS",
        description=(
            "N×M 격자가 주어진다. 0은 빈 길, 1은 벽이다. (1,1)에서 출발해 (N,M)까지 "
            "상하좌우로 이동한다. 단, 이동 도중 벽을 '딱 한 번까지' 부수고 지나갈 수 있다.\n\n"
            "출발 칸과 도착 칸을 모두 포함해 지나는 칸의 최소 개수를 구하라. "
            "벽을 한 번 부수는 것을 허용해도 도착할 수 없으면 -1을 출력한다. "
            "(출발 칸과 도착 칸은 항상 빈 길 0이다.)\n\n"
            "핵심은 '벽을 아직 안 부순 상태'와 '이미 부순 상태'를 서로 다른 칸처럼 취급하는 것이다."
        ),
        input_desc=(
            "첫째 줄에 N과 M (1 ≤ N, M ≤ 100).\n"
            "다음 N개의 줄에 길이 M인 0/1 문자열."
        ),
        output_desc="최단 경로의 칸 수. 벽을 한 번 부숴도 불가능하면 -1.",
        examples=[
            {"input": "3 3\n000\n111\n000\n", "output": "5\n"},
            {"input": "1 4\n0110\n", "output": "-1\n"},
        ],
        hints=[
            "단순 최단거리에 '벽을 부쉈는가'라는 정보를 하나 더 붙여야 합니다. 같은 칸이라도 벽을 안 부순 채 도착했는지, 부순 채 도착했는지에 따라 이후 갈 수 있는 곳이 달라집니다.",
            "상태를 (행, 열, 부순 여부 0/1)로 두고 BFS 하세요. 방문 배열도 dist[x][y][0/1]처럼 3차원으로 둡니다. 빈 길로 가면 부순 여부 유지, 벽으로 갈 때는 아직 안 부쉈을 때만(b==0) 부숨 상태(1)로 진입.",
            "큐에 (x,y,b). 빈칸 '0': dist[nx][ny][b] 미방문이면 +1. 벽 '1' and b==0: dist[nx][ny][1] 미방문이면 dist[x][y][0]+1. BFS이므로 도착 칸(어느 b든) 처음 pop되는 거리가 정답. 둘 다 못 가면 -1.",
        ],
        testcases=[
            {"input": "3 3\n000\n111\n000\n", "output": "5\n"},
            {"input": "1 4\n0110\n", "output": "-1\n"},
            {"input": "1 1\n0\n", "output": "1\n"},
            {"input": "1 3\n010\n", "output": "3\n"},
            {"input": "1 3\n000\n", "output": "3\n"},
            {"input": "4 4\n0000\n1110\n0000\n1110\n", "output": "7\n"},
        ],
        reference_py=(
            "import sys\n"
            "from collections import deque\n"
            "input = sys.stdin.readline\n"
            "n, m = map(int, input().split())\n"
            "g = [input().strip() for _ in range(n)]\n"
            "dist = [[[-1, -1] for _ in range(m)] for _ in range(n)]\n"
            "dist[0][0][0] = 1\n"
            "q = deque([(0, 0, 0)])\n"
            "ans = -1\n"
            "while q:\n"
            "    x, y, b = q.popleft()\n"
            "    if x == n - 1 and y == m - 1:\n"
            "        ans = dist[x][y][b]\n"
            "        break\n"
            "    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):\n"
            "        nx, ny = x + dx, y + dy\n"
            "        if 0 <= nx < n and 0 <= ny < m:\n"
            "            if g[nx][ny] == '0' and dist[nx][ny][b] == -1:\n"
            "                dist[nx][ny][b] = dist[x][y][b] + 1\n"
            "                q.append((nx, ny, b))\n"
            "            elif g[nx][ny] == '1' and b == 0 and dist[nx][ny][1] == -1:\n"
            "                dist[nx][ny][1] = dist[x][y][0] + 1\n"
            "                q.append((nx, ny, 1))\n"
            "print(ans)\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());\n"
            "        char[][] g = new char[n][];\n"
            "        for (int i = 0; i < n; i++) g[i] = br.readLine().toCharArray();\n"
            "        int[][][] dist = new int[n][m][2];\n"
            "        for (int[][] a : dist) for (int[] r : a) Arrays.fill(r, -1);\n"
            "        dist[0][0][0] = 1;\n"
            "        ArrayDeque<int[]> q = new ArrayDeque<>();\n"
            "        q.add(new int[]{0, 0, 0});\n"
            "        int[] dx = {1,-1,0,0}, dy = {0,0,1,-1};\n"
            "        int ans = -1;\n"
            "        while (!q.isEmpty()) {\n"
            "            int[] c = q.poll();\n"
            "            int x = c[0], y = c[1], b = c[2];\n"
            "            if (x == n-1 && y == m-1) { ans = dist[x][y][b]; break; }\n"
            "            for (int d = 0; d < 4; d++) {\n"
            "                int nx = x+dx[d], ny = y+dy[d];\n"
            "                if (nx<0||nx>=n||ny<0||ny>=m) continue;\n"
            "                if (g[nx][ny]=='0' && dist[nx][ny][b]==-1) {\n"
            "                    dist[nx][ny][b] = dist[x][y][b] + 1;\n"
            "                    q.add(new int[]{nx, ny, b});\n"
            "                } else if (g[nx][ny]=='1' && b==0 && dist[nx][ny][1]==-1) {\n"
            "                    dist[nx][ny][1] = dist[x][y][0] + 1;\n"
            "                    q.add(new int[]{nx, ny, 1});\n"
            "                }\n"
            "            }\n"
            "        }\n"
            "        System.out.println(ans);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "from collections import deque\n"
            "input = sys.stdin.readline\n"
            "# 벽 한 번 부수고 탈출 (상태 공간 BFS: 행, 열, 부순여부)\n"
            "n, m = map(int, input().split())\n"
            "g = [input().strip() for _ in range(n)]\n"
            "# TODO: dist[x][y][0/1] 로 BFS\n"
        ),
    ),

]
