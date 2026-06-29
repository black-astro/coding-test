"""해시 유형 실전 문제 모음.

완주하지 못한 선수 / 빈도수·중복 / 전화번호 접두어 / 의상 조합 등
'개수를 빠르게 세거나 매핑한다'는 해시의 감각을 익히는 4문제.
"""

from engine.models import Problem

CATEGORY = "해시"

PROBLEMS = [

    Problem(
        id="hash-01",
        rank="Bronze",
        title="완주하지 못한 선수",
        style="프로그래머스",
        topic="해시",
        type="func",
        func_name="solution",
        description=(
            "마라톤 대회에 참가한 선수 이름 목록 participant 와 완주한 선수 이름 목록 "
            "completion 이 주어진다. 단 한 명만 완주하지 못했을 때, 완주하지 못한 선수의 "
            "이름을 반환하세요. 참가자 중에는 동명이인이 있을 수 있습니다."
        ),
        input_desc=(
            "participant : 참가 선수 이름 리스트 (1 ≤ len ≤ 100000)\n"
            "completion  : 완주 선수 이름 리스트 (len(participant) - 1)"
        ),
        output_desc="완주하지 못한 선수의 이름(문자열) 하나",
        examples=[
            {"args": [["leo", "kiki", "eden"], ["eden", "kiki"]], "output": "leo"},
            {"args": [["mislav", "stanko", "mislav", "ana"],
                      ["stanko", "ana", "mislav"]], "output": "mislav"},
        ],
        hints=[
            "두 목록의 차이를 찾는 문제입니다. 이름 하나하나를 일일이 비교하면 느리니, "
            "'각 이름이 몇 번 나오는지'를 세는 방향으로 생각해 보세요.",
            "딕셔너리(또는 collections.Counter)로 참가자 이름의 등장 횟수를 세고, "
            "완주자 이름마다 그 횟수를 1씩 빼세요. 동명이인 때문에 단순 집합 차집합은 안 됩니다.",
            "cnt = Counter(participant); 완주자마다 cnt[name] -= 1; "
            "마지막에 cnt 에서 값이 0보다 큰 이름을 반환하면 됩니다.",
        ],
        testcases=[
            {"args": [["leo", "kiki", "eden"], ["eden", "kiki"]], "expected": "leo"},
            {"args": [["marina", "josipa", "nikola", "vinko", "filipa"],
                      ["josipa", "filipa", "marina", "nikola"]], "expected": "vinko"},
            {"args": [["mislav", "stanko", "mislav", "ana"],
                      ["stanko", "ana", "mislav"]], "expected": "mislav"},
            {"args": [["kim"], []], "expected": "kim"},
        ],
        reference_py=(
            "from collections import Counter\n"
            "def solution(participant, completion):\n"
            "    cnt = Counter(participant)\n"
            "    for name in completion:\n"
            "        cnt[name] -= 1\n"
            "    for name, c in cnt.items():\n"
            "        if c > 0:\n"
            "            return name\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public String solution(String[] participant, String[] completion) {\n"
            "        HashMap<String, Integer> map = new HashMap<>();\n"
            "        for (String p : participant) map.put(p, map.getOrDefault(p, 0) + 1);\n"
            "        for (String c : completion) map.put(c, map.get(c) - 1);\n"
            "        for (Map.Entry<String, Integer> e : map.entrySet())\n"
            "            if (e.getValue() > 0) return e.getKey();\n"
            "        return \"\";\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 완주하지 못한 선수의 이름을 반환하세요.\n"
            "def solution(participant, completion):\n"
            "    answer = ''\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="hash-02",
        rank="Silver",
        title="가장 많이 등장한 수",
        style="소프티어",
        topic="빈도수",
        type="stdin",
        description=(
            "N개의 정수가 주어진다. 이 중 가장 많이 등장한 수를 출력하라. "
            "가장 많이 등장한 수가 여러 개라면 그중 가장 작은 수를 출력한다."
        ),
        input_desc=(
            "첫째 줄에 정수의 개수 N (1 ≤ N ≤ 100000)\n"
            "둘째 줄에 N개의 정수가 공백으로 구분되어 주어진다."
        ),
        output_desc="가장 많이 등장한 수(동률이면 가장 작은 수)를 한 줄에 출력한다.",
        examples=[
            {"input": "5\n1 3 3 2 1\n", "output": "1\n"},
            {"input": "6\n5 5 5 2 2 9\n", "output": "5\n"},
        ],
        hints=[
            "각 수가 몇 번 나왔는지 먼저 세야 합니다. 정렬만으로도 가능하지만, "
            "등장 횟수를 직접 세면 더 직관적입니다.",
            "딕셔너리(또는 Counter)로 수마다 빈도를 셉니다. 그다음 '빈도가 가장 크고, "
            "빈도가 같으면 값이 가장 작은' 수를 골라야 합니다.",
            "cnt = Counter(nums) 후 min(cnt, key=lambda x: (-cnt[x], x)) 를 출력하면 "
            "빈도 내림차순·값 오름차순으로 정확히 원하는 수가 선택됩니다.",
        ],
        testcases=[
            {"input": "5\n1 3 3 2 1\n", "output": "1\n"},
            {"input": "1\n7\n", "output": "7\n"},
            {"input": "6\n5 5 5 2 2 9\n", "output": "5\n"},
            {"input": "4\n-1 -1 -2 -2\n", "output": "-2\n"},
        ],
        reference_py=(
            "import sys\n"
            "from collections import Counter\n"
            "input = sys.stdin.readline\n"
            "n = int(input())\n"
            "nums = list(map(int, input().split()))\n"
            "cnt = Counter(nums)\n"
            "print(min(cnt, key=lambda x: (-cnt[x], x)))\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        int n = Integer.parseInt(br.readLine().trim());\n"
            "        StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "        HashMap<Integer, Integer> map = new HashMap<>();\n"
            "        for (int i = 0; i < n; i++) {\n"
            "            int v = Integer.parseInt(st.nextToken());\n"
            "            map.put(v, map.getOrDefault(v, 0) + 1);\n"
            "        }\n"
            "        int best = 0, bestCnt = -1;\n"
            "        for (Map.Entry<Integer, Integer> e : map.entrySet()) {\n"
            "            int v = e.getKey(), c = e.getValue();\n"
            "            if (c > bestCnt || (c == bestCnt && v < best)) { best = v; bestCnt = c; }\n"
            "        }\n"
            "        System.out.println(best);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "# 가장 많이 등장한 수(동률이면 가장 작은 수)를 출력\n"
            "n = int(input())\n"
            "# ...\n"
        ),
    ),

    Problem(
        id="hash-03",
        rank="Silver",
        title="전화번호 접두어 검사",
        style="라인",
        topic="문자열 해시",
        type="func",
        func_name="solution",
        description=(
            "전화번호부에 등록된 번호 목록 phone_book 이 주어진다. 어떤 번호도 다른 번호의 "
            "접두어(앞부분)가 아니면 번호부가 '일관성 있다'고 한다. 예를 들어 '119' 가 "
            "'1195524421' 의 접두어이면 일관성이 깨진다. 일관성이 있으면 True, 깨지면 False 를 "
            "반환하세요."
        ),
        input_desc=(
            "phone_book : 전화번호(숫자로 이루어진 문자열) 리스트 (1 ≤ len ≤ 1000000)"
        ),
        output_desc="번호부가 일관성 있으면 True, 한 번호가 다른 번호의 접두어이면 False",
        examples=[
            {"args": [["119", "97674223", "1195524421"]], "output": False},
            {"args": [["123", "456", "789"]], "output": True},
        ],
        hints=[
            "모든 번호 쌍을 비교하면 번호가 많을 때 너무 느립니다. 접두어 관계는 "
            "두 문자열이 '비슷한 시작'을 공유한다는 뜻인데, 그런 번호들을 어떻게 모을까요?",
            "번호들을 사전순으로 정렬하면, 접두어 관계인 번호들은 반드시 바로 옆에 인접해 "
            "위치합니다. 인접한 두 번호만 검사하면 됩니다. (해시 셋으로도 풀 수 있습니다.)",
            "phone_book.sort() 후 인접한 (a, b) 쌍마다 b.startswith(a) 이면 접두어 관계이므로 "
            "False, 끝까지 없으면 True 를 반환합니다.",
        ],
        testcases=[
            {"args": [["119", "97674223", "1195524421"]], "expected": False},
            {"args": [["123", "456", "789"]], "expected": True},
            {"args": [["12", "123", "1235", "567", "88"]], "expected": False},
            {"args": [["1"]], "expected": True},
            {"args": [["113", "12340", "123440", "12345", "98346"]], "expected": True},
        ],
        reference_py=(
            "def solution(phone_book):\n"
            "    phone_book.sort()\n"
            "    for a, b in zip(phone_book, phone_book[1:]):\n"
            "        if b.startswith(a):\n"
            "            return False\n"
            "    return True\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public boolean solution(String[] phoneBook) {\n"
            "        Arrays.sort(phoneBook);\n"
            "        for (int i = 0; i + 1 < phoneBook.length; i++)\n"
            "            if (phoneBook[i + 1].startsWith(phoneBook[i])) return false;\n"
            "        return true;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 번호부가 일관성 있으면 True, 접두어 관계가 있으면 False\n"
            "def solution(phone_book):\n"
            "    answer = True\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="hash-04",
        rank="Gold",
        title="의상 조합의 수",
        style="카카오",
        topic="해시/조합",
        type="func",
        func_name="solution",
        description=(
            "스파이는 매일 서로 다른 옷의 조합으로 변장한다. 같은 종류(예: 모자, 안경)의 옷은 "
            "하루에 한 개만 착용할 수 있고, 각 종류는 입거나 입지 않을 수 있다. 단, 아무것도 "
            "입지 않는 경우는 제외한다. 가진 의상 목록 clothes 가 주어질 때 서로 다른 옷 조합의 "
            "수를 반환하세요."
        ),
        input_desc=(
            "clothes : [옷이름, 종류] 쌍의 리스트 (1 ≤ len ≤ 30)\n"
            "각 옷이름은 고유하며, 종류는 같은 것이 여러 개 있을 수 있다."
        ),
        output_desc="서로 다른 의상 조합의 수(정수)",
        examples=[
            {"args": [[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"],
                       ["green_turban", "headgear"]]], "output": 5},
            {"args": [[["crow_mask", "face"], ["blue_sunglasses", "face"],
                       ["smoky_makeup", "face"]]], "output": 3},
        ],
        hints=[
            "각 옷을 따로 보지 말고 '종류별로 몇 개가 있는가'로 묶어 생각해 보세요. "
            "한 종류에서 고를 수 있는 선택지는 무엇무엇일까요?",
            "종류별 개수를 해시(딕셔너리)로 셉니다. 어떤 종류에 옷이 k개 있으면 그 종류의 "
            "선택지는 'k개 중 하나를 입거나, 안 입거나'로 (k+1)가지입니다.",
            "각 종류의 (개수+1)을 모두 곱하면 '아무것도 안 입는 경우'까지 포함된 전체 경우의 "
            "수입니다. 마지막에 1(아무것도 안 입은 경우)을 빼면 답입니다.",
        ],
        testcases=[
            {"args": [[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"],
                       ["green_turban", "headgear"]]], "expected": 5},
            {"args": [[["crow_mask", "face"], ["blue_sunglasses", "face"],
                       ["smoky_makeup", "face"]]], "expected": 3},
            {"args": [[["a", "top"]]], "expected": 1},
            {"args": [[["a", "x"], ["b", "x"], ["c", "y"], ["d", "y"]]], "expected": 8},
        ],
        reference_py=(
            "from collections import Counter\n"
            "def solution(clothes):\n"
            "    cnt = Counter(kind for _, kind in clothes)\n"
            "    answer = 1\n"
            "    for v in cnt.values():\n"
            "        answer *= (v + 1)\n"
            "    return answer - 1\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int solution(String[][] clothes) {\n"
            "        HashMap<String, Integer> map = new HashMap<>();\n"
            "        for (String[] c : clothes) map.put(c[1], map.getOrDefault(c[1], 0) + 1);\n"
            "        int answer = 1;\n"
            "        for (int v : map.values()) answer *= (v + 1);\n"
            "        return answer - 1;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 서로 다른 의상 조합의 수를 반환하세요.\n"
            "def solution(clothes):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

]
