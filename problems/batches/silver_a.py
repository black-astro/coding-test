"""실버 추가 배치 A — 정렬 응용 / 매개변수 탐색(이분) / 좌표 압축.

silver-06 ~ silver-20 (15문제).
base(silver.py)의 기본 정렬·괄호·존재여부 이분탐색·거스름돈·누적합과 중복되지 않도록
다중 키 정렬, 좌표 정렬, 커스텀 정렬, 매개변수 탐색(나무/랜선/예산),
lower_bound·개수 세기, 좌표 압축·순위 매기기 를 다룬다.
"""

from engine.models import Problem

RANK = "Silver"

PROBLEMS = [

    Problem(
        id="silver-06",
        rank="Silver",
        title="회원 나이 정렬",
        style="백준",
        topic="안정 정렬",
        type="stdin",
        description=(
            "온라인 회원의 나이와 이름이 주어진다. 회원을 나이가 적은 순으로 정렬하되, "
            "나이가 같으면 먼저 가입한 사람(입력에서 먼저 들어온 사람)이 앞에 오도록 출력하시오."
        ),
        input_desc=(
            "첫째 줄에 회원 수 N(1 ≤ N ≤ 100000). 다음 N개의 줄에 각 회원의 나이(정수)와 "
            "이름(공백 없는 영문 문자열)이 공백으로 구분되어 주어진다."
        ),
        output_desc="정렬된 순서대로 한 줄에 한 명씩 '나이 이름' 형식으로 출력한다.",
        examples=[
            {"input": "3\n21 Junkyu\n21 Dohyun\n20 Sunyoung\n",
             "output": "20 Sunyoung\n21 Junkyu\n21 Dohyun\n"},
            {"input": "2\n30 A\n30 B\n", "output": "30 A\n30 B\n"},
        ],
        hints=[
            "나이만 기준으로 정렬하면 되는데, 나이가 같을 때 '입력 순서'를 어떻게 보존할지 생각해 보세요.",
            "파이썬의 sort/sorted 는 안정 정렬(stable)입니다. 나이 하나만 key 로 주면 같은 나이끼리는 원래 순서가 유지됩니다.",
            "members.append((int(age), name)); members.sort(key=lambda x: x[0]) 한 뒤 한 줄씩 출력하면 됩니다.",
        ],
        testcases=[
            {"input": "3\n21 Junkyu\n21 Dohyun\n20 Sunyoung\n",
             "output": "20 Sunyoung\n21 Junkyu\n21 Dohyun\n"},
            {"input": "2\n30 A\n30 B\n", "output": "30 A\n30 B\n"},
            {"input": "1\n5 Kim\n", "output": "5 Kim\n"},
            {"input": "4\n40 a\n10 b\n40 c\n10 d\n", "output": "10 b\n10 d\n40 a\n40 c\n"},
        ],
        reference_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "n = int(input())\n"
            "members = []\n"
            "for _ in range(n):\n"
            "    age, name = input().split()\n"
            "    members.append((int(age), name))\n"
            "members.sort(key=lambda x: x[0])\n"
            "print('\\n'.join(f'{age} {name}' for age, name in members))\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        int n = Integer.parseInt(br.readLine().trim());\n"
            "        String[][] m = new String[n][2];\n"
            "        for (int i = 0; i < n; i++) {\n"
            "            StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "            m[i][0] = st.nextToken();\n"
            "            m[i][1] = st.nextToken();\n"
            "        }\n"
            "        Arrays.sort(m, (a, b) -> Integer.parseInt(a[0]) - Integer.parseInt(b[0]));\n"
            "        StringBuilder sb = new StringBuilder();\n"
            "        for (String[] p : m) sb.append(p[0]).append(' ').append(p[1]).append('\\n');\n"
            "        System.out.print(sb);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "# 나이 오름차순, 같으면 가입(입력) 순서 유지\n"
            "n = int(input())\n"
            "# members = ...\n"
        ),
    ),

    Problem(
        id="silver-07",
        rank="Silver",
        title="좌표 정렬하기",
        style="백준",
        topic="다중 키 정렬",
        type="stdin",
        description=(
            "2차원 평면 위의 점 N개가 주어진다. x좌표가 작은 것부터, x좌표가 같으면 "
            "y좌표가 작은 것부터 순서대로 정렬하여 출력하시오."
        ),
        input_desc=(
            "첫째 줄에 점의 개수 N(1 ≤ N ≤ 100000). 다음 N개의 줄에 점의 x, y좌표가 "
            "공백으로 구분되어 주어진다. (-100000 ≤ x, y ≤ 100000)"
        ),
        output_desc="정렬된 순서대로 한 줄에 한 점씩 'x y' 형식으로 출력한다.",
        examples=[
            {"input": "3\n3 4\n1 1\n1 -1\n", "output": "1 -1\n1 1\n3 4\n"},
            {"input": "2\n-1 5\n-1 -5\n", "output": "-1 -5\n-1 5\n"},
        ],
        hints=[
            "정렬 기준이 두 개입니다. 먼저 x, 그다음 y 를 비교하도록 만들어야 합니다.",
            "튜플 (x, y) 를 그대로 비교하면 파이썬은 x 를 먼저, 같으면 y 를 비교합니다. key 로 (x, y) 를 주면 됩니다.",
            "pts = [tuple(map(int, input().split())) for _ in range(n)]; pts.sort() 만 하면 (x, y) 사전식 정렬이 됩니다.",
        ],
        testcases=[
            {"input": "3\n3 4\n1 1\n1 -1\n", "output": "1 -1\n1 1\n3 4\n"},
            {"input": "1\n0 0\n", "output": "0 0\n"},
            {"input": "2\n-1 5\n-1 -5\n", "output": "-1 -5\n-1 5\n"},
            {"input": "4\n2 2\n2 1\n1 9\n1 0\n", "output": "1 0\n1 9\n2 1\n2 2\n"},
        ],
        reference_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "n = int(input())\n"
            "pts = [tuple(map(int, input().split())) for _ in range(n)]\n"
            "pts.sort()\n"
            "print('\\n'.join(f'{x} {y}' for x, y in pts))\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        int n = Integer.parseInt(br.readLine().trim());\n"
            "        int[][] p = new int[n][2];\n"
            "        for (int i = 0; i < n; i++) {\n"
            "            StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "            p[i][0] = Integer.parseInt(st.nextToken());\n"
            "            p[i][1] = Integer.parseInt(st.nextToken());\n"
            "        }\n"
            "        Arrays.sort(p, (a, b) -> a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);\n"
            "        StringBuilder sb = new StringBuilder();\n"
            "        for (int[] q : p) sb.append(q[0]).append(' ').append(q[1]).append('\\n');\n"
            "        System.out.print(sb);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "# x 오름차순, 같으면 y 오름차순\n"
            "n = int(input())\n"
            "# pts = ...\n"
        ),
    ),

    Problem(
        id="silver-08",
        rank="Silver",
        title="단어 정렬",
        style="백준",
        topic="커스텀 정렬",
        type="stdin",
        description=(
            "알파벳 소문자로 이루어진 N개의 단어가 주어진다. 다음 조건에 따라 정렬해 출력하시오. "
            "(1) 길이가 짧은 것부터, (2) 길이가 같으면 사전 순으로. 단, 중복된 단어는 한 번만 출력한다."
        ),
        input_desc="첫째 줄에 단어 수 N(1 ≤ N ≤ 20000). 다음 N개의 줄에 단어가 하나씩 주어진다.",
        output_desc="조건에 맞게 정렬한 단어를 중복 없이 한 줄에 하나씩 출력한다.",
        examples=[
            {"input": "4\napple\npen\napple\nbanana\n", "output": "pen\napple\nbanana\n"},
            {"input": "3\nbb\naa\nb\n", "output": "b\naa\nbb\n"},
        ],
        hints=[
            "먼저 중복을 어떻게 제거할지, 그다음 두 가지 기준(길이, 사전순)을 어떻게 동시에 적용할지 나눠서 생각하세요.",
            "set 으로 중복을 없앤 뒤, key=(len(단어), 단어) 로 정렬하면 길이 우선, 같으면 사전순이 됩니다.",
            "words = sorted(set(arr), key=lambda w: (len(w), w)) 한 줄로 끝납니다.",
        ],
        testcases=[
            {"input": "4\napple\npen\napple\nbanana\n", "output": "pen\napple\nbanana\n"},
            {"input": "3\nbb\naa\nb\n", "output": "b\naa\nbb\n"},
            {"input": "1\nz\n", "output": "z\n"},
            {"input": "5\nkim\nkim\nan\nbo\nan\n", "output": "an\nbo\nkim\n"},
        ],
        reference_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "n = int(input())\n"
            "arr = [input().strip() for _ in range(n)]\n"
            "words = sorted(set(arr), key=lambda w: (len(w), w))\n"
            "print('\\n'.join(words))\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        int n = Integer.parseInt(br.readLine().trim());\n"
            "        TreeSet<String> set = new TreeSet<>((a, b) ->\n"
            "            a.length() != b.length() ? a.length() - b.length() : a.compareTo(b));\n"
            "        for (int i = 0; i < n; i++) set.add(br.readLine().trim());\n"
            "        StringBuilder sb = new StringBuilder();\n"
            "        for (String w : set) sb.append(w).append('\\n');\n"
            "        System.out.print(sb);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "# 중복 제거 후 (길이, 사전순) 정렬\n"
            "n = int(input())\n"
            "# arr = ...\n"
        ),
    ),

    Problem(
        id="silver-09",
        rank="Silver",
        title="나무 자르기",
        style="백준",
        topic="매개변수 탐색",
        type="stdin",
        description=(
            "절단기에 높이 H를 설정하면, H보다 높은 나무는 H 위 부분이 잘리고 낮은 나무는 잘리지 않는다. "
            "상근이가 적어도 M미터의 나무를 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하시오."
        ),
        input_desc=(
            "첫째 줄에 나무의 수 N과 필요한 나무 길이 M(1 ≤ N ≤ 1000000, 1 ≤ M ≤ 2000000000). "
            "둘째 줄에 나무 N그루의 높이가 공백으로 구분되어 주어진다."
        ),
        output_desc="적어도 M미터를 가져가기 위해 설정할 수 있는 절단기 높이의 최댓값을 출력한다.",
        examples=[
            {"input": "4 7\n20 15 10 17\n", "output": "15\n"},
            {"input": "5 20\n4 42 40 26 46\n", "output": "36\n"},
        ],
        hints=[
            "높이 H를 정하면 잘리는 나무의 총량이 정해집니다. H가 클수록 가져가는 양은 줄어드는 단조적 관계입니다.",
            "0부터 가장 높은 나무 높이까지의 H 후보를 이분 탐색(매개변수 탐색)하세요. 조건은 '총합 ≥ M' 입니다.",
            "while lo<=hi: mid=(lo+hi)//2; got=sum(t-mid for t in trees if t>mid); got>=M 이면 ans=mid, lo=mid+1 아니면 hi=mid-1.",
        ],
        testcases=[
            {"input": "4 7\n20 15 10 17\n", "output": "15\n"},
            {"input": "5 20\n4 42 40 26 46\n", "output": "36\n"},
            {"input": "1 5\n10\n", "output": "5\n"},
            {"input": "2 0\n3 3\n", "output": "3\n"},
        ],
        reference_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "n, m = map(int, input().split())\n"
            "trees = list(map(int, input().split()))\n"
            "lo, hi, ans = 0, max(trees), 0\n"
            "while lo <= hi:\n"
            "    mid = (lo + hi) // 2\n"
            "    got = sum(t - mid for t in trees if t > mid)\n"
            "    if got >= m:\n"
            "        ans = mid\n"
            "        lo = mid + 1\n"
            "    else:\n"
            "        hi = mid - 1\n"
            "print(ans)\n"
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
            "        int[] t = new int[n];\n"
            "        st = new StringTokenizer(br.readLine());\n"
            "        long hi = 0;\n"
            "        for (int i = 0; i < n; i++) { t[i] = Integer.parseInt(st.nextToken()); hi = Math.max(hi, t[i]); }\n"
            "        long lo = 0, ans = 0;\n"
            "        while (lo <= hi) {\n"
            "            long mid = (lo + hi) / 2, got = 0;\n"
            "            for (int x : t) if (x > mid) got += x - mid;\n"
            "            if (got >= m) { ans = mid; lo = mid + 1; } else hi = mid - 1;\n"
            "        }\n"
            "        System.out.println(ans);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "# 절단기 높이 H의 최댓값 (총합 >= M)\n"
            "n, m = map(int, input().split())\n"
            "# trees = ...\n"
        ),
    ),

    Problem(
        id="silver-10",
        rank="Silver",
        title="랜선 자르기",
        style="백준",
        topic="매개변수 탐색",
        type="stdin",
        description=(
            "K개의 랜선을 잘라 같은 길이의 랜선 N개 이상을 만들려고 한다. 자른 랜선의 길이는 "
            "양의 정수여야 한다. N개를 만들 수 있는 랜선의 최대 길이를 구하시오. (만들 수 없으면 0)"
        ),
        input_desc=(
            "첫째 줄에 가진 랜선 수 K와 필요한 랜선 수 N(1 ≤ K ≤ 10000, 1 ≤ N ≤ 1000000). "
            "다음 K개의 줄에 각 랜선의 길이가 하나씩 주어진다."
        ),
        output_desc="N개 이상을 만들 수 있는 랜선의 최대 길이를 출력한다.",
        examples=[
            {"input": "4 11\n802\n743\n457\n539\n", "output": "200\n"},
            {"input": "2 3\n10\n10\n", "output": "5\n"},
        ],
        hints=[
            "랜선 길이 L을 정하면 만들 수 있는 개수는 sum(len // L) 로 정해집니다. L이 커질수록 개수는 줄어듭니다.",
            "1부터 가장 긴 랜선까지 L을 이분 탐색(매개변수 탐색)하면서 '개수 ≥ N' 을 만족하는 최대 L을 찾으세요.",
            "while lo<=hi: mid=(lo+hi)//2; cnt=sum(x//mid for x in lines); cnt>=N 이면 ans=mid, lo=mid+1 아니면 hi=mid-1.",
        ],
        testcases=[
            {"input": "4 11\n802\n743\n457\n539\n", "output": "200\n"},
            {"input": "1 1\n5\n", "output": "5\n"},
            {"input": "2 3\n10\n10\n", "output": "5\n"},
            {"input": "3 7\n1\n2\n3\n", "output": "0\n"},
        ],
        reference_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "k, n = map(int, input().split())\n"
            "lines = [int(input()) for _ in range(k)]\n"
            "lo, hi, ans = 1, max(lines), 0\n"
            "while lo <= hi:\n"
            "    mid = (lo + hi) // 2\n"
            "    cnt = sum(x // mid for x in lines)\n"
            "    if cnt >= n:\n"
            "        ans = mid\n"
            "        lo = mid + 1\n"
            "    else:\n"
            "        hi = mid - 1\n"
            "print(ans)\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int k = Integer.parseInt(st.nextToken());\n"
            "        long n = Long.parseLong(st.nextToken());\n"
            "        long[] a = new long[k];\n"
            "        long hi = 1;\n"
            "        for (int i = 0; i < k; i++) { a[i] = Long.parseLong(br.readLine().trim()); hi = Math.max(hi, a[i]); }\n"
            "        long lo = 1, ans = 0;\n"
            "        while (lo <= hi) {\n"
            "            long mid = (lo + hi) / 2, cnt = 0;\n"
            "            for (long x : a) cnt += x / mid;\n"
            "            if (cnt >= n) { ans = mid; lo = mid + 1; } else hi = mid - 1;\n"
            "        }\n"
            "        System.out.println(ans);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "# N개 이상 만들 수 있는 랜선의 최대 길이\n"
            "k, n = map(int, input().split())\n"
            "# lines = ...\n"
        ),
    ),

    Problem(
        id="silver-11",
        rank="Silver",
        title="좌표 압축하기",
        style="백준",
        topic="좌표 압축",
        type="stdin",
        description=(
            "수열의 각 원소를, 그 원소보다 작은 서로 다른 값의 개수로 바꾸는 것을 좌표 압축이라 한다. "
            "즉 값들을 크기 순위(0부터 시작)로 치환한다. 압축된 수열을 출력하시오."
        ),
        input_desc=(
            "첫째 줄에 수열의 길이 N(1 ≤ N ≤ 1000000). 둘째 줄에 N개의 정수가 공백으로 "
            "구분되어 주어진다. (-1000000000 ≤ 값 ≤ 1000000000)"
        ),
        output_desc="압축된 N개의 값을 공백으로 구분해 한 줄에 출력한다.",
        examples=[
            {"input": "5\n2 4 -10 4 -9\n", "output": "2 3 0 3 1\n"},
            {"input": "4\n-1 0 1 0\n", "output": "0 1 2 1\n"},
        ],
        hints=[
            "각 값을 '자신보다 작은 서로 다른 값의 개수' 로 바꾸는 것은, 정렬된 고유값들 속에서의 위치(인덱스)와 같습니다.",
            "중복을 제거하고 정렬한 뒤(sorted(set(arr))), 각 값 -> 인덱스 매핑을 dict 로 만들어 두면 빠르게 변환할 수 있습니다.",
            "comp = sorted(set(arr)); rank = {v: i for i, v in enumerate(comp)}; 결과는 [rank[x] for x in arr].",
        ],
        testcases=[
            {"input": "5\n2 4 -10 4 -9\n", "output": "2 3 0 3 1\n"},
            {"input": "1\n100\n", "output": "0\n"},
            {"input": "3\n5 5 5\n", "output": "0 0 0\n"},
            {"input": "4\n-1 0 1 0\n", "output": "0 1 2 1\n"},
        ],
        reference_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "n = int(input())\n"
            "arr = list(map(int, input().split()))\n"
            "comp = sorted(set(arr))\n"
            "rank = {v: i for i, v in enumerate(comp)}\n"
            "print(' '.join(str(rank[x]) for x in arr))\n"
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
            "        int[] s = arr.clone();\n"
            "        Arrays.sort(s);\n"
            "        TreeMap<Integer, Integer> rank = new TreeMap<>();\n"
            "        int idx = 0;\n"
            "        for (int v : s) if (!rank.containsKey(v)) rank.put(v, idx++);\n"
            "        StringBuilder sb = new StringBuilder();\n"
            "        for (int x : arr) sb.append(rank.get(x)).append(' ');\n"
            "        System.out.println(sb.toString().trim());\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "# 각 값을 '자신보다 작은 서로 다른 값의 개수' 로 변환\n"
            "n = int(input())\n"
            "# arr = ...\n"
        ),
    ),

    Problem(
        id="silver-12",
        rank="Silver",
        title="K번째 수 뽑기",
        style="프로그래머스",
        topic="정렬",
        type="func",
        func_name="solution",
        description=(
            "배열 array 와 명령 목록 commands 가 주어진다. 각 명령 [i, j, k] 는 "
            "array 의 i번째부터 j번째까지(1-based, 양 끝 포함)를 잘라 정렬했을 때 k번째에 "
            "있는 수를 의미한다. 각 명령의 결과를 순서대로 담은 리스트를 반환하세요."
        ),
        input_desc="array : 정수 리스트, commands : [[i, j, k], ...] (1 ≤ i ≤ j ≤ len(array), 1 ≤ k ≤ j-i+1)",
        output_desc="각 명령에 대한 K번째 수를 담은 리스트",
        examples=[
            {"args": [[1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]], "output": [5, 6, 3]},
            {"args": [[1, 2, 3], [[1, 3, 2]]], "output": [2]},
        ],
        hints=[
            "명령마다 '구간을 자르고 → 정렬하고 → k번째를 고른다' 라는 같은 작업을 반복하면 됩니다.",
            "리스트 슬라이싱 array[i-1:j] 로 구간을 자르고 sorted() 로 정렬한 뒤 인덱스 [k-1] 을 고르세요.",
            "return [sorted(array[i-1:j])[k-1] for i, j, k in commands]",
        ],
        testcases=[
            {"args": [[1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]], "expected": [5, 6, 3]},
            {"args": [[1, 2, 3], [[1, 3, 2]]], "expected": [2]},
            {"args": [[3, 1, 2], [[1, 1, 1], [2, 3, 1]]], "expected": [3, 1]},
            {"args": [[10], [[1, 1, 1]]], "expected": [10]},
        ],
        reference_py=(
            "def solution(array, commands):\n"
            "    return [sorted(array[i - 1:j])[k - 1] for i, j, k in commands]\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int[] solution(int[] array, int[][] commands) {\n"
            "        int[] ans = new int[commands.length];\n"
            "        for (int c = 0; c < commands.length; c++) {\n"
            "            int i = commands[c][0], j = commands[c][1], k = commands[c][2];\n"
            "            int[] sub = Arrays.copyOfRange(array, i - 1, j);\n"
            "            Arrays.sort(sub);\n"
            "            ans[c] = sub[k - 1];\n"
            "        }\n"
            "        return ans;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 각 명령 [i, j, k] 에 대해 구간을 정렬해 k번째 수를 모아 반환\n"
            "def solution(array, commands):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="silver-13",
        rank="Silver",
        title="성적 순위표 만들기",
        style="대기업",
        topic="다중 키 정렬",
        type="func",
        func_name="solution",
        description=(
            "학생들의 [이름, 점수] 목록이 주어진다. 점수가 높은 순으로 정렬하되, 점수가 같으면 "
            "이름의 사전 순으로 정렬하여 이름만 순서대로 담은 리스트를 반환하세요."
        ),
        input_desc="students : [[name, score], ...] (name 은 영문 문자열, score 는 정수)",
        output_desc="정렬된 순서대로의 이름 리스트",
        examples=[
            {"args": [[["alice", 90], ["bob", 85], ["carol", 90]]], "output": ["alice", "carol", "bob"]},
            {"args": [[["x", 10], ["y", 20], ["z", 15]]], "output": ["y", "z", "x"]},
        ],
        hints=[
            "정렬 기준이 둘입니다. 하나는 점수(내림차순), 하나는 이름(오름차순)이라 방향이 서로 다릅니다.",
            "key=lambda s: (-s[1], s[0]) 처럼 점수에 음수를 붙이면 내림차순, 이름은 그대로 오름차순으로 한 번에 정렬됩니다.",
            "ordered = sorted(students, key=lambda s: (-s[1], s[0])); return [name for name, score in ordered]",
        ],
        testcases=[
            {"args": [[["alice", 90], ["bob", 85], ["carol", 90]]], "expected": ["alice", "carol", "bob"]},
            {"args": [[["z", 50]]], "expected": ["z"]},
            {"args": [[["a", 70], ["b", 70]]], "expected": ["a", "b"]},
            {"args": [[["x", 10], ["y", 20], ["z", 15]]], "expected": ["y", "z", "x"]},
        ],
        reference_py=(
            "def solution(students):\n"
            "    ordered = sorted(students, key=lambda s: (-s[1], s[0]))\n"
            "    return [name for name, score in ordered]\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public String[] solution(Object[][] students) {\n"
            "        Arrays.sort(students, (a, b) -> {\n"
            "            int sa = (int) a[1], sb = (int) b[1];\n"
            "            if (sa != sb) return sb - sa;\n"
            "            return ((String) a[0]).compareTo((String) b[0]);\n"
            "        });\n"
            "        String[] ans = new String[students.length];\n"
            "        for (int i = 0; i < students.length; i++) ans[i] = (String) students[i][0];\n"
            "        return ans;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 점수 내림차순, 같으면 이름 오름차순 -> 이름 리스트 반환\n"
            "def solution(students):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="silver-14",
        rank="Silver",
        title="정렬된 배열에서 삽입 위치 찾기",
        style="해외대기업",
        topic="이분 탐색",
        type="func",
        func_name="solution",
        description=(
            "오름차순으로 정렬된 정수 배열 arr 와 정수 x 가 주어진다. x 이상인 첫 번째 원소의 "
            "인덱스(0-based)를 반환하세요. 그런 원소가 없으면 배열의 길이를 반환합니다. "
            "(이는 x 를 정렬을 유지하며 삽입할 수 있는 가장 왼쪽 위치, 즉 lower bound 입니다.)"
        ),
        input_desc="arr : 오름차순 정렬된 정수 리스트(중복 가능), x : 찾을 기준 정수",
        output_desc="arr[i] >= x 를 만족하는 가장 작은 인덱스 i (없으면 len(arr))",
        examples=[
            {"args": [[1, 3, 3, 5, 7], 3], "output": 1},
            {"args": [[1, 3, 3, 5, 7], 8], "output": 5},
        ],
        hints=[
            "정렬된 배열이라는 점을 이용하면 선형 탐색(O(N))보다 빠르게 위치를 찾을 수 있습니다.",
            "이분 탐색의 lower bound 패턴입니다. arr[mid] < x 이면 오른쪽(lo=mid+1), 아니면 왼쪽(hi=mid)으로 범위를 좁힙니다. bisect.bisect_left 도 동일합니다.",
            "lo, hi = 0, len(arr); while lo<hi: mid=(lo+hi)//2; arr[mid]<x 이면 lo=mid+1 아니면 hi=mid; return lo",
        ],
        testcases=[
            {"args": [[1, 3, 3, 5, 7], 3], "expected": 1},
            {"args": [[1, 3, 3, 5, 7], 4], "expected": 3},
            {"args": [[1, 3, 3, 5, 7], 8], "expected": 5},
            {"args": [[1, 3, 3, 5, 7], 0], "expected": 0},
            {"args": [[], 5], "expected": 0},
        ],
        reference_py=(
            "def solution(arr, x):\n"
            "    lo, hi = 0, len(arr)\n"
            "    while lo < hi:\n"
            "        mid = (lo + hi) // 2\n"
            "        if arr[mid] < x:\n"
            "            lo = mid + 1\n"
            "        else:\n"
            "            hi = mid\n"
            "    return lo\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(int[] arr, int x) {\n"
            "        int lo = 0, hi = arr.length;\n"
            "        while (lo < hi) {\n"
            "            int mid = (lo + hi) / 2;\n"
            "            if (arr[mid] < x) lo = mid + 1; else hi = mid;\n"
            "        }\n"
            "        return lo;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# x 이상인 첫 인덱스(lower bound), 없으면 len(arr)\n"
            "def solution(arr, x):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="silver-15",
        rank="Silver",
        title="원점에서 가까운 K개 좌표",
        style="해외대기업",
        topic="좌표 정렬",
        type="func",
        func_name="solution",
        description=(
            "평면 위 점들의 목록 points 와 정수 k 가 주어진다. 원점(0, 0)에서 가까운 순서로 "
            "k개의 점을 반환하세요. 거리가 같으면 x좌표가 작은 것, x도 같으면 y좌표가 작은 것을 "
            "먼저 둡니다. 반환 형식은 [[x, y], ...] 입니다."
        ),
        input_desc="points : [[x, y], ...] 형태의 좌표 리스트, k : 고를 개수 (1 ≤ k ≤ len(points))",
        output_desc="원점에서 가까운 순으로 정렬한 상위 k개의 [x, y] 리스트",
        examples=[
            {"args": [[[1, 3], [-2, 2]], 1], "output": [[-2, 2]]},
            {"args": [[[3, 3], [5, -1], [-2, 4]], 2], "output": [[3, 3], [-2, 4]]},
        ],
        hints=[
            "유클리드 거리는 제곱근까지 구할 필요 없이, 거리의 제곱 x*x + y*y 만으로 대소를 비교할 수 있습니다.",
            "거리 제곱을 기준으로 정렬한 뒤 앞에서 k개를 잘라내면 됩니다. 동점 처리를 위해 (거리, x, y) 를 key 로 쓰세요.",
            "pts = sorted(points, key=lambda p: (p[0]*p[0]+p[1]*p[1], p[0], p[1])); return pts[:k]",
        ],
        testcases=[
            {"args": [[[1, 3], [-2, 2]], 1], "expected": [[-2, 2]]},
            {"args": [[[3, 3], [5, -1], [-2, 4]], 2], "expected": [[3, 3], [-2, 4]]},
            {"args": [[[1, 1]], 1], "expected": [[1, 1]]},
            {"args": [[[0, 1], [1, 0]], 2], "expected": [[0, 1], [1, 0]]},
        ],
        reference_py=(
            "def solution(points, k):\n"
            "    pts = sorted(points, key=lambda p: (p[0] * p[0] + p[1] * p[1], p[0], p[1]))\n"
            "    return pts[:k]\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int[][] solution(int[][] points, int k) {\n"
            "        Arrays.sort(points, (a, b) -> {\n"
            "            long da = (long) a[0]*a[0] + (long) a[1]*a[1];\n"
            "            long db = (long) b[0]*b[0] + (long) b[1]*b[1];\n"
            "            if (da != db) return Long.compare(da, db);\n"
            "            if (a[0] != b[0]) return a[0] - b[0];\n"
            "            return a[1] - b[1];\n"
            "        });\n"
            "        return Arrays.copyOfRange(points, 0, k);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 원점에서 가까운 순으로 k개 반환 ([[x, y], ...])\n"
            "def solution(points, k):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="silver-16",
        rank="Silver",
        title="예산 배정",
        style="백준",
        topic="매개변수 탐색",
        type="stdin",
        description=(
            "각 지방의 예산 요청 금액과 총예산이 주어진다. 모든 요청에 상한액을 정해, 요청이 상한액 "
            "이하면 그대로, 초과하면 상한액만큼 배정한다. 배정 총액이 총예산을 넘지 않는 범위에서 "
            "가능한 상한액의 최댓값을 구하시오. (모든 요청을 들어줄 수 있으면 가장 큰 요청 금액)"
        ),
        input_desc=(
            "첫째 줄에 지방의 수 N(1 ≤ N ≤ 10000). 둘째 줄에 각 지방의 요청 금액 N개가 공백으로, "
            "셋째 줄에 총예산 M 이 주어진다."
        ),
        output_desc="가능한 상한액의 최댓값을 출력한다.",
        examples=[
            {"input": "4\n120 110 140 150\n485\n", "output": "127\n"},
            {"input": "3\n70 80 30\n10\n", "output": "3\n"},
        ],
        hints=[
            "상한액을 크게 잡을수록 배정 총액이 커집니다. 상한액과 배정 총액 사이에 단조 증가 관계가 있습니다.",
            "0부터 가장 큰 요청 금액까지 상한액을 이분 탐색(매개변수 탐색)하면서 'sum(min(요청, 상한)) ≤ M' 을 만족하는 최대값을 찾으세요.",
            "while lo<=hi: mid=(lo+hi)//2; total=sum(min(x,mid) for x in req); total<=M 이면 ans=mid, lo=mid+1 아니면 hi=mid-1.",
        ],
        testcases=[
            {"input": "4\n120 110 140 150\n485\n", "output": "127\n"},
            {"input": "3\n70 80 30\n10\n", "output": "3\n"},
            {"input": "1\n5\n100\n", "output": "5\n"},
            {"input": "2\n10 10\n0\n", "output": "0\n"},
        ],
        reference_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "n = int(input())\n"
            "req = list(map(int, input().split()))\n"
            "m = int(input())\n"
            "lo, hi, ans = 0, max(req), 0\n"
            "while lo <= hi:\n"
            "    mid = (lo + hi) // 2\n"
            "    total = sum(min(x, mid) for x in req)\n"
            "    if total <= m:\n"
            "        ans = mid\n"
            "        lo = mid + 1\n"
            "    else:\n"
            "        hi = mid - 1\n"
            "print(ans)\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        int n = Integer.parseInt(br.readLine().trim());\n"
            "        int[] req = new int[n];\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int hi = 0;\n"
            "        for (int i = 0; i < n; i++) { req[i] = Integer.parseInt(st.nextToken()); hi = Math.max(hi, req[i]); }\n"
            "        long m = Long.parseLong(br.readLine().trim());\n"
            "        int lo = 0, ans = 0;\n"
            "        while (lo <= hi) {\n"
            "            int mid = (lo + hi) / 2;\n"
            "            long total = 0;\n"
            "            for (int x : req) total += Math.min(x, mid);\n"
            "            if (total <= m) { ans = mid; lo = mid + 1; } else hi = mid - 1;\n"
            "        }\n"
            "        System.out.println(ans);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "# 배정 총액이 M 이하가 되는 상한액의 최댓값\n"
            "n = int(input())\n"
            "# req = ...\n"
        ),
    ),

    Problem(
        id="silver-17",
        rank="Silver",
        title="정렬된 배열에서 값의 개수",
        style="해외대기업",
        topic="이분 탐색",
        type="func",
        func_name="solution",
        description=(
            "오름차순으로 정렬된 정수 배열 arr 와 정수 x 가 주어진다. arr 안에 x 가 몇 번 "
            "등장하는지 그 개수를 반환하세요. 배열이 크다고 가정하고 O(log N) 으로 풀어 보세요."
        ),
        input_desc="arr : 오름차순 정렬된 정수 리스트(중복 가능), x : 셀 대상 정수",
        output_desc="arr 에서 x 가 등장하는 횟수",
        examples=[
            {"args": [[1, 1, 2, 2, 2, 3], 2], "output": 3},
            {"args": [[1, 1, 2, 2, 2, 3], 4], "output": 0},
        ],
        hints=[
            "정렬되어 있으므로 같은 값은 항상 연속으로 모여 있습니다. x의 '시작 위치'와 '끝 다음 위치'만 알면 개수를 알 수 있습니다.",
            "x 이상이 처음 나오는 위치(lower bound)와 x 초과가 처음 나오는 위치(upper bound)를 이분 탐색으로 찾아 그 차이를 구하세요. bisect_left, bisect_right 와 동일합니다.",
            "import bisect; return bisect.bisect_right(arr, x) - bisect.bisect_left(arr, x)",
        ],
        testcases=[
            {"args": [[1, 1, 2, 2, 2, 3], 2], "expected": 3},
            {"args": [[1, 1, 2, 2, 2, 3], 4], "expected": 0},
            {"args": [[1, 1, 2, 2, 2, 3], 1], "expected": 2},
            {"args": [[], 1], "expected": 0},
            {"args": [[5, 5, 5, 5], 5], "expected": 4},
        ],
        reference_py=(
            "import bisect\n"
            "def solution(arr, x):\n"
            "    return bisect.bisect_right(arr, x) - bisect.bisect_left(arr, x)\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    private int lower(int[] a, int x) {\n"
            "        int lo = 0, hi = a.length;\n"
            "        while (lo < hi) { int m = (lo + hi) / 2; if (a[m] < x) lo = m + 1; else hi = m; }\n"
            "        return lo;\n"
            "    }\n"
            "    private int upper(int[] a, int x) {\n"
            "        int lo = 0, hi = a.length;\n"
            "        while (lo < hi) { int m = (lo + hi) / 2; if (a[m] <= x) lo = m + 1; else hi = m; }\n"
            "        return lo;\n"
            "    }\n"
            "    public int solution(int[] arr, int x) {\n"
            "        return upper(arr, x) - lower(arr, x);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 정렬된 배열에서 x 의 등장 횟수 (O(log N))\n"
            "def solution(arr, x):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="silver-18",
        rank="Silver",
        title="문자열 길이순 정렬",
        style="대기업",
        topic="커스텀 정렬",
        type="func",
        func_name="solution",
        description=(
            "문자열 목록 words 가 주어진다. 길이가 긴 것부터, 길이가 같으면 사전 순(오름차순)으로 "
            "정렬한 리스트를 반환하세요."
        ),
        input_desc="words : 문자열 리스트",
        output_desc="(길이 내림차순, 같으면 사전 오름차순) 으로 정렬한 문자열 리스트",
        examples=[
            {"args": [["bb", "a", "ccc", "dd"]], "output": ["ccc", "bb", "dd", "a"]},
            {"args": [["zz", "aa", "mm"]], "output": ["aa", "mm", "zz"]},
        ],
        hints=[
            "정렬 방향이 기준마다 다릅니다. 길이는 내림차순, 사전 순은 오름차순이라 단순히 reverse=True 한 번으로는 안 됩니다.",
            "key=lambda w: (-len(w), w) 를 쓰면 길이는 음수로 만들어 내림차순, 문자열은 그대로 오름차순으로 한 번에 정렬됩니다.",
            "return sorted(words, key=lambda w: (-len(w), w))",
        ],
        testcases=[
            {"args": [["bb", "a", "ccc", "dd"]], "expected": ["ccc", "bb", "dd", "a"]},
            {"args": [["x"]], "expected": ["x"]},
            {"args": [["ab", "cd", "a"]], "expected": ["ab", "cd", "a"]},
            {"args": [["zz", "aa", "mm"]], "expected": ["aa", "mm", "zz"]},
        ],
        reference_py=(
            "def solution(words):\n"
            "    return sorted(words, key=lambda w: (-len(w), w))\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public String[] solution(String[] words) {\n"
            "        Arrays.sort(words, (a, b) ->\n"
            "            a.length() != b.length() ? b.length() - a.length() : a.compareTo(b));\n"
            "        return words;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 길이 내림차순, 같으면 사전 오름차순\n"
            "def solution(words):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="silver-19",
        rank="Silver",
        title="중앙값 구하기",
        style="백준",
        topic="정렬",
        type="stdin",
        description=(
            "홀수 개의 정수가 주어졌을 때, 이들을 정렬했을 때 한가운데에 오는 값(중앙값)을 출력하시오."
        ),
        input_desc=(
            "첫째 줄에 정수의 개수 N(N 은 홀수, 1 ≤ N ≤ 100000). 둘째 줄에 N개의 정수가 "
            "공백으로 구분되어 주어진다."
        ),
        output_desc="정렬했을 때 가운데에 위치하는 값을 출력한다.",
        examples=[
            {"input": "5\n5 1 4 3 2\n", "output": "3\n"},
            {"input": "3\n-5 0 -1\n", "output": "-1\n"},
        ],
        hints=[
            "중앙값은 '정렬했을 때 가운데 위치' 의 값입니다. 먼저 정렬부터 생각하세요.",
            "정렬한 배열에서 인덱스 N//2 (0-based) 가 가운데 위치입니다. 별도의 통계 계산이 필요 없습니다.",
            "arr.sort(); print(arr[n // 2])",
        ],
        testcases=[
            {"input": "5\n5 1 4 3 2\n", "output": "3\n"},
            {"input": "1\n7\n", "output": "7\n"},
            {"input": "3\n-5 0 -1\n", "output": "-1\n"},
            {"input": "5\n1 1 1 1 1\n", "output": "1\n"},
        ],
        reference_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "n = int(input())\n"
            "arr = list(map(int, input().split()))\n"
            "arr.sort()\n"
            "print(arr[n // 2])\n"
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
            "        Arrays.sort(arr);\n"
            "        System.out.println(arr[n / 2]);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "# 정렬 후 가운데 값 출력\n"
            "n = int(input())\n"
            "# arr = ...\n"
        ),
    ),

    Problem(
        id="silver-20",
        rank="Silver",
        title="점수 순위 매기기",
        style="프로그래머스",
        topic="좌표 압축",
        type="func",
        func_name="solution",
        description=(
            "학생들의 점수 리스트 scores 가 주어진다. 각 학생의 등수를 같은 순서로 담은 리스트를 "
            "반환하세요. 점수가 높을수록 등수가 높고(1등), 점수가 같으면 같은 등수입니다. "
            "어떤 점수의 등수는 '자신보다 점수가 높은 사람 수 + 1' 입니다."
        ),
        input_desc="scores : 정수 점수 리스트",
        output_desc="각 학생의 등수를 입력과 같은 순서로 담은 리스트",
        examples=[
            {"args": [[80, 60, 70, 100, 90]], "output": [3, 5, 4, 1, 2]},
            {"args": [[10, 20, 20, 40]], "output": [4, 2, 2, 1]},
        ],
        hints=[
            "각 점수의 등수는 '자신보다 높은 점수가 몇 개 있는가' 에 1을 더한 값입니다. 동점은 자연히 같은 등수가 됩니다.",
            "점수를 내림차순으로 정렬해 두면, 어떤 값의 등수는 정렬된 배열에서 그 값이 처음 등장하는 위치 + 1 과 같습니다(좌표 압축/순위화). dict 로 점수→등수를 미리 만들어 두세요.",
            "ordered = sorted(scores, reverse=True); rank = {}; for i, v in enumerate(ordered): rank.setdefault(v, i + 1); return [rank[s] for s in scores]",
        ],
        testcases=[
            {"args": [[80, 60, 70, 100, 90]], "expected": [3, 5, 4, 1, 2]},
            {"args": [[100]], "expected": [1]},
            {"args": [[50, 50, 50]], "expected": [1, 1, 1]},
            {"args": [[10, 20, 20, 40]], "expected": [4, 2, 2, 1]},
        ],
        reference_py=(
            "def solution(scores):\n"
            "    ordered = sorted(scores, reverse=True)\n"
            "    rank = {}\n"
            "    for i, v in enumerate(ordered):\n"
            "        rank.setdefault(v, i + 1)\n"
            "    return [rank[s] for s in scores]\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int[] solution(int[] scores) {\n"
            "        int n = scores.length;\n"
            "        Integer[] ordered = new Integer[n];\n"
            "        for (int i = 0; i < n; i++) ordered[i] = scores[i];\n"
            "        Arrays.sort(ordered, Collections.reverseOrder());\n"
            "        HashMap<Integer, Integer> rank = new HashMap<>();\n"
            "        for (int i = 0; i < n; i++) rank.putIfAbsent(ordered[i], i + 1);\n"
            "        int[] ans = new int[n];\n"
            "        for (int i = 0; i < n; i++) ans[i] = rank.get(scores[i]);\n"
            "        return ans;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 각 점수의 등수(자신보다 높은 점수 수 + 1) 리스트 반환\n"
            "def solution(scores):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

]
