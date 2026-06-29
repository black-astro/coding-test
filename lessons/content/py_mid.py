"""Python 중급 문법 (함수·람다·컴프리헨션·예외·OOP·모듈·collections·문자열)."""

from engine.models import Lesson

LESSONS = [

    Lesson(
        id="py-mid-01",
        lang="python", level="중급",
        title="함수와 기본/가변 인자 (*args, **kwargs)",
        summary="기본값 인자 · 가변 위치인자 *args · 가변 키워드인자 **kwargs",
        explanation=(
            "함수는 def 이름(매개변수): 로 정의하고 return 으로 값을 돌려준다.\n"
            "매개변수에 기본값을 주면(def f(x, y=10)) 호출 시 인자를 생략할 수 있다.\n"
            "*args 는 정해지지 않은 개수의 위치 인자를 튜플로 모아 받는다.\n"
            "**kwargs 는 정해지지 않은 키워드 인자(key=value)를 딕셔너리로 모아 받는다.\n"
            "동작 방식: 호출할 때 넘긴 인자들이 먼저 기본 매개변수에 채워지고,\n"
            "남는 위치 인자는 args 튜플로, 남는 키워드 인자는 kwargs 딕셔너리로 들어간다.\n"
            "반대로 호출 시 *리스트 / **딕셔너리 로 풀어서(언패킹) 넘길 수도 있다.\n"
            "주의: 기본값으로 빈 리스트 같은 가변 객체를 쓰면 모든 호출이 공유하므로 None 으로 두고 안에서 만든다."
        ),
        usage=(
            "공통 로직을 함수로 묶어 재사용한다. *args/**kwargs 는 인자 개수가 유동적인 "
            "래퍼/데코레이터/로깅 함수에 유용하다. 코딩테스트에서는 재귀 함수(DFS/백트래킹)와 "
            "기본값을 활용한 재귀 깊이/누적값 전달에 자주 쓴다."
        ),
        cons=(
            "기본값에 [] 나 {} 같은 가변 객체를 쓰면 호출 간에 값이 누적되는 함정이 있다(반드시 None 으로).\n"
            "인자가 너무 많아지면 가독성이 떨어지고, **kwargs 남용은 어떤 인자가 필요한지 숨겨 디버깅을 어렵게 한다."
        ),
        code=(
            "def add_all(*args, start=0):\n"
            "    # 가변 위치 인자를 모두 더한다\n"
            "    total = start\n"
            "    for v in args:\n"
            "        total += v\n"
            "    return total\n"
            "\n"
            "def make_user(**kwargs):\n"
            "    # 키워드 인자를 딕셔너리로 받는다\n"
            "    return kwargs\n"
            "\n"
            "def bad_default(item, box=None):\n"
            "    # 가변 기본값 함정을 피하는 올바른 방법\n"
            "    if box is None:\n"
            "        box = []\n"
            "    box.append(item)\n"
            "    return box\n"
            "\n"
            "print(add_all(1, 2, 3))            # 6\n"
            "print(add_all(1, 2, 3, start=10))  # 16\n"
            "nums = [4, 5, 6]\n"
            "print(add_all(*nums))             # 언패킹 → 15\n"
            "print(make_user(name='홍길동', age=20))\n"
            "print(bad_default(1))             # [1]\n"
            "print(bad_default(2))             # [2] (누적되지 않음)\n"
        ),
    ),

    Lesson(
        id="py-mid-02",
        lang="python", level="중급",
        title="람다와 정렬 key",
        summary="익명 함수 lambda · sorted/sort 의 key · reverse",
        explanation=(
            "lambda 매개변수: 식 은 이름 없는 한 줄짜리 함수를 만든다.\n"
            "예를 들어 lambda x: x*2 는 def f(x): return x*2 와 같다.\n"
            "주로 정렬 기준(key)이나 map/filter 의 함수 인자로 즉석에서 쓴다.\n"
            "sorted(반복가능, key=함수) 는 각 원소를 key 함수에 넣은 결과를 기준으로 정렬한다.\n"
            "동작 방식: key 함수가 각 원소마다 호출되어 '비교용 값'을 만들고, 그 값으로 비교한다.\n"
            "튜플을 반환하면 다중 기준 정렬이 된다. (예: 먼저 점수 내림차순, 같으면 이름 오름차순)\n"
            "내림차순은 reverse=True 이거나, 숫자 앞에 -를 붙여(-x) 표현한다."
        ),
        usage=(
            "정렬 기준을 한 줄로 지정할 때 가장 많이 쓴다. 코딩테스트에서 '여러 조건으로 정렬' "
            "(예: 나이 오름차순, 같으면 이름 사전순) 문제는 key=lambda x: (x[0], x[1]) 형태로 해결한다. "
            "max/min 의 key 인자에도 동일하게 쓴다."
        ),
        cons=(
            "lambda 는 한 줄 식만 가능하고 문장(if 블록, 반복문)을 넣을 수 없어 복잡한 로직엔 부적합하다.\n"
            "이름이 없어 디버깅 시 추적이 어렵고, 너무 복잡한 lambda 는 def 로 빼는 편이 가독성에 좋다."
        ),
        code=(
            "people = [('kim', 30), ('lee', 20), ('park', 30), ('choi', 20)]\n"
            "\n"
            "# 나이 오름차순, 같으면 이름 사전순 (다중 기준 정렬)\n"
            "by_age_name = sorted(people, key=lambda p: (p[1], p[0]))\n"
            "print(by_age_name)\n"
            "\n"
            "# 나이 내림차순\n"
            "by_age_desc = sorted(people, key=lambda p: -p[1])\n"
            "print(by_age_desc)\n"
            "\n"
            "nums = [3, 1, -5, 2, -8]\n"
            "# 절댓값 기준 정렬\n"
            "print(sorted(nums, key=lambda x: abs(x)))   # [1, 2, 3, -5, -8]\n"
            "print(max(people, key=lambda p: p[1]))      # 나이 최대\n"
            "double = list(map(lambda x: x * 2, nums))\n"
            "print(double)\n"
        ),
    ),

    Lesson(
        id="py-mid-03",
        lang="python", level="중급",
        title="리스트/딕셔너리 컴프리헨션 심화",
        summary="조건부 표현식 · 중첩 컴프리헨션 · dict/set 컴프리헨션",
        explanation=(
            "컴프리헨션은 반복문을 한 줄 식으로 압축하는 문법이다.\n"
            "기본형: [식 for x in 반복 if 조건]. if 는 필터링(통과한 것만 포함)이다.\n"
            "삼항(조건부 표현식)을 식 자리에 쓰면 값을 분기할 수 있다:\n"
            "  [x if x > 0 else 0 for x in nums]  → 음수는 0 으로 바꿔 담는다.\n"
            "  (필터 if 는 for 뒤, 값 분기 if-else 는 for 앞에 온다는 위치 차이에 주의)\n"
            "중첩 컴프리헨션 [[...] for ...] 으로 2차원 리스트를 만들거나,\n"
            "[식 for a in A for b in B] 로 이중 반복을 펼칠 수 있다(앞 for 가 바깥 루프).\n"
            "딕셔너리 컴프리헨션 {k: v for ...}, 집합 컴프리헨션 {x for ...} 도 같은 원리다."
        ),
        usage=(
            "반복+변환+필터를 간결하게 처리할 때. 코딩테스트에서 입력 파싱(2차원 배열 생성), "
            "인덱스→값 매핑 딕셔너리 만들기, 조건에 맞는 원소만 추리기 등에 매우 자주 쓴다. "
            "일반 for 루프보다 약간 빠르기도 하다."
        ),
        cons=(
            "조건과 중첩이 많아지면 한 줄이 너무 길어져 오히려 읽기 어렵다(2중 이상 중첩은 일반 루프 권장).\n"
            "메모리에 결과 전체를 만들므로 거대한 데이터에는 제너레이터 표현식 (x for ...) 을 고려해야 한다."
        ),
        code=(
            "nums = [-2, 5, -1, 8, 0, -7]\n"
            "\n"
            "# 필터: 양수만\n"
            "pos = [x for x in nums if x > 0]\n"
            "print(pos)                       # [5, 8]\n"
            "\n"
            "# 값 분기: 음수는 0 으로\n"
            "clip = [x if x > 0 else 0 for x in nums]\n"
            "print(clip)                      # [0, 5, 0, 8, 0, 0]\n"
            "\n"
            "# 2차원 배열 생성\n"
            "grid = [[r * 3 + c for c in range(3)] for r in range(2)]\n"
            "print(grid)                      # [[0,1,2],[3,4,5]]\n"
            "\n"
            "# 이중 반복 펼치기\n"
            "pairs = [(a, b) for a in [1, 2] for b in ['x', 'y']]\n"
            "print(pairs)\n"
            "\n"
            "# dict / set 컴프리헨션\n"
            "square_map = {x: x * x for x in range(1, 5)}\n"
            "print(square_map)                # {1:1, 2:4, 3:9, 4:16}\n"
            "print({len(w) for w in ['a', 'bb', 'cc', 'ddd']})  # {1, 2, 3}\n"
        ),
    ),

    Lesson(
        id="py-mid-04",
        lang="python", level="중급",
        title="예외 처리 (try/except/finally)",
        summary="try/except/else/finally · 예외 종류 · raise",
        explanation=(
            "실행 중 오류가 나면 예외(Exception)가 발생하고, 처리하지 않으면 프로그램이 멈춘다.\n"
            "try: 블록에서 오류가 날 수 있는 코드를 실행하고, except 에서 오류를 잡아 처리한다.\n"
            "동작 방식: try 안에서 예외가 생기면 즉시 해당 타입에 맞는 except 로 점프한다.\n"
            "except ValueError as e: 처럼 예외 타입을 지정하고 as 로 객체를 받아 내용을 볼 수 있다.\n"
            "여러 except 를 나열해 타입별로 다르게 처리할 수 있다(구체적인 타입을 위에).\n"
            "else: 는 예외가 '없을 때만' 실행되고, finally: 는 예외 여부와 상관없이 항상 실행된다\n"
            "(파일 닫기, 자원 정리 등에 사용). raise 로 직접 예외를 발생시킬 수도 있다."
        ),
        usage=(
            "입력 검증, 파일/네트워크 처리 등 실패 가능성이 있는 작업의 안전한 처리에 쓴다. "
            "코딩테스트에서는 형변환 실패(int('a'))나 0 나눗셈 방어, 그리고 '값이 없을 때까지 입력 받기' "
            "패턴(try: input() except EOFError)에 활용한다."
        ),
        cons=(
            "except: 로 모든 예외를 통째로 잡으면 진짜 버그(오타 등)까지 숨겨 디버깅이 어려워진다 → 구체적 타입 지정.\n"
            "예외 처리는 정상 흐름 제어용이 아니다(반복적으로 예외에 의존하면 느리고 의도가 불명확)."
        ),
        code=(
            "def safe_div(a, b):\n"
            "    try:\n"
            "        result = a / b\n"
            "    except ZeroDivisionError:\n"
            "        print('0 으로 나눌 수 없음')\n"
            "        return None\n"
            "    else:\n"
            "        # 예외가 없을 때만 실행\n"
            "        return result\n"
            "    finally:\n"
            "        # 항상 실행\n"
            "        print(f'나눗셈 시도: {a} / {b}')\n"
            "\n"
            "print(safe_div(10, 2))   # 5.0\n"
            "print(safe_div(10, 0))   # None\n"
            "\n"
            "# 형변환 예외 처리\n"
            "for token in ['10', 'abc', '20']:\n"
            "    try:\n"
            "        print('숫자:', int(token))\n"
            "    except ValueError as e:\n"
            "        print('변환 실패:', token)\n"
            "\n"
            "# 직접 예외 발생\n"
            "def check_age(age):\n"
            "    if age < 0:\n"
            "        raise ValueError('나이는 음수가 될 수 없음')\n"
            "    return age\n"
            "\n"
            "try:\n"
            "    check_age(-5)\n"
            "except ValueError as e:\n"
            "    print('에러:', e)\n"
        ),
    ),

    Lesson(
        id="py-mid-05",
        lang="python", level="중급",
        title="클래스와 객체 (OOP 기초)",
        summary="class · __init__ · self · 메서드 · 상속",
        explanation=(
            "클래스는 데이터(속성)와 동작(메서드)을 한 묶음으로 만드는 설계도이고,\n"
            "그 설계도로 만든 실체를 객체(인스턴스)라고 한다.\n"
            "class 이름: 으로 정의하고, __init__ 은 객체 생성 시 자동 호출되는 생성자다.\n"
            "self 는 '그 객체 자신'을 가리키며, 모든 인스턴스 메서드의 첫 매개변수다.\n"
            "동작 방식: obj = Dog('바둑이') 하면 __init__(self, name) 이 호출되어 self.name 에 저장된다.\n"
            "이후 obj.bark() 처럼 호출하면 self 에 obj 가 자동으로 넘어간다.\n"
            "상속(class 자식(부모):)으로 부모의 속성/메서드를 물려받고, 같은 이름 메서드를 다시 정의해\n"
            "동작을 바꾸는 것을 오버라이딩이라 한다. __str__ 을 정의하면 print 출력 형태를 지정할 수 있다."
        ),
        usage=(
            "상태와 동작이 함께 묶이는 대상(플레이어, 그래프 노드, 게임 보드 등)을 모델링할 때 쓴다. "
            "코딩테스트에서 자주 쓰진 않지만, 복잡한 시뮬레이션/객체 상태 관리나 우선순위 비교 객체를 "
            "정의할 때 유용하다."
        ),
        cons=(
            "단순한 데이터 묶음에는 클래스가 과하다(딕셔너리/튜플/namedtuple/dataclass 가 더 간단).\n"
            "self 누락, 클래스 변수와 인스턴스 변수 혼동 등 초보자가 실수하기 쉬운 지점이 많다."
        ),
        code=(
            "class Animal:\n"
            "    def __init__(self, name):\n"
            "        self.name = name      # 인스턴스 속성\n"
            "\n"
            "    def speak(self):\n"
            "        return f'{self.name} 가 소리를 낸다'\n"
            "\n"
            "class Dog(Animal):            # 상속\n"
            "    def speak(self):          # 오버라이딩\n"
            "        return f'{self.name}: 멍멍!'\n"
            "\n"
            "    def __str__(self):\n"
            "        return f'Dog(name={self.name})'\n"
            "\n"
            "a = Animal('고양이')\n"
            "d = Dog('바둑이')\n"
            "print(a.speak())     # 고양이 가 소리를 낸다\n"
            "print(d.speak())     # 바둑이: 멍멍!\n"
            "print(d)             # Dog(name=바둑이)  (__str__)\n"
            "print(isinstance(d, Animal))   # True (자식은 부모 타입)\n"
        ),
    ),

    Lesson(
        id="py-mid-06",
        lang="python", level="중급",
        title="모듈/패키지와 import",
        summary="import · from import · as · 표준 라이브러리",
        explanation=(
            "모듈은 함수/변수/클래스를 모아둔 .py 파일이고, 패키지는 모듈을 모아둔 폴더다.\n"
            "다른 파일의 기능을 가져오려면 import 한다.\n"
            "  import math            → math.sqrt(9) 처럼 모듈이름.기능 으로 사용\n"
            "  from math import sqrt  → sqrt(9) 처럼 기능을 바로 사용\n"
            "  import numpy as np     → as 로 별칭(짧은 이름) 지정\n"
            "동작 방식: import 하면 해당 모듈이 한 번 실행되어 메모리에 올라가고, 그 안의 이름을 쓸 수 있다.\n"
            "파이썬은 표준 라이브러리가 풍부하다: math(수학), random(난수), itertools(조합/순열),\n"
            "collections(자료구조), sys(시스템), heapq(힙) 등은 별도 설치 없이 바로 import 된다.\n"
            "__name__ == '__main__' 은 '이 파일을 직접 실행했는가'를 판별하는 관용구다."
        ),
        usage=(
            "코드를 파일 단위로 분리·재사용할 때 필수. 코딩테스트에서는 표준 라이브러리가 핵심 무기다: "
            "math.gcd, itertools.permutations/combinations, heapq, bisect, collections 등을 알면 "
            "직접 구현할 코드를 크게 줄일 수 있다."
        ),
        cons=(
            "from 모듈 import * 는 어떤 이름이 들어왔는지 불분명해 이름 충돌·가독성 문제가 생긴다(지양).\n"
            "무거운 패키지를 불필요하게 import 하면 시작이 느려지고, 순환 import(서로 import) 는 오류를 낸다."
        ),
        code=(
            "import math\n"
            "from itertools import combinations, permutations\n"
            "from collections import Counter\n"
            "import random as rnd\n"
            "\n"
            "print(math.gcd(12, 18))            # 6\n"
            "print(math.sqrt(16))               # 4.0\n"
            "\n"
            "# 조합/순열 (코딩테스트 단골)\n"
            "print(list(combinations([1, 2, 3], 2)))   # [(1,2),(1,3),(2,3)]\n"
            "print(list(permutations([1, 2], 2)))      # [(1,2),(2,1)]\n"
            "\n"
            "rnd.seed(42)                       # 시드 고정 → 결과 재현 가능\n"
            "print(rnd.randint(1, 100))\n"
            "\n"
            "print(Counter('mississippi'))\n"
            "\n"
            "if __name__ == '__main__':\n"
            "    print('이 파일을 직접 실행했습니다')\n"
        ),
    ),

    Lesson(
        id="py-mid-07",
        lang="python", level="중급",
        title="collections (deque, defaultdict, Counter)",
        summary="양방향 큐 deque · 기본값 딕셔너리 defaultdict · 빈도 Counter",
        explanation=(
            "collections 모듈은 자주 쓰는 고급 자료구조를 제공한다.\n"
            "deque(데크)는 양쪽 끝에서 O(1) 로 추가/삭제가 되는 큐다.\n"
            "  append/appendleft(추가), pop/popleft(삭제). 리스트의 pop(0) 은 O(n) 이라 BFS 큐로는 deque 가 필수.\n"
            "defaultdict(기본값팩토리)는 없는 키에 접근하면 자동으로 기본값을 만들어 준다.\n"
            "  defaultdict(int) → 없는 키는 0, defaultdict(list) → 없는 키는 [] 로 시작.\n"
            "  덕분에 d[k] += 1 이나 d[k].append(...) 를 키 존재 확인 없이 바로 쓸 수 있다.\n"
            "Counter 는 원소 빈도를 한 번에 세는 딕셔너리로, most_common(n) 으로 상위 n개를 뽑는다.\n"
            "Counter 끼리 +, - 연산도 가능하다."
        ),
        usage=(
            "코딩테스트의 핵심 도구다. deque 는 BFS/슬라이딩 윈도우/큐 시뮬레이션에, "
            "defaultdict 는 그래프 인접 리스트(defaultdict(list))나 그룹핑/빈도수 누적에, "
            "Counter 는 빈도수 문제·애너그램·최빈값 찾기에 거의 항상 등장한다."
        ),
        cons=(
            "deque 는 중간 인덱스 접근(d[i])이 O(n) 으로 느리다(임의 접근이 잦으면 리스트가 낫다).\n"
            "defaultdict 는 조회만 해도 키가 생겨 버리는 부작용이 있어, 단순 조회엔 일반 dict.get 이 안전하다."
        ),
        code=(
            "from collections import deque, defaultdict, Counter\n"
            "\n"
            "# deque: 양방향 큐 (BFS 큐로 사용)\n"
            "q = deque([1, 2, 3])\n"
            "q.append(4)        # 오른쪽 추가\n"
            "q.appendleft(0)    # 왼쪽 추가\n"
            "print(q)           # deque([0, 1, 2, 3, 4])\n"
            "print(q.popleft()) # 0 (왼쪽 제거, O(1))\n"
            "print(q.pop())     # 4 (오른쪽 제거)\n"
            "\n"
            "# defaultdict: 그래프 인접 리스트\n"
            "graph = defaultdict(list)\n"
            "for a, b in [(1, 2), (1, 3), (2, 3)]:\n"
            "    graph[a].append(b)\n"
            "print(dict(graph))     # {1: [2, 3], 2: [3]}\n"
            "\n"
            "cnt = defaultdict(int)\n"
            "for ch in 'banana':\n"
            "    cnt[ch] += 1       # 키 확인 없이 누적\n"
            "print(dict(cnt))       # {'b':1,'a':3,'n':2}\n"
            "\n"
            "# Counter: 빈도수 + 최빈값\n"
            "c = Counter('mississippi')\n"
            "print(c.most_common(2))   # [('i', 4), ('s', 4)]\n"
        ),
    ),

    Lesson(
        id="py-mid-08",
        lang="python", level="중급",
        title="문자열 포맷팅 (f-string, join, split 심화)",
        summary="f-string 표현식·정렬·자릿수 · join · split/rsplit/splitlines",
        explanation=(
            "f-string 은 f'...' 안에 {식} 을 직접 넣어 문자열을 만드는 가장 빠르고 읽기 쉬운 방법이다.\n"
            "  중괄호 안에 변수뿐 아니라 식(a+b), 함수 호출도 넣을 수 있다.\n"
            "포맷 지정자: {x:.2f}(소수 둘째 자리), {x:5d}(폭 5 오른쪽 정렬), {x:<5}/{x:^5}(왼쪽/가운데),\n"
            "  {x:,}(천 단위 콤마), {x:05d}(앞을 0으로 채움), {x:b}/{x:x}(2진/16진).\n"
            "  {var=} 처럼 쓰면 '변수명=값' 형태로 디버깅 출력이 된다.\n"
            "join: '구분자'.join(문자열들) 은 여러 문자열을 하나로 잇는다(리스트 출력에 핵심, 매우 빠름).\n"
            "  숫자 리스트는 ' '.join(map(str, nums)) 처럼 문자열로 바꿔 넣어야 한다.\n"
            "split: s.split() 은 공백 기준으로 자르고, s.split(',') 는 구분자 지정, maxsplit 으로 횟수 제한,\n"
            "  rsplit 은 오른쪽부터, splitlines 는 줄 단위로 자른다."
        ),
        usage=(
            "출력 형식 맞추기(표, 소수 자릿수)에 f-string 이 표준이다. 코딩테스트에서는 "
            "여러 줄/여러 값 출력을 '\\n'.join(...) 으로 모아 한 번에 print 하면 출력이 빨라 시간초과를 피한다. "
            "split/map 조합은 입력 파싱의 기본이다."
        ),
        cons=(
            "f-string 안에서 같은 종류의 따옴표를 중첩하면 충돌하므로 바깥/안쪽 따옴표를 다르게 써야 한다.\n"
            "join 은 모든 원소가 문자열이어야 하며(숫자 섞이면 TypeError), 반대로 문자열 + 반복 연결은 느리다."
        ),
        code=(
            "name, score = '홍길동', 92.3456\n"
            "\n"
            "# f-string: 식, 자릿수, 정렬\n"
            "print(f'{name} 님 점수: {score:.1f}점')   # 92.3\n"
            "print(f'합계: {3 + 4}')                    # 식 삽입 → 7\n"
            "print(f'[{name:^8}]')                      # 가운데 정렬 폭 8\n"
            "print(f'{1234567:,}')                      # 천 단위 콤마\n"
            "print(f'{42:05d} / {255:x}')               # 00042 / ff\n"
            "\n"
            "# join: 리스트를 한 줄 문자열로\n"
            "words = ['파이썬', '자바', 'C++']\n"
            "print(', '.join(words))                    # 파이썬, 자바, C++\n"
            "nums = [3, 1, 4, 1, 5]\n"
            "print(' '.join(map(str, nums)))            # 3 1 4 1 5\n"
            "\n"
            "# split 심화\n"
            "print('a,b,c'.split(','))                  # ['a', 'b', 'c']\n"
            "print('a b c d'.split(maxsplit=1))         # ['a', 'b c d']\n"
            "print('x=1=2'.rsplit('=', 1))              # ['x=1', '2']\n"
            "print('line1\\nline2'.splitlines())        # ['line1', 'line2']\n"
        ),
    ),
]
