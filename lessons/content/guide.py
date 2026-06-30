"""환경 설정 가이드 — JDK / C++(g++) 설치·적용·사용법.

사이드바 'guide' 섹션에 표시된다. (lang="guide")
"""

from engine.models import Lesson

LESSONS = [

    Lesson(
        id="guide-00-overview",
        lang="guide", level="개요",
        title="이 프로그램과 언어 환경 한눈에",
        summary="Python은 바로 됨 · Java는 JDK · C++는 g++ 필요",
        explanation=(
            "이 프로그램은 Python / Java / C++ 코드를 직접 실행·채점합니다.\n"
            "각 언어를 '실제로 돌리려면' 해당 언어의 실행기(toolchain)가 필요합니다.\n\n"
            "● Python : 이 프로그램에 함께 들어있어 바로 됩니다(무설치판 기준).\n"
            "● Java   : JDK(자바 개발 키트)가 필요합니다. (javac=컴파일, java=실행)\n"
            "● C++    : g++(MinGW) 컴파일러가 필요합니다.\n\n"
            "현재 PC에 깔린 것을 자동으로 찾고, 무설치판에서는 프로그램 옆 runtime/ 폴더의\n"
            "toolchain 을 먼저 사용합니다. 없으면 그 언어 채점만 잠깁니다(프로그램은 정상)."
        ),
        usage="먼저 이 개요를 읽고, Java를 쓸 거면 'JDK 설치', C++를 쓸 거면 'g++ 설치'로 가세요.",
        cons="toolchain 이 없으면 해당 언어 실행/채점만 비활성화됩니다.",
        code="",
    ),

    Lesson(
        id="guide-01-jdk",
        lang="guide", level="설치",
        title="Java(JDK) 설치·적용",
        summary="Temurin/Oracle JDK 설치 후 javac/java 확인",
        explanation=(
            "JDK는 이 프로그램에 '기본 포함되어 있지 않습니다'.\n"
            "(무설치 배포판을 만들 때는 미니 JDK를 함께 넣을 수 있습니다 — BUILD.md 참고)\n\n"
            "[설치]\n"
            "1) https://adoptium.net (Eclipse Temurin) 접속 → JDK 21(LTS) 다운로드\n"
            "   또는 winget:  winget install EclipseAdoptium.Temurin.21.JDK\n"
            "2) 설치 시 'Add to PATH' / 'Set JAVA_HOME' 옵션을 체크.\n\n"
            "[적용 확인] 새 터미널(또는 이 프로그램 재시작) 후:\n"
            "   javac -version   → javac 21.x 처럼 나오면 OK\n"
            "   java -version    → openjdk 21.x\n\n"
            "[프로그램 적용] javac/java 가 PATH 에 잡히면 이 프로그램이 자동 인식합니다.\n"
            "상단 언어 토글에서 Java 선택 → 코드 작성 → Run."
        ),
        usage="설치 후 재시작하면 자동 적용. 무설치판은 runtime/jdk/ 에 넣으면 됨.",
        cons="32bit/구버전 JRE가 PATH에 먼저 있으면 충돌할 수 있어 최신 JDK 권장.",
        code="",
    ),

    Lesson(
        id="guide-02-gpp",
        lang="guide", level="설치",
        title="C++(g++/MinGW) 설치·적용",
        summary="MinGW-w64 설치 후 g++ 확인",
        explanation=(
            "C++ 실행에는 g++ 컴파일러가 필요합니다(현재 PC엔 없을 수 있음).\n\n"
            "[가장 쉬운 방법: WinLibs 포터블]\n"
            "1) https://winlibs.com 접속 → UCRT runtime, 최신 GCC 'Win64' zip 다운로드\n"
            "2) 압축 해제 → 안의 mingw64 폴더를 원하는 곳에 둠 (예: C:\\mingw64)\n"
            "3) 시스템 환경변수 PATH 에  C:\\mingw64\\bin  추가\n\n"
            "[또는 MSYS2]\n"
            "   winget install MSYS2.MSYS2  → MSYS2 셸에서\n"
            "   pacman -S mingw-w64-ucrt-x86_64-gcc\n\n"
            "[적용 확인] 새 터미널에서:\n"
            "   g++ --version   → g++ (GCC) 13.x 처럼 나오면 OK\n\n"
            "[프로그램 적용] g++ 가 PATH 에 잡히면 자동 인식. 무설치판은 runtime/mingw/ 에 넣으면 됨.\n"
            "이 프로그램은 -static 으로 컴파일해 DLL 없이도 결과가 돌아갑니다."
        ),
        usage="설치 후 재시작하면 상단 토글에서 C++ 선택해 Run 가능.",
        cons="용량이 큼(100~300MB). C++가 필요 없으면 안 깔아도 됩니다.",
        code="",
    ),

    Lesson(
        id="guide-03-java-howto",
        lang="guide", level="사용법",
        title="Java로 코딩테스트 푸는 법",
        summary="public class Main + BufferedReader 입력",
        explanation=(
            "이 프로그램의 Java 채점은 표준입출력(stdin/stdout) 기반이며,\n"
            "반드시 'public class Main' 과 main 메서드가 있어야 합니다.\n\n"
            "[기본 골격]\n"
            "  import java.util.*; import java.io.*;\n"
            "  public class Main {\n"
            "    public static void main(String[] a) throws IOException {\n"
            "      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "      int n = Integer.parseInt(br.readLine().trim());\n"
            "      // ... 풀이 ...\n"
            "      System.out.print(sb);   // 출력은 StringBuilder 로 모아 한 번에\n"
            "    }\n  }\n\n"
            "[팁] 입력이 많으면 Scanner 대신 BufferedReader+StringTokenizer, 출력은 StringBuilder.\n"
            "함수 구현형(프로그래머스식) 문제는 Java 채점이 안 되고 정답 코드만 참고합니다."
        ),
        usage="상단 토글 Java → 코드 작성 → Run(F5). 오른쪽 terminal 에 결과/시간/메모리.",
        cons="JVM 기동 때문에 실행 시간에 +100~200ms 가산됩니다(제한은 넉넉히 잡힘).",
        code=(
            "import java.util.*;\n"
            "import java.io.*;\n"
            "public class Main {\n"
            "    public static void main(String[] args) throws IOException {\n"
            "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
            "        // 예시: 한 줄에 두 수를 읽어 합 출력 (입력 없이 데모로 고정값 사용)\n"
            "        int a = 3, b = 5;\n"
            "        System.out.println(a + b);\n"
            "    }\n"
            "}\n"
        ),
    ),

    Lesson(
        id="guide-04-cpp-howto",
        lang="guide", level="사용법",
        title="C++로 코딩테스트 푸는 법",
        summary="bits/stdc++.h + 빠른 입출력",
        explanation=(
            "C++ 채점도 표준입출력 기반이고, 완전한 main 이 있는 프로그램이어야 합니다.\n\n"
            "[기본 골격]\n"
            "  #include <bits/stdc++.h>\n  using namespace std;\n"
            "  int main(){\n"
            "    ios_base::sync_with_stdio(false); cin.tie(nullptr);  // 빠른 입출력\n"
            "    int n; cin >> n;\n"
            "    // ... 풀이 ...\n"
            "    cout << ans << '\\n';\n"
            "    return 0;\n  }\n\n"
            "[팁] cin/cout 동기화 해제(sync_with_stdio(false))로 속도 확보. endl 대신 '\\n'.\n"
            "vector, sort, map, set, priority_queue 등 STL 적극 활용."
        ),
        usage="상단 토글 C++ → 코드 작성 → Run. (g++ 설치 필요)",
        cons="포인터/메모리 관리 실수 시 런타임 에러가 잦음. 인덱스 범위·오버플로(long long) 주의.",
        code=(
            "#include <bits/stdc++.h>\n"
            "using namespace std;\n"
            "int main(){\n"
            "    ios_base::sync_with_stdio(false); cin.tie(nullptr);\n"
            "    int a = 3, b = 5;   // 데모 고정값\n"
            "    cout << a + b << '\\n';\n"
            "    return 0;\n"
            "}\n"
        ),
    ),

    Lesson(
        id="guide-05-node",
        lang="guide", level="설치",
        title="JavaScript(Node.js) 설치·적용",
        summary="Node.js 설치 후 node 확인",
        explanation=(
            "JavaScript 채점에는 Node.js 런타임이 필요합니다(현재 PC엔 없을 수 있음).\n\n"
            "[설치]\n"
            "1) https://nodejs.org 접속 → LTS 버전 Windows Installer(.msi) 다운로드\n"
            "2) 설치 시 'Add to PATH' 옵션은 기본으로 켜져 있음 → 그대로 설치\n"
            "   (또는 winget install OpenJS.NodeJS.LTS)\n\n"
            "[적용 확인] 새 터미널에서:\n"
            "   node --version   → v20.x 처럼 나오면 OK\n\n"
            "[프로그램 적용] node 가 PATH 에 잡히면 자동 인식됩니다.\n"
            "설치 후 프로그램을 다시 켜면 상단 토글에서 JS 를 선택해 채점할 수 있습니다."
        ),
        usage="설치 후 재시작 → 상단 토글 JS 선택 → 코드 작성 → Run/제출.",
        cons="JS 가 필요 없으면 안 깔아도 되고, 그 경우 JS 채점만 비활성화됩니다.",
        code="",
    ),

    Lesson(
        id="guide-06-js-howto",
        lang="guide", level="사용법",
        title="JavaScript로 코딩테스트 푸는 법",
        summary="fs.readFileSync(0) 로 표준입력 읽기",
        explanation=(
            "이 프로그램의 JS 채점은 Node.js 기반이며 표준입출력(stdin/stdout)을 사용합니다.\n\n"
            "[입력 읽기] 브라우저의 prompt 가 아니라, 표준입력 전체를 한 번에 읽습니다.\n"
            "  const data = require('fs').readFileSync(0, 'utf8').trim();\n"
            "  const lines = data.split('\\n');          // 줄 단위\n"
            "  const [a, b] = lines[0].split(' ').map(Number);  // 공백 분리 → 숫자\n\n"
            "[출력] console.log 로 출력합니다.\n"
            "  console.log(a + b);\n\n"
            "[팁]\n"
            " - 숫자는 split 후 Number/parseInt 로 변환(문자열 + 문자열은 이어붙음 주의).\n"
            " - 입력이 많으면 lines 를 인덱스로 순회하거나, 한 줄을 split(' ')/map(Number).\n"
            " - 출력이 많으면 배열에 모아 console.log(arr.join('\\n')) 로 한 번에."
        ),
        usage="상단 토글 JS → 코드 작성 → Run(F5). 입력칸에 값 넣고 실행해 확인. (Node 설치 필요)",
        cons="함수 구현형 문제는 JS 채점이 안 되고, 표준입출력형만 채점됩니다.",
        code=(
            "// 표준입력 전체 읽기 (Node.js)\n"
            "const data = require('fs').readFileSync(0, 'utf8').trim();\n"
            "const lines = data.split('\\n');\n"
            "// 예: 첫 줄에 두 수가 공백으로 주어질 때\n"
            "const [a, b] = lines[0].split(' ').map(Number);\n"
            "console.log(a + b);\n"
        ),
    ),
]
