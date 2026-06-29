"""정렬 유형별 실전 문제 (sort-01 ~ sort-04).

대한민국 대기업 코딩테스트의 정렬 실전 감각을 위한 모음.
"""

from engine.models import Problem

CATEGORY = "정렬"

PROBLEMS = [

    # ────────────────────────────────────────────────────────────
    Problem(
        id="sort-01",
        rank="Silver",
        title="파일명 자연 정렬",
        style="카카오",
        topic="문자열 파싱 + 다중 키 정렬",
        category="정렬",
        type="func",
        func_name="solution",
        description=(
            "운영체제가 파일 목록을 보여줄 때, 사람은 \"img10\" 보다 \"img2\" 가 앞에 오기를 "
            "기대한다. 일반적인 사전 정렬은 문자 단위로 비교하기 때문에 \"img10\" 이 "
            "\"img2\" 보다 앞에 와 버린다. 이를 자연스럽게 정렬하기 위해 각 파일명을 세 "
            "부분으로 나누어 비교한다.\n\n"
            "  - HEAD : 파일명 맨 앞에서 시작하여 '숫자가 아닌' 문자들이 이어지는 부분. "
            "숫자가 처음 나오기 직전까지다.\n"
            "  - NUMBER : HEAD 바로 뒤에서 시작하여 '숫자'가 이어지는 부분. 최대 5글자까지만 "
            "NUMBER로 인정하며, 그 뒤의 문자는 모두 TAIL이다. NUMBER는 반드시 한 글자 이상 "
            "존재한다.\n"
            "  - TAIL : NUMBER 뒤의 나머지 전부(없을 수도 있다).\n\n"
            "정렬 규칙은 다음과 같다.\n"
            "  1) HEAD를 '대소문자 구분 없이' 사전순으로 비교한다.\n"
            "  2) HEAD가 같으면 NUMBER를 '정수 값'으로 비교한다(앞에 0이 붙어도 값으로 본다).\n"
            "  3) HEAD와 NUMBER가 모두 같으면, 원래 입력에 주어진 순서를 그대로 유지한다(안정 정렬).\n\n"
            "파일명 리스트 files 가 주어질 때, 위 규칙으로 정렬한 파일명 리스트를 반환하라. "
            "각 파일명에는 NUMBER로 인정될 숫자가 반드시 하나 이상 들어 있다."
        ),
        input_desc="files : 파일명 문자열 리스트 (각 파일명에는 숫자가 1개 이상 포함됨)",
        output_desc="규칙에 따라 정렬된 파일명 문자열 리스트.",
        examples=[
            {"args": [["img12.png", "img10.png", "img02.png", "img1.png",
                       "IMG01.GIF", "img2.JPG", "IMG3.jpg"]],
             "output": ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG",
                        "IMG3.jpg", "img10.png", "img12.png"]},
            {"args": [["F-5 Freedom Fighter", "B-50 Superfortress",
                       "A-10 Thunderbolt II", "F-14 Tomcat"]],
             "output": ["A-10 Thunderbolt II", "B-50 Superfortress",
                        "F-5 Freedom Fighter", "F-14 Tomcat"]},
        ],
        hints=[
            "각 파일명을 (HEAD, NUMBER) 키로 변환한 뒤 그 키로 정렬하면 됩니다. 파이썬의 sorted 는 안정 정렬이라 키가 같으면 원래 순서가 유지됩니다.",
            "문자를 앞에서부터 훑으며 isdigit() 으로 HEAD/NUMBER 경계를 찾으세요. HEAD는 .lower() 로 소문자화하고, NUMBER는 int() 로 정수 변환합니다. NUMBER는 최대 5글자까지만 모읍니다.",
            "def key(f): head 모으기(숫자 아닐 동안), num 모으기(숫자이고 len<5 동안). return (head.lower(), int(num)). return sorted(files, key=key).",
        ],
        testcases=[
            {"args": [["img12.png", "img10.png", "img02.png", "img1.png",
                       "IMG01.GIF", "img2.JPG", "IMG3.jpg"]],
             "expected": ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG",
                          "IMG3.jpg", "img10.png", "img12.png"]},
            {"args": [["F-5 Freedom Fighter", "B-50 Superfortress",
                       "A-10 Thunderbolt II", "F-14 Tomcat"]],
             "expected": ["A-10 Thunderbolt II", "B-50 Superfortress",
                          "F-5 Freedom Fighter", "F-14 Tomcat"]},
            {"args": [["foo9.txt", "foo10.txt", "foo1.txt", "bar2.dat", "bar10.dat"]],
             "expected": ["bar2.dat", "bar10.dat", "foo1.txt", "foo9.txt", "foo10.txt"]},
            {"args": [["a1"]], "expected": ["a1"]},
            {"args": [["file00001", "file1", "file001"]],
             "expected": ["file00001", "file1", "file001"]},
        ],
        reference_py=(
            "def solution(files):\n"
            "    def key(f):\n"
            "        head = ''\n"
            "        i = 0\n"
            "        while i < len(f) and not f[i].isdigit():\n"
            "            head += f[i]\n"
            "            i += 1\n"
            "        num = ''\n"
            "        while i < len(f) and f[i].isdigit() and len(num) < 5:\n"
            "            num += f[i]\n"
            "            i += 1\n"
            "        return (head.lower(), int(num))\n"
            "    return sorted(files, key=key)\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public String[] solution(String[] files) {\n"
            "        String[] arr = files.clone();\n"
            "        Arrays.sort(arr, (a, b) -> {\n"
            "            Object[] ka = key(a), kb = key(b);\n"
            "            int c = ((String) ka[0]).compareTo((String) kb[0]);\n"
            "            if (c != 0) return c;\n"
            "            return Integer.compare((Integer) ka[1], (Integer) kb[1]);\n"
            "        });\n"
            "        return arr;\n"
            "    }\n"
            "    private Object[] key(String f) {\n"
            "        int i = 0;\n"
            "        StringBuilder head = new StringBuilder();\n"
            "        while (i < f.length() && !Character.isDigit(f.charAt(i))) head.append(f.charAt(i++));\n"
            "        StringBuilder num = new StringBuilder();\n"
            "        while (i < f.length() && Character.isDigit(f.charAt(i)) && num.length() < 5) num.append(f.charAt(i++));\n"
            "        return new Object[]{head.toString().toLowerCase(), Integer.parseInt(num.toString())};\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 파일명 자연 정렬: (HEAD 소문자, NUMBER 정수) 키로 안정 정렬\n"
            "def solution(files):\n"
            "    answer = files\n"
            "    return answer\n"
        ),
    ),

    # ────────────────────────────────────────────────────────────
    Problem(
        id="sort-02",
        rank="Silver",
        title="로그 데이터 재정렬",
        style="라인",
        topic="조건부 안정 정렬",
        category="정렬",
        type="func",
        func_name="solution",
        description=(
            "서버 로그 한 줄은 \"식별자 내용\" 형식의 문자열이다. 식별자는 맨 앞 공백 전까지의 "
            "토큰이고, 그 뒤가 내용이다. 로그는 내용의 첫 글자에 따라 두 종류로 나뉜다.\n\n"
            "  - 문자 로그(letter-log) : 내용이 알파벳 소문자로 시작하는 로그.\n"
            "  - 숫자 로그(digit-log) : 내용이 숫자로 시작하는 로그.\n\n"
            "다음 규칙에 따라 로그를 재정렬하라.\n"
            "  1) 모든 문자 로그가 모든 숫자 로그보다 앞에 온다.\n"
            "  2) 문자 로그끼리는 '내용'을 기준으로 사전순 정렬한다. 내용이 완전히 같으면 "
            "'식별자'를 기준으로 사전순 정렬한다.\n"
            "  3) 숫자 로그끼리는 입력에 주어진 원래 순서를 그대로 유지한다.\n\n"
            "각 로그는 식별자 뒤에 공백이 하나 있고, 그 뒤에 공백으로 구분된 단어가 하나 이상 "
            "이어진다. 로그 리스트 logs 가 주어질 때, 위 규칙으로 재정렬한 리스트를 반환하라."
        ),
        input_desc="logs : \"식별자 내용\" 형식의 로그 문자열 리스트",
        output_desc="규칙에 따라 재정렬된 로그 문자열 리스트.",
        examples=[
            {"args": [["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
                       "let2 own kit dig", "let3 art zero"]],
             "output": ["let1 art can", "let3 art zero", "let2 own kit dig",
                        "dig1 8 1 5 1", "dig2 3 6"]},
            {"args": [["a1 9 2 3 1", "g1 act car", "zo4 4 7",
                       "ab1 off key dog", "a8 act zoo"]],
             "output": ["g1 act car", "a8 act zoo", "ab1 off key dog",
                        "a1 9 2 3 1", "zo4 4 7"]},
        ],
        hints=[
            "로그를 식별자와 내용으로 한 번만 나누고(첫 공백 기준), 내용의 첫 글자가 숫자인지로 두 그룹으로 분리하세요.",
            "문자 로그는 (내용, 식별자) 튜플을 키로 정렬하면 규칙 2가 그대로 충족됩니다. 숫자 로그는 정렬하지 말고 원래 순서대로 뒤에 붙이세요.",
            "letters=[], digits=[]; 각 로그를 split(' ',1)로 (식별자, 내용)으로 나눔; 내용[0].isdigit()이면 digits에 원본 추가, 아니면 letters에 (내용,식별자,원본) 추가; letters.sort(key=lambda x:(x[0],x[1])); 반환 = [원본 for letters] + digits.",
        ],
        testcases=[
            {"args": [["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
                       "let2 own kit dig", "let3 art zero"]],
             "expected": ["let1 art can", "let3 art zero", "let2 own kit dig",
                          "dig1 8 1 5 1", "dig2 3 6"]},
            {"args": [["a1 9 2 3 1", "g1 act car", "zo4 4 7",
                       "ab1 off key dog", "a8 act zoo"]],
             "expected": ["g1 act car", "a8 act zoo", "ab1 off key dog",
                          "a1 9 2 3 1", "zo4 4 7"]},
            {"args": [["log1 5 3 1", "log2 2 8 6"]],
             "expected": ["log1 5 3 1", "log2 2 8 6"]},
            {"args": [["x1 apple", "y2 apple"]],
             "expected": ["x1 apple", "y2 apple"]},
            {"args": [["id3 zoo", "id1 bee bee", "id2 bee bee"]],
             "expected": ["id1 bee bee", "id2 bee bee", "id3 zoo"]},
        ],
        reference_py=(
            "def solution(logs):\n"
            "    letters = []\n"
            "    digits = []\n"
            "    for lg in logs:\n"
            "        ident, rest = lg.split(' ', 1)\n"
            "        if rest[0].isdigit():\n"
            "            digits.append(lg)\n"
            "        else:\n"
            "            letters.append((rest, ident, lg))\n"
            "    letters.sort(key=lambda x: (x[0], x[1]))\n"
            "    return [x[2] for x in letters] + digits\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public String[] solution(String[] logs) {\n"
            "        List<String> letters = new ArrayList<>();\n"
            "        List<String> digits = new ArrayList<>();\n"
            "        for (String lg : logs) {\n"
            "            int sp = lg.indexOf(' ');\n"
            "            String rest = lg.substring(sp + 1);\n"
            "            if (Character.isDigit(rest.charAt(0))) digits.add(lg);\n"
            "            else letters.add(lg);\n"
            "        }\n"
            "        letters.sort((a, b) -> {\n"
            "            String ra = a.substring(a.indexOf(' ') + 1);\n"
            "            String rb = b.substring(b.indexOf(' ') + 1);\n"
            "            int c = ra.compareTo(rb);\n"
            "            if (c != 0) return c;\n"
            "            String ia = a.substring(0, a.indexOf(' '));\n"
            "            String ib = b.substring(0, b.indexOf(' '));\n"
            "            return ia.compareTo(ib);\n"
            "        });\n"
            "        List<String> res = new ArrayList<>(letters);\n"
            "        res.addAll(digits);\n"
            "        return res.toArray(new String[0]);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 로그 재정렬: 문자 로그(내용,식별자 순) 먼저, 숫자 로그는 원래 순서로\n"
            "def solution(logs):\n"
            "    answer = []\n"
            "    return answer\n"
        ),
    ),

    # ────────────────────────────────────────────────────────────
    Problem(
        id="sort-03",
        rank="Silver",
        title="성적표 다중 기준 정렬",
        style="현대",
        topic="다중 키 정렬",
        category="정렬",
        type="stdin",
        description=(
            "N명의 학생이 국어, 영어, 수학 점수를 받았다. 다음 우선순위 기준에 따라 학생을 "
            "정렬한 뒤 이름을 차례대로 출력하려 한다.\n\n"
            "  1) 국어 점수가 '높은' 순서(내림차순)로 정렬한다.\n"
            "  2) 국어 점수가 같으면 영어 점수가 '낮은' 순서(오름차순)로 정렬한다.\n"
            "  3) 국어, 영어 점수가 모두 같으면 수학 점수가 '높은' 순서(내림차순)로 정렬한다.\n"
            "  4) 세 점수가 모두 같으면 이름을 사전순(오름차순)으로 정렬한다. 이름이 같은 "
            "학생은 없다.\n\n"
            "각 점수는 0 이상 100 이하의 정수이며, 이름은 알파벳으로만 이루어진다. 위 기준에 "
            "따라 정렬한 결과에서 학생들의 이름을 한 줄에 하나씩 출력하라."
        ),
        input_desc=(
            "첫째 줄에 학생 수 N (1 ≤ N ≤ 100000).\n"
            "다음 N개의 줄에 '이름 국어 영어 수학' 이 공백으로 구분되어 주어진다."
        ),
        output_desc="정렬 기준에 따라 정렬한 학생들의 이름을 한 줄에 하나씩 출력.",
        examples=[
            {"input": ("12\nJunkyu 50 60 100\nSangkeun 80 60 50\nSunyoung 80 70 100\n"
                       "Soong 50 60 90\nHaebin 50 60 100\nKangsoo 60 80 100\n"
                       "Hanuel 80 80 80\nPangja 90 90 90\nDoyeon 70 70 70\n"
                       "Wonseob 70 70 90\nSangwoo 80 60 100\nSunwoong 80 60 80\n"),
             "output": ("Pangja\nSangwoo\nSunwoong\nSangkeun\nSunyoung\nHanuel\n"
                        "Wonseob\nDoyeon\nKangsoo\nHaebin\nJunkyu\nSoong\n")},
            {"input": "3\nAlice 90 50 50\nBob 90 50 60\nCara 90 50 50\n",
             "output": "Bob\nAlice\nCara\n"},
        ],
        hints=[
            "여러 기준이 섞여 있을 때는 하나의 정렬 키 튜플로 만들면 깔끔합니다. 오름차순 기준은 값을 그대로, 내림차순 기준은 값에 음수를 붙이면 됩니다.",
            "각 학생을 (이름, 국어, 영어, 수학)으로 읽고, key=(-국어, 영어, -수학, 이름) 튜플로 정렬하세요. 입력이 크니 sys.stdin 으로 한 번에 읽는 게 좋습니다.",
            "arr.sort(key=lambda s: (-s[1], s[2], -s[3], s[0])) 로 정렬한 뒤 이름들을 줄바꿈으로 이어 출력. 국어는 내림(-), 영어는 오름(+), 수학은 내림(-), 이름은 오름(+).",
        ],
        testcases=[
            {"input": ("12\nJunkyu 50 60 100\nSangkeun 80 60 50\nSunyoung 80 70 100\n"
                       "Soong 50 60 90\nHaebin 50 60 100\nKangsoo 60 80 100\n"
                       "Hanuel 80 80 80\nPangja 90 90 90\nDoyeon 70 70 70\n"
                       "Wonseob 70 70 90\nSangwoo 80 60 100\nSunwoong 80 60 80\n"),
             "output": ("Pangja\nSangwoo\nSunwoong\nSangkeun\nSunyoung\nHanuel\n"
                        "Wonseob\nDoyeon\nKangsoo\nHaebin\nJunkyu\nSoong\n")},
            {"input": "3\nAlice 90 50 50\nBob 90 50 60\nCara 90 50 50\n",
             "output": "Bob\nAlice\nCara\n"},
            {"input": "1\nSolo 100 100 100\n", "output": "Solo\n"},
            {"input": "4\nDd 70 70 70\nAa 70 70 70\nCc 70 70 70\nBb 70 70 70\n",
             "output": "Aa\nBb\nCc\nDd\n"},
            {"input": "2\nLow 0 100 0\nHigh 100 0 100\n", "output": "High\nLow\n"},
        ],
        reference_py=(
            "import sys\n"
            "def main():\n"
            "    data = sys.stdin.read().split('\\n')\n"
            "    n = int(data[0])\n"
            "    arr = []\n"
            "    for i in range(1, n + 1):\n"
            "        name, k, e, m = data[i].split()\n"
            "        arr.append((name, int(k), int(e), int(m)))\n"
            "    arr.sort(key=lambda s: (-s[1], s[2], -s[3], s[0]))\n"
            "    sys.stdout.write('\\n'.join(s[0] for s in arr) + '\\n')\n"
            "main()\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        int n = Integer.parseInt(br.readLine().trim());\n"
            "        String[][] arr = new String[n][];\n"
            "        for (int i = 0; i < n; i++) arr[i] = br.readLine().split(\" \");\n"
            "        Arrays.sort(arr, (a, b) -> {\n"
            "            int ka = Integer.parseInt(a[1]), kb = Integer.parseInt(b[1]);\n"
            "            if (ka != kb) return kb - ka;\n"
            "            int ea = Integer.parseInt(a[2]), eb = Integer.parseInt(b[2]);\n"
            "            if (ea != eb) return ea - eb;\n"
            "            int ma = Integer.parseInt(a[3]), mb = Integer.parseInt(b[3]);\n"
            "            if (ma != mb) return mb - ma;\n"
            "            return a[0].compareTo(b[0]);\n"
            "        });\n"
            "        StringBuilder sb = new StringBuilder();\n"
            "        for (String[] s : arr) sb.append(s[0]).append('\\n');\n"
            "        System.out.print(sb);\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "import sys\n"
            "def main():\n"
            "    data = sys.stdin.read().split('\\n')\n"
            "    # N명을 읽어 (이름,국어,영어,수학)으로 만들고 다중 키로 정렬\n"
            "    pass\n"
            "main()\n"
        ),
    ),

    # ────────────────────────────────────────────────────────────
    Problem(
        id="sort-04",
        rank="Silver",
        title="외계어 사전 순서 정렬",
        style="쿠팡",
        topic="커스텀 우선순위 정렬",
        category="정렬",
        type="func",
        func_name="solution",
        description=(
            "어떤 외계 문명은 우리와 같은 26개의 알파벳 소문자를 쓰지만, 글자의 '순서'가 "
            "다르다. 그들의 사전 순서는 길이 26짜리 문자열 order 로 주어지며, order 의 앞에 "
            "있는 글자일수록 사전에서 먼저 온다(order 에는 'a'~'z' 가 한 번씩 모두 등장한다).\n\n"
            "이 외계어 사전 순서에 따라 단어 목록 words 를 오름차순으로 정렬하라. 두 단어를 "
            "비교할 때는 앞 글자부터 차례로 비교하되, 각 글자의 우열은 order 에서의 위치로 "
            "판단한다. 한 단어가 다른 단어의 접두사인 경우(예: 한 단어가 비교 중 먼저 끝난 "
            "경우)에는 더 짧은 단어가 앞에 온다.\n\n"
            "정렬 결과는 유일하며, 같은 단어가 여러 번 주어질 수 있다(이 경우 그대로 둔다). "
            "정렬된 단어 리스트를 반환하라."
        ),
        input_desc=(
            "words : 알파벳 소문자로 이루어진 단어 문자열 리스트.\n"
            "order : 'a'~'z' 가 한 번씩 등장하는 길이 26의 문자열(외계어 사전 순서)."
        ),
        output_desc="order 기준으로 오름차순 정렬된 단어 리스트.",
        examples=[
            {"args": [["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"],
             "output": ["world", "word", "row"]},
            {"args": [["apple", "app", "banana"], "abcdefghijklmnopqrstuvwxyz"],
             "output": ["app", "apple", "banana"]},
        ],
        hints=[
            "order 에서 각 글자가 몇 번째에 있는지를 미리 표(딕셔너리)로 만들어 두면, 글자 비교를 위치 숫자 비교로 바꿀 수 있습니다.",
            "단어를 '각 글자의 order 내 위치 리스트'로 변환해 그 리스트를 정렬 키로 쓰면, 리스트 비교 규칙이 자연스럽게 접두사 처리(짧은 쪽이 앞)까지 해결해 줍니다.",
            "idx = {c: i for i, c in enumerate(order)}; return sorted(words, key=lambda w: [idx[c] for c in w]).",
        ],
        testcases=[
            {"args": [["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"],
             "expected": ["world", "word", "row"]},
            {"args": [["apple", "app", "banana"], "abcdefghijklmnopqrstuvwxyz"],
             "expected": ["app", "apple", "banana"]},
            {"args": [["a", "b", "c"], "zyxwvutsrqponmlkjihgfedcba"],
             "expected": ["c", "b", "a"]},
            {"args": [["kgf", "kf", "k"], "kgfabcdehijlmnopqrstuvwxyz"],
             "expected": ["k", "kgf", "kf"]},
            {"args": [["zz", "zz"], "abcdefghijklmnopqrstuvwxyz"],
             "expected": ["zz", "zz"]},
        ],
        reference_py=(
            "def solution(words, order):\n"
            "    idx = {c: i for i, c in enumerate(order)}\n"
            "    return sorted(words, key=lambda w: [idx[c] for c in w])\n"
        ),
        reference_java=(
            "import java.util.*;\n"
            "class Solution {\n"
            "    public String[] solution(String[] words, String order) {\n"
            "        int[] idx = new int[128];\n"
            "        for (int i = 0; i < order.length(); i++) idx[order.charAt(i)] = i;\n"
            "        String[] arr = words.clone();\n"
            "        Arrays.sort(arr, (a, b) -> {\n"
            "            int n = Math.min(a.length(), b.length());\n"
            "            for (int i = 0; i < n; i++) {\n"
            "                int ca = idx[a.charAt(i)], cb = idx[b.charAt(i)];\n"
            "                if (ca != cb) return ca - cb;\n"
            "            }\n"
            "            return a.length() - b.length();\n"
            "        });\n"
            "        return arr;\n"
            "    }\n"
            "}\n"
        ),
        template_py=(
            "# 외계어 사전 순서로 단어 정렬\n"
            "def solution(words, order):\n"
            "    answer = words\n"
            "    return answer\n"
        ),
    ),

]
