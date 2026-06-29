"""Python 기초 문법 (스타터 — 더 많은 항목은 추가 가능)."""

from engine.models import Lesson

LESSONS = [

    Lesson(
        id="py-basic-01-var",
        lang="python", level="기초",
        title="변수와 자료형",
        summary="동적 타입 · int/float/str/bool",
        explanation=(
            "파이썬 변수는 선언 없이 바로 대입하며, 타입이 자동으로 정해진다(동적 타입).\n"
            "정수 int, 실수 float, 문자열 str, 불리언 bool 이 기본이다.\n"
            "type(x) 로 타입을 확인하고, int()/str()/float() 로 형변환한다."
        ),
        usage="대부분의 값 저장에 바로 사용. 코딩테스트에서 입력을 int()/map(int,...)로 변환할 때 핵심.",
        cons="동적 타입이라 실수로 타입이 섞여도 실행 중에야 에러가 난다. 큰 프로젝트에선 타입 힌트 권장.",
        code=(
            "a = 10          # int\n"
            "b = 3.14        # float\n"
            "name = '홍길동'  # str\n"
            "flag = True     # bool\n"
            "print(type(a), type(b), type(name), type(flag))\n"
            "print(a + int('5'))      # 형변환 후 덧셈 → 15\n"
            "print(name * 2)          # 문자열 반복 → 홍길동홍길동\n"
        ),
    ),

    Lesson(
        id="py-basic-02-io",
        lang="python", level="기초",
        title="표준 입출력",
        summary="input() / print() / map · split",
        explanation=(
            "input() 은 한 줄을 문자열로 읽는다. 숫자는 int() 로 변환해야 한다.\n"
            "한 줄에 여러 수는 input().split() 으로 나눈 뒤 map(int, ...) 으로 한 번에 변환한다.\n"
            "출력은 print(). 여러 줄 출력이 많으면 ''.join(...) 으로 모아 한 번에 출력하면 빠르다."
        ),
        usage="코딩테스트 입력 처리의 기본. 빠른 입력은 sys.stdin.readline 사용.",
        cons="input() 은 많이 호출하면 느리다. 대량 입력은 sys.stdin 으로 바꿔야 시간초과를 피한다.",
        code=(
            "# 데모: 입력 대신 고정 문자열로 시연\n"
            "line = '3 5 7'\n"
            "nums = list(map(int, line.split()))\n"
            "print(nums)            # [3, 5, 7]\n"
            "print(sum(nums))       # 15\n"
            "print(' '.join(map(str, nums)))   # '3 5 7'\n"
        ),
    ),

    Lesson(
        id="py-basic-03-list",
        lang="python", level="기초",
        title="리스트(list)",
        summary="동적 배열 · 슬라이싱 · 컴프리헨션",
        explanation=(
            "리스트는 순서가 있는 가변 배열이다. append/pop 으로 끝에서 추가·제거(O(1)).\n"
            "슬라이싱 a[i:j], 뒤집기 a[::-1], 정렬 a.sort()/sorted(a).\n"
            "리스트 컴프리헨션 [f(x) for x in it if cond] 으로 간결하게 생성한다."
        ),
        usage="배열/스택 대용으로 가장 많이 쓴다. 2차원은 [[0]*m for _ in range(n)] (주의: [[0]*m]*n 금지).",
        cons="중간 삽입/삭제(insert/pop(0))는 O(n)으로 느리다 → 앞쪽 연산이 잦으면 collections.deque 사용.",
        code=(
            "a = [5, 2, 9, 1]\n"
            "a.append(7)\n"
            "print(a, a[1:3], a[::-1])\n"
            "print(sorted(a))\n"
            "squares = [x*x for x in range(1, 6)]\n"
            "print(squares)            # [1, 4, 9, 16, 25]\n"
            "grid = [[0]*3 for _ in range(2)]   # 2x3 (올바른 2차원 생성)\n"
            "print(grid)\n"
        ),
    ),

    Lesson(
        id="py-basic-04-loop",
        lang="python", level="기초",
        title="반복문과 조건문",
        summary="for/while · range · enumerate",
        explanation=(
            "for x in 반복가능: 으로 순회한다. range(n)/range(a,b)/range(a,b,step).\n"
            "인덱스가 필요하면 enumerate(seq), 두 시퀀스를 동시에 돌면 zip(a, b).\n"
            "조건은 if/elif/else. break/continue 로 흐름 제어."
        ),
        usage="모든 반복 처리의 기본. enumerate/zip 은 코드량을 크게 줄여준다.",
        cons="파이썬 반복문은 C/Java보다 느리다. 무거운 반복은 내장함수(sum, max)나 컴프리헨션으로 대체.",
        code=(
            "for i, ch in enumerate('abc'):\n"
            "    print(i, ch)\n"
            "names = ['kim', 'lee']; ages = [20, 30]\n"
            "for n, a in zip(names, ages):\n"
            "    print(n, a)\n"
            "total = 0\n"
            "for x in range(1, 11):\n"
            "    if x % 2 == 0:\n"
            "        total += x\n"
            "print('짝수합', total)    # 30\n"
        ),
    ),

    Lesson(
        id="py-basic-05-dict",
        lang="python", level="기초",
        title="딕셔너리(dict)와 집합(set)",
        summary="해시맵 · get/setdefault · Counter",
        explanation=(
            "dict 는 키-값 해시맵으로 평균 O(1) 조회/삽입. set 은 중복 없는 집합.\n"
            "없는 키 기본값은 d.get(k, 0) 또는 collections.defaultdict, Counter 활용.\n"
            "빈도수 세기는 Counter(iterable) 가 가장 간단하다."
        ),
        usage="빈도수/중복 체크/매핑 문제의 핵심 자료구조. in 연산이 리스트보다 훨씬 빠르다.",
        cons="키는 해시 가능(불변)해야 함(리스트는 키로 못 씀). 순서는 삽입순(파이썬 3.7+)이라 정렬은 별도.",
        code=(
            "from collections import Counter\n"
            "freq = {}\n"
            "for ch in 'banana':\n"
            "    freq[ch] = freq.get(ch, 0) + 1\n"
            "print(freq)               # {'b':1,'a':3,'n':2}\n"
            "print(Counter('banana'))  # 같은 결과를 한 줄로\n"
            "s = set([1, 2, 2, 3])\n"
            "print(s, 2 in s)          # {1,2,3} True\n"
        ),
    ),

    Lesson(
        id="py-basic-06-func",
        lang="python", level="기초",
        title="함수 정의와 반환",
        summary="def · return · 기본 인자",
        explanation=(
            "def 이름(매개변수): 으로 함수를 정의하고 return 으로 값을 돌려준다.\n"
            "return 이 없으면 None 을 반환한다. 기본값 인자(def f(x, y=10))로 호출을 간단히 한다.\n"
            "여러 값을 return a, b 로 묶어 반환하면 튜플로 받는다."
        ),
        usage="반복되는 로직을 묶어 재사용. 코딩테스트에서 DFS/재귀를 함수로 분리하면 깔끔하다.",
        cons="기본값 인자에 리스트 같은 가변 객체를 쓰면 호출 간 공유되는 함정이 있다(def f(a=[]) 금지).",
        code=(
            "def add(a, b=10):\n"
            "    return a + b\n"
            "def minmax(arr):\n"
            "    return min(arr), max(arr)\n"
            "print(add(5))         # 15 (기본값 b=10)\n"
            "print(add(5, 20))     # 25\n"
            "lo, hi = minmax([3, 9, 1])\n"
            "print(lo, hi)         # 1 9\n"
        ),
    ),

    Lesson(
        id="py-basic-07-str",
        lang="python", level="기초",
        title="문자열 다루기",
        summary="인덱싱 · 슬라이싱 · 주요 메서드",
        explanation=(
            "문자열은 불변(immutable) 시퀀스다. s[i] 인덱싱, s[i:j] 슬라이싱, s[::-1] 뒤집기.\n"
            "주요 메서드: upper/lower, strip(공백제거), split(나누기), join(합치기),\n"
            "replace(치환), find/index(위치), startswith/endswith, count."
        ),
        usage="입력 파싱(split), 출력 조립(join), 문자열 규칙 처리 문제에 필수.",
        cons="불변이라 한 글자씩 += 로 이어붙이면 O(n^2)로 느리다 → 리스트에 모아 ''.join() 권장.",
        code=(
            "s = '  Hello, World  '\n"
            "print(s.strip())              # 'Hello, World'\n"
            "print(s.strip().upper())      # 'HELLO, WORLD'\n"
            "print('a,b,c'.split(','))     # ['a','b','c']\n"
            "print('-'.join(['2024','01','15']))  # '2024-01-15'\n"
            "print('banana'.count('a'), 'banana'.replace('a','*'))\n"
        ),
    ),

    Lesson(
        id="py-basic-08-tuple",
        lang="python", level="기초",
        title="튜플과 언패킹",
        summary="불변 묶음 · 다중 대입 · swap",
        explanation=(
            "튜플 (a, b) 은 불변 묶음이다. 여러 값을 한 번에 대입(언패킹)할 때 유용하다.\n"
            "a, b = b, a 로 임시변수 없이 교환하고, x, y = map(int, input().split()) 처럼 입력에도 쓴다.\n"
            "딕셔너리 키나 좌표처럼 '바뀌면 안 되는 묶음'에 적합하다."
        ),
        usage="좌표 (x, y), 다중 반환값 받기, 한 번에 여러 변수 초기화에 자주 쓴다.",
        cons="불변이라 원소 변경 불가(변경이 필요하면 리스트). 원소 1개 튜플은 (x,) 처럼 콤마 필요.",
        code=(
            "point = (3, 5)\n"
            "x, y = point          # 언패킹\n"
            "print(x, y)           # 3 5\n"
            "a, b = 1, 2\n"
            "a, b = b, a           # 임시변수 없이 swap\n"
            "print(a, b)           # 2 1\n"
            "nums = tuple([1, 2, 3])\n"
            "print(nums, len(nums))\n"
        ),
    ),
]
