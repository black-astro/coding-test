"""플래티넘 추가 배치 C — 문자열(KMP/트라이/Z) · 고급 그래프(SCC/MST) ·
위상 정렬 응용 · 분할 정복.

platinum-36 ~ platinum-50 (15문제). base 의 다익스트라/위상정렬(줄세우기) 와 중복되지 않도록
주제를 달리한다.
"""

from engine.models import Problem

RANK = "Platinum"

PROBLEMS = [

    Problem(
        id="platinum-36",
        rank="Platinum",
        title="문자열 패턴 등장 횟수 (KMP)",
        style="백준",
        topic="KMP",
        type="func",
        func_name="solution",
        description=(
            "긴 문자열 text 안에서 짧은 문자열 pattern 이 몇 번 나타나는지 세세요. "
            "겹쳐서 나타나는 경우도 모두 센다. 예를 들어 text='aaaa', pattern='aa' 이면 "
            "위치 0,1,2 에서 모두 나타나므로 3번이다. 문자열 길이가 크다고 가정하고 "
            "선형 시간 알고리즘으로 풀어야 한다."
        ),
        input_desc="text : 대상 문자열, pattern : 찾을 패턴 (모두 소문자 알파벳)",
        output_desc="text 안에 pattern 이 등장하는 횟수 (겹침 허용)",
        examples=[
            {"args": ["ababcababa", "aba"], "output": 3},
            {"args": ["aaaa", "aa"], "output": 3},
        ],
        hints=[
            "단순히 모든 시작 위치에서 비교하면 최악의 경우 느립니다. 비교에 실패했을 때 "
            "패턴의 어디서부터 다시 비교하면 되는지를 미리 알 수 있다면 빠르게 풀 수 있습니다.",
            "KMP 알고리즘을 사용하세요. 패턴의 '실패 함수(접두사이면서 접미사인 최대 길이)' 배열을 "
            "먼저 만들고, text 를 한 번 훑으면서 매칭합니다.",
            "pi 배열을 만든 뒤 k 를 현재 일치 길이로 두고 text 를 순회: 불일치면 k=pi[k-1], "
            "일치면 k+=1, k==m 이면 count+=1 후 k=pi[k-1] 로 되돌려 겹침을 처리합니다.",
        ],
        testcases=[
            {"args": ["ababcababa", "aba"], "expected": 3},
            {"args": ["aaaa", "aa"], "expected": 3},
            {"args": ["abc", "d"], "expected": 0},
            {"args": ["abcabcabc", "abc"], "expected": 3},
            {"args": ["a", "a"], "expected": 1},
        ],
        reference_py=(
            "def solution(text, pattern):\n"
            "    n, m = len(text), len(pattern)\n"
            "    if m == 0 or m > n:\n"
            "        return 0\n"
            "    pi = [0] * m\n"
            "    k = 0\n"
            "    for i in range(1, m):\n"
            "        while k > 0 and pattern[i] != pattern[k]:\n"
            "            k = pi[k - 1]\n"
            "        if pattern[i] == pattern[k]:\n"
            "            k += 1\n"
            "            pi[i] = k\n"
            "    count = 0\n"
            "    k = 0\n"
            "    for i in range(n):\n"
            "        while k > 0 and text[i] != pattern[k]:\n"
            "            k = pi[k - 1]\n"
            "        if text[i] == pattern[k]:\n"
            "            k += 1\n"
            "            if k == m:\n"
            "                count += 1\n"
            "                k = pi[k - 1]\n"
            "    return count\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(String text, String pattern) {\n"
            "        int n = text.length(), m = pattern.length();\n"
            "        if (m == 0 || m > n) return 0;\n"
            "        int[] pi = new int[m];\n"
            "        int k = 0;\n"
            "        for (int i = 1; i < m; i++) {\n"
            "            while (k > 0 && pattern.charAt(i) != pattern.charAt(k)) k = pi[k - 1];\n"
            "            if (pattern.charAt(i) == pattern.charAt(k)) pi[i] = ++k;\n"
            "        }\n"
            "        int count = 0; k = 0;\n"
            "        for (int i = 0; i < n; i++) {\n"
            "            while (k > 0 && text.charAt(i) != pattern.charAt(k)) k = pi[k - 1];\n"
            "            if (text.charAt(i) == pattern.charAt(k)) {\n"
            "                k++;\n"
            "                if (k == m) { count++; k = pi[k - 1]; }\n"
            "            }\n"
            "        }\n"
            "        return count;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# KMP : text 안에 pattern 이 등장하는 횟수(겹침 허용)\n"
            "def solution(text, pattern):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="platinum-37",
        rank="Platinum",
        title="패턴의 첫 등장 위치 (KMP)",
        style="해외대기업",
        topic="KMP",
        type="func",
        func_name="solution",
        description=(
            "문자열 text 안에서 pattern 이 처음으로 나타나는 시작 위치를 1-based 로 반환하세요. "
            "한 번도 나타나지 않으면 -1 을 반환합니다. (LeetCode 'Find the Index of the First "
            "Occurrence' 의 1-based 변형) 선형 시간으로 처리해야 한다."
        ),
        input_desc="text : 대상 문자열, pattern : 찾을 패턴 (모두 소문자 알파벳)",
        output_desc="pattern 이 처음 등장하는 1-based 시작 위치, 없으면 -1",
        examples=[
            {"args": ["haystack", "stack"], "output": 4},
            {"args": ["abcabd", "abd"], "output": 4},
        ],
        hints=[
            "이중 반복으로 모든 위치를 검사하면 느립니다. 패턴 내부 구조를 이용해 실패 시 "
            "되돌아갈 위치를 미리 계산해 두면 한 번의 스캔으로 찾을 수 있습니다.",
            "KMP 의 실패 함수(pi 배열)를 만든 뒤, text 를 순회하며 일치 길이 k 가 패턴 길이에 "
            "도달하는 순간의 위치를 답으로 합니다.",
            "k==m 이 되는 i 에서 시작 위치(0-based)는 i-m+1 이므로 1-based 답은 i-m+2 를 "
            "즉시 반환하면 됩니다. 끝까지 못 찾으면 -1.",
        ],
        testcases=[
            {"args": ["haystack", "stack"], "expected": 4},
            {"args": ["aaaaa", "bba"], "expected": -1},
            {"args": ["mississippi", "issip"], "expected": 5},
            {"args": ["abc", "abc"], "expected": 1},
            {"args": ["abcabd", "abd"], "expected": 4},
        ],
        reference_py=(
            "def solution(text, pattern):\n"
            "    n, m = len(text), len(pattern)\n"
            "    if m == 0:\n"
            "        return 1\n"
            "    if m > n:\n"
            "        return -1\n"
            "    pi = [0] * m\n"
            "    k = 0\n"
            "    for i in range(1, m):\n"
            "        while k > 0 and pattern[i] != pattern[k]:\n"
            "            k = pi[k - 1]\n"
            "        if pattern[i] == pattern[k]:\n"
            "            k += 1\n"
            "            pi[i] = k\n"
            "    k = 0\n"
            "    for i in range(n):\n"
            "        while k > 0 and text[i] != pattern[k]:\n"
            "            k = pi[k - 1]\n"
            "        if text[i] == pattern[k]:\n"
            "            k += 1\n"
            "            if k == m:\n"
            "                return i - m + 2\n"
            "    return -1\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public int solution(String text, String pattern) {\n"
            "        int n = text.length(), m = pattern.length();\n"
            "        if (m == 0) return 1;\n"
            "        if (m > n) return -1;\n"
            "        int[] pi = new int[m];\n"
            "        int k = 0;\n"
            "        for (int i = 1; i < m; i++) {\n"
            "            while (k > 0 && pattern.charAt(i) != pattern.charAt(k)) k = pi[k - 1];\n"
            "            if (pattern.charAt(i) == pattern.charAt(k)) pi[i] = ++k;\n"
            "        }\n"
            "        k = 0;\n"
            "        for (int i = 0; i < n; i++) {\n"
            "            while (k > 0 && text.charAt(i) != pattern.charAt(k)) k = pi[k - 1];\n"
            "            if (text.charAt(i) == pattern.charAt(k)) {\n"
            "                k++;\n"
            "                if (k == m) return i - m + 2;\n"
            "            }\n"
            "        }\n"
            "        return -1;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# KMP : pattern 의 첫 등장 위치(1-based), 없으면 -1\n"
            "def solution(text, pattern):\n"
            "    answer = -1\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="platinum-38",
        rank="Platinum",
        title="접두사로 시작하는 단어 수 (트라이)",
        style="프로그래머스",
        topic="트라이",
        type="func",
        func_name="solution",
        description=(
            "단어 목록 words 와 질의 목록 queries 가 주어진다. 각 질의는 하나의 접두사 문자열이며, "
            "words 중에서 그 접두사로 시작하는 단어가 몇 개인지 세야 한다. 모든 질의의 답을 "
            "순서대로 리스트로 반환하세요. 단어 수와 질의 수가 많을 수 있으므로 매번 전체를 "
            "훑지 않는 자료구조가 필요하다."
        ),
        input_desc="words : 단어(소문자) 리스트, queries : 접두사(소문자) 리스트",
        output_desc="각 질의 접두사로 시작하는 단어의 개수를 순서대로 담은 리스트",
        examples=[
            {
                "args": [["apple", "app", "application", "apply", "banana"], ["app", "appl", "ban", "cat"]],
                "output": [4, 3, 1, 0],
            },
            {
                "args": [["abc", "abd"], ["ab", "abc", "abcd"]],
                "output": [2, 1, 0],
            },
        ],
        hints=[
            "질의마다 모든 단어를 startswith 로 검사하면 단어×질의 만큼 느려집니다. 단어들을 "
            "글자 단위로 미리 정리해 두면 접두사 질의를 빠르게 답할 수 있습니다.",
            "트라이(Trie)를 사용하세요. 단어를 삽입할 때 지나가는 모든 노드의 카운터를 1씩 "
            "올려 두면, 그 노드를 지나는 단어의 수(=그 접두사로 시작하는 단어 수)가 됩니다.",
            "각 노드를 dict 로 만들고 자식과 별도로 통과 횟수 '#' 를 둡니다. 질의는 접두사를 "
            "따라 내려가다 도중에 글자가 없으면 0, 끝까지 가면 그 노드의 '#' 값을 답으로 합니다.",
        ],
        testcases=[
            {
                "args": [["apple", "app", "application", "apply", "banana"], ["app", "appl", "ban", "cat"]],
                "expected": [4, 3, 1, 0],
            },
            {
                "args": [["abc", "abd"], ["ab", "abc", "abcd"]],
                "expected": [2, 1, 0],
            },
            {
                "args": [["x", "xy", "xyz"], ["x", "xy", "xyz", "xyzw"]],
                "expected": [3, 2, 1, 0],
            },
            {
                "args": [["a"], ["a", "b"]],
                "expected": [1, 0],
            },
        ],
        reference_py=(
            "def solution(words, queries):\n"
            "    trie = {}\n"
            "    for w in words:\n"
            "        node = trie\n"
            "        for ch in w:\n"
            "            if ch not in node:\n"
            "                node[ch] = {'#': 0}\n"
            "            node = node[ch]\n"
            "            node['#'] += 1\n"
            "    res = []\n"
            "    for q in queries:\n"
            "        node = trie\n"
            "        ok = True\n"
            "        for ch in q:\n"
            "            if ch not in node:\n"
            "                ok = False\n"
            "                break\n"
            "            node = node[ch]\n"
            "        res.append(node['#'] if ok else 0)\n"
            "    return res\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    static class Node { Map<Character, Node> ch = new HashMap<>(); int cnt = 0; }\n"
            "    public List<Integer> solution(String[] words, String[] queries) {\n"
            "        Node root = new Node();\n"
            "        for (String w : words) {\n"
            "            Node node = root;\n"
            "            for (char c : w.toCharArray()) {\n"
            "                node = node.ch.computeIfAbsent(c, k -> new Node());\n"
            "                node.cnt++;\n"
            "            }\n"
            "        }\n"
            "        List<Integer> res = new ArrayList<>();\n"
            "        for (String q : queries) {\n"
            "            Node node = root; boolean ok = true;\n"
            "            for (char c : q.toCharArray()) {\n"
            "                node = node.ch.get(c);\n"
            "                if (node == null) { ok = false; break; }\n"
            "            }\n"
            "            res.add(ok ? node.cnt : 0);\n"
            "        }\n"
            "        return res;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 트라이 : 각 질의 접두사로 시작하는 단어 수의 리스트\n"
            "def solution(words, queries):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="platinum-39",
        rank="Platinum",
        title="Z 알고리즘 패턴 검색",
        style="백준",
        topic="Z 알고리즘",
        type="stdin",
        description=(
            "문자열 text 와 pattern 이 주어진다. text 안에서 pattern 이 나타나는 모든 시작 "
            "위치(1-based)를 찾아라. Z 알고리즘을 이용하면 pattern+구분자+text 의 Z 배열만으로 "
            "모든 등장 위치를 선형 시간에 구할 수 있다."
        ),
        input_desc="첫째 줄에 text, 둘째 줄에 pattern (모두 소문자 알파벳).",
        output_desc=(
            "첫째 줄에 등장 횟수 c 를 출력한다. c 가 1 이상이면 둘째 줄에 등장 시작 위치(1-based)를 "
            "오름차순으로 공백으로 구분해 출력한다. c 가 0 이면 둘째 줄은 출력하지 않는다."
        ),
        examples=[
            {"input": "ababababa\naba\n", "output": "4\n1 3 5 7\n"},
            {"input": "aaaaa\naa\n", "output": "4\n1 2 3 4\n"},
        ],
        hints=[
            "각 위치에서 pattern 과 얼마나 길게 일치하는지를 알면 됩니다. 'pattern + 절대 안 나오는 "
            "구분자 + text' 라는 합친 문자열을 만들어 생각해 보세요.",
            "Z 배열(각 위치 i 에서 시작해 문자열 전체 접두사와 일치하는 최대 길이)을 계산하세요. "
            "합친 문자열에서 Z[i] 가 pattern 길이 이상인 위치가 곧 등장 위치입니다.",
            "s = pattern + chr(1) + text 의 Z 배열을 구해, i 가 (m+1) 이상이고 Z[i] >= m 인 곳의 "
            "text 내 1-based 위치 i-(m+1)+1 을 모읍니다. 개수와 위치들을 출력하세요.",
        ],
        testcases=[
            {"input": "ababababa\naba\n", "output": "4\n1 3 5 7\n"},
            {"input": "aaaaa\naa\n", "output": "4\n1 2 3 4\n"},
            {"input": "abcdef\nxyz\n", "output": "0\n"},
            {"input": "zzz\nzzz\n", "output": "1\n1\n"},
        ],
        reference_py=(
            "import sys\n"
            "def z_func(s):\n"
            "    n = len(s)\n"
            "    z = [0] * n\n"
            "    if n:\n"
            "        z[0] = n\n"
            "    l = r = 0\n"
            "    for i in range(1, n):\n"
            "        if i < r:\n"
            "            z[i] = min(r - i, z[i - l])\n"
            "        while i + z[i] < n and s[z[i]] == s[i + z[i]]:\n"
            "            z[i] += 1\n"
            "        if i + z[i] > r:\n"
            "            l = i\n"
            "            r = i + z[i]\n"
            "    return z\n"
            "data = sys.stdin.read().split()\n"
            "text = data[0]\n"
            "pattern = data[1]\n"
            "m = len(pattern)\n"
            "s = pattern + chr(1) + text\n"
            "z = z_func(s)\n"
            "pos = []\n"
            "for i in range(m + 1, len(s)):\n"
            "    if z[i] >= m:\n"
            "        pos.append(str(i - (m + 1) + 1))\n"
            "print(len(pos))\n"
            "if pos:\n"
            "    print(' '.join(pos))\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    static int[] z(String s) {\n"
            "        int n = s.length();\n"
            "        int[] z = new int[n];\n"
            "        if (n > 0) z[0] = n;\n"
            "        int l = 0, r = 0;\n"
            "        for (int i = 1; i < n; i++) {\n"
            "            if (i < r) z[i] = Math.min(r - i, z[i - l]);\n"
            "            while (i + z[i] < n && s.charAt(z[i]) == s.charAt(i + z[i])) z[i]++;\n"
            "            if (i + z[i] > r) { l = i; r = i + z[i]; }\n"
            "        }\n"
            "        return z;\n"
            "    }\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        String text = br.readLine().trim();\n"
            "        String pattern = br.readLine().trim();\n"
            "        int m = pattern.length();\n"
            "        String s = pattern + (char) 1 + text;\n"
            "        int[] zz = z(s);\n"
            "        List<Integer> pos = new ArrayList<>();\n"
            "        for (int i = m + 1; i < s.length(); i++) if (zz[i] >= m) pos.add(i - (m + 1) + 1);\n"
            "        StringBuilder sb = new StringBuilder();\n"
            "        sb.append(pos.size());\n"
            "        if (!pos.isEmpty()) {\n"
            "            sb.append('\\n');\n"
            "            for (int k = 0; k < pos.size(); k++) {\n"
            "                if (k > 0) sb.append(' ');\n"
            "                sb.append(pos.get(k));\n"
            "            }\n"
            "        }\n"
            "        System.out.println(sb.toString());\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "# Z 알고리즘으로 pattern 의 모든 등장 위치(1-based) 찾기\n"
            "data = sys.stdin.read().split()\n"
            "# ...\n"
        ),
    ),

    Problem(
        id="platinum-40",
        rank="Platinum",
        title="강한 연결 요소의 개수 (SCC)",
        style="대기업",
        topic="SCC",
        type="func",
        func_name="solution",
        description=(
            "정점 1..n 과 방향 간선 목록이 주어진 그래프에서 강한 연결 요소(SCC)의 개수를 "
            "구하세요. 강한 연결 요소란 서로 도달 가능한 정점들의 최대 집합을 말한다. "
            "간선이 하나도 없는 정점은 자기 자신만으로 하나의 SCC 를 이룬다."
        ),
        input_desc="n : 정점 수(정점 번호 1..n), edges : [u, v] (u→v 방향 간선) 리스트",
        output_desc="강한 연결 요소의 개수",
        examples=[
            {"args": [6, [[1, 2], [2, 3], [3, 1], [3, 4], [4, 5], [5, 4]]], "output": 3},
            {"args": [3, [[1, 2], [2, 3]]], "output": 3},
        ],
        hints=[
            "방향 그래프에서 '서로 오갈 수 있는' 정점들을 묶는 문제입니다. 한 번의 DFS 만으로는 "
            "양방향 도달성을 판단하기 어렵다는 점에 주목하세요.",
            "코사라주(Kosaraju) 알고리즘을 쓰세요. 원그래프에서 DFS 종료 순서를 구하고, 역방향 "
            "그래프에서 그 역순으로 DFS 하면 한 번의 탐색이 하나의 SCC 가 됩니다.",
            "1) 원그래프 DFS 로 끝나는 순서(order)를 기록 → 2) 간선을 뒤집은 그래프에서 "
            "order 의 역순으로 미방문 정점을 DFS, 시작할 때마다 카운트 +1. (재귀 깊이 주의: 반복 스택 사용)",
        ],
        testcases=[
            {"args": [6, [[1, 2], [2, 3], [3, 1], [3, 4], [4, 5], [5, 4]]], "expected": 3},
            {"args": [3, [[1, 2], [2, 3], [3, 1]]], "expected": 1},
            {"args": [3, [[1, 2], [2, 3]]], "expected": 3},
            {"args": [1, []], "expected": 1},
            {"args": [4, [[1, 2], [2, 1], [3, 4], [4, 3]]], "expected": 2},
        ],
        reference_py=(
            "def solution(n, edges):\n"
            "    g = [[] for _ in range(n + 1)]\n"
            "    rg = [[] for _ in range(n + 1)]\n"
            "    for u, v in edges:\n"
            "        g[u].append(v)\n"
            "        rg[v].append(u)\n"
            "    visited = [False] * (n + 1)\n"
            "    order = []\n"
            "    for s in range(1, n + 1):\n"
            "        if visited[s]:\n"
            "            continue\n"
            "        stack = [(s, 0)]\n"
            "        visited[s] = True\n"
            "        while stack:\n"
            "            node, idx = stack.pop()\n"
            "            if idx < len(g[node]):\n"
            "                stack.append((node, idx + 1))\n"
            "                nxt = g[node][idx]\n"
            "                if not visited[nxt]:\n"
            "                    visited[nxt] = True\n"
            "                    stack.append((nxt, 0))\n"
            "            else:\n"
            "                order.append(node)\n"
            "    visited2 = [False] * (n + 1)\n"
            "    count = 0\n"
            "    for s in reversed(order):\n"
            "        if visited2[s]:\n"
            "            continue\n"
            "        count += 1\n"
            "        stack = [s]\n"
            "        visited2[s] = True\n"
            "        while stack:\n"
            "            node = stack.pop()\n"
            "            for nxt in rg[node]:\n"
            "                if not visited2[nxt]:\n"
            "                    visited2[nxt] = True\n"
            "                    stack.append(nxt)\n"
            "    return count\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int solution(int n, int[][] edges) {\n"
            "        List<Integer>[] g = new List[n + 1];\n"
            "        List<Integer>[] rg = new List[n + 1];\n"
            "        for (int i = 1; i <= n; i++) { g[i] = new ArrayList<>(); rg[i] = new ArrayList<>(); }\n"
            "        for (int[] e : edges) { g[e[0]].add(e[1]); rg[e[1]].add(e[0]); }\n"
            "        boolean[] vis = new boolean[n + 1];\n"
            "        Deque<int[]> stack = new ArrayDeque<>();\n"
            "        List<Integer> order = new ArrayList<>();\n"
            "        for (int s = 1; s <= n; s++) {\n"
            "            if (vis[s]) continue;\n"
            "            vis[s] = true; stack.push(new int[]{s, 0});\n"
            "            while (!stack.isEmpty()) {\n"
            "                int[] top = stack.peek();\n"
            "                if (top[1] < g[top[0]].size()) {\n"
            "                    int nxt = g[top[0]].get(top[1]++);\n"
            "                    if (!vis[nxt]) { vis[nxt] = true; stack.push(new int[]{nxt, 0}); }\n"
            "                } else { order.add(top[0]); stack.pop(); }\n"
            "            }\n"
            "        }\n"
            "        boolean[] vis2 = new boolean[n + 1];\n"
            "        int count = 0;\n"
            "        for (int i = order.size() - 1; i >= 0; i--) {\n"
            "            int s = order.get(i);\n"
            "            if (vis2[s]) continue;\n"
            "            count++;\n"
            "            Deque<Integer> st = new ArrayDeque<>(); st.push(s); vis2[s] = true;\n"
            "            while (!st.isEmpty()) {\n"
            "                int node = st.pop();\n"
            "                for (int nxt : rg[node]) if (!vis2[nxt]) { vis2[nxt] = true; st.push(nxt); }\n"
            "            }\n"
            "        }\n"
            "        return count;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# SCC(코사라주) : 강한 연결 요소의 개수\n"
            "def solution(n, edges):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="platinum-41",
        rank="Platinum",
        title="가장 큰 강한 연결 요소 (SCC)",
        style="해외대기업",
        topic="SCC",
        type="func",
        func_name="solution",
        description=(
            "정점 1..n 과 방향 간선 목록이 주어진 그래프에서, 강한 연결 요소(SCC) 중 가장 많은 "
            "정점을 포함하는 것의 크기를 반환하세요. 모든 정점은 최소한 자기 자신만으로도 크기 1 의 "
            "SCC 에 속한다."
        ),
        input_desc="n : 정점 수(정점 번호 1..n), edges : [u, v] (u→v 방향 간선) 리스트",
        output_desc="가장 큰 강한 연결 요소에 속한 정점 수",
        examples=[
            {"args": [6, [[1, 2], [2, 3], [3, 1], [3, 4], [4, 5], [5, 4]]], "output": 3},
            {"args": [4, [[1, 2], [2, 1], [3, 4], [4, 3]]], "output": 2},
        ],
        hints=[
            "SCC 들을 모두 구한 뒤 각 컴포넌트의 크기를 비교하면 됩니다. 핵심은 SCC 들을 정확히 "
            "분리하는 것입니다.",
            "코사라주로 SCC 를 나누되, 두 번째(역방향) 탐색에서 한 번의 DFS 가 방문한 정점 수를 "
            "세면 그 SCC 의 크기가 됩니다. 그 최댓값을 답으로 합니다.",
            "역방향 그래프를 order 역순으로 순회하며, 새 SCC 를 시작할 때마다 size 를 0 으로 두고 "
            "방문 정점마다 +1, 컴포넌트가 끝나면 best=max(best, size).",
        ],
        testcases=[
            {"args": [6, [[1, 2], [2, 3], [3, 1], [3, 4], [4, 5], [5, 4]]], "expected": 3},
            {"args": [3, [[1, 2], [2, 3], [3, 1]]], "expected": 3},
            {"args": [3, [[1, 2], [2, 3]]], "expected": 1},
            {"args": [4, [[1, 2], [2, 1], [3, 4], [4, 3]]], "expected": 2},
            {"args": [5, [[1, 2], [2, 3], [3, 1], [3, 4], [4, 5]]], "expected": 3},
        ],
        reference_py=(
            "def solution(n, edges):\n"
            "    g = [[] for _ in range(n + 1)]\n"
            "    rg = [[] for _ in range(n + 1)]\n"
            "    for u, v in edges:\n"
            "        g[u].append(v)\n"
            "        rg[v].append(u)\n"
            "    visited = [False] * (n + 1)\n"
            "    order = []\n"
            "    for s in range(1, n + 1):\n"
            "        if visited[s]:\n"
            "            continue\n"
            "        stack = [(s, 0)]\n"
            "        visited[s] = True\n"
            "        while stack:\n"
            "            node, idx = stack.pop()\n"
            "            if idx < len(g[node]):\n"
            "                stack.append((node, idx + 1))\n"
            "                nxt = g[node][idx]\n"
            "                if not visited[nxt]:\n"
            "                    visited[nxt] = True\n"
            "                    stack.append((nxt, 0))\n"
            "            else:\n"
            "                order.append(node)\n"
            "    visited2 = [False] * (n + 1)\n"
            "    best = 0\n"
            "    for s in reversed(order):\n"
            "        if visited2[s]:\n"
            "            continue\n"
            "        size = 0\n"
            "        stack = [s]\n"
            "        visited2[s] = True\n"
            "        while stack:\n"
            "            node = stack.pop()\n"
            "            size += 1\n"
            "            for nxt in rg[node]:\n"
            "                if not visited2[nxt]:\n"
            "                    visited2[nxt] = True\n"
            "                    stack.append(nxt)\n"
            "        if size > best:\n"
            "            best = size\n"
            "    return best\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int solution(int n, int[][] edges) {\n"
            "        List<Integer>[] g = new List[n + 1];\n"
            "        List<Integer>[] rg = new List[n + 1];\n"
            "        for (int i = 1; i <= n; i++) { g[i] = new ArrayList<>(); rg[i] = new ArrayList<>(); }\n"
            "        for (int[] e : edges) { g[e[0]].add(e[1]); rg[e[1]].add(e[0]); }\n"
            "        boolean[] vis = new boolean[n + 1];\n"
            "        Deque<int[]> stack = new ArrayDeque<>();\n"
            "        List<Integer> order = new ArrayList<>();\n"
            "        for (int s = 1; s <= n; s++) {\n"
            "            if (vis[s]) continue;\n"
            "            vis[s] = true; stack.push(new int[]{s, 0});\n"
            "            while (!stack.isEmpty()) {\n"
            "                int[] top = stack.peek();\n"
            "                if (top[1] < g[top[0]].size()) {\n"
            "                    int nxt = g[top[0]].get(top[1]++);\n"
            "                    if (!vis[nxt]) { vis[nxt] = true; stack.push(new int[]{nxt, 0}); }\n"
            "                } else { order.add(top[0]); stack.pop(); }\n"
            "            }\n"
            "        }\n"
            "        boolean[] vis2 = new boolean[n + 1];\n"
            "        int best = 0;\n"
            "        for (int i = order.size() - 1; i >= 0; i--) {\n"
            "            int s = order.get(i);\n"
            "            if (vis2[s]) continue;\n"
            "            int size = 0;\n"
            "            Deque<Integer> st = new ArrayDeque<>(); st.push(s); vis2[s] = true;\n"
            "            while (!st.isEmpty()) {\n"
            "                int node = st.pop(); size++;\n"
            "                for (int nxt : rg[node]) if (!vis2[nxt]) { vis2[nxt] = true; st.push(nxt); }\n"
            "            }\n"
            "            best = Math.max(best, size);\n"
            "        }\n"
            "        return best;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# SCC : 가장 큰 강한 연결 요소의 크기\n"
            "def solution(n, edges):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="platinum-42",
        rank="Platinum",
        title="최소 스패닝 트리 비용 (크루스칼)",
        style="백준",
        topic="최소 스패닝 트리",
        type="stdin",
        description=(
            "정점 V 개와 무방향 가중치 간선 E 개로 이루어진 연결 그래프가 주어진다. 모든 정점을 "
            "연결하면서 사용한 간선 가중치의 합이 최소가 되도록 하는 최소 스패닝 트리(MST)의 "
            "가중치 합을 출력하라."
        ),
        input_desc=(
            "첫째 줄에 V E (정점 수, 간선 수, 정점 번호는 1..V). 다음 E개의 줄에 a b w "
            "(정점 a 와 b 를 잇는 가중치 w 인 무방향 간선)."
        ),
        output_desc="최소 스패닝 트리의 간선 가중치 총합을 한 줄에 출력.",
        examples=[
            {"input": "3 3\n1 2 1\n2 3 2\n1 3 3\n", "output": "3\n"},
            {"input": "4 5\n1 2 1\n2 3 1\n3 4 1\n1 3 5\n2 4 5\n", "output": "3\n"},
        ],
        hints=[
            "모든 정점을 잇되 사이클을 만들지 않으면서 가장 싼 간선부터 욕심내어 고르는 전략을 "
            "떠올려 보세요.",
            "크루스칼 알고리즘을 쓰세요. 간선을 가중치 오름차순으로 정렬하고, 유니온-파인드로 "
            "사이클이 생기지 않는 간선만 골라 합칩니다.",
            "find/union 으로 두 정점이 다른 집합일 때만 간선을 채택하고 가중치를 누적합에 더합니다. "
            "정렬 후 차례로 처리하면 V-1 개를 고른 시점의 합이 답입니다.",
        ],
        testcases=[
            {"input": "3 3\n1 2 1\n2 3 2\n1 3 3\n", "output": "3\n"},
            {"input": "4 5\n1 2 1\n2 3 1\n3 4 1\n1 3 5\n2 4 5\n", "output": "3\n"},
            {"input": "5 7\n1 2 2\n1 3 3\n2 3 1\n3 4 4\n4 5 5\n2 5 7\n1 5 9\n", "output": "12\n"},
            {"input": "1 0\n", "output": "0\n"},
        ],
        reference_py=(
            "import sys\n"
            "data = sys.stdin.read().split()\n"
            "idx = 0\n"
            "v = int(data[idx]); e = int(data[idx + 1]); idx += 2\n"
            "edges = []\n"
            "for _ in range(e):\n"
            "    a = int(data[idx]); b = int(data[idx + 1]); w = int(data[idx + 2]); idx += 3\n"
            "    edges.append((w, a, b))\n"
            "edges.sort()\n"
            "parent = list(range(v + 1))\n"
            "def find(x):\n"
            "    while parent[x] != x:\n"
            "        parent[x] = parent[parent[x]]\n"
            "        x = parent[x]\n"
            "    return x\n"
            "total = 0\n"
            "for w, a, b in edges:\n"
            "    ra, rb = find(a), find(b)\n"
            "    if ra != rb:\n"
            "        parent[ra] = rb\n"
            "        total += w\n"
            "print(total)\n"
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
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int v = Integer.parseInt(st.nextToken());\n"
            "        int e = Integer.parseInt(st.nextToken());\n"
            "        int[][] edges = new int[e][3];\n"
            "        for (int i = 0; i < e; i++) {\n"
            "            st = new StringTokenizer(br.readLine());\n"
            "            edges[i][1] = Integer.parseInt(st.nextToken());\n"
            "            edges[i][2] = Integer.parseInt(st.nextToken());\n"
            "            edges[i][0] = Integer.parseInt(st.nextToken());\n"
            "        }\n"
            "        Arrays.sort(edges, (x, y) -> Integer.compare(x[0], y[0]));\n"
            "        parent = new int[v + 1];\n"
            "        for (int i = 0; i <= v; i++) parent[i] = i;\n"
            "        long total = 0;\n"
            "        for (int[] ed : edges) {\n"
            "            int ra = find(ed[1]), rb = find(ed[2]);\n"
            "            if (ra != rb) { parent[ra] = rb; total += ed[0]; }\n"
            "        }\n"
            "        System.out.println(total);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "# 크루스칼 MST : 최소 스패닝 트리 가중치 합\n"
            "data = sys.stdin.read().split()\n"
            "# ...\n"
        ),
    ),

    Problem(
        id="platinum-43",
        rank="Platinum",
        title="네트워크 연결 최소 비용 (프림)",
        style="해외대기업",
        topic="최소 스패닝 트리",
        type="func",
        func_name="solution",
        description=(
            "n 대의 컴퓨터(번호 1..n)를 모두 연결하려고 한다. 두 컴퓨터를 직접 연결하는 후보 케이블 "
            "목록 edges 가 주어지며 각 케이블에는 비용이 있다. 모든 컴퓨터가 서로 통신 가능하도록 "
            "(직접·간접 연결 포함) 만드는 최소 총비용을 반환하세요. 그래프는 항상 연결 가능하다고 "
            "가정한다. (LeetCode 'Min Cost to Connect All Points' 류)"
        ),
        input_desc="n : 컴퓨터 수, edges : [u, v, w] (u-v 를 비용 w 로 잇는 무방향 케이블) 리스트",
        output_desc="모든 컴퓨터를 연결하는 최소 총비용",
        examples=[
            {"args": [3, [[1, 2, 1], [2, 3, 2], [1, 3, 3]]], "output": 3},
            {"args": [5, [[1, 2, 2], [1, 3, 3], [2, 3, 1], [3, 4, 4], [4, 5, 5], [2, 5, 7]]], "output": 12},
        ],
        hints=[
            "모든 정점을 잇는 최소 비용 = 최소 스패닝 트리 비용입니다. 한 정점에서 시작해 트리를 "
            "키워 나가는 방식을 생각해 보세요.",
            "프림(Prim) 알고리즘을 우선순위 큐로 구현하세요. 현재 트리에 닿는 간선 중 가장 싼 것을 "
            "골라 새 정점을 트리에 편입합니다.",
            "heap=[(0,1)] 로 시작, pop 한 정점이 미방문이면 방문 처리하고 비용을 더한 뒤 인접 간선 "
            "(가중치, 상대정점)을 push. n 개 정점을 모두 편입하면 누적 비용이 답입니다.",
        ],
        testcases=[
            {"args": [3, [[1, 2, 1], [2, 3, 2], [1, 3, 3]]], "expected": 3},
            {"args": [4, [[1, 2, 1], [2, 3, 2], [3, 4, 3], [1, 4, 10]]], "expected": 6},
            {"args": [1, []], "expected": 0},
            {"args": [5, [[1, 2, 2], [1, 3, 3], [2, 3, 1], [3, 4, 4], [4, 5, 5], [2, 5, 7]]], "expected": 12},
            {"args": [2, [[1, 2, 7]]], "expected": 7},
        ],
        reference_py=(
            "import heapq\n"
            "def solution(n, edges):\n"
            "    g = [[] for _ in range(n + 1)]\n"
            "    for u, v, w in edges:\n"
            "        g[u].append((w, v))\n"
            "        g[v].append((w, u))\n"
            "    visited = [False] * (n + 1)\n"
            "    pq = [(0, 1)]\n"
            "    total = 0\n"
            "    cnt = 0\n"
            "    while pq and cnt < n:\n"
            "        w, u = heapq.heappop(pq)\n"
            "        if visited[u]:\n"
            "            continue\n"
            "        visited[u] = True\n"
            "        total += w\n"
            "        cnt += 1\n"
            "        for nw, nv in g[u]:\n"
            "            if not visited[nv]:\n"
            "                heapq.heappush(pq, (nw, nv))\n"
            "    return total\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int solution(int n, int[][] edges) {\n"
            "        List<int[]>[] g = new List[n + 1];\n"
            "        for (int i = 1; i <= n; i++) g[i] = new ArrayList<>();\n"
            "        for (int[] e : edges) { g[e[0]].add(new int[]{e[2], e[1]}); g[e[1]].add(new int[]{e[2], e[0]}); }\n"
            "        boolean[] vis = new boolean[n + 1];\n"
            "        PriorityQueue<int[]> pq = new PriorityQueue<>((x, y) -> Integer.compare(x[0], y[0]));\n"
            "        pq.add(new int[]{0, 1});\n"
            "        int total = 0, cnt = 0;\n"
            "        while (!pq.isEmpty() && cnt < n) {\n"
            "            int[] c = pq.poll();\n"
            "            if (vis[c[1]]) continue;\n"
            "            vis[c[1]] = true; total += c[0]; cnt++;\n"
            "            for (int[] nx : g[c[1]]) if (!vis[nx[1]]) pq.add(nx);\n"
            "        }\n"
            "        return total;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import heapq\n"
            "# 프림 MST : 모든 컴퓨터 연결 최소 비용\n"
            "def solution(n, edges):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="platinum-44",
        rank="Platinum",
        title="작업 스케줄링 최소 완료 시간 (위상 정렬)",
        style="대기업",
        topic="위상정렬",
        type="func",
        func_name="solution",
        description=(
            "n 개의 작업(번호 1..n)이 있고, 각 작업 i 를 처리하는 데 times[i-1] 만큼의 시간이 "
            "걸린다. 일부 작업 쌍에 대해 '작업 a 가 완전히 끝나야 작업 b 를 시작할 수 있다'는 "
            "선행 관계 deps 가 주어진다. 선행 관계만 지키면 여러 작업을 동시에(병렬로) 진행할 수 "
            "있을 때, 모든 작업을 끝내는 데 걸리는 최소 시간을 반환하세요."
        ),
        input_desc=(
            "n : 작업 수, times : 길이 n 의 정수 리스트(times[i-1] = 작업 i 의 소요 시간), "
            "deps : [a, b] (a 가 끝나야 b 시작 가능) 리스트"
        ),
        output_desc="모든 작업을 완료하는 데 걸리는 최소 시간",
        examples=[
            {"args": [3, [10, 1, 1], [[1, 2], [1, 3]]], "output": 11},
            {"args": [4, [5, 1, 1, 5], [[1, 2], [1, 3], [2, 4], [3, 4]]], "output": 11},
        ],
        hints=[
            "각 작업의 '완료 시각'은 자신의 모든 선행 작업이 끝난 가장 늦은 시각에 자기 소요 시간을 "
            "더한 값입니다. 이는 선행 관계 순서대로 계산해야 합니다.",
            "위상 정렬 순서로 진행하며 finish[v] = times[v] + max(선행 작업들의 finish) 를 구하세요. "
            "전체 답은 모든 finish 값의 최댓값(임계 경로)입니다.",
            "진입차수 0 인 작업의 finish 를 자기 소요 시간으로 두고 큐에 넣습니다. 작업 u 를 꺼낼 때 "
            "후속 v 에 대해 finish[v]=max(finish[v], finish[u]+times[v]) 로 갱신, 진입차수 0 이 되면 push.",
        ],
        testcases=[
            {"args": [3, [10, 1, 1], [[1, 2], [1, 3]]], "expected": 11},
            {"args": [4, [5, 1, 1, 5], [[1, 2], [1, 3], [2, 4], [3, 4]]], "expected": 11},
            {"args": [1, [7], []], "expected": 7},
            {"args": [3, [3, 3, 3], []], "expected": 3},
            {"args": [5, [1, 2, 3, 4, 5], [[1, 2], [2, 3], [3, 4], [4, 5]]], "expected": 15},
        ],
        reference_py=(
            "from collections import deque\n"
            "def solution(n, times, deps):\n"
            "    g = [[] for _ in range(n + 1)]\n"
            "    indeg = [0] * (n + 1)\n"
            "    for a, b in deps:\n"
            "        g[a].append(b)\n"
            "        indeg[b] += 1\n"
            "    finish = [0] * (n + 1)\n"
            "    q = deque()\n"
            "    for i in range(1, n + 1):\n"
            "        if indeg[i] == 0:\n"
            "            finish[i] = times[i - 1]\n"
            "            q.append(i)\n"
            "    while q:\n"
            "        u = q.popleft()\n"
            "        for v in g[u]:\n"
            "            if finish[u] + times[v - 1] > finish[v]:\n"
            "                finish[v] = finish[u] + times[v - 1]\n"
            "            indeg[v] -= 1\n"
            "            if indeg[v] == 0:\n"
            "                q.append(v)\n"
            "    return max(finish[1:n + 1])\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int solution(int n, int[] times, int[][] deps) {\n"
            "        List<Integer>[] g = new List[n + 1];\n"
            "        for (int i = 1; i <= n; i++) g[i] = new ArrayList<>();\n"
            "        int[] indeg = new int[n + 1];\n"
            "        for (int[] d : deps) { g[d[0]].add(d[1]); indeg[d[1]]++; }\n"
            "        int[] finish = new int[n + 1];\n"
            "        Deque<Integer> q = new ArrayDeque<>();\n"
            "        for (int i = 1; i <= n; i++) if (indeg[i] == 0) { finish[i] = times[i - 1]; q.add(i); }\n"
            "        while (!q.isEmpty()) {\n"
            "            int u = q.poll();\n"
            "            for (int v : g[u]) {\n"
            "                finish[v] = Math.max(finish[v], finish[u] + times[v - 1]);\n"
            "                if (--indeg[v] == 0) q.add(v);\n"
            "            }\n"
            "        }\n"
            "        int ans = 0;\n"
            "        for (int i = 1; i <= n; i++) ans = Math.max(ans, finish[i]);\n"
            "        return ans;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "from collections import deque\n"
            "# 위상 정렬 + 임계 경로 : 모든 작업 완료 최소 시간\n"
            "def solution(n, times, deps):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="platinum-45",
        rank="Platinum",
        title="선수 과목과 최소 학기 수 (위상 정렬)",
        style="프로그래머스",
        topic="위상정렬",
        type="func",
        func_name="solution",
        description=(
            "n 개의 과목(번호 1..n)이 있고, 선수 관계 prereqs 가 주어진다. [a, b] 는 과목 a 를 "
            "들어야 과목 b 를 들을 수 있다는 뜻이다. 한 학기에는 선수 조건을 모두 만족한 과목을 "
            "원하는 만큼 동시에 수강할 수 있다. 모든 과목을 이수하는 데 필요한 최소 학기 수를 "
            "반환하세요. (선수 관계에 사이클은 없다.)"
        ),
        input_desc="n : 과목 수, prereqs : [a, b] (a 가 b 의 선수 과목) 리스트",
        output_desc="모든 과목을 이수하는 데 필요한 최소 학기 수",
        examples=[
            {"args": [3, [[1, 2], [2, 3]]], "output": 3},
            {"args": [5, [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5]]], "output": 4},
        ],
        hints=[
            "한 학기에 들을 수 있는 과목은 선수 과목이 모두 끝난 것들입니다. 결국 가장 긴 선수 "
            "사슬의 길이가 필요한 학기 수가 됩니다.",
            "위상 정렬을 하면서 각 과목의 '깊이(레벨)'를 계산하세요. 선수 과목의 레벨보다 1 큰 값이 "
            "그 과목의 레벨이고, 최대 레벨이 답입니다.",
            "진입차수 0 인 과목 레벨을 1 로 두고 큐에 넣습니다. u 를 꺼내 후속 v 에 대해 "
            "level[v]=max(level[v], level[u]+1), 진입차수 0 이면 push. 답은 max(level).",
        ],
        testcases=[
            {"args": [3, [[1, 2], [2, 3]]], "expected": 3},
            {"args": [4, [[1, 3], [2, 3], [3, 4]]], "expected": 3},
            {"args": [3, []], "expected": 1},
            {"args": [5, [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5]]], "expected": 4},
            {"args": [1, []], "expected": 1},
        ],
        reference_py=(
            "from collections import deque\n"
            "def solution(n, prereqs):\n"
            "    g = [[] for _ in range(n + 1)]\n"
            "    indeg = [0] * (n + 1)\n"
            "    for a, b in prereqs:\n"
            "        g[a].append(b)\n"
            "        indeg[b] += 1\n"
            "    level = [0] * (n + 1)\n"
            "    q = deque()\n"
            "    for i in range(1, n + 1):\n"
            "        if indeg[i] == 0:\n"
            "            level[i] = 1\n"
            "            q.append(i)\n"
            "    while q:\n"
            "        u = q.popleft()\n"
            "        for v in g[u]:\n"
            "            if level[u] + 1 > level[v]:\n"
            "                level[v] = level[u] + 1\n"
            "            indeg[v] -= 1\n"
            "            if indeg[v] == 0:\n"
            "                q.append(v)\n"
            "    return max(level[1:n + 1])\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int solution(int n, int[][] prereqs) {\n"
            "        List<Integer>[] g = new List[n + 1];\n"
            "        for (int i = 1; i <= n; i++) g[i] = new ArrayList<>();\n"
            "        int[] indeg = new int[n + 1];\n"
            "        for (int[] p : prereqs) { g[p[0]].add(p[1]); indeg[p[1]]++; }\n"
            "        int[] level = new int[n + 1];\n"
            "        Deque<Integer> q = new ArrayDeque<>();\n"
            "        for (int i = 1; i <= n; i++) if (indeg[i] == 0) { level[i] = 1; q.add(i); }\n"
            "        while (!q.isEmpty()) {\n"
            "            int u = q.poll();\n"
            "            for (int v : g[u]) {\n"
            "                level[v] = Math.max(level[v], level[u] + 1);\n"
            "                if (--indeg[v] == 0) q.add(v);\n"
            "            }\n"
            "        }\n"
            "        int ans = 0;\n"
            "        for (int i = 1; i <= n; i++) ans = Math.max(ans, level[i]);\n"
            "        return ans;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "from collections import deque\n"
            "# 위상 정렬 : 모든 과목 이수 최소 학기 수\n"
            "def solution(n, prereqs):\n"
            "    answer = 1\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="platinum-46",
        rank="Platinum",
        title="거듭제곱 나머지 (분할 정복)",
        style="백준",
        topic="분할정복",
        type="func",
        func_name="solution",
        description=(
            "정수 a, b, m 이 주어질 때 a 의 b 제곱을 m 으로 나눈 나머지, 즉 (a^b) mod m 을 "
            "구하세요. b 가 매우 클 수 있으므로 단순 반복으로는 시간이 부족하다. 분할 정복(제곱을 "
            "반씩 쪼개는 빠른 거듭제곱)으로 O(log b) 에 계산해야 한다. (파이썬 내장 3-인자 pow 를 "
            "쓰지 말고 직접 구현하는 연습)"
        ),
        input_desc="a : 밑(0 이상), b : 지수(0 이상), m : 모듈러(1 이상)",
        output_desc="(a^b) mod m 의 값",
        examples=[
            {"args": [10, 11, 1000000007], "output": 999999307},
            {"args": [2, 10, 1000], "output": 24},
        ],
        hints=[
            "b 번 곱하면 b 가 클 때 너무 느립니다. a^b 를 (a^(b/2))^2 형태로 쪼개면 지수를 절반씩 "
            "줄일 수 있다는 점을 이용하세요.",
            "분할 정복(이진 거듭제곱)을 사용하세요. 지수를 이진수로 보고, 비트가 1 인 자리에서만 "
            "현재 밑을 곱하며, 매 단계 밑을 제곱합니다. 곱할 때마다 mod 를 취합니다.",
            "result=1%m, base=a%m; b>0 동안: b 가 홀수면 result=result*base%m, base=base*base%m, "
            "b//=2. 마지막 result 가 답. (m==1 이면 답은 0)",
        ],
        testcases=[
            {"args": [10, 11, 1000000007], "expected": 999999307},
            {"args": [2, 10, 1000], "expected": 24},
            {"args": [5, 0, 7], "expected": 1},
            {"args": [7, 1, 5], "expected": 2},
            {"args": [2, 5, 100], "expected": 32},
            {"args": [123456, 0, 1], "expected": 0},
        ],
        reference_py=(
            "def solution(a, b, m):\n"
            "    result = 1 % m\n"
            "    base = a % m\n"
            "    while b > 0:\n"
            "        if b & 1:\n"
            "            result = (result * base) % m\n"
            "        base = (base * base) % m\n"
            "        b >>= 1\n"
            "    return result\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    public long solution(long a, long b, long m) {\n"
            "        long result = 1 % m;\n"
            "        long base = a % m;\n"
            "        while (b > 0) {\n"
            "            if ((b & 1) == 1) result = (result * base) % m;\n"
            "            base = (base * base) % m;\n"
            "            b >>= 1;\n"
            "        }\n"
            "        return result;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 분할 정복 빠른 거듭제곱 : (a^b) mod m\n"
            "def solution(a, b, m):\n"
            "    answer = 1\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="platinum-47",
        rank="Platinum",
        title="행렬 거듭제곱 피보나치 (분할 정복)",
        style="해외대기업",
        topic="분할정복",
        type="func",
        func_name="solution",
        description=(
            "피보나치 수열을 F(0)=0, F(1)=1, F(k)=F(k-1)+F(k-2) 로 정의한다. n 과 m 이 주어질 때 "
            "F(n) 을 m 으로 나눈 나머지를 반환하세요. n 이 매우 클 수 있으므로 [[1,1],[1,0]] 행렬의 "
            "거듭제곱을 분할 정복(이진 거듭제곱)으로 계산해 O(log n) 에 구해야 한다."
        ),
        input_desc="n : 구할 피보나치 항의 번호(0 이상), m : 모듈러(1 이상)",
        output_desc="F(n) mod m 의 값",
        examples=[
            {"args": [10, 1000000007], "output": 55},
            {"args": [100, 1000], "output": 75},
        ],
        hints=[
            "[[1,1],[1,0]] 를 n 제곱한 행렬의 한 원소가 F(n) 이라는 성질을 이용하면 덧셈을 n 번 "
            "반복하지 않아도 됩니다.",
            "행렬의 이진 거듭제곱(분할 정복)을 구현하세요. 거듭제곱 47번 문제와 같은 구조이되 곱셈을 "
            "2x2 행렬 곱으로 바꾸고, 각 원소에 mod 를 취합니다.",
            "M=[[1,1],[1,0]], 단위행렬에서 시작해 비트가 1 인 자리에서 result=result*M, 매 단계 "
            "M=M*M. M^n 의 (0,1) 원소가 F(n). 모든 곱셈 후 %m. (n==0 이면 0)",
        ],
        testcases=[
            {"args": [10, 1000000007], "expected": 55},
            {"args": [0, 100], "expected": 0},
            {"args": [1, 100], "expected": 1},
            {"args": [100, 1000], "expected": 75},
            {"args": [2, 10], "expected": 1},
            {"args": [7, 1000], "expected": 13},
        ],
        reference_py=(
            "def solution(n, m):\n"
            "    def mul(A, B):\n"
            "        return [\n"
            "            [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % m,\n"
            "             (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % m],\n"
            "            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % m,\n"
            "             (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % m],\n"
            "        ]\n"
            "    result = [[1, 0], [0, 1]]\n"
            "    base = [[1, 1], [1, 0]]\n"
            "    e = n\n"
            "    while e > 0:\n"
            "        if e & 1:\n"
            "            result = mul(result, base)\n"
            "        base = mul(base, base)\n"
            "        e >>= 1\n"
            "    return result[0][1] % m\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    long mod;\n"
            "    long[][] mul(long[][] A, long[][] B) {\n"
            "        return new long[][]{\n"
            "            {(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % mod, (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % mod},\n"
            "            {(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % mod, (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % mod}\n"
            "        };\n"
            "    }\n"
            "    public long solution(long n, long m) {\n"
            "        mod = m;\n"
            "        long[][] result = {{1, 0}, {0, 1}};\n"
            "        long[][] base = {{1, 1}, {1, 0}};\n"
            "        long e = n;\n"
            "        while (e > 0) {\n"
            "            if ((e & 1) == 1) result = mul(result, base);\n"
            "            base = mul(base, base);\n"
            "            e >>= 1;\n"
            "        }\n"
            "        return result[0][1] % m;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 행렬 거듭제곱(분할 정복)으로 F(n) mod m\n"
            "def solution(n, m):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="platinum-48",
        rank="Platinum",
        title="역순 쌍의 개수 (분할 정복 정렬)",
        style="해외대기업",
        topic="분할정복",
        type="func",
        func_name="solution",
        description=(
            "정수 배열 arr 가 주어질 때, i < j 이면서 arr[i] > arr[j] 인 쌍 (i, j) 의 개수를 "
            "반환하세요. 이를 역순 쌍(inversion)이라 한다. 배열이 클 수 있으므로 O(n^2) 비교가 "
            "아니라 병합 정렬을 응용한 분할 정복으로 O(n log n) 에 세야 한다."
        ),
        input_desc="arr : 정수 리스트",
        output_desc="역순 쌍 (i<j 이고 arr[i]>arr[j]) 의 총 개수",
        examples=[
            {"args": [[3, 1, 2]], "output": 2},
            {"args": [[4, 3, 2, 1]], "output": 6},
        ],
        hints=[
            "모든 쌍을 직접 비교하면 n^2 입니다. 배열을 반으로 나눠 각각 정렬하면서, 두 절반을 "
            "합칠 때 생기는 역순 쌍을 한꺼번에 세는 방법을 생각해 보세요.",
            "병합 정렬(분할 정복)을 변형하세요. 병합 단계에서 오른쪽 원소를 먼저 가져갈 때, 왼쪽에 "
            "남은 원소 개수만큼 역순 쌍이 추가됩니다.",
            "merge 중 left[i] <= right[j] 면 left 채택, 아니면 right[j] 채택하며 cnt += len(left)-i. "
            "왼쪽·오른쪽 재귀에서 나온 역순 수와 병합에서 센 수를 모두 합산해 반환합니다.",
        ],
        testcases=[
            {"args": [[3, 1, 2]], "expected": 2},
            {"args": [[1, 2, 3, 4]], "expected": 0},
            {"args": [[4, 3, 2, 1]], "expected": 6},
            {"args": [[2, 4, 1, 3, 5]], "expected": 3},
            {"args": [[]], "expected": 0},
            {"args": [[1]], "expected": 0},
        ],
        reference_py=(
            "def solution(arr):\n"
            "    def sort_count(a):\n"
            "        if len(a) <= 1:\n"
            "            return a, 0\n"
            "        mid = len(a) // 2\n"
            "        left, lc = sort_count(a[:mid])\n"
            "        right, rc = sort_count(a[mid:])\n"
            "        merged = []\n"
            "        i = j = 0\n"
            "        cnt = lc + rc\n"
            "        while i < len(left) and j < len(right):\n"
            "            if left[i] <= right[j]:\n"
            "                merged.append(left[i])\n"
            "                i += 1\n"
            "            else:\n"
            "                merged.append(right[j])\n"
            "                j += 1\n"
            "                cnt += len(left) - i\n"
            "        merged.extend(left[i:])\n"
            "        merged.extend(right[j:])\n"
            "        return merged, cnt\n"
            "    return sort_count(arr)[1]\n"
        ),
        reference_java=(
            "class Solution {\n"
            "    long count;\n"
            "    int[] merge(int[] a) {\n"
            "        if (a.length <= 1) return a;\n"
            "        int mid = a.length / 2;\n"
            "        int[] left = merge(java.util.Arrays.copyOfRange(a, 0, mid));\n"
            "        int[] right = merge(java.util.Arrays.copyOfRange(a, mid, a.length));\n"
            "        int[] res = new int[a.length];\n"
            "        int i = 0, j = 0, k = 0;\n"
            "        while (i < left.length && j < right.length) {\n"
            "            if (left[i] <= right[j]) res[k++] = left[i++];\n"
            "            else { res[k++] = right[j++]; count += left.length - i; }\n"
            "        }\n"
            "        while (i < left.length) res[k++] = left[i++];\n"
            "        while (j < right.length) res[k++] = right[j++];\n"
            "        return res;\n"
            "    }\n"
            "    public long solution(int[] arr) {\n"
            "        count = 0;\n"
            "        merge(arr);\n"
            "        return count;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 분할 정복(병합 정렬)으로 역순 쌍 개수 세기\n"
            "def solution(arr):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="platinum-49",
        rank="Platinum",
        title="전화번호 목록 일관성 (트라이)",
        style="대기업",
        topic="트라이",
        type="stdin",
        description=(
            "n 개의 전화번호 목록이 주어진다. 목록이 '일관성 있다'는 것은 어떤 번호도 다른 번호의 "
            "접두사가 되지 않는다는 뜻이다. 예를 들어 911 과 91125426 이 함께 있으면 911 이 "
            "91125426 의 접두사이므로 일관성이 없다. 목록이 일관성 있으면 YES, 아니면 NO 를 "
            "출력하라."
        ),
        input_desc="첫째 줄에 전화번호 개수 n. 다음 n개의 줄에 각각 전화번호(숫자 문자열).",
        output_desc="목록이 일관성 있으면 YES, 그렇지 않으면 NO 를 출력.",
        examples=[
            {"input": "3\n911\n97625999\n91125426\n", "output": "NO\n"},
            {"input": "5\n113\n12340\n123440\n12345\n98346\n", "output": "YES\n"},
        ],
        hints=[
            "어떤 번호가 다른 번호의 '시작 부분'인지 검사하는 문제입니다. 번호들을 글자 단위로 한 "
            "구조에 모아 두면 접두사 관계를 효율적으로 확인할 수 있습니다.",
            "트라이(Trie)에 번호를 하나씩 삽입하세요. 삽입 중 (1) 이미 끝(end)으로 표시된 노드를 "
            "지나가거나 (2) 삽입을 마친 노드가 이미 자식을 가지고 있으면 접두사 충돌입니다.",
            "각 번호 삽입: 경로의 노드에 end 표시가 있으면 NO. 삽입을 마친 노드에 다른 자식이 "
            "있거나 이미 end 면 NO. 끝까지 충돌 없으면 YES. 마지막 노드에 end 를 표시합니다.",
        ],
        testcases=[
            {"input": "3\n911\n97625999\n91125426\n", "output": "NO\n"},
            {"input": "5\n113\n12340\n123440\n12345\n98346\n", "output": "YES\n"},
            {"input": "2\n12\n123\n", "output": "NO\n"},
            {"input": "1\n5\n", "output": "YES\n"},
            {"input": "2\n123\n456\n", "output": "YES\n"},
        ],
        reference_py=(
            "import sys\n"
            "data = sys.stdin.read().split()\n"
            "n = int(data[0])\n"
            "nums = data[1:1 + n]\n"
            "trie = {}\n"
            "bad = False\n"
            "for num in nums:\n"
            "    node = trie\n"
            "    for ch in num:\n"
            "        if node.get('end'):\n"
            "            bad = True\n"
            "        if ch not in node:\n"
            "            node[ch] = {}\n"
            "        node = node[ch]\n"
            "    if any(k != 'end' for k in node):\n"
            "        bad = True\n"
            "    if node.get('end'):\n"
            "        bad = True\n"
            "    node['end'] = True\n"
            "    if bad:\n"
            "        break\n"
            "print('NO' if bad else 'YES')\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    static class Node { Map<Character, Node> ch = new HashMap<>(); boolean end = false; }\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        int n = Integer.parseInt(br.readLine().trim());\n"
            "        Node root = new Node();\n"
            "        boolean bad = false;\n"
            "        for (int t = 0; t < n; t++) {\n"
            "            String num = br.readLine().trim();\n"
            "            Node node = root;\n"
            "            for (char c : num.toCharArray()) {\n"
            "                if (node.end) bad = true;\n"
            "                node = node.ch.computeIfAbsent(c, k -> new Node());\n"
            "            }\n"
            "            if (!node.ch.isEmpty()) bad = true;\n"
            "            if (node.end) bad = true;\n"
            "            node.end = true;\n"
            "            if (bad) break;\n"
            "        }\n"
            "        System.out.println(bad ? \"NO\" : \"YES\");\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "# 트라이 : 전화번호 목록 일관성(YES/NO)\n"
            "data = sys.stdin.read().split()\n"
            "# ...\n"
        ),
    ),

    Problem(
        id="platinum-50",
        rank="Platinum",
        title="쿼드트리 압축 (분할 정복)",
        style="백준",
        topic="분할정복",
        type="stdin",
        description=(
            "0 과 1 로 이루어진 N x N 영상이 주어진다(N 은 2 의 거듭제곱). 영상 전체가 같은 숫자면 "
            "그 숫자 하나로 압축한다. 그렇지 않으면 영상을 네 등분(왼쪽 위, 오른쪽 위, 왼쪽 아래, "
            "오른쪽 아래 순서)하여 각각을 같은 방식으로 압축한 결과를 괄호로 묶어 '(' + 네 결과 + ')' "
            "로 표현한다. 주어진 영상의 압축 결과 문자열을 출력하라."
        ),
        input_desc=(
            "첫째 줄에 N (2 의 거듭제곱). 다음 N개의 줄에 각각 길이 N 의 0/1 문자열로 영상이 주어진다."
        ),
        output_desc="쿼드트리 방식으로 압축한 결과 문자열을 한 줄에 출력.",
        examples=[
            {
                "input": "8\n11110000\n11110000\n00011100\n00011100\n11110000\n11110000\n11110011\n11110011\n",
                "output": "((110(0101))(0010)1(0001))\n",
            },
            {
                "input": "4\n1110\n1100\n0010\n0001\n",
                "output": "(1(1000)0(1001))\n",
            },
        ],
        hints=[
            "전체가 같은 값이면 한 글자, 아니면 네 조각으로 쪼개 같은 문제를 푸는 전형적인 분할 "
            "정복 구조입니다. 좌상, 우상, 좌하, 우하 순서를 정확히 지키세요.",
            "재귀 함수 compress(행, 열, 크기)를 만드세요. 해당 정사각형이 모두 같은 값이면 그 값을 "
            "반환, 아니면 절반 크기로 네 부분을 재귀 호출해 괄호로 묶습니다.",
            "크기 size 정사각형의 모든 칸이 grid[r][c] 와 같은지 검사 → 같으면 그 글자 반환. 아니면 "
            "h=size//2 로 '(' + rec(r,c,h)+rec(r,c+h,h)+rec(r+h,c,h)+rec(r+h,c+h,h) + ')'.",
        ],
        testcases=[
            {
                "input": "8\n11110000\n11110000\n00011100\n00011100\n11110000\n11110000\n11110011\n11110011\n",
                "output": "((110(0101))(0010)1(0001))\n",
            },
            {
                "input": "4\n1110\n1100\n0010\n0001\n",
                "output": "(1(1000)0(1001))\n",
            },
            {"input": "2\n10\n01\n", "output": "(1001)\n"},
            {"input": "1\n1\n", "output": "1\n"},
            {"input": "2\n00\n00\n", "output": "0\n"},
        ],
        reference_py=(
            "import sys\n"
            "data = sys.stdin.read().split()\n"
            "n = int(data[0])\n"
            "grid = data[1:1 + n]\n"
            "def rec(r, c, size):\n"
            "    first = grid[r][c]\n"
            "    same = all(grid[r + i][c + j] == first for i in range(size) for j in range(size))\n"
            "    if same:\n"
            "        return first\n"
            "    h = size // 2\n"
            "    return ('(' + rec(r, c, h) + rec(r, c + h, h)\n"
            "            + rec(r + h, c, h) + rec(r + h, c + h, h) + ')')\n"
            "print(rec(0, 0, n))\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    static String[] grid;\n"
            "    static String rec(int r, int c, int size) {\n"
            "        char first = grid[r].charAt(c);\n"
            "        boolean same = true;\n"
            "        for (int i = 0; i < size && same; i++)\n"
            "            for (int j = 0; j < size; j++)\n"
            "                if (grid[r + i].charAt(c + j) != first) { same = false; break; }\n"
            "        if (same) return String.valueOf(first);\n"
            "        int h = size / 2;\n"
            "        return \"(\" + rec(r, c, h) + rec(r, c + h, h)\n"
            "             + rec(r + h, c, h) + rec(r + h, c + h, h) + \")\";\n"
            "    }\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        int n = Integer.parseInt(br.readLine().trim());\n"
            "        grid = new String[n];\n"
            "        for (int i = 0; i < n; i++) grid[i] = br.readLine().trim();\n"
            "        System.out.println(rec(0, 0, n));\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "# 쿼드트리 압축(분할 정복)\n"
            "data = sys.stdin.read().split()\n"
            "# ...\n"
        ),
    ),

]
