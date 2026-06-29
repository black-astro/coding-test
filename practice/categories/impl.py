"""구현/시뮬레이션 유형별 실전 문제 (impl-01 ~ impl-05).

대한민국 대기업 코딩테스트 실전 감각을 위한 구현/시뮬레이션 모음.
"""

from engine.models import Problem

CATEGORY = "구현/시뮬레이션"

PROBLEMS = [

    # ────────────────────────────────────────────────────────────
    Problem(
        id="impl-01",
        rank="Silver",
        title="청소 로봇의 격자 순찰",
        style="삼성",
        topic="격자 시뮬레이션",
        category="구현/시뮬레이션",
        type="stdin",
        description=(
            "R행 C열의 격자형 사무실에 청소 로봇 한 대가 놓여 있다. 격자의 각 칸은 빈 칸('.') "
            "또는 책상('#') 중 하나다. 로봇은 처음에 (sr, sc) 칸에서 특정 방향(N=북, E=동, "
            "S=남, W=서)을 바라보고 서 있다.\n\n"
            "로봇은 명령 문자열을 한 글자씩 순서대로 수행한다. 명령은 다음 세 가지뿐이다.\n"
            "  - 'L' : 제자리에서 시계 반대 방향으로 90도 회전한다(이동하지 않는다).\n"
            "  - 'R' : 제자리에서 시계 방향으로 90도 회전한다(이동하지 않는다).\n"
            "  - 'F' : 바라보는 방향으로 한 칸 전진한다. 단, 전진하려는 칸이 격자 밖이거나 "
            "책상('#')이면 이동하지 않고 그 자리에 그대로 머문다(방향도 그대로).\n\n"
            "북쪽은 행 번호가 감소하는 방향, 남쪽은 행 번호가 증가하는 방향, 동쪽은 열 번호가 "
            "증가하는 방향, 서쪽은 열 번호가 감소하는 방향이다. 격자의 좌상단 칸이 (1, 1)이다. "
            "회전 방향 순서는 시계 방향으로 N → E → S → W → N 이다.\n\n"
            "모든 명령을 수행한 뒤 로봇의 최종 위치와 바라보는 방향을 구하라. 시작 칸은 절대 "
            "책상이 아님이 보장된다."
        ),
        input_desc=(
            "첫째 줄에 R C (1 ≤ R, C ≤ 50).\n"
            "다음 R개의 줄에 길이 C인 격자 문자열('.' 또는 '#').\n"
            "다음 줄에 sr sc d (1 ≤ sr ≤ R, 1 ≤ sc ≤ C, d는 N/E/S/W 중 하나).\n"
            "마지막 줄에 명령 문자열(길이 1 이상, 문자는 L/R/F 만)."
        ),
        output_desc="모든 명령 수행 후 '최종행 최종열 최종방향' 을 공백으로 구분해 한 줄에 출력.",
        examples=[
            {"input": "3 3\n...\n.#.\n...\n2 1 E\nFFRFLFR\n", "output": "3 2 S\n"},
            {"input": "2 2\n..\n..\n1 1 N\nRFRFRFRF\n", "output": "1 1 N\n"},
        ],
        hints=[
            "방향을 N,E,S,W 순서의 배열로 두면 시계 방향 회전은 인덱스 +1, 반시계 회전은 인덱스 +3(=-1)을 4로 나눈 나머지로 간단히 표현됩니다.",
            "각 방향에 대한 행/열 증가량(델타)을 미리 표로 만들어 두고, 'F'일 때만 경계 검사와 책상 검사를 통과하면 좌표를 갱신하세요.",
            "dirs=['N','E','S','W']; d=dirs.index(시작방향). 각 명령마다: L이면 d=(d+3)%4, R이면 d=(d+1)%4, F이면 nr,nc 계산 후 1<=nr<=R and 1<=nc<=C and grid[nr-1][nc-1]!='#' 일 때만 이동. 마지막에 r c dirs[d] 출력.",
        ],
        testcases=[
            {"input": "3 3\n...\n.#.\n...\n2 1 E\nFFRFLFR\n", "output": "3 2 S\n"},
            {"input": "2 2\n..\n..\n1 1 N\nRFRFRFRF\n", "output": "1 1 N\n"},
            {"input": "1 1\n.\n1 1 N\nFFFF\n", "output": "1 1 N\n"},
            {"input": "3 4\n....\n..#.\n....\n1 1 S\nFFRFF\n", "output": "3 1 W\n"},
            {"input": "2 2\n..\n..\n1 1 N\nL\n", "output": "1 1 W\n"},
        ],
        reference_py=(
            "import sys\n"
            "def main():\n"
            "    data = sys.stdin.read().split('\\n')\n"
            "    idx = 0\n"
            "    R, C = map(int, data[idx].split()); idx += 1\n"
            "    grid = []\n"
            "    for _ in range(R):\n"
            "        grid.append(data[idx]); idx += 1\n"
            "    sr, sc, sd = data[idx].split(); idx += 1\n"
            "    sr = int(sr); sc = int(sc)\n"
            "    cmds = data[idx].strip()\n"
            "    dirs = ['N', 'E', 'S', 'W']\n"
            "    dr = {'N': -1, 'E': 0, 'S': 1, 'W': 0}\n"
            "    dc = {'N': 0, 'E': 1, 'S': 0, 'W': -1}\n"
            "    d = dirs.index(sd)\n"
            "    r, c = sr, sc\n"
            "    for ch in cmds:\n"
            "        if ch == 'L':\n"
            "            d = (d + 3) % 4\n"
            "        elif ch == 'R':\n"
            "            d = (d + 1) % 4\n"
            "        elif ch == 'F':\n"
            "            nd = dirs[d]\n"
            "            nr, nc = r + dr[nd], c + dc[nd]\n"
            "            if 1 <= nr <= R and 1 <= nc <= C and grid[nr - 1][nc - 1] != '#':\n"
            "                r, c = nr, nc\n"
            "    print(r, c, dirs[d])\n"
            "main()\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int R = Integer.parseInt(st.nextToken());\n"
            "        int C = Integer.parseInt(st.nextToken());\n"
            "        char[][] grid = new char[R][];\n"
            "        for (int i = 0; i < R; i++) grid[i] = br.readLine().toCharArray();\n"
            "        st = new StringTokenizer(br.readLine());\n"
            "        int r = Integer.parseInt(st.nextToken());\n"
            "        int c = Integer.parseInt(st.nextToken());\n"
            "        String sd = st.nextToken();\n"
            "        String cmds = br.readLine().trim();\n"
            "        String dirs = \"NESW\";\n"
            "        int[] dr = {-1, 0, 1, 0};\n"
            "        int[] dc = {0, 1, 0, -1};\n"
            "        int d = dirs.indexOf(sd);\n"
            "        for (int k = 0; k < cmds.length(); k++) {\n"
            "            char ch = cmds.charAt(k);\n"
            "            if (ch == 'L') d = (d + 3) % 4;\n"
            "            else if (ch == 'R') d = (d + 1) % 4;\n"
            "            else if (ch == 'F') {\n"
            "                int nr = r + dr[d], nc = c + dc[d];\n"
            "                if (nr >= 1 && nr <= R && nc >= 1 && nc <= C && grid[nr-1][nc-1] != '#') {\n"
            "                    r = nr; c = nc;\n"
            "                }\n"
            "            }\n"
            "        }\n"
            "        System.out.println(r + \" \" + c + \" \" + dirs.charAt(d));\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "def main():\n"
            "    data = sys.stdin.read().split('\\n')\n"
            "    # R C, 격자 R줄, 시작(sr sc d), 명령 문자열 순으로 파싱\n"
            "    # dirs=['N','E','S','W'] 로 회전/전진 시뮬레이션\n"
            "    pass\n"
            "main()\n"
        ),
    ),

    # ────────────────────────────────────────────────────────────
    Problem(
        id="impl-02",
        rank="Silver",
        title="게임판 시계방향 회전",
        style="네이버",
        topic="2차원 배열 회전",
        category="구현/시뮬레이션",
        type="func",
        func_name="solution",
        description=(
            "퍼즐 게임의 보드는 R행 C열의 2차원 정수 배열 board 로 주어진다. 사용자가 회전 "
            "버튼을 k번 누르면 보드 전체가 매번 시계 방향으로 90도씩 회전한다.\n\n"
            "시계 방향 90도 회전이란, 원래 보드의 첫 번째 '행'이 결과 보드의 마지막 '열'이 "
            "되도록 돌리는 것을 말한다. 한 번 회전하면 R행 C열 보드는 C행 R열 보드가 된다.\n\n"
            "회전 횟수 k가 4의 배수면 원래 보드와 같아진다(k는 0 이상의 정수이며 매우 클 수도 "
            "있으니 유의하라). board 와 누른 횟수 k가 주어질 때, k번 회전한 최종 보드를 "
            "2차원 리스트로 반환하라."
        ),
        input_desc="board : 정수 2차원 리스트 (1 ≤ R, C ≤ 100), k : 회전 횟수 (0 ≤ k ≤ 10^9)",
        output_desc="시계 방향으로 k번 회전한 결과 보드(2차원 리스트).",
        examples=[
            {"args": [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1],
             "output": [[7, 4, 1], [8, 5, 2], [9, 6, 3]]},
            {"args": [[[1, 2], [3, 4]], 2], "output": [[4, 3], [2, 1]]},
        ],
        hints=[
            "k를 그대로 다 돌릴 필요가 없습니다. 4번 회전하면 제자리이므로 실제로 필요한 회전 수는 k를 4로 나눈 나머지뿐입니다.",
            "한 번의 시계방향 회전은 새 배열 nb[j][R-1-i] = board[i][j] 공식으로 만들 수 있습니다. 회전마다 행/열 크기가 바뀜에 유의하세요.",
            "k%=4; for _ in range(k): R,C=len(b),len(b[0]); nb=[[0]*R for _ in range(C)]; for i in range(R): for j in range(C): nb[j][R-1-i]=b[i][j]; b=nb. 마지막 b를 반환.",
        ],
        testcases=[
            {"args": [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1],
             "expected": [[7, 4, 1], [8, 5, 2], [9, 6, 3]]},
            {"args": [[[1, 2], [3, 4]], 2], "expected": [[4, 3], [2, 1]]},
            {"args": [[[1, 2, 3, 4]], 1], "expected": [[1], [2], [3], [4]]},
            {"args": [[[1, 2], [3, 4]], 0], "expected": [[1, 2], [3, 4]]},
            {"args": [[[5]], 1000000000], "expected": [[5]]},
            {"args": [[[1, 2], [3, 4], [5, 6]], 3], "expected": [[2, 4, 6], [1, 3, 5]]},
        ],
        reference_py=(
            "def solution(board, k):\n"
            "    k %= 4\n"
            "    b = [row[:] for row in board]\n"
            "    for _ in range(k):\n"
            "        R = len(b)\n"
            "        C = len(b[0])\n"
            "        nb = [[0] * R for _ in range(C)]\n"
            "        for i in range(R):\n"
            "            for j in range(C):\n"
            "                nb[j][R - 1 - i] = b[i][j]\n"
            "        b = nb\n"
            "    return b\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int[][] solution(int[][] board, int k) {\n"
            "        k %= 4;\n"
            "        int[][] b = board;\n"
            "        for (int t = 0; t < k; t++) {\n"
            "            int R = b.length, C = b[0].length;\n"
            "            int[][] nb = new int[C][R];\n"
            "            for (int i = 0; i < R; i++)\n"
            "                for (int j = 0; j < C; j++)\n"
            "                    nb[j][R - 1 - i] = b[i][j];\n"
            "            b = nb;\n"
            "        }\n"
            "        return b;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 게임판 시계방향 90도 회전을 k번 적용\n"
            "def solution(board, k):\n"
            "    answer = board\n"
            "    return answer\n"
        ),
    ),

    # ────────────────────────────────────────────────────────────
    Problem(
        id="impl-03",
        rank="Gold",
        title="색깔 블록 터뜨리기",
        style="라인",
        topic="연결요소 시뮬레이션",
        category="구현/시뮬레이션",
        type="stdin",
        description=(
            "R행 C열의 보드에 색깔 블록이 쌓여 있다. 각 칸은 알파벳 대문자(블록의 색) 또는 "
            "'.'(빈 칸)이다. 게임은 다음 규칙으로 진행된다.\n\n"
            "1) 같은 색 블록이 상하좌우로 이어져 하나의 덩어리를 이룬다. 한 덩어리의 크기가 "
            "3개 이상이면 그 덩어리의 모든 블록이 동시에 터져 사라진다(빈 칸이 된다). 같은 "
            "단계에서 크기 3 이상인 덩어리는 모두 함께 터진다.\n"
            "2) 블록이 터져 사라지면 중력이 작용한다. 각 열에서 위에 떠 있던 블록들이 아래로 "
            "떨어져 빈 칸을 메운다(열 안에서의 위아래 순서는 그대로 유지된다).\n"
            "3) 중력으로 블록이 내려온 뒤, 다시 크기 3 이상의 덩어리가 생겼다면 그 덩어리도 "
            "터진다. 더 이상 터질 덩어리가 없을 때까지 1)~2) 과정을 반복한다(연쇄 반응).\n\n"
            "행 번호는 위에서 아래로 1부터 증가하며, 중력은 행 번호가 커지는 '아래쪽'으로 "
            "작용한다. 모든 연쇄 반응이 끝났을 때까지 터져 사라진 블록의 총 개수를 구하라."
        ),
        input_desc=(
            "첫째 줄에 R C (1 ≤ R, C ≤ 30).\n"
            "다음 R개의 줄에 길이 C인 보드 문자열(대문자 또는 '.')."
        ),
        output_desc="모든 연쇄 반응이 끝날 때까지 사라진 블록의 총 개수를 한 줄에 출력.",
        examples=[
            {"input": "3 3\nAAB\nCAB\nCCB\n", "output": "9\n"},
            {"input": "2 2\nRG\nGR\n", "output": "0\n"},
        ],
        hints=[
            "매 단계마다 '터질 칸'을 먼저 모두 찾아 표시한 뒤 한꺼번에 지우고, 그다음 중력을 적용하는 순서가 중요합니다. 찾으면서 동시에 지우면 안 됩니다.",
            "BFS나 DFS로 같은 색 연결요소(덩어리)를 구해 크기 3 이상이면 제거 대상에 모읍니다. 중력은 각 열별로 남은 블록을 모아 아래에서부터 다시 채우면 됩니다.",
            "while True: visited로 모든 연결요소 탐색해 size>=3인 칸을 to_remove에 모음; to_remove가 비면 break; total+=len(to_remove); 해당 칸들을 '.'로; 각 열마다 남은 블록 리스트를 만들어 아래 행부터 채우고 위는 '.'. 마지막에 total 출력.",
        ],
        testcases=[
            {"input": "3 3\nAAB\nCAB\nCCB\n", "output": "9\n"},
            {"input": "2 2\nRG\nGR\n", "output": "0\n"},
            {"input": "3 3\nRRR\nGGR\nRGR\n", "output": "8\n"},
            {"input": "3 3\nXYY\nXYX\nXXX\n", "output": "9\n"},
            {"input": "1 5\nAABBB\n", "output": "3\n"},
            {"input": "1 1\nA\n", "output": "0\n"},
        ],
        reference_py=(
            "import sys\n"
            "from collections import deque\n"
            "def main():\n"
            "    data = sys.stdin.read().split('\\n')\n"
            "    R, C = map(int, data[0].split())\n"
            "    g = [list(data[1 + i]) for i in range(R)]\n"
            "    total = 0\n"
            "    while True:\n"
            "        visited = [[False] * C for _ in range(R)]\n"
            "        to_remove = set()\n"
            "        for i in range(R):\n"
            "            for j in range(C):\n"
            "                if g[i][j] == '.' or visited[i][j]:\n"
            "                    continue\n"
            "                color = g[i][j]\n"
            "                comp = []\n"
            "                dq = deque([(i, j)])\n"
            "                visited[i][j] = True\n"
            "                while dq:\n"
            "                    x, y = dq.popleft()\n"
            "                    comp.append((x, y))\n"
            "                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):\n"
            "                        nx, ny = x + dx, y + dy\n"
            "                        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and g[nx][ny] == color:\n"
            "                            visited[nx][ny] = True\n"
            "                            dq.append((nx, ny))\n"
            "                if len(comp) >= 3:\n"
            "                    to_remove.update(comp)\n"
            "        if not to_remove:\n"
            "            break\n"
            "        total += len(to_remove)\n"
            "        for x, y in to_remove:\n"
            "            g[x][y] = '.'\n"
            "        for col in range(C):\n"
            "            stack = [g[row][col] for row in range(R) if g[row][col] != '.']\n"
            "            for row in range(R - 1, -1, -1):\n"
            "                g[row][col] = stack.pop() if stack else '.'\n"
            "    print(total)\n"
            "main()\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int R = Integer.parseInt(st.nextToken());\n"
            "        int C = Integer.parseInt(st.nextToken());\n"
            "        char[][] g = new char[R][];\n"
            "        for (int i = 0; i < R; i++) g[i] = br.readLine().toCharArray();\n"
            "        int total = 0;\n"
            "        int[] dx = {1, -1, 0, 0}, dy = {0, 0, 1, -1};\n"
            "        while (true) {\n"
            "            boolean[][] visited = new boolean[R][C];\n"
            "            boolean[][] mark = new boolean[R][C];\n"
            "            int removed = 0;\n"
            "            for (int i = 0; i < R; i++) for (int j = 0; j < C; j++) {\n"
            "                if (g[i][j] == '.' || visited[i][j]) continue;\n"
            "                char color = g[i][j];\n"
            "                ArrayList<int[]> comp = new ArrayList<>();\n"
            "                ArrayDeque<int[]> dq = new ArrayDeque<>();\n"
            "                dq.add(new int[]{i, j}); visited[i][j] = true;\n"
            "                while (!dq.isEmpty()) {\n"
            "                    int[] c = dq.poll(); comp.add(c);\n"
            "                    for (int d = 0; d < 4; d++) {\n"
            "                        int nx = c[0] + dx[d], ny = c[1] + dy[d];\n"
            "                        if (nx >= 0 && nx < R && ny >= 0 && ny < C && !visited[nx][ny] && g[nx][ny] == color) {\n"
            "                            visited[nx][ny] = true; dq.add(new int[]{nx, ny});\n"
            "                        }\n"
            "                    }\n"
            "                }\n"
            "                if (comp.size() >= 3) for (int[] c : comp) mark[c[0]][c[1]] = true;\n"
            "            }\n"
            "            for (int i = 0; i < R; i++) for (int j = 0; j < C; j++)\n"
            "                if (mark[i][j]) { g[i][j] = '.'; removed++; }\n"
            "            if (removed == 0) break;\n"
            "            total += removed;\n"
            "            for (int col = 0; col < C; col++) {\n"
            "                ArrayList<Character> stack = new ArrayList<>();\n"
            "                for (int row = 0; row < R; row++) if (g[row][col] != '.') stack.add(g[row][col]);\n"
            "                int p = stack.size() - 1;\n"
            "                for (int row = R - 1; row >= 0; row--) g[row][col] = (p >= 0) ? stack.get(p--) : '.';\n"
            "            }\n"
            "        }\n"
            "        System.out.println(total);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "from collections import deque\n"
            "def main():\n"
            "    data = sys.stdin.read().split('\\n')\n"
            "    # R C 와 보드를 읽고, 연결요소 탐색->제거->중력 을 반복\n"
            "    pass\n"
            "main()\n"
        ),
    ),

    # ────────────────────────────────────────────────────────────
    Problem(
        id="impl-04",
        rank="Gold",
        title="주차장 요금 정산",
        style="카카오",
        topic="시간 계산 시뮬레이션",
        category="구현/시뮬레이션",
        type="func",
        func_name="solution",
        description=(
            "어느 주차장의 요금 정책과 차량들의 입출차 기록이 주어진다. 이를 바탕으로 각 "
            "차량에 청구할 주차 요금을 계산하려 한다.\n\n"
            "요금 정책은 [기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)] 형태의 "
            "리스트 fees 로 주어진다. 정산 규칙은 다음과 같다.\n"
            "  - 차량의 누적 주차 시간이 '기본 시간' 이하이면 '기본 요금'만 청구한다.\n"
            "  - 누적 주차 시간이 '기본 시간'을 초과하면, 초과한 시간에 대해 '단위 시간'으로 "
            "나누어 올림한 횟수만큼 '단위 요금'을 기본 요금에 더해 청구한다. 즉 "
            "기본요금 + ceil((누적시간 - 기본시간) / 단위시간) × 단위요금 이다.\n\n"
            "입출차 기록 records 는 \"HH:MM 차량번호 행동\" 형식의 문자열 리스트이며 시각 "
            "오름차순으로 정렬되어 있다. 행동은 \"IN\"(입차) 또는 \"OUT\"(출차)이다. 같은 "
            "차량은 입차와 출차를 번갈아 하며, 한 번 출차하면 누적 시간에 그 구간이 더해진다. "
            "어떤 차량이 출차 기록 없이 하루를 마감하면 23:59에 출차한 것으로 간주한다.\n\n"
            "차량번호가 작은 순서대로, 각 차량의 청구 요금을 정수 리스트로 반환하라."
        ),
        input_desc=(
            "fees : [기본시간, 기본요금, 단위시간, 단위요금] 정수 4개 리스트.\n"
            "records : \"HH:MM 차량번호 IN|OUT\" 형식 문자열 리스트."
        ),
        output_desc="차량번호 오름차순으로 정렬한, 각 차량의 청구 요금(원) 정수 리스트.",
        examples=[
            {"args": [[180, 5000, 10, 600],
                      ["05:34 0000 IN", "06:00 0000 OUT", "06:34 0001 IN",
                       "18:59 0001 OUT", "21:30 0001 IN", "22:59 0001 OUT",
                       "04:11 0002 IN"]],
             "output": [5000, 44600, 65600]},
            {"args": [[120, 0, 60, 591],
                      ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT",
                       "18:00 0202 OUT", "23:58 3961 IN"]],
             "output": [0, 591]},
        ],
        hints=[
            "차량별로 '현재 입차 시각'과 '누적 주차 분'을 따로 관리하면 됩니다. 시각은 HH*60+MM 으로 분 단위 정수로 바꾸면 계산이 쉽습니다.",
            "딕셔너리 두 개(입차중인 차량의 입차시각, 차량별 누적시간)를 쓰세요. 기록을 다 처리한 뒤에도 입차 상태인 차량은 23:59 출차로 누적시간에 더합니다.",
            "import math; 기록마다 IN이면 in_time[번호]=분, OUT이면 total[번호]+= (분 - in_time[번호]) 후 in_time에서 제거. 끝나고 남은 in_time은 (23*60+59 - 입차분)을 더함. 정렬된 번호마다 fee=기본요금; dur>기본시간이면 fee+=ceil((dur-기본시간)/단위시간)*단위요금.",
        ],
        testcases=[
            {"args": [[180, 5000, 10, 600],
                      ["05:34 0000 IN", "06:00 0000 OUT", "06:34 0001 IN",
                       "18:59 0001 OUT", "21:30 0001 IN", "22:59 0001 OUT",
                       "04:11 0002 IN"]],
             "expected": [5000, 44600, 65600]},
            {"args": [[120, 0, 60, 591],
                      ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT",
                       "18:00 0202 OUT", "23:58 3961 IN"]],
             "expected": [0, 591]},
            {"args": [[1, 461, 1, 10], ["00:00 1234 IN", "23:59 1234 OUT"]],
             "expected": [14841]},
            {"args": [[180, 5000, 10, 600], ["09:00 0001 IN", "11:59 0001 OUT"]],
             "expected": [5000]},
            {"args": [[60, 1000, 30, 500],
                      ["10:00 0001 IN", "10:30 0001 OUT", "12:00 0001 IN",
                       "13:01 0001 OUT"]],
             "expected": [2000]},
        ],
        reference_py=(
            "import math\n"
            "def solution(fees, records):\n"
            "    base_t, base_f, unit_t, unit_f = fees\n"
            "    in_time = {}\n"
            "    total = {}\n"
            "    for rec in records:\n"
            "        t, num, act = rec.split()\n"
            "        h, m = t.split(':')\n"
            "        minutes = int(h) * 60 + int(m)\n"
            "        if act == 'IN':\n"
            "            in_time[num] = minutes\n"
            "        else:\n"
            "            total[num] = total.get(num, 0) + (minutes - in_time[num])\n"
            "            del in_time[num]\n"
            "    for num, t in in_time.items():\n"
            "        total[num] = total.get(num, 0) + (23 * 60 + 59 - t)\n"
            "    answer = []\n"
            "    for num in sorted(total.keys()):\n"
            "        dur = total[num]\n"
            "        fee = base_f\n"
            "        if dur > base_t:\n"
            "            fee += math.ceil((dur - base_t) / unit_t) * unit_f\n"
            "        answer.append(fee)\n"
            "    return answer\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int[] solution(int[] fees, String[] records) {\n"
            "        int baseT = fees[0], baseF = fees[1], unitT = fees[2], unitF = fees[3];\n"
            "        Map<String, Integer> inTime = new HashMap<>();\n"
            "        Map<String, Integer> total = new TreeMap<>();\n"
            "        for (String rec : records) {\n"
            "            String[] p = rec.split(\" \");\n"
            "            String[] hm = p[0].split(\":\");\n"
            "            int minutes = Integer.parseInt(hm[0]) * 60 + Integer.parseInt(hm[1]);\n"
            "            String num = p[1];\n"
            "            if (p[2].equals(\"IN\")) {\n"
            "                inTime.put(num, minutes);\n"
            "            } else {\n"
            "                total.merge(num, minutes - inTime.get(num), Integer::sum);\n"
            "                inTime.remove(num);\n"
            "            }\n"
            "        }\n"
            "        for (Map.Entry<String, Integer> e : inTime.entrySet())\n"
            "            total.merge(e.getKey(), 23 * 60 + 59 - e.getValue(), Integer::sum);\n"
            "        int[] answer = new int[total.size()];\n"
            "        int i = 0;\n"
            "        for (int dur : total.values()) {\n"
            "            int fee = baseF;\n"
            "            if (dur > baseT) fee += (int) Math.ceil((dur - baseT) / (double) unitT) * unitF;\n"
            "            answer[i++] = fee;\n"
            "        }\n"
            "        return answer;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import math\n"
            "# 주차장 요금 정산: 차량번호 오름차순으로 요금 리스트 반환\n"
            "def solution(fees, records):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

    # ────────────────────────────────────────────────────────────
    Problem(
        id="impl-05",
        rank="Silver",
        title="반복 문자열 압축",
        style="카카오",
        topic="문자열 처리",
        category="구현/시뮬레이션",
        type="func",
        func_name="solution",
        description=(
            "데이터 전송량을 줄이기 위해 문자열을 압축하려 한다. 압축 방식은 다음과 같다.\n\n"
            "문자열을 앞에서부터 정해진 길이의 '토막' 단위로 잘라, 같은 토막이 연속해서 "
            "반복되면 (반복 횟수 + 토막 한 개)로 줄여 적는다. 예를 들어 \"aaaaa\"를 길이 1 "
            "토막으로 자르면 'a'가 5번 반복되므로 \"5a\"(길이 2)로 압축된다. 반복 횟수가 "
            "1인 토막은 숫자를 붙이지 않고 토막만 적는다(예: 'a' 한 개는 그냥 \"a\").\n\n"
            "토막의 길이는 1부터 문자열 길이의 절반까지 모두 시도해 볼 수 있으며, 그중 "
            "압축 결과(문자 수)가 가장 짧아지는 길이를 골라 압축한다. 단, 토막은 반드시 "
            "문자열의 맨 앞에서부터 같은 길이로 잘라야 한다.\n\n"
            "압축할 문자열 s가 주어질 때, 위 방식으로 만들 수 있는 가장 짧은 압축 결과의 "
            "길이(문자 수)를 반환하라. 길이가 1인 문자열은 압축할 수 없으므로 결과 길이는 "
            "1이다."
        ),
        input_desc="s : 알파벳 소문자로 이루어진 문자열 (1 ≤ len(s) ≤ 1000)",
        output_desc="가능한 모든 토막 길이로 압축했을 때 나올 수 있는 가장 짧은 길이(정수).",
        examples=[
            {"args": ["aabbaccc"], "output": 7},
            {"args": ["ababcdcdababcdcd"], "output": 9},
        ],
        hints=[
            "토막 길이를 1부터 len(s)//2 까지 하나씩 고정해 보고, 각 경우의 압축 길이를 모두 구한 다음 최솟값을 고르면 됩니다. 길이 1 문자열은 그냥 1입니다.",
            "고정한 토막 길이로 문자열을 잘라가며 '직전 토막'과 같은지 비교해 연속 횟수를 셉니다. 토막이 바뀔 때마다 (횟수가 2 이상이면 숫자 자릿수) + (토막 길이)를 누적하세요.",
            "best=len(s); for unit in 1..len(s)//2: cnt=1, prev=s[0:unit], comp=0; for i in range(unit,len(s),unit): cur=s[i:i+unit]; 같으면 cnt+=1 else comp+=(len(str(cnt)) if cnt>1 else 0)+unit, prev=cur, cnt=1; 루프 후 마지막 토막도 동일하게 더함; best=min(best,comp). best 반환.",
        ],
        testcases=[
            {"args": ["aabbaccc"], "expected": 7},
            {"args": ["ababcdcdababcdcd"], "expected": 9},
            {"args": ["abcabcdede"], "expected": 8},
            {"args": ["aaaaa"], "expected": 2},
            {"args": ["xababcdcdababcdcd"], "expected": 17},
            {"args": ["a"], "expected": 1},
        ],
        reference_py=(
            "def solution(s):\n"
            "    n = len(s)\n"
            "    best = n\n"
            "    for unit in range(1, n // 2 + 1):\n"
            "        comp = 0\n"
            "        prev = s[0:unit]\n"
            "        cnt = 1\n"
            "        for i in range(unit, n, unit):\n"
            "            cur = s[i:i + unit]\n"
            "            if cur == prev:\n"
            "                cnt += 1\n"
            "            else:\n"
            "                comp += (len(str(cnt)) if cnt > 1 else 0) + len(prev)\n"
            "                prev = cur\n"
            "                cnt = 1\n"
            "        comp += (len(str(cnt)) if cnt > 1 else 0) + len(prev)\n"
            "        best = min(best, comp)\n"
            "    return best\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(String s) {\n"
            "        int n = s.length();\n"
            "        int best = n;\n"
            "        for (int unit = 1; unit <= n / 2; unit++) {\n"
            "            int comp = 0, cnt = 1;\n"
            "            String prev = s.substring(0, Math.min(unit, n));\n"
            "            for (int i = unit; i < n; i += unit) {\n"
            "                String cur = s.substring(i, Math.min(i + unit, n));\n"
            "                if (cur.equals(prev)) {\n"
            "                    cnt++;\n"
            "                } else {\n"
            "                    comp += (cnt > 1 ? String.valueOf(cnt).length() : 0) + prev.length();\n"
            "                    prev = cur;\n"
            "                    cnt = 1;\n"
            "                }\n"
            "            }\n"
            "            comp += (cnt > 1 ? String.valueOf(cnt).length() : 0) + prev.length();\n"
            "            best = Math.min(best, comp);\n"
            "        }\n"
            "        return best;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 반복 문자열 압축: 가장 짧은 압축 길이 반환\n"
            "def solution(s):\n"
            "    answer = len(s)\n"
            "    return answer\n"
        ),
    ),

]
