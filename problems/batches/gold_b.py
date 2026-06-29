"""골드 추가 배치 B — 그래프 탐색(BFS/DFS)과 백트래킹 15문제.

gold-21 ~ gold-35.
base 의 미로 BFS(gold-02)와 주제가 겹치지 않도록 구성했다.
"""

from engine.models import Problem

RANK = "Gold"

PROBLEMS = [

    Problem(
        id="gold-21",
        rank="Gold",
        title="연결 요소의 개수",
        style="백준",
        topic="그래프 탐색",
        type="stdin",
        description=(
            "방향 없는 그래프가 주어졌을 때, 연결 요소(서로 이어진 정점들의 묶음)의 개수를 "
            "구하시오. 정점은 1번부터 N번까지 번호가 매겨져 있다."
        ),
        input_desc=(
            "첫째 줄에 정점의 개수 N과 간선의 개수 M (1 ≤ N ≤ 1000, 0 ≤ M ≤ N·(N-1)/2). "
            "다음 M개의 줄에 간선의 양 끝점 u v 가 주어진다."
        ),
        output_desc="첫째 줄에 연결 요소의 개수를 출력한다.",
        examples=[
            {"input": "6 5\n1 2\n2 5\n5 1\n3 4\n4 6\n", "output": "2\n"},
            {"input": "6 8\n1 2\n2 5\n5 1\n3 4\n4 6\n5 4\n2 4\n2 3\n", "output": "1\n"},
        ],
        hints=[
            "아직 방문하지 않은 정점에서 탐색을 시작할 때마다 새로운 연결 요소가 하나 생깁니다.",
            "인접 리스트를 만든 뒤 BFS(또는 DFS)로 한 덩어리를 모두 방문 처리하고, 시작 횟수를 세면 됩니다.",
            "for s in 1..N: if not visited[s]: cnt+=1; BFS로 s가 속한 덩어리 전체를 방문 처리. 답은 cnt.",
        ],
        testcases=[
            {"input": "6 5\n1 2\n2 5\n5 1\n3 4\n4 6\n", "output": "2\n"},
            {"input": "6 8\n1 2\n2 5\n5 1\n3 4\n4 6\n5 4\n2 4\n2 3\n", "output": "1\n"},
            {"input": "1 0\n", "output": "1\n"},
            {"input": "5 0\n", "output": "5\n"},
            {"input": "4 2\n1 2\n3 4\n", "output": "2\n"},
        ],
        reference_py=r'''import sys
from collections import deque
input = sys.stdin.readline
def main():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    visited = [False] * (n + 1)
    cnt = 0
    for s in range(1, n + 1):
        if not visited[s]:
            cnt += 1
            visited[s] = True
            q = deque([s])
            while q:
                x = q.popleft()
                for y in adj[x]:
                    if not visited[y]:
                        visited[y] = True
                        q.append(y)
    print(cnt)
main()
''',
        reference_java=r'''import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i <= n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            adj.get(u).add(v);
            adj.get(v).add(u);
        }
        boolean[] visited = new boolean[n + 1];
        int cnt = 0;
        for (int s = 1; s <= n; s++) {
            if (!visited[s]) {
                cnt++;
                visited[s] = true;
                ArrayDeque<Integer> q = new ArrayDeque<>();
                q.add(s);
                while (!q.isEmpty()) {
                    int x = q.poll();
                    for (int y : adj.get(x)) {
                        if (!visited[y]) { visited[y] = true; q.add(y); }
                    }
                }
            }
        }
        System.out.println(cnt);
    }
}
''',
        template_py=r'''import sys
from collections import deque
input = sys.stdin.readline
# 연결 요소의 개수
def main():
    n, m = map(int, input().split())
    # 인접 리스트를 만들고, 방문하지 않은 정점에서 탐색을 시작하세요.
    pass
main()
''',
    ),

    Problem(
        id="gold-22",
        rank="Gold",
        title="섬의 개수 (8방향)",
        style="해외대기업",
        topic="DFS/BFS",
        type="func",
        func_name="solution",
        description=(
            "0과 1로 이루어진 2차원 격자 grid 가 주어진다. 1은 땅, 0은 바다이다. "
            "상하좌우와 대각선(8방향)으로 이어진 1들의 묶음을 하나의 섬이라 할 때, "
            "섬의 개수를 반환하세요."
        ),
        input_desc="grid : 0/1 로 이루어진 2차원 리스트(list[list[int]]).",
        output_desc="섬의 개수 (int).",
        examples=[
            {"args": [[[1, 1, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 1]]], "output": 2},
            {"args": [[[1, 0, 1], [0, 0, 0], [1, 0, 1]]], "output": 4},
        ],
        hints=[
            "땅 칸 하나를 만나면 그와 8방향으로 이어진 모든 땅을 한 섬으로 묶어 표시하세요.",
            "방문하지 않은 1을 찾을 때마다 섬 개수를 +1 하고, 그 자리에서 8방향 DFS/BFS로 전부 방문 처리합니다.",
            "이중 for 로 격자를 훑다가 grid[i][j]==1 이고 미방문이면 cnt+=1 후 8방향 탐색으로 같은 섬을 모두 방문. 답은 cnt.",
        ],
        testcases=[
            {"args": [[[1, 1, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 1]]], "expected": 2},
            {"args": [[[1, 0, 1], [0, 0, 0], [1, 0, 1]]], "expected": 4},
            {"args": [[[0, 0], [0, 0]]], "expected": 0},
            {"args": [[[1]]], "expected": 1},
            {"args": [[[1, 1, 1, 1, 1]]], "expected": 1},
        ],
        reference_py=r'''from collections import deque
def solution(grid):
    if not grid or not grid[0]:
        return 0
    n = len(grid)
    m = len(grid[0])
    visited = [[False] * m for _ in range(n)]
    dirs = [(dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1) if not (dx == 0 and dy == 0)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                cnt += 1
                visited[i][j] = True
                q = deque([(i, j)])
                while q:
                    x, y = q.popleft()
                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))
    return cnt
''',
        reference_java=r'''import java.util.*;
class Solution {
    public int solution(int[][] grid) {
        if (grid.length == 0 || grid[0].length == 0) return 0;
        int n = grid.length, m = grid[0].length, cnt = 0;
        boolean[][] visited = new boolean[n][m];
        int[] dx = {-1,-1,-1,0,0,1,1,1};
        int[] dy = {-1,0,1,-1,1,-1,0,1};
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 1 && !visited[i][j]) {
                    cnt++;
                    visited[i][j] = true;
                    ArrayDeque<int[]> q = new ArrayDeque<>();
                    q.add(new int[]{i, j});
                    while (!q.isEmpty()) {
                        int[] c = q.poll();
                        for (int d = 0; d < 8; d++) {
                            int nx = c[0] + dx[d], ny = c[1] + dy[d];
                            if (nx >= 0 && nx < n && ny >= 0 && ny < m && grid[nx][ny] == 1 && !visited[nx][ny]) {
                                visited[nx][ny] = true;
                                q.add(new int[]{nx, ny});
                            }
                        }
                    }
                }
            }
        }
        return cnt;
    }
}
''',
        template_py=r'''# 섬의 개수 (8방향 연결 요소)
def solution(grid):
    answer = 0
    return answer
''',
    ),

    Problem(
        id="gold-23",
        rank="Gold",
        title="단지번호붙이기",
        style="백준",
        topic="DFS",
        type="stdin",
        description=(
            "정사각형 지도가 있다. 1은 집이 있는 칸, 0은 집이 없는 칸이다. 상하좌우로 이어진 "
            "집들의 모임을 하나의 단지라 한다. 단지의 수와 각 단지에 속한 집의 수를 "
            "오름차순으로 정렬해 출력하시오."
        ),
        input_desc=(
            "첫째 줄에 지도의 한 변의 길이 N (1 ≤ N ≤ 25). 다음 N개의 줄에 0과 1로 이루어진 "
            "길이 N 의 문자열이 주어진다."
        ),
        output_desc=(
            "첫째 줄에 단지 수를 출력하고, 둘째 줄부터 각 단지의 집 수를 오름차순으로 한 줄에 "
            "하나씩 출력한다."
        ),
        examples=[
            {
                "input": "7\n0110100\n0110101\n1110101\n0000101\n0111101\n0100101\n0011101\n",
                "output": "3\n6\n7\n13\n",
            },
            {"input": "3\n111\n000\n111\n", "output": "2\n3\n3\n"},
        ],
        hints=[
            "집 칸에서 시작해 상하좌우로 이어진 집들을 모두 세면 한 단지의 크기를 알 수 있습니다.",
            "미방문 집을 만날 때마다 BFS/DFS로 단지 하나의 크기를 센 뒤 리스트에 담고, 마지막에 정렬합니다.",
            "sizes=[]; 격자 순회 중 미방문 '1' 발견 시 탐색으로 cnt 세서 sizes.append(cnt). 끝에 sizes.sort(); 단지 수와 각 크기 출력.",
        ],
        testcases=[
            {
                "input": "7\n0110100\n0110101\n1110101\n0000101\n0111101\n0100101\n0011101\n",
                "output": "3\n6\n7\n13\n",
            },
            {"input": "3\n111\n000\n111\n", "output": "2\n3\n3\n"},
            {"input": "1\n0\n", "output": "0\n"},
            {"input": "1\n1\n", "output": "1\n1\n"},
            {"input": "5\n00000\n00000\n00000\n00000\n00000\n", "output": "0\n"},
        ],
        reference_py=r'''import sys
from collections import deque
input = sys.stdin.readline
def main():
    n = int(input())
    g = [list(input().strip()) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    sizes = []
    for i in range(n):
        for j in range(n):
            if g[i][j] == '1' and not visited[i][j]:
                visited[i][j] = True
                q = deque([(i, j)])
                cnt = 0
                while q:
                    x, y = q.popleft()
                    cnt += 1
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n and g[nx][ny] == '1' and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                sizes.append(cnt)
    sizes.sort()
    print(len(sizes))
    for s in sizes:
        print(s)
main()
''',
        reference_java=r'''import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        char[][] g = new char[n][];
        for (int i = 0; i < n; i++) g[i] = br.readLine().trim().toCharArray();
        boolean[][] visited = new boolean[n][n];
        List<Integer> sizes = new ArrayList<>();
        int[] dx = {1,-1,0,0}, dy = {0,0,1,-1};
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (g[i][j] == '1' && !visited[i][j]) {
                    visited[i][j] = true;
                    ArrayDeque<int[]> q = new ArrayDeque<>();
                    q.add(new int[]{i, j});
                    int cnt = 0;
                    while (!q.isEmpty()) {
                        int[] c = q.poll();
                        cnt++;
                        for (int d = 0; d < 4; d++) {
                            int nx = c[0]+dx[d], ny = c[1]+dy[d];
                            if (nx>=0&&nx<n&&ny>=0&&ny<n&&g[nx][ny]=='1'&&!visited[nx][ny]) {
                                visited[nx][ny] = true;
                                q.add(new int[]{nx, ny});
                            }
                        }
                    }
                    sizes.add(cnt);
                }
            }
        }
        Collections.sort(sizes);
        StringBuilder sb = new StringBuilder();
        sb.append(sizes.size()).append("\n");
        for (int s : sizes) sb.append(s).append("\n");
        System.out.print(sb);
    }
}
''',
        template_py=r'''import sys
from collections import deque
input = sys.stdin.readline
# 단지번호붙이기
def main():
    n = int(input())
    # 각 단지의 크기를 구해 정렬 후 출력하세요.
    pass
main()
''',
    ),

    Problem(
        id="gold-24",
        rank="Gold",
        title="토마토 익히기",
        style="대기업",
        topic="다중 시작 BFS",
        type="stdin",
        description=(
            "창고에 격자 모양으로 토마토가 들어 있다. 1은 익은 토마토, 0은 익지 않은 토마토, "
            "-1은 토마토가 없는 칸이다. 하루가 지나면 익은 토마토의 상하좌우 인접한 익지 않은 "
            "토마토가 익는다. 모든 토마토가 익기까지의 최소 일수를 구하시오. 이미 모두 익어 있으면 0, "
            "끝내 모두 익지 못하면 -1을 출력한다."
        ),
        input_desc=(
            "첫째 줄에 가로 칸 수 M과 세로 칸 수 N (1 ≤ M, N ≤ 1000). 다음 N개의 줄에 각 "
            "M개의 정수(1/0/-1)가 공백으로 구분되어 주어진다."
        ),
        output_desc="모든 토마토가 익는 최소 일수. 불가능하면 -1, 이미 다 익었으면 0.",
        examples=[
            {
                "input": "6 4\n0 0 0 0 0 0\n0 0 0 0 0 0\n0 0 0 0 0 0\n0 0 0 0 0 1\n",
                "output": "8\n",
            },
            {
                "input": "6 4\n0 -1 0 0 0 0\n-1 0 0 0 0 0\n0 0 0 0 0 0\n0 0 0 0 0 1\n",
                "output": "-1\n",
            },
        ],
        hints=[
            "이미 익은 모든 토마토에서 동시에 한 칸씩 번져나가는 상황입니다. 시작점이 여러 개인 BFS를 떠올리세요.",
            "처음에 익은 토마토 좌표를 모두 큐에 넣고 BFS를 돌리면, 각 칸이 익는 날짜가 곧 거리(레벨)가 됩니다.",
            "익은 칸 전부를 큐에 넣고 레벨 단위 BFS로 0인 칸을 익히며 days 증가. 끝나고 0이 남으면 -1, 아니면 마지막 days.",
        ],
        testcases=[
            {
                "input": "6 4\n0 0 0 0 0 0\n0 0 0 0 0 0\n0 0 0 0 0 0\n0 0 0 0 0 1\n",
                "output": "8\n",
            },
            {
                "input": "6 4\n0 -1 0 0 0 0\n-1 0 0 0 0 0\n0 0 0 0 0 0\n0 0 0 0 0 1\n",
                "output": "-1\n",
            },
            {"input": "2 2\n1 1\n1 1\n", "output": "0\n"},
            {"input": "1 1\n0\n", "output": "-1\n"},
            {"input": "2 1\n1 0\n", "output": "1\n"},
            {"input": "3 2\n1 0 0\n0 0 0\n", "output": "3\n"},
        ],
        reference_py=r'''import sys
from collections import deque
input = sys.stdin.readline
def main():
    m, n = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(m):
            if g[i][j] == 1:
                q.append((i, j))
    days = 0
    while q:
        nq = deque()
        while q:
            x, y = q.popleft()
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == 0:
                    g[nx][ny] = 1
                    nq.append((nx, ny))
        if nq:
            days += 1
        q = nq
    for row in g:
        if 0 in row:
            print(-1)
            return
    print(days)
main()
''',
        reference_java=r'''import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        int[][] g = new int[n][m];
        ArrayDeque<int[]> q = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                g[i][j] = Integer.parseInt(st.nextToken());
                if (g[i][j] == 1) q.add(new int[]{i, j});
            }
        }
        int[] dx = {1,-1,0,0}, dy = {0,0,1,-1};
        int days = 0;
        while (!q.isEmpty()) {
            ArrayDeque<int[]> nq = new ArrayDeque<>();
            while (!q.isEmpty()) {
                int[] c = q.poll();
                for (int d = 0; d < 4; d++) {
                    int nx = c[0]+dx[d], ny = c[1]+dy[d];
                    if (nx>=0&&nx<n&&ny>=0&&ny<m&&g[nx][ny]==0) {
                        g[nx][ny] = 1;
                        nq.add(new int[]{nx, ny});
                    }
                }
            }
            if (!nq.isEmpty()) days++;
            q = nq;
        }
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                if (g[i][j] == 0) { System.out.println(-1); return; }
        System.out.println(days);
    }
}
''',
        template_py=r'''import sys
from collections import deque
input = sys.stdin.readline
# 토마토 익히기 (다중 시작 BFS)
def main():
    m, n = map(int, input().split())
    # 익은 토마토 좌표를 모두 큐에 넣고 레벨 단위 BFS를 돌리세요.
    pass
main()
''',
    ),

    Problem(
        id="gold-25",
        rank="Gold",
        title="벽 부수고 이동하기",
        style="백준",
        topic="BFS",
        type="stdin",
        description=(
            "N×M 격자 지도에서 0은 이동 가능한 칸, 1은 벽이다. (1,1)에서 (N,M)까지 상하좌우로 "
            "이동하되, 벽을 정확히 한 번까지 부수고 지나갈 수 있다. 지나는 칸 수(시작·도착 포함)가 "
            "가장 적은 경로의 칸 수를 구하시오. 불가능하면 -1을 출력한다."
        ),
        input_desc=(
            "첫째 줄에 N M (1 ≤ N, M ≤ 1000). 다음 N개의 줄에 0과 1로 이루어진 길이 M 문자열이 "
            "주어진다. (1,1)과 (N,M)은 0이다."
        ),
        output_desc="최소 칸 수. 도달할 수 없으면 -1.",
        examples=[
            {"input": "3 3\n010\n010\n010\n", "output": "5\n"},
            {
                "input": "6 4\n010010\n010010\n010010\n010010\n010010\n010010\n",
                "output": "9\n",
            },
        ],
        hints=[
            "단순 최단거리에 '벽을 아직 부쉈는가'라는 상태가 하나 더 붙습니다. 위치만이 아니라 (행, 열, 부순여부)를 한 상태로 보세요.",
            "방문 배열을 visited[x][y][0/1] 로 두고, 부순 적이 있는지 여부까지 포함해 BFS를 돌립니다.",
            "벽(1)이면 아직 안 부쉈을 때만(b==0) 부수고 b=1 상태로 이동, 길(0)이면 같은 b 상태로 이동. (N,M) 도달 시 거리 출력, 끝까지 못 가면 -1.",
        ],
        testcases=[
            {"input": "3 3\n010\n010\n010\n", "output": "5\n"},
            {"input": "1 1\n0\n", "output": "1\n"},
            {"input": "2 2\n01\n00\n", "output": "3\n"},
            {"input": "2 2\n01\n10\n", "output": "3\n"},
            {"input": "2 2\n01\n11\n", "output": "-1\n"},
            {
                "input": "6 4\n010010\n010010\n010010\n010010\n010010\n010010\n",
                "output": "9\n",
            },
        ],
        reference_py=r'''import sys
from collections import deque
input = sys.stdin.readline
def main():
    n, m = map(int, input().split())
    g = [input().strip() for _ in range(n)]
    visited = [[[False, False] for _ in range(m)] for _ in range(n)]
    q = deque([(0, 0, 0, 1)])
    visited[0][0][0] = True
    while q:
        x, y, b, d = q.popleft()
        if x == n - 1 and y == m - 1:
            print(d)
            return
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if g[nx][ny] == '0' and not visited[nx][ny][b]:
                    visited[nx][ny][b] = True
                    q.append((nx, ny, b, d + 1))
                elif g[nx][ny] == '1' and b == 0 and not visited[nx][ny][1]:
                    visited[nx][ny][1] = True
                    q.append((nx, ny, 1, d + 1))
    print(-1)
main()
''',
        reference_java=r'''import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        char[][] g = new char[n][];
        for (int i = 0; i < n; i++) g[i] = br.readLine().trim().toCharArray();
        boolean[][][] visited = new boolean[n][m][2];
        ArrayDeque<int[]> q = new ArrayDeque<>();
        q.add(new int[]{0, 0, 0, 1});
        visited[0][0][0] = true;
        int[] dx = {1,-1,0,0}, dy = {0,0,1,-1};
        while (!q.isEmpty()) {
            int[] c = q.poll();
            int x = c[0], y = c[1], b = c[2], d = c[3];
            if (x == n - 1 && y == m - 1) { System.out.println(d); return; }
            for (int dir = 0; dir < 4; dir++) {
                int nx = x + dx[dir], ny = y + dy[dir];
                if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                if (g[nx][ny] == '0' && !visited[nx][ny][b]) {
                    visited[nx][ny][b] = true;
                    q.add(new int[]{nx, ny, b, d + 1});
                } else if (g[nx][ny] == '1' && b == 0 && !visited[nx][ny][1]) {
                    visited[nx][ny][1] = true;
                    q.add(new int[]{nx, ny, 1, d + 1});
                }
            }
        }
        System.out.println(-1);
    }
}
''',
        template_py=r'''import sys
from collections import deque
input = sys.stdin.readline
# 벽 부수고 이동하기 (상태 BFS)
def main():
    n, m = map(int, input().split())
    # visited[x][y][부순여부] 로 상태를 구분해 BFS 하세요.
    pass
main()
''',
    ),

    Problem(
        id="gold-26",
        rank="Gold",
        title="N과 M (순열)",
        style="백준",
        topic="백트래킹",
        type="stdin",
        description=(
            "자연수 N과 M이 주어졌을 때, 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 "
            "수열을 모두 구하시오. 같은 수를 두 번 이상 고를 수 없으며, 고른 순서가 다르면 다른 "
            "수열이다."
        ),
        input_desc="첫째 줄에 N과 M (1 ≤ M ≤ N ≤ 8).",
        output_desc=(
            "한 줄에 하나씩, 길이 M의 수열을 공백으로 구분해 출력한다. 사전 순으로 증가하는 "
            "순서로 출력한다."
        ),
        examples=[
            {"input": "3 1\n", "output": "1\n2\n3\n"},
            {"input": "2 2\n", "output": "1 2\n2 1\n"},
        ],
        hints=[
            "M자리를 앞에서부터 한 칸씩 채우되, 이미 쓴 수는 다시 쓰지 않도록 표시하며 채웁니다.",
            "사용 여부 배열 used 를 두고 깊이 우선으로 수를 고르는 백트래킹을 사용하세요.",
            "고른 길이가 M이면 출력. 아니면 i=1..N 중 used[i]가 아니면 표시 후 재귀, 돌아오면 표시 해제. 1부터 순서대로 고르면 사전 순이 됩니다.",
        ],
        testcases=[
            {"input": "3 1\n", "output": "1\n2\n3\n"},
            {"input": "2 2\n", "output": "1 2\n2 1\n"},
            {"input": "1 1\n", "output": "1\n"},
            {"input": "3 3\n", "output": "1 2 3\n1 3 2\n2 1 3\n2 3 1\n3 1 2\n3 2 1\n"},
            {
                "input": "4 2\n",
                "output": "1 2\n1 3\n1 4\n2 1\n2 3\n2 4\n3 1\n3 2\n3 4\n4 1\n4 2\n4 3\n",
            },
        ],
        reference_py=r'''import sys
input = sys.stdin.readline
def main():
    n, m = map(int, input().split())
    res = []
    chosen = []
    used = [False] * (n + 1)
    def bt():
        if len(chosen) == m:
            res.append(' '.join(map(str, chosen)))
            return
        for i in range(1, n + 1):
            if not used[i]:
                used[i] = True
                chosen.append(i)
                bt()
                chosen.pop()
                used[i] = False
    bt()
    print('\n'.join(res))
main()
''',
        reference_java=r'''import java.util.*;
import java.io.*;
public class Main {
    static int n, m;
    static boolean[] used;
    static int[] chosen;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        used = new boolean[n + 1];
        chosen = new int[m];
        bt(0);
        System.out.print(sb);
    }
    static void bt(int depth) {
        if (depth == m) {
            for (int i = 0; i < m; i++) {
                sb.append(chosen[i]);
                if (i < m - 1) sb.append(' ');
            }
            sb.append('\n');
            return;
        }
        for (int i = 1; i <= n; i++) {
            if (!used[i]) {
                used[i] = true;
                chosen[depth] = i;
                bt(depth + 1);
                used[i] = false;
            }
        }
    }
}
''',
        template_py=r'''import sys
input = sys.stdin.readline
# N과 M (순열)
def main():
    n, m = map(int, input().split())
    # used 배열을 이용한 백트래킹으로 모든 수열을 만드세요.
    pass
main()
''',
    ),

    Problem(
        id="gold-27",
        rank="Gold",
        title="N과 M (조합)",
        style="프로그래머스",
        topic="백트래킹",
        type="stdin",
        description=(
            "자연수 N과 M이 주어졌을 때, 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 "
            "수열을 모두 구하시오. 단, 고른 수열은 오름차순이어야 한다(즉 조합)."
        ),
        input_desc="첫째 줄에 N과 M (1 ≤ M ≤ N ≤ 8).",
        output_desc=(
            "한 줄에 하나씩, 오름차순으로 고른 길이 M의 수열을 공백으로 구분해 출력한다. "
            "사전 순으로 증가하는 순서로 출력한다."
        ),
        examples=[
            {"input": "3 2\n", "output": "1 2\n1 3\n2 3\n"},
            {"input": "4 4\n", "output": "1 2 3 4\n"},
        ],
        hints=[
            "오름차순 조합이므로, 다음에 고를 수는 항상 '직전에 고른 수보다 큰' 수여야 합니다.",
            "탐색 시작 인덱스 start 를 넘겨, i 를 고르면 다음 재귀는 i+1 부터 고르게 하는 백트래킹을 쓰세요.",
            "bt(start): 길이가 M이면 출력. 아니면 for i in range(start, N+1): 고르고 bt(i+1) 재귀. bt(1) 로 시작하면 사전 순.",
        ],
        testcases=[
            {"input": "3 2\n", "output": "1 2\n1 3\n2 3\n"},
            {"input": "4 4\n", "output": "1 2 3 4\n"},
            {"input": "1 1\n", "output": "1\n"},
            {
                "input": "4 2\n",
                "output": "1 2\n1 3\n1 4\n2 3\n2 4\n3 4\n",
            },
            {
                "input": "5 3\n",
                "output": "1 2 3\n1 2 4\n1 2 5\n1 3 4\n1 3 5\n1 4 5\n2 3 4\n2 3 5\n2 4 5\n3 4 5\n",
            },
        ],
        reference_py=r'''import sys
input = sys.stdin.readline
def main():
    n, m = map(int, input().split())
    res = []
    chosen = []
    def bt(start):
        if len(chosen) == m:
            res.append(' '.join(map(str, chosen)))
            return
        for i in range(start, n + 1):
            chosen.append(i)
            bt(i + 1)
            chosen.pop()
    bt(1)
    print('\n'.join(res))
main()
''',
        reference_java=r'''import java.util.*;
import java.io.*;
public class Main {
    static int n, m;
    static int[] chosen;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        chosen = new int[m];
        bt(1, 0);
        System.out.print(sb);
    }
    static void bt(int start, int depth) {
        if (depth == m) {
            for (int i = 0; i < m; i++) {
                sb.append(chosen[i]);
                if (i < m - 1) sb.append(' ');
            }
            sb.append('\n');
            return;
        }
        for (int i = start; i <= n; i++) {
            chosen[depth] = i;
            bt(i + 1, depth + 1);
        }
    }
}
''',
        template_py=r'''import sys
input = sys.stdin.readline
# N과 M (조합)
def main():
    n, m = map(int, input().split())
    # 시작 인덱스를 넘기는 백트래킹으로 오름차순 조합을 만드세요.
    pass
main()
''',
    ),

    Problem(
        id="gold-28",
        rank="Gold",
        title="N-퀸 배치 가짓수",
        style="해외대기업",
        topic="백트래킹",
        type="func",
        func_name="solution",
        description=(
            "N×N 체스판에 N개의 퀸을, 서로 공격할 수 없도록 놓는 경우의 수를 구하세요. "
            "퀸은 같은 행, 같은 열, 같은 대각선에 있는 다른 퀸을 공격한다."
        ),
        input_desc="n : 체스판의 크기이자 퀸의 개수 (1 ≤ n ≤ 12).",
        output_desc="서로 공격하지 않게 N개의 퀸을 배치하는 경우의 수 (int).",
        examples=[
            {"args": [4], "output": 2},
            {"args": [8], "output": 92},
        ],
        hints=[
            "한 행에 퀸을 하나씩 놓는다고 생각하면, 각 행마다 어떤 열에 놓을지만 정하면 됩니다.",
            "열 사용 여부와 두 방향 대각선(행+열, 행-열) 사용 여부를 표시하며 행 단위로 백트래킹하세요.",
            "bt(r): r==n 이면 경우의 수 +1. 아니면 c=0..n-1 중 열·대각선이 모두 비어 있으면 표시 후 bt(r+1), 복귀 시 표시 해제.",
        ],
        testcases=[
            {"args": [1], "expected": 1},
            {"args": [2], "expected": 0},
            {"args": [3], "expected": 0},
            {"args": [4], "expected": 2},
            {"args": [5], "expected": 10},
            {"args": [8], "expected": 92},
        ],
        reference_py=r'''def solution(n):
    cols = [False] * n
    diag1 = [False] * (2 * n)
    diag2 = [False] * (2 * n)
    count = 0
    def bt(r):
        nonlocal count
        if r == n:
            count += 1
            return
        for c in range(n):
            if not cols[c] and not diag1[r + c] and not diag2[r - c + n]:
                cols[c] = diag1[r + c] = diag2[r - c + n] = True
                bt(r + 1)
                cols[c] = diag1[r + c] = diag2[r - c + n] = False
    bt(0)
    return count
''',
        reference_java=r'''class Solution {
    int n, count = 0;
    boolean[] cols, diag1, diag2;
    public int solution(int n) {
        this.n = n;
        cols = new boolean[n];
        diag1 = new boolean[2 * n];
        diag2 = new boolean[2 * n];
        bt(0);
        return count;
    }
    void bt(int r) {
        if (r == n) { count++; return; }
        for (int c = 0; c < n; c++) {
            if (!cols[c] && !diag1[r + c] && !diag2[r - c + n]) {
                cols[c] = diag1[r + c] = diag2[r - c + n] = true;
                bt(r + 1);
                cols[c] = diag1[r + c] = diag2[r - c + n] = false;
            }
        }
    }
}
''',
        template_py=r'''# N-퀸 배치 가짓수 (백트래킹)
def solution(n):
    answer = 0
    return answer
''',
    ),

    Problem(
        id="gold-29",
        rank="Gold",
        title="부분수열의 합 가짓수",
        style="백준",
        topic="백트래킹",
        type="func",
        func_name="solution",
        description=(
            "정수 배열 nums 와 정수 S 가 주어진다. nums 의 원소 중 하나 이상을 골라 만든 "
            "부분수열 중에서, 고른 원소들의 합이 정확히 S 가 되는 경우의 수를 반환하세요. "
            "(같은 값이라도 서로 다른 위치의 원소는 다른 것으로 본다.)"
        ),
        input_desc="nums : 정수 리스트 (1 ≤ len ≤ 20), S : 목표 합(정수).",
        output_desc="합이 S 가 되는, 크기가 1 이상인 부분수열의 개수 (int).",
        examples=[
            {"args": [[1, 2, 3], 3], "output": 2},
            {"args": [[-7, -3, -2, 5, 8], 0], "output": 1},
        ],
        hints=[
            "각 원소는 '고른다 / 고르지 않는다' 두 가지뿐입니다. 모든 선택을 따라가며 합을 누적해 보세요.",
            "인덱스를 하나씩 진행하며 현재 원소를 더한 경우와 더하지 않은 경우로 갈라지는 백트래킹/완전탐색을 사용하세요.",
            "bt(i, total, picked): i==len 이면 picked>0 이고 total==S 일 때만 +1. 아니면 nums[i]를 더한 가지와 더하지 않은 가지로 재귀.",
        ],
        testcases=[
            {"args": [[1, 2, 3], 3], "expected": 2},
            {"args": [[-7, -3, -2, 5, 8], 0], "expected": 1},
            {"args": [[5, -1, 1, 5, -1], 0], "expected": 2},
            {"args": [[1, 1, 1], 10], "expected": 0},
            {"args": [[0], 0], "expected": 1},
        ],
        reference_py=r'''def solution(nums, S):
    n = len(nums)
    count = 0
    def bt(i, total, picked):
        nonlocal count
        if i == n:
            if picked > 0 and total == S:
                count += 1
            return
        bt(i + 1, total + nums[i], picked + 1)
        bt(i + 1, total, picked)
    bt(0, 0, 0)
    return count
''',
        reference_java=r'''class Solution {
    int[] nums;
    int n, S, count = 0;
    public int solution(int[] nums, int S) {
        this.nums = nums;
        this.n = nums.length;
        this.S = S;
        bt(0, 0, 0);
        return count;
    }
    void bt(int i, int total, int picked) {
        if (i == n) {
            if (picked > 0 && total == S) count++;
            return;
        }
        bt(i + 1, total + nums[i], picked + 1);
        bt(i + 1, total, picked);
    }
}
''',
        template_py=r'''# 부분수열의 합 가짓수 (완전탐색/백트래킹)
def solution(nums, S):
    answer = 0
    return answer
''',
    ),

    Problem(
        id="gold-30",
        rank="Gold",
        title="합이 목표가 되는 조합 수",
        style="대기업",
        topic="백트래킹",
        type="func",
        func_name="solution",
        description=(
            "정수 배열 nums 에서 서로 다른 위치의 원소 k개를 고르는 모든 조합 중, 고른 k개의 "
            "합이 정확히 target 이 되는 조합의 개수를 반환하세요. (조합이므로 고르는 순서는 "
            "구분하지 않는다.)"
        ),
        input_desc="nums : 정수 리스트, k : 고를 개수(1 ≤ k ≤ len), target : 목표 합.",
        output_desc="합이 target 인 크기 k 조합의 개수 (int).",
        examples=[
            {"args": [[1, 2, 3, 4], 2, 5], "output": 2},
            {"args": [[2, 2, 2], 2, 4], "output": 3},
        ],
        hints=[
            "k개를 고르는 조합을 모두 만들면서 합이 target 인 것만 세면 됩니다.",
            "시작 인덱스를 넘기는 조합 백트래킹으로 중복 없이 k개를 고르고, 다 골랐을 때 합을 비교하세요.",
            "bt(start, cnt, total): cnt==k 이면 total==target 일 때 +1. 아니면 i in range(start, len): bt(i+1, cnt+1, total+nums[i]).",
        ],
        testcases=[
            {"args": [[1, 2, 3, 4], 2, 5], "expected": 2},
            {"args": [[2, 2, 2], 2, 4], "expected": 3},
            {"args": [[1, 2, 3, 4, 5], 3, 9], "expected": 2},
            {"args": [[1, 2, 3], 2, 100], "expected": 0},
            {"args": [[5, 5, 5, 5], 1, 5], "expected": 4},
        ],
        reference_py=r'''def solution(nums, k, target):
    n = len(nums)
    count = 0
    def bt(start, cnt, total):
        nonlocal count
        if cnt == k:
            if total == target:
                count += 1
            return
        for i in range(start, n):
            bt(i + 1, cnt + 1, total + nums[i])
    bt(0, 0, 0)
    return count
''',
        reference_java=r'''class Solution {
    int[] nums;
    int n, k, target, count = 0;
    public int solution(int[] nums, int k, int target) {
        this.nums = nums;
        this.n = nums.length;
        this.k = k;
        this.target = target;
        bt(0, 0, 0);
        return count;
    }
    void bt(int start, int cnt, int total) {
        if (cnt == k) {
            if (total == target) count++;
            return;
        }
        for (int i = start; i < n; i++) {
            bt(i + 1, cnt + 1, total + nums[i]);
        }
    }
}
''',
        template_py=r'''# 합이 target 이 되는 크기 k 조합의 개수
def solution(nums, k, target):
    answer = 0
    return answer
''',
    ),

    Problem(
        id="gold-31",
        rank="Gold",
        title="안전 영역 최대 개수",
        style="백준",
        topic="BFS",
        type="stdin",
        description=(
            "N×N 지역의 각 칸에 높이가 적혀 있다. 장마철에 물에 잠기는 높이 h(정수)를 적절히 "
            "정하면, 높이가 h 이하인 칸은 모두 물에 잠긴다. 물에 잠기지 않은 칸들이 상하좌우로 "
            "이어진 덩어리를 안전 영역이라 할 때, 잠기는 높이를 바꿔 가며 만들 수 있는 안전 영역의 "
            "최대 개수를 구하시오. 비가 오지 않는 경우도 고려한다."
        ),
        input_desc=(
            "첫째 줄에 N (2 ≤ N ≤ 100). 다음 N개의 줄에 각 칸의 높이(1 이상 100 이하의 정수) "
            "N개가 공백으로 주어진다."
        ),
        output_desc="만들 수 있는 안전 영역 개수의 최댓값.",
        examples=[
            {
                "input": "5\n6 8 2 6 2\n3 2 3 4 6\n6 7 3 3 2\n7 2 5 3 6\n8 9 5 2 7\n",
                "output": "5\n",
            },
            {"input": "2\n1 1\n1 1\n", "output": "1\n"},
        ],
        hints=[
            "물 높이 h 를 0부터 (최대 높이-1)까지 바꿔 가며 각각 안전 영역 개수를 세고, 그중 최댓값을 답으로 합니다.",
            "각 h마다 '높이 > h' 인 칸들에 대해 연결 요소(상하좌우)를 세는 BFS/DFS를 수행하세요.",
            "for h in range(0, maxHeight): 방문 배열 초기화 후 높이>h 인 미방문 칸에서 탐색 시작할 때마다 cnt+=1. 모든 h의 cnt 중 최댓값 출력.",
        ],
        testcases=[
            {
                "input": "5\n6 8 2 6 2\n3 2 3 4 6\n6 7 3 3 2\n7 2 5 3 6\n8 9 5 2 7\n",
                "output": "5\n",
            },
            {"input": "1\n5\n", "output": "1\n"},
            {"input": "2\n1 1\n1 1\n", "output": "1\n"},
            {"input": "3\n1 2 1\n2 1 2\n1 2 1\n", "output": "4\n"},
            {
                "input": "5\n5 5 5 5 5\n5 1 5 1 5\n5 5 5 5 5\n5 1 5 1 5\n5 5 5 5 5\n",
                "output": "1\n",
            },
        ],
        reference_py=r'''import sys
from collections import deque
input = sys.stdin.readline
def main():
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(n)]
    top = max(max(row) for row in g)
    best = 0
    for h in range(0, top):
        visited = [[False] * n for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if g[i][j] > h and not visited[i][j]:
                    cnt += 1
                    visited[i][j] = True
                    q = deque([(i, j)])
                    while q:
                        x, y = q.popleft()
                        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < n and 0 <= ny < n and g[nx][ny] > h and not visited[nx][ny]:
                                visited[nx][ny] = True
                                q.append((nx, ny))
        best = max(best, cnt)
    print(best)
main()
''',
        reference_java=r'''import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        int[][] g = new int[n][n];
        int top = 0;
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                g[i][j] = Integer.parseInt(st.nextToken());
                top = Math.max(top, g[i][j]);
            }
        }
        int[] dx = {1,-1,0,0}, dy = {0,0,1,-1};
        int best = 0;
        for (int h = 0; h < top; h++) {
            boolean[][] visited = new boolean[n][n];
            int cnt = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (g[i][j] > h && !visited[i][j]) {
                        cnt++;
                        visited[i][j] = true;
                        ArrayDeque<int[]> q = new ArrayDeque<>();
                        q.add(new int[]{i, j});
                        while (!q.isEmpty()) {
                            int[] c = q.poll();
                            for (int d = 0; d < 4; d++) {
                                int nx = c[0]+dx[d], ny = c[1]+dy[d];
                                if (nx>=0&&nx<n&&ny>=0&&ny<n&&g[nx][ny]>h&&!visited[nx][ny]) {
                                    visited[nx][ny] = true;
                                    q.add(new int[]{nx, ny});
                                }
                            }
                        }
                    }
                }
            }
            best = Math.max(best, cnt);
        }
        System.out.println(best);
    }
}
''',
        template_py=r'''import sys
from collections import deque
input = sys.stdin.readline
# 안전 영역 최대 개수
def main():
    n = int(input())
    # 물 높이 h 를 바꿔 가며 안전 영역(연결 요소) 개수의 최댓값을 구하세요.
    pass
main()
''',
    ),

    Problem(
        id="gold-32",
        rank="Gold",
        title="단어 변환 최단 길이",
        style="프로그래머스",
        topic="BFS",
        type="func",
        func_name="solution",
        description=(
            "길이가 같은 두 단어 begin 과 target, 그리고 단어 목록 words 가 주어진다. 한 번에 "
            "한 글자만 바꿔서 begin 을 target 으로 변환하려 한다. 단, 변환 과정의 모든 단어는 "
            "words 안에 있어야 한다. 최소 변환 횟수를 반환하고, 변환할 수 없으면 0을 반환하세요."
        ),
        input_desc="begin : 시작 단어, target : 목표 단어, words : 단어 목록(list[str]).",
        output_desc="begin 에서 target 으로 가는 최소 변환 횟수. 불가능하면 0 (int).",
        examples=[
            {"args": ["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]], "output": 4},
            {"args": ["hit", "cog", ["hot", "dot", "dog", "lot", "log"]], "output": 0},
        ],
        hints=[
            "한 글자만 다른 단어끼리 간선으로 이어진 그래프에서 begin 에서 target 까지의 최단 거리를 찾는 문제입니다.",
            "정확히 한 글자만 다른지 검사하는 함수를 만들고, begin 에서 시작하는 BFS로 단계(거리)를 세세요.",
            "target 이 words 에 없으면 0. 큐에 (단어, 거리)를 넣고 BFS; 한 글자 차이 나는 미방문 단어로 확장. target 을 꺼내면 그 거리를 반환.",
        ],
        testcases=[
            {"args": ["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]], "expected": 4},
            {"args": ["hit", "cog", ["hot", "dot", "dog", "lot", "log"]], "expected": 0},
            {"args": ["aaa", "aac", ["aab", "aac"]], "expected": 1},
            {"args": ["abc", "abc", ["abd", "abc"]], "expected": 0},
            {"args": ["red", "tax", ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]], "expected": 3},
        ],
        reference_py=r'''from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    def one_diff(a, b):
        return sum(1 for x, y in zip(a, b) if x != y) == 1
    visited = set([begin])
    q = deque([(begin, 0)])
    while q:
        cur, d = q.popleft()
        if cur == target:
            return d
        for w in words:
            if w not in visited and one_diff(cur, w):
                visited.add(w)
                q.append((w, d + 1))
    return 0
''',
        reference_java=r'''import java.util.*;
class Solution {
    public int solution(String begin, String target, String[] words) {
        boolean inList = false;
        for (String w : words) if (w.equals(target)) inList = true;
        if (!inList) return 0;
        Set<String> visited = new HashSet<>();
        visited.add(begin);
        ArrayDeque<String> q = new ArrayDeque<>();
        ArrayDeque<Integer> dist = new ArrayDeque<>();
        q.add(begin);
        dist.add(0);
        while (!q.isEmpty()) {
            String cur = q.poll();
            int d = dist.poll();
            if (cur.equals(target)) return d;
            for (String w : words) {
                if (!visited.contains(w) && oneDiff(cur, w)) {
                    visited.add(w);
                    q.add(w);
                    dist.add(d + 1);
                }
            }
        }
        return 0;
    }
    boolean oneDiff(String a, String b) {
        int diff = 0;
        for (int i = 0; i < a.length(); i++) if (a.charAt(i) != b.charAt(i)) diff++;
        return diff == 1;
    }
}
''',
        template_py=r'''from collections import deque
# 단어 변환 최단 길이 (BFS)
def solution(begin, target, words):
    answer = 0
    return answer
''',
    ),

    Problem(
        id="gold-33",
        rank="Gold",
        title="스타트와 링크 팀 나누기",
        style="대기업",
        topic="백트래킹",
        type="stdin",
        description=(
            "N명(짝수)을 N/2명씩 두 팀으로 나눈다. 두 사람 i, j 가 같은 팀이면 S[i][j]+S[j][i] "
            "만큼의 능력치가 더해진다. 한 팀의 능력치는 그 팀에 속한 모든 쌍의 능력치 합이다. "
            "두 팀의 능력치 차이가 최소가 되도록 나눌 때, 그 최소 차이를 구하시오."
        ),
        input_desc=(
            "첫째 줄에 N (2 ≤ N ≤ 12, 짝수). 다음 N개의 줄에 능력치 행렬 S 가 주어지며, i번째 "
            "줄의 j번째 수가 S[i][j] 이다. (대각선 S[i][i] = 0)"
        ),
        output_desc="두 팀의 능력치 차이의 최솟값.",
        examples=[
            {"input": "4\n0 1 2 3\n4 0 5 6\n7 1 0 2\n3 4 5 0\n", "output": "0\n"},
            {"input": "2\n0 5\n3 0\n", "output": "0\n"},
        ],
        hints=[
            "한 팀(N/2명)을 정하면 나머지가 자동으로 다른 팀이 됩니다. 가능한 모든 절반 조합을 만들어 보세요.",
            "0번 사람을 한쪽 팀에 고정하면 중복을 줄일 수 있고, 조합으로 팀을 정한 뒤 각 팀의 쌍 능력치 합을 계산합니다.",
            "combinations 로 절반을 고르고, 팀별로 i<j 인 모든 쌍의 S[i][j]+S[j][i] 를 더한 두 합의 절댓값 차를 구해 최솟값을 갱신.",
        ],
        testcases=[
            {"input": "4\n0 1 2 3\n4 0 5 6\n7 1 0 2\n3 4 5 0\n", "output": "0\n"},
            {"input": "2\n0 5\n3 0\n", "output": "0\n"},
            {"input": "4\n0 10 0 0\n0 0 0 0\n0 0 0 0\n0 0 0 0\n", "output": "0\n"},
            {
                "input": "6\n0 1 2 3 4 5\n1 0 2 3 4 5\n1 2 0 3 4 5\n1 2 3 0 4 5\n1 2 3 4 0 5\n1 2 3 4 5 0\n",
                "output": "2\n",
            },
        ],
        reference_py=r'''import sys
from itertools import combinations
input = sys.stdin.readline
def main():
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(n)]
    half = n // 2
    best = float('inf')
    for team in combinations(range(n), half):
        teamset = set(team)
        other = [i for i in range(n) if i not in teamset]
        ts = sum(s[i][j] + s[j][i] for i in team for j in team if i < j)
        os = sum(s[i][j] + s[j][i] for i in other for j in other if i < j)
        diff = abs(ts - os)
        if diff < best:
            best = diff
    print(best)
main()
''',
        reference_java=r'''import java.util.*;
import java.io.*;
public class Main {
    static int n, half;
    static int[][] s;
    static int best = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine().trim());
        s = new int[n][n];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) s[i][j] = Integer.parseInt(st.nextToken());
        }
        half = n / 2;
        boolean[] pick = new boolean[n];
        choose(0, 0, pick);
        System.out.println(best);
    }
    static void choose(int idx, int cnt, boolean[] pick) {
        if (cnt == half) {
            int ts = 0, os = 0;
            for (int i = 0; i < n; i++)
                for (int j = i + 1; j < n; j++) {
                    if (pick[i] && pick[j]) ts += s[i][j] + s[j][i];
                    else if (!pick[i] && !pick[j]) os += s[i][j] + s[j][i];
                }
            best = Math.min(best, Math.abs(ts - os));
            return;
        }
        if (idx == n) return;
        pick[idx] = true;
        choose(idx + 1, cnt + 1, pick);
        pick[idx] = false;
        choose(idx + 1, cnt, pick);
    }
}
''',
        template_py=r'''import sys
from itertools import combinations
input = sys.stdin.readline
# 스타트와 링크 팀 나누기
def main():
    n = int(input())
    # 절반 조합을 만들어 두 팀 능력치 차의 최솟값을 구하세요.
    pass
main()
''',
    ),

    Problem(
        id="gold-34",
        rank="Gold",
        title="알파벳 최대 칸 이동",
        style="해외대기업",
        topic="DFS 백트래킹",
        type="stdin",
        description=(
            "R×C 격자의 각 칸에는 대문자 알파벳이 하나씩 적혀 있다. 말은 왼쪽 위(1행 1열)에서 "
            "시작하며, 상하좌우 인접한 칸으로 이동할 수 있다. 단, 한 번 지난 알파벳이 적힌 칸으로는 "
            "다시 갈 수 없다(같은 알파벳을 두 번 밟을 수 없음). 말이 지날 수 있는 최대 칸 수를 "
            "구하시오."
        ),
        input_desc=(
            "첫째 줄에 R C (1 ≤ R, C ≤ 20). 다음 R개의 줄에 대문자로 이루어진 길이 C 의 "
            "문자열이 주어진다."
        ),
        output_desc="말이 지날 수 있는 칸 수의 최댓값(시작 칸 포함).",
        examples=[
            {"input": "2 4\nCAAB\nADCB\n", "output": "3\n"},
            {"input": "3 6\nHFDFFB\nAJHGDH\nDGAGEH\n", "output": "6\n"},
        ],
        hints=[
            "지금까지 밟은 알파벳 집합을 들고 다니며, 더 갈 곳이 없을 때까지 깊이 우선으로 뻗어 보는 문제입니다.",
            "사용한 알파벳 표시 배열(26칸)을 두고, 이동·복귀 시 표시를 켰다 끄는 DFS 백트래킹을 사용하세요.",
            "dfs(x, y, length): 답을 length 와 비교해 갱신. 인접 칸의 알파벳이 아직 안 쓰였으면 표시 후 dfs(.., length+1), 복귀 시 표시 해제.",
        ],
        testcases=[
            {"input": "2 4\nCAAB\nADCB\n", "output": "3\n"},
            {"input": "3 6\nHFDFFB\nAJHGDH\nDGAGEH\n", "output": "6\n"},
            {"input": "1 1\nA\n", "output": "1\n"},
            {"input": "2 2\nAB\nBA\n", "output": "2\n"},
            {
                "input": "5 5\nABCDE\nFGHIJ\nKLMNO\nPQRST\nUVWXY\n",
                "output": "25\n",
            },
        ],
        reference_py=r'''import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
def main():
    r, c = map(int, input().split())
    g = [input().strip() for _ in range(r)]
    used = [False] * 26
    res = [0]
    def dfs(x, y, length):
        if length > res[0]:
            res[0] = length
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c:
                idx = ord(g[nx][ny]) - 65
                if not used[idx]:
                    used[idx] = True
                    dfs(nx, ny, length + 1)
                    used[idx] = False
    used[ord(g[0][0]) - 65] = True
    dfs(0, 0, 1)
    print(res[0])
main()
''',
        reference_java=r'''import java.util.*;
import java.io.*;
public class Main {
    static int r, c, best = 0;
    static char[][] g;
    static boolean[] used = new boolean[26];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        g = new char[r][];
        for (int i = 0; i < r; i++) g[i] = br.readLine().trim().toCharArray();
        used[g[0][0] - 'A'] = true;
        dfs(0, 0, 1);
        System.out.println(best);
    }
    static void dfs(int x, int y, int length) {
        if (length > best) best = length;
        int[] dx = {1,-1,0,0}, dy = {0,0,1,-1};
        for (int d = 0; d < 4; d++) {
            int nx = x + dx[d], ny = y + dy[d];
            if (nx >= 0 && nx < r && ny >= 0 && ny < c) {
                int idx = g[nx][ny] - 'A';
                if (!used[idx]) {
                    used[idx] = true;
                    dfs(nx, ny, length + 1);
                    used[idx] = false;
                }
            }
        }
    }
}
''',
        template_py=r'''import sys
input = sys.stdin.readline
# 알파벳 최대 칸 이동 (DFS 백트래킹)
def main():
    r, c = map(int, input().split())
    # 밟은 알파벳을 표시하며 DFS로 최대 길이를 구하세요.
    pass
main()
''',
    ),

    Problem(
        id="gold-35",
        rank="Gold",
        title="숨바꼭질 최소 시간",
        style="백준",
        topic="BFS",
        type="stdin",
        description=(
            "수직선 위 점 N에 있는 사람이 점 K에 있는 동생을 찾으려 한다. 현재 위치가 x일 때 "
            "1초 후 x-1, x+1, 또는 2x 중 한 곳으로 이동할 수 있다(0 이상 100000 이하 범위). "
            "동생을 찾는 데 걸리는 최소 시간(초)을 구하시오."
        ),
        input_desc="첫째 줄에 N과 K (0 ≤ N, K ≤ 100000).",
        output_desc="N에서 K에 도달하는 최소 시간(초).",
        examples=[
            {"input": "5 17\n", "output": "4\n"},
            {"input": "5 5\n", "output": "0\n"},
        ],
        hints=[
            "각 위치를 정점, 가능한 이동(-1, +1, ×2)을 간선으로 보면 가중치 1짜리 최단거리 문제입니다.",
            "방문한 위치의 도달 시간을 기록하며 BFS로 한 단계씩 퍼뜨리세요.",
            "dist 배열을 -1로 두고 dist[N]=0; 큐에서 x를 꺼내 x-1, x+1, 2x 중 범위 안의 미방문 칸에 dist+1 기록. x==K 를 처음 만나는 순간의 dist 가 답.",
        ],
        testcases=[
            {"input": "5 17\n", "output": "4\n"},
            {"input": "5 5\n", "output": "0\n"},
            {"input": "10 5\n", "output": "5\n"},
            {"input": "1 100\n", "output": "8\n"},
            {"input": "100000 1\n", "output": "99999\n"},
        ],
        reference_py=r'''import sys
from collections import deque
input = sys.stdin.readline
def main():
    n, k = map(int, input().split())
    MAX = 100001
    dist = [-1] * MAX
    dist[n] = 0
    q = deque([n])
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            return
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx < MAX and dist[nx] == -1:
                dist[nx] = dist[x] + 1
                q.append(nx)
    print(dist[k])
main()
''',
        reference_java=r'''import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int MAX = 100001;
        int[] dist = new int[MAX];
        Arrays.fill(dist, -1);
        dist[n] = 0;
        ArrayDeque<Integer> q = new ArrayDeque<>();
        q.add(n);
        while (!q.isEmpty()) {
            int x = q.poll();
            if (x == k) { System.out.println(dist[x]); return; }
            int[] nexts = {x - 1, x + 1, x * 2};
            for (int nx : nexts) {
                if (nx >= 0 && nx < MAX && dist[nx] == -1) {
                    dist[nx] = dist[x] + 1;
                    q.add(nx);
                }
            }
        }
        System.out.println(dist[k]);
    }
}
''',
        template_py=r'''import sys
from collections import deque
input = sys.stdin.readline
# 숨바꼭질 최소 시간 (1차원 BFS)
def main():
    n, k = map(int, input().split())
    # dist 배열로 BFS 최단 시간을 구하세요.
    pass
main()
''',
    ),

]
