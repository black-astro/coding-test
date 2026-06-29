"""투포인터 / 누적합 유형 실전 문제 모음.

연속 부분수열의 합·길이, 구간 합 질의, 슬라이딩 윈도우로 풀리는 4문제.
"""

from engine.models import Problem

CATEGORY = "투포인터/누적합"

PROBLEMS = [

    Problem(
        id="twopointer-01",
        rank="Silver",
        title="합이 목표인 연속 부분수열의 개수",
        style="네이버",
        topic="투포인터",
        type="func",
        func_name="solution",
        description=(
            "양의 정수로 이루어진 수열 nums 와 목표값 target 이 주어진다. 연속한 부분수열 중 "
            "원소의 합이 정확히 target 인 부분수열의 개수를 반환하세요. 모든 원소가 양수이므로 "
            "두 포인터로 효율적으로 셀 수 있습니다."
        ),
        input_desc=(
            "nums   : 양의 정수 리스트 (1 ≤ len ≤ 100000, 각 원소 ≥ 1)\n"
            "target : 찾고자 하는 구간 합 (정수)"
        ),
        output_desc="합이 target 인 연속 부분수열의 개수(정수)",
        examples=[
            {"args": [[1, 2, 3, 4, 5], 5], "output": 2},
            {"args": [[1, 1, 1], 2], "output": 2},
        ],
        hints=[
            "모든 시작/끝 쌍을 직접 더하면 느립니다. 원소가 모두 양수라는 점을 이용하면, "
            "구간을 늘리면 합이 늘고 줄이면 합이 준다는 성질을 쓸 수 있습니다.",
            "왼쪽(left)·오른쪽(right) 두 포인터로 창을 만드세요. right 를 늘려 합을 더하고, "
            "합이 target 을 넘으면 left 를 늘려 합을 줄입니다. 합이 정확히 target 이면 세면 됩니다.",
            "cur 에 nums[right] 를 더하고, while cur > target 이면 cur -= nums[left]; left += 1. "
            "그 후 cur == target 이면 cnt += 1. 모든 right 에 대해 반복합니다.",
        ],
        testcases=[
            {"args": [[1, 2, 3, 4, 5], 5], "expected": 2},
            {"args": [[1, 1, 1], 2], "expected": 2},
            {"args": [[3, 1, 2, 1, 3], 3], "expected": 4},
            {"args": [[5], 5], "expected": 1},
            {"args": [[1, 2, 3], 7], "expected": 0},
        ],
        reference_py=(
            "def solution(nums, target):\n"
            "    left = 0\n"
            "    cur = 0\n"
            "    cnt = 0\n"
            "    for right in range(len(nums)):\n"
            "        cur += nums[right]\n"
            "        while cur > target and left <= right:\n"
            "            cur -= nums[left]\n"
            "            left += 1\n"
            "        if cur == target:\n"
            "            cnt += 1\n"
            "    return cnt\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int[] nums, int target) {\n"
            "        int left = 0, cur = 0, cnt = 0;\n"
            "        for (int right = 0; right < nums.length; right++) {\n"
            "            cur += nums[right];\n"
            "            while (cur > target && left <= right) cur -= nums[left++];\n"
            "            if (cur == target) cnt++;\n"
            "        }\n"
            "        return cnt;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 합이 target 인 연속 부분수열의 개수를 반환하세요.\n"
            "def solution(nums, target):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="twopointer-02",
        rank="Silver",
        title="합 이상인 최소 길이 부분수열",
        style="쿠팡",
        topic="슬라이딩 윈도우",
        type="func",
        func_name="solution",
        description=(
            "양의 정수 수열 nums 와 목표값 target 이 주어진다. 원소의 합이 target 이상이 되는 "
            "연속 부분수열 중 가장 짧은 것의 길이를 반환하세요. 그런 부분수열이 하나도 없으면 "
            "0을 반환합니다."
        ),
        input_desc=(
            "nums   : 양의 정수 리스트 (1 ≤ len ≤ 100000, 각 원소 ≥ 1)\n"
            "target : 목표 합 (정수)"
        ),
        output_desc="합이 target 이상인 가장 짧은 연속 부분수열의 길이(없으면 0)",
        examples=[
            {"args": [[2, 3, 1, 2, 4, 3], 7], "output": 2},
            {"args": [[1, 1, 1, 1], 10], "output": 0},
        ],
        hints=[
            "길이를 하나씩 늘려 가며 모든 구간을 확인하면 느립니다. 창의 합이 충분히 커지면 "
            "왼쪽을 줄여서 더 짧게 만들 수 있다는 점에 주목하세요.",
            "투포인터(슬라이딩 윈도우)를 쓰세요. right 를 늘려 합을 키우고, 합이 target 이상이 "
            "되는 순간 left 를 늘리면서 가능한 한 창을 좁혀 최소 길이를 갱신합니다.",
            "cur += nums[right]; while cur >= target: best = min(best, right-left+1); "
            "cur -= nums[left]; left += 1. 끝까지 갱신이 없으면 0을 반환합니다.",
        ],
        testcases=[
            {"args": [[2, 3, 1, 2, 4, 3], 7], "expected": 2},
            {"args": [[1, 1, 1, 1], 10], "expected": 0},
            {"args": [[1, 2, 3, 4], 4], "expected": 1},
            {"args": [[1, 2, 3, 4, 5], 11], "expected": 3},
            {"args": [[5], 5], "expected": 1},
        ],
        reference_py=(
            "def solution(nums, target):\n"
            "    left = 0\n"
            "    cur = 0\n"
            "    best = float('inf')\n"
            "    for right in range(len(nums)):\n"
            "        cur += nums[right]\n"
            "        while cur >= target:\n"
            "            if right - left + 1 < best:\n"
            "                best = right - left + 1\n"
            "            cur -= nums[left]\n"
            "            left += 1\n"
            "    return best if best != float('inf') else 0\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int[] nums, int target) {\n"
            "        int left = 0, cur = 0, best = Integer.MAX_VALUE;\n"
            "        for (int right = 0; right < nums.length; right++) {\n"
            "            cur += nums[right];\n"
            "            while (cur >= target) {\n"
            "                best = Math.min(best, right - left + 1);\n"
            "                cur -= nums[left++];\n"
            "            }\n"
            "        }\n"
            "        return best == Integer.MAX_VALUE ? 0 : best;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 합이 target 이상인 최소 길이 부분수열의 길이(없으면 0)\n"
            "def solution(nums, target):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="twopointer-03",
        rank="Silver",
        title="구간 합 질의 처리",
        style="삼성",
        topic="누적합",
        type="stdin",
        description=(
            "길이 N의 수열과 Q개의 질의가 주어진다. 각 질의는 두 정수 i, j (1-based)로 주어지며 "
            "i번째부터 j번째까지의 합을 묻는다. 질의가 매우 많을 수 있으므로 매번 더하지 말고 "
            "누적합을 이용해 각 질의를 빠르게 처리하라."
        ),
        input_desc=(
            "첫째 줄에 N과 Q (1 ≤ N, Q ≤ 100000)\n"
            "둘째 줄에 N개의 정수\n"
            "다음 Q개의 줄에 각 질의 i j (1 ≤ i ≤ j ≤ N)"
        ),
        output_desc="각 질의에 대한 구간 합을 한 줄에 하나씩 출력한다.",
        examples=[
            {"input": "5 3\n5 4 3 2 1\n1 3\n2 4\n5 5\n", "output": "12\n9\n1\n"},
            {"input": "5 2\n1 2 3 4 5\n1 5\n3 3\n", "output": "15\n3\n"},
        ],
        hints=[
            "질의마다 i부터 j까지 직접 더하면 질의가 많을 때 시간이 폭발합니다. 미리 한 번만 "
            "계산해 두면 각 질의를 상수 시간에 답할 수 있습니다.",
            "누적합 배열 prefix 를 만드세요. prefix[k] 는 앞에서부터 k개 원소의 합입니다. "
            "그러면 i..j 구간 합은 prefix[j] - prefix[i-1] 입니다.",
            "prefix = [0]; for x in nums: prefix.append(prefix[-1] + x). "
            "각 질의 (i, j) 의 답은 prefix[j] - prefix[i-1] 를 출력하면 됩니다.",
        ],
        testcases=[
            {"input": "5 3\n5 4 3 2 1\n1 3\n2 4\n5 5\n", "output": "12\n9\n1\n"},
            {"input": "1 1\n10\n1 1\n", "output": "10\n"},
            {"input": "5 2\n1 2 3 4 5\n1 5\n3 3\n", "output": "15\n3\n"},
            {"input": "4 2\n-1 -2 -3 -4\n1 4\n2 3\n", "output": "-10\n-5\n"},
        ],
        reference_py=(
            "import sys\n"
            "data = sys.stdin.buffer.read().split()\n"
            "idx = 0\n"
            "n = int(data[idx]); idx += 1\n"
            "q = int(data[idx]); idx += 1\n"
            "prefix = [0] * (n + 1)\n"
            "for k in range(1, n + 1):\n"
            "    prefix[k] = prefix[k - 1] + int(data[idx]); idx += 1\n"
            "out = []\n"
            "for _ in range(q):\n"
            "    i = int(data[idx]); j = int(data[idx + 1]); idx += 2\n"
            "    out.append(str(prefix[j] - prefix[i - 1]))\n"
            "print('\\n'.join(out))\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int n = Integer.parseInt(st.nextToken());\n"
            "        int q = Integer.parseInt(st.nextToken());\n"
            "        long[] prefix = new long[n + 1];\n"
            "        st = new StringTokenizer(br.readLine());\n"
            "        for (int k = 1; k <= n; k++)\n"
            "            prefix[k] = prefix[k - 1] + Long.parseLong(st.nextToken());\n"
            "        StringBuilder sb = new StringBuilder();\n"
            "        for (int t = 0; t < q; t++) {\n"
            "            st = new StringTokenizer(br.readLine());\n"
            "            int i = Integer.parseInt(st.nextToken());\n"
            "            int j = Integer.parseInt(st.nextToken());\n"
            "            sb.append(prefix[j] - prefix[i - 1]).append('\\n');\n"
            "        }\n"
            "        System.out.print(sb);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "# 누적합으로 각 구간 합 질의를 처리하세요.\n"
            "data = sys.stdin.buffer.read().split()\n"
            "# ...\n"
        ),
    ),

    Problem(
        id="twopointer-04",
        rank="Gold",
        title="서로 다른 원소 K개 이하인 가장 긴 구간",
        style="카카오",
        topic="슬라이딩 윈도우",
        type="func",
        func_name="solution",
        description=(
            "정수 수열 nums 와 정수 k 가 주어진다. 연속한 구간 중 서로 다른 값의 종류가 k개 "
            "이하인 가장 긴 구간의 길이를 반환하세요. 빈 수열이면 0을 반환합니다."
        ),
        input_desc=(
            "nums : 정수 리스트 (0 ≤ len ≤ 100000)\n"
            "k    : 허용되는 서로 다른 값의 최대 종류 수 (k ≥ 1)"
        ),
        output_desc="서로 다른 값이 k개 이하인 가장 긴 연속 구간의 길이(정수)",
        examples=[
            {"args": [[1, 2, 1, 2, 3], 2], "output": 4},
            {"args": [[1, 2, 3, 4, 5], 1], "output": 1},
        ],
        hints=[
            "모든 구간을 다 확인하면 느립니다. 구간을 오른쪽으로 늘리다가 종류가 너무 많아지면 "
            "왼쪽을 줄여 가며 조건을 회복한다는 슬라이딩 윈도우 아이디어를 떠올리세요.",
            "창 안의 값별 개수를 딕셔너리로 관리하고, 서로 다른 종류 수(distinct)를 함께 셉니다. "
            "right 를 늘려 새 값을 넣고, distinct > k 이면 left 를 늘려 값을 빼며 회복합니다.",
            "right 에서 count[nums[right]] 가 0->1 이면 distinct += 1. "
            "while distinct > k: count[nums[left]] -= 1; 0이 되면 distinct -= 1; left += 1. "
            "매 단계 best = max(best, right - left + 1).",
        ],
        testcases=[
            {"args": [[1, 2, 1, 2, 3], 2], "expected": 4},
            {"args": [[1, 2, 3, 4, 5], 1], "expected": 1},
            {"args": [[1, 1, 1, 1], 3], "expected": 4},
            {"args": [[1, 2, 1, 3, 4], 2], "expected": 3},
            {"args": [[], 2], "expected": 0},
        ],
        reference_py=(
            "from collections import defaultdict\n"
            "def solution(nums, k):\n"
            "    count = defaultdict(int)\n"
            "    left = 0\n"
            "    distinct = 0\n"
            "    best = 0\n"
            "    for right in range(len(nums)):\n"
            "        if count[nums[right]] == 0:\n"
            "            distinct += 1\n"
            "        count[nums[right]] += 1\n"
            "        while distinct > k:\n"
            "            count[nums[left]] -= 1\n"
            "            if count[nums[left]] == 0:\n"
            "                distinct -= 1\n"
            "            left += 1\n"
            "        if right - left + 1 > best:\n"
            "            best = right - left + 1\n"
            "    return best\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int solution(int[] nums, int k) {\n"
            "        HashMap<Integer, Integer> count = new HashMap<>();\n"
            "        int left = 0, distinct = 0, best = 0;\n"
            "        for (int right = 0; right < nums.length; right++) {\n"
            "            int v = nums[right];\n"
            "            if (count.getOrDefault(v, 0) == 0) distinct++;\n"
            "            count.put(v, count.getOrDefault(v, 0) + 1);\n"
            "            while (distinct > k) {\n"
            "                int lv = nums[left];\n"
            "                count.put(lv, count.get(lv) - 1);\n"
            "                if (count.get(lv) == 0) distinct--;\n"
            "                left++;\n"
            "            }\n"
            "            best = Math.max(best, right - left + 1);\n"
            "        }\n"
            "        return best;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 서로 다른 원소가 k개 이하인 가장 긴 구간의 길이\n"
            "def solution(nums, k):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

]
