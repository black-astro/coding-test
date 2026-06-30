"""유형별 실전 — 완전탐색 / 백트래킹.

N개 중 M개 고르기(조합) / 메뉴 세트 할인 완전탐색 / 후보키 찾기 /
순열을 모두 탐색해 조건 만족 개수 세기.
"""

from engine.models import Problem

CATEGORY = "완전탐색/백트래킹"

PROBLEMS = [

    # ──────────────────────────────────────────────────────────────
    Problem(
        id="bruteforce-01",
        rank="Silver",
        title="N개 중 M개 고르기",
        style="삼성",
        topic="조합 백트래킹",
        type="stdin",
        category="완전탐색/백트래킹",
        description=(
            "1부터 N까지의 자연수 중에서 서로 다른 M개를 고르는 모든 경우를 출력하라. "
            "단, 한 경우 안의 수는 오름차순으로 적고, 경우들 사이의 순서는 사전순(앞 수가 작은 것 먼저, "
            "같으면 다음 수가 작은 것 먼저)으로 출력해야 한다.\n\n"
            "예를 들어 N=4, M=2이면 (1 2), (1 3), (1 4), (2 3), (2 4), (3 4) 순서로 출력한다."
        ),
        input_desc="첫째 줄에 자연수 N과 M이 공백으로 주어진다 (1 ≤ M ≤ N ≤ 8).",
        output_desc=(
            "한 줄에 하나의 조합을 공백으로 구분해 출력한다. 조합은 사전순으로 출력한다."
        ),
        examples=[
            {"input": "4 2\n", "output": "1 2\n1 3\n1 4\n2 3\n2 4\n3 4\n"},
            {"input": "3 3\n", "output": "1 2 3\n"},
        ],
        hints=[
            "수를 작은 것부터 차례로 '쓸지 말지' 고르되, 한 번 고른 수보다 큰 수만 다음 자리에 올 수 있게 하면 자연스럽게 오름차순·사전순이 됩니다.",
            "백트래킹으로 현재 고른 리스트와 '다음에 고를 수 있는 시작 값'을 들고 재귀하세요. M개를 다 고르면 출력. 또는 itertools.combinations(range(1,N+1), M)을 그대로 쓰면 이미 사전순입니다.",
            "from itertools import combinations; for c in combinations(range(1,n+1), m): print(' '.join(map(str,c)))",
        ],
        testcases=[
            {"input": "4 2\n", "output": "1 2\n1 3\n1 4\n2 3\n2 4\n3 4\n"},
            {"input": "3 3\n", "output": "1 2 3\n"},
            {"input": "1 1\n", "output": "1\n"},
            {"input": "4 1\n", "output": "1\n2\n3\n4\n"},
            {"input": "3 2\n", "output": "1 2\n1 3\n2 3\n"},
        ],
        reference_py=(
            "import sys\n"
            "from itertools import combinations\n"
            "input = sys.stdin.readline\n"
            "n, m = map(int, input().split())\n"
            "out = []\n"
            "for c in combinations(range(1, n + 1), m):\n"
            "    out.append(' '.join(map(str, c)))\n"
            "print('\\n'.join(out))\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    static int n, m;\n"
            "    static int[] pick;\n"
            "    static StringBuilder sb = new StringBuilder();\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        n = Integer.parseInt(st.nextToken());\n"
            "        m = Integer.parseInt(st.nextToken());\n"
            "        pick = new int[m];\n"
            "        rec(0, 1);\n"
            "        System.out.print(sb);\n"
            "    }\n"
            "    static void rec(int depth, int start) {\n"
            "        if (depth == m) {\n"
            "            for (int i = 0; i < m; i++) {\n"
            "                sb.append(pick[i]);\n"
            "                if (i < m - 1) sb.append(' ');\n"
            "            }\n"
            "            sb.append('\\n');\n"
            "            return;\n"
            "        }\n"
            "        for (int v = start; v <= n; v++) {\n"
            "            pick[depth] = v;\n"
            "            rec(depth + 1, v + 1);\n"
            "        }\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "# N개 중 M개 고르기 (조합, 사전순)\n"
            "n, m = map(int, input().split())\n"
            "# TODO: 백트래킹 또는 itertools.combinations 로 사전순 출력\n"
        ),
    ),

    # ──────────────────────────────────────────────────────────────
    Problem(
        id="bruteforce-02",
        rank="Silver",
        title="세트 메뉴 최대 결제액",
        style="카카오",
        topic="조합 완전탐색",
        type="func",
        func_name="solution",
        category="완전탐색/백트래킹",
        description=(
            "한 식당에서 서로 다른 메뉴 3개를 한 번에 주문하면 '세트 할인'이 적용되어, "
            "고른 3개 중 가장 싼 메뉴 1개의 가격만큼 합계에서 깎아 준다. "
            "즉 실제 결제액은 (세 메뉴 가격의 합) − (셋 중 최저가)이다.\n\n"
            "메뉴 가격 목록 menu와 예산 budget이 주어질 때, 결제액이 예산을 넘지 않는 "
            "(결제액 ≤ budget) 조합 중에서 결제액을 최대로 하는 값을 반환하라. "
            "메뉴가 3개 미만이거나 조건을 만족하는 조합이 하나도 없으면 -1을 반환한다."
        ),
        input_desc="menu : 메뉴 가격 리스트(정수), budget : 예산(정수)",
        output_desc="조건을 만족하는 최대 결제액. 불가능하면 -1.",
        examples=[
            {"args": [[1, 2, 3, 4], 10], "output": 7},
            {"args": [[5, 5, 5], 100], "output": 10},
        ],
        hints=[
            "메뉴 수가 적으므로 가능한 3개 조합을 모두 만들어 보고, 각 조합의 결제액을 직접 계산해 보면 됩니다(완전탐색).",
            "itertools.combinations(menu, 3)으로 모든 3개 조합을 순회하며 결제액 = 합 − 최저가를 구하고, budget 이하인 것들 중 최댓값을 갱신하세요.",
            "best=-1; for c in combinations(menu,3): pay=sum(c)-min(c); if pay<=budget and pay>best: best=pay; return best",
        ],
        testcases=[
            {"args": [[1, 2, 3, 4], 10], "expected": 7},
            {"args": [[5, 5, 5], 100], "expected": 10},
            {"args": [[10, 20], 50], "expected": -1},
            {"args": [[8, 8, 8], 10], "expected": -1},
            {"args": [[3, 1, 2, 7, 5], 9], "expected": 9},
        ],
        reference_py=(
            "from itertools import combinations\n"
            "def solution(menu, budget):\n"
            "    best = -1\n"
            "    for c in combinations(menu, 3):\n"
            "        pay = sum(c) - min(c)\n"
            "        if pay <= budget and pay > best:\n"
            "            best = pay\n"
            "    return best\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int solution(int[] menu, int budget) {\n"
            "        int n = menu.length, best = -1;\n"
            "        for (int i = 0; i < n; i++)\n"
            "            for (int j = i + 1; j < n; j++)\n"
            "                for (int k = j + 1; k < n; k++) {\n"
            "                    int sum = menu[i] + menu[j] + menu[k];\n"
            "                    int min = Math.min(menu[i], Math.min(menu[j], menu[k]));\n"
            "                    int pay = sum - min;\n"
            "                    if (pay <= budget && pay > best) best = pay;\n"
            "                }\n"
            "        return best;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "from itertools import combinations\n"
            "# 세트 메뉴 최대 결제액 (3개 조합 완전탐색)\n"
            "def solution(menu, budget):\n"
            "    answer = -1\n"
            "    return answer\n"
        ),
    ),

    # ──────────────────────────────────────────────────────────────
    Problem(
        id="bruteforce-03",
        rank="Gold",
        title="후보키 개수 구하기",
        style="프로그래머스",
        topic="부분집합 완전탐색",
        type="func",
        func_name="solution",
        category="완전탐색/백트래킹",
        description=(
            "관계형 데이터베이스의 릴레이션 relation이 2차원 리스트로 주어진다. "
            "각 행은 하나의 튜플이고, 각 열은 하나의 속성이다(값은 문자열).\n\n"
            "후보키는 다음 두 조건을 모두 만족하는 속성들의 집합이다.\n"
            " - 유일성: 그 속성들의 값 조합이 모든 행에서 서로 달라, 각 행을 유일하게 구분한다.\n"
            " - 최소성: 그 집합에서 어떤 속성을 빼도 더 이상 유일성을 만족하지 못한다 "
            "(즉, 유일성을 만족하는 더 작은 부분집합이 없다).\n\n"
            "주어진 릴레이션에서 후보키의 개수를 반환하라."
        ),
        input_desc="relation : 행(튜플)들의 리스트, 각 행은 같은 길이의 문자열 리스트(속성 값)",
        output_desc="후보키의 개수 (정수)",
        examples=[
            {"args": [[["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]], "output": 2},
            {"args": [[["a", "1"], ["b", "1"]]], "output": 1},
        ],
        hints=[
            "속성 수가 적으므로(보통 8개 이하) 속성들의 모든 부분집합을 만들어, 각 부분집합이 유일성을 만족하는지 직접 검사하는 완전탐색이 가능합니다.",
            "크기가 작은 부분집합부터 검사하세요. 유일성을 만족하면 후보키 후보로 저장하되, '이미 저장된 후보키의 상위집합'은 최소성을 어기므로 건너뜁니다.",
            "size를 1부터 늘리며 combinations(range(cols), size): 이미 찾은 후보키 중 부분집합이 있으면 skip; 각 행의 해당 열 값을 tuple로 모아 set 크기가 행 수와 같으면 후보키로 추가. 마지막에 후보키 개수 반환.",
        ],
        testcases=[
            {"args": [[["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]], "expected": 2},
            {"args": [[["a", "1"], ["b", "1"]]], "expected": 1},
            {"args": [[["a", "x"], ["a", "y"]]], "expected": 1},
            {"args": [[["1", "1", "1"]]], "expected": 3},
            {"args": [[["a", "b"], ["a", "b"]]], "expected": 0},
        ],
        reference_py=(
            "from itertools import combinations\n"
            "def solution(relation):\n"
            "    rows = len(relation)\n"
            "    cols = len(relation[0])\n"
            "    candidates = []\n"
            "    for size in range(1, cols + 1):\n"
            "        for cand in combinations(range(cols), size):\n"
            "            cset = set(cand)\n"
            "            if any(c.issubset(cset) for c in candidates):\n"
            "                continue\n"
            "            seen = set()\n"
            "            uniq = True\n"
            "            for r in relation:\n"
            "                key = tuple(r[i] for i in cand)\n"
            "                if key in seen:\n"
            "                    uniq = False\n"
            "                    break\n"
            "                seen.add(key)\n"
            "            if uniq:\n"
            "                candidates.append(cset)\n"
            "    return len(candidates)\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int solution(String[][] relation) {\n"
            "        int rows = relation.length, cols = relation[0].length;\n"
            "        List<Integer> candidates = new ArrayList<>();\n"
            "        for (int mask = 1; mask < (1 << cols); mask++) {\n"
            "            boolean superset = false;\n"
            "            for (int c : candidates) if ((mask & c) == c) { superset = true; break; }\n"
            "            if (superset) continue;\n"
            "            Set<String> seen = new HashSet<>();\n"
            "            boolean uniq = true;\n"
            "            for (int r = 0; r < rows; r++) {\n"
            "                StringBuilder key = new StringBuilder();\n"
            "                for (int c = 0; c < cols; c++)\n"
            "                    if ((mask & (1 << c)) != 0) key.append(relation[r][c]).append('#');\n"
            "                if (!seen.add(key.toString())) { uniq = false; break; }\n"
            "            }\n"
            "            if (uniq) candidates.add(mask);\n"
            "        }\n"
            "        return candidates.size();\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "from itertools import combinations\n"
            "# 후보키 개수 (유일성 + 최소성 완전탐색)\n"
            "def solution(relation):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    # ──────────────────────────────────────────────────────────────
    Problem(
        id="bruteforce-04",
        rank="Gold",
        title="소수 이웃 줄세우기",
        style="삼성",
        topic="순열 완전탐색",
        type="stdin",
        category="완전탐색/백트래킹",
        description=(
            "1부터 N까지의 수를 한 줄로 나란히 세운다. 이때 '서로 이웃한 두 수의 합이 항상 소수'가 "
            "되도록 세우는 방법(순열)의 가짓수를 구하라.\n\n"
            "예를 들어 N=3이면 (1 2 3)은 1+2=3, 2+3=5로 모두 소수라 조건을 만족하고, "
            "(2 1 3)은 1+3=4가 소수가 아니라 조건을 만족하지 않는다. N=1이면 이웃 쌍이 없으므로 "
            "유일한 줄세우기 1가지를 조건 만족으로 본다."
        ),
        input_desc="첫째 줄에 자연수 N (1 ≤ N ≤ 8).",
        output_desc="조건을 만족하는 줄세우기(순열)의 개수를 정수 한 줄로 출력한다.",
        examples=[
            {"input": "3\n", "output": "2\n"},
            {"input": "4\n", "output": "8\n"},
        ],
        hints=[
            "N이 작으므로 1..N의 모든 순열을 직접 만들어 보고, 각 순열이 조건을 만족하는지 일일이 확인하는 완전탐색이 가능합니다.",
            "itertools.permutations(range(1,N+1))로 모든 순열을 돌면서, 인접한 두 수의 합이 모두 소수인지 검사해 개수를 셉니다. 소수 판정은 간단한 함수로 미리 만들어 두세요.",
            "for p in permutations(range(1,n+1)): if all(is_prime(p[i]+p[i+1]) for i in range(n-1)): cnt+=1; print(cnt). N=1이면 all(빈 것)=True 라 1이 됩니다.",
        ],
        testcases=[
            {"input": "1\n", "output": "1\n"},
            {"input": "2\n", "output": "2\n"},
            {"input": "3\n", "output": "2\n"},
            {"input": "4\n", "output": "8\n"},
            {"input": "5\n", "output": "4\n"},
        ],
        reference_py=(
            "import sys\n"
            "from itertools import permutations\n"
            "def is_prime(x):\n"
            "    if x < 2:\n"
            "        return False\n"
            "    i = 2\n"
            "    while i * i <= x:\n"
            "        if x % i == 0:\n"
            "            return False\n"
            "        i += 1\n"
            "    return True\n"
            "n = int(sys.stdin.readline())\n"
            "cnt = 0\n"
            "for p in permutations(range(1, n + 1)):\n"
            "    if all(is_prime(p[i] + p[i + 1]) for i in range(n - 1)):\n"
            "        cnt += 1\n"
            "print(cnt)\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    static int n, cnt = 0;\n"
            "    static int[] perm;\n"
            "    static boolean[] used;\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        n = Integer.parseInt(br.readLine().trim());\n"
            "        perm = new int[n];\n"
            "        used = new boolean[n + 1];\n"
            "        rec(0);\n"
            "        System.out.println(cnt);\n"
            "    }\n"
            "    static boolean isPrime(int x) {\n"
            "        if (x < 2) return false;\n"
            "        for (int i = 2; (long) i * i <= x; i++) if (x % i == 0) return false;\n"
            "        return true;\n"
            "    }\n"
            "    static void rec(int depth) {\n"
            "        if (depth == n) { cnt++; return; }\n"
            "        for (int v = 1; v <= n; v++) {\n"
            "            if (used[v]) continue;\n"
            "            if (depth > 0 && !isPrime(perm[depth - 1] + v)) continue;\n"
            "            used[v] = true;\n"
            "            perm[depth] = v;\n"
            "            rec(depth + 1);\n"
            "            used[v] = false;\n"
            "        }\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "from itertools import permutations\n"
            "# 소수 이웃 줄세우기 (순열 완전탐색)\n"
            "n = int(sys.stdin.readline())\n"
            "# TODO: 모든 순열을 만들어 인접 합이 모두 소수인 경우의 수를 세기\n"
        ),
    ),

    Problem(
        id="bruteforce-08",
        rank="Gold",
        title="연구소 (바이러스 차단)",
        style="실전",
        topic="완전탐색+BFS",
        type="stdin",
        description=(
            "N x M 연구소 지도에서 0은 빈 칸, 1은 벽, 2는 바이러스다. 빈 칸 중 정확히 3곳에 "
            "벽을 새로 세운 뒤, 바이러스가 상하좌우로 인접한 빈 칸으로 퍼진다. 벽 3개를 가장 잘 "
            "세웠을 때 남는 안전 영역(바이러스가 닿지 않은 빈 칸)의 최대 개수를 구하라."
        ),
        input_desc="첫 줄에 N M (3 ≤ N,M ≤ 8). 다음 N개의 줄에 M개의 정수(0/1/2)가 공백으로 주어진다.",
        output_desc="벽 3개를 세운 뒤 얻을 수 있는 안전 영역의 최대 크기.",
        examples=[
            {"input": "7 7\n2 0 0 0 1 1 0\n0 0 1 0 1 2 0\n0 1 1 0 1 0 0\n0 1 0 0 0 0 0\n0 0 0 0 0 1 1\n0 1 0 0 0 0 0\n0 1 0 0 0 0 0", "output": "27"},
        ],
        hints=[
            "빈 칸 중 3곳을 고르는 모든 조합(완전탐색)에 대해 바이러스를 퍼뜨려 안전 영역을 센다.",
            "조합은 combinations(빈칸, 3). 각 조합마다 그 3칸을 벽으로 막고 BFS로 바이러스를 전파한 뒤 안전 칸을 카운트.",
            "N,M ≤ 8 이라 빈칸 조합 수가 작아 완전탐색이 충분히 빠르다.",
        ],
        testcases=[
            {"input": "7 7\n2 0 0 0 1 1 0\n0 0 1 0 1 2 0\n0 1 1 0 1 0 0\n0 1 0 0 0 0 0\n0 0 0 0 0 1 1\n0 1 0 0 0 0 0\n0 1 0 0 0 0 0", "output": "27"},
            {"input": "4 6\n0 0 0 0 0 0\n1 0 0 0 0 2\n1 1 1 0 0 2\n0 0 0 0 0 2", "output": "9"},
            {"input": "8 8\n2 0 0 0 0 0 0 2\n2 0 0 0 0 0 0 2\n2 0 0 0 0 0 0 2\n2 0 0 0 0 0 0 2\n2 0 0 0 0 0 0 2\n0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0", "output": "3"},
            {"input": "3 3\n0 0 0\n0 2 0\n0 0 0", "output": "2"},
        ],
        reference_py=(
            "import sys\n"
            "from collections import deque\n"
            "from itertools import combinations\n"
            "d = sys.stdin.read().split()\n"
            "idx = 0; n = int(d[idx]); m = int(d[idx+1]); idx += 2\n"
            "g = [[int(d[idx + r*m + c]) for c in range(m)] for r in range(n)]\n"
            "empties = [(r, c) for r in range(n) for c in range(m) if g[r][c] == 0]\n"
            "viruses = [(r, c) for r in range(n) for c in range(m) if g[r][c] == 2]\n"
            "best = 0\n"
            "for walls in combinations(empties, 3):\n"
            "    wset = set(walls)\n"
            "    vis = [[False] * m for _ in range(n)]\n"
            "    q = deque(viruses)\n"
            "    for r, c in viruses: vis[r][c] = True\n"
            "    while q:\n"
            "        r, c = q.popleft()\n"
            "        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):\n"
            "            nr, nc = r + dr, c + dc\n"
            "            if 0 <= nr < n and 0 <= nc < m and not vis[nr][nc] and g[nr][nc] == 0 and (nr, nc) not in wset:\n"
            "                vis[nr][nc] = True; q.append((nr, nc))\n"
            "    safe = sum(1 for r in range(n) for c in range(m) if g[r][c] == 0 and (r, c) not in wset and not vis[r][c])\n"
            "    best = max(best, safe)\n"
            "print(best)\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    static int n, m; static int[][] g;\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        StreamTokenizer st = new StreamTokenizer(br);\n"
            "        st.nextToken(); n = (int) st.nval; st.nextToken(); m = (int) st.nval;\n"
            "        g = new int[n][m];\n"
            "        List<int[]> empties = new ArrayList<>(), viruses = new ArrayList<>();\n"
            "        for (int r = 0; r < n; r++) for (int c = 0; c < m; c++) {\n"
            "            st.nextToken(); g[r][c] = (int) st.nval;\n"
            "            if (g[r][c] == 0) empties.add(new int[]{r, c});\n"
            "            else if (g[r][c] == 2) viruses.add(new int[]{r, c});\n"
            "        }\n"
            "        int E = empties.size(), best = 0;\n"
            "        int[] dr = {1, -1, 0, 0}, dc = {0, 0, 1, -1};\n"
            "        for (int i = 0; i < E; i++) for (int j = i + 1; j < E; j++) for (int k = j + 1; k < E; k++) {\n"
            "            boolean[][] wall = new boolean[n][m];\n"
            "            for (int[] w : new int[][]{empties.get(i), empties.get(j), empties.get(k)}) wall[w[0]][w[1]] = true;\n"
            "            boolean[][] vis = new boolean[n][m];\n"
            "            ArrayDeque<int[]> q = new ArrayDeque<>();\n"
            "            for (int[] v : viruses) { vis[v[0]][v[1]] = true; q.add(v); }\n"
            "            while (!q.isEmpty()) { int[] cur = q.poll();\n"
            "                for (int t = 0; t < 4; t++) { int nr = cur[0] + dr[t], nc = cur[1] + dc[t];\n"
            "                    if (nr >= 0 && nr < n && nc >= 0 && nc < m && !vis[nr][nc] && g[nr][nc] == 0 && !wall[nr][nc]) {\n"
            "                        vis[nr][nc] = true; q.add(new int[]{nr, nc}); } }\n"
            "            }\n"
            "            int safe = 0;\n"
            "            for (int r = 0; r < n; r++) for (int c = 0; c < m; c++)\n"
            "                if (g[r][c] == 0 && !wall[r][c] && !vis[r][c]) safe++;\n"
            "            best = Math.max(best, safe);\n"
            "        }\n"
            "        System.out.println(best);\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp=(
            "#include <bits/stdc++.h>\n"
            "using namespace std;\n"
            "int n, m, g[8][8];\n"
            "int main(){\n"
            "    scanf(\"%d %d\", &n, &m);\n"
            "    vector<pair<int,int>> empties, viruses;\n"
            "    for (int r = 0; r < n; r++) for (int c = 0; c < m; c++) {\n"
            "        scanf(\"%d\", &g[r][c]);\n"
            "        if (g[r][c] == 0) empties.push_back({r, c});\n"
            "        else if (g[r][c] == 2) viruses.push_back({r, c});\n"
            "    }\n"
            "    int E = empties.size(), best = 0;\n"
            "    int dr[] = {1, -1, 0, 0}, dc[] = {0, 0, 1, -1};\n"
            "    for (int i = 0; i < E; i++) for (int j = i + 1; j < E; j++) for (int k = j + 1; k < E; k++) {\n"
            "        bool wall[8][8] = {false}, vis[8][8] = {false};\n"
            "        wall[empties[i].first][empties[i].second] = true;\n"
            "        wall[empties[j].first][empties[j].second] = true;\n"
            "        wall[empties[k].first][empties[k].second] = true;\n"
            "        queue<pair<int,int>> q;\n"
            "        for (auto& v : viruses) { vis[v.first][v.second] = true; q.push(v); }\n"
            "        while (!q.empty()) { auto cur = q.front(); q.pop();\n"
            "            for (int t = 0; t < 4; t++) { int nr = cur.first + dr[t], nc = cur.second + dc[t];\n"
            "                if (nr >= 0 && nr < n && nc >= 0 && nc < m && !vis[nr][nc] && g[nr][nc] == 0 && !wall[nr][nc]) {\n"
            "                    vis[nr][nc] = true; q.push({nr, nc}); } }\n"
            "        }\n"
            "        int safe = 0;\n"
            "        for (int r = 0; r < n; r++) for (int c = 0; c < m; c++)\n"
            "            if (g[r][c] == 0 && !wall[r][c] && !vis[r][c]) safe++;\n"
            "        best = max(best, safe);\n"
            "    }\n"
            "    printf(\"%d\\n\", best);\n"
            "    return 0;\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "from itertools import combinations\n"
            "from collections import deque\n"
            "d = sys.stdin.read().split()\n"
            "# 첫 줄 N M, 다음 격자(0빈칸/1벽/2바이러스). 벽 3개로 최대 안전영역.\n"
        ),
    ),

]
