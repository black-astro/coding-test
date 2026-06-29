"""유형별 실전 — 세그먼트 트리.

각 문제는 Problem 객체 하나로 표현된다.
"""

from engine.models import Problem

CATEGORY = "세그먼트트리"

PROBLEMS = [

    Problem(
        id="segtree-01",
        rank="Platinum",
        title="구간 매출 합과 갱신",
        style="라인",
        topic="세그먼트트리",
        type="func",
        func_name="solution",
        description=(
            "어떤 가게의 날짜별 매출이 배열 sales 로 주어진다(1-based). 이후 다음 두 종류의 질의가 "
            "섞여 들어온다.\n"
            "  - [1, i, x] : i번째 날의 매출을 x 로 수정한다.\n"
            "  - [2, l, r] : l번째 날부터 r번째 날까지의 매출 합을 구한다.\n"
            "수정과 합 질의가 매우 많이 섞여 들어오므로, 모든 '2' 질의의 답을 순서대로 리스트로 반환하세요."
        ),
        input_desc=(
            "sales : 날짜별 매출 정수 리스트 (1 ≤ len ≤ 100000), "
            "queries : [1,i,x] (수정) 또는 [2,l,r] (구간 합) 의 리스트 (인덱스 1-based)"
        ),
        output_desc="'2' (구간 합) 질의들의 답을 순서대로 담은 리스트",
        examples=[
            {
                "args": [[1, 2, 3, 4, 5], [[2, 1, 3], [1, 2, 10], [2, 1, 3], [2, 4, 5]]],
                "output": [6, 14, 9],
            },
            {
                "args": [[3, 1, 4, 1, 5, 9, 2, 6], [[2, 2, 5], [1, 4, 10], [2, 2, 5], [2, 1, 8]]],
                "output": [11, 20, 40],
            },
        ],
        hints=[
            "매출이 계속 바뀌므로 누적합 배열을 매번 다시 만들면 너무 느립니다. 수정과 질의 둘 다 빠른 구조가 필요합니다.",
            "세그먼트 트리를 쓰세요. 리프는 각 날의 매출, 내부 노드는 자식 구간의 합. 점 갱신과 구간 합 질의 모두 O(log n) 입니다.",
            "size 를 n 이상의 2의 거듭제곱으로 잡고 tree 크기 2*size. update(i,x): 리프 갱신 후 부모로 올라가며 tree[p]=tree[2p]+tree[2p+1]. query(l,r): 반복형 세그트리 합. '2' 질의의 답만 모아 반환.",
        ],
        testcases=[
            {
                "args": [[1, 2, 3, 4, 5], [[2, 1, 3], [1, 2, 10], [2, 1, 3], [2, 4, 5]]],
                "expected": [6, 14, 9],
            },
            {
                "args": [[3, 1, 4, 1, 5, 9, 2, 6], [[2, 2, 5], [1, 4, 10], [2, 2, 5], [2, 1, 8]]],
                "expected": [11, 20, 40],
            },
            {
                "args": [[5, 5, 5], [[2, 1, 3], [1, 1, 0], [2, 1, 1]]],
                "expected": [15, 0],
            },
            {
                "args": [[10], [[2, 1, 1], [1, 1, 7], [2, 1, 1]]],
                "expected": [10, 7],
            },
        ],
        reference_py=(
            "def solution(sales, queries):\n"
            "    n = len(sales)\n"
            "    size = 1\n"
            "    while size < n:\n"
            "        size *= 2\n"
            "    tree = [0] * (2 * size)\n"
            "    for i in range(n):\n"
            "        tree[size + i] = sales[i]\n"
            "    for p in range(size - 1, 0, -1):\n"
            "        tree[p] = tree[2 * p] + tree[2 * p + 1]\n"
            "\n"
            "    def update(idx, val):\n"
            "        p = size + idx\n"
            "        tree[p] = val\n"
            "        p //= 2\n"
            "        while p:\n"
            "            tree[p] = tree[2 * p] + tree[2 * p + 1]\n"
            "            p //= 2\n"
            "\n"
            "    def query(l, r):\n"
            "        res = 0\n"
            "        l += size\n"
            "        r += size + 1\n"
            "        while l < r:\n"
            "            if l & 1:\n"
            "                res += tree[l]\n"
            "                l += 1\n"
            "            if r & 1:\n"
            "                r -= 1\n"
            "                res += tree[r]\n"
            "            l //= 2\n"
            "            r //= 2\n"
            "        return res\n"
            "\n"
            "    out = []\n"
            "    for q in queries:\n"
            "        if q[0] == 1:\n"
            "            update(q[1] - 1, q[2])\n"
            "        else:\n"
            "            out.append(query(q[1] - 1, q[2] - 1))\n"
            "    return out\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    long[] tree; int size;\n"
            "    public int[] solution(int[] sales, int[][] queries) {\n"
            "        int n = sales.length; size = 1;\n"
            "        while (size < n) size *= 2;\n"
            "        tree = new long[2 * size];\n"
            "        for (int i = 0; i < n; i++) tree[size + i] = sales[i];\n"
            "        for (int p = size - 1; p >= 1; p--) tree[p] = tree[2*p] + tree[2*p+1];\n"
            "        List<Integer> out = new ArrayList<>();\n"
            "        for (int[] q : queries) {\n"
            "            if (q[0] == 1) update(q[1] - 1, q[2]);\n"
            "            else out.add((int) query(q[1] - 1, q[2] - 1));\n"
            "        }\n"
            "        return out.stream().mapToInt(Integer::intValue).toArray();\n"
            "    }\n"
            "    void update(int idx, long val) {\n"
            "        int p = size + idx; tree[p] = val; p /= 2;\n"
            "        while (p >= 1) { tree[p] = tree[2*p] + tree[2*p+1]; p /= 2; }\n"
            "    }\n"
            "    long query(int l, int r) {\n"
            "        long res = 0; l += size; r += size + 1;\n"
            "        while (l < r) {\n"
            "            if ((l & 1) == 1) res += tree[l++];\n"
            "            if ((r & 1) == 1) res += tree[--r];\n"
            "            l /= 2; r /= 2;\n"
            "        }\n"
            "        return res;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 구간 매출 합과 갱신 : '2' 질의의 답 리스트 반환\n"
            "def solution(sales, queries):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="segtree-02",
        rank="Platinum",
        title="구간 최댓값 질의",
        style="현대",
        topic="세그먼트트리",
        type="stdin",
        description=(
            "N개의 정수 배열이 주어지고, 다음 두 종류의 질의가 Q개 들어온다.\n"
            "  - 1 i x : i번째(1-based) 원소를 x 로 바꾼다.\n"
            "  - 2 l r : l번째부터 r번째까지의 원소 중 최댓값을 출력한다.\n"
            "갱신과 최댓값 질의가 많이 섞여 들어오므로 세그먼트 트리로 처리하시오."
        ),
        input_desc=(
            "첫째 줄에 N Q (1 ≤ N ≤ 100000, 1 ≤ Q ≤ 100000). "
            "둘째 줄에 N개의 정수. 다음 Q개의 줄에 '1 i x' 또는 '2 l r' 형식의 질의."
        ),
        output_desc="각 '2 l r' 질의에 대해 해당 구간의 최댓값을 한 줄에 하나씩 출력.",
        examples=[
            {
                "input": "5 3\n1 3 2 5 4\n2 1 5\n1 3 10\n2 1 3\n",
                "output": "5\n10\n",
            },
            {
                "input": "6 4\n4 2 7 1 9 3\n2 2 4\n2 4 6\n1 5 0\n2 4 6\n",
                "output": "7\n9\n3\n",
            },
        ],
        hints=[
            "원소가 계속 바뀌므로 매 질의마다 구간을 직접 훑으면 느립니다. 점 갱신과 구간 최댓값 둘 다 빠른 구조가 필요합니다.",
            "세그먼트 트리를 쓰되 내부 노드에 '자식 구간의 최댓값' 을 저장하세요. 갱신·질의 모두 O(log N) 입니다.",
            "리프 밖 빈 칸은 -무한대로 채우고, 내부 노드 tree[p]=max(tree[2p],tree[2p+1]). query(l,r): 반복형 세그트리에서 합 대신 max 로 모읍니다.",
        ],
        testcases=[
            {
                "input": "5 3\n1 3 2 5 4\n2 1 5\n1 3 10\n2 1 3\n",
                "output": "5\n10\n",
            },
            {
                "input": "6 4\n4 2 7 1 9 3\n2 2 4\n2 4 6\n1 5 0\n2 4 6\n",
                "output": "7\n9\n3\n",
            },
            {
                "input": "1 2\n7\n2 1 1\n1 1 3\n",
                "output": "7\n",
            },
            {
                "input": "3 1\n5 5 5\n2 1 3\n",
                "output": "5\n",
            },
        ],
        reference_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "\n"
            "def main():\n"
            "    n, q = map(int, input().split())\n"
            "    arr = list(map(int, input().split()))\n"
            "    size = 1\n"
            "    while size < n:\n"
            "        size *= 2\n"
            "    NEG = float('-inf')\n"
            "    tree = [NEG] * (2 * size)\n"
            "    for i in range(n):\n"
            "        tree[size + i] = arr[i]\n"
            "    for p in range(size - 1, 0, -1):\n"
            "        tree[p] = max(tree[2 * p], tree[2 * p + 1])\n"
            "\n"
            "    def update(idx, val):\n"
            "        p = size + idx\n"
            "        tree[p] = val\n"
            "        p //= 2\n"
            "        while p:\n"
            "            tree[p] = max(tree[2 * p], tree[2 * p + 1])\n"
            "            p //= 2\n"
            "\n"
            "    def query(l, r):\n"
            "        res = NEG\n"
            "        l += size\n"
            "        r += size + 1\n"
            "        while l < r:\n"
            "            if l & 1:\n"
            "                res = max(res, tree[l])\n"
            "                l += 1\n"
            "            if r & 1:\n"
            "                r -= 1\n"
            "                res = max(res, tree[r])\n"
            "            l //= 2\n"
            "            r //= 2\n"
            "        return res\n"
            "\n"
            "    out = []\n"
            "    for _ in range(q):\n"
            "        t = list(map(int, input().split()))\n"
            "        if t[0] == 1:\n"
            "            update(t[1] - 1, t[2])\n"
            "        else:\n"
            "            out.append(str(query(t[1] - 1, t[2] - 1)))\n"
            "    print('\\n'.join(out))\n"
            "\n"
            "main()\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    static long[] tree; static int size;\n"
            "    static final long NEG = Long.MIN_VALUE;\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int n = Integer.parseInt(st.nextToken());\n"
            "        int q = Integer.parseInt(st.nextToken());\n"
            "        size = 1;\n"
            "        while (size < n) size *= 2;\n"
            "        tree = new long[2 * size];\n"
            "        Arrays.fill(tree, NEG);\n"
            "        st = new StringTokenizer(br.readLine());\n"
            "        for (int i = 0; i < n; i++) tree[size + i] = Long.parseLong(st.nextToken());\n"
            "        for (int p = size - 1; p >= 1; p--) tree[p] = Math.max(tree[2*p], tree[2*p+1]);\n"
            "        StringBuilder sb = new StringBuilder();\n"
            "        for (int i = 0; i < q; i++) {\n"
            "            st = new StringTokenizer(br.readLine());\n"
            "            int type = Integer.parseInt(st.nextToken());\n"
            "            int a = Integer.parseInt(st.nextToken());\n"
            "            int b = Integer.parseInt(st.nextToken());\n"
            "            if (type == 1) update(a - 1, b);\n"
            "            else sb.append(query(a - 1, b - 1)).append('\\n');\n"
            "        }\n"
            "        System.out.print(sb);\n"
            "    }\n"
            "    static void update(int idx, long val) {\n"
            "        int p = size + idx; tree[p] = val; p /= 2;\n"
            "        while (p >= 1) { tree[p] = Math.max(tree[2*p], tree[2*p+1]); p /= 2; }\n"
            "    }\n"
            "    static long query(int l, int r) {\n"
            "        long res = NEG; l += size; r += size + 1;\n"
            "        while (l < r) {\n"
            "            if ((l & 1) == 1) res = Math.max(res, tree[l++]);\n"
            "            if ((r & 1) == 1) res = Math.max(res, tree[--r]);\n"
            "            l /= 2; r /= 2;\n"
            "        }\n"
            "        return res;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "# 구간 최댓값 질의 (점 갱신 + 구간 max)\n"
            "def main():\n"
            "    pass\n"
            "main()\n"
        ),
    ),

    Problem(
        id="segtree-03",
        rank="Platinum",
        title="구간 최솟값 질의",
        style="소프티어",
        topic="세그먼트트리",
        type="func",
        func_name="solution",
        description=(
            "정수 배열 arr 가 주어지고(1-based), 다음 두 종류의 질의가 섞여 들어온다.\n"
            "  - ['U', i, x] : i번째 원소를 x 로 바꾼다.\n"
            "  - ['Q', l, r] : l번째부터 r번째까지의 원소 중 최솟값을 구한다.\n"
            "갱신과 최솟값 질의가 많이 섞여 들어오므로, 모든 'Q' 질의의 답을 순서대로 리스트로 반환하세요."
        ),
        input_desc=(
            "arr : 정수 리스트 (1 ≤ len ≤ 100000), "
            "queries : ['U', i, x] (갱신) 또는 ['Q', l, r] (구간 최솟값) 의 리스트 (인덱스 1-based)"
        ),
        output_desc="'Q' (구간 최솟값) 질의들의 답을 순서대로 담은 리스트",
        examples=[
            {
                "args": [[5, 2, 7, 1, 9, 3], [["Q", 1, 6], ["U", 4, 10], ["Q", 1, 6], ["Q", 2, 3]]],
                "output": [1, 2, 2],
            },
            {
                "args": [[8, 6, 4, 2, 1, 3, 5, 7], [["Q", 3, 6], ["U", 5, 0], ["Q", 3, 6]]],
                "output": [1, 0],
            },
        ],
        hints=[
            "원소가 계속 바뀌므로 매 질의마다 구간 전체를 훑으면 느립니다. 점 갱신과 구간 최솟값 둘 다 빠른 구조가 필요합니다.",
            "세그먼트 트리를 쓰되 내부 노드에 '자식 구간의 최솟값' 을 저장하세요. 갱신·질의 모두 O(log n) 입니다.",
            "리프 밖 빈 칸은 +무한대로 채우고, 내부 노드 tree[p]=min(tree[2p],tree[2p+1]). query(l,r): 반복형 세그트리에서 min 으로 모아 'Q' 질의의 답만 반환.",
        ],
        testcases=[
            {
                "args": [[5, 2, 7, 1, 9, 3], [["Q", 1, 6], ["U", 4, 10], ["Q", 1, 6], ["Q", 2, 3]]],
                "expected": [1, 2, 2],
            },
            {
                "args": [[8, 6, 4, 2, 1, 3, 5, 7], [["Q", 3, 6], ["U", 5, 0], ["Q", 3, 6]]],
                "expected": [1, 0],
            },
            {
                "args": [[10], [["Q", 1, 1], ["U", 1, 3], ["Q", 1, 1]]],
                "expected": [10, 3],
            },
            {
                "args": [[4, 4, 4], [["Q", 1, 3], ["U", 2, 1], ["Q", 1, 3]]],
                "expected": [4, 1],
            },
        ],
        reference_py=(
            "def solution(arr, queries):\n"
            "    n = len(arr)\n"
            "    size = 1\n"
            "    while size < n:\n"
            "        size *= 2\n"
            "    INF = float('inf')\n"
            "    tree = [INF] * (2 * size)\n"
            "    for i in range(n):\n"
            "        tree[size + i] = arr[i]\n"
            "    for p in range(size - 1, 0, -1):\n"
            "        tree[p] = min(tree[2 * p], tree[2 * p + 1])\n"
            "\n"
            "    def update(idx, val):\n"
            "        p = size + idx\n"
            "        tree[p] = val\n"
            "        p //= 2\n"
            "        while p:\n"
            "            tree[p] = min(tree[2 * p], tree[2 * p + 1])\n"
            "            p //= 2\n"
            "\n"
            "    def query(l, r):\n"
            "        res = INF\n"
            "        l += size\n"
            "        r += size + 1\n"
            "        while l < r:\n"
            "            if l & 1:\n"
            "                res = min(res, tree[l])\n"
            "                l += 1\n"
            "            if r & 1:\n"
            "                r -= 1\n"
            "                res = min(res, tree[r])\n"
            "            l //= 2\n"
            "            r //= 2\n"
            "        return res\n"
            "\n"
            "    out = []\n"
            "    for q in queries:\n"
            "        if q[0] == 'U':\n"
            "            update(q[1] - 1, q[2])\n"
            "        else:\n"
            "            out.append(query(q[1] - 1, q[2] - 1))\n"
            "    return out\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    long[] tree; int size;\n"
            "    static final long INF = Long.MAX_VALUE;\n"
            "    public int[] solution(int[] arr, Object[][] queries) {\n"
            "        int n = arr.length; size = 1;\n"
            "        while (size < n) size *= 2;\n"
            "        tree = new long[2 * size];\n"
            "        Arrays.fill(tree, INF);\n"
            "        for (int i = 0; i < n; i++) tree[size + i] = arr[i];\n"
            "        for (int p = size - 1; p >= 1; p--) tree[p] = Math.min(tree[2*p], tree[2*p+1]);\n"
            "        List<Integer> out = new ArrayList<>();\n"
            "        for (Object[] q : queries) {\n"
            "            if (q[0].equals(\"U\")) update((int) q[1] - 1, (int) q[2]);\n"
            "            else out.add((int) query((int) q[1] - 1, (int) q[2] - 1));\n"
            "        }\n"
            "        return out.stream().mapToInt(Integer::intValue).toArray();\n"
            "    }\n"
            "    void update(int idx, long val) {\n"
            "        int p = size + idx; tree[p] = val; p /= 2;\n"
            "        while (p >= 1) { tree[p] = Math.min(tree[2*p], tree[2*p+1]); p /= 2; }\n"
            "    }\n"
            "    long query(int l, int r) {\n"
            "        long res = INF; l += size; r += size + 1;\n"
            "        while (l < r) {\n"
            "            if ((l & 1) == 1) res = Math.min(res, tree[l++]);\n"
            "            if ((r & 1) == 1) res = Math.min(res, tree[--r]);\n"
            "            l /= 2; r /= 2;\n"
            "        }\n"
            "        return res;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 구간 최솟값 질의 : 'Q' 질의의 답 리스트 반환\n"
            "def solution(arr, queries):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

]
