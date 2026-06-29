"""이분탐색 / 파라메트릭 서치 유형 실전 문제 모음.

입국심사, 예산 배정, 나무 자르기, 공유기 설치 등 '답을 직접 찾지 말고
답을 가정해 가능/불가능을 판정'하는 파라메트릭 서치 4문제.
"""

from engine.models import Problem

CATEGORY = "이분탐색"

PROBLEMS = [

    Problem(
        id="binsearch-01",
        rank="Gold",
        title="입국심사 최소 시간",
        style="프로그래머스",
        topic="파라메트릭 서치",
        type="func",
        func_name="solution",
        description=(
            "공항에 입국하려는 사람이 n명 있다. 각 심사대가 한 명을 심사하는 데 걸리는 시간이 "
            "times 로 주어진다. 모든 심사대는 동시에 일하며, 한 심사대는 앞사람 심사가 끝나야 "
            "다음 사람을 받는다. n명이 모두 심사를 마치는 데 걸리는 최소 시간을 반환하세요."
        ),
        input_desc=(
            "n     : 심사받을 사람 수 (1 ≤ n ≤ 1000000000)\n"
            "times : 각 심사관이 한 명을 심사하는 시간 리스트 (1 ≤ 원소 ≤ 1000000000)"
        ),
        output_desc="모든 사람이 심사를 마치는 데 필요한 최소 시간(정수)",
        examples=[
            {"args": [6, [7, 10]], "output": 28},
            {"args": [5, [2, 3]], "output": 6},
        ],
        hints=[
            "'몇 명을 심사할 수 있나'를 직접 구하긴 어렵지만, '시간 T가 주어지면 그동안 몇 명을 "
            "심사할 수 있나'는 쉽게 계산됩니다. 답(시간)을 가정해 보는 방향으로 생각하세요.",
            "시간 T에 대해 각 심사관은 T // time 명을 처리하므로 총 처리 인원은 그 합입니다. "
            "이 인원이 n 이상이면 T는 충분합니다. 충분한 최소 T를 이분탐색으로 찾으세요.",
            "lo=1, hi=max(times)*n. mid 에서 sum(mid // t) >= n 이면 hi=mid, 아니면 lo=mid+1. "
            "lo == hi 가 되면 그 값이 답입니다.",
        ],
        testcases=[
            {"args": [6, [7, 10]], "expected": 28},
            {"args": [1, [1]], "expected": 1},
            {"args": [10, [1]], "expected": 10},
            {"args": [5, [2, 3]], "expected": 6},
        ],
        reference_py=(
            "def solution(n, times):\n"
            "    lo, hi = 1, max(times) * n\n"
            "    while lo < hi:\n"
            "        mid = (lo + hi) // 2\n"
            "        done = sum(mid // t for t in times)\n"
            "        if done >= n:\n"
            "            hi = mid\n"
            "        else:\n"
            "            lo = mid + 1\n"
            "    return lo\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public long solution(int n, int[] times) {\n"
            "        long lo = 1, hi = 0;\n"
            "        for (int t : times) hi = Math.max(hi, (long) t * n);\n"
            "        while (lo < hi) {\n"
            "            long mid = (lo + hi) / 2;\n"
            "            long done = 0;\n"
            "            for (int t : times) done += mid / t;\n"
            "            if (done >= n) hi = mid; else lo = mid + 1;\n"
            "        }\n"
            "        return lo;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 모든 사람이 심사를 마치는 최소 시간을 반환하세요.\n"
            "def solution(n, times):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="binsearch-02",
        rank="Silver",
        title="예산 배정 상한",
        style="삼성",
        topic="파라메트릭 서치",
        type="stdin",
        description=(
            "각 지방의 예산 요청 금액과 총예산이 주어진다. 모든 요청을 들어줄 수 없으면 상한액을 "
            "정해, 요청액이 상한보다 크면 상한만큼만, 작거나 같으면 요청액 그대로 배정한다. "
            "배정 총액이 총예산을 넘지 않으면서 상한을 최대로 할 때, 그 상한을 출력하라. "
            "(모든 요청을 들어줄 수 있으면 요청액 중 최댓값을 출력한다.)"
        ),
        input_desc=(
            "첫째 줄에 지방의 수 N (1 ≤ N ≤ 10000)\n"
            "둘째 줄에 각 지방의 요청 금액 N개 (1 ≤ 금액 ≤ 100000)\n"
            "셋째 줄에 총예산 M (N ≤ M ≤ 1000000000)"
        ),
        output_desc="가능한 최대 상한액(정수)을 한 줄에 출력한다.",
        examples=[
            {"input": "4\n120 110 140 150\n485\n", "output": "127\n"},
            {"input": "3\n110 90 90\n290\n", "output": "110\n"},
        ],
        hints=[
            "상한을 직접 구하긴 어렵지만, '상한을 x로 정하면 배정 총액이 얼마인가'는 쉽게 "
            "계산됩니다. 상한 x가 커지면 배정 총액도 늘어난다는 단조성을 이용하세요.",
            "상한 x에 대한 배정 총액은 sum(min(요청액, x)) 입니다. 이 값이 총예산 이하가 되는 "
            "최대 x를 이분탐색으로 찾습니다. (요청 합이 총예산 이하이면 곧장 최댓값이 답입니다.)",
            "lo=0, hi=max(req). mid=(lo+hi+1)//2 에서 sum(min(r, mid)) <= M 이면 lo=mid, "
            "아니면 hi=mid-1. 최종 lo 가 답입니다.",
        ],
        testcases=[
            {"input": "4\n120 110 140 150\n485\n", "output": "127\n"},
            {"input": "3\n110 90 90\n290\n", "output": "110\n"},
            {"input": "5\n70 80 30 40 100\n450\n", "output": "100\n"},
            {"input": "1\n100\n50\n", "output": "50\n"},
        ],
        reference_py=(
            "import sys\n"
            "data = sys.stdin.buffer.read().split()\n"
            "n = int(data[0])\n"
            "req = [int(x) for x in data[1:1 + n]]\n"
            "m = int(data[1 + n])\n"
            "if sum(req) <= m:\n"
            "    print(max(req))\n"
            "else:\n"
            "    lo, hi = 0, max(req)\n"
            "    while lo < hi:\n"
            "        mid = (lo + hi + 1) // 2\n"
            "        total = sum(min(r, mid) for r in req)\n"
            "        if total <= m:\n"
            "            lo = mid\n"
            "        else:\n"
            "            hi = mid - 1\n"
            "    print(lo)\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        int n = Integer.parseInt(br.readLine().trim());\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int[] req = new int[n];\n"
            "        int maxReq = 0; long sum = 0;\n"
            "        for (int i = 0; i < n; i++) {\n"
            "            req[i] = Integer.parseInt(st.nextToken());\n"
            "            maxReq = Math.max(maxReq, req[i]); sum += req[i];\n"
            "        }\n"
            "        long m = Long.parseLong(br.readLine().trim());\n"
            "        if (sum <= m) { System.out.println(maxReq); return; }\n"
            "        int lo = 0, hi = maxReq;\n"
            "        while (lo < hi) {\n"
            "            int mid = (lo + hi + 1) / 2;\n"
            "            long total = 0;\n"
            "            for (int r : req) total += Math.min(r, mid);\n"
            "            if (total <= m) lo = mid; else hi = mid - 1;\n"
            "        }\n"
            "        System.out.println(lo);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "# 가능한 최대 예산 상한을 출력하세요.\n"
            "data = sys.stdin.buffer.read().split()\n"
            "# ...\n"
        ),
    ),

    Problem(
        id="binsearch-03",
        rank="Silver",
        title="나무 자르기 최대 높이",
        style="소프티어",
        topic="파라메트릭 서치",
        type="stdin",
        description=(
            "절단기에 높이 H를 설정하면 모든 나무를 H 높이에서 자른다. 높이 H보다 큰 나무는 "
            "H 위로 잘리고, 작은 나무는 잘리지 않는다. 잘려 나간 나무의 총 길이가 적어도 M이 "
            "되도록 하려고 한다. M만큼의 나무를 집으로 가져갈 수 있는 절단기 높이 H의 최댓값을 "
            "구하라. (H는 0 이상의 정수)"
        ),
        input_desc=(
            "첫째 줄에 나무의 수 N과 필요한 나무 길이 M (1 ≤ N ≤ 1000000, 1 ≤ M ≤ 2000000000, "
            "단 M이 0일 수도 있다)\n"
            "둘째 줄에 각 나무의 높이 N개 (1 ≤ 높이 ≤ 1000000000)"
        ),
        output_desc="적어도 M 길이를 얻을 수 있는 절단기 높이의 최댓값(정수)을 출력한다.",
        examples=[
            {"input": "4 7\n20 15 10 17\n", "output": "15\n"},
            {"input": "5 20\n4 42 40 26 46\n", "output": "36\n"},
        ],
        hints=[
            "절단기 높이 H가 커지면 얻는 나무 길이는 줄어듭니다. 이 단조성 덕분에 'H일 때 얻는 "
            "길이 >= M' 을 만족하는 최대 H를 이분탐색으로 찾을 수 있습니다.",
            "높이 H에서 얻는 길이는 sum(나무높이 - H, 단 나무높이 > H 인 것만) 입니다. "
            "이 값이 M 이상이면 H를 더 높여 보고, 모자라면 낮춰야 합니다.",
            "lo=0, hi=max(trees). mid=(lo+hi+1)//2 에서 sum(t-mid for t in trees if t>mid) >= M "
            "이면 lo=mid, 아니면 hi=mid-1. 최종 lo 가 답입니다.",
        ],
        testcases=[
            {"input": "4 7\n20 15 10 17\n", "output": "15\n"},
            {"input": "5 20\n4 42 40 26 46\n", "output": "36\n"},
            {"input": "3 8\n10 10 10\n", "output": "7\n"},
            {"input": "1 0\n5\n", "output": "5\n"},
        ],
        reference_py=(
            "import sys\n"
            "data = sys.stdin.buffer.read().split()\n"
            "n = int(data[0]); m = int(data[1])\n"
            "trees = [int(x) for x in data[2:2 + n]]\n"
            "lo, hi = 0, max(trees)\n"
            "while lo < hi:\n"
            "    mid = (lo + hi + 1) // 2\n"
            "    total = 0\n"
            "    for t in trees:\n"
            "        if t > mid:\n"
            "            total += t - mid\n"
            "    if total >= m:\n"
            "        lo = mid\n"
            "    else:\n"
            "        hi = mid - 1\n"
            "print(lo)\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int n = Integer.parseInt(st.nextToken());\n"
            "        long m = Long.parseLong(st.nextToken());\n"
            "        int[] trees = new int[n];\n"
            "        int max = 0;\n"
            "        st = new StringTokenizer(br.readLine());\n"
            "        for (int i = 0; i < n; i++) {\n"
            "            trees[i] = Integer.parseInt(st.nextToken());\n"
            "            max = Math.max(max, trees[i]);\n"
            "        }\n"
            "        int lo = 0, hi = max;\n"
            "        while (lo < hi) {\n"
            "            int mid = (int)(((long) lo + hi + 1) / 2);\n"
            "            long total = 0;\n"
            "            for (int t : trees) if (t > mid) total += t - mid;\n"
            "            if (total >= m) lo = mid; else hi = mid - 1;\n"
            "        }\n"
            "        System.out.println(lo);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "# 적어도 M 길이를 얻는 절단기 높이의 최댓값을 출력\n"
            "data = sys.stdin.buffer.read().split()\n"
            "# ...\n"
        ),
    ),

    Problem(
        id="binsearch-04",
        rank="Gold",
        title="공유기 설치 최대 최소거리",
        style="현대",
        topic="파라메트릭 서치",
        type="func",
        func_name="solution",
        description=(
            "수직선 위 여러 집의 좌표 houses 가 주어진다. 이 집들 중 c곳에 공유기를 설치하려고 "
            "한다. 가장 가까운 두 공유기 사이의 거리를 최대가 되도록 설치할 때, 그 최댓값을 "
            "반환하세요."
        ),
        input_desc=(
            "houses : 집의 좌표 리스트 (2 ≤ len ≤ 200000, 각 좌표는 서로 다른 정수)\n"
            "c      : 설치할 공유기 수 (2 ≤ c ≤ len(houses))"
        ),
        output_desc="가장 인접한 두 공유기 사이 거리의 최댓값(정수)",
        examples=[
            {"args": [[1, 2, 8, 4, 9], 3], "output": 3},
            {"args": [[1, 2, 3, 4, 5], 2], "output": 4},
        ],
        hints=[
            "공유기 배치를 직접 다 시도할 순 없습니다. 대신 '인접 거리를 최소 d 이상으로 두면 "
            "공유기를 몇 대 놓을 수 있나'를 생각하면, d가 커질수록 놓을 수 있는 대수가 줄어듭니다.",
            "집을 좌표순으로 정렬한 뒤, 거리 d에 대해 그리디로 공유기를 놓아 봅니다. 직전 설치 "
            "위치에서 d 이상 떨어진 집마다 공유기를 놓고, 놓은 수가 c 이상이면 d는 가능합니다.",
            "houses.sort(); lo=1, hi=houses[-1]-houses[0]. mid 로 그리디 카운트해 cnt>=c 이면 "
            "answer=mid; lo=mid+1, 아니면 hi=mid-1. 가능했던 최대 mid 가 답입니다.",
        ],
        testcases=[
            {"args": [[1, 2, 8, 4, 9], 3], "expected": 3},
            {"args": [[1, 2, 3, 4, 5], 2], "expected": 4},
            {"args": [[1, 2, 3, 4, 5], 5], "expected": 1},
            {"args": [[10, 20, 30], 2], "expected": 20},
        ],
        reference_py=(
            "def solution(houses, c):\n"
            "    houses.sort()\n"
            "    lo, hi = 1, houses[-1] - houses[0]\n"
            "    answer = 0\n"
            "    while lo <= hi:\n"
            "        mid = (lo + hi) // 2\n"
            "        cnt = 1\n"
            "        last = houses[0]\n"
            "        for h in houses[1:]:\n"
            "            if h - last >= mid:\n"
            "                cnt += 1\n"
            "                last = h\n"
            "        if cnt >= c:\n"
            "            answer = mid\n"
            "            lo = mid + 1\n"
            "        else:\n"
            "            hi = mid - 1\n"
            "    return answer\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int solution(int[] houses, int c) {\n"
            "        Arrays.sort(houses);\n"
            "        int lo = 1, hi = houses[houses.length - 1] - houses[0], answer = 0;\n"
            "        while (lo <= hi) {\n"
            "            int mid = (lo + hi) / 2;\n"
            "            int cnt = 1, last = houses[0];\n"
            "            for (int i = 1; i < houses.length; i++) {\n"
            "                if (houses[i] - last >= mid) { cnt++; last = houses[i]; }\n"
            "            }\n"
            "            if (cnt >= c) { answer = mid; lo = mid + 1; }\n"
            "            else hi = mid - 1;\n"
            "        }\n"
            "        return answer;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 가장 인접한 두 공유기 사이 거리의 최댓값을 반환하세요.\n"
            "def solution(houses, c):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

]
