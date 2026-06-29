"""문제 변형(랜덤 리셋) 생성기.

'구구단 2단' 의 2처럼, 문제의 변수 부분을 랜덤으로 바꿔 매번 다른 값으로
다시 풀 수 있게 한다. 각 생성기는 seed 로 시드된 rng 를 받아
{examples, testcases, description?} 를 돌려준다(원 문제 형식 그대로).

새 문제를 변형 가능하게 하려면 GENERATORS 에 id -> 생성기 를 추가하면 된다.
"""

import random
import string

# stdin 형: examples/testcases = {"input","output"}
# func  형: examples = {"args","output"}, testcases = {"args","expected"}


def _ab(rng):
    cases = []
    for _ in range(4):
        a, b = rng.randint(1, 9), rng.randint(1, 9)
        cases.append({"input": f"{a} {b}\n", "output": f"{a + b}\n"})
    return {"examples": cases[:2], "testcases": cases}


def _stars(rng):
    cases = []
    for _ in range(3):
        n = rng.randint(1, 7)
        out = "\n".join("*" * i for i in range(1, n + 1)) + "\n"
        cases.append({"input": f"{n}\n", "output": out})
    return {"examples": cases[:2], "testcases": cases}


def _even_odd(rng):
    cases, ex = [], []
    for _ in range(4):
        n = rng.randint(0, 9999)
        cases.append({"args": [n], "expected": "Even" if n % 2 == 0 else "Odd"})
    ex = [{"args": c["args"], "output": c["expected"]} for c in cases[:2]]
    return {"examples": ex, "testcases": cases}


def _max_val(rng):
    cases = []
    for _ in range(4):
        n = rng.randint(1, 8)
        arr = [rng.randint(-50, 50) for _ in range(n)]
        cases.append({"input": f"{n}\n{' '.join(map(str, arr))}\n", "output": f"{max(arr)}\n"})
    return {"examples": cases[:2], "testcases": cases}


def _reverse(rng):
    cases = []
    for _ in range(4):
        ln = rng.randint(1, 9)
        s = "".join(rng.choice(string.ascii_letters + string.digits) for _ in range(ln))
        cases.append({"args": [s], "expected": s[::-1]})
    ex = [{"args": c["args"], "output": c["expected"]} for c in cases[:2]]
    return {"examples": ex, "testcases": cases}


def _sort_numbers(rng):
    cases = []
    for _ in range(3):
        n = rng.randint(1, 7)
        arr = [rng.randint(-99, 99) for _ in range(n)]
        inp = f"{n}\n" + "".join(f"{x}\n" for x in arr)
        out = "".join(f"{x}\n" for x in sorted(arr))
        cases.append({"input": inp, "output": out})
    return {"examples": cases[:1], "testcases": cases}


def _gugudan(rng):
    cases = []
    for _ in range(3):
        n = rng.randint(2, 9)
        out = "".join(f"{n} * {i} = {n * i}\n" for i in range(1, 10))
        cases.append({"input": f"{n}\n", "output": out})
    desc = (f"N을 입력받아 N단의 구구단을 출력하는 프로그램을 작성하시오. "
            f"출력 형식은 'N * i = N*i' 이다. (이번 변형 예시는 {cases[0]['input'].strip()}단)")
    return {"examples": cases[:1], "testcases": cases, "description": desc}


def _mult_table(rng):
    cases, ex = [], []
    for _ in range(3):
        n = rng.randint(1, 6)
        table = [[i * j for j in range(1, n + 1)] for i in range(1, n + 1)]
        cases.append({"args": [n], "expected": table})
    ex = [{"args": c["args"], "output": c["expected"]} for c in cases[:2]]
    return {"examples": ex, "testcases": cases}


GENERATORS = {
    "bronze-01": _ab,
    "bronze-02": _stars,
    "bronze-03": _even_odd,
    "bronze-04": _max_val,
    "bronze-05": _reverse,
    "bronze-28": _gugudan,
    "bronze-29": _mult_table,
    "silver-01": _sort_numbers,
}


def has(problem_id: str) -> bool:
    return problem_id in GENERATORS


def make(problem_id: str, seed) -> dict:
    rng = random.Random(f"{seed}:{problem_id}")
    return GENERATORS[problem_id](rng)


def variantable_ids():
    return list(GENERATORS.keys())
