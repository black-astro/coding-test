"""유형별 실전 — DP.

정수 삼각형 / 등굣길 / 스티커 / 도둑질 / 가장 긴 증가 부분 수열(LIS).
각 문제는 점화식이 자연스럽게 떠오르도록 상태 정의를 힌트에 명시했다.
"""

from engine.models import Problem

CATEGORY = "DP"

PROBLEMS = [

    Problem(
        id="dp-01",
        rank="Silver",
        title="정수 삼각형 최대 경로",
        style="삼성",
        topic="DP",
        type="stdin",
        description=(
            "맨 위 칸에서 시작해 아래로 내려가며 숫자를 더한다. 현재 칸에서는 바로 아래의 "
            "왼쪽 대각선 칸 또는 오른쪽 대각선 칸으로만 이동할 수 있다. 맨 아래 줄에 도달할 때까지 "
            "지나온 숫자의 합이 최대가 되도록 했을 때, 그 최대 합을 구하시오.\n\n"
            "한 칸의 최적은 '그 칸으로 올 수 있는 두 칸(바로 위 왼쪽/오른쪽)의 최적 중 더 큰 값'에 "
            "자기 값을 더한 것이므로, 위에서 아래로 누적하며 채우면 된다."
        ),
        input_desc=(
            "첫째 줄에 삼각형의 줄 수 n (1 ≤ n ≤ 500). 다음 n개의 줄에 i번째 줄은 i개의 정수가 "
            "공백으로 주어진다(각 정수는 0 이상 9999 이하)."
        ),
        output_desc="맨 위에서 맨 아래까지 내려오며 만들 수 있는 최대 합을 한 줄에 출력.",
        examples=[
            {"input": "5\n7\n3 8\n8 1 0\n2 7 4 4\n4 5 2 6 5\n", "output": "30\n"},
            {"input": "2\n1\n2 3\n", "output": "4\n"},
        ],
        hints=[
            "한 칸까지 오는 경로의 최댓값만 알면 충분합니다. 그 칸 아래로 어떤 경로가 이어질지는 위쪽과 무관합니다.",
            "dp[i][j] = (i,j)까지 내려오며 얻는 최대 합. 끝 칸은 위쪽 한 칸에서만, 가운데 칸은 위쪽 두 칸 중 큰 쪽에서 옵니다.",
            "for i in 1..n-1: for j in 0..i: 위쪽 후보는 j==0 -> dp[i-1][0], j==i -> dp[i-1][i-1], 그 외 max(dp[i-1][j-1],dp[i-1][j]). 답은 마지막 줄의 최댓값.",
        ],
        testcases=[
            {"input": "5\n7\n3 8\n8 1 0\n2 7 4 4\n4 5 2 6 5\n", "output": "30\n"},
            {"input": "2\n1\n2 3\n", "output": "4\n"},
            {"input": "1\n5\n", "output": "5\n"},
            {"input": "3\n1\n1 1\n1 1 1\n", "output": "3\n"},
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
            "        for (int i = 1; i < n; i++) {\n"
            "            for (int j = 0; j <= i; j++) {\n"
            "                if (j == 0) tri[i][j] += tri[i - 1][0];\n"
            "                else if (j == i) tri[i][j] += tri[i - 1][i - 1];\n"
            "                else tri[i][j] += Math.max(tri[i - 1][j - 1], tri[i - 1][j]);\n"
            "            }\n"
            "        }\n"
            "        int ans = 0;\n"
            "        for (int v : tri[n - 1]) ans = Math.max(ans, v);\n"
            "        System.out.println(ans);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "# 정수 삼각형 : 최대 합 경로 (DP)\n"
            "n = int(input())\n"
            "# ...\n"
        ),
    ),

    Problem(
        id="dp-02",
        rank="Gold",
        title="등굣길 격자 경로 수",
        style="카카오",
        topic="DP",
        type="func",
        func_name="solution",
        description=(
            "가로 m 칸, 세로 n 칸의 격자 도시가 있다. 학생은 항상 오른쪽 또는 아래쪽으로만 한 칸씩 "
            "이동해 왼쪽 위 (1,1) 집에서 오른쪽 아래 (m,n) 학교까지 간다. 비가 와서 일부 칸은 "
            "물에 잠겼고(puddles), 그 칸은 지날 수 없다. (1,1)에서 (m,n)까지 가는 서로 다른 "
            "경로의 수를 1,000,000,007 로 나눈 나머지를 반환하세요.\n\n"
            "한 칸에 도달하는 경로 수는 '왼쪽 칸까지의 경로 수'와 '위쪽 칸까지의 경로 수'의 합이다. "
            "물에 잠긴 칸의 경로 수는 0 으로 둔다."
        ),
        input_desc=(
            "m : 격자의 가로 길이(열 수), n : 세로 길이(행 수), "
            "puddles : 물에 잠긴 칸의 [열, 행] 좌표 리스트(1-indexed). 물웅덩이가 없으면 [[0, 0]] 으로 주어질 수 있다."
        ),
        output_desc="(1,1)에서 (m,n)까지 가는 경로의 수를 1,000,000,007 로 나눈 나머지(정수)",
        examples=[
            {"args": [4, 3, [[2, 2]]], "output": 4},
            {"args": [4, 3, [[0, 0]]], "output": 10},
        ],
        hints=[
            "오른쪽/아래로만 가므로, 어떤 칸에 오는 길은 왼쪽 또는 위에서 들어오는 길뿐입니다. 경로 수가 더해진다는 점에 주목하세요.",
            "dp[행][열] = 그 칸까지 오는 경로 수. dp[i][j] = dp[i-1][j] + dp[i][j-1]. 물웅덩이면 0. 합이 커지므로 매번 1,000,000,007 로 나눕니다.",
            "좌표가 [열,행]임에 주의. puddle={(행,열)}; dp[1][1]=1; for i,j: if puddle -> 0 else (dp[i-1][j]+dp[i][j-1])%MOD. 답은 dp[n][m].",
        ],
        testcases=[
            {"args": [4, 3, [[2, 2]]], "expected": 4},
            {"args": [4, 3, [[0, 0]]], "expected": 10},
            {"args": [1, 1, [[0, 0]]], "expected": 1},
            {"args": [2, 2, [[1, 2]]], "expected": 1},
            {"args": [3, 3, [[2, 1], [1, 2]]], "expected": 0},
        ],
        reference_py=(
            "def solution(m, n, puddles):\n"
            "    MOD = 1000000007\n"
            "    puddle = {(y, x) for x, y in puddles}\n"
            "    dp = [[0] * (m + 1) for _ in range(n + 1)]\n"
            "    dp[1][1] = 1\n"
            "    for i in range(1, n + 1):\n"
            "        for j in range(1, m + 1):\n"
            "            if i == 1 and j == 1:\n"
            "                continue\n"
            "            if (i, j) in puddle:\n"
            "                dp[i][j] = 0\n"
            "                continue\n"
            "            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD\n"
            "    return dp[n][m]\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int solution(int m, int n, int[][] puddles) {\n"
            "        final int MOD = 1000000007;\n"
            "        Set<Long> puddle = new HashSet<>();\n"
            "        for (int[] p : puddles) puddle.add((long) p[1] * 100000 + p[0]);\n"
            "        long[][] dp = new long[n + 1][m + 1];\n"
            "        dp[1][1] = 1;\n"
            "        for (int i = 1; i <= n; i++) {\n"
            "            for (int j = 1; j <= m; j++) {\n"
            "                if (i == 1 && j == 1) continue;\n"
            "                if (puddle.contains((long) i * 100000 + j)) { dp[i][j] = 0; continue; }\n"
            "                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD;\n"
            "            }\n"
            "        }\n"
            "        return (int) dp[n][m];\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 등굣길 : 경로 수 mod 1,000,000,007 (격자 DP)\n"
            "def solution(m, n, puddles):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="dp-03",
        rank="Gold",
        title="스티커 떼기 최대합",
        style="라인",
        topic="DP",
        type="stdin",
        description=(
            "2행 N열로 배열된 스티커가 있다. 각 스티커에는 점수가 적혀 있고, 스티커 하나를 떼면 "
            "그 스티커와 변을 맞댄 스티커(상하/좌우로 인접한 칸)는 찢어져 더 이상 뗄 수 없다. "
            "(대각선으로 인접한 스티커는 영향을 받지 않는다.) 뗄 수 있는 스티커 점수의 합이 "
            "최대가 되도록 했을 때, 그 최댓값을 구하시오.\n\n"
            "각 열에서는 '아무것도 안 뗌 / 윗칸 뗌 / 아랫칸 뗌' 세 가지 상태만 존재한다. "
            "어떤 칸을 떼려면 바로 이전 열에서 같은 행을 떼지 않았어야 하므로, 열 단위로 상태를 이어가며 채운다."
        ),
        input_desc=(
            "첫째 줄에 열의 수 N (1 ≤ N ≤ 100000). 둘째 줄에 1행의 N개 점수, 셋째 줄에 2행의 N개 점수가 "
            "각각 공백으로 주어진다(각 점수는 0 이상 100 이하)."
        ),
        output_desc="뗄 수 있는 스티커 점수 합의 최댓값을 한 줄에 출력.",
        examples=[
            {"input": "5\n50 10 100 20 40\n30 50 70 10 60\n", "output": "260\n"},
            {"input": "2\n1 100\n100 1\n", "output": "200\n"},
        ],
        hints=[
            "열을 왼쪽부터 처리한다고 생각하세요. 지금 열에서 윗칸을 떼려면, 직전 열에서는 윗칸을 떼지 않았어야 합니다(아랫칸이나 아무것도 안 뗌은 가능).",
            "dp[i] = [i열에서 아무것도 안 뗌, 윗칸 뗌, 아랫칸 뗌]의 최대 점수. 윗칸을 뗄 땐 직전 열의 '안 뗌'과 '아랫칸 뗌' 중 큰 값을 더합니다.",
            "dp0=[0,a0,b0]; dp[i][0]=max(dp[i-1]); dp[i][1]=max(dp[i-1][0],dp[i-1][2])+a[i]; dp[i][2]=max(dp[i-1][0],dp[i-1][1])+b[i]. 답은 max(dp[N-1]).",
        ],
        testcases=[
            {"input": "5\n50 10 100 20 40\n30 50 70 10 60\n", "output": "260\n"},
            {"input": "2\n1 100\n100 1\n", "output": "200\n"},
            {"input": "1\n5\n8\n", "output": "8\n"},
            {"input": "3\n1 1 1\n1 1 1\n", "output": "3\n"},
            {"input": "1\n0\n0\n", "output": "0\n"},
        ],
        reference_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "n = int(input())\n"
            "a = list(map(int, input().split()))\n"
            "b = list(map(int, input().split()))\n"
            "dp = [[0, 0, 0] for _ in range(n)]\n"
            "dp[0] = [0, a[0], b[0]]\n"
            "for i in range(1, n):\n"
            "    dp[i][0] = max(dp[i - 1])\n"
            "    dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + a[i]\n"
            "    dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + b[i]\n"
            "print(max(dp[n - 1]))\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        int n = Integer.parseInt(br.readLine().trim());\n"
            "        int[] a = new int[n], b = new int[n];\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        for (int i = 0; i < n; i++) a[i] = Integer.parseInt(st.nextToken());\n"
            "        st = new StringTokenizer(br.readLine());\n"
            "        for (int i = 0; i < n; i++) b[i] = Integer.parseInt(st.nextToken());\n"
            "        int[][] dp = new int[n][3];\n"
            "        dp[0][0] = 0; dp[0][1] = a[0]; dp[0][2] = b[0];\n"
            "        for (int i = 1; i < n; i++) {\n"
            "            dp[i][0] = Math.max(dp[i - 1][0], Math.max(dp[i - 1][1], dp[i - 1][2]));\n"
            "            dp[i][1] = Math.max(dp[i - 1][0], dp[i - 1][2]) + a[i];\n"
            "            dp[i][2] = Math.max(dp[i - 1][0], dp[i - 1][1]) + b[i];\n"
            "        }\n"
            "        System.out.println(Math.max(dp[n - 1][0], Math.max(dp[n - 1][1], dp[n - 1][2])));\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "# 스티커 : 2xN 인접 금지 최대합 (DP)\n"
            "n = int(input())\n"
            "# ...\n"
        ),
    ),

    Problem(
        id="dp-04",
        rank="Gold",
        title="원형 마을 도둑질",
        style="네이버",
        topic="DP",
        type="func",
        func_name="solution",
        description=(
            "도둑이 원형으로 늘어선 집들을 털려고 한다. 각 집에는 훔칠 금액 money[i] 가 있다. "
            "단, 서로 인접한 두 집을 연속해서 털면 경보가 울린다. 집들이 원형이므로 첫 번째 집과 "
            "마지막 집도 인접한다. 경보를 울리지 않고 훔칠 수 있는 최대 금액을 반환하세요.\n\n"
            "원형이라 첫 집과 마지막 집을 동시에 털 수는 없다. 그래서 '첫 집을 포함할 수 있는 "
            "일직선 구간(마지막 집 제외)'과 '마지막 집을 포함할 수 있는 일직선 구간(첫 집 제외)' "
            "두 경우로 나눠, 각각 일직선 도둑질을 풀고 더 큰 값을 택한다."
        ),
        input_desc="money : 각 집에 있는 금액 정수 리스트 (3 ≤ len, 집이 하나면 그 집을 턴다)",
        output_desc="경보 없이 훔칠 수 있는 최대 금액(정수)",
        examples=[
            {"args": [[1, 2, 3, 1]], "output": 4},
            {"args": [[2, 3, 2]], "output": 3},
        ],
        hints=[
            "원형이라는 제약은 결국 '첫 집과 마지막 집을 둘 다 털 수 없다'는 한 문장입니다. 두 가지 일직선 문제로 쪼개세요.",
            "일직선 도둑질: dp 점화식 cur = max(직전 cur, 전전 prev + 현재 집). 이를 money[:-1] 과 money[1:] 두 배열에 각각 적용합니다.",
            "def rob(arr): prev=cur=0; for x in arr: prev,cur=cur,max(cur,prev+x); return cur. 답은 max(rob(money[:-1]), rob(money[1:])). (집이 1채면 money[0])",
        ],
        testcases=[
            {"args": [[1, 2, 3, 1]], "expected": 4},
            {"args": [[2, 3, 2]], "expected": 3},
            {"args": [[200, 3, 140, 20, 10]], "expected": 340},
            {"args": [[10]], "expected": 10},
            {"args": [[100, 100, 100]], "expected": 100},
        ],
        reference_py=(
            "def solution(money):\n"
            "    n = len(money)\n"
            "    if n == 1:\n"
            "        return money[0]\n"
            "    def rob(arr):\n"
            "        prev = cur = 0\n"
            "        for x in arr:\n"
            "            prev, cur = cur, max(cur, prev + x)\n"
            "        return cur\n"
            "    return max(rob(money[:-1]), rob(money[1:]))\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    private int rob(int[] a, int lo, int hi) {\n"
            "        int prev = 0, cur = 0;\n"
            "        for (int i = lo; i <= hi; i++) {\n"
            "            int t = Math.max(cur, prev + a[i]);\n"
            "            prev = cur; cur = t;\n"
            "        }\n"
            "        return cur;\n"
            "    }\n"
            "    public int solution(int[] money) {\n"
            "        int n = money.length;\n"
            "        if (n == 1) return money[0];\n"
            "        return Math.max(rob(money, 0, n - 2), rob(money, 1, n - 1));\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 도둑질 : 원형 인접 금지 최대 금액 (DP)\n"
            "def solution(money):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="dp-05",
        rank="Gold",
        title="최장 증가 부분 수열 길이",
        style="쿠팡",
        topic="DP",
        type="func",
        func_name="solution",
        description=(
            "정수 수열 nums 가 주어진다. 원소들의 순서를 유지한 채 일부를 골라(연속일 필요는 없음) "
            "만든 부분 수열 중, 값이 순증가(엄격히 증가)하는 가장 긴 부분 수열의 길이를 반환하세요. "
            "예) [10, 20, 10, 30, 20, 50] 에서는 [10, 20, 30, 50] 으로 길이 4 가 최대다.\n\n"
            "각 위치까지의 부분 결과(그 원소로 끝나는 최장 길이)를 쌓아 올리는 전형적인 DP 문제다. "
            "끝값들을 정렬 상태로 관리하면 이분 탐색으로 더 빠르게 풀 수도 있다."
        ),
        input_desc="nums : 정수 리스트 (0 ≤ len ≤ 100000). 빈 리스트면 0 을 반환한다.",
        output_desc="가장 긴 순증가 부분 수열의 길이(정수)",
        examples=[
            {"args": [[10, 20, 10, 30, 20, 50]], "output": 4},
            {"args": [[5, 4, 3, 2, 1]], "output": 1},
        ],
        hints=[
            "각 원소를 '마지막 원소로 삼는' 증가 수열의 최대 길이를 구하면, 전체 답은 그 값들의 최댓값입니다.",
            "O(n^2) DP: dp[i] = nums[i]로 끝나는 LIS 길이. 더 빠르게는 'tails 배열(길이 k인 증가 수열의 가능한 가장 작은 끝값)'을 이분 탐색으로 갱신합니다.",
            "tails=[]; for x in nums: i=bisect_left(tails,x); if i==len(tails): tails.append(x) else tails[i]=x. 답은 len(tails).",
        ],
        testcases=[
            {"args": [[10, 20, 10, 30, 20, 50]], "expected": 4},
            {"args": [[1, 2, 3, 4, 5]], "expected": 5},
            {"args": [[5, 4, 3, 2, 1]], "expected": 1},
            {"args": [[3]], "expected": 1},
            {"args": [[], ], "expected": 0},
            {"args": [[2, 2, 2, 2]], "expected": 1},
        ],
        reference_py=(
            "import bisect\n"
            "def solution(nums):\n"
            "    tails = []\n"
            "    for x in nums:\n"
            "        i = bisect.bisect_left(tails, x)\n"
            "        if i == len(tails):\n"
            "            tails.append(x)\n"
            "        else:\n"
            "            tails[i] = x\n"
            "    return len(tails)\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int solution(int[] nums) {\n"
            "        int[] tails = new int[nums.length];\n"
            "        int size = 0;\n"
            "        for (int x : nums) {\n"
            "            int lo = 0, hi = size;\n"
            "            while (lo < hi) {\n"
            "                int mid = (lo + hi) >>> 1;\n"
            "                if (tails[mid] < x) lo = mid + 1;\n"
            "                else hi = mid;\n"
            "            }\n"
            "            tails[lo] = x;\n"
            "            if (lo == size) size++;\n"
            "        }\n"
            "        return size;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# LIS : 가장 긴 순증가 부분 수열 길이 (DP / 이분 탐색)\n"
            "def solution(nums):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

]
