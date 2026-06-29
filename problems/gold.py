"""골드 랭크 — DP / BFS·DFS / 배낭 / LIS / 투포인터.

목표 50문제. 현재 시드 5문제.
"""

from engine.models import Problem

PROBLEMS = [

    Problem(
        id="gold-01",
        rank="Gold",
        title="1로 만들기 (DP)",
        style="백준",
        topic="DP",
        type="func",
        func_name="solution",
        description=(
            "정수 n 에 대해 다음 연산을 사용한다: (1) 3으로 나누기(나눠떨어질 때), "
            "(2) 2로 나누기(나눠떨어질 때), (3) 1 빼기. n을 1로 만드는 데 필요한 "
            "최소 연산 횟수를 구하세요."
        ),
        input_desc="n : int (1 ≤ n ≤ 1_000_000)",
        output_desc="1로 만드는 최소 연산 횟수",
        examples=[
            {"args": [10], "output": 3},   # 10 -> 9 -> 3 -> 1
            {"args": [1], "output": 0},
        ],
        hints=[
            "n에서 한 번에 갈 수 있는 상태(n-1, n/2, n/3)들의 '최소 횟수'를 알면 n의 답을 알 수 있습니다.",
            "dp[i] = i를 1로 만드는 최소 횟수. dp[i] = dp[i-1]+1, 그리고 2·3으로 나눠지면 그 경우도 비교.",
            "dp[1]=0; for i in 2..n: dp[i]=dp[i-1]+1; if i%2==0: dp[i]=min(dp[i],dp[i//2]+1); if i%3==0: dp[i]=min(dp[i],dp[i//3]+1)",
        ],
        testcases=[
            {"args": [10], "expected": 3},
            {"args": [1], "expected": 0},
            {"args": [2], "expected": 1},
            {"args": [9], "expected": 2},
            {"args": [25], "expected": 5},
        ],
        reference_py=(
            "def solution(n):\n"
            "    dp = [0] * (n + 1)\n"
            "    for i in range(2, n + 1):\n"
            "        dp[i] = dp[i - 1] + 1\n"
            "        if i % 2 == 0:\n"
            "            dp[i] = min(dp[i], dp[i // 2] + 1)\n"
            "        if i % 3 == 0:\n"
            "            dp[i] = min(dp[i], dp[i // 3] + 1)\n"
            "    return dp[n]\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int n) {\n"
            "        int[] dp = new int[n + 1];\n"
            "        for (int i = 2; i <= n; i++) {\n"
            "            dp[i] = dp[i - 1] + 1;\n"
            "            if (i % 2 == 0) dp[i] = Math.min(dp[i], dp[i / 2] + 1);\n"
            "            if (i % 3 == 0) dp[i] = Math.min(dp[i], dp[i / 3] + 1);\n"
            "        }\n"
            "        return dp[n];\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 1로 만들기 : 최소 연산 횟수 (DP)\n"
            "def solution(n):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="gold-02",
        rank="Gold",
        title="미로 탐색 (BFS)",
        style="백준",
        topic="BFS",
        type="stdin",
        description=(
            "N×M 크기의 미로가 있다. 1은 이동 가능, 0은 벽이다. (1,1)에서 출발해 "
            "(N,M)까지 이동할 때 지나는 최소 칸 수(시작·도착 포함)를 구하시오. "
            "상하좌우로만 이동한다."
        ),
        input_desc="첫째 줄 N M, 다음 N개의 줄에 0/1로 이루어진 길이 M 문자열.",
        output_desc="(1,1)에서 (N,M)까지 지나는 최소 칸 수.",
        examples=[
            {"input": "4 6\n101111\n101010\n101011\n111011\n", "output": "15\n"},
            {"input": "2 2\n11\n11\n", "output": "3\n"},
        ],
        hints=[
            "최단 거리 = 가중치 없는 그래프의 최소 이동. 너비 우선으로 한 칸씩 퍼져나가는 방식을 생각하세요.",
            "BFS 를 쓰세요. 큐에 (행,열)을 넣고, 방문하지 않은 인접 칸으로 가며 거리값을 +1 해 채웁니다.",
            "dist[0][0]=1; deque로 BFS; 인접칸이 '1'이고 dist==0이면 dist[nx][ny]=dist[x][y]+1. 답은 dist[N-1][M-1].",
        ],
        testcases=[
            {"input": "4 6\n101111\n101010\n101011\n111011\n", "output": "15\n"},
            {"input": "2 2\n11\n11\n", "output": "3\n"},
            {"input": "1 1\n1\n", "output": "1\n"},
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
            "print(dist[n - 1][m - 1])\n"
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
            "                if (nx>=0&&nx<n&&ny>=0&&ny<m&&g[nx][ny]=='1'&&dist[nx][ny]==0){\n"
            "                    dist[nx][ny] = dist[c[0]][c[1]] + 1;\n"
            "                    q.add(new int[]{nx, ny});\n"
            "                }\n"
            "            }\n"
            "        }\n"
            "        System.out.println(dist[n-1][m-1]);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "from collections import deque\n"
            "input = sys.stdin.readline\n"
            "# 미로 탐색 (BFS 최단거리)\n"
            "n, m = map(int, input().split())\n"
            "# ...\n"
        ),
    ),

    Problem(
        id="gold-03",
        rank="Gold",
        title="0/1 배낭 문제",
        style="대기업",
        topic="DP",
        type="func",
        func_name="solution",
        description=(
            "무게 한도 capacity 인 배낭이 있다. 각 물건은 무게 weights[i], 가치 values[i] 를 "
            "가지며 한 번만 담을 수 있다(쪼갤 수 없음). 담을 수 있는 최대 가치 합을 구하세요."
        ),
        input_desc="weights : 무게 리스트, values : 가치 리스트, capacity : 배낭 한도",
        output_desc="담을 수 있는 최대 가치 합",
        examples=[
            {"args": [[6, 4, 3, 5], [13, 8, 6, 12], 7], "output": 14},
        ],
        hints=[
            "각 물건을 '담는다/안 담는다' 두 선택이 있고, 남은 용량에 따라 최선이 달라집니다.",
            "dp[w] = 무게 w를 넘지 않고 담을 수 있는 최대 가치. 물건마다 무게를 '큰 쪽부터' 갱신하세요(1차원 배낭).",
            "for wt,val in zip(weights,values): for w in range(capacity, wt-1, -1): dp[w]=max(dp[w], dp[w-wt]+val)",
        ],
        testcases=[
            {"args": [[6, 4, 3, 5], [13, 8, 6, 12], 7], "expected": 14},
            {"args": [[1, 2, 3], [6, 10, 12], 5], "expected": 22},
            {"args": [[5], [10], 4], "expected": 0},
            {"args": [[2, 2, 2], [3, 3, 3], 4], "expected": 6},
        ],
        reference_py=(
            "def solution(weights, values, capacity):\n"
            "    dp = [0] * (capacity + 1)\n"
            "    for wt, val in zip(weights, values):\n"
            "        for w in range(capacity, wt - 1, -1):\n"
            "            dp[w] = max(dp[w], dp[w - wt] + val)\n"
            "    return dp[capacity]\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int[] weights, int[] values, int capacity) {\n"
            "        int[] dp = new int[capacity + 1];\n"
            "        for (int i = 0; i < weights.length; i++)\n"
            "            for (int w = capacity; w >= weights[i]; w--)\n"
            "                dp[w] = Math.max(dp[w], dp[w - weights[i]] + values[i]);\n"
            "        return dp[capacity];\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 0/1 배낭 : 최대 가치 합\n"
            "def solution(weights, values, capacity):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="gold-04",
        rank="Gold",
        title="가장 긴 증가하는 부분 수열 (LIS)",
        style="백준",
        topic="DP",
        type="func",
        func_name="solution",
        description=(
            "수열 nums 가 주어졌을 때, 가장 긴 '증가하는' 부분 수열(연속이 아니어도 됨)의 "
            "길이를 구하세요. 예) [10,20,10,30,20,50] → [10,20,30,50] 길이 4."
        ),
        input_desc="nums : 정수 리스트 (1 ≤ len ≤ 1000)",
        output_desc="가장 긴 증가하는 부분 수열의 길이",
        examples=[
            {"args": [[10, 20, 10, 30, 20, 50]], "output": 4},
        ],
        hints=[
            "각 원소를 '마지막 원소로 하는' 증가 부분 수열의 최대 길이를 구해 보세요.",
            "dp[i] = nums[i]로 끝나는 LIS 길이. j<i 이고 nums[j]<nums[i] 인 dp[j] 중 최댓값 +1.",
            "dp=[1]*n; for i in range(n): for j in range(i): if nums[j]<nums[i]: dp[i]=max(dp[i],dp[j]+1). 답은 max(dp).",
        ],
        testcases=[
            {"args": [[10, 20, 10, 30, 20, 50]], "expected": 4},
            {"args": [[1, 2, 3, 4, 5]], "expected": 5},
            {"args": [[5, 4, 3, 2, 1]], "expected": 1},
            {"args": [[3]], "expected": 1},
        ],
        reference_py=(
            "def solution(nums):\n"
            "    n = len(nums)\n"
            "    dp = [1] * n\n"
            "    for i in range(n):\n"
            "        for j in range(i):\n"
            "            if nums[j] < nums[i]:\n"
            "                dp[i] = max(dp[i], dp[j] + 1)\n"
            "    return max(dp)\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int[] nums) {\n"
            "        int n = nums.length, best = 1;\n"
            "        int[] dp = new int[n];\n"
            "        for (int i = 0; i < n; i++) {\n"
            "            dp[i] = 1;\n"
            "            for (int j = 0; j < i; j++)\n"
            "                if (nums[j] < nums[i]) dp[i] = Math.max(dp[i], dp[j] + 1);\n"
            "            best = Math.max(best, dp[i]);\n"
            "        }\n"
            "        return best;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# LIS : 가장 긴 증가하는 부분 수열의 길이\n"
            "def solution(nums):\n"
            "    answer = 1\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="gold-05",
        rank="Gold",
        title="두 수의 합 (투 포인터)",
        style="대기업",
        topic="투포인터",
        type="func",
        func_name="solution",
        description=(
            "정수 배열 nums 와 목표값 target 이 주어진다. 서로 다른 두 원소를 더해 "
            "target 이 되는 쌍이 존재하면 True, 없으면 False 를 반환하세요. (정렬 + 투 포인터)"
        ),
        input_desc="nums : 정수 리스트, target : 정수",
        output_desc="합이 target 인 두 원소가 존재하면 True, 아니면 False",
        examples=[
            {"args": [[1, 3, 5, 7], 8], "output": True},
            {"args": [[1, 3, 5, 7], 100], "output": False},
        ],
        hints=[
            "모든 쌍을 다 검사하면 O(n^2)입니다. 배열을 정렬하면 양쪽 끝에서 좁혀가는 방법이 보입니다.",
            "정렬 후 left=0, right=n-1. 합이 크면 right를 줄이고, 작으면 left를 늘립니다.",
            "s=sorted(nums); l,r=0,len(s)-1; while l<r: t=s[l]+s[r]; if t==target: return True; elif t<target: l+=1; else: r-=1 → return False",
        ],
        testcases=[
            {"args": [[1, 3, 5, 7], 8], "expected": True},
            {"args": [[1, 3, 5, 7], 100], "expected": False},
            {"args": [[2, 2], 4], "expected": True},
            {"args": [[5], 5], "expected": False},
            {"args": [[-3, 1, 4, 2], -1], "expected": True},
        ],
        reference_py=(
            "def solution(nums, target):\n"
            "    s = sorted(nums)\n"
            "    l, r = 0, len(s) - 1\n"
            "    while l < r:\n"
            "        t = s[l] + s[r]\n"
            "        if t == target:\n"
            "            return True\n"
            "        elif t < target:\n"
            "            l += 1\n"
            "        else:\n"
            "            r -= 1\n"
            "    return False\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public boolean solution(int[] nums, int target) {\n"
            "        int[] s = nums.clone();\n"
            "        Arrays.sort(s);\n"
            "        int l = 0, r = s.length - 1;\n"
            "        while (l < r) {\n"
            "            int t = s[l] + s[r];\n"
            "            if (t == target) return true;\n"
            "            else if (t < target) l++;\n"
            "            else r--;\n"
            "        }\n"
            "        return false;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 두 수의 합 = target 쌍 존재 여부 (투 포인터)\n"
            "def solution(nums, target):\n"
            "    answer = False\n"
            "    return answer\n"
        ),
    ),

]
