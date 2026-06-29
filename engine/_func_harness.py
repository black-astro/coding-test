"""함수 구현형(func) 문제를 별도 프로세스에서 실행하기 위한 하니스.

사용:
    python _func_harness.py <solution.py> <args.json> <func_name>

stdin/stdout 기반으로 동작하도록, 인자는 JSON 파일로 받고
함수 반환값을 repr() 로 표준출력에 찍는다. (채점기가 repr 끼리 비교)
"""

import sys
import json
import importlib.util


def main():
    sol_path, args_path, func_name = sys.argv[1], sys.argv[2], sys.argv[3]
    with open(args_path, "r", encoding="utf-8") as f:
        args = json.load(f)

    spec = importlib.util.spec_from_file_location("user_solution", sol_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    fn = getattr(module, func_name)
    result = fn(*args)
    sys.stdout.write(repr(result))


if __name__ == "__main__":
    main()
