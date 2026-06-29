"""유형별 실전 — 유니온파인드 (분리 집합).

각 문제는 Problem 객체 하나로 표현된다.
"""

from engine.models import Problem

CATEGORY = "유니온파인드"

PROBLEMS = [

    Problem(
        id="union-01",
        rank="Gold",
        title="네트워크 그룹 수",
        style="프로그래머스",
        topic="유니온파인드",
        type="func",
        func_name="solution",
        description=(
            "컴퓨터 n대가 있고, 일부는 케이블로 직접 연결되어 있다. A가 B와 연결되어 있고 "
            "B가 C와 연결되어 있으면 A와 C도 같은 네트워크에 속한다. 연결 관계는 "
            "n x n 인접 행렬 computers 로 주어지며, computers[i][j]=1 이면 i번과 j번이 직접 연결되어 있다. "
            "(자기 자신 computers[i][i] 는 항상 1, 행렬은 대칭이다.) 전체 네트워크의 개수를 구하세요."
        ),
        input_desc=(
            "n : 컴퓨터 수 (1 ≤ n ≤ 200), "
            "computers : n x n 인접 행렬 (0/1, 0-based)"
        ),
        output_desc="서로 분리된 네트워크의 개수",
        examples=[
            {"args": [3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]], "output": 2},
            {"args": [3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]], "output": 1},
        ],
        hints=[
            "서로 연결된 컴퓨터들을 하나의 '그룹'으로 묶고, 마지막에 그룹이 몇 개인지 세는 문제입니다.",
            "유니온파인드(분리 집합)를 쓰세요. computers[i][j]==1 인 모든 쌍을 union 하고, 서로 다른 루트의 개수를 세면 됩니다. (DFS/BFS 로도 가능)",
            "parent=list(range(n)); 모든 i<j 에 대해 computers[i][j]==1 이면 union(i,j); 답은 len({find(i) for i in range(n)}).",
        ],
        testcases=[
            {"args": [3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]], "expected": 2},
            {"args": [3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]], "expected": 1},
            {"args": [3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]]], "expected": 3},
            {"args": [1, [[1]]], "expected": 1},
            {"args": [4, [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]], "expected": 2},
        ],
        reference_py=(
            "def solution(n, computers):\n"
            "    parent = list(range(n))\n"
            "\n"
            "    def find(x):\n"
            "        while parent[x] != x:\n"
            "            parent[x] = parent[parent[x]]\n"
            "            x = parent[x]\n"
            "        return x\n"
            "\n"
            "    def union(a, b):\n"
            "        ra, rb = find(a), find(b)\n"
            "        if ra != rb:\n"
            "            parent[ra] = rb\n"
            "\n"
            "    for i in range(n):\n"
            "        for j in range(i + 1, n):\n"
            "            if computers[i][j] == 1:\n"
            "                union(i, j)\n"
            "    return len({find(i) for i in range(n)})\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    int[] parent;\n"
            "    int find(int x) {\n"
            "        while (parent[x] != x) { parent[x] = parent[parent[x]]; x = parent[x]; }\n"
            "        return x;\n"
            "    }\n"
            "    void union(int a, int b) {\n"
            "        int ra = find(a), rb = find(b);\n"
            "        if (ra != rb) parent[ra] = rb;\n"
            "    }\n"
            "    public int solution(int n, int[][] computers) {\n"
            "        parent = new int[n];\n"
            "        for (int i = 0; i < n; i++) parent[i] = i;\n"
            "        for (int i = 0; i < n; i++)\n"
            "            for (int j = i + 1; j < n; j++)\n"
            "                if (computers[i][j] == 1) union(i, j);\n"
            "        java.util.Set<Integer> roots = new java.util.HashSet<>();\n"
            "        for (int i = 0; i < n; i++) roots.add(find(i));\n"
            "        return roots.size();\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 네트워크 그룹 수 : 인접 행렬에서 분리된 네트워크 개수\n"
            "def solution(n, computers):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="union-02",
        rank="Gold",
        title="최소 비용 네트워크 연결",
        style="삼성",
        topic="최소신장트리",
        type="stdin",
        description=(
            "V개의 컴퓨터를 케이블로 연결하려고 한다. 두 컴퓨터를 직접 잇는 케이블 후보들이 "
            "각각의 설치 비용과 함께 주어진다. 모든 컴퓨터가 (직접 또는 간접으로) 서로 통신할 수 있도록 "
            "케이블 일부를 골라 설치할 때, 필요한 최소 총비용을 구하시오. "
            "입력으로 주어지는 케이블만으로 모든 컴퓨터를 연결할 수 있음이 보장된다."
        ),
        input_desc=(
            "첫째 줄에 V E (컴퓨터 수, 케이블 후보 수, 1 ≤ V ≤ 10000). "
            "다음 E개의 줄에 a b c (a번과 b번을 잇는 비용 c 케이블). 컴퓨터 번호는 1..V."
        ),
        output_desc="모든 컴퓨터를 연결하는 최소 총비용 (최소 신장 트리의 가중치 합).",
        examples=[
            {
                "input": "3\n3\n1 2 1\n2 3 2\n1 3 3\n",
                "output": "3\n",
            },
            {
                "input": "4\n5\n1 2 1\n1 3 2\n2 3 3\n3 4 4\n2 4 5\n",
                "output": "7\n",
            },
        ],
        hints=[
            "모든 정점을 잇되 비용을 최소로 — 최소 신장 트리(MST) 문제입니다.",
            "간선을 비용 오름차순으로 정렬한 뒤, 사이클을 만들지 않는 간선만 골라 더하는 크루스칼 알고리즘을 유니온파인드로 구현하세요.",
            "edges 를 비용순 정렬; 각 (c,a,b) 에 대해 find(a)!=find(b) 면 union 하고 total+=c. 정점 V개를 모두 연결하면 종료. total 출력.",
        ],
        testcases=[
            {
                "input": "3\n3\n1 2 1\n2 3 2\n1 3 3\n",
                "output": "3\n",
            },
            {
                "input": "4\n5\n1 2 1\n1 3 2\n2 3 3\n3 4 4\n2 4 5\n",
                "output": "7\n",
            },
            {
                "input": "1\n0\n",
                "output": "0\n",
            },
            {
                "input": "5\n7\n1 2 3\n1 3 5\n2 3 4\n2 4 6\n3 4 2\n4 5 7\n3 5 9\n",
                "output": "16\n",
            },
        ],
        reference_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "\n"
            "def main():\n"
            "    first = input().split()\n"
            "    v = int(first[0])\n"
            "    e = int(input())\n"
            "    edges = []\n"
            "    for _ in range(e):\n"
            "        a, b, c = map(int, input().split())\n"
            "        edges.append((c, a, b))\n"
            "    edges.sort()\n"
            "    parent = list(range(v + 1))\n"
            "\n"
            "    def find(x):\n"
            "        while parent[x] != x:\n"
            "            parent[x] = parent[parent[x]]\n"
            "            x = parent[x]\n"
            "        return x\n"
            "\n"
            "    total = 0\n"
            "    used = 0\n"
            "    for c, a, b in edges:\n"
            "        ra, rb = find(a), find(b)\n"
            "        if ra != rb:\n"
            "            parent[ra] = rb\n"
            "            total += c\n"
            "            used += 1\n"
            "            if used == v - 1:\n"
            "                break\n"
            "    print(total)\n"
            "\n"
            "main()\n"
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
            "        int v = Integer.parseInt(br.readLine().trim());\n"
            "        int e = Integer.parseInt(br.readLine().trim());\n"
            "        int[][] edges = new int[e][3];\n"
            "        for (int i = 0; i < e; i++) {\n"
            "            StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "            edges[i][1] = Integer.parseInt(st.nextToken());\n"
            "            edges[i][2] = Integer.parseInt(st.nextToken());\n"
            "            edges[i][0] = Integer.parseInt(st.nextToken());\n"
            "        }\n"
            "        Arrays.sort(edges, (x, y) -> Integer.compare(x[0], y[0]));\n"
            "        parent = new int[v + 1];\n"
            "        for (int i = 0; i <= v; i++) parent[i] = i;\n"
            "        long total = 0; int used = 0;\n"
            "        for (int[] ed : edges) {\n"
            "            int ra = find(ed[1]), rb = find(ed[2]);\n"
            "            if (ra != rb) { parent[ra] = rb; total += ed[0]; if (++used == v - 1) break; }\n"
            "        }\n"
            "        System.out.println(total);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "# 최소 비용 네트워크 연결 (크루스칼 MST)\n"
            "def main():\n"
            "    pass\n"
            "main()\n"
        ),
    ),

    Problem(
        id="union-03",
        rank="Gold",
        title="가장 큰 친구 그룹",
        style="네이버",
        topic="유니온파인드",
        type="func",
        func_name="solution",
        description=(
            "사람 n명이 1번부터 n번까지 번호로 구분된다. 두 사람이 친구라는 관계가 목록으로 주어지며, "
            "친구의 친구도 같은 친구 그룹에 속한다(친구 관계는 전이된다). 모든 친구 그룹 중 "
            "가장 많은 사람이 속한 그룹의 인원 수를 구하세요. (친구 관계가 하나도 없으면 각자 혼자이므로 1이다.)"
        ),
        input_desc=(
            "n : 사람 수 (1 ≤ n ≤ 100000), "
            "relations : 각 원소가 [a, b] 인 리스트 (a번과 b번이 친구). 번호는 1..n."
        ),
        output_desc="가장 큰 친구 그룹의 인원 수",
        examples=[
            {"args": [5, [[1, 2], [2, 3], [4, 5]]], "output": 3},
            {"args": [6, [[1, 2], [1, 3], [1, 4], [5, 6]]], "output": 4},
        ],
        hints=[
            "친구 관계로 이어지는 사람들을 하나의 집합으로 묶고, 각 집합의 크기 중 최댓값을 찾는 문제입니다.",
            "유니온파인드를 쓰되, 각 루트가 거느린 집합의 크기를 size 배열로 함께 관리하세요. union 할 때 작은 쪽 크기를 큰 쪽에 더합니다.",
            "union(a,b) 시 ra,rb 가 다르면 parent[ra]=rb; size[rb]+=size[ra]. 답은 max(size[find(i)] for i in 1..n).",
        ],
        testcases=[
            {"args": [5, [[1, 2], [2, 3], [4, 5]]], "expected": 3},
            {"args": [6, [[1, 2], [1, 3], [1, 4], [5, 6]]], "expected": 4},
            {"args": [3, []], "expected": 1},
            {"args": [1, []], "expected": 1},
            {"args": [4, [[1, 2], [3, 4], [2, 3]]], "expected": 4},
        ],
        reference_py=(
            "def solution(n, relations):\n"
            "    parent = list(range(n + 1))\n"
            "    size = [1] * (n + 1)\n"
            "\n"
            "    def find(x):\n"
            "        while parent[x] != x:\n"
            "            parent[x] = parent[parent[x]]\n"
            "            x = parent[x]\n"
            "        return x\n"
            "\n"
            "    def union(a, b):\n"
            "        ra, rb = find(a), find(b)\n"
            "        if ra != rb:\n"
            "            parent[ra] = rb\n"
            "            size[rb] += size[ra]\n"
            "\n"
            "    for a, b in relations:\n"
            "        union(a, b)\n"
            "    return max(size[find(i)] for i in range(1, n + 1))\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    int[] parent, size;\n"
            "    int find(int x) {\n"
            "        while (parent[x] != x) { parent[x] = parent[parent[x]]; x = parent[x]; }\n"
            "        return x;\n"
            "    }\n"
            "    void union(int a, int b) {\n"
            "        int ra = find(a), rb = find(b);\n"
            "        if (ra != rb) { parent[ra] = rb; size[rb] += size[ra]; }\n"
            "    }\n"
            "    public int solution(int n, int[][] relations) {\n"
            "        parent = new int[n + 1];\n"
            "        size = new int[n + 1];\n"
            "        for (int i = 0; i <= n; i++) { parent[i] = i; size[i] = 1; }\n"
            "        for (int[] r : relations) union(r[0], r[1]);\n"
            "        int best = 0;\n"
            "        for (int i = 1; i <= n; i++) best = Math.max(best, size[find(i)]);\n"
            "        return best;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 가장 큰 친구 그룹 : 친구 관계로 묶인 집합 중 최대 크기\n"
            "def solution(n, relations):\n"
            "    answer = 1\n"
            "    return answer\n"
        ),
    ),

]
