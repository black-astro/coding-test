# -*- coding: utf-8 -*-
"""SQL 고급 문제 sql-35 ~ sql-50.

SQLD 고급 활용(서브쿼리/집합 연산/윈도우 함수) 실전 수준.
서브쿼리 → CASE 피벗 → 집합 연산 → 문자열/날짜 → 윈도우 → CTE → 종합.
SQLite 문법 기준(윈도우 함수/CTE 는 SQLite 3.25+ 지원).
"""
from engine.models import Problem

PROBLEMS_PART = [
    # ------------------------------------------------------------------
    # sql-35 스칼라 서브쿼리 (중첩) — 2위 점수 찾기
    # ------------------------------------------------------------------
    Problem(
        id="sql-35",
        rank="Gold",
        title="2위 점수 받은 사람 전부 찾기 (중첩 스칼라 서브쿼리)",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "사내 자격시험에서 '2위 점수'를 받은 사람을 모두 찾아야 한다.\n"
            "여기서 2위 점수란 사람 기준이 아니라 점수 기준이다:\n"
            "최고 점수 다음으로 높은 '서로 다른 점수' 중 최댓값.\n"
            "예) 점수가 97,97,91,88 이면 2위 점수는 91 이다.\n"
            "2위 점수를 받은 사람이 여러 명이면 모두 출력한다.\n\n"
            "테이블 스키마:\n"
            "  exam_result(name TEXT, score INTEGER)\n"
            "    - name  : 응시자 이름 (중복 없음)\n"
            "    - score : 시험 점수 (0~100, 서로 다른 점수가 2개 이상 존재)\n\n"
            "2위 점수를 받은 응시자의 이름과 점수를 조회하라.\n"
        ),
        input_desc="채점 시 테스트케이스의 CREATE/INSERT 스크립트로 테이블이 자동 생성된다. SELECT 문 하나만 작성하면 된다.",
        output_desc="name, score 두 컬럼. name 오름차순 정렬.",
        examples=[{
            "input": (
                "exam_result\n"
                "name   | score\n"
                "-------+------\n"
                "김민준 | 88\n"
                "이서연 | 97\n"
                "박도윤 | 75\n"
                "최지우 | 91\n"
                "정하은 | 64\n"
                "강시우 | 91\n"
                "윤서아 | 82"
            ),
            "output": "",
        }],
        hints=[
            "2위 점수 = '최고 점수보다 작은 점수들 중의 최댓값'. MAX 를 두 번 겹쳐 쓰면 된다.",
            "(SELECT MAX(score) FROM exam_result WHERE score < (SELECT MAX(score) FROM exam_result)) — 안쪽 서브쿼리가 1위 점수, 바깥이 그보다 작은 것들의 MAX = 2위 점수.",
            "SELECT name, score FROM exam_result WHERE score = (SELECT MAX(score) FROM exam_result WHERE score < (SELECT MAX(score) FROM exam_result)) ORDER BY name;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE exam_result(name TEXT, score INTEGER);\n"
                    "INSERT INTO exam_result VALUES\n"
                    "('김민준',88),('이서연',97),('박도윤',75),('최지우',91),\n"
                    "('정하은',64),('강시우',91),('윤서아',82);"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE exam_result(name TEXT, score INTEGER);\n"
                    "INSERT INTO exam_result VALUES\n"
                    "('한지민',55),('오세훈',73),('신유나',92),('임재현',61),\n"
                    "('송가을',89),('문준호',89),('배소율',92);"
                ),
                "output": "",
            },
        ],
        reference_sql=(
            "SELECT name, score FROM exam_result "
            "WHERE score = (SELECT MAX(score) FROM exam_result "
            "WHERE score < (SELECT MAX(score) FROM exam_result)) "
            "ORDER BY name;"
        ),
        tier="G3",
        freq=2,
    ),

    # ------------------------------------------------------------------
    # sql-36 3중 IN 서브쿼리
    # ------------------------------------------------------------------
    Problem(
        id="sql-36",
        rank="Gold",
        title="서울 고객이 주문한 상품 (3중 IN 서브쿼리)",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "쇼핑몰이 서울 지역 프로모션 효과를 분석한다.\n"
            "'서울' 거주 고객이 한 번이라도 주문한 상품 목록이 필요하다.\n"
            "고객 → 주문 → 상품으로 이어지는 3단계를 IN 서브쿼리 중첩으로 푼다.\n\n"
            "테이블 스키마:\n"
            "  customers(cust_id INTEGER, name TEXT, city TEXT)\n"
            "    - cust_id : 고객 번호 (고유)\n"
            "    - city    : 거주 도시\n"
            "  orders(order_id INTEGER, cust_id INTEGER, product_id INTEGER)\n"
            "    - order_id   : 주문 번호 (고유)\n"
            "    - cust_id    : 주문 고객 번호\n"
            "    - product_id : 주문 상품 번호\n"
            "  products(product_id INTEGER, name TEXT, price INTEGER)\n"
            "    - product_id : 상품 번호 (고유)\n\n"
            "city 가 '서울' 인 고객이 주문한 상품의 번호·이름·가격을 조회하라.\n"
            "같은 상품이 여러 번 주문돼도 한 번만 출력한다.\n"
        ),
        input_desc="채점 시 테스트케이스의 CREATE/INSERT 스크립트로 테이블이 자동 생성된다. SELECT 문 하나만 작성하면 된다.",
        output_desc="product_id, name, price 세 컬럼. product_id 오름차순 정렬.",
        examples=[{
            "input": (
                "customers\n"
                "cust_id | name   | city\n"
                "--------+--------+-----\n"
                "1       | 김하나 | 서울\n"
                "2       | 박두리 | 부산\n"
                "3       | 이세찬 | 서울\n"
                "4       | 정네온 | 대구\n"
                "5       | 오다미 | 서울\n\n"
                "orders\n"
                "order_id | cust_id | product_id\n"
                "---------+---------+-----------\n"
                "1        | 1       | 3\n"
                "2        | 2       | 5\n"
                "3        | 3       | 3\n"
                "4        | 1       | 6\n"
                "5        | 4       | 2\n"
                "6        | 5       | 7\n"
                "7        | 2       | 1\n\n"
                "products\n"
                "product_id | name         | price\n"
                "-----------+--------------+-------\n"
                "1          | 무선마우스   | 25000\n"
                "2          | 기계식키보드 | 89000\n"
                "3          | 모니터암     | 45000\n"
                "4          | 웹캠         | 60000\n"
                "5          | USB허브      | 15000\n"
                "6          | 노트북거치대 | 32000\n"
                "7          | 마이크       | 120000"
            ),
            "output": "",
        }],
        hints=[
            "안쪽부터: 서울 고객의 cust_id 목록 → 그 고객들의 주문에서 product_id 목록 → 그 목록에 속한 상품. IN 을 두 번 겹친다.",
            "WHERE product_id IN (SELECT product_id FROM orders WHERE cust_id IN (SELECT cust_id FROM customers WHERE city = '서울')) — 안쪽 서브쿼리 결과가 바깥 IN 의 목록이 된다.",
            "SELECT product_id, name, price FROM products WHERE product_id IN (SELECT product_id FROM orders WHERE cust_id IN (SELECT cust_id FROM customers WHERE city = '서울')) ORDER BY product_id;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE customers(cust_id INTEGER, name TEXT, city TEXT);\n"
                    "INSERT INTO customers VALUES\n"
                    "(1,'김하나','서울'),(2,'박두리','부산'),(3,'이세찬','서울'),\n"
                    "(4,'정네온','대구'),(5,'오다미','서울');\n"
                    "CREATE TABLE orders(order_id INTEGER, cust_id INTEGER, product_id INTEGER);\n"
                    "INSERT INTO orders VALUES\n"
                    "(1,1,3),(2,2,5),(3,3,3),(4,1,6),(5,4,2),(6,5,7),(7,2,1);\n"
                    "CREATE TABLE products(product_id INTEGER, name TEXT, price INTEGER);\n"
                    "INSERT INTO products VALUES\n"
                    "(1,'무선마우스',25000),(2,'기계식키보드',89000),(3,'모니터암',45000),\n"
                    "(4,'웹캠',60000),(5,'USB허브',15000),(6,'노트북거치대',32000),(7,'마이크',120000);"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE customers(cust_id INTEGER, name TEXT, city TEXT);\n"
                    "INSERT INTO customers VALUES\n"
                    "(1,'한가온','서울'),(2,'나봄','인천'),(3,'마리솔','서울'),(4,'라윤','대전');\n"
                    "CREATE TABLE orders(order_id INTEGER, cust_id INTEGER, product_id INTEGER);\n"
                    "INSERT INTO orders VALUES\n"
                    "(1,2,1),(2,1,4),(3,3,4),(4,3,2),(5,4,6),(6,1,5);\n"
                    "CREATE TABLE products(product_id INTEGER, name TEXT, price INTEGER);\n"
                    "INSERT INTO products VALUES\n"
                    "(1,'생수',800),(2,'컵라면',1200),(3,'삼각김밥',1500),\n"
                    "(4,'커피',2000),(5,'과자',1700),(6,'아이스크림',2500);"
                ),
                "output": "",
            },
        ],
        reference_sql=(
            "SELECT product_id, name, price FROM products "
            "WHERE product_id IN (SELECT product_id FROM orders "
            "WHERE cust_id IN (SELECT cust_id FROM customers WHERE city = '서울')) "
            "ORDER BY product_id;"
        ),
        tier="G3",
        freq=2,
    ),

    # ------------------------------------------------------------------
    # sql-37 이중 NOT EXISTS — division (모든 필수 교육 이수)
    # ------------------------------------------------------------------
    Problem(
        id="sql-37",
        rank="Gold",
        title="필수 교육을 전부 이수한 직원 (이중 NOT EXISTS)",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "인사팀이 법정 필수 교육을 '하나도 빠짐없이' 이수한 직원을 찾는다.\n"
            "'모든 X 를 만족하는 행 찾기'는 관계 나눗셈(division) 문제로,\n"
            "SQL 에는 FOR ALL 이 없어 이중 부정으로 푼다:\n"
            "\"이수하지 않은 필수 교육이 존재하지 않는 직원\" = NOT EXISTS 안에 NOT EXISTS.\n\n"
            "테이블 스키마:\n"
            "  employees(emp_name TEXT)              -- 직원 이름 (고유)\n"
            "  required_courses(course TEXT)         -- 필수 교육명 (고유, 1개 이상)\n"
            "  completions(emp_name TEXT, course TEXT)\n"
            "    - 직원이 이수한 교육 기록 (필수가 아닌 교육도 섞여 있음)\n\n"
            "필수 교육을 전부 이수한 직원의 이름을 조회하라.\n"
        ),
        input_desc="채점 시 테스트케이스의 CREATE/INSERT 스크립트로 테이블이 자동 생성된다. SELECT 문 하나만 작성하면 된다.",
        output_desc="emp_name 한 컬럼. emp_name 오름차순 정렬.",
        examples=[{
            "input": (
                "employees\n"
                "emp_name\n"
                "--------\n"
                "강단비\n"
                "김무진\n"
                "박초이\n"
                "이든해\n"
                "최라율\n\n"
                "required_courses\n"
                "course\n"
                "-------------\n"
                "보안교육\n"
                "성희롱예방\n"
                "개인정보보호\n\n"
                "completions\n"
                "emp_name | course\n"
                "---------+-------------\n"
                "강단비   | 보안교육\n"
                "강단비   | 성희롱예방\n"
                "강단비   | 개인정보보호\n"
                "강단비   | 직무리더십\n"
                "김무진   | 보안교육\n"
                "김무진   | 개인정보보호\n"
                "박초이   | 성희롱예방\n"
                "박초이   | 보안교육\n"
                "박초이   | 개인정보보호\n"
                "이든해   | 성희롱예방\n"
                "최라율   | 직무리더십"
            ),
            "output": "",
        }],
        hints=[
            "'모든 필수 교육을 이수' = '안 들은 필수 교육이 하나도 없다'로 뒤집어라. 부정을 두 번 쓰면 전칭(FOR ALL)이 된다.",
            "바깥: 직원마다 검사. 안쪽 1: 필수 교육 중 (안쪽 2: 그 직원의 이수 기록에 없는) 것이 존재하는가 → NOT EXISTS 로 그런 교육이 없어야 통과.",
            "SELECT e.emp_name FROM employees e WHERE NOT EXISTS (SELECT 1 FROM required_courses r WHERE NOT EXISTS (SELECT 1 FROM completions c WHERE c.emp_name = e.emp_name AND c.course = r.course)) ORDER BY e.emp_name;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE employees(emp_name TEXT);\n"
                    "INSERT INTO employees VALUES ('강단비'),('김무진'),('박초이'),('이든해'),('최라율');\n"
                    "CREATE TABLE required_courses(course TEXT);\n"
                    "INSERT INTO required_courses VALUES ('보안교육'),('성희롱예방'),('개인정보보호');\n"
                    "CREATE TABLE completions(emp_name TEXT, course TEXT);\n"
                    "INSERT INTO completions VALUES\n"
                    "('강단비','보안교육'),('강단비','성희롱예방'),('강단비','개인정보보호'),\n"
                    "('강단비','직무리더십'),('김무진','보안교육'),('김무진','개인정보보호'),\n"
                    "('박초이','성희롱예방'),('박초이','보안교육'),('박초이','개인정보보호'),\n"
                    "('이든해','성희롱예방'),('최라율','직무리더십');"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE employees(emp_name TEXT);\n"
                    "INSERT INTO employees VALUES ('노기쁨'),('도삼돌'),('모아진'),('소금별');\n"
                    "CREATE TABLE required_courses(course TEXT);\n"
                    "INSERT INTO required_courses VALUES ('안전교육'),('윤리교육');\n"
                    "CREATE TABLE completions(emp_name TEXT, course TEXT);\n"
                    "INSERT INTO completions VALUES\n"
                    "('노기쁨','안전교육'),('도삼돌','안전교육'),('도삼돌','윤리교육'),\n"
                    "('모아진','윤리교육'),('모아진','안전교육'),('모아진','전산교육'),\n"
                    "('소금별','전산교육');"
                ),
                "output": "",
            },
        ],
        reference_sql=(
            "SELECT e.emp_name FROM employees e "
            "WHERE NOT EXISTS (SELECT 1 FROM required_courses r "
            "WHERE NOT EXISTS (SELECT 1 FROM completions c "
            "WHERE c.emp_name = e.emp_name AND c.course = r.course)) "
            "ORDER BY e.emp_name;"
        ),
        tier="G1",
        freq=1,
    ),

    # ------------------------------------------------------------------
    # sql-38 상관 서브쿼리 — 부서별 최고 연봉자 (동률 포함)
    # ------------------------------------------------------------------
    Problem(
        id="sql-38",
        rank="Gold",
        title="부서별 최고 연봉자 (상관 서브쿼리, 동률 처리)",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "인사팀이 부서마다 연봉이 가장 높은 직원을 조사한다.\n"
            "부서별 최고 연봉은 부서마다 다르므로, 바깥 행의 부서 값을 참조하는\n"
            "상관 서브쿼리(correlated subquery)가 필요하다.\n"
            "GROUP BY + MAX 만으로는 '그 연봉을 받는 사람이 누구인지'를 안전하게\n"
            "못 가져온다는 점이 포인트다(동률자가 누락되거나 임의로 붙는다).\n\n"
            "테이블 스키마:\n"
            "  employees(emp_id INTEGER, name TEXT, dept TEXT, salary INTEGER)\n"
            "    - emp_id : 사번 (고유)\n"
            "    - name   : 이름 (중복 없음)\n"
            "    - dept   : 부서명\n"
            "    - salary : 연봉(만원)\n\n"
            "각 부서에서 연봉이 가장 높은 직원의 부서·이름·연봉을 조회하라.\n"
            "한 부서에 최고 연봉 동률자가 여러 명이면 반드시 모두 출력한다.\n"
        ),
        input_desc="채점 시 테스트케이스의 CREATE/INSERT 스크립트로 테이블이 자동 생성된다. SELECT 문 하나만 작성하면 된다.",
        output_desc="dept, name, salary 세 컬럼. dept 오름차순, 같은 부서면 name 오름차순 정렬.",
        examples=[{
            "input": (
                "employees\n"
                "emp_id | name   | dept | salary\n"
                "-------+--------+------+-------\n"
                "1      | 김철수 | 개발 | 5200\n"
                "2      | 이영희 | 개발 | 6100\n"
                "3      | 박민수 | 영업 | 4800\n"
                "4      | 최수진 | 영업 | 4800\n"
                "5      | 정대현 | 인사 | 3900\n"
                "6      | 강미래 | 개발 | 5700\n"
                "7      | 윤태호 | 인사 | 4200"
            ),
            "output": "",
        }],
        hints=[
            "행마다 '내가 속한 부서의 최고 연봉'과 내 연봉을 비교하면 된다. 서브쿼리가 바깥 쿼리의 dept 를 참조해야 한다.",
            "WHERE e.salary = (SELECT MAX(salary) FROM employees x WHERE x.dept = e.dept) — 서브쿼리 안에서 바깥 별칭 e 를 쓰는 것이 상관 서브쿼리다. 동률이면 = 비교로 둘 다 남는다.",
            "SELECT e.dept, e.name, e.salary FROM employees e WHERE e.salary = (SELECT MAX(salary) FROM employees x WHERE x.dept = e.dept) ORDER BY e.dept, e.name;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE employees(emp_id INTEGER, name TEXT, dept TEXT, salary INTEGER);\n"
                    "INSERT INTO employees VALUES\n"
                    "(1,'김철수','개발',5200),(2,'이영희','개발',6100),(3,'박민수','영업',4800),\n"
                    "(4,'최수진','영업',4800),(5,'정대현','인사',3900),(6,'강미래','개발',5700),\n"
                    "(7,'윤태호','인사',4200);"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE employees(emp_id INTEGER, name TEXT, dept TEXT, salary INTEGER);\n"
                    "INSERT INTO employees VALUES\n"
                    "(1,'서지수','기획',4500),(2,'문성민','기획',5100),(3,'임채원','디자인',4300),\n"
                    "(4,'배현우','디자인',4300),(5,'송민아','마케팅',4700),(6,'조은별','마케팅',5300),\n"
                    "(7,'황인성','기획',4900),(8,'노아름','디자인',3800);"
                ),
                "output": "",
            },
        ],
        reference_sql=(
            "SELECT e.dept, e.name, e.salary FROM employees e "
            "WHERE e.salary = (SELECT MAX(salary) FROM employees x WHERE x.dept = e.dept) "
            "ORDER BY e.dept, e.name;"
        ),
        tier="G2",
        freq=2,
    ),

    # ------------------------------------------------------------------
    # sql-39 CASE 분류 후 재집계 (서브쿼리 2단계)
    # ------------------------------------------------------------------
    Problem(
        id="sql-39",
        rank="Gold",
        title="등급별 인원과 평균 점수 (CASE 분류 후 재집계)",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "어학시험 결과를 등급으로 나눈 뒤, '등급별' 통계를 내야 한다.\n"
            "등급 기준:\n"
            "  - 90점 이상        : 'A'\n"
            "  - 80점 이상 90 미만: 'B'\n"
            "  - 70점 이상 80 미만: 'C'\n"
            "  - 70점 미만        : 'F'\n"
            "CASE 로 만든 파생 컬럼(grade)을 기준으로 다시 GROUP BY 해야 하므로,\n"
            "인라인 뷰(FROM 절 서브쿼리)로 2단계 구조를 만든다.\n\n"
            "테이블 스키마:\n"
            "  test_score(name TEXT, score INTEGER)\n"
            "    - name  : 응시자 이름 (중복 없음)\n"
            "    - score : 점수 (0~100)\n\n"
            "등급별 인원수(cnt)와 평균 점수(avg_score, 소수 첫째 자리 반올림)를 조회하라.\n"
            "응시자가 없는 등급은 출력하지 않는다.\n"
        ),
        input_desc="채점 시 테스트케이스의 CREATE/INSERT 스크립트로 테이블이 자동 생성된다. SELECT 문 하나만 작성하면 된다.",
        output_desc="grade, cnt, avg_score 세 컬럼. grade 오름차순(A,B,C,F 문자 순) 정렬.",
        examples=[{
            "input": (
                "test_score\n"
                "name   | score\n"
                "-------+------\n"
                "김민아 | 95\n"
                "박서준 | 82\n"
                "이하늘 | 74\n"
                "최다연 | 91\n"
                "정우진 | 68\n"
                "한소미 | 88\n"
                "오건우 | 79"
            ),
            "output": "",
        }],
        hints=[
            "1단계에서 각 행에 CASE 로 grade 를 붙이고, 2단계에서 그 grade 로 GROUP BY 한다. FROM (SELECT ...) 인라인 뷰를 쓰면 된다.",
            "FROM (SELECT score, CASE WHEN score >= 90 THEN 'A' ... END AS grade FROM test_score) t GROUP BY grade — 파생 컬럼을 바깥에서 일반 컬럼처럼 쓸 수 있다. 평균은 ROUND(AVG(score), 1).",
            "SELECT grade, COUNT(*) AS cnt, ROUND(AVG(score), 1) AS avg_score FROM (SELECT score, CASE WHEN score >= 90 THEN 'A' WHEN score >= 80 THEN 'B' WHEN score >= 70 THEN 'C' ELSE 'F' END AS grade FROM test_score) t GROUP BY grade ORDER BY grade;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE test_score(name TEXT, score INTEGER);\n"
                    "INSERT INTO test_score VALUES\n"
                    "('김민아',95),('박서준',82),('이하늘',74),('최다연',91),\n"
                    "('정우진',68),('한소미',88),('오건우',79);"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE test_score(name TEXT, score INTEGER);\n"
                    "INSERT INTO test_score VALUES\n"
                    "('강예린',90),('임도훈',59),('신보라',85),('전민규',77),\n"
                    "('백지호',93),('유세라',70);"
                ),
                "output": "",
            },
        ],
        reference_sql=(
            "SELECT grade, COUNT(*) AS cnt, ROUND(AVG(score), 1) AS avg_score "
            "FROM (SELECT score, "
            "CASE WHEN score >= 90 THEN 'A' WHEN score >= 80 THEN 'B' "
            "WHEN score >= 70 THEN 'C' ELSE 'F' END AS grade "
            "FROM test_score) t "
            "GROUP BY grade ORDER BY grade;"
        ),
        tier="G3",
        freq=2,
    ),

    # ------------------------------------------------------------------
    # sql-40 CASE 피벗 — 월별 컬럼 전개
    # ------------------------------------------------------------------
    Problem(
        id="sql-40",
        rank="Gold",
        title="카테고리별 1~3월 매출 피벗 (CASE 컬럼 전개)",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "유통사 1분기 결산 보고서: 행은 상품 카테고리, 열은 월(1월/2월/3월)인\n"
            "피벗 표를 SQL 로 만들어야 한다.\n"
            "세로로 쌓인 판매 기록을 CASE WHEN + 집계로 가로로 펼친다.\n\n"
            "테이블 스키마:\n"
            "  sales(sale_id INTEGER, category TEXT, sale_date TEXT, amount INTEGER)\n"
            "    - sale_id   : 판매 번호 (고유)\n"
            "    - category  : 상품 카테고리\n"
            "    - sale_date : 판매일 'YYYY-MM-DD' (2024년 1~3월 데이터만 존재)\n"
            "    - amount    : 판매 금액(원)\n\n"
            "카테고리별로 1월 매출(m1), 2월 매출(m2), 3월 매출(m3),\n"
            "분기 합계(total)를 조회하라. 매출이 없는 달은 0 으로 표시한다.\n"
        ),
        input_desc="채점 시 테스트케이스의 CREATE/INSERT 스크립트로 테이블이 자동 생성된다. SELECT 문 하나만 작성하면 된다.",
        output_desc="category, m1, m2, m3, total 다섯 컬럼. category 오름차순 정렬.",
        examples=[{
            "input": (
                "sales\n"
                "sale_id | category | sale_date  | amount\n"
                "--------+----------+------------+-------\n"
                "1       | 가전     | 2024-01-12 | 300000\n"
                "2       | 식품     | 2024-01-20 | 45000\n"
                "3       | 의류     | 2024-02-05 | 120000\n"
                "4       | 가전     | 2024-02-18 | 250000\n"
                "5       | 식품     | 2024-02-25 | 52000\n"
                "6       | 의류     | 2024-03-03 | 98000\n"
                "7       | 가전     | 2024-03-15 | 410000\n"
                "8       | 식품     | 2024-03-22 | 61000\n"
                "9       | 의류     | 2024-01-28 | 87000\n"
                "10      | 식품     | 2024-01-05 | 33000"
            ),
            "output": "",
        }],
        hints=[
            "GROUP BY category 한 줄 안에서 월별로 나눠 더해야 한다. 집계 함수 안에 월 판별 CASE 를 넣는다.",
            "SUM(CASE WHEN strftime('%m', sale_date) = '01' THEN amount ELSE 0 END) AS m1 — 1월 행만 금액을 더하고 나머지는 0. 이를 '02','03' 으로 반복하면 열이 펼쳐진다.",
            "SELECT category, SUM(CASE WHEN strftime('%m',sale_date)='01' THEN amount ELSE 0 END) AS m1, SUM(CASE WHEN strftime('%m',sale_date)='02' THEN amount ELSE 0 END) AS m2, SUM(CASE WHEN strftime('%m',sale_date)='03' THEN amount ELSE 0 END) AS m3, SUM(amount) AS total FROM sales GROUP BY category ORDER BY category;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE sales(sale_id INTEGER, category TEXT, sale_date TEXT, amount INTEGER);\n"
                    "INSERT INTO sales VALUES\n"
                    "(1,'가전','2024-01-12',300000),(2,'식품','2024-01-20',45000),\n"
                    "(3,'의류','2024-02-05',120000),(4,'가전','2024-02-18',250000),\n"
                    "(5,'식품','2024-02-25',52000),(6,'의류','2024-03-03',98000),\n"
                    "(7,'가전','2024-03-15',410000),(8,'식품','2024-03-22',61000),\n"
                    "(9,'의류','2024-01-28',87000),(10,'식품','2024-01-05',33000);"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE sales(sale_id INTEGER, category TEXT, sale_date TEXT, amount INTEGER);\n"
                    "INSERT INTO sales VALUES\n"
                    "(1,'도서','2024-01-08',15000),(2,'문구','2024-01-15',7000),\n"
                    "(3,'도서','2024-02-11',22000),(4,'문구','2024-03-06',9500),\n"
                    "(5,'도서','2024-03-27',18000),(6,'문구','2024-02-19',4500),\n"
                    "(7,'도서','2024-01-30',27000),(8,'문구','2024-03-25',12000);"
                ),
                "output": "",
            },
        ],
        reference_sql=(
            "SELECT category, "
            "SUM(CASE WHEN strftime('%m', sale_date) = '01' THEN amount ELSE 0 END) AS m1, "
            "SUM(CASE WHEN strftime('%m', sale_date) = '02' THEN amount ELSE 0 END) AS m2, "
            "SUM(CASE WHEN strftime('%m', sale_date) = '03' THEN amount ELSE 0 END) AS m3, "
            "SUM(amount) AS total "
            "FROM sales GROUP BY category ORDER BY category;"
        ),
        tier="G2",
        freq=2,
    ),

    # ------------------------------------------------------------------
    # sql-41 UNION ALL 함정 — 중복을 보존해야 하는 집계
    # ------------------------------------------------------------------
    Problem(
        id="sql-41",
        rank="Gold",
        title="두 매장 방문 횟수 합산 (UNION vs UNION ALL 함정)",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "카페 본점과 분점의 방문 기록을 합쳐 회원별 총 방문 횟수를 구한다.\n"
            "같은 회원이 같은 매장을 여러 번 방문한 기록도 각각 1회로 세야 한다.\n\n"
            "★ 함정: UNION 은 중복 행을 제거하므로 방문 횟수가 사라진다.\n"
            "  기록을 '전부' 보존하며 이어 붙이려면 UNION ALL 을 써야 한다.\n"
            "  (SQLD 단골 출제 포인트: UNION = 중복 제거+정렬 비용, UNION ALL = 전부 유지)\n\n"
            "테이블 스키마:\n"
            "  visits_main(name TEXT)    -- 본점 방문 기록 (방문 1회당 1행, 중복 존재)\n"
            "  visits_sub(name TEXT)     -- 분점 방문 기록 (방문 1회당 1행, 중복 존재)\n\n"
            "두 매장 기록을 합쳐 회원별 총 방문 횟수(visit_cnt)를 조회하라.\n"
        ),
        input_desc="채점 시 테스트케이스의 CREATE/INSERT 스크립트로 테이블이 자동 생성된다. SELECT 문 하나만 작성하면 된다.",
        output_desc="name, visit_cnt 두 컬럼. visit_cnt 내림차순, 같으면 name 오름차순 정렬.",
        examples=[{
            "input": (
                "visits_main\n"
                "name\n"
                "------\n"
                "김온유\n"
                "김온유\n"
                "박하람\n"
                "이슬비\n"
                "정다운\n"
                "이슬비\n\n"
                "visits_sub\n"
                "name\n"
                "------\n"
                "김온유\n"
                "윤새봄\n"
                "이슬비\n"
                "윤새봄\n"
                "한바다"
            ),
            "output": "",
        }],
        hints=[
            "두 테이블을 세로로 이어 붙인 뒤 이름별로 COUNT 하면 된다. 단, 이어 붙일 때 중복 행이 지워지면 횟수가 틀어진다.",
            "UNION 은 중복을 제거해 '김온유 3회'가 '1회'로 뭉개진다. 기록 보존에는 UNION ALL. 이어 붙인 결과는 FROM 절 서브쿼리(인라인 뷰)로 감싸 GROUP BY 한다.",
            "SELECT name, COUNT(*) AS visit_cnt FROM (SELECT name FROM visits_main UNION ALL SELECT name FROM visits_sub) v GROUP BY name ORDER BY visit_cnt DESC, name;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE visits_main(name TEXT);\n"
                    "INSERT INTO visits_main VALUES ('김온유'),('김온유'),('박하람'),('이슬비'),('정다운'),('이슬비');\n"
                    "CREATE TABLE visits_sub(name TEXT);\n"
                    "INSERT INTO visits_sub VALUES ('김온유'),('윤새봄'),('이슬비'),('윤새봄'),('한바다');"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE visits_main(name TEXT);\n"
                    "INSERT INTO visits_main VALUES ('고운결'),('나예솔'),('고운결'),('도한별'),('고운결');\n"
                    "CREATE TABLE visits_sub(name TEXT);\n"
                    "INSERT INTO visits_sub VALUES ('나예솔'),('마루한'),('나예솔'),('도한별'),('서리아'),('마루한');"
                ),
                "output": "",
            },
        ],
        reference_sql=(
            "SELECT name, COUNT(*) AS visit_cnt "
            "FROM (SELECT name FROM visits_main UNION ALL SELECT name FROM visits_sub) v "
            "GROUP BY name ORDER BY visit_cnt DESC, name;"
        ),
        tier="G3",
        freq=2,
    ),

    # ------------------------------------------------------------------
    # sql-42 문자열 함수 — 아이디 추출 + 이메일 마스킹
    # ------------------------------------------------------------------
    Problem(
        id="sql-42",
        rank="Gold",
        title="이메일 아이디 추출과 마스킹 (문자열 함수 조합)",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "개인정보 노출을 줄이기 위해 회원 이메일을 가공해 보여줘야 한다.\n"
            "  1) login_id : '@' 앞부분을 대문자로 변환\n"
            "  2) masked   : 아이디 첫 글자 + '***@' + 도메인\n"
            "     예) sunpark@webmail.com → s***@webmail.com\n\n"
            "테이블 스키마:\n"
            "  members(member_id INTEGER, name TEXT, email TEXT)\n"
            "    - member_id : 회원 번호 (고유)\n"
            "    - name      : 이름\n"
            "    - email     : 이메일 (반드시 '@' 를 정확히 1개 포함, 아이디 2자 이상)\n\n"
            "회원 번호·이름·login_id·masked 를 조회하라.\n"
            "SQLite 문자열 함수: SUBSTR(문자열, 시작[, 길이]), INSTR(문자열, 찾을문자),\n"
            "LENGTH, UPPER/LOWER, REPLACE, || (문자열 연결)\n"
        ),
        input_desc="채점 시 테스트케이스의 CREATE/INSERT 스크립트로 테이블이 자동 생성된다. SELECT 문 하나만 작성하면 된다.",
        output_desc="member_id, name, login_id, masked 네 컬럼. member_id 오름차순 정렬.",
        examples=[{
            "input": (
                "members\n"
                "member_id | name   | email\n"
                "----------+--------+----------------------\n"
                "1         | 김유정 | yjkim@mailbox.kr\n"
                "2         | 박태양 | sunpark@webmail.com\n"
                "3         | 이초록 | green.lee@mailbox.kr\n"
                "4         | 최바다 | sea.choi@oceanmail.net\n"
                "5         | 정별님 | star.jung@webmail.com"
            ),
            "output": "",
        }],
        hints=[
            "'@' 위치를 INSTR 로 찾으면 앞(아이디)과 뒤(도메인)를 SUBSTR 로 자를 수 있다. 마스킹은 조각들을 || 로 이어 붙인다.",
            "아이디: SUBSTR(email, 1, INSTR(email,'@') - 1), 도메인: SUBSTR(email, INSTR(email,'@') + 1). 마스킹: SUBSTR(email,1,1) || '***@' || 도메인.",
            "SELECT member_id, name, UPPER(SUBSTR(email, 1, INSTR(email,'@') - 1)) AS login_id, SUBSTR(email, 1, 1) || '***@' || SUBSTR(email, INSTR(email,'@') + 1) AS masked FROM members ORDER BY member_id;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE members(member_id INTEGER, name TEXT, email TEXT);\n"
                    "INSERT INTO members VALUES\n"
                    "(1,'김유정','yjkim@mailbox.kr'),(2,'박태양','sunpark@webmail.com'),\n"
                    "(3,'이초록','green.lee@mailbox.kr'),(4,'최바다','sea.choi@oceanmail.net'),\n"
                    "(5,'정별님','star.jung@webmail.com');"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE members(member_id INTEGER, name TEXT, email TEXT);\n"
                    "INSERT INTO members VALUES\n"
                    "(1,'한결','hangyeol@devhub.io'),(2,'서준희','jhseo@codenet.kr'),\n"
                    "(3,'임보검','bogum.lim@devhub.io'),(4,'남하늬','sky.nam@cloudpost.com'),\n"
                    "(5,'표은호','eunho.pyo@codenet.kr'),(6,'길채원','cw.gil@cloudpost.com');"
                ),
                "output": "",
            },
        ],
        reference_sql=(
            "SELECT member_id, name, "
            "UPPER(SUBSTR(email, 1, INSTR(email, '@') - 1)) AS login_id, "
            "SUBSTR(email, 1, 1) || '***@' || SUBSTR(email, INSTR(email, '@') + 1) AS masked "
            "FROM members ORDER BY member_id;"
        ),
        tier="G3",
        freq=1,
    ),

    # ------------------------------------------------------------------
    # sql-43 날짜 함수 + 조건부 집계 복합
    # ------------------------------------------------------------------
    Problem(
        id="sql-43",
        rank="Gold",
        title="월별 매출과 고액 주문 비율 (날짜 + 조건부 집계)",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "온라인 서점의 월별 리포트가 한 단계 깊어졌다.\n"
            "월별 주문 건수·매출 합계에 더해, 3만원 이상 '고액 주문'의 건수와\n"
            "비율(%)까지 한 번에 뽑아야 한다.\n\n"
            "테이블 스키마:\n"
            "  orders(order_id INTEGER, order_date TEXT, amount INTEGER)\n"
            "    - order_id   : 주문 번호 (고유)\n"
            "    - order_date : 주문일 'YYYY-MM-DD' 형식 TEXT\n"
            "    - amount     : 주문 금액(원)\n\n"
            "월(ym, 'YYYY-MM')별로 다음을 조회하라:\n"
            "  - order_cnt    : 주문 건수\n"
            "  - total_amount : 매출 합계\n"
            "  - big_cnt      : 3만원(30000) 이상 주문 건수\n"
            "  - big_ratio    : 고액 주문 비율(%) = big_cnt * 100.0 / order_cnt,\n"
            "                   소수 첫째 자리 반올림\n"
            "정수 나눗셈 함정 주의: 100 이 아니라 100.0 을 곱해야 소수가 산다.\n"
        ),
        input_desc="채점 시 테스트케이스의 CREATE/INSERT 스크립트로 테이블이 자동 생성된다. SELECT 문 하나만 작성하면 된다.",
        output_desc="ym, order_cnt, total_amount, big_cnt, big_ratio 다섯 컬럼. ym 오름차순 정렬.",
        examples=[{
            "input": (
                "orders\n"
                "order_id | order_date | amount\n"
                "---------+------------+-------\n"
                "1        | 2024-01-05 | 18000\n"
                "2        | 2024-01-22 | 32000\n"
                "3        | 2024-02-03 | 15000\n"
                "4        | 2024-02-14 | 27000\n"
                "5        | 2024-02-28 | 9000\n"
                "6        | 2024-03-01 | 41000\n"
                "7        | 2024-03-19 | 12000\n"
                "8        | 2024-01-30 | 22000"
            ),
            "output": "",
        }],
        hints=[
            "월 추출은 strftime('%Y-%m', order_date), 고액 건수는 SUM(CASE WHEN ...) 조건부 집계. 둘을 한 GROUP BY 안에서 조합한다.",
            "비율 = SUM(CASE WHEN amount >= 30000 THEN 1 ELSE 0 END) * 100.0 / COUNT(*). 100.0 (실수) 을 써야 정수 나눗셈으로 0 이 되는 것을 막는다. ROUND(x, 1) 로 반올림.",
            "SELECT strftime('%Y-%m',order_date) AS ym, COUNT(*) AS order_cnt, SUM(amount) AS total_amount, SUM(CASE WHEN amount>=30000 THEN 1 ELSE 0 END) AS big_cnt, ROUND(SUM(CASE WHEN amount>=30000 THEN 1 ELSE 0 END)*100.0/COUNT(*),1) AS big_ratio FROM orders GROUP BY strftime('%Y-%m',order_date) ORDER BY ym;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE orders(order_id INTEGER, order_date TEXT, amount INTEGER);\n"
                    "INSERT INTO orders VALUES\n"
                    "(1,'2024-01-05',18000),(2,'2024-01-22',32000),(3,'2024-02-03',15000),\n"
                    "(4,'2024-02-14',27000),(5,'2024-02-28',9000),(6,'2024-03-01',41000),\n"
                    "(7,'2024-03-19',12000),(8,'2024-01-30',22000);"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE orders(order_id INTEGER, order_date TEXT, amount INTEGER);\n"
                    "INSERT INTO orders VALUES\n"
                    "(1,'2023-11-02',55000),(2,'2023-11-25',13000),(3,'2023-12-08',26000),\n"
                    "(4,'2023-12-24',78000),(5,'2024-01-03',30000),(6,'2023-12-30',8000),\n"
                    "(7,'2024-01-15',19000);"
                ),
                "output": "",
            },
        ],
        reference_sql=(
            "SELECT strftime('%Y-%m', order_date) AS ym, COUNT(*) AS order_cnt, "
            "SUM(amount) AS total_amount, "
            "SUM(CASE WHEN amount >= 30000 THEN 1 ELSE 0 END) AS big_cnt, "
            "ROUND(SUM(CASE WHEN amount >= 30000 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) AS big_ratio "
            "FROM orders GROUP BY strftime('%Y-%m', order_date) ORDER BY ym;"
        ),
        tier="G2",
        freq=2,
    ),

    # ------------------------------------------------------------------
    # sql-44 기간 필터 + HAVING
    # ------------------------------------------------------------------
    Problem(
        id="sql-44",
        rank="Gold",
        title="상반기 단골 대출자 (기간 필터 + HAVING)",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "도서관이 2024년 상반기(1월 1일 ~ 6월 30일, 양끝 포함) 동안\n"
            "2회 이상 대출한 '단골 회원'을 뽑아 이벤트 대상자로 선정한다.\n"
            "기간 밖 대출은 제외하고, 집계 후 조건(2회 이상)은 HAVING 으로 거른다.\n"
            "WHERE(집계 전 행 필터)와 HAVING(집계 후 그룹 필터)의 역할 구분이 핵심.\n\n"
            "테이블 스키마:\n"
            "  loans(loan_id INTEGER, member_name TEXT, loan_date TEXT)\n"
            "    - loan_id     : 대출 번호 (고유)\n"
            "    - member_name : 회원 이름\n"
            "    - loan_date   : 대출일 'YYYY-MM-DD' 형식 TEXT\n\n"
            "상반기 대출 2회 이상 회원의 이름, 대출 횟수(loan_cnt),\n"
            "상반기 첫 대출일(first_loan)을 조회하라.\n"
        ),
        input_desc="채점 시 테스트케이스의 CREATE/INSERT 스크립트로 테이블이 자동 생성된다. SELECT 문 하나만 작성하면 된다.",
        output_desc="member_name, loan_cnt, first_loan 세 컬럼. loan_cnt 내림차순, 같으면 member_name 오름차순 정렬.",
        examples=[{
            "input": (
                "loans\n"
                "loan_id | member_name | loan_date\n"
                "--------+-------------+-----------\n"
                "1       | 김책벌레    | 2024-01-10\n"
                "2       | 박다독      | 2024-02-14\n"
                "3       | 김책벌레    | 2024-03-02\n"
                "4       | 이야무      | 2023-12-28\n"
                "5       | 박다독      | 2024-05-21\n"
                "6       | 김책벌레    | 2024-06-30\n"
                "7       | 이야무      | 2024-04-11\n"
                "8       | 박다독      | 2024-07-01\n"
                "9       | 최독서      | 2024-06-15"
            ),
            "output": "",
        }],
        hints=[
            "순서: WHERE 로 기간 내 행만 남김 → GROUP BY 회원 → HAVING 으로 2회 이상 그룹만. 첫 대출일은 MIN(loan_date).",
            "'YYYY-MM-DD' TEXT 는 문자열 비교가 곧 날짜 비교다. loan_date BETWEEN '2024-01-01' AND '2024-06-30'. 집계 결과 조건은 WHERE 가 아니라 HAVING COUNT(*) >= 2 에 쓴다.",
            "SELECT member_name, COUNT(*) AS loan_cnt, MIN(loan_date) AS first_loan FROM loans WHERE loan_date BETWEEN '2024-01-01' AND '2024-06-30' GROUP BY member_name HAVING COUNT(*) >= 2 ORDER BY loan_cnt DESC, member_name;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE loans(loan_id INTEGER, member_name TEXT, loan_date TEXT);\n"
                    "INSERT INTO loans VALUES\n"
                    "(1,'김책벌레','2024-01-10'),(2,'박다독','2024-02-14'),(3,'김책벌레','2024-03-02'),\n"
                    "(4,'이야무','2023-12-28'),(5,'박다독','2024-05-21'),(6,'김책벌레','2024-06-30'),\n"
                    "(7,'이야무','2024-04-11'),(8,'박다독','2024-07-01'),(9,'최독서','2024-06-15');"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE loans(loan_id INTEGER, member_name TEXT, loan_date TEXT);\n"
                    "INSERT INTO loans VALUES\n"
                    "(1,'정글자','2024-01-01'),(2,'한페이지','2024-08-09'),(3,'정글자','2024-02-20'),\n"
                    "(4,'한페이지','2024-03-15'),(5,'오문장','2024-06-30'),(6,'정글자','2023-11-05'),\n"
                    "(7,'오문장','2024-04-04'),(8,'한페이지','2024-05-05');"
                ),
                "output": "",
            },
        ],
        reference_sql=(
            "SELECT member_name, COUNT(*) AS loan_cnt, MIN(loan_date) AS first_loan "
            "FROM loans "
            "WHERE loan_date BETWEEN '2024-01-01' AND '2024-06-30' "
            "GROUP BY member_name HAVING COUNT(*) >= 2 "
            "ORDER BY loan_cnt DESC, member_name;"
        ),
        tier="G3",
        freq=2,
    ),

    # ------------------------------------------------------------------
    # sql-45 ROW_NUMBER vs RANK vs DENSE_RANK
    # ------------------------------------------------------------------
    Problem(
        id="sql-45",
        rank="Gold",
        title="세 가지 순위 함수 한눈에 비교 (ROW_NUMBER/RANK/DENSE_RANK)",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "코딩대회 순위표를 두고 세 가지 순위 방식이 어떻게 다른지\n"
            "한 표로 비교해 달라는 요청이 왔다. 동점자 구간에서 차이가 드러난다:\n"
            "  - ROW_NUMBER : 동점이어도 무조건 서로 다른 연속 번호 (1,2,3,4,...)\n"
            "  - RANK       : 동점은 같은 순위, 다음은 인원수만큼 건너뜀 (1,1,3,...)\n"
            "  - DENSE_RANK : 동점은 같은 순위, 다음은 이어서 (1,1,2,...)\n\n"
            "테이블 스키마:\n"
            "  contest(name TEXT, score INTEGER)\n"
            "    - name  : 참가자 이름 (중복 없음)\n"
            "    - score : 대회 점수 (동점 존재)\n\n"
            "이름·점수와 함께 세 방식의 순위(rn, rnk, dense_rnk)를 조회하라.\n"
            "세 함수 모두 점수 내림차순 기준이며, ROW_NUMBER 의 동점 처리는\n"
            "이름 오름차순을 2차 기준으로 한다.\n"
        ),
        input_desc="채점 시 테스트케이스의 CREATE/INSERT 스크립트로 테이블이 자동 생성된다. SELECT 문 하나만 작성하면 된다.",
        output_desc="name, score, rn, rnk, dense_rnk 다섯 컬럼. score 내림차순, 동점이면 name 오름차순 정렬.",
        examples=[{
            "input": (
                "contest\n"
                "name   | score\n"
                "-------+------\n"
                "김수아 | 92\n"
                "박정민 | 88\n"
                "이태경 | 92\n"
                "최윤서 | 75\n"
                "정가온 | 88\n"
                "한도윤 | 60\n"
                "오라윤 | 88"
            ),
            "output": "",
        }],
        hints=[
            "세 윈도우 함수를 SELECT 절에 나란히 쓰면 된다. OVER 안의 ORDER BY 가 순위 산정 기준, 바깥 ORDER BY 는 출력 순서로 서로 별개다.",
            "ROW_NUMBER() OVER (ORDER BY score DESC, name), RANK() OVER (ORDER BY score DESC), DENSE_RANK() OVER (ORDER BY score DESC). ROW_NUMBER 만 2차 키(name)를 줘야 결과가 유일해진다.",
            "SELECT name, score, ROW_NUMBER() OVER (ORDER BY score DESC, name) AS rn, RANK() OVER (ORDER BY score DESC) AS rnk, DENSE_RANK() OVER (ORDER BY score DESC) AS dense_rnk FROM contest ORDER BY score DESC, name;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE contest(name TEXT, score INTEGER);\n"
                    "INSERT INTO contest VALUES\n"
                    "('김수아',92),('박정민',88),('이태경',92),('최윤서',75),\n"
                    "('정가온',88),('한도윤',60),('오라윤',88);"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE contest(name TEXT, score INTEGER);\n"
                    "INSERT INTO contest VALUES\n"
                    "('갈해준',100),('나봄이',85),('다슬아',85),('라온제',70),\n"
                    "('마음결',95),('바다윤',70);"
                ),
                "output": "",
            },
        ],
        reference_sql=(
            "SELECT name, score, "
            "ROW_NUMBER() OVER (ORDER BY score DESC, name) AS rn, "
            "RANK() OVER (ORDER BY score DESC) AS rnk, "
            "DENSE_RANK() OVER (ORDER BY score DESC) AS dense_rnk "
            "FROM contest ORDER BY score DESC, name;"
        ),
        tier="G2",
        freq=2,
    ),

    # ------------------------------------------------------------------
    # sql-46 그룹별 상위 N (CTE + ROW_NUMBER + PARTITION BY)
    # ------------------------------------------------------------------
    Problem(
        id="sql-46",
        rank="Gold",
        title="부서별 연봉 상위 2명 (그룹별 Top-N)",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "성과급 지급 대상으로 '각 부서에서 연봉 상위 2명'을 뽑는다.\n"
            "전체 상위 N 이 아니라 그룹별 상위 N — 실무·시험 단골 고난도 패턴이다.\n"
            "윈도우 함수 결과는 WHERE 절에서 바로 쓸 수 없으므로\n"
            "CTE(또는 인라인 뷰)로 감싼 뒤 바깥에서 필터링해야 한다.\n\n"
            "테이블 스키마:\n"
            "  employees(name TEXT, dept TEXT, salary INTEGER)\n"
            "    - name   : 이름 (중복 없음)\n"
            "    - dept   : 부서명\n"
            "    - salary : 연봉(만원)\n\n"
            "각 부서 연봉 상위 2명의 부서·이름·연봉·부서 내 순번(rn)을 조회하라.\n"
            "순번은 ROW_NUMBER 로 부서별 연봉 내림차순, 동률이면 이름 오름차순이\n"
            "앞 순번이다. 인원이 1명뿐인 부서는 그 1명만 나온다.\n"
        ),
        input_desc="채점 시 테스트케이스의 CREATE/INSERT 스크립트로 테이블이 자동 생성된다. SELECT 문 하나만 작성하면 된다(WITH ... SELECT 는 한 문장).",
        output_desc="dept, name, salary, rn 네 컬럼. dept 오름차순, 같은 부서는 rn 오름차순 정렬.",
        examples=[{
            "input": (
                "employees\n"
                "name   | dept | salary\n"
                "-------+------+-------\n"
                "김이든 | 개발 | 6200\n"
                "박로운 | 개발 | 5400\n"
                "이해나 | 개발 | 5400\n"
                "최다온 | 영업 | 4700\n"
                "정소울 | 영업 | 5100\n"
                "한윤슬 | 총무 | 3900\n"
                "오재이 | 총무 | 4300\n"
                "신라온 | 영업 | 4400"
            ),
            "output": "",
        }],
        hints=[
            "부서별로 1,2,3... 순번을 매긴 뒤 순번이 2 이하인 행만 남기면 된다. 순번 매기기와 필터링을 두 단계로 나눠라.",
            "WITH ranked AS (SELECT ..., ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC, name) AS rn FROM employees) — 윈도우 함수는 WHERE 에서 못 쓰므로 CTE 바깥에서 WHERE rn <= 2.",
            "WITH ranked AS (SELECT dept, name, salary, ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC, name) AS rn FROM employees) SELECT dept, name, salary, rn FROM ranked WHERE rn <= 2 ORDER BY dept, rn;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE employees(name TEXT, dept TEXT, salary INTEGER);\n"
                    "INSERT INTO employees VALUES\n"
                    "('김이든','개발',6200),('박로운','개발',5400),('이해나','개발',5400),\n"
                    "('최다온','영업',4700),('정소울','영업',5100),('한윤슬','총무',3900),\n"
                    "('오재이','총무',4300),('신라온','영업',4400);"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE employees(name TEXT, dept TEXT, salary INTEGER);\n"
                    "INSERT INTO employees VALUES\n"
                    "('구슬비','기획',4800),('두리안','기획',5600),('루시아','품질',4100),\n"
                    "('미르내','품질',4100),('보라미','기획',5200),('소라단','품질',4600),\n"
                    "('아리수','감사',5000);"
                ),
                "output": "",
            },
        ],
        reference_sql=(
            "WITH ranked AS ("
            "SELECT dept, name, salary, "
            "ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC, name) AS rn "
            "FROM employees"
            ") SELECT dept, name, salary, rn FROM ranked WHERE rn <= 2 "
            "ORDER BY dept, rn;"
        ),
        tier="G1",
        freq=2,
    ),

    # ------------------------------------------------------------------
    # sql-47 PARTITION BY — 그룹 내 순위 + 그룹 내 비중
    # ------------------------------------------------------------------
    Problem(
        id="sql-47",
        rank="Gold",
        title="부서 내 연봉 순위와 인건비 비중 (PARTITION BY 이중 활용)",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "인사평가 자료로 부서 안에서의 연봉 순위와 함께,\n"
            "각자의 연봉이 '부서 전체 인건비에서 차지하는 비중(%)'까지 필요하다.\n"
            "순위 함수와 집계 윈도우 함수(SUM OVER)를 같은 PARTITION 으로 함께 쓴다.\n\n"
            "테이블 스키마:\n"
            "  employees(name TEXT, dept TEXT, salary INTEGER)\n"
            "    - name   : 이름 (중복 없음)\n"
            "    - dept   : 부서명\n"
            "    - salary : 연봉(만원)\n\n"
            "부서·이름·연봉과 함께 다음 두 컬럼을 조회하라:\n"
            "  - dept_rank : 부서 내 연봉 내림차순 RANK() 순위 (동률은 같은 순위)\n"
            "  - pay_ratio : 연봉 * 100.0 / 부서 연봉 총합, 소수 첫째 자리 반올림\n"
        ),
        input_desc="채점 시 테스트케이스의 CREATE/INSERT 스크립트로 테이블이 자동 생성된다. SELECT 문 하나만 작성하면 된다.",
        output_desc="dept, name, salary, dept_rank, pay_ratio 다섯 컬럼. dept 오름차순, 같은 부서는 dept_rank 오름차순, 동순위면 name 오름차순 정렬.",
        examples=[{
            "input": (
                "employees\n"
                "name   | dept | salary\n"
                "-------+------+-------\n"
                "김이든 | 개발 | 6200\n"
                "박로운 | 개발 | 5400\n"
                "이해나 | 개발 | 5400\n"
                "최다온 | 영업 | 4700\n"
                "정소울 | 영업 | 5100\n"
                "한윤슬 | 총무 | 3900\n"
                "오재이 | 총무 | 4300\n"
                "신라온 | 영업 | 4400"
            ),
            "output": "",
        }],
        hints=[
            "순위는 RANK() OVER (PARTITION BY dept ...), 부서 총합은 SUM(salary) OVER (PARTITION BY dept). 윈도우 함수 두 개를 SELECT 절에 나란히 쓴다.",
            "SUM(salary) OVER (PARTITION BY dept) 는 ORDER BY 없이 쓰면 누적이 아니라 '파티션 전체 합'이다. 비중 = salary * 100.0 / 그 값, ROUND(x, 1).",
            "SELECT dept, name, salary, RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS dept_rank, ROUND(salary * 100.0 / SUM(salary) OVER (PARTITION BY dept), 1) AS pay_ratio FROM employees ORDER BY dept, dept_rank, name;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE employees(name TEXT, dept TEXT, salary INTEGER);\n"
                    "INSERT INTO employees VALUES\n"
                    "('김이든','개발',6200),('박로운','개발',5400),('이해나','개발',5400),\n"
                    "('최다온','영업',4700),('정소울','영업',5100),('한윤슬','총무',3900),\n"
                    "('오재이','총무',4300),('신라온','영업',4400);"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE employees(name TEXT, dept TEXT, salary INTEGER);\n"
                    "INSERT INTO employees VALUES\n"
                    "('구슬비','기획',4800),('두리안','기획',5600),('루시아','품질',4100),\n"
                    "('미르내','품질',4100),('보라미','기획',5200),('소라단','품질',4600),\n"
                    "('아리수','기획',4800);"
                ),
                "output": "",
            },
        ],
        reference_sql=(
            "SELECT dept, name, salary, "
            "RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS dept_rank, "
            "ROUND(salary * 100.0 / SUM(salary) OVER (PARTITION BY dept), 1) AS pay_ratio "
            "FROM employees ORDER BY dept, dept_rank, name;"
        ),
        tier="G2",
        freq=2,
    ),

    # ------------------------------------------------------------------
    # sql-48 PARTITION BY + 누적 합 (프레임)
    # ------------------------------------------------------------------
    Problem(
        id="sql-48",
        rank="Gold",
        title="지점별 일 매출 누적 합 (PARTITION + 누적 프레임)",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "프랜차이즈 본부가 지점별로 '그 날짜까지의 누적 매출'을 추적한다.\n"
            "누적 합(running total)이 지점이 바뀌면 0 부터 다시 시작해야 하므로\n"
            "PARTITION BY 와 ORDER BY 를 OVER 절에 함께 넣는다.\n"
            "(OVER 안에 ORDER BY 가 있으면 기본 프레임이 '처음~현재 행'이 되어\n"
            " 누적 합이 된다는 것이 윈도우 프레임의 핵심이다.)\n\n"
            "테이블 스키마:\n"
            "  branch_sales(branch TEXT, sale_date TEXT, amount INTEGER)\n"
            "    - branch    : 지점명\n"
            "    - sale_date : 날짜 'YYYY-MM-DD' 형식 TEXT (지점 내 중복 없음)\n"
            "    - amount    : 그날 매출(원)\n\n"
            "지점·날짜·그날 매출·해당 지점의 그 날짜까지 누적 매출(cum_amount)을\n"
            "조회하라.\n"
        ),
        input_desc="채점 시 테스트케이스의 CREATE/INSERT 스크립트로 테이블이 자동 생성된다. SELECT 문 하나만 작성하면 된다.",
        output_desc="branch, sale_date, amount, cum_amount 네 컬럼. branch 오름차순, 같은 지점은 sale_date 오름차순 정렬.",
        examples=[{
            "input": (
                "branch_sales\n"
                "branch | sale_date  | amount\n"
                "-------+------------+-------\n"
                "강변점 | 2024-05-01 | 120000\n"
                "강변점 | 2024-05-02 | 95000\n"
                "강변점 | 2024-05-03 | 143000\n"
                "강변점 | 2024-05-04 | 88000\n"
                "호수점 | 2024-05-01 | 76000\n"
                "호수점 | 2024-05-02 | 132000\n"
                "호수점 | 2024-05-03 | 54000"
            ),
            "output": "",
        }],
        hints=[
            "SUM 에 OVER 를 붙이면 행을 줄이지 않고 합계를 구한다. 지점별로 따로, 날짜 순서대로 누적해야 하니 PARTITION BY 와 ORDER BY 둘 다 필요하다.",
            "SUM(amount) OVER (PARTITION BY branch ORDER BY sale_date) — PARTITION 이 지점 경계에서 누적을 리셋하고, ORDER BY 가 '처음부터 현재 행까지' 프레임을 만든다.",
            "SELECT branch, sale_date, amount, SUM(amount) OVER (PARTITION BY branch ORDER BY sale_date) AS cum_amount FROM branch_sales ORDER BY branch, sale_date;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE branch_sales(branch TEXT, sale_date TEXT, amount INTEGER);\n"
                    "INSERT INTO branch_sales VALUES\n"
                    "('강변점','2024-05-01',120000),('강변점','2024-05-02',95000),\n"
                    "('강변점','2024-05-03',143000),('강변점','2024-05-04',88000),\n"
                    "('호수점','2024-05-01',76000),('호수점','2024-05-02',132000),\n"
                    "('호수점','2024-05-03',54000);"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE branch_sales(branch TEXT, sale_date TEXT, amount INTEGER);\n"
                    "INSERT INTO branch_sales VALUES\n"
                    "('달빛점','2024-09-10',54000),('달빛점','2024-09-11',87000),\n"
                    "('달빛점','2024-09-12',61000),('별빛점','2024-09-10',149000),\n"
                    "('별빛점','2024-09-11',73000),('별빛점','2024-09-12',98000);"
                ),
                "output": "",
            },
        ],
        reference_sql=(
            "SELECT branch, sale_date, amount, "
            "SUM(amount) OVER (PARTITION BY branch ORDER BY sale_date) AS cum_amount "
            "FROM branch_sales ORDER BY branch, sale_date;"
        ),
        tier="G2",
        freq=2,
    ),

    # ------------------------------------------------------------------
    # sql-49 CTE 2단계 — 집계 결과를 다시 집계
    # ------------------------------------------------------------------
    Problem(
        id="sql-49",
        rank="Gold",
        title="평균을 넘긴 달 찾기 (CTE 2단계 집계)",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "경영진이 '월 매출이 전체 월평균을 넘긴 달'과 그 초과분을 보고 싶어 한다.\n"
            "  1단계: 주문을 월별로 묶어 월 매출 합계를 구한다.  (집계)\n"
            "  2단계: 그 월 매출들의 평균을 구한다.              (집계의 집계)\n"
            "  3단계: 평균보다 큰 달만 남기고 초과분을 계산한다.\n"
            "집계 결과를 다시 집계해야 하므로 CTE 를 연결해 푼다.\n\n"
            "테이블 스키마:\n"
            "  orders(order_id INTEGER, order_date TEXT, amount INTEGER)\n"
            "    - order_id   : 주문 번호 (고유)\n"
            "    - order_date : 주문일 'YYYY-MM-DD' 형식 TEXT\n"
            "    - amount     : 주문 금액(원)\n\n"
            "월 매출(total)이 전체 월평균을 초과하는 달의\n"
            "ym('YYYY-MM')·total·초과분(diff = total - 월평균, 소수 첫째 자리 반올림)을\n"
            "조회하라.\n"
        ),
        input_desc="채점 시 테스트케이스의 CREATE/INSERT 스크립트로 테이블이 자동 생성된다. SELECT 문 하나만 작성하면 된다(WITH ... SELECT 는 한 문장).",
        output_desc="ym, total, diff 세 컬럼. ym 오름차순 정렬.",
        examples=[{
            "input": (
                "orders\n"
                "order_id | order_date | amount\n"
                "---------+------------+-------\n"
                "1        | 2024-01-05 | 18000\n"
                "2        | 2024-01-22 | 32000\n"
                "3        | 2024-01-30 | 22000\n"
                "4        | 2024-02-03 | 15000\n"
                "5        | 2024-02-14 | 27000\n"
                "6        | 2024-02-28 | 9000\n"
                "7        | 2024-03-01 | 41000\n"
                "8        | 2024-03-19 | 12000"
            ),
            "output": "",
        }],
        hints=[
            "CTE 를 두 개 연결하라: monthly(월별 SUM) → stats(monthly 의 AVG). 마지막 SELECT 에서 monthly 와 stats 를 조인해 비교한다.",
            "WITH monthly AS (SELECT strftime('%Y-%m',order_date) AS ym, SUM(amount) AS total FROM orders GROUP BY 1), stats AS (SELECT AVG(total) AS avg_total FROM monthly) — 두 번째 CTE 가 첫 CTE 를 참조하는 것이 핵심.",
            "WITH monthly AS (SELECT strftime('%Y-%m',order_date) AS ym, SUM(amount) AS total FROM orders GROUP BY strftime('%Y-%m',order_date)), stats AS (SELECT AVG(total) AS avg_total FROM monthly) SELECT m.ym, m.total, ROUND(m.total - s.avg_total, 1) AS diff FROM monthly m CROSS JOIN stats s WHERE m.total > s.avg_total ORDER BY m.ym;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE orders(order_id INTEGER, order_date TEXT, amount INTEGER);\n"
                    "INSERT INTO orders VALUES\n"
                    "(1,'2024-01-05',18000),(2,'2024-01-22',32000),(3,'2024-01-30',22000),\n"
                    "(4,'2024-02-03',15000),(5,'2024-02-14',27000),(6,'2024-02-28',9000),\n"
                    "(7,'2024-03-01',41000),(8,'2024-03-19',12000);"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE orders(order_id INTEGER, order_date TEXT, amount INTEGER);\n"
                    "INSERT INTO orders VALUES\n"
                    "(1,'2023-11-02',55000),(2,'2023-11-25',13000),(3,'2023-12-08',26000),\n"
                    "(4,'2023-12-24',78000),(5,'2024-01-03',30000),(6,'2023-12-30',8000),\n"
                    "(7,'2024-01-15',19000);"
                ),
                "output": "",
            },
        ],
        reference_sql=(
            "WITH monthly AS ("
            "SELECT strftime('%Y-%m', order_date) AS ym, SUM(amount) AS total "
            "FROM orders GROUP BY strftime('%Y-%m', order_date)"
            "), stats AS ("
            "SELECT AVG(total) AS avg_total FROM monthly"
            ") SELECT m.ym, m.total, ROUND(m.total - s.avg_total, 1) AS diff "
            "FROM monthly m CROSS JOIN stats s "
            "WHERE m.total > s.avg_total ORDER BY m.ym;"
        ),
        tier="G1",
        freq=2,
    ),

    # ------------------------------------------------------------------
    # sql-50 종합 (JOIN + CTE + 윈도우 + CASE)
    # ------------------------------------------------------------------
    Problem(
        id="sql-50",
        rank="Gold",
        title="부서별 인재 등급 리포트 (JOIN+CTE+윈도우+CASE 종합)",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "경영진 보고용 인재 리포트를 만든다. 요구사항:\n"
            "  1) 직원 테이블과 부서 테이블을 JOIN 해 부서 이름을 붙인다.\n"
            "  2) 부서 안에서 연봉 내림차순 RANK() 순위(rnk)를 매긴다.\n"
            "     (동률이면 같은 순위)\n"
            "  3) 순위에 따라 등급(grade)을 부여한다:\n"
            "     - 1위   : '에이스'\n"
            "     - 2~3위 : '우수'\n"
            "     - 그 외 : '일반'\n"
            "윈도우 함수 결과(rnk)를 CASE 에서 쓰려면 CTE 로 한 번 감싸는 것이\n"
            "정석 패턴이다. JOIN + 윈도우 + CASE + CTE 4가지 조합 문제.\n\n"
            "테이블 스키마:\n"
            "  departments(dept_id INTEGER, dept_name TEXT)\n"
            "    - dept_id   : 부서 번호 (고유)\n"
            "    - dept_name : 부서 이름 (고유)\n"
            "  employees(emp_id INTEGER, name TEXT, dept_id INTEGER, salary INTEGER)\n"
            "    - emp_id  : 사번 (고유)\n"
            "    - name    : 이름 (중복 없음)\n"
            "    - dept_id : 소속 부서 번호\n"
            "    - salary  : 연봉(만원)\n\n"
            "부서 이름·직원 이름·연봉·부서 내 순위(rnk)·등급(grade)을 조회하라.\n"
        ),
        input_desc="채점 시 테스트케이스의 CREATE/INSERT 스크립트로 테이블이 자동 생성된다. SELECT 문 하나만 작성하면 된다(WITH ... SELECT 는 한 문장).",
        output_desc="dept_name, name, salary, rnk, grade 다섯 컬럼. dept_name 오름차순, 같은 부서는 rnk 오름차순, 동순위면 name 오름차순 정렬.",
        examples=[{
            "input": (
                "departments\n"
                "dept_id | dept_name\n"
                "--------+----------\n"
                "1       | 개발팀\n"
                "2       | 영업팀\n"
                "3       | 인사팀\n\n"
                "employees\n"
                "emp_id | name   | dept_id | salary\n"
                "-------+--------+---------+-------\n"
                "1      | 김온새 | 1       | 6500\n"
                "2      | 박누리 | 1       | 5800\n"
                "3      | 이가람 | 1       | 5800\n"
                "4      | 최미리 | 1       | 4900\n"
                "5      | 정찬빛 | 2       | 5200\n"
                "6      | 한별하 | 2       | 4600\n"
                "7      | 오누림 | 2       | 4100\n"
                "8      | 신아람 | 3       | 4400\n"
                "9      | 임솔찬 | 3       | 3900"
            ),
            "output": "",
        }],
        hints=[
            "단계를 나눠라. (1) JOIN + 부서별 RANK 를 구하는 쿼리를 만들고, (2) 그 결과를 CTE 로 감싼 뒤 바깥에서 CASE 로 등급을 붙인다.",
            "WITH ranked AS (SELECT d.dept_name, e.name, e.salary, RANK() OVER (PARTITION BY d.dept_name ORDER BY e.salary DESC) AS rnk FROM employees e JOIN departments d ON e.dept_id = d.dept_id) — 바깥 SELECT 에서 rnk 를 일반 컬럼처럼 CASE 에 쓸 수 있다.",
            "WITH ranked AS (SELECT d.dept_name, e.name, e.salary, RANK() OVER (PARTITION BY d.dept_name ORDER BY e.salary DESC) AS rnk FROM employees e JOIN departments d ON e.dept_id = d.dept_id) SELECT dept_name, name, salary, rnk, CASE WHEN rnk = 1 THEN '에이스' WHEN rnk <= 3 THEN '우수' ELSE '일반' END AS grade FROM ranked ORDER BY dept_name, rnk, name;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE departments(dept_id INTEGER, dept_name TEXT);\n"
                    "INSERT INTO departments VALUES (1,'개발팀'),(2,'영업팀'),(3,'인사팀');\n"
                    "CREATE TABLE employees(emp_id INTEGER, name TEXT, dept_id INTEGER, salary INTEGER);\n"
                    "INSERT INTO employees VALUES\n"
                    "(1,'김온새',1,6500),(2,'박누리',1,5800),(3,'이가람',1,5800),\n"
                    "(4,'최미리',1,4900),(5,'정찬빛',2,5200),(6,'한별하',2,4600),\n"
                    "(7,'오누림',2,4100),(8,'신아람',3,4400),(9,'임솔찬',3,3900);"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE departments(dept_id INTEGER, dept_name TEXT);\n"
                    "INSERT INTO departments VALUES (10,'물류팀'),(20,'보안팀');\n"
                    "CREATE TABLE employees(emp_id INTEGER, name TEXT, dept_id INTEGER, salary INTEGER);\n"
                    "INSERT INTO employees VALUES\n"
                    "(1,'감초록',10,4200),(2,'나린해',10,5100),(3,'다솜결',10,4200),\n"
                    "(4,'라온빛',10,3800),(5,'마주리',20,5900),(6,'바로미',20,5900),\n"
                    "(7,'사이나',20,4700);"
                ),
                "output": "",
            },
        ],
        reference_sql=(
            "WITH ranked AS ("
            "SELECT d.dept_name, e.name, e.salary, "
            "RANK() OVER (PARTITION BY d.dept_name ORDER BY e.salary DESC) AS rnk "
            "FROM employees e JOIN departments d ON e.dept_id = d.dept_id"
            ") SELECT dept_name, name, salary, rnk, "
            "CASE WHEN rnk = 1 THEN '에이스' WHEN rnk <= 3 THEN '우수' ELSE '일반' END AS grade "
            "FROM ranked ORDER BY dept_name, rnk, name;"
        ),
        tier="G1",
        freq=2,
    ),
]
