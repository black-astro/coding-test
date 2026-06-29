"""실버 랭크 배치 C — 그리디 / 투 포인터·슬라이딩 윈도우 / 완전탐색 / 수학 / 재귀.

silver-36 ~ silver-50 (15문제).
base(silver.py) 및 정렬·탐색·스택큐해시 배치와 주제 중복 금지.
"""

from engine.models import Problem

RANK = "Silver"

PROBLEMS = [

    Problem(
        id="silver-36",
        rank="Silver",
        title="회의실 배정",
        style="백준",
        topic="그리디",
        type="func",
        func_name="solution",
        description=(
            "하나의 회의실에 회의 시작/종료 시간이 적힌 회의 목록이 주어진다. "
            "한 회의실에서는 동시에 한 개의 회의만 열 수 있고, 한 회의가 끝나는 시각과 "
            "다른 회의가 시작하는 시각이 같아도 된다. 겹치지 않게 최대한 많은 회의를 "
            "배정했을 때, 배정 가능한 회의의 최대 개수를 구하세요."
        ),
        input_desc="meetings : [[시작, 종료], ...] (0 ≤ 시작 ≤ 종료)",
        output_desc="겹치지 않게 배정할 수 있는 회의의 최대 개수",
        examples=[
            {"args": [[[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]], "output": 4},
            {"args": [[[1, 2], [2, 3], [3, 4]]], "output": 3},
        ],
        hints=[
            "어떤 회의를 먼저 골라야 다음에 더 많은 회의를 넣을 수 있을지 생각해 보세요. 기준이 되는 값이 있습니다.",
            "그리디로 풉니다. 회의를 '끝나는 시간' 기준으로 오름차순 정렬한 뒤, 앞에서부터 겹치지 않으면 선택하세요.",
            "meetings.sort(key=lambda x:(x[1],x[0])); last=-1; for s,e: if s>=last: cnt+=1; last=e",
        ],
        testcases=[
            {"args": [[[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]], "expected": 4},
            {"args": [[[1, 2], [2, 3], [3, 4]]], "expected": 3},
            {"args": [[[1, 3], [2, 4], [3, 5]]], "expected": 2},
            {"args": [[]], "expected": 0},
            {"args": [[[5, 5]]], "expected": 1},
        ],
        reference_py=(
            "def solution(meetings):\n"
            "    meetings = sorted(meetings, key=lambda x: (x[1], x[0]))\n"
            "    cnt = 0\n"
            "    last = -1\n"
            "    for s, e in meetings:\n"
            "        if s >= last:\n"
            "            cnt += 1\n"
            "            last = e\n"
            "    return cnt\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int solution(int[][] meetings) {\n"
            "        Arrays.sort(meetings, (a, b) -> a[1] != b[1] ? a[1] - b[1] : a[0] - b[0]);\n"
            "        int cnt = 0, last = -1;\n"
            "        for (int[] m : meetings) {\n"
            "            if (m[0] >= last) { cnt++; last = m[1]; }\n"
            "        }\n"
            "        return cnt;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 겹치지 않게 배정할 수 있는 회의의 최대 개수\n"
            "def solution(meetings):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="silver-37",
        rank="Silver",
        title="동전 개수 최대화",
        style="대기업",
        topic="그리디",
        type="func",
        func_name="solution",
        description=(
            "서로 배수 관계인 동전 단위 coins 로 정확히 amount 원을 만들려고 한다. "
            "이번에는 동전 '개수를 최대로' 사용하려고 한다. 사용할 수 있는 최대 동전 개수를 "
            "구하세요. 정확히 만들 수 없으면 -1 을 반환합니다."
        ),
        input_desc="coins : 배수 관계인 동전 단위 리스트, amount : 만들 금액 (0 ≤ amount)",
        output_desc="사용 가능한 최대 동전 개수 (불가능하면 -1)",
        examples=[
            {"args": [[500, 100, 50, 10], 1260], "output": 126},
            {"args": [[500, 100, 50, 10], 33], "output": -1},
        ],
        hints=[
            "동전 개수를 늘리려면 큰 동전과 작은 동전 중 어느 쪽을 많이 써야 할지 생각해 보세요.",
            "그리디입니다. 가장 작은 동전 하나가 가장 많은 개수를 만듭니다. 배수 관계이므로 가장 작은 단위로 나눠떨어지면 그 단위로만 채우는 것이 최대입니다.",
            "m = min(coins); return amount // m if amount % m == 0 else -1",
        ],
        testcases=[
            {"args": [[500, 100, 50, 10], 1260], "expected": 126},
            {"args": [[500, 100, 50, 10], 33], "expected": -1},
            {"args": [[500, 100, 50, 10], 0], "expected": 0},
            {"args": [[1000, 500, 100], 1700], "expected": 17},
            {"args": [[25, 5, 1], 30], "expected": 30},
        ],
        reference_py=(
            "def solution(coins, amount):\n"
            "    m = min(coins)\n"
            "    if amount % m != 0:\n"
            "        return -1\n"
            "    return amount // m\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int solution(int[] coins, int amount) {\n"
            "        int m = coins[0];\n"
            "        for (int c : coins) m = Math.min(m, c);\n"
            "        if (amount % m != 0) return -1;\n"
            "        return amount / m;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 사용 가능한 최대 동전 개수 (불가능하면 -1)\n"
            "def solution(coins, amount):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="silver-38",
        rank="Silver",
        title="거스름돈 최소 화폐 개수",
        style="프로그래머스",
        topic="그리디",
        type="stdin",
        description=(
            "거슬러 줄 금액 N 이 주어진다. 사용할 수 있는 화폐 단위는 "
            "50000, 10000, 5000, 1000, 500, 100, 50, 10 원이다. "
            "N 원을 거슬러 줄 때 필요한 화폐(지폐와 동전)의 최소 개수를 구하시오. "
            "N 은 항상 10의 배수이다."
        ),
        input_desc="첫째 줄에 거슬러 줄 금액 N (0 ≤ N ≤ 1,000,000, N은 10의 배수)",
        output_desc="필요한 화폐의 최소 개수를 한 줄에 출력한다.",
        examples=[
            {"input": "4790\n", "output": "12\n"},
            {"input": "80\n", "output": "4\n"},
        ],
        hints=[
            "큰 단위 화폐부터 최대한 많이 쓰는 것이 개수를 줄이는 길입니다.",
            "화폐 단위가 서로 배수 관계이므로 그리디가 최적입니다. 큰 단위부터 N//단위 개를 쓰고 나머지를 다음 단위로 넘기세요.",
            "for c in [50000,10000,...,10]: cnt += n//c; n %= c → 마지막에 cnt 출력",
        ],
        testcases=[
            {"input": "4790\n", "output": "12\n"},
            {"input": "80\n", "output": "4\n"},
            {"input": "0\n", "output": "0\n"},
            {"input": "50000\n", "output": "1\n"},
            {"input": "1000000\n", "output": "20\n"},
        ],
        reference_py=(
            "n = int(input())\n"
            "coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10]\n"
            "cnt = 0\n"
            "for c in coins:\n"
            "    cnt += n // c\n"
            "    n %= c\n"
            "print(cnt)\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        int n = Integer.parseInt(br.readLine().trim());\n"
            "        int[] coins = {50000, 10000, 5000, 1000, 500, 100, 50, 10};\n"
            "        int cnt = 0;\n"
            "        for (int c : coins) { cnt += n / c; n %= c; }\n"
            "        System.out.println(cnt);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 거스름돈 N을 만드는 최소 화폐 개수\n"
            "n = int(input())\n"
            "# coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10]\n"
        ),
    ),

    Problem(
        id="silver-39",
        rank="Silver",
        title="연속 부분수열의 합",
        style="해외대기업",
        topic="투포인터",
        type="func",
        func_name="solution",
        description=(
            "양의 정수로 이루어진 수열 nums 가 있다. 연속한 부분수열 중에서 그 합이 정확히 "
            "target 이 되는 경우의 수를 구하세요. (부분수열의 시작과 끝이 다르면 다른 경우로 센다.)"
        ),
        input_desc="nums : 양의 정수 리스트, target : 찾을 합 (target ≥ 1)",
        output_desc="합이 정확히 target 인 연속 부분수열의 개수",
        examples=[
            {"args": [[1, 2, 3, 4, 2, 5, 3, 1, 1, 2], 5], "output": 3},
            {"args": [[1, 1, 1, 1], 2], "output": 3},
        ],
        hints=[
            "모든 시작점과 끝점을 이중 반복으로 보면 느립니다. 수가 모두 양수라는 점을 활용해 보세요.",
            "투 포인터(슬라이딩 윈도우)를 씁니다. 오른쪽 끝을 늘려 합을 더하고, 합이 target 을 넘으면 왼쪽을 줄이세요. 합이 정확히 같을 때마다 +1.",
            "left=0;s=0; for right: s+=nums[right]; while s>target: s-=nums[left];left+=1; if s==target: cnt+=1",
        ],
        testcases=[
            {"args": [[1, 2, 3, 4, 2, 5, 3, 1, 1, 2], 5], "expected": 3},
            {"args": [[1, 1, 1, 1], 2], "expected": 3},
            {"args": [[5], 5], "expected": 1},
            {"args": [[1, 2, 3], 7], "expected": 0},
            {"args": [[2, 2, 2, 2], 4], "expected": 3},
        ],
        reference_py=(
            "def solution(nums, target):\n"
            "    left = 0\n"
            "    s = 0\n"
            "    cnt = 0\n"
            "    for right in range(len(nums)):\n"
            "        s += nums[right]\n"
            "        while s > target:\n"
            "            s -= nums[left]\n"
            "            left += 1\n"
            "        if s == target:\n"
            "            cnt += 1\n"
            "    return cnt\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int[] nums, int target) {\n"
            "        int left = 0, s = 0, cnt = 0;\n"
            "        for (int right = 0; right < nums.length; right++) {\n"
            "            s += nums[right];\n"
            "            while (s > target) { s -= nums[left]; left++; }\n"
            "            if (s == target) cnt++;\n"
            "        }\n"
            "        return cnt;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 합이 정확히 target 인 연속 부분수열의 개수\n"
            "def solution(nums, target):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="silver-40",
        rank="Silver",
        title="최소 길이 부분합",
        style="백준",
        topic="슬라이딩윈도우",
        type="stdin",
        description=(
            "길이 N 인 수열과 정수 S 가 주어진다. 연속한 부분수열 중에서 그 합이 S 이상이 되는 것 중 "
            "가장 짧은 것의 길이를 구하시오. 조건을 만족하는 부분수열이 없으면 0 을 출력한다."
        ),
        input_desc=(
            "첫째 줄에 N 과 S (1 ≤ N ≤ 100000, 1 ≤ S), "
            "둘째 줄에 N 개의 양의 정수가 공백으로 주어진다."
        ),
        output_desc="합이 S 이상인 가장 짧은 연속 부분수열의 길이 (없으면 0).",
        examples=[
            {"input": "10 15\n5 1 3 5 10 7 4 9 2 8\n", "output": "2\n"},
            {"input": "5 100\n1 2 3 4 5\n", "output": "0\n"},
        ],
        hints=[
            "모든 구간을 직접 다 더하면 느립니다. 양수 수열이라는 점을 이용해 창(window)을 움직여 보세요.",
            "슬라이딩 윈도우입니다. 오른쪽을 늘려 합을 더하고, 합이 S 이상이면 길이를 갱신하며 왼쪽을 줄여 합을 빼세요.",
            "for right: cur+=a[right]; while cur>=S: best=min(best,right-left+1); cur-=a[left];left+=1",
        ],
        testcases=[
            {"input": "10 15\n5 1 3 5 10 7 4 9 2 8\n", "output": "2\n"},
            {"input": "5 100\n1 2 3 4 5\n", "output": "0\n"},
            {"input": "1 5\n5\n", "output": "1\n"},
            {"input": "1 6\n5\n", "output": "0\n"},
            {"input": "5 11\n1 2 3 4 5\n", "output": "3\n"},
        ],
        reference_py=(
            "import sys\n"
            "data = sys.stdin.read().split()\n"
            "n = int(data[0]); s = int(data[1])\n"
            "a = list(map(int, data[2:2 + n]))\n"
            "left = 0\n"
            "cur = 0\n"
            "best = n + 1\n"
            "for right in range(n):\n"
            "    cur += a[right]\n"
            "    while cur >= s:\n"
            "        if right - left + 1 < best:\n"
            "            best = right - left + 1\n"
            "        cur -= a[left]\n"
            "        left += 1\n"
            "print(best if best <= n else 0)\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int n = Integer.parseInt(st.nextToken());\n"
            "        int s = Integer.parseInt(st.nextToken());\n"
            "        int[] a = new int[n];\n"
            "        st = new StringTokenizer(br.readLine());\n"
            "        for (int i = 0; i < n; i++) a[i] = Integer.parseInt(st.nextToken());\n"
            "        int left = 0, cur = 0, best = n + 1;\n"
            "        for (int right = 0; right < n; right++) {\n"
            "            cur += a[right];\n"
            "            while (cur >= s) {\n"
            "                best = Math.min(best, right - left + 1);\n"
            "                cur -= a[left++];\n"
            "            }\n"
            "        }\n"
            "        System.out.println(best <= n ? best : 0);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "# 합이 S 이상인 가장 짧은 연속 부분수열의 길이\n"
            "data = sys.stdin.read().split()\n"
            "# n, s = ...\n"
        ),
    ),

    Problem(
        id="silver-41",
        rank="Silver",
        title="블랙잭 (세 장의 합)",
        style="해외대기업",
        topic="브루트포스",
        type="func",
        func_name="solution",
        description=(
            "N 장의 카드 숫자가 주어진다. 이 중 서로 다른 카드 3장을 골라 합이 M 을 넘지 않으면서 "
            "M 에 최대한 가깝게(즉 M 이하의 최댓값) 만들고자 한다. 그 최대 합을 구하세요. "
            "어떤 3장을 골라도 합이 M 을 넘으면 0 을 반환합니다."
        ),
        input_desc="cards : 카드 숫자 리스트(길이 ≥ 3), M : 넘지 않아야 할 한도",
        output_desc="3장을 골라 만들 수 있는 M 이하의 최대 합 (불가능하면 0)",
        examples=[
            {"args": [[5, 6, 7, 8, 9], 21], "output": 21},
            {"args": [[1, 2, 3], 5], "output": 0},
        ],
        hints=[
            "카드 수가 많지 않으니 가능한 3장 조합을 전부 확인해도 됩니다.",
            "완전탐색(브루트포스)입니다. 삼중 반복문으로 i<j<k 인 모든 조합의 합을 구해 M 이하 중 최댓값을 고르세요.",
            "for i: for j>i: for k>j: s=cards[i]+cards[j]+cards[k]; if s<=M: best=max(best,s)",
        ],
        testcases=[
            {"args": [[5, 6, 7, 8, 9], 21], "expected": 21},
            {"args": [[1, 2, 3], 5], "expected": 0},
            {"args": [[1, 2, 3], 6], "expected": 6},
            {"args": [[10, 20, 30, 40], 100], "expected": 90},
            {"args": [[2, 2, 2, 2], 6], "expected": 6},
        ],
        reference_py=(
            "def solution(cards, m):\n"
            "    n = len(cards)\n"
            "    best = 0\n"
            "    for i in range(n):\n"
            "        for j in range(i + 1, n):\n"
            "            for k in range(j + 1, n):\n"
            "                s = cards[i] + cards[j] + cards[k]\n"
            "                if s <= m and s > best:\n"
            "                    best = s\n"
            "    return best\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int[] cards, int m) {\n"
            "        int n = cards.length, best = 0;\n"
            "        for (int i = 0; i < n; i++)\n"
            "            for (int j = i + 1; j < n; j++)\n"
            "                for (int k = j + 1; k < n; k++) {\n"
            "                    int s = cards[i] + cards[j] + cards[k];\n"
            "                    if (s <= m && s > best) best = s;\n"
            "                }\n"
            "        return best;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 3장을 골라 만드는 M 이하의 최대 합 (불가능하면 0)\n"
            "def solution(cards, m):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="silver-42",
        rank="Silver",
        title="체스판 다시 칠하기",
        style="백준",
        topic="브루트포스",
        type="stdin",
        description=(
            "N×M 크기의 보드의 각 칸은 흰색(W) 또는 검은색(B)으로 칠해져 있다. 이 보드에서 "
            "8×8 크기를 잘라내어 체스판(이웃한 칸끼리 색이 다른)으로 만들려고 한다. 잘라낸 8×8 을 "
            "올바른 체스판으로 만들기 위해 다시 칠해야 하는 칸 수의 최솟값을 구하시오."
        ),
        input_desc=(
            "첫째 줄에 N 과 M (8 ≤ N, M ≤ 50), 다음 N 개의 줄에 길이 M 인 'W'/'B' 문자열이 주어진다."
        ),
        output_desc="다시 칠해야 하는 칸 수의 최솟값.",
        examples=[
            {"input": "8 8\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBWBWBW\n", "output": "0\n"},
            {"input": "8 8\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBWBWBB\n", "output": "1\n"},
        ],
        hints=[
            "잘라낼 수 있는 8×8 영역의 왼쪽 위 모서리 위치는 많지 않습니다. 모든 시작 위치를 시험해 보세요.",
            "브루트포스입니다. 각 8×8 영역마다 'W로 시작하는 패턴'과의 불일치 수를 세면, 'B로 시작하는 패턴'과의 불일치는 64에서 뺀 값입니다. 둘 중 작은 값이 그 영역의 비용.",
            "for r in range(N-7): for c in range(M-7): cost = sum(board[r+i][c+j] != ('WB'[(i+j)%2]) ...); best=min(best,min(cost,64-cost))",
        ],
        testcases=[
            {"input": "8 8\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBWBWBW\n", "output": "0\n"},
            {"input": "8 8\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBWBWBB\n", "output": "1\n"},
            {"input": "8 8\nWWWWWWWW\nWWWWWWWW\nWWWWWWWW\nWWWWWWWW\nWWWWWWWW\nWWWWWWWW\nWWWWWWWW\nWWWWWWWW\n", "output": "32\n"},
            {"input": "8 9\nWBWBWBWBW\nBWBWBWBWB\nWBWBWBWBW\nBWBWBWBWB\nWBWBWBWBW\nBWBWBWBWB\nWBWBWBWBW\nBWBWBWBWB\n", "output": "0\n"},
        ],
        reference_py=(
            "import sys\n"
            "lines = sys.stdin.read().splitlines()\n"
            "n, m = map(int, lines[0].split())\n"
            "board = lines[1:1 + n]\n"
            "def cost(r, c):\n"
            "    cnt = 0\n"
            "    for i in range(8):\n"
            "        for j in range(8):\n"
            "            expected = 'W' if (i + j) % 2 == 0 else 'B'\n"
            "            if board[r + i][c + j] != expected:\n"
            "                cnt += 1\n"
            "    return min(cnt, 64 - cnt)\n"
            "best = 64\n"
            "for r in range(n - 7):\n"
            "    for c in range(m - 7):\n"
            "        v = cost(r, c)\n"
            "        if v < best:\n"
            "            best = v\n"
            "print(best)\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    static String[] board;\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int n = Integer.parseInt(st.nextToken());\n"
            "        int m = Integer.parseInt(st.nextToken());\n"
            "        board = new String[n];\n"
            "        for (int i = 0; i < n; i++) board[i] = br.readLine();\n"
            "        int best = 64;\n"
            "        for (int r = 0; r <= n - 8; r++)\n"
            "            for (int c = 0; c <= m - 8; c++)\n"
            "                best = Math.min(best, cost(r, c));\n"
            "        System.out.println(best);\n"
            "    }\n"
            "    static int cost(int r, int c) {\n"
            "        int cnt = 0;\n"
            "        for (int i = 0; i < 8; i++)\n"
            "            for (int j = 0; j < 8; j++) {\n"
            "                char exp = ((i + j) % 2 == 0) ? 'W' : 'B';\n"
            "                if (board[r + i].charAt(c + j) != exp) cnt++;\n"
            "            }\n"
            "        return Math.min(cnt, 64 - cnt);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "# 8x8 체스판으로 만들기 위한 최소 재칠 칸 수\n"
            "lines = sys.stdin.read().splitlines()\n"
            "# n, m = map(int, lines[0].split())\n"
        ),
    ),

    Problem(
        id="silver-43",
        rank="Silver",
        title="최대공약수와 최소공배수",
        style="프로그래머스",
        topic="수학",
        type="func",
        func_name="solution",
        description=(
            "두 자연수 a, b 가 주어질 때, 이 두 수의 최대공약수(GCD)와 최소공배수(LCM)를 "
            "차례대로 담은 리스트 [최대공약수, 최소공배수] 를 반환하세요."
        ),
        input_desc="a, b : 두 자연수 (1 ≤ a, b)",
        output_desc="[최대공약수, 최소공배수] 형태의 리스트",
        examples=[
            {"args": [24, 18], "output": [6, 72]},
            {"args": [7, 5], "output": [1, 35]},
        ],
        hints=[
            "최소공배수는 두 수의 곱을 최대공약수로 나눈 값과 같습니다.",
            "유클리드 호제법으로 GCD 를 구하세요. gcd(a,b)=gcd(b, a%b). LCM = a*b // gcd.",
            "import math; g=math.gcd(a,b); return [g, a*b//g]",
        ],
        testcases=[
            {"args": [24, 18], "expected": [6, 72]},
            {"args": [7, 5], "expected": [1, 35]},
            {"args": [1, 1], "expected": [1, 1]},
            {"args": [100, 80], "expected": [20, 400]},
            {"args": [12, 12], "expected": [12, 12]},
        ],
        reference_py=(
            "import math\n"
            "def solution(a, b):\n"
            "    g = math.gcd(a, b)\n"
            "    return [g, a * b // g]\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }\n"
            "    public int[] solution(int a, int b) {\n"
            "        int g = gcd(a, b);\n"
            "        return new int[]{g, a * b / g};\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# [최대공약수, 최소공배수] 반환\n"
            "def solution(a, b):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="silver-44",
        rank="Silver",
        title="소수 구하기",
        style="백준",
        topic="수학",
        type="stdin",
        description=(
            "두 정수 M 과 N 이 주어질 때, M 이상 N 이하의 소수를 모두 한 줄에 하나씩 작은 수부터 "
            "출력하시오."
        ),
        input_desc="첫째 줄에 M 과 N 이 공백으로 주어진다. (1 ≤ M ≤ N ≤ 1,000,000)",
        output_desc="M 이상 N 이하의 소수를 한 줄에 하나씩 오름차순으로 출력한다.",
        examples=[
            {"input": "3 16\n", "output": "3\n5\n7\n11\n13\n"},
            {"input": "2 2\n", "output": "2\n"},
        ],
        hints=[
            "각 수마다 일일이 나눠 보면 범위가 클 때 느립니다. 한 번에 소수 여부를 표시해 두는 방법이 있습니다.",
            "에라토스테네스의 체를 사용하세요. 2부터 시작해 각 소수의 배수를 모두 합성수로 표시하면 됩니다.",
            "sieve=[True]*(N+1); sieve[0]=sieve[1]=False; for i in range(2,int(N**0.5)+1): if sieve[i]: sieve[i*i::i]=...",
        ],
        testcases=[
            {"input": "3 16\n", "output": "3\n5\n7\n11\n13\n"},
            {"input": "2 2\n", "output": "2\n"},
            {"input": "1 1\n", "output": "\n"},
            {"input": "20 30\n", "output": "23\n29\n"},
            {"input": "1 10\n", "output": "2\n3\n5\n7\n"},
        ],
        reference_py=(
            "import sys\n"
            "m, n = map(int, input().split())\n"
            "sieve = [True] * (n + 1)\n"
            "sieve[0] = False\n"
            "if n >= 1:\n"
            "    sieve[1] = False\n"
            "for i in range(2, int(n ** 0.5) + 1):\n"
            "    if sieve[i]:\n"
            "        for j in range(i * i, n + 1, i):\n"
            "            sieve[j] = False\n"
            "out = [str(i) for i in range(max(m, 2), n + 1) if sieve[i]]\n"
            "print('\\n'.join(out))\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int m = Integer.parseInt(st.nextToken());\n"
            "        int n = Integer.parseInt(st.nextToken());\n"
            "        boolean[] sieve = new boolean[n + 1];\n"
            "        Arrays.fill(sieve, true);\n"
            "        if (n >= 0) sieve[0] = false;\n"
            "        if (n >= 1) sieve[1] = false;\n"
            "        for (int i = 2; (long)i * i <= n; i++)\n"
            "            if (sieve[i])\n"
            "                for (int j = i * i; j <= n; j += i) sieve[j] = false;\n"
            "        StringBuilder sb = new StringBuilder();\n"
            "        for (int i = Math.max(m, 2); i <= n; i++)\n"
            "            if (sieve[i]) sb.append(i).append('\\n');\n"
            "        System.out.print(sb);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# M 이상 N 이하의 소수를 한 줄에 하나씩 출력\n"
            "m, n = map(int, input().split())\n"
            "# sieve = [True] * (n + 1)\n"
        ),
    ),

    Problem(
        id="silver-45",
        rank="Silver",
        title="조합 nCr 계산",
        style="대기업",
        topic="수학",
        type="func",
        func_name="solution",
        description=(
            "서로 다른 n 개에서 r 개를 순서 없이 고르는 경우의 수, 즉 조합 nCr 의 값을 구하세요. "
            "(0 ≤ r ≤ n)"
        ),
        input_desc="n, r : 정수 (0 ≤ r ≤ n)",
        output_desc="조합 nCr 의 값",
        examples=[
            {"args": [5, 2], "output": 10},
            {"args": [10, 3], "output": 120},
        ],
        hints=[
            "nCr 은 n! / (r! * (n-r)!) 로 정의됩니다. 경계값(r=0, r=n)도 함께 생각하세요.",
            "팩토리얼을 직접 구해 나눠도 되고, nCr = nC(r-1) * (n-r+1) / r 같은 점화식이나 파스칼의 삼각형을 써도 됩니다.",
            "from math import comb; return comb(n, r)  (직접 구현 시 분자 r개 곱, 분모 r! 로 나눔)",
        ],
        testcases=[
            {"args": [5, 2], "expected": 10},
            {"args": [10, 3], "expected": 120},
            {"args": [10, 0], "expected": 1},
            {"args": [6, 6], "expected": 1},
            {"args": [20, 10], "expected": 184756},
        ],
        reference_py=(
            "from math import comb\n"
            "def solution(n, r):\n"
            "    return comb(n, r)\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public long solution(int n, int r) {\n"
            "        long result = 1;\n"
            "        r = Math.min(r, n - r);\n"
            "        for (int i = 0; i < r; i++) {\n"
            "            result = result * (n - i) / (i + 1);\n"
            "        }\n"
            "        return result;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 조합 nCr 의 값\n"
            "def solution(n, r):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="silver-46",
        rank="Silver",
        title="진법 변환",
        style="프로그래머스",
        topic="수학",
        type="func",
        func_name="solution",
        description=(
            "10진수 정수 n 을 b 진법으로 변환한 문자열을 반환하세요. (2 ≤ b ≤ 16) "
            "10 이상의 자리는 영문 대문자 A(10), B(11), …, F(15) 로 표기합니다. n 이 0 이면 \"0\" 입니다."
        ),
        input_desc="n : 변환할 10진수 (0 ≤ n), b : 진법 (2 ≤ b ≤ 16)",
        output_desc="n 을 b 진법으로 표현한 문자열",
        examples=[
            {"args": [10, 2], "output": "1010"},
            {"args": [255, 16], "output": "FF"},
        ],
        hints=[
            "n 을 b 로 나눈 나머지가 가장 낮은 자리의 숫자가 됩니다. 이를 반복하세요.",
            "n 을 b 로 계속 나누며 나머지를 모으고, 나머지가 10 이상이면 문자로 바꿔야 합니다. 나머지를 앞쪽에 붙이거나, 모은 뒤 뒤집으세요.",
            "digits='0123456789ABCDEF'; res=''; while n>0: res=digits[n%b]+res; n//=b → n==0 이면 '0'",
        ],
        testcases=[
            {"args": [10, 2], "expected": "1010"},
            {"args": [255, 16], "expected": "FF"},
            {"args": [0, 2], "expected": "0"},
            {"args": [28, 16], "expected": "1C"},
            {"args": [8, 8], "expected": "10"},
        ],
        reference_py=(
            "def solution(n, b):\n"
            "    if n == 0:\n"
            "        return \"0\"\n"
            "    digits = \"0123456789ABCDEF\"\n"
            "    res = \"\"\n"
            "    while n > 0:\n"
            "        res = digits[n % b] + res\n"
            "        n //= b\n"
            "    return res\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public String solution(int n, int b) {\n"
            "        if (n == 0) return \"0\";\n"
            "        String digits = \"0123456789ABCDEF\";\n"
            "        StringBuilder sb = new StringBuilder();\n"
            "        while (n > 0) {\n"
            "            sb.append(digits.charAt(n % b));\n"
            "            n /= b;\n"
            "        }\n"
            "        return sb.reverse().toString();\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# n 을 b 진법 문자열로 변환\n"
            "def solution(n, b):\n"
            "    answer = \"\"\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="silver-47",
        rank="Silver",
        title="하노이 탑 이동 횟수",
        style="백준",
        topic="재귀",
        type="func",
        func_name="solution",
        description=(
            "원판 n 개가 첫 번째 기둥에 크기 순으로 쌓여 있다. 한 번에 한 개의 원판만 옮길 수 있고, "
            "큰 원판을 작은 원판 위에 올릴 수 없을 때, 모든 원판을 세 번째 기둥으로 옮기는 데 필요한 "
            "최소 이동 횟수를 구하세요."
        ),
        input_desc="n : 원판의 개수 (0 ≤ n)",
        output_desc="모든 원판을 옮기는 최소 이동 횟수",
        examples=[
            {"args": [3], "output": 7},
            {"args": [1], "output": 1},
        ],
        hints=[
            "원판 n 개를 옮기려면, 위쪽 n-1 개를 보조 기둥으로 옮기고 → 가장 큰 것을 옮기고 → n-1 개를 다시 옮겨야 합니다.",
            "재귀로 표현하면 move(n) = move(n-1) + 1 + move(n-1) = 2*move(n-1)+1, move(0)=0. 닫힌 식은 2^n - 1.",
            "def solution(n): return 0 if n==0 else 2*solution(n-1)+1  (또는 return 2**n - 1)",
        ],
        testcases=[
            {"args": [3], "expected": 7},
            {"args": [1], "expected": 1},
            {"args": [0], "expected": 0},
            {"args": [10], "expected": 1023},
            {"args": [20], "expected": 1048575},
        ],
        reference_py=(
            "def solution(n):\n"
            "    if n == 0:\n"
            "        return 0\n"
            "    return 2 * solution(n - 1) + 1\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public long solution(int n) {\n"
            "        if (n == 0) return 0;\n"
            "        return 2 * solution(n - 1) + 1;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 하노이 탑 최소 이동 횟수\n"
            "def solution(n):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="silver-48",
        rank="Silver",
        title="피보나치 수",
        style="해외대기업",
        topic="재귀",
        type="stdin",
        description=(
            "피보나치 수는 0과 1로 시작하며, n 번째 피보나치 수는 바로 앞 두 수의 합이다. "
            "즉 F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2) 이다. 정수 n 이 주어질 때 F(n) 을 출력하시오."
        ),
        input_desc="첫째 줄에 정수 n (0 ≤ n ≤ 90)",
        output_desc="n 번째 피보나치 수 F(n) 을 출력한다.",
        examples=[
            {"input": "10\n", "output": "55\n"},
            {"input": "1\n", "output": "1\n"},
        ],
        hints=[
            "정의 그대로 단순 재귀로 짜면 같은 값을 여러 번 다시 계산해 매우 느려집니다. 작은 값부터 차곡차곡 쌓아 보세요.",
            "두 변수 a, b 를 F(0), F(1) 로 두고 n 번 (a, b) = (b, a+b) 로 갱신하는 반복(또는 메모이제이션)을 쓰세요.",
            "a,b=0,1; for _ in range(n): a,b=b,a+b → print(a)",
        ],
        testcases=[
            {"input": "10\n", "output": "55\n"},
            {"input": "1\n", "output": "1\n"},
            {"input": "0\n", "output": "0\n"},
            {"input": "15\n", "output": "610\n"},
            {"input": "20\n", "output": "6765\n"},
        ],
        reference_py=(
            "n = int(input())\n"
            "a, b = 0, 1\n"
            "for _ in range(n):\n"
            "    a, b = b, a + b\n"
            "print(a)\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        int n = Integer.parseInt(br.readLine().trim());\n"
            "        long a = 0, b = 1;\n"
            "        for (int i = 0; i < n; i++) { long t = a + b; a = b; b = t; }\n"
            "        System.out.println(a);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# n 번째 피보나치 수\n"
            "n = int(input())\n"
            "# a, b = 0, 1\n"
        ),
    ),

    Problem(
        id="silver-49",
        rank="Silver",
        title="두 수의 합 존재 여부",
        style="해외대기업",
        topic="투포인터",
        type="func",
        func_name="solution",
        description=(
            "오름차순으로 정렬된 정수 배열 nums 에서 서로 다른 두 원소를 골라 그 합이 정확히 target 이 "
            "되는 쌍이 존재하는지 판별하세요. 존재하면 True, 없으면 False 를 반환합니다."
        ),
        input_desc="nums : 오름차순 정렬된 정수 리스트, target : 목표 합",
        output_desc="합이 target 인 두 원소 쌍이 있으면 True, 없으면 False",
        examples=[
            {"args": [[2, 7, 11, 15], 9], "output": True},
            {"args": [[1, 2, 3, 4, 5], 10], "output": False},
        ],
        hints=[
            "모든 쌍을 이중 반복으로 확인할 수도 있지만, 배열이 정렬되어 있다는 점을 활용하면 더 빠릅니다.",
            "투 포인터를 쓰세요. 양쪽 끝에서 시작해 합이 작으면 왼쪽을 오른쪽으로, 크면 오른쪽을 왼쪽으로 옮깁니다.",
            "l,r=0,len(nums)-1; while l<r: s=nums[l]+nums[r]; s==target→True; s<target→l+=1; else r-=1",
        ],
        testcases=[
            {"args": [[2, 7, 11, 15], 9], "expected": True},
            {"args": [[1, 2, 3, 4, 5], 10], "expected": False},
            {"args": [[1, 2, 3, 4, 5], 9], "expected": True},
            {"args": [[], 5], "expected": False},
            {"args": [[3], 3], "expected": False},
        ],
        reference_py=(
            "def solution(nums, target):\n"
            "    l, r = 0, len(nums) - 1\n"
            "    while l < r:\n"
            "        s = nums[l] + nums[r]\n"
            "        if s == target:\n"
            "            return True\n"
            "        elif s < target:\n"
            "            l += 1\n"
            "        else:\n"
            "            r -= 1\n"
            "    return False\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public boolean solution(int[] nums, int target) {\n"
            "        int l = 0, r = nums.length - 1;\n"
            "        while (l < r) {\n"
            "            int s = nums[l] + nums[r];\n"
            "            if (s == target) return true;\n"
            "            else if (s < target) l++;\n"
            "            else r--;\n"
            "        }\n"
            "        return false;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 합이 target 인 두 원소 쌍 존재 여부\n"
            "def solution(nums, target):\n"
            "    answer = False\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="silver-50",
        rank="Silver",
        title="팩토리얼 끝 0의 개수",
        style="대기업",
        topic="수학",
        type="stdin",
        description=(
            "N! (N 팩토리얼) 을 계산했을 때, 수의 끝에 연속으로 나타나는 0 의 개수를 구하시오. "
            "예를 들어 5! = 120 이므로 끝 0 의 개수는 1 이다."
        ),
        input_desc="첫째 줄에 정수 N (0 ≤ N ≤ 1,000,000)",
        output_desc="N! 의 끝에 연속으로 오는 0 의 개수를 출력한다.",
        examples=[
            {"input": "5\n", "output": "1\n"},
            {"input": "25\n", "output": "6\n"},
        ],
        hints=[
            "끝의 0 은 10 = 2×5 에서 생깁니다. 1부터 N 까지의 곱에서 2 는 5 보다 훨씬 많으니, 무엇의 개수를 세면 될까요?",
            "N! 안에 들어 있는 소인수 5 의 개수가 곧 끝 0 의 개수입니다. 5의 배수, 25의 배수, 125의 배수 … 를 모두 더하세요.",
            "cnt=0; p=5; while p<=N: cnt += N//p; p*=5 → print(cnt)",
        ],
        testcases=[
            {"input": "5\n", "output": "1\n"},
            {"input": "25\n", "output": "6\n"},
            {"input": "0\n", "output": "0\n"},
            {"input": "10\n", "output": "2\n"},
            {"input": "100\n", "output": "24\n"},
        ],
        reference_py=(
            "n = int(input())\n"
            "cnt = 0\n"
            "p = 5\n"
            "while p <= n:\n"
            "    cnt += n // p\n"
            "    p *= 5\n"
            "print(cnt)\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        long n = Long.parseLong(br.readLine().trim());\n"
            "        long cnt = 0, p = 5;\n"
            "        while (p <= n) { cnt += n / p; p *= 5; }\n"
            "        System.out.println(cnt);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# N! 의 끝 0의 개수\n"
            "n = int(input())\n"
            "# cnt, p = 0, 5\n"
        ),
    ),

]
