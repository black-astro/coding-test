"""Python 고급 문법 (제너레이터·데코레이터·컨텍스트 매니저·itertools·heapq·bisect·functools·빠른 입출력)."""

from engine.models import Lesson

LESSONS = [

    Lesson(
        id="py-adv-01",
        lang="python", level="고급",
        title="제너레이터와 이터레이터(yield)",
        summary="yield 로 값을 하나씩 지연 생성",
        explanation=(
            "이터레이터는 __next__ 로 값을 하나씩 꺼낼 수 있는 객체이고, 제너레이터는\n"
            "이를 가장 쉽게 만드는 방법이다. 함수 안에 yield 가 있으면 호출 시 즉시 실행되지 않고\n"
            "제너레이터 객체를 돌려준다. next() 또는 for 로 돌릴 때마다 yield 지점까지만 실행되고\n"
            "값을 내보낸 뒤 그 자리에서 멈춰 상태를 보존한다.\n"
            "리스트와 달리 모든 값을 미리 메모리에 올리지 않아 대용량/무한 수열 처리에 유리하다.\n"
            "yield from 으로 다른 이터러블을 그대로 위임할 수도 있다."
        ),
        usage="대용량 데이터를 한 줄씩 흘려보낼 때, 무한 수열, 파이프라인 처리에 메모리 절약용으로 쓴다.",
        cons="한 번 소비하면 다시 못 돌린다(재사용하려면 다시 생성). 길이(len)나 인덱싱이 불가능하다.",
        code=(
            "def countdown(n):\n"
            "    while n > 0:\n"
            "        yield n          # 여기서 값을 내보내고 멈춘다\n"
            "        n -= 1\n"
            "\n"
            "def fib(k):\n"
            "    a, b = 0, 1\n"
            "    for _ in range(k):\n"
            "        yield a\n"
            "        a, b = b, a + b\n"
            "\n"
            "gen = countdown(3)\n"
            "print(next(gen), next(gen))   # 3 2\n"
            "print(list(countdown(5)))     # [5, 4, 3, 2, 1]\n"
            "print(list(fib(8)))           # [0, 1, 1, 2, 3, 5, 8, 13]\n"
            "\n"
            "# 제너레이터 표현식: 리스트를 만들지 않고 합계만 계산(메모리 절약)\n"
            "print(sum(x * x for x in range(1, 6)))   # 55\n"
        ),
    ),

    Lesson(
        id="py-adv-02",
        lang="python", level="고급",
        title="데코레이터",
        summary="함수를 감싸 기능을 덧붙이는 @문법",
        explanation=(
            "데코레이터는 함수를 인자로 받아 새 함수를 돌려주는 함수다. @데코레이터 를 함수 위에 붙이면\n"
            "그 함수를 자동으로 감싸 준다. 원래 함수 호출 전후에 로깅·시간측정·권한확인 같은\n"
            "공통 기능을 끼워 넣을 수 있다(횡단 관심사 분리).\n"
            "감싸는 함수는 보통 *args, **kwargs 로 어떤 인자든 그대로 받아 원본에 넘긴다.\n"
            "functools.wraps 를 쓰면 원본 함수의 이름·docstring 등 메타정보가 보존된다."
        ),
        usage="로깅, 실행시간 측정, 캐싱, 재시도, 접근 제어 등 여러 함수에 공통으로 끼워 넣을 때.",
        cons="중첩이 많으면 스택 추적이 복잡해지고 디버깅이 어렵다. 과용하면 흐름 파악이 힘들다.",
        code=(
            "import functools\n"
            "\n"
            "def logged(func):\n"
            "    @functools.wraps(func)\n"
            "    def wrapper(*args, **kwargs):\n"
            "        print(f'호출: {func.__name__}{args}')\n"
            "        result = func(*args, **kwargs)\n"
            "        print(f'결과: {result}')\n"
            "        return result\n"
            "    return wrapper\n"
            "\n"
            "@logged\n"
            "def add(a, b):\n"
            "    return a + b\n"
            "\n"
            "print(add(3, 4))\n"
            "print(add.__name__)   # wraps 덕분에 'add' 가 그대로 보인다\n"
        ),
    ),

    Lesson(
        id="py-adv-03",
        lang="python", level="고급",
        title="컨텍스트 매니저(with)",
        summary="자원 획득/해제를 자동으로 보장",
        explanation=(
            "with 문은 블록에 들어갈 때 __enter__, 나갈 때 __exit__ 를 자동 호출해 준다.\n"
            "중간에 예외가 나도 __exit__ 가 반드시 실행되므로 파일 닫기, 락 해제, 연결 종료 같은\n"
            "정리 작업을 빼먹지 않는다.\n"
            "클래스로 __enter__/__exit__ 를 직접 구현할 수도 있고, contextlib.contextmanager\n"
            "데코레이터로 제너레이터(yield 한 번) 하나만 써서 간단히 만들 수도 있다.\n"
            "yield 앞부분이 진입(setup), 뒷부분이 종료(teardown)에 해당한다."
        ),
        usage="파일·소켓·DB 연결·락 등 반드시 닫아야 하는 자원, 임시 상태 변경 후 원복할 때.",
        cons="__exit__ 의 반환값으로 예외를 삼킬 수 있어 실수하면 오류를 숨긴다. 남용하면 흐름이 가려진다.",
        code=(
            "from contextlib import contextmanager\n"
            "\n"
            "class Timer:\n"
            "    def __enter__(self):\n"
            "        print('시작')\n"
            "        return self\n"
            "    def __exit__(self, exc_type, exc, tb):\n"
            "        print('종료(정리)')\n"
            "        return False        # 예외를 삼키지 않음\n"
            "\n"
            "with Timer():\n"
            "    print('작업 중...')\n"
            "\n"
            "@contextmanager\n"
            "def tag(name):\n"
            "    print(f'<{name}>')\n"
            "    yield                  # 이 지점이 with 블록 본문\n"
            "    print(f'</{name}>')\n"
            "\n"
            "with tag('b'):\n"
            "    print('굵게')\n"
        ),
    ),

    Lesson(
        id="py-adv-04",
        lang="python", level="고급",
        title="itertools(조합/순열/product)",
        summary="조합·순열·곱집합을 효율적으로 생성",
        explanation=(
            "itertools 는 반복 처리를 위한 고성능 도구 모음이다.\n"
            "- permutations(it, r): 순서가 있는 r개 순열(nPr)\n"
            "- combinations(it, r): 순서가 없는 r개 조합(nCr)\n"
            "- product(a, b, ...): 곱집합(중첩 for 문 대체), repeat= 로 같은 집합 반복\n"
            "- combinations_with_replacement: 중복 허용 조합\n"
            "모두 제너레이터를 돌려주므로 필요한 만큼만 꺼내 쓰면 메모리에 전부 올리지 않는다.\n"
            "그 밖에 chain, groupby, accumulate, count 등도 자주 쓰인다."
        ),
        usage="완전탐색(브루트포스)에서 부분집합·순열·여러 칸 조합을 만들 때 직접 재귀 대신 사용한다.",
        cons="경우의 수가 폭발적으로 늘어나므로(n! 등) 큰 입력에선 시간초과. 결과를 list로 만들면 메모리 급증.",
        code=(
            "from itertools import permutations, combinations, product\n"
            "\n"
            "nums = [1, 2, 3]\n"
            "print(list(permutations(nums, 2)))   # 순열 nP2\n"
            "print(list(combinations(nums, 2)))   # 조합 nC2\n"
            "\n"
            "# 2자리 비밀번호 후보(00~11) 같은 곱집합\n"
            "print(list(product([0, 1], repeat=2)))\n"
            "\n"
            "# 중첩 for 문 대체\n"
            "for a, b in product('AB', '12'):\n"
            "    print(a + b, end=' ')   # A1 A2 B1 B2\n"
            "print()\n"
        ),
    ),

    Lesson(
        id="py-adv-05",
        lang="python", level="고급",
        title="heapq(우선순위 큐)",
        summary="최소 힙으로 최솟값을 O(log n)에 관리",
        explanation=(
            "heapq 는 리스트를 최소 힙(min-heap)처럼 다루는 함수 모음이다. 항상 가장 작은 값이\n"
            "맨 앞(heap[0])에 온다.\n"
            "- heappush(h, x): 삽입 O(log n)\n"
            "- heappop(h): 최솟값 꺼내며 제거 O(log n)\n"
            "- heapify(list): 기존 리스트를 제자리에서 힙으로 O(n)\n"
            "최대 힙이 필요하면 값에 -1을 곱해 넣거나 (-우선순위, 값) 튜플을 쓴다.\n"
            "튜플을 넣으면 첫 원소(우선순위) 기준으로 정렬되어 우선순위 큐가 된다."
        ),
        usage="다익스트라 최단경로, 작업 스케줄링, '가장 작은/큰 K개', 실시간 중앙값 등.",
        cons="중간 임의 원소의 삭제·갱신이 직접 불가(보통 무효표시 기법 사용). 정렬 전체가 필요하면 sort가 낫다.",
        code=(
            "import heapq\n"
            "\n"
            "h = []\n"
            "for x in [5, 1, 8, 3]:\n"
            "    heapq.heappush(h, x)\n"
            "print(heapq.heappop(h))   # 1 (최솟값)\n"
            "print(heapq.heappop(h))   # 3\n"
            "\n"
            "data = [9, 2, 7, 4, 1]\n"
            "heapq.heapify(data)        # 제자리 힙 구성\n"
            "print(data[0])             # 1\n"
            "\n"
            "# 최대 힙: 부호 반전\n"
            "maxh = []\n"
            "for x in [5, 1, 8, 3]:\n"
            "    heapq.heappush(maxh, -x)\n"
            "print(-heapq.heappop(maxh))   # 8 (최댓값)\n"
            "\n"
            "# 우선순위 큐: (우선순위, 작업)\n"
            "pq = [(2, '낮음'), (0, '긴급'), (1, '보통')]\n"
            "heapq.heapify(pq)\n"
            "print(heapq.heappop(pq))   # (0, '긴급')\n"
        ),
    ),

    Lesson(
        id="py-adv-06",
        lang="python", level="고급",
        title="bisect(이분 탐색)",
        summary="정렬 리스트에서 위치를 O(log n)에 탐색",
        explanation=(
            "bisect 는 이미 정렬된 리스트에 대해 이분 탐색으로 삽입 위치를 찾아 준다.\n"
            "- bisect_left(a, x): x 가 들어갈 가장 왼쪽 위치(같은 값들의 앞)\n"
            "- bisect_right(a, x): x 가 들어갈 가장 오른쪽 위치(같은 값들의 뒤)\n"
            "- insort(a, x): 정렬을 유지하며 x 를 삽입\n"
            "두 함수의 차이로 'x 의 개수' = bisect_right - bisect_left 를 구할 수 있고,\n"
            "'x 이상인 첫 원소', 'x 이하인 마지막 원소'를 빠르게 찾는다."
        ),
        usage="정렬된 데이터에서 특정 값/범위 개수 세기, 좌표압축, LIS 길이(O(n log n)) 등에 쓴다.",
        cons="반드시 정렬 상태를 전제로 한다(아니면 틀린 결과). insort 삽입 자체는 원소 이동 때문에 O(n).",
        code=(
            "import bisect\n"
            "\n"
            "a = [1, 3, 3, 3, 5, 7]\n"
            "print(bisect.bisect_left(a, 3))    # 1\n"
            "print(bisect.bisect_right(a, 3))   # 4\n"
            "print(bisect.bisect_right(a, 3) - bisect.bisect_left(a, 3))  # 3의 개수 = 3\n"
            "\n"
            "# 정렬 유지 삽입\n"
            "bisect.insort(a, 4)\n"
            "print(a)   # [1, 3, 3, 3, 4, 5, 7]\n"
            "\n"
            "# x 이상인 첫 원소 찾기\n"
            "idx = bisect.bisect_left(a, 5)\n"
            "print(a[idx])   # 5\n"
        ),
    ),

    Lesson(
        id="py-adv-07",
        lang="python", level="고급",
        title="functools(lru_cache 메모이제이션, reduce)",
        summary="자동 캐싱과 누적 계산 도구",
        explanation=(
            "functools 는 함수를 다루는 유틸리티 모음이다.\n"
            "- @lru_cache(maxsize=None): 함수의 인자별 결과를 자동 저장(메모이제이션). 같은 인자로\n"
            "  다시 호출되면 계산 없이 캐시 값을 즉시 반환한다. 재귀 DP를 한 줄로 빠르게 만든다.\n"
            "  (파이썬 3.9+ 에서는 @cache 가 lru_cache(maxsize=None) 의 단축형)\n"
            "- reduce(func, it, init): 왼쪽부터 두 값씩 접어 하나로 누적한다. 곱·최대공약수 누적 등.\n"
            "- partial: 일부 인자를 미리 고정한 새 함수를 만든다.\n"
            "캐시가 잘 듣는지 cache_info() 로 hit/miss 를 확인할 수 있다."
        ),
        usage="피보나치·조합수 같은 겹치는 부분문제 재귀 DP 가속, 순수 함수의 반복 호출 결과 재사용.",
        cons="인자는 해시 가능(불변)해야 캐싱된다. 캐시가 메모리를 계속 점유하고, 부수효과 함수엔 위험.",
        code=(
            "from functools import lru_cache, reduce\n"
            "from math import gcd\n"
            "\n"
            "@lru_cache(maxsize=None)\n"
            "def fib(n):\n"
            "    if n < 2:\n"
            "        return n\n"
            "    return fib(n - 1) + fib(n - 2)\n"
            "\n"
            "print(fib(30))            # 832040 (캐시 덕분에 즉시)\n"
            "print(fib.cache_info())   # hits/misses 확인\n"
            "\n"
            "# reduce: 1*2*...*5 = 120\n"
            "print(reduce(lambda acc, x: acc * x, range(1, 6), 1))\n"
            "\n"
            "# reduce + gcd: 여러 수의 최대공약수\n"
            "print(reduce(gcd, [24, 36, 60]))   # 12\n"
        ),
    ),

    Lesson(
        id="py-adv-08",
        lang="python", level="고급",
        title="sys.stdin 빠른 입출력과 재귀한도",
        summary="대량 입력 가속과 setrecursionlimit",
        explanation=(
            "input() 은 호출마다 느리므로 대량 입력에선 sys.stdin 을 쓴다.\n"
            "- input = sys.stdin.readline 으로 바꿔 한 줄을 빠르게 읽는다(끝의 개행은 rstrip).\n"
            "- 전체를 sys.stdin.read() 로 한 번에 읽고 split() 하면 가장 빠르다.\n"
            "- 출력이 많으면 결과를 리스트에 모아 sys.stdout.write('\\n'.join(...)) 로 한 번에.\n"
            "또 파이썬 기본 재귀 한도는 약 1000이라 깊은 DFS는 RecursionError 가 난다.\n"
            "sys.setrecursionlimit(10**6) 처럼 한도를 늘려 준다(과도하면 메모리 위험).\n"
            "아래 데모는 채점기에 입력이 없으므로 io.StringIO 로 가짜 표준입력을 만들어 시연한다."
        ),
        usage="입력 줄 수가 수만~수십만인 백준 문제, 깊은 재귀 DFS/분할정복에서 필수.",
        cons="setrecursionlimit 을 너무 키우면 스택 초과로 인터프리터가 죽을 수 있다. readline 은 개행 처리 주의.",
        code=(
            "import sys, io\n"
            "\n"
            "# 데모: 실제 표준입력 대신 고정 데이터를 sys.stdin 에 주입\n"
            "sample = '3\\n10 20\\n30 40\\n50 60\\n'\n"
            "sys.stdin = io.StringIO(sample)\n"
            "\n"
            "input = sys.stdin.readline      # 빠른 입력\n"
            "n = int(input())\n"
            "out = []\n"
            "for _ in range(n):\n"
            "    a, b = map(int, input().split())\n"
            "    out.append(str(a + b))\n"
            "sys.stdout.write('\\n'.join(out) + '\\n')   # 한 번에 출력 → 30 70 110\n"
            "\n"
            "# 깊은 재귀를 위해 한도 상향\n"
            "sys.setrecursionlimit(10**6)\n"
            "\n"
            "def depth(k):\n"
            "    if k == 0:\n"
            "        return 0\n"
            "    return 1 + depth(k - 1)\n"
            "\n"
            "print(depth(2000))   # 기본 한도였다면 에러, 상향 후 2000\n"
        ),
    ),
]
