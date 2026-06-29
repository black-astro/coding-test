"""유형별 실전 — 그리디.

구명보트 / 체육복 / 단속카메라 / 회의실 배정.
각 문제는 '왜 이 그리디 선택이 최적인지'가 드러나도록 작성했다.
"""

from engine.models import Problem

CATEGORY = "그리디"

PROBLEMS = [

    Problem(
        id="greedy-01",
        rank="Silver",
        title="구명보트",
        style="프로그래머스",
        topic="그리디",
        type="func",
        func_name="solution",
        description=(
            "무인도에 갇힌 사람들을 구명보트로 구출한다. 보트 한 척에는 최대 2명만 탈 수 있고, "
            "두 사람 몸무게의 합이 보트 한도 limit 를 넘으면 안 된다. 사람들의 몸무게 배열 people 와 "
            "보트 한도 limit 가 주어질 때, 모두를 구출하는 데 필요한 최소 보트 수를 반환하세요.\n\n"
            "[왜 그리디가 최적인가] 가장 무거운 사람은 어차피 누군가와 짝을 짓거나 혼자 타야 한다. "
            "이때 '가장 가벼운 사람'과 짝지어 보지 못하면 다른 누구와도 짝지을 수 없다. "
            "즉 가장 무거운 사람을 가장 가벼운 사람과 맞춰보는 것이 항상 손해가 없으므로, "
            "양 끝에서 좁혀가는 선택이 전체 최적해를 만든다."
        ),
        input_desc="people : 1명당 몸무게 정수 리스트, limit : 보트 한 척의 무게 한도(정수)",
        output_desc="모두 구출하는 데 필요한 최소 보트 수(정수)",
        examples=[
            {"args": [[70, 50, 80, 50], 100], "output": 3},
            {"args": [[70, 80, 50], 100], "output": 3},
        ],
        hints=[
            "가장 무거운 사람부터 생각하세요. 그와 함께 태울 수 있는 사람은 '가장 가벼운 사람' 하나뿐일 수도 있습니다.",
            "정렬 후 투 포인터(양 끝)를 쓰세요. 가장 가벼운 사람 l 과 가장 무거운 사람 r 의 합이 limit 이하면 둘을 함께 태웁니다.",
            "people.sort(); l,r=0,n-1; while l<=r: if people[l]+people[r]<=limit: l+=1; r-=1; boats+=1",
        ],
        testcases=[
            {"args": [[70, 50, 80, 50], 100], "expected": 3},
            {"args": [[70, 80, 50], 100], "expected": 3},
            {"args": [[40], 100], "expected": 1},
            {"args": [[100, 100], 100], "expected": 2},
            {"args": [[30, 30, 30, 30], 100], "expected": 2},
        ],
        reference_py=(
            "def solution(people, limit):\n"
            "    people.sort()\n"
            "    l, r = 0, len(people) - 1\n"
            "    boats = 0\n"
            "    while l <= r:\n"
            "        if people[l] + people[r] <= limit:\n"
            "            l += 1\n"
            "        r -= 1\n"
            "        boats += 1\n"
            "    return boats\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int solution(int[] people, int limit) {\n"
            "        Arrays.sort(people);\n"
            "        int l = 0, r = people.length - 1, boats = 0;\n"
            "        while (l <= r) {\n"
            "            if (people[l] + people[r] <= limit) l++;\n"
            "            r--;\n"
            "            boats++;\n"
            "        }\n"
            "        return boats;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 구명보트 : 최소 보트 수 (정렬 + 투 포인터 그리디)\n"
            "def solution(people, limit):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="greedy-02",
        rank="Silver",
        title="체육복",
        style="카카오",
        topic="그리디",
        type="func",
        func_name="solution",
        description=(
            "체육 수업을 듣는 학생 n 명 중 일부는 체육복을 도난당했고(lost), 일부는 여벌을 가져왔다(reserve). "
            "여벌이 있는 학생은 자신의 바로 앞 번호 또는 바로 뒤 번호 학생에게만 빌려줄 수 있다. "
            "단, 도난당했지만 여벌도 있는 학생은 빌려줄 수 없다(자기 것을 입어야 함). "
            "체육 수업을 들을 수 있는 학생의 최댓값을 반환하세요.\n\n"
            "[왜 그리디가 최적인가] 여벌을 가진 학생은 '앞 번호부터 먼저' 빌려주는 것이 최적이다. "
            "만약 앞 번호 학생도 도난, 뒤 번호 학생도 도난이라면, 더 작은 번호에게 먼저 주어야 "
            "그 다음 여벌 학생이 자신의 뒤 번호를 구제할 여지를 남긴다. 번호 순으로 처리하면 "
            "지역적 최선이 곧 전체 최선이 된다."
        ),
        input_desc="n : 전체 학생 수, lost : 도난당한 학생 번호 리스트, reserve : 여벌이 있는 학생 번호 리스트",
        output_desc="체육 수업을 들을 수 있는 학생 수의 최댓값(정수)",
        examples=[
            {"args": [5, [2, 4], [1, 3, 5]], "output": 5},
            {"args": [5, [2, 4], [3]], "output": 4},
        ],
        hints=[
            "도난당했지만 여벌도 있는 학생은 남에게 빌려줄 수 없고 자기 것을 입습니다. 먼저 이 교집합을 걸러내세요.",
            "여벌 학생을 번호 오름차순으로 보며, 앞 번호(r-1)가 부족하면 먼저 주고, 아니면 뒤 번호(r+1)에게 줍니다.",
            "lost-={reserve}; reserve-={lost}; for r in sorted(reserve): if r-1 in lost: lost.remove(r-1) elif r+1 in lost: lost.remove(r+1). 답 = n - 남은 lost 수",
        ],
        testcases=[
            {"args": [5, [2, 4], [1, 3, 5]], "expected": 5},
            {"args": [5, [2, 4], [3]], "expected": 4},
            {"args": [3, [3], [1]], "expected": 2},
            {"args": [5, [1, 2, 3, 4, 5], [1]], "expected": 1},
            {"args": [4, [2, 3], [1, 2, 3, 4]], "expected": 4},
        ],
        reference_py=(
            "def solution(n, lost, reserve):\n"
            "    lost_set = set(lost) - set(reserve)\n"
            "    reserve_set = set(reserve) - set(lost)\n"
            "    answer = n - len(lost_set)\n"
            "    for r in sorted(reserve_set):\n"
            "        if r - 1 in lost_set:\n"
            "            lost_set.remove(r - 1)\n"
            "            answer += 1\n"
            "        elif r + 1 in lost_set:\n"
            "            lost_set.remove(r + 1)\n"
            "            answer += 1\n"
            "    return answer\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public int solution(int n, int[] lost, int[] reserve) {\n"
            "        Set<Integer> lostSet = new TreeSet<>();\n"
            "        Set<Integer> resSet = new TreeSet<>();\n"
            "        for (int x : lost) lostSet.add(x);\n"
            "        for (int x : reserve) resSet.add(x);\n"
            "        Set<Integer> both = new HashSet<>(lostSet);\n"
            "        both.retainAll(resSet);\n"
            "        lostSet.removeAll(both);\n"
            "        resSet.removeAll(both);\n"
            "        int answer = n - lostSet.size();\n"
            "        for (int r : resSet) {\n"
            "            if (lostSet.remove(r - 1)) answer++;\n"
            "            else if (lostSet.remove(r + 1)) answer++;\n"
            "        }\n"
            "        return answer;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 체육복 : 수업 들을 수 있는 학생 최댓값 (번호순 그리디)\n"
            "def solution(n, lost, reserve):\n"
            "    answer = 0\n"
            "    return answer\n"
        ),
    ),

    Problem(
        id="greedy-03",
        rank="Gold",
        title="고속도로 단속카메라 최소 설치",
        style="소프티어",
        topic="그리디",
        type="stdin",
        description=(
            "일직선 고속도로를 달리는 차량 n 대가 있다. 각 차량 i 는 진입 지점 s_i 에서 진출 지점 e_i 까지 "
            "주행한다(s_i ≤ e_i). 도로 위 한 지점에 단속카메라를 설치하면, 그 지점을 주행 구간에 포함하는 "
            "모든 차량을 동시에 단속할 수 있다. 모든 차량을 최소 한 번씩 단속하기 위해 필요한 카메라의 "
            "최소 개수를 구하시오.\n\n"
            "[왜 그리디가 최적인가] 진출 지점(e)이 가장 빠른 차량을 먼저 단속해야 한다. 그 차량을 "
            "단속할 카메라는 늦어도 그 차량의 e 지점에 두어야 하며, e 보다 더 뒤에 두면 그 차량을 "
            "놓친다. 카메라를 '가장 이른 e' 위치에 두면 같은 카메라가 커버할 수 있는 다른 차량이 "
            "최대로 많아지므로, 진출 순 정렬 후 탐욕적으로 두는 것이 최소 개수를 보장한다."
        ),
        input_desc=(
            "첫째 줄에 차량 수 n (1 ≤ n ≤ 10000). 다음 n개의 줄에 각 차량의 진입 지점 s 와 진출 지점 e "
            "(-30000 ≤ s ≤ e ≤ 30000)가 공백으로 주어진다."
        ),
        output_desc="모든 차량을 단속하는 데 필요한 카메라의 최소 개수를 한 줄에 출력.",
        examples=[
            {"input": "4\n-20 -15\n-14 -5\n-18 -13\n-5 -3\n", "output": "2\n"},
            {"input": "3\n0 1\n2 3\n4 5\n", "output": "3\n"},
        ],
        hints=[
            "구간들을 '끝나는 지점(e)' 기준으로 정렬한 뒤, 아직 단속되지 않은 가장 이른 구간의 끝에 카메라를 두는 장면을 그려 보세요.",
            "진출 지점 e 오름차순 정렬 후, 마지막으로 설치한 카메라 위치 last 를 추적합니다. 현재 차량의 s 가 last 보다 크면 새 카메라가 필요합니다.",
            "routes.sort(key=lambda x:x[1]); last=-30001; for s,e in routes: if s>last: cnt+=1; last=e",
        ],
        testcases=[
            {"input": "4\n-20 -15\n-14 -5\n-18 -13\n-5 -3\n", "output": "2\n"},
            {"input": "3\n0 1\n2 3\n4 5\n", "output": "3\n"},
            {"input": "1\n0 5\n", "output": "1\n"},
            {"input": "3\n0 10\n1 2\n3 4\n", "output": "2\n"},
            {"input": "5\n-30000 30000\n-1 0\n0 1\n100 200\n150 250\n", "output": "2\n"},
        ],
        reference_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "n = int(input())\n"
            "routes = [tuple(map(int, input().split())) for _ in range(n)]\n"
            "routes.sort(key=lambda x: x[1])\n"
            "cnt = 0\n"
            "last = -30001\n"
            "for s, e in routes:\n"
            "    if s > last:\n"
            "        cnt += 1\n"
            "        last = e\n"
            "print(cnt)\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        int n = Integer.parseInt(br.readLine().trim());\n"
            "        int[][] r = new int[n][2];\n"
            "        for (int i = 0; i < n; i++) {\n"
            "            StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "            r[i][0] = Integer.parseInt(st.nextToken());\n"
            "            r[i][1] = Integer.parseInt(st.nextToken());\n"
            "        }\n"
            "        Arrays.sort(r, (a, b) -> Integer.compare(a[1], b[1]));\n"
            "        int cnt = 0, last = -30001;\n"
            "        for (int[] c : r) {\n"
            "            if (c[0] > last) { cnt++; last = c[1]; }\n"
            "        }\n"
            "        System.out.println(cnt);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "# 단속카메라 최소 개수 (진출 지점 정렬 그리디)\n"
            "n = int(input())\n"
            "# ...\n"
        ),
    ),

    Problem(
        id="greedy-04",
        rank="Silver",
        title="회의실 배정 최대 개수",
        style="삼성",
        topic="그리디",
        type="stdin",
        description=(
            "하나의 회의실에 n 개의 회의가 신청되었다. 각 회의는 시작 시각 s 와 끝 시각 e 를 가진다. "
            "한 회의가 끝남과 동시에 다음 회의를 시작할 수 있다(끝 시각 == 시작 시각 허용). "
            "회의실을 사용할 수 있는 회의의 최대 개수를 구하시오.\n\n"
            "[왜 그리디가 최적인가] '끝나는 시각이 가장 이른' 회의를 먼저 선택하는 것이 최적이다. "
            "가장 빨리 끝나는 회의를 고르면 남는 시간이 최대가 되어, 이후에 더 많은 회의를 넣을 "
            "여지를 남긴다. 같은 개수의 회의를 고르는 어떤 해도, 첫 회의를 '가장 빨리 끝나는 회의'로 "
            "바꿔도 손해가 없으므로(교환 논증) 끝 시각 정렬 후 탐욕 선택이 최댓값을 보장한다."
        ),
        input_desc=(
            "첫째 줄에 회의 수 n (1 ≤ n ≤ 100000). 다음 n개의 줄에 회의의 시작 시각 s 와 끝 시각 e "
            "(0 ≤ s ≤ e ≤ 2^31-1)가 공백으로 주어진다."
        ),
        output_desc="사용 가능한 회의의 최대 개수를 한 줄에 출력.",
        examples=[
            {"input": "11\n1 4\n3 5\n0 6\n5 7\n3 8\n5 9\n6 10\n8 11\n8 12\n2 13\n12 14\n", "output": "4\n"},
            {"input": "3\n1 3\n2 4\n3 5\n", "output": "2\n"},
        ],
        hints=[
            "끝 시각이 빠른 회의부터 고르면, 이후 회의를 넣을 시간이 가장 많이 남습니다. 끝 시각 기준 정렬을 떠올리세요.",
            "끝 시각 오름차순(같으면 시작 시각 오름차순)으로 정렬한 뒤, 현재 회의 시작 시각이 직전에 고른 회의의 끝 시각 이상이면 선택합니다.",
            "meets.sort(key=lambda x:(x[1],x[0])); end=0; for s,e in meets: if s>=end: cnt+=1; end=e",
        ],
        testcases=[
            {"input": "11\n1 4\n3 5\n0 6\n5 7\n3 8\n5 9\n6 10\n8 11\n8 12\n2 13\n12 14\n", "output": "4\n"},
            {"input": "3\n1 3\n2 4\n3 5\n", "output": "2\n"},
            {"input": "1\n5 5\n", "output": "1\n"},
            {"input": "3\n2 2\n2 2\n2 2\n", "output": "3\n"},
            {"input": "4\n0 1\n1 2\n2 3\n0 3\n", "output": "3\n"},
        ],
        reference_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "n = int(input())\n"
            "meets = [tuple(map(int, input().split())) for _ in range(n)]\n"
            "meets.sort(key=lambda x: (x[1], x[0]))\n"
            "cnt = 0\n"
            "end = 0\n"
            "for s, e in meets:\n"
            "    if s >= end:\n"
            "        cnt += 1\n"
            "        end = e\n"
            "print(cnt)\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        int n = Integer.parseInt(br.readLine().trim());\n"
            "        long[][] m = new long[n][2];\n"
            "        for (int i = 0; i < n; i++) {\n"
            "            StringTokenizer st = new StringTokenizer(br.readLine());\n"
            "            m[i][0] = Long.parseLong(st.nextToken());\n"
            "            m[i][1] = Long.parseLong(st.nextToken());\n"
            "        }\n"
            "        Arrays.sort(m, (a, b) -> a[1] != b[1] ? Long.compare(a[1], b[1]) : Long.compare(a[0], b[0]));\n"
            "        int cnt = 0; long end = 0;\n"
            "        for (long[] c : m) {\n"
            "            if (c[0] >= end) { cnt++; end = c[1]; }\n"
            "        }\n"
            "        System.out.println(cnt);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "input = sys.stdin.readline\n"
            "# 회의실 배정 : 최대 회의 수 (끝 시각 정렬 그리디)\n"
            "n = int(input())\n"
            "# ...\n"
        ),
    ),

]
