"""플래티넘 배치 B — 고급 자료구조.

세그먼트 트리(최솟값/최댓값/곱), 펜윅 트리(BIT), LCA, 이분 탐색+세그트리,
좌표 압축+세그트리. base 의 '구간 합 세그먼트 트리'와 겹치지 않게 구성.

문제 15개 : platinum-21 ~ platinum-35.
"""

from engine.models import Problem

RANK = "Platinum"

PROBLEMS = [

    # ============================================================ 21
    Problem(
        id="platinum-21",
        rank="Platinum",
        title="구간 최솟값 질의와 갱신",
        style="프로그래머스",
        topic="세그먼트트리",
        type="func",
        func_name="solution",
        description=(
            "정수 배열 arr 와 질의 목록 queries 가 주어집니다. 각 질의는 두 종류입니다.\n"
            "  - ['U', i, x] : arr 의 i번째(1-based) 값을 x 로 바꿉니다.\n"
            "  - ['Q', l, r] : l번째부터 r번째까지(1-based, 양끝 포함) 구간의 최솟값을 답합니다.\n"
            "모든 'Q' 질의의 답을 순서대로 리스트로 반환하세요. 갱신과 질의가 번갈아 많이 들어옵니다."
        ),
        input_desc="arr : 정수 리스트, queries : ['U',i,x] / ['Q',l,r] 의 리스트 (모두 1-based)",
        output_desc="'Q' 질의들의 답(구간 최솟값)을 순서대로 담은 리스트",
        examples=[
            {"args": [[5, 3, 8, 1, 9, 2], [["Q", 1, 3], ["U", 4, 7], ["Q", 3, 5], ["Q", 1, 6]]],
             "output": [3, 7, 2]},
            {"args": [[5, 3, 8, 1, 9, 2], [["Q", 2, 2], ["U", 2, 0], ["Q", 1, 3]]],
             "output": [3, 0]},
        ],
        hints=[
            "값이 계속 바뀌므로 매번 구간을 다시 훑으면 느립니다. 갱신과 질의 둘 다 빠르게 처리할 구조가 필요합니다.",
            "구간 최솟값 세그먼트 트리를 쓰세요. 리프는 원소, 내부 노드는 두 자식의 최솟값을 보관합니다.",
            "tree 크기 2*size(=2의 거듭제곱). update: 리프 갱신 후 부모로 올라가며 tree[p]=min(tree[2p],tree[2p+1]). query(l,r): 표준 반복 세그트리로 min 누적.",
        ],
        testcases=[
            {"args": [[5, 3, 8, 1, 9, 2], [["Q", 1, 3], ["U", 4, 7], ["Q", 3, 5], ["Q", 1, 6]]],
             "expected": [3, 7, 2]},
            {"args": [[5, 3, 8, 1, 9, 2], [["Q", 2, 2], ["U", 2, 0], ["Q", 1, 3]]],
             "expected": [3, 0]},
            {"args": [[10], [["Q", 1, 1], ["U", 1, 3], ["Q", 1, 1]]],
             "expected": [10, 3]},
            {"args": [[4, 4, 4, 4], [["Q", 1, 4], ["U", 2, 1], ["Q", 1, 2], ["Q", 3, 4]]],
             "expected": [4, 1, 4]},
        ],
        reference_py=r'''def solution(arr, queries):
    n = len(arr)
    size = 1
    while size < n:
        size *= 2
    INF = float('inf')
    tree = [INF] * (2 * size)
    for i in range(n):
        tree[size + i] = arr[i]
    for p in range(size - 1, 0, -1):
        tree[p] = min(tree[2 * p], tree[2 * p + 1])

    def update(idx, val):
        p = size + idx
        tree[p] = val
        p //= 2
        while p:
            tree[p] = min(tree[2 * p], tree[2 * p + 1])
            p //= 2

    def query(l, r):
        res = INF
        l += size
        r += size + 1
        while l < r:
            if l & 1:
                res = min(res, tree[l]); l += 1
            if r & 1:
                r -= 1; res = min(res, tree[r])
            l //= 2; r //= 2
        return res

    out = []
    for q in queries:
        if q[0] == 'U':
            update(q[1] - 1, q[2])
        else:
            out.append(query(q[1] - 1, q[2] - 1))
    return out
''',
        reference_java=r'''import java.util.*;
class Solution {
    int size; long[] tree;
    public int[] solution(int[] arr, Object[][] queries) {
        int n = arr.length; size = 1;
        while (size < n) size *= 2;
        long INF = Long.MAX_VALUE;
        tree = new long[2 * size];
        Arrays.fill(tree, INF);
        for (int i = 0; i < n; i++) tree[size + i] = arr[i];
        for (int p = size - 1; p >= 1; p--) tree[p] = Math.min(tree[2*p], tree[2*p+1]);
        List<Integer> out = new ArrayList<>();
        for (Object[] q : queries) {
            if (q[0].equals("U")) update((int)q[1] - 1, (int)q[2]);
            else out.add((int) query((int)q[1] - 1, (int)q[2] - 1));
        }
        return out.stream().mapToInt(Integer::intValue).toArray();
    }
    void update(int idx, long val) {
        int p = size + idx; tree[p] = val; p /= 2;
        while (p >= 1) { tree[p] = Math.min(tree[2*p], tree[2*p+1]); p /= 2; }
    }
    long query(int l, int r) {
        long res = Long.MAX_VALUE; l += size; r += size + 1;
        while (l < r) {
            if ((l & 1) == 1) res = Math.min(res, tree[l++]);
            if ((r & 1) == 1) res = Math.min(res, tree[--r]);
            l /= 2; r /= 2;
        }
        return res;
    }
}
''',
        template_py=(
            "# 구간 최솟값 세그먼트 트리 : 갱신(U)과 최솟값 질의(Q) 처리\n"
            "def solution(arr, queries):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

    # ============================================================ 22
    Problem(
        id="platinum-22",
        rank="Platinum",
        title="구간 최댓값 추적기",
        style="대기업",
        topic="세그먼트트리",
        type="func",
        func_name="solution",
        description=(
            "정수 배열 arr 와 질의 목록 queries 가 주어집니다. 각 질의는 두 종류입니다.\n"
            "  - ['U', i, x] : arr 의 i번째(1-based) 값을 x 로 바꿉니다.\n"
            "  - ['Q', l, r] : l번째부터 r번째까지(1-based, 양끝 포함) 구간의 최댓값을 답합니다.\n"
            "모든 'Q' 질의의 답을 순서대로 리스트로 반환하세요. 음수도 등장할 수 있습니다."
        ),
        input_desc="arr : 정수 리스트, queries : ['U',i,x] / ['Q',l,r] 의 리스트 (모두 1-based)",
        output_desc="'Q' 질의들의 답(구간 최댓값)을 순서대로 담은 리스트",
        examples=[
            {"args": [[5, 3, 8, 1, 9, 2], [["Q", 1, 3], ["U", 4, 7], ["Q", 3, 5], ["Q", 1, 6]]],
             "output": [8, 9, 9]},
            {"args": [[1, 2, 3], [["Q", 1, 3], ["U", 3, 0], ["Q", 1, 3]]],
             "output": [3, 2]},
        ],
        hints=[
            "최솟값 대신 최댓값을 묶어 올린다는 점만 다릅니다. 갱신·질의가 섞여 빠른 구조가 필요합니다.",
            "구간 최댓값 세그먼트 트리를 쓰세요. 항등원은 -무한대이며 내부 노드는 두 자식의 max 입니다.",
            "tree 초기값 -inf. update 후 부모로 올라가며 tree[p]=max(tree[2p],tree[2p+1]). query(l,r)는 반복 세그트리로 max 누적.",
        ],
        testcases=[
            {"args": [[5, 3, 8, 1, 9, 2], [["Q", 1, 3], ["U", 4, 7], ["Q", 3, 5], ["Q", 1, 6]]],
             "expected": [8, 9, 9]},
            {"args": [[1, 2, 3], [["Q", 1, 3], ["U", 3, 0], ["Q", 1, 3]]],
             "expected": [3, 2]},
            {"args": [[7], [["Q", 1, 1], ["U", 1, 2], ["Q", 1, 1]]],
             "expected": [7, 2]},
            {"args": [[-5, -3, -8], [["Q", 1, 3], ["U", 2, -1], ["Q", 1, 2]]],
             "expected": [-3, -1]},
        ],
        reference_py=r'''def solution(arr, queries):
    n = len(arr)
    size = 1
    while size < n:
        size *= 2
    NEG = float('-inf')
    tree = [NEG] * (2 * size)
    for i in range(n):
        tree[size + i] = arr[i]
    for p in range(size - 1, 0, -1):
        tree[p] = max(tree[2 * p], tree[2 * p + 1])

    def update(idx, val):
        p = size + idx
        tree[p] = val
        p //= 2
        while p:
            tree[p] = max(tree[2 * p], tree[2 * p + 1])
            p //= 2

    def query(l, r):
        res = NEG
        l += size
        r += size + 1
        while l < r:
            if l & 1:
                res = max(res, tree[l]); l += 1
            if r & 1:
                r -= 1; res = max(res, tree[r])
            l //= 2; r //= 2
        return res

    out = []
    for q in queries:
        if q[0] == 'U':
            update(q[1] - 1, q[2])
        else:
            out.append(query(q[1] - 1, q[2] - 1))
    return out
''',
        reference_java=r'''import java.util.*;
class Solution {
    int size; long[] tree;
    public int[] solution(int[] arr, Object[][] queries) {
        int n = arr.length; size = 1;
        while (size < n) size *= 2;
        tree = new long[2 * size];
        Arrays.fill(tree, Long.MIN_VALUE);
        for (int i = 0; i < n; i++) tree[size + i] = arr[i];
        for (int p = size - 1; p >= 1; p--) tree[p] = Math.max(tree[2*p], tree[2*p+1]);
        List<Integer> out = new ArrayList<>();
        for (Object[] q : queries) {
            if (q[0].equals("U")) update((int)q[1] - 1, (int)q[2]);
            else out.add((int) query((int)q[1] - 1, (int)q[2] - 1));
        }
        return out.stream().mapToInt(Integer::intValue).toArray();
    }
    void update(int idx, long val) {
        int p = size + idx; tree[p] = val; p /= 2;
        while (p >= 1) { tree[p] = Math.max(tree[2*p], tree[2*p+1]); p /= 2; }
    }
    long query(int l, int r) {
        long res = Long.MIN_VALUE; l += size; r += size + 1;
        while (l < r) {
            if ((l & 1) == 1) res = Math.max(res, tree[l++]);
            if ((r & 1) == 1) res = Math.max(res, tree[--r]);
            l /= 2; r /= 2;
        }
        return res;
    }
}
''',
        template_py=(
            "# 구간 최댓값 세그먼트 트리 : 갱신(U)과 최댓값 질의(Q) 처리\n"
            "def solution(arr, queries):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

    # ============================================================ 23
    Problem(
        id="platinum-23",
        rank="Platinum",
        title="구간 곱 나머지 질의",
        style="백준",
        topic="세그먼트트리",
        type="func",
        func_name="solution",
        description=(
            "정수 배열 arr 와 질의 목록 queries 가 주어집니다.\n"
            "  - ['U', i, x] : arr 의 i번째(1-based) 값을 x 로 바꿉니다.\n"
            "  - ['Q', l, r] : l번째부터 r번째까지의 모든 값을 곱한 결과를 1,000,000,007 로 나눈 나머지를 답합니다.\n"
            "모든 'Q' 질의의 답을 순서대로 리스트로 반환하세요. 0이 곱에 섞이는 경우도 처리해야 합니다."
        ),
        input_desc="arr : 0 이상 정수 리스트, queries : ['U',i,x] / ['Q',l,r] 의 리스트 (1-based)",
        output_desc="'Q' 질의들의 답(구간 곱 mod 1e9+7)을 순서대로 담은 리스트",
        examples=[
            {"args": [[1, 2, 3, 4, 5], [["Q", 1, 3], ["U", 2, 10], ["Q", 1, 3], ["Q", 4, 5]]],
             "output": [6, 30, 20]},
            {"args": [[2, 2, 2], [["Q", 1, 3], ["U", 1, 5], ["Q", 1, 2]]],
             "output": [8, 10]},
        ],
        hints=[
            "곱도 결합법칙이 성립하므로 구간으로 묶어 올릴 수 있습니다. 갱신이 섞여 단순 누적곱은 매번 다시 만들어야 해 비효율적입니다.",
            "곱 세그먼트 트리를 쓰세요. 항등원은 1이고 내부 노드는 두 자식 곱을 모듈러 곱으로 보관합니다. 0이 들어가면 자연스럽게 구간 곱이 0이 됩니다.",
            "tree 초기값 1. 모든 연산에 %MOD 적용. update: tree[p]=tree[2p]*tree[2p+1]%MOD 로 부모 갱신. query(l,r)는 반복 세그트리로 곱 누적(res*tree[*]%MOD).",
        ],
        testcases=[
            {"args": [[1, 2, 3, 4, 5], [["Q", 1, 3], ["U", 2, 10], ["Q", 1, 3], ["Q", 4, 5]]],
             "expected": [6, 30, 20]},
            {"args": [[2, 2, 2], [["Q", 1, 3], ["U", 1, 5], ["Q", 1, 2]]],
             "expected": [8, 10]},
            {"args": [[6], [["Q", 1, 1], ["U", 1, 7], ["Q", 1, 1]]],
             "expected": [6, 7]},
            {"args": [[1, 0, 4], [["Q", 1, 3], ["U", 2, 3], ["Q", 1, 3]]],
             "expected": [0, 12]},
        ],
        reference_py=r'''def solution(arr, queries):
    MOD = 1000000007
    n = len(arr)
    size = 1
    while size < n:
        size *= 2
    tree = [1] * (2 * size)
    for i in range(n):
        tree[size + i] = arr[i] % MOD
    for p in range(size - 1, 0, -1):
        tree[p] = tree[2 * p] * tree[2 * p + 1] % MOD

    def update(idx, val):
        p = size + idx
        tree[p] = val % MOD
        p //= 2
        while p:
            tree[p] = tree[2 * p] * tree[2 * p + 1] % MOD
            p //= 2

    def query(l, r):
        res = 1
        l += size
        r += size + 1
        while l < r:
            if l & 1:
                res = res * tree[l] % MOD; l += 1
            if r & 1:
                r -= 1; res = res * tree[r] % MOD
            l //= 2; r //= 2
        return res

    out = []
    for q in queries:
        if q[0] == 'U':
            update(q[1] - 1, q[2])
        else:
            out.append(query(q[1] - 1, q[2] - 1))
    return out
''',
        reference_java=r'''import java.util.*;
class Solution {
    static final long MOD = 1000000007L;
    int size; long[] tree;
    public int[] solution(int[] arr, Object[][] queries) {
        int n = arr.length; size = 1;
        while (size < n) size *= 2;
        tree = new long[2 * size];
        Arrays.fill(tree, 1L);
        for (int i = 0; i < n; i++) tree[size + i] = arr[i] % MOD;
        for (int p = size - 1; p >= 1; p--) tree[p] = tree[2*p] * tree[2*p+1] % MOD;
        List<Integer> out = new ArrayList<>();
        for (Object[] q : queries) {
            if (q[0].equals("U")) update((int)q[1] - 1, (int)q[2]);
            else out.add((int) query((int)q[1] - 1, (int)q[2] - 1));
        }
        return out.stream().mapToInt(Integer::intValue).toArray();
    }
    void update(int idx, long val) {
        int p = size + idx; tree[p] = val % MOD; p /= 2;
        while (p >= 1) { tree[p] = tree[2*p] * tree[2*p+1] % MOD; p /= 2; }
    }
    long query(int l, int r) {
        long res = 1; l += size; r += size + 1;
        while (l < r) {
            if ((l & 1) == 1) res = res * tree[l++] % MOD;
            if ((r & 1) == 1) res = res * tree[--r] % MOD;
            l /= 2; r /= 2;
        }
        return res;
    }
}
''',
        template_py=(
            "# 구간 곱(mod 1e9+7) 세그먼트 트리 : 갱신(U)과 곱 질의(Q) 처리\n"
            "def solution(arr, queries):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

    # ============================================================ 24
    Problem(
        id="platinum-24",
        rank="Platinum",
        title="펜윅 트리로 가산과 구간합",
        style="백준",
        topic="펜윅트리",
        type="func",
        func_name="solution",
        description=(
            "정수 배열 arr 와 질의 목록 queries 가 주어집니다.\n"
            "  - ['A', i, x] : arr 의 i번째(1-based) 값에 x 를 더합니다(누적 가산).\n"
            "  - ['Q', l, r] : l번째부터 r번째까지의 구간 합을 답합니다.\n"
            "모든 'Q' 질의의 답을 순서대로 리스트로 반환하세요. 펜윅 트리(BIT)로 처리하세요."
        ),
        input_desc="arr : 정수 리스트, queries : ['A',i,x] / ['Q',l,r] 의 리스트 (1-based)",
        output_desc="'Q' 질의들의 답(구간 합)을 순서대로 담은 리스트",
        examples=[
            {"args": [[1, 2, 3, 4, 5], [["Q", 1, 3], ["A", 2, 10], ["Q", 1, 3], ["Q", 4, 5]]],
             "output": [6, 16, 9]},
            {"args": [[5, 5, 5], [["Q", 1, 3], ["A", 1, -5], ["Q", 1, 1]]],
             "output": [15, 0]},
        ],
        hints=[
            "한 점에 값을 더하고 임의 구간 합을 빠르게 묻는 전형적인 패턴입니다. 누적합은 가산마다 다시 만들어야 해 비효율적입니다.",
            "펜윅 트리(BIT)를 쓰세요. add(i,v)는 i에서 시작해 i += i&-i 로 올라가고, prefix(i)는 i -= i&-i 로 내려가며 합을 모읍니다.",
            "구간합 [l,r] = prefix(r) - prefix(l-1). 초기 배열은 각 원소를 add 로 한 번씩 넣어 만듭니다. 인덱스는 1-based.",
        ],
        testcases=[
            {"args": [[1, 2, 3, 4, 5], [["Q", 1, 3], ["A", 2, 10], ["Q", 1, 3], ["Q", 4, 5]]],
             "expected": [6, 16, 9]},
            {"args": [[5, 5, 5], [["Q", 1, 3], ["A", 1, -5], ["Q", 1, 1]]],
             "expected": [15, 0]},
            {"args": [[10], [["Q", 1, 1], ["A", 1, 7], ["Q", 1, 1]]],
             "expected": [10, 17]},
            {"args": [[1, 1, 1, 1], [["A", 1, 4], ["A", 4, 2], ["Q", 1, 4], ["Q", 2, 3]]],
             "expected": [10, 2]},
        ],
        reference_py=r'''def solution(arr, queries):
    n = len(arr)
    bit = [0] * (n + 1)

    def add(i, v):
        while i <= n:
            bit[i] += v
            i += i & -i

    def prefix(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    for i in range(n):
        add(i + 1, arr[i])

    out = []
    for q in queries:
        if q[0] == 'A':
            add(q[1], q[2])
        else:
            out.append(prefix(q[2]) - prefix(q[1] - 1))
    return out
''',
        reference_java=r'''import java.util.*;
class Solution {
    int n; long[] bit;
    public int[] solution(int[] arr, Object[][] queries) {
        n = arr.length; bit = new long[n + 1];
        for (int i = 0; i < n; i++) add(i + 1, arr[i]);
        List<Integer> out = new ArrayList<>();
        for (Object[] q : queries) {
            if (q[0].equals("A")) add((int)q[1], (int)q[2]);
            else out.add((int) (prefix((int)q[2]) - prefix((int)q[1] - 1)));
        }
        return out.stream().mapToInt(Integer::intValue).toArray();
    }
    void add(int i, long v) { for (; i <= n; i += i & -i) bit[i] += v; }
    long prefix(int i) { long s = 0; for (; i > 0; i -= i & -i) s += bit[i]; return s; }
}
''',
        template_py=(
            "# 펜윅 트리(BIT) : 한 점 가산(A)과 구간합 질의(Q) 처리\n"
            "def solution(arr, queries):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

    # ============================================================ 25
    Problem(
        id="platinum-25",
        rank="Platinum",
        title="뒤집힌 쌍의 개수",
        style="해외대기업",
        topic="펜윅트리",
        type="func",
        func_name="solution",
        description=(
            "정수 배열 arr 가 주어집니다. i < j 이면서 arr[i] > arr[j] 인 쌍 (i, j) 의 개수,\n"
            "즉 역순 쌍(inversion)의 개수를 구해 정수로 반환하세요.\n"
            "값의 범위가 넓을 수 있으므로 좌표 압축 후 펜윅 트리로 세는 것이 효율적입니다."
        ),
        input_desc="arr : 정수 리스트 (중복 값이 있을 수 있음)",
        output_desc="역순 쌍 (i<j 이고 arr[i]>arr[j]) 의 총 개수 (정수)",
        examples=[
            {"args": [[3, 1, 2]], "output": 2},
            {"args": [[4, 3, 2, 1]], "output": 6},
        ],
        hints=[
            "각 원소를 기준으로 '자기 오른쪽에 있으면서 자기보다 작은 값의 개수'를 모두 더하면 됩니다. 이중 반복은 느립니다.",
            "값을 좌표 압축해 순위로 바꾼 뒤 펜윅 트리를 쓰세요. 오른쪽 끝에서 왼쪽으로 훑으며, 지금까지 본 값들 중 현재보다 작은 개수를 prefix 로 구합니다.",
            "오른쪽→왼쪽으로 j 진행. r=rank(arr[j]); inv += prefix(r-1); add(r,1). 압축 순위는 정렬된 고유값의 인덱스+1로 매깁니다.",
        ],
        testcases=[
            {"args": [[3, 1, 2]], "expected": 2},
            {"args": [[1, 2, 3, 4]], "expected": 0},
            {"args": [[4, 3, 2, 1]], "expected": 6},
            {"args": [[2, 2, 2]], "expected": 0},
            {"args": [[5, 1, 4, 2, 3]], "expected": 6},
        ],
        reference_py=r'''def solution(arr):
    n = len(arr)
    uniq = sorted(set(arr))
    rank = {v: i + 1 for i, v in enumerate(uniq)}
    m = len(uniq)
    bit = [0] * (m + 1)

    def add(i, v):
        while i <= m:
            bit[i] += v
            i += i & -i

    def prefix(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    inv = 0
    for j in range(n - 1, -1, -1):
        r = rank[arr[j]]
        inv += prefix(r - 1)
        add(r, 1)
    return inv
''',
        reference_java=r'''import java.util.*;
class Solution {
    int m; int[] bit;
    public long solution(int[] arr) {
        int n = arr.length;
        int[] sorted = arr.clone();
        Arrays.sort(sorted);
        TreeMap<Integer, Integer> rank = new TreeMap<>();
        int r = 0;
        for (int v : sorted) if (!rank.containsKey(v)) rank.put(v, ++r);
        m = r; bit = new int[m + 1];
        long inv = 0;
        for (int j = n - 1; j >= 0; j--) {
            int rk = rank.get(arr[j]);
            inv += prefix(rk - 1);
            add(rk, 1);
        }
        return inv;
    }
    void add(int i, int v) { for (; i <= m; i += i & -i) bit[i] += v; }
    int prefix(int i) { int s = 0; for (; i > 0; i -= i & -i) s += bit[i]; return s; }
}
''',
        template_py=(
            "# 역순 쌍(inversion) 개수 : 좌표 압축 + 펜윅 트리\n"
            "def solution(arr):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    # ============================================================ 26
    Problem(
        id="platinum-26",
        rank="Platinum",
        title="최소 공통 조상 찾기",
        style="백준",
        topic="LCA",
        type="func",
        func_name="solution",
        description=(
            "정점 1을 루트로 하는 트리가 주어집니다. 간선 목록 edges(무방향)와 질의 목록 queries 가 주어질 때,\n"
            "각 질의 [u, v] 에 대해 두 정점 u, v 의 최소 공통 조상(LCA) 번호를 구해 순서대로 리스트로 반환하세요.\n"
            "u == v 이면 그 정점 자신이 답입니다."
        ),
        input_desc="n : 정점 수(1..n), edges : [a,b] 무방향 간선 n-1개, queries : [u,v] 리스트 (루트=1)",
        output_desc="각 질의의 LCA 정점 번호를 순서대로 담은 리스트",
        examples=[
            {"args": [6, [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6]], [[4, 5], [4, 6], [5, 5], [4, 1]]],
             "output": [2, 1, 5, 1]},
            {"args": [4, [[1, 2], [2, 3], [3, 4]], [[4, 2], [3, 1], [4, 4]]],
             "output": [2, 1, 4]},
        ],
        hints=[
            "먼저 루트(1)에서 BFS/DFS로 각 정점의 깊이와 부모를 구하세요. 그다음 두 정점을 같은 깊이로 맞추고 함께 위로 올립니다.",
            "이진 승급(binary lifting)으로 LCA를 구하세요. up[k][v] = v의 2^k번째 조상. 깊이를 맞춘 뒤 두 정점이 갈라지는 지점을 찾습니다.",
            "깊이 차만큼 깊은 쪽을 끌어올려 같은 깊이로 만들고, 같으면 그 정점이 답. 아니면 k를 크게→작게 내리며 up[k][u]!=up[k][v]일 때만 동시에 올린 뒤 up[0][u] 반환.",
        ],
        testcases=[
            {"args": [6, [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6]], [[4, 5], [4, 6], [5, 5], [4, 1]]],
             "expected": [2, 1, 5, 1]},
            {"args": [6, [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6]], [[6, 4], [2, 3], [6, 2]]],
             "expected": [1, 1, 1]},
            {"args": [4, [[1, 2], [2, 3], [3, 4]], [[4, 2], [3, 1], [4, 4]]],
             "expected": [2, 1, 4]},
            {"args": [6, [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6]], [[4, 4], [1, 1], [5, 6]]],
             "expected": [4, 1, 1]},
        ],
        reference_py=r'''def solution(n, edges, queries):
    from collections import deque
    g = [[] for _ in range(n + 1)]
    for a, b in edges:
        g[a].append(b)
        g[b].append(a)
    LOG = 1
    while (1 << LOG) < n:
        LOG += 1
    LOG += 1
    up = [[0] * (n + 1) for _ in range(LOG)]
    depth = [0] * (n + 1)
    visited = [False] * (n + 1)
    dq = deque([1])
    visited[1] = True
    up[0][1] = 0
    while dq:
        u = dq.popleft()
        for v in g[u]:
            if not visited[v]:
                visited[v] = True
                depth[v] = depth[u] + 1
                up[0][v] = u
                dq.append(v)
    for k in range(1, LOG):
        for v in range(1, n + 1):
            up[k][v] = up[k - 1][up[k - 1][v]]

    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        d = depth[u] - depth[v]
        for k in range(LOG):
            if (d >> k) & 1:
                u = up[k][u]
        if u == v:
            return u
        for k in range(LOG - 1, -1, -1):
            if up[k][u] != up[k][v]:
                u = up[k][u]
                v = up[k][v]
        return up[0][u]

    return [lca(u, v) for u, v in queries]
''',
        reference_java=r'''import java.util.*;
class Solution {
    public int[] solution(int n, int[][] edges, int[][] queries) {
        List<Integer>[] g = new List[n + 1];
        for (int i = 1; i <= n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) { g[e[0]].add(e[1]); g[e[1]].add(e[0]); }
        int LOG = 1;
        while ((1 << LOG) < n) LOG++;
        LOG++;
        int[][] up = new int[LOG][n + 1];
        int[] depth = new int[n + 1];
        boolean[] vis = new boolean[n + 1];
        ArrayDeque<Integer> dq = new ArrayDeque<>();
        dq.add(1); vis[1] = true;
        while (!dq.isEmpty()) {
            int u = dq.poll();
            for (int v : g[u]) if (!vis[v]) { vis[v] = true; depth[v] = depth[u] + 1; up[0][v] = u; dq.add(v); }
        }
        for (int k = 1; k < LOG; k++)
            for (int v = 1; v <= n; v++) up[k][v] = up[k-1][up[k-1][v]];
        int[] res = new int[queries.length];
        for (int i = 0; i < queries.length; i++) res[i] = lca(queries[i][0], queries[i][1], up, depth, LOG);
        return res;
    }
    int lca(int u, int v, int[][] up, int[] depth, int LOG) {
        if (depth[u] < depth[v]) { int t = u; u = v; v = t; }
        int d = depth[u] - depth[v];
        for (int k = 0; k < LOG; k++) if (((d >> k) & 1) == 1) u = up[k][u];
        if (u == v) return u;
        for (int k = LOG - 1; k >= 0; k--) if (up[k][u] != up[k][v]) { u = up[k][u]; v = up[k][v]; }
        return up[0][u];
    }
}
''',
        template_py=(
            "# 최소 공통 조상(LCA) : 루트=1, 각 질의 [u,v]의 LCA 리스트 반환\n"
            "def solution(n, edges, queries):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

    # ============================================================ 27
    Problem(
        id="platinum-27",
        rank="Platinum",
        title="트리 위 두 정점의 거리",
        style="대기업",
        topic="LCA",
        type="func",
        func_name="solution",
        description=(
            "정점 1을 루트로 하는 트리에서, 각 질의 [u, v] 에 대해 두 정점 사이 경로의 간선 수(거리)를 구하세요.\n"
            "거리 = depth[u] + depth[v] - 2 * depth[lca(u,v)] 로 계산할 수 있습니다.\n"
            "모든 질의의 답을 순서대로 리스트로 반환하세요."
        ),
        input_desc="n : 정점 수(1..n), edges : [a,b] 무방향 간선 n-1개, queries : [u,v] 리스트 (루트=1)",
        output_desc="각 질의의 두 정점 사이 거리(간선 수)를 순서대로 담은 리스트",
        examples=[
            {"args": [6, [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6]], [[4, 5], [4, 6], [5, 5], [4, 1]]],
             "output": [2, 4, 0, 2]},
            {"args": [4, [[1, 2], [2, 3], [3, 4]], [[4, 1], [4, 2]]],
             "output": [3, 2]},
        ],
        hints=[
            "두 정점 사이 경로는 항상 LCA를 지납니다. 따라서 거리는 두 깊이의 합에서 LCA 깊이를 두 번 뺀 값입니다.",
            "이진 승급으로 LCA를 구하고 깊이 배열을 함께 만들면 됩니다. 거리는 depth[u]+depth[v]-2*depth[lca].",
            "BFS로 depth, up[0] 채우고 up[k]=up[k-1][up[k-1]] 전처리. lca(u,v) 구한 뒤 공식으로 거리 계산해 리스트에 담습니다.",
        ],
        testcases=[
            {"args": [6, [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6]], [[4, 5], [4, 6], [5, 5], [4, 1]]],
             "expected": [2, 4, 0, 2]},
            {"args": [6, [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6]], [[6, 4], [6, 1]]],
             "expected": [4, 2]},
            {"args": [4, [[1, 2], [2, 3], [3, 4]], [[4, 1], [4, 2]]],
             "expected": [3, 2]},
            {"args": [6, [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6]], [[4, 4], [5, 6]]],
             "expected": [0, 4]},
        ],
        reference_py=r'''def solution(n, edges, queries):
    from collections import deque
    g = [[] for _ in range(n + 1)]
    for a, b in edges:
        g[a].append(b)
        g[b].append(a)
    LOG = 1
    while (1 << LOG) < n:
        LOG += 1
    LOG += 1
    up = [[0] * (n + 1) for _ in range(LOG)]
    depth = [0] * (n + 1)
    visited = [False] * (n + 1)
    dq = deque([1])
    visited[1] = True
    while dq:
        u = dq.popleft()
        for v in g[u]:
            if not visited[v]:
                visited[v] = True
                depth[v] = depth[u] + 1
                up[0][v] = u
                dq.append(v)
    for k in range(1, LOG):
        for v in range(1, n + 1):
            up[k][v] = up[k - 1][up[k - 1][v]]

    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        d = depth[u] - depth[v]
        for k in range(LOG):
            if (d >> k) & 1:
                u = up[k][u]
        if u == v:
            return u
        for k in range(LOG - 1, -1, -1):
            if up[k][u] != up[k][v]:
                u = up[k][u]
                v = up[k][v]
        return up[0][u]

    return [depth[u] + depth[v] - 2 * depth[lca(u, v)] for u, v in queries]
''',
        reference_java=r'''import java.util.*;
class Solution {
    public int[] solution(int n, int[][] edges, int[][] queries) {
        List<Integer>[] g = new List[n + 1];
        for (int i = 1; i <= n; i++) g[i] = new ArrayList<>();
        for (int[] e : edges) { g[e[0]].add(e[1]); g[e[1]].add(e[0]); }
        int LOG = 1;
        while ((1 << LOG) < n) LOG++;
        LOG++;
        int[][] up = new int[LOG][n + 1];
        int[] depth = new int[n + 1];
        boolean[] vis = new boolean[n + 1];
        ArrayDeque<Integer> dq = new ArrayDeque<>();
        dq.add(1); vis[1] = true;
        while (!dq.isEmpty()) {
            int u = dq.poll();
            for (int v : g[u]) if (!vis[v]) { vis[v] = true; depth[v] = depth[u] + 1; up[0][v] = u; dq.add(v); }
        }
        for (int k = 1; k < LOG; k++)
            for (int v = 1; v <= n; v++) up[k][v] = up[k-1][up[k-1][v]];
        int[] res = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int u = queries[i][0], v = queries[i][1];
            res[i] = depth[u] + depth[v] - 2 * depth[lca(u, v, up, depth, LOG)];
        }
        return res;
    }
    int lca(int u, int v, int[][] up, int[] depth, int LOG) {
        if (depth[u] < depth[v]) { int t = u; u = v; v = t; }
        int d = depth[u] - depth[v];
        for (int k = 0; k < LOG; k++) if (((d >> k) & 1) == 1) u = up[k][u];
        if (u == v) return u;
        for (int k = LOG - 1; k >= 0; k--) if (up[k][u] != up[k][v]) { u = up[k][u]; v = up[k][v]; }
        return up[0][u];
    }
}
''',
        template_py=(
            "# 트리 두 정점 거리 : LCA로 depth[u]+depth[v]-2*depth[lca] 계산\n"
            "def solution(n, edges, queries):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

    # ============================================================ 28
    Problem(
        id="platinum-28",
        rank="Platinum",
        title="동적 K번째 작은 수",
        style="해외대기업",
        topic="세그먼트트리",
        type="func",
        func_name="solution",
        description=(
            "1부터 m 까지의 값을 담는 다중집합(중복 허용)이 처음엔 비어 있습니다. 질의 목록 queries 가 주어집니다.\n"
            "  - ['+', x] : 값 x 를 하나 넣습니다.\n"
            "  - ['-', x] : 값 x 를 하나 뺍니다(반드시 존재함).\n"
            "  - ['K', k] : 현재 다중집합에서 k번째로 작은 값을 답합니다(반드시 존재함).\n"
            "모든 'K' 질의의 답을 순서대로 리스트로 반환하세요."
        ),
        input_desc="m : 값의 최댓값(1..m), queries : ['+',x] / ['-',x] / ['K',k] 의 리스트",
        output_desc="'K' 질의들의 답(현재 k번째 작은 값)을 순서대로 담은 리스트",
        examples=[
            {"args": [5, [["+", 3], ["+", 1], ["+", 4], ["K", 1], ["K", 2], ["-", 1], ["K", 1]]],
             "output": [1, 3, 3]},
            {"args": [3, [["+", 2], ["+", 2], ["K", 1], ["K", 2]]],
             "output": [2, 2]},
        ],
        hints=[
            "값마다 등장 횟수(빈도)를 세그먼트 트리에 저장하면, 'k번째 작은 값'은 누적 빈도가 처음으로 k 이상이 되는 값입니다.",
            "빈도 세그먼트 트리에서 루트부터 내려가며 이분 탐색하세요. 왼쪽 자식의 합이 k 이상이면 왼쪽, 아니면 k에서 왼쪽 합을 빼고 오른쪽으로 갑니다.",
            "'+'/'-'는 해당 리프에 +1/-1 갱신. kth(k): p=1; while p<size: if tree[2p]>=k: p=2p else k-=tree[2p]; p=2p+1. 답은 p-size+1.",
        ],
        testcases=[
            {"args": [5, [["+", 3], ["+", 1], ["+", 4], ["K", 1], ["K", 2], ["-", 1], ["K", 1]]],
             "expected": [1, 3, 3]},
            {"args": [3, [["+", 2], ["+", 2], ["K", 1], ["K", 2]]],
             "expected": [2, 2]},
            {"args": [10, [["+", 5], ["+", 5], ["+", 7], ["K", 2], ["K", 3], ["-", 5], ["K", 2]]],
             "expected": [5, 7, 7]},
            {"args": [5, [["+", 1], ["+", 2], ["+", 3], ["K", 1], ["K", 3], ["-", 2], ["K", 2]]],
             "expected": [1, 3, 3]},
        ],
        reference_py=r'''def solution(m, queries):
    size = 1
    while size < m:
        size *= 2
    tree = [0] * (2 * size)

    def update(idx, delta):
        p = size + idx
        tree[p] += delta
        p //= 2
        while p:
            tree[p] = tree[2 * p] + tree[2 * p + 1]
            p //= 2

    def kth(k):
        p = 1
        while p < size:
            if tree[2 * p] >= k:
                p = 2 * p
            else:
                k -= tree[2 * p]
                p = 2 * p + 1
        return p - size + 1

    out = []
    for q in queries:
        if q[0] == '+':
            update(q[1] - 1, 1)
        elif q[0] == '-':
            update(q[1] - 1, -1)
        else:
            out.append(kth(q[1]))
    return out
''',
        reference_java=r'''import java.util.*;
class Solution {
    int size; int[] tree;
    public int[] solution(int m, Object[][] queries) {
        size = 1;
        while (size < m) size *= 2;
        tree = new int[2 * size];
        List<Integer> out = new ArrayList<>();
        for (Object[] q : queries) {
            String op = (String) q[0];
            if (op.equals("+")) update((int)q[1] - 1, 1);
            else if (op.equals("-")) update((int)q[1] - 1, -1);
            else out.add(kth((int)q[1]));
        }
        return out.stream().mapToInt(Integer::intValue).toArray();
    }
    void update(int idx, int delta) {
        int p = size + idx; tree[p] += delta; p /= 2;
        while (p >= 1) { tree[p] = tree[2*p] + tree[2*p+1]; p /= 2; }
    }
    int kth(int k) {
        int p = 1;
        while (p < size) {
            if (tree[2*p] >= k) p = 2*p;
            else { k -= tree[2*p]; p = 2*p+1; }
        }
        return p - size + 1;
    }
}
''',
        template_py=(
            "# 동적 K번째 작은 수 : 빈도 세그먼트 트리 + 트리 위 이분 탐색\n"
            "def solution(m, queries):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

    # ============================================================ 29
    Problem(
        id="platinum-29",
        rank="Platinum",
        title="값 범위 안의 점 세기",
        style="백준",
        topic="좌표압축",
        type="func",
        func_name="solution",
        description=(
            "수직선 위에 점들을 하나씩 추가하면서, 특정 값 구간 안에 들어 있는 점의 개수를 묻습니다. 질의는 두 종류입니다.\n"
            "  - ['I', x] : 값 x 인 점을 하나 추가합니다(같은 값이 여러 번 추가될 수 있음).\n"
            "  - ['C', l, r] : 현재까지 추가된 점들 중 값이 l 이상 r 이하인 점의 개수를 답합니다.\n"
            "값 x 는 매우 클 수 있으므로 좌표 압축이 필요합니다. 모든 'C' 질의의 답을 순서대로 리스트로 반환하세요."
        ),
        input_desc="queries : ['I',x] / ['C',l,r] 의 리스트 (x, l, r 은 큰 정수일 수 있음)",
        output_desc="'C' 질의들의 답(구간 [l,r] 안의 점 개수)을 순서대로 담은 리스트",
        examples=[
            {"args": [[["I", 5], ["I", 100], ["I", 50], ["C", 1, 60], ["I", 3], ["C", 1, 4], ["C", 50, 100]]],
             "output": [2, 1, 2]},
            {"args": [[["I", 10], ["C", 1, 5], ["I", 2], ["C", 1, 5], ["C", 2, 2]]],
             "output": [0, 1, 1]},
        ],
        hints=[
            "값이 매우 커서 배열 인덱스로 바로 쓸 수 없습니다. 등장하는 값들을 작은 정수 순위로 바꾸는 전처리가 필요합니다.",
            "삽입될 모든 값(I 의 x)을 미리 모아 좌표 압축한 뒤, 그 순위 위에서 개수 세그먼트 트리를 운용하세요.",
            "압축 좌표 정렬배열에서 l은 bisect_left, r은 bisect_right-1 로 순위 구간을 구하고 세그트리 구간합으로 개수를 답합니다. 'I' 는 해당 순위 리프에 +1.",
        ],
        testcases=[
            {"args": [[["I", 5], ["I", 100], ["I", 50], ["C", 1, 60], ["I", 3], ["C", 1, 4], ["C", 50, 100]]],
             "expected": [2, 1, 2]},
            {"args": [[["I", 10], ["C", 1, 5], ["I", 2], ["C", 1, 5], ["C", 2, 2]]],
             "expected": [0, 1, 1]},
            {"args": [[["I", 1000000000], ["I", 1], ["C", 1, 1000000000], ["C", 2, 999999999]]],
             "expected": [2, 0]},
            {"args": [[["I", 7], ["I", 7], ["C", 7, 7], ["C", 1, 6]]],
             "expected": [2, 0]},
        ],
        reference_py=r'''def solution(queries):
    from bisect import bisect_left, bisect_right
    coords = sorted(set(q[1] for q in queries if q[0] == 'I'))
    pos = {v: i for i, v in enumerate(coords)}
    m = len(coords)
    size = 1
    while size < max(m, 1):
        size *= 2
    tree = [0] * (2 * size)

    def update(i):
        p = size + i
        tree[p] += 1
        p //= 2
        while p:
            tree[p] = tree[2 * p] + tree[2 * p + 1]
            p //= 2

    def query(l, r):
        if l > r:
            return 0
        res = 0
        l += size
        r += size + 1
        while l < r:
            if l & 1:
                res += tree[l]; l += 1
            if r & 1:
                r -= 1; res += tree[r]
            l //= 2; r //= 2
        return res

    out = []
    for q in queries:
        if q[0] == 'I':
            update(pos[q[1]])
        else:
            lo = bisect_left(coords, q[1])
            hi = bisect_right(coords, q[2]) - 1
            out.append(query(lo, hi))
    return out
''',
        reference_java=r'''import java.util.*;
class Solution {
    int size; int[] tree;
    public int[] solution(Object[][] queries) {
        TreeSet<Integer> set = new TreeSet<>();
        for (Object[] q : queries) if (q[0].equals("I")) set.add((int)q[1]);
        List<Integer> coords = new ArrayList<>(set);
        int m = coords.size();
        size = 1;
        while (size < Math.max(m, 1)) size *= 2;
        tree = new int[2 * size];
        List<Integer> out = new ArrayList<>();
        for (Object[] q : queries) {
            if (q[0].equals("I")) {
                int idx = Collections.binarySearch(coords, (int)q[1]);
                update(idx);
            } else {
                int lo = lowerBound(coords, (int)q[1]);
                int hi = upperBound(coords, (int)q[2]) - 1;
                out.add(query(lo, hi));
            }
        }
        return out.stream().mapToInt(Integer::intValue).toArray();
    }
    int lowerBound(List<Integer> a, int x) {
        int lo = 0, hi = a.size();
        while (lo < hi) { int mid = (lo + hi) / 2; if (a.get(mid) < x) lo = mid + 1; else hi = mid; }
        return lo;
    }
    int upperBound(List<Integer> a, int x) {
        int lo = 0, hi = a.size();
        while (lo < hi) { int mid = (lo + hi) / 2; if (a.get(mid) <= x) lo = mid + 1; else hi = mid; }
        return lo;
    }
    void update(int i) {
        int p = size + i; tree[p] += 1; p /= 2;
        while (p >= 1) { tree[p] = tree[2*p] + tree[2*p+1]; p /= 2; }
    }
    int query(int l, int r) {
        if (l > r) return 0;
        int res = 0; l += size; r += size + 1;
        while (l < r) {
            if ((l & 1) == 1) res += tree[l++];
            if ((r & 1) == 1) res += tree[--r];
            l /= 2; r /= 2;
        }
        return res;
    }
}
''',
        template_py=(
            "# 좌표 압축 + 세그먼트 트리 : 점 추가(I)와 값 구간 개수 질의(C)\n"
            "def solution(queries):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

    # ============================================================ 30
    Problem(
        id="platinum-30",
        rank="Platinum",
        title="최솟값 구간 질의 (입출력형)",
        style="백준",
        topic="세그먼트트리",
        type="stdin",
        description=(
            "길이 N 의 정수 배열에 대해 M 개의 연산을 수행한다. 연산은 두 종류다.\n"
            "  - '1 i x' : i번째(1-based) 원소를 x 로 바꾼다.\n"
            "  - '2 l r' : l번째부터 r번째까지의 구간 최솟값을 출력한다.\n"
            "갱신과 질의가 섞여 들어오므로 세그먼트 트리로 처리한다."
        ),
        input_desc=(
            "첫째 줄에 N M. 둘째 줄에 N개의 정수. 다음 M개의 줄에 '1 i x' 또는 '2 l r' 형식의 연산."
        ),
        output_desc="'2 l r' 연산마다 구간 최솟값을 한 줄에 하나씩 출력.",
        examples=[
            {"input": "6 4\n5 3 8 1 9 2\n2 1 3\n1 4 7\n2 3 5\n2 1 6\n",
             "output": "3\n7\n2\n"},
            {"input": "4 3\n4 4 4 4\n2 1 4\n1 2 1\n2 1 2\n",
             "output": "4\n1\n"},
        ],
        hints=[
            "갱신이 끼어들어 매번 구간을 다시 훑으면 느립니다. 갱신·질의를 모두 O(log N)에 처리할 구조가 필요합니다.",
            "구간 최솟값 세그먼트 트리를 만들고, 입력을 빠르게 읽어 연산 종류에 따라 update/query 를 호출하세요.",
            "리프에 배열을 깔고 부모를 min으로 채움. update: 리프 변경 후 부모로 올라가며 min 갱신. query(l,r): 반복 세그트리. 결과는 모아서 한 번에 출력.",
        ],
        testcases=[
            {"input": "6 4\n5 3 8 1 9 2\n2 1 3\n1 4 7\n2 3 5\n2 1 6\n",
             "output": "3\n7\n2\n"},
            {"input": "1 2\n10\n2 1 1\n1 1 3\n",
             "output": "10\n"},
            {"input": "4 3\n4 4 4 4\n2 1 4\n1 2 1\n2 1 2\n",
             "output": "4\n1\n"},
            {"input": "5 2\n2 2 2 2 2\n2 2 4\n2 1 5\n",
             "output": "2\n2\n"},
        ],
        reference_py=r'''import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    arr = [int(data[idx + i]) for i in range(n)]
    idx += n
    size = 1
    while size < n:
        size *= 2
    INF = float('inf')
    tree = [INF] * (2 * size)
    for i in range(n):
        tree[size + i] = arr[i]
    for p in range(size - 1, 0, -1):
        tree[p] = min(tree[2 * p], tree[2 * p + 1])
    out = []
    for _ in range(m):
        t = int(data[idx]); idx += 1
        if t == 1:
            i = int(data[idx]); x = int(data[idx + 1]); idx += 2
            p = size + i - 1
            tree[p] = x
            p //= 2
            while p:
                tree[p] = min(tree[2 * p], tree[2 * p + 1])
                p //= 2
        else:
            l = int(data[idx]); r = int(data[idx + 1]); idx += 2
            res = INF
            l = l - 1 + size
            r = r + size
            while l < r:
                if l & 1:
                    res = min(res, tree[l]); l += 1
                if r & 1:
                    r -= 1; res = min(res, tree[r])
                l //= 2; r //= 2
            out.append(str(res))
    print('\n'.join(out))


main()
''',
        reference_java=r'''import java.util.*;
import java.io.*;
public class Main {
    static int size; static long[] tree;
    public static void main(String[] args) throws IOException {
        DataInputStream in = new DataInputStream(new BufferedInputStream(System.in));
        int n = nextInt(in), m = nextInt(in);
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = nextInt(in);
        size = 1;
        while (size < n) size *= 2;
        tree = new long[2 * size];
        Arrays.fill(tree, Long.MAX_VALUE);
        for (int i = 0; i < n; i++) tree[size + i] = arr[i];
        for (int p = size - 1; p >= 1; p--) tree[p] = Math.min(tree[2*p], tree[2*p+1]);
        StringBuilder sb = new StringBuilder();
        for (int q = 0; q < m; q++) {
            int t = nextInt(in);
            if (t == 1) {
                int i = nextInt(in), x = nextInt(in);
                int p = size + i - 1; tree[p] = x; p /= 2;
                while (p >= 1) { tree[p] = Math.min(tree[2*p], tree[2*p+1]); p /= 2; }
            } else {
                int l = nextInt(in), r = nextInt(in);
                long res = Long.MAX_VALUE; l = l - 1 + size; r = r + size;
                while (l < r) {
                    if ((l & 1) == 1) res = Math.min(res, tree[l++]);
                    if ((r & 1) == 1) res = Math.min(res, tree[--r]);
                    l /= 2; r /= 2;
                }
                sb.append(res).append('\n');
            }
        }
        System.out.print(sb);
    }
    static int nextInt(DataInputStream in) throws IOException {
        int ret = 0, b; boolean neg = false;
        do { b = in.read(); } while (b < '0' && b != '-');
        if (b == '-') { neg = true; b = in.read(); }
        while (b >= '0') { ret = ret * 10 + b - '0'; b = in.read(); }
        return neg ? -ret : ret;
    }
}
''',
        template_py=(
            "import sys\n"
            "# 구간 최솟값 세그먼트 트리 (갱신 '1', 질의 '2')\n"
            "data = sys.stdin.buffer.read().split()\n"
            "# ...\n"
        ),
    ),

    # ============================================================ 31
    Problem(
        id="platinum-31",
        rank="Platinum",
        title="펜윅 트리 구간합 (입출력형)",
        style="백준",
        topic="펜윅트리",
        type="stdin",
        description=(
            "길이 N 의 정수 배열에 대해 M 개의 연산을 수행한다.\n"
            "  - '1 i x' : i번째(1-based) 원소를 x 로 바꾼다(대입).\n"
            "  - '2 l r' : l번째부터 r번째까지의 구간 합을 출력한다.\n"
            "펜윅 트리(BIT)로 처리한다. 대입은 (새값 - 기존값) 만큼 가산해 반영한다."
        ),
        input_desc=(
            "첫째 줄에 N M. 둘째 줄에 N개의 정수. 다음 M개의 줄에 '1 i x' 또는 '2 l r' 형식의 연산."
        ),
        output_desc="'2 l r' 연산마다 구간 합을 한 줄에 하나씩 출력.",
        examples=[
            {"input": "5 4\n1 2 3 4 5\n2 1 3\n1 2 10\n2 1 3\n2 4 5\n",
             "output": "6\n14\n9\n"},
            {"input": "3 3\n5 5 5\n2 1 3\n1 1 0\n2 1 1\n",
             "output": "15\n0\n"},
        ],
        hints=[
            "한 점 대입과 임의 구간 합이 섞입니다. 대입은 차이값만큼 더하는 것으로 바꿔 생각하세요.",
            "펜윅 트리(BIT)를 쓰세요. 현재값 배열을 따로 들고, '1 i x' 는 add(i, x-현재값) 후 현재값 갱신.",
            "구간합 [l,r] = prefix(r) - prefix(l-1). add(i,v): i += i&-i. prefix(i): i -= i&-i. 결과는 모아서 출력.",
        ],
        testcases=[
            {"input": "5 4\n1 2 3 4 5\n2 1 3\n1 2 10\n2 1 3\n2 4 5\n",
             "output": "6\n14\n9\n"},
            {"input": "3 3\n5 5 5\n2 1 3\n1 1 0\n2 1 1\n",
             "output": "15\n0\n"},
            {"input": "1 2\n10\n2 1 1\n1 1 7\n",
             "output": "10\n"},
            {"input": "4 3\n1 1 1 1\n1 1 5\n2 1 4\n2 2 3\n",
             "output": "8\n2\n"},
        ],
        reference_py=r'''import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    arr = [int(data[idx + i]) for i in range(n)]
    idx += n
    bit = [0] * (n + 1)
    cur = [0] * (n + 1)

    def add(i, v):
        while i <= n:
            bit[i] += v
            i += i & -i

    def prefix(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    for i in range(n):
        cur[i + 1] = arr[i]
        add(i + 1, arr[i])
    out = []
    for _ in range(m):
        t = int(data[idx]); idx += 1
        if t == 1:
            i = int(data[idx]); x = int(data[idx + 1]); idx += 2
            add(i, x - cur[i])
            cur[i] = x
        else:
            l = int(data[idx]); r = int(data[idx + 1]); idx += 2
            out.append(str(prefix(r) - prefix(l - 1)))
    print('\n'.join(out))


main()
''',
        reference_java=r'''import java.util.*;
import java.io.*;
public class Main {
    static int n; static long[] bit;
    public static void main(String[] args) throws IOException {
        DataInputStream in = new DataInputStream(new BufferedInputStream(System.in));
        n = nextInt(in); int m = nextInt(in);
        long[] cur = new long[n + 1];
        bit = new long[n + 1];
        for (int i = 1; i <= n; i++) { cur[i] = nextInt(in); add(i, cur[i]); }
        StringBuilder sb = new StringBuilder();
        for (int q = 0; q < m; q++) {
            int t = nextInt(in);
            if (t == 1) {
                int i = nextInt(in); long x = nextInt(in);
                add(i, x - cur[i]); cur[i] = x;
            } else {
                int l = nextInt(in), r = nextInt(in);
                sb.append(prefix(r) - prefix(l - 1)).append('\n');
            }
        }
        System.out.print(sb);
    }
    static void add(int i, long v) { for (; i <= n; i += i & -i) bit[i] += v; }
    static long prefix(int i) { long s = 0; for (; i > 0; i -= i & -i) s += bit[i]; return s; }
    static int nextInt(DataInputStream in) throws IOException {
        int ret = 0, b; boolean neg = false;
        do { b = in.read(); } while (b < '0' && b != '-');
        if (b == '-') { neg = true; b = in.read(); }
        while (b >= '0') { ret = ret * 10 + b - '0'; b = in.read(); }
        return neg ? -ret : ret;
    }
}
''',
        template_py=(
            "import sys\n"
            "# 펜윅 트리(BIT) : 대입 '1', 구간합 질의 '2'\n"
            "data = sys.stdin.buffer.read().split()\n"
            "# ...\n"
        ),
    ),

    # ============================================================ 32
    Problem(
        id="platinum-32",
        rank="Platinum",
        title="공통 조상 (입출력형)",
        style="백준",
        topic="LCA",
        type="stdin",
        description=(
            "정점 1을 루트로 하는 트리가 주어진다. 여러 쌍의 정점에 대해 최소 공통 조상(LCA)을 구한다."
        ),
        input_desc=(
            "첫째 줄에 정점 수 N. 다음 N-1개의 줄에 트리의 간선 'a b'(무방향). "
            "그다음 줄에 질의 수 M. 다음 M개의 줄에 'u v'. 루트는 1이다."
        ),
        output_desc="각 질의 'u v' 의 LCA 정점 번호를 한 줄에 하나씩 출력.",
        examples=[
            {"input": "6\n1 2\n1 3\n2 4\n2 5\n3 6\n4\n4 5\n4 6\n5 5\n4 1\n",
             "output": "2\n1\n5\n1\n"},
            {"input": "4\n1 2\n2 3\n3 4\n3\n4 2\n3 1\n4 4\n",
             "output": "2\n1\n4\n"},
        ],
        hints=[
            "루트(1)에서 BFS/DFS로 각 정점의 깊이와 부모를 먼저 구하세요. 그다음 두 정점을 같은 깊이로 맞춰 함께 올립니다.",
            "이진 승급(binary lifting) 테이블 up[k][v] 를 전처리해 LCA를 O(log N)에 구하세요.",
            "깊이 차만큼 깊은 쪽을 끌어올려 같은 깊이로, 같으면 답. 아니면 k를 크게→작게 내리며 up[k][u]!=up[k][v]일 때만 함께 올린 뒤 부모 출력.",
        ],
        testcases=[
            {"input": "6\n1 2\n1 3\n2 4\n2 5\n3 6\n4\n4 5\n4 6\n5 5\n4 1\n",
             "output": "2\n1\n5\n1\n"},
            {"input": "4\n1 2\n2 3\n3 4\n3\n4 2\n3 1\n4 4\n",
             "output": "2\n1\n4\n"},
            {"input": "2\n1 2\n1\n2 1\n",
             "output": "1\n"},
            {"input": "5\n1 2\n1 3\n1 4\n1 5\n2\n2 3\n4 5\n",
             "output": "1\n1\n"},
        ],
        reference_py=r'''import sys
from collections import deque


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a = int(data[idx]); b = int(data[idx + 1]); idx += 2
        g[a].append(b)
        g[b].append(a)
    LOG = 1
    while (1 << LOG) < n:
        LOG += 1
    LOG += 1
    up = [[0] * (n + 1) for _ in range(LOG)]
    depth = [0] * (n + 1)
    visited = [False] * (n + 1)
    dq = deque([1])
    visited[1] = True
    while dq:
        u = dq.popleft()
        for v in g[u]:
            if not visited[v]:
                visited[v] = True
                depth[v] = depth[u] + 1
                up[0][v] = u
                dq.append(v)
    for k in range(1, LOG):
        row = up[k]
        prev = up[k - 1]
        for v in range(1, n + 1):
            row[v] = prev[prev[v]]

    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        d = depth[u] - depth[v]
        for k in range(LOG):
            if (d >> k) & 1:
                u = up[k][u]
        if u == v:
            return u
        for k in range(LOG - 1, -1, -1):
            if up[k][u] != up[k][v]:
                u = up[k][u]
                v = up[k][v]
        return up[0][u]

    m = int(data[idx]); idx += 1
    out = []
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); idx += 2
        out.append(str(lca(u, v)))
    print('\n'.join(out))


main()
''',
        reference_java=r'''import java.util.*;
import java.io.*;
public class Main {
    static int LOG; static int[][] up; static int[] depth;
    public static void main(String[] args) throws IOException {
        DataInputStream in = new DataInputStream(new BufferedInputStream(System.in));
        int n = nextInt(in);
        List<Integer>[] g = new List[n + 1];
        for (int i = 1; i <= n; i++) g[i] = new ArrayList<>();
        for (int i = 0; i < n - 1; i++) { int a = nextInt(in), b = nextInt(in); g[a].add(b); g[b].add(a); }
        LOG = 1;
        while ((1 << LOG) < n) LOG++;
        LOG++;
        up = new int[LOG][n + 1];
        depth = new int[n + 1];
        boolean[] vis = new boolean[n + 1];
        ArrayDeque<Integer> dq = new ArrayDeque<>();
        dq.add(1); vis[1] = true;
        while (!dq.isEmpty()) {
            int u = dq.poll();
            for (int v : g[u]) if (!vis[v]) { vis[v] = true; depth[v] = depth[u] + 1; up[0][v] = u; dq.add(v); }
        }
        for (int k = 1; k < LOG; k++)
            for (int v = 1; v <= n; v++) up[k][v] = up[k-1][up[k-1][v]];
        int m = nextInt(in);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < m; i++) { int u = nextInt(in), v = nextInt(in); sb.append(lca(u, v)).append('\n'); }
        System.out.print(sb);
    }
    static int lca(int u, int v) {
        if (depth[u] < depth[v]) { int t = u; u = v; v = t; }
        int d = depth[u] - depth[v];
        for (int k = 0; k < LOG; k++) if (((d >> k) & 1) == 1) u = up[k][u];
        if (u == v) return u;
        for (int k = LOG - 1; k >= 0; k--) if (up[k][u] != up[k][v]) { u = up[k][u]; v = up[k][v]; }
        return up[0][u];
    }
    static int nextInt(DataInputStream in) throws IOException {
        int ret = 0, b; boolean neg = false;
        do { b = in.read(); } while (b < '0' && b != '-');
        if (b == '-') { neg = true; b = in.read(); }
        while (b >= '0') { ret = ret * 10 + b - '0'; b = in.read(); }
        return neg ? -ret : ret;
    }
}
''',
        template_py=(
            "import sys\n"
            "from collections import deque\n"
            "# LCA (binary lifting), 루트=1\n"
            "data = sys.stdin.buffer.read().split()\n"
            "# ...\n"
        ),
    ),

    # ============================================================ 33
    Problem(
        id="platinum-33",
        rank="Platinum",
        title="왼쪽의 더 큰 수 세기",
        style="대기업",
        topic="좌표압축",
        type="func",
        func_name="solution",
        description=(
            "정수 배열 arr 가 주어집니다. 각 위치 i 에 대해, 자신보다 왼쪽(인덱스가 작은 쪽)에 있으면서\n"
            "값이 자기보다 큰(arr[j] > arr[i], j < i) 원소의 개수를 구해 같은 길이의 리스트로 반환하세요.\n"
            "값의 범위가 넓을 수 있으므로 좌표 압축 후 펜윅 트리로 세는 것이 효율적입니다."
        ),
        input_desc="arr : 정수 리스트 (중복 값이 있을 수 있음)",
        output_desc="각 위치 i 에 대해 '왼쪽에 있으면서 더 큰 값'의 개수를 담은 리스트",
        examples=[
            {"args": [[3, 1, 2]], "output": [0, 1, 1]},
            {"args": [[5, 1, 4, 2, 3]], "output": [0, 1, 1, 2, 2]},
        ],
        hints=[
            "왼쪽에서 오른쪽으로 진행하며, 지금까지 본 값 중 현재보다 큰 것이 몇 개인지를 매번 빠르게 알아야 합니다.",
            "값을 좌표 압축해 순위로 바꾸고 펜윅 트리에 등장 개수를 누적하세요. '현재보다 큰 개수 = 지금까지 넣은 총 개수 - (현재 순위 이하 개수)'.",
            "왼쪽→오른쪽으로 i 진행. r=rank(arr[i]); ans[i] = cnt - prefix(r); 그 뒤 add(r,1); cnt+=1. 압축 순위는 정렬된 고유값 인덱스+1.",
        ],
        testcases=[
            {"args": [[3, 1, 2]], "expected": [0, 1, 1]},
            {"args": [[1, 2, 3, 4]], "expected": [0, 0, 0, 0]},
            {"args": [[4, 3, 2, 1]], "expected": [0, 1, 2, 3]},
            {"args": [[2, 2, 2]], "expected": [0, 0, 0]},
            {"args": [[5, 1, 4, 2, 3]], "expected": [0, 1, 1, 2, 2]},
        ],
        reference_py=r'''def solution(arr):
    uniq = sorted(set(arr))
    rank = {v: i + 1 for i, v in enumerate(uniq)}
    m = len(uniq)
    bit = [0] * (m + 1)

    def add(i, v):
        while i <= m:
            bit[i] += v
            i += i & -i

    def prefix(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    out = []
    cnt = 0
    for x in arr:
        r = rank[x]
        out.append(cnt - prefix(r))
        add(r, 1)
        cnt += 1
    return out
''',
        reference_java=r'''import java.util.*;
class Solution {
    int m; int[] bit;
    public int[] solution(int[] arr) {
        int n = arr.length;
        int[] sorted = arr.clone();
        Arrays.sort(sorted);
        TreeMap<Integer, Integer> rank = new TreeMap<>();
        int r = 0;
        for (int v : sorted) if (!rank.containsKey(v)) rank.put(v, ++r);
        m = r; bit = new int[m + 1];
        int[] out = new int[n];
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            int rk = rank.get(arr[i]);
            out[i] = cnt - prefix(rk);
            add(rk, 1); cnt++;
        }
        return out;
    }
    void add(int i, int v) { for (; i <= m; i += i & -i) bit[i] += v; }
    int prefix(int i) { int s = 0; for (; i > 0; i -= i & -i) s += bit[i]; return s; }
}
''',
        template_py=(
            "# 왼쪽의 더 큰 수 세기 : 좌표 압축 + 펜윅 트리\n"
            "def solution(arr):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

    # ============================================================ 34
    Problem(
        id="platinum-34",
        rank="Platinum",
        title="누적합 임계 위치 찾기",
        style="해외대기업",
        topic="세그먼트트리",
        type="func",
        func_name="solution",
        description=(
            "음이 아닌 정수 배열 arr 와 질의 목록 queries 가 주어집니다.\n"
            "  - ['U', i, x] : arr 의 i번째(1-based) 값을 x 로 바꿉니다.\n"
            "  - ['F', v] : 앞에서부터의 누적합(arr[1]+...+arr[i])이 처음으로 v 이상이 되는 가장 작은 1-based 인덱스 i 를 답합니다. "
            "전체 합이 v 미만이면 -1 을 답합니다.\n"
            "모든 'F' 질의의 답을 순서대로 리스트로 반환하세요. 세그먼트 트리 위에서 직접 이분 탐색하면 빠릅니다."
        ),
        input_desc="arr : 0 이상 정수 리스트, queries : ['U',i,x] / ['F',v] 의 리스트 (1-based)",
        output_desc="'F' 질의들의 답(임계 인덱스, 없으면 -1)을 순서대로 담은 리스트",
        examples=[
            {"args": [[1, 2, 3, 4, 5], [["F", 6], ["U", 2, 10], ["F", 6], ["F", 100], ["F", 1]]],
             "output": [3, 2, -1, 1]},
            {"args": [[2, 2, 2], [["F", 1], ["F", 5], ["F", 7]]],
             "output": [1, 3, -1]},
        ],
        hints=[
            "누적합이 단조 증가(값이 음이 아니므로)인 점을 이용하면, 조건을 만족하는 첫 위치를 이분 탐색으로 찾을 수 있습니다. 갱신도 섞여 있습니다.",
            "구간합 세그먼트 트리를 만들고, 루트에서부터 내려가며 트리 위에서 이분 탐색하세요. 왼쪽 자식 합이 v 이상이면 왼쪽으로, 아니면 v에서 빼고 오른쪽으로.",
            "전체합 tree[1] < v 이면 -1. 아니면 p=1; while p<size: if tree[2p]>=v: p=2p else v-=tree[2p]; p=2p+1. 답은 p-size+1. 'U'는 리프 갱신 후 부모 합 갱신.",
        ],
        testcases=[
            {"args": [[1, 2, 3, 4, 5], [["F", 6], ["U", 2, 10], ["F", 6], ["F", 100], ["F", 1]]],
             "expected": [3, 2, -1, 1]},
            {"args": [[2, 2, 2], [["F", 1], ["F", 5], ["F", 7]]],
             "expected": [1, 3, -1]},
            {"args": [[3], [["F", 3], ["F", 4], ["U", 1, 10], ["F", 10]]],
             "expected": [1, -1, 1]},
            {"args": [[1, 1, 1, 1], [["F", 2], ["F", 4], ["U", 1, 5], ["F", 2]]],
             "expected": [2, 4, 1]},
        ],
        reference_py=r'''def solution(arr, queries):
    n = len(arr)
    size = 1
    while size < n:
        size *= 2
    tree = [0] * (2 * size)
    for i in range(n):
        tree[size + i] = arr[i]
    for p in range(size - 1, 0, -1):
        tree[p] = tree[2 * p] + tree[2 * p + 1]

    def update(idx, val):
        p = size + idx
        tree[p] = val
        p //= 2
        while p:
            tree[p] = tree[2 * p] + tree[2 * p + 1]
            p //= 2

    def find(v):
        if tree[1] < v:
            return -1
        p = 1
        while p < size:
            if tree[2 * p] >= v:
                p = 2 * p
            else:
                v -= tree[2 * p]
                p = 2 * p + 1
        return p - size + 1

    out = []
    for q in queries:
        if q[0] == 'U':
            update(q[1] - 1, q[2])
        else:
            out.append(find(q[1]))
    return out
''',
        reference_java=r'''import java.util.*;
class Solution {
    int size; long[] tree;
    public int[] solution(int[] arr, Object[][] queries) {
        int n = arr.length; size = 1;
        while (size < n) size *= 2;
        tree = new long[2 * size];
        for (int i = 0; i < n; i++) tree[size + i] = arr[i];
        for (int p = size - 1; p >= 1; p--) tree[p] = tree[2*p] + tree[2*p+1];
        List<Integer> out = new ArrayList<>();
        for (Object[] q : queries) {
            if (q[0].equals("U")) update((int)q[1] - 1, (int)q[2]);
            else out.add(find((long)(int)q[1]));
        }
        return out.stream().mapToInt(Integer::intValue).toArray();
    }
    void update(int idx, long val) {
        int p = size + idx; tree[p] = val; p /= 2;
        while (p >= 1) { tree[p] = tree[2*p] + tree[2*p+1]; p /= 2; }
    }
    int find(long v) {
        if (tree[1] < v) return -1;
        int p = 1;
        while (p < size) {
            if (tree[2*p] >= v) p = 2*p;
            else { v -= tree[2*p]; p = 2*p+1; }
        }
        return p - size + 1;
    }
}
''',
        template_py=(
            "# 누적합 임계 위치 : 구간합 세그먼트 트리 위에서 이분 탐색\n"
            "def solution(arr, queries):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

    # ============================================================ 35
    Problem(
        id="platinum-35",
        rank="Platinum",
        title="값 구간 개수 (입출력형)",
        style="프로그래머스",
        topic="좌표압축",
        type="stdin",
        description=(
            "수직선 위에 점을 추가하면서 특정 값 구간 안의 점 개수를 세는 연산을 Q번 수행한다.\n"
            "  - 'I x' : 값 x 인 점을 하나 추가한다(같은 값 중복 가능).\n"
            "  - 'C l r' : 현재까지 추가된 점들 중 값이 l 이상 r 이하인 것의 개수를 출력한다.\n"
            "값은 매우 클 수 있으므로 좌표 압축 후 세그먼트 트리(혹은 펜윅)로 처리한다."
        ),
        input_desc=(
            "첫째 줄에 연산 수 Q. 다음 Q개의 줄에 'I x' 또는 'C l r'. 값 x, l, r 은 큰 정수일 수 있다."
        ),
        output_desc="'C l r' 연산마다 구간 [l,r] 안의 점 개수를 한 줄에 하나씩 출력.",
        examples=[
            {"input": "7\nI 5\nI 100\nI 50\nC 1 60\nI 3\nC 1 4\nC 50 100\n",
             "output": "2\n1\n2\n"},
            {"input": "5\nI 10\nC 1 5\nI 2\nC 1 5\nC 2 2\n",
             "output": "0\n1\n1\n"},
        ],
        hints=[
            "값이 너무 커서 그대로 인덱스로 못 씁니다. 추가될 모든 값을 미리 모아 작은 순위로 바꾸는 전처리가 필요합니다.",
            "삽입되는 값(I 의 x)을 모두 모아 좌표 압축한 뒤, 순위 위에서 개수 세그먼트 트리를 운용하세요.",
            "정렬된 압축 좌표에서 l은 bisect_left, r은 bisect_right-1 로 순위 구간을 구해 세그트리 구간합으로 개수를 답합니다. 'I' 는 해당 순위 리프에 +1.",
        ],
        testcases=[
            {"input": "7\nI 5\nI 100\nI 50\nC 1 60\nI 3\nC 1 4\nC 50 100\n",
             "output": "2\n1\n2\n"},
            {"input": "5\nI 10\nC 1 5\nI 2\nC 1 5\nC 2 2\n",
             "output": "0\n1\n1\n"},
            {"input": "4\nI 1000000000\nI 1\nC 1 1000000000\nC 2 999999999\n",
             "output": "2\n0\n"},
            {"input": "6\nI 7\nI 7\nC 7 7\nI 3\nC 1 7\nC 4 6\n",
             "output": "2\n3\n0\n"},
        ],
        reference_py=r'''import sys
from bisect import bisect_left, bisect_right


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    q = int(data[idx]); idx += 1
    ops = []
    for _ in range(q):
        op = data[idx].decode(); idx += 1
        if op == 'I':
            x = int(data[idx]); idx += 1
            ops.append(('I', x))
        else:
            l = int(data[idx]); r = int(data[idx + 1]); idx += 2
            ops.append(('C', l, r))
    coords = sorted(set(o[1] for o in ops if o[0] == 'I'))
    pos = {v: i for i, v in enumerate(coords)}
    m = len(coords)
    size = 1
    while size < max(m, 1):
        size *= 2
    tree = [0] * (2 * size)

    def update(i):
        p = size + i
        tree[p] += 1
        p //= 2
        while p:
            tree[p] = tree[2 * p] + tree[2 * p + 1]
            p //= 2

    def query(l, r):
        if l > r:
            return 0
        res = 0
        l += size
        r += size + 1
        while l < r:
            if l & 1:
                res += tree[l]; l += 1
            if r & 1:
                r -= 1; res += tree[r]
            l //= 2; r //= 2
        return res

    out = []
    for o in ops:
        if o[0] == 'I':
            update(pos[o[1]])
        else:
            lo = bisect_left(coords, o[1])
            hi = bisect_right(coords, o[2]) - 1
            out.append(str(query(lo, hi)))
    print('\n'.join(out))


main()
''',
        reference_java=r'''import java.util.*;
import java.io.*;
public class Main {
    static int size; static int[] tree;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int q = Integer.parseInt(br.readLine().trim());
        int[][] ops = new int[q][3];
        TreeSet<Integer> set = new TreeSet<>();
        for (int i = 0; i < q; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String op = st.nextToken();
            if (op.equals("I")) {
                int x = Integer.parseInt(st.nextToken());
                ops[i] = new int[]{0, x, 0};
                set.add(x);
            } else {
                int l = Integer.parseInt(st.nextToken());
                int r = Integer.parseInt(st.nextToken());
                ops[i] = new int[]{1, l, r};
            }
        }
        List<Integer> coords = new ArrayList<>(set);
        int m = coords.size();
        size = 1;
        while (size < Math.max(m, 1)) size *= 2;
        tree = new int[2 * size];
        StringBuilder sb = new StringBuilder();
        for (int[] o : ops) {
            if (o[0] == 0) {
                update(Collections.binarySearch(coords, o[1]));
            } else {
                int lo = lowerBound(coords, o[1]);
                int hi = upperBound(coords, o[2]) - 1;
                sb.append(query(lo, hi)).append('\n');
            }
        }
        System.out.print(sb);
    }
    static int lowerBound(List<Integer> a, int x) {
        int lo = 0, hi = a.size();
        while (lo < hi) { int mid = (lo + hi) / 2; if (a.get(mid) < x) lo = mid + 1; else hi = mid; }
        return lo;
    }
    static int upperBound(List<Integer> a, int x) {
        int lo = 0, hi = a.size();
        while (lo < hi) { int mid = (lo + hi) / 2; if (a.get(mid) <= x) lo = mid + 1; else hi = mid; }
        return lo;
    }
    static void update(int i) {
        int p = size + i; tree[p] += 1; p /= 2;
        while (p >= 1) { tree[p] = tree[2*p] + tree[2*p+1]; p /= 2; }
    }
    static int query(int l, int r) {
        if (l > r) return 0;
        int res = 0; l += size; r += size + 1;
        while (l < r) {
            if ((l & 1) == 1) res += tree[l++];
            if ((r & 1) == 1) res += tree[--r];
            l /= 2; r /= 2;
        }
        return res;
    }
}
''',
        template_py=(
            "import sys\n"
            "from bisect import bisect_left, bisect_right\n"
            "# 좌표 압축 + 세그먼트 트리 : 'I x' 추가, 'C l r' 개수 질의\n"
            "data = sys.stdin.buffer.read().split()\n"
            "# ...\n"
        ),
    ),

]
