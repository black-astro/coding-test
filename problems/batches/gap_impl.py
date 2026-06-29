"""유형 보강 배치 — 구현/시뮬레이션·문자열·정수론·자료구조·투포인터·힙.

같은 유형을 난이도별로 여러 랭크(Silver/Gold/Platinum)에 배치한다.
모든 reference_py 는 전체 testcase 를 통과한다.
"""

from engine.models import Problem

PROBLEMS = [

    # =====================================================================
    # 1) 구현/시뮬레이션 — Silver
    # =====================================================================
    Problem(
        id="gi-01",
        rank="Silver",
        tier="S2",
        category="구현/시뮬레이션",
        title="달팽이 배열 만들기",
        style="대기업",
        topic="시뮬레이션",
        type="func",
        func_name="solution",
        description=(
            "정수 n 이 주어지면 1부터 n*n 까지의 수를 시계 방향 나선형(오른쪽→아래→왼쪽→위)으로 "
            "채운 n×n 2차원 리스트를 반환하세요. 가장 바깥쪽 왼쪽 위 칸에서 1부터 시작합니다."
        ),
        input_desc="n : 정수 (1 ≤ n ≤ 100)",
        output_desc="나선형으로 채워진 n×n 2차원 리스트",
        examples=[
            {"args": [3], "output": [[1, 2, 3], [8, 9, 4], [7, 6, 5]]},
            {"args": [1], "output": [[1]]},
        ],
        hints=[
            "현재 방향으로 한 칸씩 채우다가, 벽에 닿거나 이미 채운 칸을 만나면 방향만 시계 방향으로 꺾으면 됩니다.",
            "방향 벡터 4개(오른쪽·아래·왼쪽·위)를 순서대로 두고, 다음 칸이 범위를 벗어나거나 0이 아니면 방향 인덱스를 (d+1)%4 로 바꾸세요.",
            "for v in range(1, n*n+1): 칸에 v 기록 → 다음칸 계산 → 막히면 d=(d+1)%4 후 다시 계산 → 이동.",
        ],
        testcases=[
            {"args": [1], "expected": [[1]]},
            {"args": [2], "expected": [[1, 2], [4, 3]]},
            {"args": [3], "expected": [[1, 2, 3], [8, 9, 4], [7, 6, 5]]},
            {"args": [4], "expected": [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]},
        ],
        reference_py=(
            "def solution(n):\n"
            "    m = [[0] * n for _ in range(n)]\n"
            "    dr = [0, 1, 0, -1]\n"
            "    dc = [1, 0, -1, 0]\n"
            "    r = c = d = 0\n"
            "    for v in range(1, n * n + 1):\n"
            "        m[r][c] = v\n"
            "        nr, nc = r + dr[d], c + dc[d]\n"
            "        if not (0 <= nr < n and 0 <= nc < n and m[nr][nc] == 0):\n"
            "            d = (d + 1) % 4\n"
            "            nr, nc = r + dr[d], c + dc[d]\n"
            "        r, c = nr, nc\n"
            "    return m\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int[][] solution(int n) {\n"
            "        int[][] m = new int[n][n];\n"
            "        int[] dr = {0, 1, 0, -1}, dc = {1, 0, -1, 0};\n"
            "        int r = 0, c = 0, d = 0;\n"
            "        for (int v = 1; v <= n * n; v++) {\n"
            "            m[r][c] = v;\n"
            "            int nr = r + dr[d], nc = c + dc[d];\n"
            "            if (!(nr >= 0 && nr < n && nc >= 0 && nc < n && m[nr][nc] == 0)) {\n"
            "                d = (d + 1) % 4;\n"
            "                nr = r + dr[d]; nc = c + dc[d];\n"
            "            }\n"
            "            r = nr; c = nc;\n"
            "        }\n"
            "        return m;\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp="",
        template_py=(
            "# 달팽이(나선) 배열 : 1..n*n 을 시계방향으로 채운 n x n 리스트 반환\n"
            "def solution(n):\n"
            "    answer = [[0] * n for _ in range(n)]\n"
            "    return answer\n"
        ),
    ),

    # =====================================================================
    # 2) 구현/시뮬레이션 — Gold
    # =====================================================================
    Problem(
        id="gi-02",
        rank="Gold",
        tier="G4",
        category="구현/시뮬레이션",
        title="배열 테두리 돌리기",
        style="백준",
        topic="시뮬레이션",
        type="stdin",
        description=(
            "N×M 격자가 있다. 격자의 각 테두리(가장 바깥쪽 테두리부터 안쪽으로)를 "
            "시계 방향으로 R칸씩 회전시킨 결과를 출력하시오. 한 테두리의 원소들은 "
            "시계 방향 순서대로 이어져 있다고 보고, 그 줄을 통째로 R칸 밀어 돌린다."
        ),
        input_desc=(
            "첫째 줄에 N M R (2 ≤ N, M ≤ 300, 1 ≤ R ≤ 1000), 다음 N개의 줄에 "
            "M개의 정수가 공백으로 주어진다."
        ),
        output_desc="회전이 끝난 격자를 N개의 줄에 걸쳐 출력한다.",
        examples=[
            {
                "input": "4 4 1\n1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16\n",
                "output": "5 1 2 3\n9 10 6 4\n13 11 7 8\n14 15 16 12\n",
            },
            {
                "input": "3 3 1\n1 2 3\n4 5 6\n7 8 9\n",
                "output": "4 1 2\n7 5 3\n8 9 6\n",
            },
        ],
        hints=[
            "각 테두리를 따로 떼어 1차원 배열로 펼친 다음, 그 배열을 회전시키고 다시 제자리에 써 넣는 방식이 깔끔합니다.",
            "테두리 칸의 좌표를 시계 방향(윗변→오른변→아랫변→왼변) 순서로 모으고, 길이 L에 대해 R%L 만큼 민 배열을 만드세요.",
            "rot = vals[L-r:] + vals[:L-r] (r=R%L). 같은 좌표 순서로 rot 값을 다시 격자에 기록하면 됩니다.",
        ],
        testcases=[
            {
                "input": "4 4 1\n1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16\n",
                "output": "5 1 2 3\n9 10 6 4\n13 11 7 8\n14 15 16 12\n",
            },
            {
                "input": "3 3 1\n1 2 3\n4 5 6\n7 8 9\n",
                "output": "4 1 2\n7 5 3\n8 9 6\n",
            },
            {
                "input": "2 4 2\n1 2 3 4\n5 6 7 8\n",
                "output": "6 5 1 2\n7 8 4 3\n",
            },
            {
                "input": "4 4 2\n1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16\n",
                "output": "9 5 1 2\n13 11 10 3\n14 7 6 4\n15 16 12 8\n",
            },
        ],
        reference_py=(
            "import sys\n"
            "data = sys.stdin.read().split('\\n')\n"
            "n, m, R = map(int, data[0].split())\n"
            "a = [list(map(int, data[1 + i].split())) for i in range(n)]\n"
            "for layer in range(min(n, m) // 2):\n"
            "    top, bottom, left, right = layer, n - 1 - layer, layer, m - 1 - layer\n"
            "    pos = []\n"
            "    for c in range(left, right + 1):\n"
            "        pos.append((top, c))\n"
            "    for r in range(top + 1, bottom + 1):\n"
            "        pos.append((r, right))\n"
            "    for c in range(right - 1, left - 1, -1):\n"
            "        pos.append((bottom, c))\n"
            "    for r in range(bottom - 1, top, -1):\n"
            "        pos.append((r, left))\n"
            "    L = len(pos)\n"
            "    vals = [a[r][c] for r, c in pos]\n"
            "    rr = R % L\n"
            "    rot = vals[L - rr:] + vals[:L - rr]\n"
            "    for (r, c), v in zip(pos, rot):\n"
            "        a[r][c] = v\n"
            "print('\\n'.join(' '.join(map(str, row)) for row in a))\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int n = Integer.parseInt(st.nextToken());\n"
            "        int m = Integer.parseInt(st.nextToken());\n"
            "        int R = Integer.parseInt(st.nextToken());\n"
            "        int[][] a = new int[n][m];\n"
            "        for (int i = 0; i < n; i++) {\n"
            "            st = new StringTokenizer(br.readLine());\n"
            "            for (int j = 0; j < m; j++) a[i][j] = Integer.parseInt(st.nextToken());\n"
            "        }\n"
            "        for (int layer = 0; layer < Math.min(n, m) / 2; layer++) {\n"
            "            int top = layer, bottom = n - 1 - layer, left = layer, right = m - 1 - layer;\n"
            "            ArrayList<int[]> pos = new ArrayList<>();\n"
            "            for (int c = left; c <= right; c++) pos.add(new int[]{top, c});\n"
            "            for (int r = top + 1; r <= bottom; r++) pos.add(new int[]{r, right});\n"
            "            for (int c = right - 1; c >= left; c--) pos.add(new int[]{bottom, c});\n"
            "            for (int r = bottom - 1; r > top; r--) pos.add(new int[]{r, left});\n"
            "            int L = pos.size();\n"
            "            int[] vals = new int[L];\n"
            "            for (int i = 0; i < L; i++) vals[i] = a[pos.get(i)[0]][pos.get(i)[1]];\n"
            "            int rr = R % L;\n"
            "            for (int i = 0; i < L; i++) {\n"
            "                int[] p = pos.get(i);\n"
            "                a[p[0]][p[1]] = vals[((i - rr) % L + L) % L];\n"
            "            }\n"
            "        }\n"
            "        StringBuilder sb = new StringBuilder();\n"
            "        for (int i = 0; i < n; i++) {\n"
            "            for (int j = 0; j < m; j++) {\n"
            "                sb.append(a[i][j]);\n"
            "                if (j < m - 1) sb.append(' ');\n"
            "            }\n"
            "            sb.append('\\n');\n"
            "        }\n"
            "        System.out.print(sb);\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp="",
        template_py=(
            "import sys\n"
            "data = sys.stdin.read().split('\\n')\n"
            "# 배열 테두리 돌리기 : 각 테두리를 시계방향 R칸 회전\n"
            "n, m, R = map(int, data[0].split())\n"
            "# ...\n"
        ),
    ),

    # =====================================================================
    # 3) 문자열 처리 — Silver
    # =====================================================================
    Problem(
        id="gi-03",
        rank="Silver",
        tier="S1",
        category="문자열",
        title="문자열 런 길이 압축",
        style="대기업",
        topic="문자열",
        type="func",
        func_name="solution",
        description=(
            "문자열 s 를 런 길이 인코딩(RLE)으로 압축하세요. 같은 문자가 연속으로 나오는 "
            "구간을 '문자 + 연속개수' 로 바꿔 이어 붙입니다. 예) 'aaabbc' → 'a3b2c1'. "
            "개수는 1이어도 항상 표기하며, 빈 문자열은 빈 문자열을 반환합니다."
        ),
        input_desc="s : 소문자로 이루어진 문자열 (0 ≤ len(s) ≤ 1000)",
        output_desc="압축된 문자열",
        examples=[
            {"args": ["aaabbc"], "output": "a3b2c1"},
            {"args": ["abc"], "output": "a1b1c1"},
        ],
        hints=[
            "왼쪽부터 훑으면서 '지금 문자와 같은 문자가 몇 개나 연속되는지' 세면 됩니다.",
            "두 개의 포인터(또는 현재 문자와 카운트 변수)를 두고, 문자가 바뀌는 순간 '문자+개수'를 결과에 추가하세요.",
            "i 를 두고 j 를 s[j]==s[i] 인 동안 전진 → out += s[i] + str(j - i) → i = j 로 반복.",
        ],
        testcases=[
            {"args": [""], "expected": ""},
            {"args": ["aaabbc"], "expected": "a3b2c1"},
            {"args": ["abc"], "expected": "a1b1c1"},
            {"args": ["aaaa"], "expected": "a4"},
            {"args": ["aabbaa"], "expected": "a2b2a2"},
        ],
        reference_py=(
            "def solution(s):\n"
            "    if not s:\n"
            "        return ''\n"
            "    out = []\n"
            "    i = 0\n"
            "    while i < len(s):\n"
            "        j = i\n"
            "        while j < len(s) and s[j] == s[i]:\n"
            "            j += 1\n"
            "        out.append(s[i] + str(j - i))\n"
            "        i = j\n"
            "    return ''.join(out)\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public String solution(String s) {\n"
            "        if (s.isEmpty()) return \"\";\n"
            "        StringBuilder sb = new StringBuilder();\n"
            "        int i = 0, n = s.length();\n"
            "        while (i < n) {\n"
            "            int j = i;\n"
            "            while (j < n && s.charAt(j) == s.charAt(i)) j++;\n"
            "            sb.append(s.charAt(i)).append(j - i);\n"
            "            i = j;\n"
            "        }\n"
            "        return sb.toString();\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp="",
        template_py=(
            "# 런 길이 압축 : 'aaabbc' -> 'a3b2c1'\n"
            "def solution(s):\n"
            "    answer = ''\n"
            "    return answer\n"
        ),
    ),

    # =====================================================================
    # 4) 문자열 처리(KMP) — Gold
    # =====================================================================
    Problem(
        id="gi-04",
        rank="Gold",
        tier="G3",
        category="문자열",
        title="패턴 위치 찾기 (KMP)",
        style="백준",
        topic="문자열(KMP)",
        type="stdin",
        description=(
            "본문 문자열 T 안에서 패턴 문자열 P 가 나타나는 모든 위치를 찾으시오. "
            "겹쳐서 나타나는 경우도 모두 센다. KMP 알고리즘으로 O(|T|+|P|) 에 해결하세요."
        ),
        input_desc=(
            "첫째 줄에 본문 T, 둘째 줄에 패턴 P 가 주어진다. 두 문자열은 공백을 포함할 수 "
            "있으며 길이는 각각 1 이상 100만 이하이다."
        ),
        output_desc=(
            "첫째 줄에 P가 나타난 횟수, 둘째 줄에 나타난 시작 위치(1-based)들을 공백으로 "
            "구분해 오름차순 출력한다. 나타나지 않으면 둘째 줄은 비운다."
        ),
        examples=[
            {"input": "ABABABA\nABA\n", "output": "3\n1 3 5\n"},
            {"input": "AAAAA\nAA\n", "output": "4\n1 2 3 4\n"},
        ],
        hints=[
            "본문을 한 글자씩 보며 패턴과 비교하되, 불일치가 나도 본문 인덱스를 되돌리지 않는 것이 핵심입니다.",
            "패턴의 실패 함수(부분 일치 테이블) f 를 먼저 만들고, 매칭 중 불일치 시 k=f[k-1] 로 패턴 포인터만 점프하세요.",
            "매칭 성공(k==len(P))마다 위치 i-len(P)+2 를 기록하고 k=f[k-1] 로 이어가면 겹치는 경우까지 모두 찾습니다.",
        ],
        testcases=[
            {"input": "ABABABA\nABA\n", "output": "3\n1 3 5\n"},
            {"input": "ABCDABD\nXYZ\n", "output": "0\n\n"},
            {"input": "AAAAA\nAA\n", "output": "4\n1 2 3 4\n"},
            {"input": "hello world\no\n", "output": "2\n5 8\n"},
        ],
        reference_py=(
            "import sys\n"
            "data = sys.stdin.read().split('\\n')\n"
            "text = data[0]\n"
            "pat = data[1]\n"
            "f = [0] * len(pat)\n"
            "k = 0\n"
            "for i in range(1, len(pat)):\n"
            "    while k > 0 and pat[i] != pat[k]:\n"
            "        k = f[k - 1]\n"
            "    if pat[i] == pat[k]:\n"
            "        k += 1\n"
            "    f[i] = k\n"
            "res = []\n"
            "k = 0\n"
            "for i in range(len(text)):\n"
            "    while k > 0 and text[i] != pat[k]:\n"
            "        k = f[k - 1]\n"
            "    if text[i] == pat[k]:\n"
            "        k += 1\n"
            "    if k == len(pat):\n"
            "        res.append(i - len(pat) + 2)\n"
            "        k = f[k - 1]\n"
            "print(len(res))\n"
            "print(' '.join(map(str, res)))\n"
        ),
        reference_java=(
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        String text = br.readLine();\n"
            "        String pat = br.readLine();\n"
            "        int n = text.length(), p = pat.length();\n"
            "        int[] f = new int[p];\n"
            "        int k = 0;\n"
            "        for (int i = 1; i < p; i++) {\n"
            "            while (k > 0 && pat.charAt(i) != pat.charAt(k)) k = f[k - 1];\n"
            "            if (pat.charAt(i) == pat.charAt(k)) k++;\n"
            "            f[i] = k;\n"
            "        }\n"
            "        StringBuilder sb = new StringBuilder();\n"
            "        int cnt = 0;\n"
            "        k = 0;\n"
            "        for (int i = 0; i < n; i++) {\n"
            "            while (k > 0 && text.charAt(i) != pat.charAt(k)) k = f[k - 1];\n"
            "            if (text.charAt(i) == pat.charAt(k)) k++;\n"
            "            if (k == p) {\n"
            "                cnt++;\n"
            "                sb.append(i - p + 2).append(' ');\n"
            "                k = f[k - 1];\n"
            "            }\n"
            "        }\n"
            "        System.out.println(cnt);\n"
            "        System.out.println(sb.toString().trim());\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp="",
        template_py=(
            "import sys\n"
            "data = sys.stdin.read().split('\\n')\n"
            "# KMP 로 패턴 위치 모두 찾기\n"
            "text = data[0]\n"
            "pat = data[1]\n"
            "# ...\n"
        ),
    ),

    # =====================================================================
    # 5) 정수론(모듈러 거듭제곱) — Silver
    # =====================================================================
    Problem(
        id="gi-05",
        rank="Silver",
        tier="S1",
        category="수학/정수론",
        title="빠른 거듭제곱 (모듈러)",
        style="대기업",
        topic="정수론(분할정복 거듭제곱)",
        type="func",
        func_name="solution",
        description=(
            "정수 a, b, m 이 주어질 때 (a^b) mod m 을 구하세요. b 가 매우 클 수 있으므로 "
            "지수를 절반씩 줄이는 분할정복 거듭제곱(이진 거듭제곱)을 사용해야 합니다. "
            "b = 0 이면 a^0 = 1 로 보되, 마지막에 m 으로 나눈 나머지를 반환합니다."
        ),
        input_desc="a, b, m : 정수 (0 ≤ a, 0 ≤ b ≤ 10^18, 1 ≤ m ≤ 10^9)",
        output_desc="(a^b) mod m",
        examples=[
            {"args": [2, 10, 1000], "output": 24},
            {"args": [3, 4, 5], "output": 1},
        ],
        hints=[
            "a^b 를 그대로 곱하면 b 가 클 때 너무 느리고 수가 거대해집니다. 지수를 반씩 줄일 방법을 생각하세요.",
            "b 가 짝수면 a^b = (a^(b/2))^2, 홀수면 a^b = a * a^(b-1). 매 단계 m 으로 나머지를 취하며 진행합니다.",
            "result=1%m; base=a%m; while b>0: if b&1: result=result*base%m; base=base*base%m; b>>=1; return result.",
        ],
        testcases=[
            {"args": [2, 10, 1000], "expected": 24},
            {"args": [3, 4, 5], "expected": 1},
            {"args": [10, 0, 7], "expected": 1},
            {"args": [5, 1000, 1000000007], "expected": 169547125},
            {"args": [7, 13, 1], "expected": 0},
        ],
        reference_py=(
            "def solution(a, b, m):\n"
            "    result = 1 % m\n"
            "    base = a % m\n"
            "    while b > 0:\n"
            "        if b & 1:\n"
            "            result = result * base % m\n"
            "        base = base * base % m\n"
            "        b >>= 1\n"
            "    return result\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public long solution(long a, long b, long m) {\n"
            "        long result = 1 % m;\n"
            "        long base = a % m;\n"
            "        while (b > 0) {\n"
            "            if ((b & 1) == 1) result = result * base % m;\n"
            "            base = base * base % m;\n"
            "            b >>= 1;\n"
            "        }\n"
            "        return result;\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp="",
        template_py=(
            "# (a^b) mod m 을 이진 거듭제곱으로\n"
            "def solution(a, b, m):\n"
            "    answer = 1\n"
            "    return answer\n"
        ),
    ),

    # =====================================================================
    # 6) 정수론(이항계수, 확장유클리드) — Gold
    # =====================================================================
    Problem(
        id="gi-06",
        rank="Gold",
        tier="G3",
        category="수학/정수론",
        title="이항계수 모듈러 (확장 유클리드)",
        style="백준",
        topic="정수론(조합·모듈러 역원)",
        type="func",
        func_name="solution",
        description=(
            "이항계수 C(n, r) 을 소수 p 로 나눈 나머지를 구하세요. 분자와 분모의 곱을 각각 "
            "mod p 로 구한 뒤, 분모의 모듈러 곱셈 역원을 확장 유클리드 호제법으로 구해 "
            "곱합니다. r < 0 이거나 r > n 이면 0 을 반환합니다."
        ),
        input_desc="n, r : 정수 (0 ≤ r, n ≤ 10^6), p : 소수 (2 ≤ p ≤ 10^9+7)",
        output_desc="C(n, r) mod p",
        examples=[
            {"args": [5, 2, 1000000007], "output": 10},
            {"args": [10, 3, 1000000007], "output": 120},
        ],
        hints=[
            "C(n,r) = n! / (r!(n-r)!) 인데 나눗셈을 그대로 mod 에서 할 수 없습니다. 나눗셈 대신 무엇을 곱해야 할까요?",
            "분모 d 에 대해 d * x ≡ 1 (mod p) 인 x(모듈러 역원)를 곱하면 됩니다. 확장 유클리드로 d 의 역원을 구하세요.",
            "분자 = ∏(n-i) mod p, 분모 = ∏(i+1) mod p (i=0..r-1). 답 = 분자 * inv(분모) % p, inv 는 egcd(d,p) 의 x%p.",
        ],
        testcases=[
            {"args": [5, 2, 1000000007], "expected": 10},
            {"args": [10, 0, 1000000007], "expected": 1},
            {"args": [4, 4, 1000000007], "expected": 1},
            {"args": [2, 5, 1000000007], "expected": 0},
            {"args": [1000, 500, 1000000007], "expected": 159835829},
            {"args": [10, 3, 1000000007], "expected": 120},
        ],
        reference_py=(
            "def solution(n, r, p):\n"
            "    if r < 0 or r > n:\n"
            "        return 0\n"
            "    def egcd(a, b):\n"
            "        if b == 0:\n"
            "            return (a, 1, 0)\n"
            "        g, x, y = egcd(b, a % b)\n"
            "        return (g, y, x - (a // b) * y)\n"
            "    def inv(a):\n"
            "        _, x, _ = egcd(a % p, p)\n"
            "        return x % p\n"
            "    num = 1\n"
            "    den = 1\n"
            "    for i in range(r):\n"
            "        num = num * ((n - i) % p) % p\n"
            "        den = den * ((i + 1) % p) % p\n"
            "    return num * inv(den) % p\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    long P;\n"
            "    long[] egcd(long a, long b) {\n"
            "        if (b == 0) return new long[]{a, 1, 0};\n"
            "        long[] r = egcd(b, a % b);\n"
            "        return new long[]{r[0], r[2], r[1] - (a / b) * r[2]};\n"
            "    }\n"
            "    long inv(long a) {\n"
            "        long[] r = egcd(((a % P) + P) % P, P);\n"
            "        return ((r[1] % P) + P) % P;\n"
            "    }\n"
            "    public long solution(long n, long r, long p) {\n"
            "        if (r < 0 || r > n) return 0;\n"
            "        P = p;\n"
            "        long num = 1, den = 1;\n"
            "        for (long i = 0; i < r; i++) {\n"
            "            num = num * ((n - i) % p) % p;\n"
            "            den = den * ((i + 1) % p) % p;\n"
            "        }\n"
            "        return num * inv(den) % p;\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp="",
        template_py=(
            "# C(n, r) mod p (p 는 소수) : 확장 유클리드로 모듈러 역원 사용\n"
            "def solution(n, r, p):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    # =====================================================================
    # 7) 투포인터/슬라이딩 윈도우 — Silver
    # =====================================================================
    Problem(
        id="gi-07",
        rank="Silver",
        tier="S2",
        category="투포인터/누적합",
        title="합이 M인 연속 부분합 개수",
        style="백준",
        topic="투포인터",
        type="stdin",
        description=(
            "N개의 양의 정수로 이루어진 수열에서, 연속된 부분 수열의 합이 정확히 M 이 되는 "
            "경우의 수를 구하시오. 모든 수가 양수이므로 두 포인터로 구간을 좁혔다 넓히며 "
            "한 번의 순회로 셀 수 있습니다."
        ),
        input_desc=(
            "첫째 줄에 N M (1 ≤ N ≤ 100000, 1 ≤ M ≤ 10^9), 둘째 줄에 N개의 양의 정수 "
            "(각 1 이상 10000 이하)가 공백으로 주어진다."
        ),
        output_desc="합이 M 인 연속 부분 수열의 개수.",
        examples=[
            {"input": "4 2\n1 1 1 1\n", "output": "3\n"},
            {"input": "10 5\n1 2 3 4 2 5 3 1 1 2\n", "output": "3\n"},
        ],
        hints=[
            "모든 시작·끝 쌍을 검사하면 O(N^2)입니다. 수가 모두 양수라는 점을 이용하면 포인터를 되돌릴 필요가 없습니다.",
            "왼쪽 포인터 lo, 오른쪽 포인터 hi 와 현재 구간합 s 를 유지하세요. s 가 M보다 크면 lo 를 늘려 줄입니다.",
            "hi 를 늘리며 s += arr[hi]; while s > M: s -= arr[lo]; lo += 1; if s == M: 개수 += 1.",
        ],
        testcases=[
            {"input": "4 2\n1 1 1 1\n", "output": "3\n"},
            {"input": "10 5\n1 2 3 4 2 5 3 1 1 2\n", "output": "3\n"},
            {"input": "1 5\n5\n", "output": "1\n"},
            {"input": "3 100\n1 2 3\n", "output": "0\n"},
        ],
        reference_py=(
            "import sys\n"
            "data = sys.stdin.read().split()\n"
            "n = int(data[0])\n"
            "M = int(data[1])\n"
            "arr = list(map(int, data[2:2 + n]))\n"
            "lo = 0\n"
            "s = 0\n"
            "cnt = 0\n"
            "for hi in range(n):\n"
            "    s += arr[hi]\n"
            "    while s > M and lo <= hi:\n"
            "        s -= arr[lo]\n"
            "        lo += 1\n"
            "    if s == M:\n"
            "        cnt += 1\n"
            "print(cnt)\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int n = Integer.parseInt(st.nextToken());\n"
            "        long M = Long.parseLong(st.nextToken());\n"
            "        int[] arr = new int[n];\n"
            "        st = new StringTokenizer(br.readLine());\n"
            "        for (int i = 0; i < n; i++) arr[i] = Integer.parseInt(st.nextToken());\n"
            "        int lo = 0, cnt = 0;\n"
            "        long s = 0;\n"
            "        for (int hi = 0; hi < n; hi++) {\n"
            "            s += arr[hi];\n"
            "            while (s > M && lo <= hi) s -= arr[lo++];\n"
            "            if (s == M) cnt++;\n"
            "        }\n"
            "        System.out.println(cnt);\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp="",
        template_py=(
            "import sys\n"
            "data = sys.stdin.read().split()\n"
            "# 연속 부분합이 M 인 경우의 수 (투 포인터)\n"
            "n = int(data[0]); M = int(data[1])\n"
            "# ...\n"
        ),
    ),

    # =====================================================================
    # 8) 슬라이딩 윈도우 — Gold
    # =====================================================================
    Problem(
        id="gi-08",
        rank="Gold",
        tier="G4",
        category="투포인터/누적합",
        title="합이 S 이상인 최소 길이 부분 배열",
        style="대기업",
        topic="슬라이딩 윈도우",
        type="func",
        func_name="solution",
        description=(
            "양의 정수 배열 nums 와 정수 s 가 주어진다. 합이 s 이상이 되는 연속 부분 배열 중 "
            "가장 짧은 것의 길이를 반환하세요. 그런 부분 배열이 없으면 0 을 반환합니다. "
            "슬라이딩 윈도우로 O(n) 에 해결하세요."
        ),
        input_desc="s : 정수, nums : 양의 정수 리스트 (1 ≤ len(nums) ≤ 100000)",
        output_desc="조건을 만족하는 최소 길이(없으면 0)",
        examples=[
            {"args": [15, [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]], "output": 2},
            {"args": [7, [2, 3, 1, 2, 4, 3]], "output": 2},
        ],
        hints=[
            "고정된 시작점마다 끝점을 늘려 합을 다시 구하면 느립니다. 창(window)을 늘렸다 줄였다 하며 합을 갱신하세요.",
            "오른쪽 끝 hi 를 늘려 합을 키우고, 합 ≥ s 가 되면 왼쪽 lo 를 줄이며 최소 길이를 갱신합니다.",
            "for hi: s_sum += nums[hi]; while s_sum >= s: best = min(best, hi - lo + 1); s_sum -= nums[lo]; lo += 1.",
        ],
        testcases=[
            {"args": [15, [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]], "expected": 2},
            {"args": [100, [1, 2, 3]], "expected": 0},
            {"args": [7, [2, 3, 1, 2, 4, 3]], "expected": 2},
            {"args": [4, [1, 4, 4]], "expected": 1},
            {"args": [11, [1, 2, 3, 4, 5]], "expected": 3},
        ],
        reference_py=(
            "def solution(s, nums):\n"
            "    lo = 0\n"
            "    total = 0\n"
            "    best = float('inf')\n"
            "    for hi in range(len(nums)):\n"
            "        total += nums[hi]\n"
            "        while total >= s:\n"
            "            best = min(best, hi - lo + 1)\n"
            "            total -= nums[lo]\n"
            "            lo += 1\n"
            "    return 0 if best == float('inf') else best\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int s, int[] nums) {\n"
            "        int lo = 0, total = 0, best = Integer.MAX_VALUE;\n"
            "        for (int hi = 0; hi < nums.length; hi++) {\n"
            "            total += nums[hi];\n"
            "            while (total >= s) {\n"
            "                best = Math.min(best, hi - lo + 1);\n"
            "                total -= nums[lo++];\n"
            "            }\n"
            "        }\n"
            "        return best == Integer.MAX_VALUE ? 0 : best;\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp="",
        template_py=(
            "# 합 >= s 인 연속 부분배열의 최소 길이 (없으면 0)\n"
            "def solution(s, nums):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    # =====================================================================
    # 9) 자료구조(스택 응용 — 오큰수) — Gold
    # =====================================================================
    Problem(
        id="gi-09",
        rank="Gold",
        tier="G4",
        category="자료구조(스택·큐·덱)",
        title="오큰수 (다음 큰 수)",
        style="백준",
        topic="스택(단조 스택)",
        type="stdin",
        description=(
            "수열 A 의 각 원소 A[i] 에 대해 오큰수 NGE(i) 를 구하시오. 오큰수란 A[i] 의 "
            "오른쪽에 있으면서 A[i] 보다 큰 수 중 가장 왼쪽(가장 가까운) 수이다. 그런 수가 "
            "없으면 -1 이다. 스택을 이용해 O(N) 에 해결하세요."
        ),
        input_desc="첫째 줄에 N (1 ≤ N ≤ 1000000), 둘째 줄에 N개의 정수가 공백으로 주어진다.",
        output_desc="각 원소의 오큰수를 공백으로 구분해 한 줄에 출력한다.",
        examples=[
            {"input": "4\n3 5 2 7\n", "output": "5 7 7 -1\n"},
            {"input": "4\n9 5 4 8\n", "output": "-1 8 8 -1\n"},
        ],
        hints=[
            "각 원소마다 오른쪽을 다 훑으면 O(N^2)입니다. 아직 답을 못 찾은 원소들의 인덱스를 모아두는 자료구조가 필요합니다.",
            "스택에 '아직 오큰수를 찾지 못한 인덱스'를 쌓아 두세요. 새 값이 스택 top 의 값보다 크면 그 인덱스의 답이 정해집니다.",
            "for i: while 스택 비지 않고 A[top] < A[i]: ans[스택.pop()] = A[i]; 스택.push(i). 끝까지 남은 인덱스는 -1.",
        ],
        testcases=[
            {"input": "4\n3 5 2 7\n", "output": "5 7 7 -1\n"},
            {"input": "4\n9 5 4 8\n", "output": "-1 8 8 -1\n"},
            {"input": "1\n5\n", "output": "-1\n"},
            {"input": "5\n1 2 3 4 5\n", "output": "2 3 4 5 -1\n"},
        ],
        reference_py=(
            "import sys\n"
            "data = sys.stdin.read().split()\n"
            "n = int(data[0])\n"
            "arr = list(map(int, data[1:1 + n]))\n"
            "ans = [-1] * n\n"
            "st = []\n"
            "for i in range(n):\n"
            "    while st and arr[st[-1]] < arr[i]:\n"
            "        ans[st.pop()] = arr[i]\n"
            "    st.append(i)\n"
            "print(' '.join(map(str, ans)))\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        int n = Integer.parseInt(br.readLine().trim());\n"
            "        int[] arr = new int[n];\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        for (int i = 0; i < n; i++) arr[i] = Integer.parseInt(st.nextToken());\n"
            "        int[] ans = new int[n];\n"
            "        Arrays.fill(ans, -1);\n"
            "        int[] stack = new int[n];\n"
            "        int top = 0;\n"
            "        for (int i = 0; i < n; i++) {\n"
            "            while (top > 0 && arr[stack[top - 1]] < arr[i]) ans[stack[--top]] = arr[i];\n"
            "            stack[top++] = i;\n"
            "        }\n"
            "        StringBuilder sb = new StringBuilder();\n"
            "        for (int i = 0; i < n; i++) {\n"
            "            sb.append(ans[i]);\n"
            "            if (i < n - 1) sb.append(' ');\n"
            "        }\n"
            "        System.out.println(sb);\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp="",
        template_py=(
            "import sys\n"
            "data = sys.stdin.read().split()\n"
            "# 오큰수 : 각 원소의 오른쪽에서 가장 가까운 더 큰 수 (없으면 -1)\n"
            "n = int(data[0])\n"
            "# ...\n"
        ),
    ),

    # =====================================================================
    # 10) 힙/우선순위큐 — Silver
    # =====================================================================
    Problem(
        id="gi-10",
        rank="Silver",
        tier="S1",
        category="힙/우선순위큐",
        title="절댓값 힙 연산 처리",
        style="백준",
        topic="우선순위큐",
        type="func",
        func_name="solution",
        description=(
            "정수들이 담긴 연산 목록 ops 를 차례로 처리한다. 값 x 가 0이 아니면 힙에 x 를 "
            "넣고, x 가 0이면 절댓값이 가장 작은 값을 꺼내 결과에 추가한다(절댓값이 같으면 "
            "실제 값이 더 작은 것을 먼저 꺼낸다). 힙이 비어 있는데 0이 들어오면 0을 추가한다. "
            "꺼낸 값들의 리스트를 반환하세요."
        ),
        input_desc="ops : 정수 리스트 (각 원소의 절댓값 ≤ 10^9, 길이 ≤ 100000)",
        output_desc="0 연산마다 꺼낸 값을 모은 리스트",
        examples=[
            {"args": [[1, -1, 0, 0, 0]], "output": [-1, 1, 0]},
            {"args": [[1, 2, 3, 0, 0, 0, 0]], "output": [1, 2, 3, 0]},
        ],
        hints=[
            "꺼낼 때마다 '절댓값이 가장 작은' 원소가 필요합니다. 매번 전체를 훑지 않으려면 어떤 자료구조가 좋을까요?",
            "우선순위 큐(최소 힙)를 쓰되, 정렬 기준을 (절댓값, 실제값) 튜플로 두면 동점 처리까지 한 번에 됩니다.",
            "넣을 때 heappush(h, (abs(x), x)); 꺼낼 때 비어 있으면 0, 아니면 heappop(h)[1] 을 결과에 추가.",
        ],
        testcases=[
            {"args": [[1, -1, 0, 0, 0]], "expected": [-1, 1, 0]},
            {"args": [[1, 2, 3, 0, 0, 0, 0]], "expected": [1, 2, 3, 0]},
            {"args": [[0]], "expected": [0]},
            {"args": [[-2, 2, 0, 0]], "expected": [-2, 2]},
        ],
        reference_py=(
            "import heapq\n"
            "def solution(ops):\n"
            "    h = []\n"
            "    res = []\n"
            "    for x in ops:\n"
            "        if x != 0:\n"
            "            heapq.heappush(h, (abs(x), x))\n"
            "        else:\n"
            "            res.append(heapq.heappop(h)[1] if h else 0)\n"
            "    return res\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int[] solution(int[] ops) {\n"
            "        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) ->\n"
            "            a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);\n"
            "        ArrayList<Integer> res = new ArrayList<>();\n"
            "        for (int x : ops) {\n"
            "            if (x != 0) pq.offer(new int[]{Math.abs(x), x});\n"
            "            else res.add(pq.isEmpty() ? 0 : pq.poll()[1]);\n"
            "        }\n"
            "        int[] out = new int[res.size()];\n"
            "        for (int i = 0; i < out.length; i++) out[i] = res.get(i);\n"
            "        return out;\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp="",
        template_py=(
            "import heapq\n"
            "# 절댓값 힙 : 0 이면 절댓값 최소 원소를 꺼내 반환\n"
            "def solution(ops):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

    # =====================================================================
    # 11) 힙/우선순위큐 — Gold
    # =====================================================================
    Problem(
        id="gi-11",
        rank="Gold",
        tier="G4",
        category="힙/우선순위큐",
        title="카드 합치기 최소 점수",
        style="백준",
        topic="우선순위큐(그리디)",
        type="stdin",
        description=(
            "N개의 카드 묶음이 있고 각각 적힌 수가 있다. 한 번의 합치기는 두 묶음을 골라 "
            "각각을 두 수의 합으로 바꾼다(즉 합이 두 묶음 모두에 기록된다). 이 합치기를 "
            "정확히 M번 했을 때, 모든 카드에 적힌 수의 총합을 최소로 만들어 출력하시오. "
            "매번 가장 작은 두 묶음을 합치는 것이 최적입니다."
        ),
        input_desc=(
            "첫째 줄에 N M (2 ≤ N ≤ 1000, 0 ≤ M ≤ 15·N), 둘째 줄에 N개의 카드 수 "
            "(각 1 이상 10^6 이하)가 공백으로 주어진다."
        ),
        output_desc="M번 합친 후 모든 카드에 적힌 수의 최소 총합.",
        examples=[
            {"input": "4 2\n1 2 3 4\n", "output": "19\n"},
            {"input": "2 1\n3 4\n", "output": "14\n"},
        ],
        hints=[
            "총합을 작게 하려면 큰 수가 여러 번 더해지지 않게 해야 합니다. 어떤 두 묶음을 합치는 게 유리할까요?",
            "항상 현재 가장 작은 두 묶음을 합치는 그리디가 최적입니다. 최소값 두 개를 빠르게 꺼내려면 최소 힙을 쓰세요.",
            "최소 힙에서 a, b 를 꺼내 a+b 를 두 번 다시 넣기를 M번 반복하고, 마지막에 힙 전체의 합을 출력합니다.",
        ],
        testcases=[
            {"input": "4 2\n1 2 3 4\n", "output": "19\n"},
            {"input": "2 1\n3 4\n", "output": "14\n"},
            {"input": "5 3\n1 1 1 1 1\n", "output": "12\n"},
            {"input": "3 1\n10 20 30\n", "output": "90\n"},
        ],
        reference_py=(
            "import sys\n"
            "import heapq\n"
            "data = sys.stdin.read().split()\n"
            "n = int(data[0])\n"
            "M = int(data[1])\n"
            "arr = list(map(int, data[2:2 + n]))\n"
            "heapq.heapify(arr)\n"
            "for _ in range(M):\n"
            "    a = heapq.heappop(arr)\n"
            "    b = heapq.heappop(arr)\n"
            "    heapq.heappush(arr, a + b)\n"
            "    heapq.heappush(arr, a + b)\n"
            "print(sum(arr))\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int n = Integer.parseInt(st.nextToken());\n"
            "        int M = Integer.parseInt(st.nextToken());\n"
            "        PriorityQueue<Long> pq = new PriorityQueue<>();\n"
            "        st = new StringTokenizer(br.readLine());\n"
            "        for (int i = 0; i < n; i++) pq.offer(Long.parseLong(st.nextToken()));\n"
            "        for (int k = 0; k < M; k++) {\n"
            "            long a = pq.poll(), b = pq.poll();\n"
            "            pq.offer(a + b);\n"
            "            pq.offer(a + b);\n"
            "        }\n"
            "        long sum = 0;\n"
            "        while (!pq.isEmpty()) sum += pq.poll();\n"
            "        System.out.println(sum);\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp="",
        template_py=(
            "import sys, heapq\n"
            "data = sys.stdin.read().split()\n"
            "# 매번 가장 작은 두 묶음을 합쳐 M번, 총합 최소\n"
            "n = int(data[0]); M = int(data[1])\n"
            "# ...\n"
        ),
    ),

    # =====================================================================
    # 12) 자료구조(스택 응용 — 히스토그램) — Platinum
    # =====================================================================
    Problem(
        id="gi-12",
        rank="Platinum",
        tier="P5",
        category="자료구조(스택·큐·덱)",
        title="히스토그램 최대 직사각형",
        style="백준",
        topic="스택(단조 스택)",
        type="func",
        func_name="solution",
        description=(
            "너비가 1인 막대들이 나란히 있어 히스토그램을 이룬다. heights[i] 는 i번째 막대의 "
            "높이이다. 이 히스토그램 안에 들어갈 수 있는 가장 큰 직사각형의 넓이를 구하세요. "
            "단조 스택으로 O(n) 에 해결할 수 있습니다."
        ),
        input_desc="heights : 0 이상의 정수 리스트 (1 ≤ len ≤ 100000)",
        output_desc="포함 가능한 가장 큰 직사각형의 넓이",
        examples=[
            {"args": [[2, 1, 5, 6, 2, 3]], "output": 10},
            {"args": [[2, 4]], "output": 4},
        ],
        hints=[
            "각 막대를 '높이로 삼는' 직사각형의 최대 폭을 알면 됩니다. 막대를 왼쪽부터 보며 어디까지 넓힐 수 있는지 추적하세요.",
            "단조 증가 스택에 (시작인덱스, 높이)를 쌓다가, 더 낮은 막대를 만나면 스택에서 더 높은 것들을 빼며 넓이를 계산합니다.",
            "끝에 0 높이를 추가해 스택을 모두 비웁니다. pop 할 때 넓이 = 높이 * (현재인덱스 - 시작인덱스) 로 최댓값 갱신.",
        ],
        testcases=[
            {"args": [[2, 1, 5, 6, 2, 3]], "expected": 10},
            {"args": [[2, 4]], "expected": 4},
            {"args": [[5]], "expected": 5},
            {"args": [[1, 1, 1, 1]], "expected": 4},
            {"args": [[4, 2, 0, 3, 2, 5]], "expected": 6},
        ],
        reference_py=(
            "def solution(heights):\n"
            "    st = []\n"
            "    best = 0\n"
            "    arr = heights + [0]\n"
            "    for i, x in enumerate(arr):\n"
            "        start = i\n"
            "        while st and st[-1][1] > x:\n"
            "            idx, height = st.pop()\n"
            "            best = max(best, height * (i - idx))\n"
            "            start = idx\n"
            "        st.append((start, x))\n"
            "    return best\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public long solution(int[] heights) {\n"
            "        int n = heights.length;\n"
            "        long best = 0;\n"
            "        Deque<int[]> st = new ArrayDeque<>();\n"
            "        for (int i = 0; i <= n; i++) {\n"
            "            int x = (i == n) ? 0 : heights[i];\n"
            "            int start = i;\n"
            "            while (!st.isEmpty() && st.peek()[1] > x) {\n"
            "                int[] t = st.pop();\n"
            "                best = Math.max(best, (long) t[1] * (i - t[0]));\n"
            "                start = t[0];\n"
            "            }\n"
            "            st.push(new int[]{start, x});\n"
            "        }\n"
            "        return best;\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp="",
        template_py=(
            "# 히스토그램에서 가장 큰 직사각형 넓이 (단조 스택)\n"
            "def solution(heights):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

]
