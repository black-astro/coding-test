"""유형별 실전 — 힙 / 우선순위 큐.

각 문제는 Problem 객체 하나로 표현된다.
"""

from engine.models import Problem

CATEGORY = "힙/우선순위큐"

PROBLEMS = [

    Problem(
        id="heap-01",
        rank="Gold",
        title="더 맵게",
        style="실전",
        topic="우선순위큐",
        type="stdin",
        description=(
            "모든 음식의 스코빌 지수를 K 이상으로 만들려고 한다. 가장 맵지 않은 음식과 "
            "두 번째로 맵지 않은 음식을 섞어 새로운 음식을 만들며, 새 음식의 스코빌 지수는 "
            "(가장 맵지 않은 음식의 지수) + (두 번째로 맵지 않은 음식의 지수) * 2 이다. "
            "모든 음식의 스코빌 지수가 K 이상이 될 때까지 섞은 횟수를 구하라. "
            "아무리 섞어도 모두 K 이상으로 만들 수 없으면 -1 을 출력한다."
        ),
        input_desc=(
            "첫 줄에 음식 개수 N (1 ≤ N ≤ 1,000,000) 과 목표 K. "
            "둘째 줄에 각 음식의 스코빌 지수 N개가 공백으로 주어진다."
        ),
        output_desc="모든 음식을 K 이상으로 만들기 위한 최소 섞기 횟수 (불가능하면 -1).",
        examples=[
            {"input": "6 7\n1 2 3 9 10 12", "output": "2"},
            {"input": "4 10\n2 3 1 5", "output": "3"},
        ],
        hints=[
            "매번 '가장 작은 두 값' 을 꺼내 섞어 다시 넣는 과정을 반복한다. 매번 정렬하면 느리니 효율적인 구조가 필요하다.",
            "최소 힙(우선순위 큐)을 쓰라. 항상 가장 작은 값이 맨 위에 오므로, 두 번 꺼내 섞은 값을 다시 넣으면 된다.",
            "heapify 후, 힙의 최솟값이 K 미만인 동안: a=pop, b=pop, push(a+b*2), count+=1. 원소가 1개만 남았는데 그 값이 K 미만이면 -1.",
        ],
        testcases=[
            {"input": "6 7\n1 2 3 9 10 12", "output": "2"},
            {"input": "4 10\n2 3 1 5", "output": "3"},
            {"input": "3 5\n5 6 7", "output": "0"},
            {"input": "1 7\n1", "output": "-1"},
            {"input": "2 7\n1 1", "output": "-1"},
            {"input": "1 0\n0", "output": "0"},
        ],
        reference_py=(
            "import sys, heapq\n"
            "d = sys.stdin.buffer.read().split()\n"
            "n, k = int(d[0]), int(d[1])\n"
            "h = list(map(int, d[2:2+n]))\n"
            "heapq.heapify(h)\n"
            "c = 0\n"
            "while len(h) > 1 and h[0] < k:\n"
            "    a = heapq.heappop(h); b = heapq.heappop(h)\n"
            "    heapq.heappush(h, a + b * 2); c += 1\n"
            "print(c if h[0] >= k else -1)\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        int n = Integer.parseInt(st.nextToken());\n"
            "        long k = Long.parseLong(st.nextToken());\n"
            "        PriorityQueue<Long> pq = new PriorityQueue<>();\n"
            "        st = new StringTokenizer(br.readLine());\n"
            "        for (int i = 0; i < n; i++) pq.add(Long.parseLong(st.nextToken()));\n"
            "        int c = 0;\n"
            "        while (pq.size() > 1 && pq.peek() < k) {\n"
            "            long a = pq.poll(), b = pq.poll();\n"
            "            pq.add(a + b * 2); c++;\n"
            "        }\n"
            "        System.out.println(pq.peek() >= k ? c : -1);\n"
            "    }\n"
            "}\n"
        ),
        reference_cpp=(
            "#include <bits/stdc++.h>\n"
            "using namespace std;\n"
            "int main(){\n"
            "    int n; long long k; scanf(\"%d %lld\", &n, &k);\n"
            "    priority_queue<long long, vector<long long>, greater<long long>> pq;\n"
            "    for (int i = 0; i < n; i++) { long long x; scanf(\"%lld\", &x); pq.push(x); }\n"
            "    int c = 0;\n"
            "    while ((int)pq.size() > 1 && pq.top() < k) {\n"
            "        long long a = pq.top(); pq.pop(); long long b = pq.top(); pq.pop();\n"
            "        pq.push(a + b * 2); c++;\n"
            "    }\n"
            "    printf(\"%d\\n\", pq.top() >= k ? c : -1);\n"
            "    return 0;\n"
            "}\n"
        ),
        template_py=(
            "import sys, heapq\n"
            "data = sys.stdin.read().split()\n"
            "# 첫 줄 N K, 둘째 줄 스코빌 N개. 최소 섞기 횟수를 출력(불가능 -1).\n"
        ),
    ),

    Problem(
        id="heap-02",
        rank="Gold",
        title="이중 우선순위 큐",
        style="카카오",
        topic="우선순위큐",
        type="stdin",
        description=(
            "최댓값과 최솟값을 모두 빠르게 꺼낼 수 있는 이중 우선순위 큐를 구현한다. "
            "다음 두 종류의 명령을 순서대로 처리한다.\n"
            "  - 'I n' : 정수 n 을 큐에 삽입한다.\n"
            "  - 'D 1' : 큐에서 최댓값을 하나 삭제한다.\n"
            "  - 'D -1': 큐에서 최솟값을 하나 삭제한다.\n"
            "큐가 비어 있는데 D 명령이 들어오면 그 명령은 무시한다. 같은 값이 여러 개일 수 있다. "
            "모든 명령을 처리한 뒤 큐의 상태를 출력한다."
        ),
        input_desc=(
            "첫째 줄에 명령의 수 T (1 ≤ T ≤ 1000000). "
            "다음 T개의 줄에 명령이 'I n' / 'D 1' / 'D -1' 형식으로 주어진다."
        ),
        output_desc=(
            "모든 명령 처리 후 큐가 비어 있으면 'EMPTY' 를 출력한다. "
            "비어 있지 않으면 큐의 최댓값과 최솟값을 공백으로 구분해 한 줄에 출력한다."
        ),
        examples=[
            {
                "input": "7\nI 16\nI -5643\nD -1\nD 1\nD 1\nI 123\nD -1\n",
                "output": "EMPTY\n",
            },
            {
                "input": "9\nI -45\nI 653\nD 1\nI -642\nI 45\nI 97\nD 1\nD -1\nI 333\n",
                "output": "333 -45\n",
            },
        ],
        hints=[
            "삽입과, 최댓값/최솟값 삭제가 섞여 들어옵니다. 한쪽 끝만 빠른 일반 큐로는 부족합니다.",
            "최소 힙과 최대 힙을 동시에 운용하세요. 한쪽에서 삭제한 원소를 다른 힙에서 바로 지울 수 없으므로, '지연 삭제(lazy deletion)' 로 유효성을 표시하며 처리합니다.",
            "각 삽입에 고유 id 를 부여해 (값,id) 를 두 힙에 넣고 alive[id]=True. 삭제 시 top 의 id 가 죽은 것이면 pop 으로 버리고, 살아있는 것을 만나면 그것을 삭제·alive 끔. 마지막에 살아있는 top 두 개로 최대·최소 출력.",
        ],
        testcases=[
            {
                "input": "7\nI 16\nI -5643\nD -1\nD 1\nD 1\nI 123\nD -1\n",
                "output": "EMPTY\n",
            },
            {
                "input": "9\nI -45\nI 653\nD 1\nI -642\nI 45\nI 97\nD 1\nD -1\nI 333\n",
                "output": "333 -45\n",
            },
            {
                "input": "3\nD 1\nD -1\nI 5\n",
                "output": "5 5\n",
            },
            {
                "input": "2\nD 1\nD -1\n",
                "output": "EMPTY\n",
            },
            {
                "input": "5\nI 1\nI 2\nI 3\nD 1\nD 1\n",
                "output": "1 1\n",
            },
        ],
        reference_py=(
            "import sys, heapq\n"
            "input = sys.stdin.readline\n"
            "\n"
            "def main():\n"
            "    t = int(input())\n"
            "    minh = []\n"
            "    maxh = []\n"
            "    alive = {}\n"
            "    nxt = 0\n"
            "    size = 0\n"
            "    for _ in range(t):\n"
            "        op, num = input().split()\n"
            "        num = int(num)\n"
            "        if op == 'I':\n"
            "            heapq.heappush(minh, (num, nxt))\n"
            "            heapq.heappush(maxh, (-num, nxt))\n"
            "            alive[nxt] = True\n"
            "            nxt += 1\n"
            "            size += 1\n"
            "        else:\n"
            "            if size == 0:\n"
            "                continue\n"
            "            if num == 1:\n"
            "                while maxh and not alive.get(maxh[0][1], False):\n"
            "                    heapq.heappop(maxh)\n"
            "                _, idx = heapq.heappop(maxh)\n"
            "                alive[idx] = False\n"
            "                size -= 1\n"
            "            else:\n"
            "                while minh and not alive.get(minh[0][1], False):\n"
            "                    heapq.heappop(minh)\n"
            "                _, idx = heapq.heappop(minh)\n"
            "                alive[idx] = False\n"
            "                size -= 1\n"
            "    while minh and not alive.get(minh[0][1], False):\n"
            "        heapq.heappop(minh)\n"
            "    while maxh and not alive.get(maxh[0][1], False):\n"
            "        heapq.heappop(maxh)\n"
            "    if size == 0 or not minh or not maxh:\n"
            "        print('EMPTY')\n"
            "    else:\n"
            "        print(f'{-maxh[0][0]} {minh[0][0]}')\n"
            "\n"
            "main()\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        int t = Integer.parseInt(br.readLine().trim());\n"
            "        PriorityQueue<long[]> minh = new PriorityQueue<>((x, y) -> Long.compare(x[0], y[0]));\n"
            "        PriorityQueue<long[]> maxh = new PriorityQueue<>((x, y) -> Long.compare(y[0], x[0]));\n"
            "        Map<Long, Boolean> alive = new HashMap<>();\n"
            "        long nxt = 0; int size = 0;\n"
            "        for (int i = 0; i < t; i++) {\n"
            "            StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "            String op = st.nextToken();\n"
            "            long num = Long.parseLong(st.nextToken());\n"
            "            if (op.equals(\"I\")) {\n"
            "                minh.add(new long[]{num, nxt});\n"
            "                maxh.add(new long[]{num, nxt});\n"
            "                alive.put(nxt, true); nxt++; size++;\n"
            "            } else {\n"
            "                if (size == 0) continue;\n"
            "                PriorityQueue<long[]> h = (num == 1) ? maxh : minh;\n"
            "                while (!h.isEmpty() && !alive.getOrDefault(h.peek()[1], false)) h.poll();\n"
            "                alive.put(h.poll()[1], false); size--;\n"
            "            }\n"
            "        }\n"
            "        while (!minh.isEmpty() && !alive.getOrDefault(minh.peek()[1], false)) minh.poll();\n"
            "        while (!maxh.isEmpty() && !alive.getOrDefault(maxh.peek()[1], false)) maxh.poll();\n"
            "        if (size == 0 || minh.isEmpty() || maxh.isEmpty()) System.out.println(\"EMPTY\");\n"
            "        else System.out.println(maxh.peek()[0] + \" \" + minh.peek()[0]);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys, heapq\n"
            "input = sys.stdin.readline\n"
            "# 이중 우선순위 큐 : 최댓/최솟값 삭제 후 상태 출력\n"
            "def main():\n"
            "    pass\n"
            "main()\n"
        ),
    ),

    Problem(
        id="heap-03",
        rank="Gold",
        title="카드 합치기 최소 비용",
        style="삼성",
        topic="우선순위큐",
        type="func",
        func_name="solution",
        description=(
            "여러 묶음의 카드가 있고, 각 묶음에 든 카드 장수가 주어진다. 두 묶음을 하나로 합칠 때 "
            "드는 비용은 두 묶음의 카드 장수의 합과 같다. 모든 묶음을 하나로 합칠 때까지 드는 "
            "비용의 합을 최소로 만들고 싶다. 그 최소 비용을 구하세요. "
            "(묶음이 하나뿐이면 합칠 필요가 없으므로 비용은 0 이다.)"
        ),
        input_desc="cards : 각 묶음의 카드 장수 리스트 (1 ≤ len ≤ 100000)",
        output_desc="모든 묶음을 하나로 합치는 데 드는 최소 총비용",
        examples=[
            {"args": [[10, 20, 40]], "output": 100},
            {"args": [[1, 2, 3, 4]], "output": 19},
        ],
        hints=[
            "작은 묶음일수록 여러 번 합쳐지므로 비용에 더 많이 더해집니다. 따라서 항상 가장 작은 두 묶음부터 합쳐야 손해가 적습니다.",
            "최소 힙(heapq)을 쓰세요. 매번 가장 작은 두 묶음을 꺼내 합치고, 합친 묶음을 다시 힙에 넣으면 됩니다.",
            "heapify 후 묶음이 2개 이상인 동안: a=pop, b=pop, s=a+b, total+=s, push(s). 묶음이 1개가 되면 종료하고 total 반환. (묶음이 1개면 0)",
        ],
        testcases=[
            {"args": [[10, 20, 40]], "expected": 100},
            {"args": [[1, 2, 3, 4]], "expected": 19},
            {"args": [[10]], "expected": 0},
            {"args": [[5, 5]], "expected": 10},
            {"args": [[1, 1, 1, 1]], "expected": 8},
        ],
        reference_py=(
            "import heapq\n"
            "\n"
            "def solution(cards):\n"
            "    if len(cards) <= 1:\n"
            "        return 0\n"
            "    heap = list(cards)\n"
            "    heapq.heapify(heap)\n"
            "    total = 0\n"
            "    while len(heap) > 1:\n"
            "        a = heapq.heappop(heap)\n"
            "        b = heapq.heappop(heap)\n"
            "        s = a + b\n"
            "        total += s\n"
            "        heapq.heappush(heap, s)\n"
            "    return total\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public long solution(int[] cards) {\n"
            "        if (cards.length <= 1) return 0;\n"
            "        PriorityQueue<Long> pq = new PriorityQueue<>();\n"
            "        for (int c : cards) pq.add((long) c);\n"
            "        long total = 0;\n"
            "        while (pq.size() > 1) {\n"
            "            long s = pq.poll() + pq.poll();\n"
            "            total += s;\n"
            "            pq.add(s);\n"
            "        }\n"
            "        return total;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import heapq\n"
            "# 카드 합치기 최소 비용 : 가장 작은 두 묶음부터 합치기\n"
            "def solution(cards):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

]
