# -*- coding: utf-8 -*-
"""SQL 집계/JOIN 문제 sql-18 ~ sql-34 (SQLD 2과목 수준)."""
from engine.models import Problem

PROBLEMS_PART = [
    # ------------------------------------------------------------------
    # sql-18 : COUNT(*) vs COUNT(컬럼) — NULL 미포함 차이
    # ------------------------------------------------------------------
    Problem(
        id="sql-18",
        rank="Silver",
        title="전체 회원 수와 연락처 등록 수",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "회원 명단에서 전체 회원 수와, 연락처(phone)가 등록된 회원 수를 한 줄로 구하려고 한다.\n"
            "연락처가 등록되지 않은 회원은 phone 이 NULL 로 저장되어 있다.\n"
            "COUNT(*) 와 COUNT(컬럼) 은 NULL 처리 방식이 다르다는 점에 주의하라.\n\n"
            "MEMBERS 테이블:\n"
            "  id INTEGER — 회원 번호\n"
            "  name TEXT — 회원 이름\n"
            "  phone TEXT — 연락처(미등록이면 NULL)\n"
        ),
        input_desc="MEMBERS(id, name, phone)",
        output_desc=(
            "전체 회원 수 total, 연락처가 등록된 회원 수 has_phone 을 1행으로 출력한다. "
            "결과는 1행이지만 ORDER BY total 을 붙인다."
        ),
        examples=[{
            "input": (
                "MEMBERS\n"
                "id | name   | phone\n"
                " 1 | 김민준 | 010-1111-2222\n"
                " 2 | 이서연 | NULL\n"
                " 3 | 박지훈 | 010-3333-4444\n"
                " 4 | 최수아 | NULL\n"
                " 5 | 정도윤 | 010-5555-6666\n"
                " 6 | 강하은 | 010-7777-8888\n"
                " 7 | 윤시우 | NULL\n"
                " 8 | 임서준 | 010-9999-0000"
            ),
            "output": "",
        }],
        hints=[
            "COUNT(*) 는 NULL 여부와 상관없이 행 수를 세고, COUNT(컬럼) 은 그 컬럼이 NULL 인 행을 빼고 센다.",
            "COUNT(*) 와 COUNT(phone) 을 SELECT 절에 나란히 쓰면 WHERE 없이 한 줄로 끝난다.",
            "SELECT COUNT(*) AS total, COUNT(phone) AS has_phone FROM MEMBERS ORDER BY total;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE MEMBERS (id INTEGER, name TEXT, phone TEXT);\n"
                    "INSERT INTO MEMBERS VALUES\n"
                    "(1,'김민준','010-1111-2222'),(2,'이서연',NULL),(3,'박지훈','010-3333-4444'),\n"
                    "(4,'최수아',NULL),(5,'정도윤','010-5555-6666'),(6,'강하은','010-7777-8888'),\n"
                    "(7,'윤시우',NULL),(8,'임서준','010-9999-0000');"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE MEMBERS (id INTEGER, name TEXT, phone TEXT);\n"
                    "INSERT INTO MEMBERS VALUES\n"
                    "(1,'한지민','010-1234-5678'),(2,'서준호',NULL),(3,'문가영','010-2345-6789'),\n"
                    "(4,'배성우','010-3456-7890'),(5,'신유나',NULL),(6,'권민재','010-4567-8901');"
                ),
                "output": "",
            },
        ],
        reference_sql="SELECT COUNT(*) AS total, COUNT(phone) AS has_phone FROM MEMBERS ORDER BY total;",
        tier="S3",
        freq=3,
    ),

    # ------------------------------------------------------------------
    # sql-19 : AVG 의 NULL 제외 vs 전체 인원 평균
    # ------------------------------------------------------------------
    Problem(
        id="sql-19",
        rank="Silver",
        title="평가 점수 두 가지 평균",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "사원 평가 결과에서 두 가지 평균을 한 줄로 구하려고 한다.\n"
            "  1) 평가를 받은 사원만의 평균 점수 (AVG 는 NULL 을 자동으로 제외한다)\n"
            "  2) 미평가자를 0점으로 간주한 전체 인원 기준 평균 (총점 ÷ 전체 인원)\n"
            "두 값 모두 소수 둘째 자리에서 반올림해 첫째 자리까지 표시한다.\n\n"
            "EVALUATIONS 테이블:\n"
            "  id INTEGER — 사번\n"
            "  name TEXT — 사원 이름\n"
            "  score INTEGER — 평가 점수(미평가면 NULL)\n"
        ),
        input_desc="EVALUATIONS(id, name, score)",
        output_desc=(
            "평가자 평균 avg_scored, 전체 인원 평균 avg_all (둘 다 소수 첫째 자리 반올림) 을 "
            "1행으로 출력한다. 결과는 1행이지만 ORDER BY avg_scored 를 붙인다."
        ),
        examples=[{
            "input": (
                "EVALUATIONS\n"
                "id | name   | score\n"
                " 1 | 김민준 | 80\n"
                " 2 | 이서연 | 90\n"
                " 3 | 박지훈 | NULL\n"
                " 4 | 최수아 | 70\n"
                " 5 | 정도윤 | NULL\n"
                " 6 | 강하은 | 85\n"
                " 7 | 윤시우 | 95"
            ),
            "output": "",
        }],
        hints=[
            "AVG(score) 는 NULL 인 행을 아예 분모에서 빼고 계산한다. 전체 인원 평균과 값이 달라진다.",
            "전체 인원 평균은 SUM(score) 를 COUNT(*) 로 직접 나눈다. 정수 나눗셈이 되지 않게 1.0 을 곱한다.",
            "SELECT ROUND(AVG(score), 1) AS avg_scored, "
            "ROUND(SUM(score) * 1.0 / COUNT(*), 1) AS avg_all FROM EVALUATIONS ORDER BY avg_scored;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE EVALUATIONS (id INTEGER, name TEXT, score INTEGER);\n"
                    "INSERT INTO EVALUATIONS VALUES\n"
                    "(1,'김민준',80),(2,'이서연',90),(3,'박지훈',NULL),(4,'최수아',70),\n"
                    "(5,'정도윤',NULL),(6,'강하은',85),(7,'윤시우',95);"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE EVALUATIONS (id INTEGER, name TEXT, score INTEGER);\n"
                    "INSERT INTO EVALUATIONS VALUES\n"
                    "(1,'한지민',75),(2,'서준호',NULL),(3,'문가영',60),(4,'배성우',90),\n"
                    "(5,'신유나',NULL),(6,'권민재',45);"
                ),
                "output": "",
            },
        ],
        reference_sql=(
            "SELECT ROUND(AVG(score), 1) AS avg_scored, "
            "ROUND(SUM(score) * 1.0 / COUNT(*), 1) AS avg_all FROM EVALUATIONS ORDER BY avg_scored;"
        ),
        tier="S3",
        freq=3,
    ),

    # ------------------------------------------------------------------
    # sql-20 : MIN / MAX + WHERE + NULL 가격
    # ------------------------------------------------------------------
    Problem(
        id="sql-20",
        rank="Silver",
        title="판매 가능 상품의 최저가·최고가",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "재고가 1개 이상 남은(판매 가능한) 상품 중에서 최저가와 최고가를 구하려고 한다.\n"
            "가격이 아직 정해지지 않은 상품은 price 가 NULL 이며, MIN/MAX 집계에서 자동으로 제외된다.\n"
            "재고가 0인 상품은 가격이 아무리 높아도 대상이 아니라는 점에 주의하라.\n\n"
            "PRODUCTS 테이블:\n"
            "  id INTEGER — 상품 번호\n"
            "  name TEXT — 상품 이름\n"
            "  price INTEGER — 판매 가격(원, 미정이면 NULL)\n"
            "  stock INTEGER — 재고 수량\n"
        ),
        input_desc="PRODUCTS(id, name, price, stock)",
        output_desc=(
            "재고가 1 이상인 상품의 최저가 min_price, 최고가 max_price 를 1행으로 출력한다. "
            "결과는 1행이지만 ORDER BY min_price 를 붙인다."
        ),
        examples=[{
            "input": (
                "PRODUCTS\n"
                "id | name        | price  | stock\n"
                " 1 | 무선 키보드 |  45000 | 10\n"
                " 2 | 모니터      | 210000 |  0\n"
                " 3 | 웹캠        | NULL   |  5\n"
                " 4 | 헤드셋      |  89000 |  3\n"
                " 5 | 마이크      | 125000 |  0\n"
                " 6 | 스피커      |  67000 |  7\n"
                " 7 | 마우스      |  23000 | 12"
            ),
            "output": "",
        }],
        hints=[
            "행을 먼저 WHERE 로 걸러낸 뒤 남은 행에만 집계 함수가 적용된다.",
            "WHERE stock > 0 을 걸고 MIN(price), MAX(price) 를 쓴다. NULL 가격은 집계에서 저절로 빠진다.",
            "SELECT MIN(price) AS min_price, MAX(price) AS max_price "
            "FROM PRODUCTS WHERE stock > 0 ORDER BY min_price;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE PRODUCTS (id INTEGER, name TEXT, price INTEGER, stock INTEGER);\n"
                    "INSERT INTO PRODUCTS VALUES\n"
                    "(1,'무선 키보드',45000,10),(2,'모니터',210000,0),(3,'웹캠',NULL,5),\n"
                    "(4,'헤드셋',89000,3),(5,'마이크',125000,0),(6,'스피커',67000,7),\n"
                    "(7,'마우스',23000,12);"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE PRODUCTS (id INTEGER, name TEXT, price INTEGER, stock INTEGER);\n"
                    "INSERT INTO PRODUCTS VALUES\n"
                    "(1,'운동화',59000,4),(2,'슬리퍼',12000,0),(3,'구두',NULL,2),\n"
                    "(4,'샌들',33000,6),(5,'부츠',145000,1),(6,'로퍼',77000,0),\n"
                    "(7,'스니커즈',49000,9);"
                ),
                "output": "",
            },
        ],
        reference_sql=(
            "SELECT MIN(price) AS min_price, MAX(price) AS max_price "
            "FROM PRODUCTS WHERE stock > 0 ORDER BY min_price;"
        ),
        tier="S3",
        freq=2,
    ),

    # ------------------------------------------------------------------
    # sql-21 : GROUP BY + NULL 그룹 제외
    # ------------------------------------------------------------------
    Problem(
        id="sql-21",
        rank="Silver",
        title="부서 배정 직원의 부서별 인원",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "직원 명단에는 아직 부서가 배정되지 않아 dept 가 NULL 인 직원이 섞여 있다.\n"
            "GROUP BY 는 NULL 도 하나의 그룹으로 묶기 때문에, 그대로 집계하면 "
            "'부서 없음' 그룹이 결과에 나타난다. 부서가 배정된 직원만 대상으로 "
            "부서별 인원 수를 구하라.\n\n"
            "EMPLOYEES 테이블:\n"
            "  id INTEGER — 사번\n"
            "  name TEXT — 직원 이름\n"
            "  dept TEXT — 소속 부서(미배정이면 NULL)\n"
        ),
        input_desc="EMPLOYEES(id, name, dept)",
        output_desc=(
            "부서 이름 dept, 인원 수 cnt 를 인원 수 내림차순, "
            "인원이 같으면 부서 이름 오름차순으로 출력한다. NULL 부서 그룹은 결과에 포함하지 않는다."
        ),
        examples=[{
            "input": (
                "EMPLOYEES\n"
                "id | name   | dept\n"
                " 1 | 김민준 | 개발\n"
                " 2 | 이서연 | 기획\n"
                " 3 | 박지훈 | 개발\n"
                " 4 | 최수아 | NULL\n"
                " 5 | 정도윤 | 개발\n"
                " 6 | 강하은 | 영업\n"
                " 7 | 윤시우 | 기획\n"
                " 8 | 임서준 | NULL\n"
                " 9 | 한지민 | 영업"
            ),
            "output": "",
        }],
        hints=[
            "GROUP BY 전에 NULL 부서 행을 걸러내야 한다. 집계 후가 아니라 집계 전 조건이므로 WHERE 다.",
            "WHERE dept IS NOT NULL 을 먼저 쓰고 GROUP BY dept, 정렬 키는 두 개(cnt DESC, dept ASC)다.",
            "SELECT dept, COUNT(*) AS cnt FROM EMPLOYEES WHERE dept IS NOT NULL "
            "GROUP BY dept ORDER BY cnt DESC, dept ASC;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE EMPLOYEES (id INTEGER, name TEXT, dept TEXT);\n"
                    "INSERT INTO EMPLOYEES VALUES\n"
                    "(1,'김민준','개발'),(2,'이서연','기획'),(3,'박지훈','개발'),\n"
                    "(4,'최수아',NULL),(5,'정도윤','개발'),(6,'강하은','영업'),\n"
                    "(7,'윤시우','기획'),(8,'임서준',NULL),(9,'한지민','영업');"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE EMPLOYEES (id INTEGER, name TEXT, dept TEXT);\n"
                    "INSERT INTO EMPLOYEES VALUES\n"
                    "(1,'서준호','재무'),(2,'문가영',NULL),(3,'배성우','인사'),\n"
                    "(4,'신유나','재무'),(5,'권민재','총무'),(6,'조은채','인사'),\n"
                    "(7,'허준영','재무');"
                ),
                "output": "",
            },
        ],
        reference_sql=(
            "SELECT dept, COUNT(*) AS cnt FROM EMPLOYEES WHERE dept IS NOT NULL "
            "GROUP BY dept ORDER BY cnt DESC, dept ASC;"
        ),
        tier="S3",
        freq=3,
    ),

    # ------------------------------------------------------------------
    # sql-22 : GROUP BY + 집계 3개 (COUNT(*) / COUNT(컬럼) / AVG)
    # ------------------------------------------------------------------
    Problem(
        id="sql-22",
        rank="Silver",
        title="부서별 인원·보너스 수령·평균 급여",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "부서별로 다음 세 가지를 한 번에 집계하려고 한다.\n"
            "  1) 전체 인원 수\n"
            "  2) 보너스를 받은 인원 수 (bonus 가 NULL 이면 미수령)\n"
            "  3) 평균 급여 (소수 첫째 자리 반올림)\n"
            "보너스 수령 인원은 COUNT(*) 가 아니라 NULL 을 제외하고 세는 방법을 써야 한다.\n\n"
            "EMPLOYEES 테이블:\n"
            "  id INTEGER — 사번\n"
            "  name TEXT — 직원 이름\n"
            "  dept TEXT — 소속 부서\n"
            "  salary INTEGER — 월 급여(만원)\n"
            "  bonus INTEGER — 보너스(만원, 미수령이면 NULL)\n"
        ),
        input_desc="EMPLOYEES(id, name, dept, salary, bonus)",
        output_desc=(
            "부서 dept, 인원 수 cnt, 보너스 수령 인원 bonus_cnt, "
            "평균 급여 avg_salary(소수 첫째 자리 반올림) 를 부서 이름 오름차순으로 출력한다."
        ),
        examples=[{
            "input": (
                "EMPLOYEES\n"
                "id | name   | dept | salary | bonus\n"
                " 1 | 김민준 | 개발 | 4200   | 500\n"
                " 2 | 이서연 | 기획 | 3500   | NULL\n"
                " 3 | 박지훈 | 개발 | 3800   | NULL\n"
                " 4 | 최수아 | 영업 | 3600   | 200\n"
                " 5 | 정도윤 | 개발 | 5100   | 700\n"
                " 6 | 강하은 | 영업 | 3300   | NULL\n"
                " 7 | 윤시우 | 기획 | 4000   | 300\n"
                " 8 | 임서준 | 영업 | 4500   | 400"
            ),
            "output": "",
        }],
        hints=[
            "집계 함수는 SELECT 절에 몇 개든 나란히 쓸 수 있다. 보너스 수령 인원이 핵심이다.",
            "COUNT(bonus) 는 bonus 가 NULL 인 행을 빼고 센다. 평균은 ROUND(AVG(salary), 1).",
            "SELECT dept, COUNT(*) AS cnt, COUNT(bonus) AS bonus_cnt, "
            "ROUND(AVG(salary), 1) AS avg_salary FROM EMPLOYEES GROUP BY dept ORDER BY dept;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE EMPLOYEES (id INTEGER, name TEXT, dept TEXT, salary INTEGER, bonus INTEGER);\n"
                    "INSERT INTO EMPLOYEES VALUES\n"
                    "(1,'김민준','개발',4200,500),(2,'이서연','기획',3500,NULL),\n"
                    "(3,'박지훈','개발',3800,NULL),(4,'최수아','영업',3600,200),\n"
                    "(5,'정도윤','개발',5100,700),(6,'강하은','영업',3300,NULL),\n"
                    "(7,'윤시우','기획',4000,300),(8,'임서준','영업',4500,400);"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE EMPLOYEES (id INTEGER, name TEXT, dept TEXT, salary INTEGER, bonus INTEGER);\n"
                    "INSERT INTO EMPLOYEES VALUES\n"
                    "(1,'한지민','인사',3900,250),(2,'서준호','재무',4600,NULL),\n"
                    "(3,'문가영','인사',3400,NULL),(4,'배성우','재무',5200,600),\n"
                    "(5,'신유나','재무',4100,NULL),(6,'권민재','인사',3700,150);"
                ),
                "output": "",
            },
        ],
        reference_sql=(
            "SELECT dept, COUNT(*) AS cnt, COUNT(bonus) AS bonus_cnt, "
            "ROUND(AVG(salary), 1) AS avg_salary FROM EMPLOYEES GROUP BY dept ORDER BY dept;"
        ),
        tier="S2",
        freq=3,
    ),

    # ------------------------------------------------------------------
    # sql-23 : WHERE vs HAVING 구분
    # ------------------------------------------------------------------
    Problem(
        id="sql-23",
        rank="Silver",
        title="완료 주문 기준 우수 고객",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "주문 내역에는 '완료' 와 '취소' 주문이 섞여 있다. 취소 주문 금액은 매출이 아니므로 "
            "집계 대상에서 빼야 한다.\n"
            "완료된 주문만 합산했을 때 총액이 50000원 이상인 고객을 구하라.\n"
            "행 단위 조건(상태)은 집계 전에, 집계 결과 조건(총액)은 집계 후에 걸어야 한다.\n\n"
            "ORDERS 테이블:\n"
            "  id INTEGER — 주문 번호\n"
            "  customer TEXT — 고객 이름\n"
            "  amount INTEGER — 주문 금액(원)\n"
            "  status TEXT — 주문 상태('완료' 또는 '취소')\n"
        ),
        input_desc="ORDERS(id, customer, amount, status)",
        output_desc=(
            "완료 주문 총액이 50000원 이상인 고객의 이름 customer 와 총액 total 을 "
            "총액 내림차순, 총액이 같으면 고객 이름 오름차순으로 출력한다."
        ),
        examples=[{
            "input": (
                "ORDERS\n"
                "id | customer | amount | status\n"
                " 1 | 김하늘   | 30000  | 완료\n"
                " 2 | 박세영   | 40000  | 취소\n"
                " 3 | 김하늘   | 25000  | 완료\n"
                " 4 | 이준호   | 60000  | 완료\n"
                " 5 | 박세영   | 15000  | 완료\n"
                " 6 | 최다인   | 80000  | 취소\n"
                " 7 | 이준호   |  5000  | 취소\n"
                " 8 | 박세영   | 45000  | 완료\n"
                " 9 | 최다인   | 20000  | 완료\n"
                "10 | 김하늘   | 10000  | 취소"
            ),
            "output": "",
        }],
        hints=[
            "상태 조건을 HAVING 에 넣으면 이미 취소 금액까지 합산된 뒤라 늦다. 합산 전에 걸러야 한다.",
            "WHERE status = '완료' → GROUP BY customer → HAVING SUM(amount) >= 50000 순서다.",
            "SELECT customer, SUM(amount) AS total FROM ORDERS WHERE status = '완료' "
            "GROUP BY customer HAVING SUM(amount) >= 50000 ORDER BY total DESC, customer ASC;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE ORDERS (id INTEGER, customer TEXT, amount INTEGER, status TEXT);\n"
                    "INSERT INTO ORDERS VALUES\n"
                    "(1,'김하늘',30000,'완료'),(2,'박세영',40000,'취소'),(3,'김하늘',25000,'완료'),\n"
                    "(4,'이준호',60000,'완료'),(5,'박세영',15000,'완료'),(6,'최다인',80000,'취소'),\n"
                    "(7,'이준호',5000,'취소'),(8,'박세영',45000,'완료'),(9,'최다인',20000,'완료'),\n"
                    "(10,'김하늘',10000,'취소');"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE ORDERS (id INTEGER, customer TEXT, amount INTEGER, status TEXT);\n"
                    "INSERT INTO ORDERS VALUES\n"
                    "(1,'정우진',50000,'완료'),(2,'한소희',70000,'취소'),(3,'정우진',10000,'취소'),\n"
                    "(4,'한소희',30000,'완료'),(5,'오세훈',45000,'완료'),(6,'오세훈',15000,'완료'),\n"
                    "(7,'한소희',25000,'완료'),(8,'유지아',90000,'취소');"
                ),
                "output": "",
            },
        ],
        reference_sql=(
            "SELECT customer, SUM(amount) AS total FROM ORDERS WHERE status = '완료' "
            "GROUP BY customer HAVING SUM(amount) >= 50000 ORDER BY total DESC, customer ASC;"
        ),
        tier="S2",
        freq=3,
    ),

    # ------------------------------------------------------------------
    # sql-24 : GROUP BY + HAVING 복수 조건 + ORDER BY 종합
    # ------------------------------------------------------------------
    Problem(
        id="sql-24",
        rank="Silver",
        title="단골 우수 고객 선정",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "주문 횟수와 총액을 모두 만족하는 고객만 '단골 우수 고객'으로 선정한다.\n"
            "조건: 주문이 2건 이상이면서 총 주문 금액이 50000원 이상.\n"
            "한 번에 큰 금액을 쓴 고객(1건 고액)이나, 여러 번 주문했지만 총액이 부족한 고객은 "
            "모두 탈락한다는 점에 주의하라.\n\n"
            "ORDERS 테이블:\n"
            "  id INTEGER — 주문 번호\n"
            "  customer TEXT — 고객 이름\n"
            "  amount INTEGER — 주문 금액(원)\n"
        ),
        input_desc="ORDERS(id, customer, amount)",
        output_desc=(
            "선정된 고객의 이름 customer, 주문 건수 cnt, 총액 total 을 "
            "총액 내림차순, 총액이 같으면 고객 이름 오름차순으로 출력한다."
        ),
        examples=[{
            "input": (
                "ORDERS\n"
                "id | customer | amount\n"
                " 1 | 김하늘   |  30000\n"
                " 2 | 박세영   |  20000\n"
                " 3 | 김하늘   |  25000\n"
                " 4 | 이준호   |  60000\n"
                " 5 | 박세영   |  15000\n"
                " 6 | 최다인   |  10000\n"
                " 7 | 이준호   |   5000\n"
                " 8 | 최다인   |  55000\n"
                " 9 | 정우진   | 100000"
            ),
            "output": "",
        }],
        hints=[
            "집계 결과 두 가지(건수, 총액)에 동시에 조건을 걸어야 하므로 둘 다 HAVING 에 들어간다.",
            "HAVING COUNT(*) >= 2 AND SUM(amount) >= 50000 처럼 AND 로 잇는다.",
            "SELECT customer, COUNT(*) AS cnt, SUM(amount) AS total FROM ORDERS "
            "GROUP BY customer HAVING COUNT(*) >= 2 AND SUM(amount) >= 50000 "
            "ORDER BY total DESC, customer ASC;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE ORDERS (id INTEGER, customer TEXT, amount INTEGER);\n"
                    "INSERT INTO ORDERS VALUES\n"
                    "(1,'김하늘',30000),(2,'박세영',20000),(3,'김하늘',25000),\n"
                    "(4,'이준호',60000),(5,'박세영',15000),(6,'최다인',10000),\n"
                    "(7,'이준호',5000),(8,'최다인',55000),(9,'정우진',100000);"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE ORDERS (id INTEGER, customer TEXT, amount INTEGER);\n"
                    "INSERT INTO ORDERS VALUES\n"
                    "(1,'한소희',40000),(2,'오세훈',90000),(3,'한소희',20000),\n"
                    "(4,'유지아',30000),(5,'유지아',15000),(6,'송민호',26000),\n"
                    "(7,'송민호',26000),(8,'임나연',120000);"
                ),
                "output": "",
            },
        ],
        reference_sql=(
            "SELECT customer, COUNT(*) AS cnt, SUM(amount) AS total FROM ORDERS "
            "GROUP BY customer HAVING COUNT(*) >= 2 AND SUM(amount) >= 50000 "
            "ORDER BY total DESC, customer ASC;"
        ),
        tier="S2",
        freq=3,
    ),

    # ------------------------------------------------------------------
    # sql-25 : COUNT(*) vs COUNT(DISTINCT) + NULL 방문자
    # ------------------------------------------------------------------
    Problem(
        id="sql-25",
        rank="Silver",
        title="페이지별 조회수와 순 방문자",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "방문 로그에서 페이지마다 전체 조회수(pv)와 순 방문자 수(uv)를 함께 구하려고 한다.\n"
            "비로그인 방문은 visitor 가 NULL 로 기록된다.\n"
            "  - pv: NULL 포함 모든 방문 행 수\n"
            "  - uv: 서로 다른 로그인 방문자 수 (NULL 은 세지 않는다)\n"
            "같은 사람이 같은 페이지를 여러 번 봐도 uv 는 1명이다.\n\n"
            "VISITS 테이블:\n"
            "  id INTEGER — 로그 번호\n"
            "  page TEXT — 방문한 페이지 이름\n"
            "  visitor TEXT — 방문자 이름(비로그인이면 NULL)\n"
        ),
        input_desc="VISITS(id, page, visitor)",
        output_desc=(
            "페이지 page, 조회수 pv, 순 방문자 수 uv 를 "
            "순 방문자 수 내림차순, 같으면 페이지 이름 오름차순으로 출력한다."
        ),
        examples=[{
            "input": (
                "VISITS\n"
                "id | page   | visitor\n"
                " 1 | 메인   | 김민준\n"
                " 2 | 메인   | 이서연\n"
                " 3 | 공지   | 이서연\n"
                " 4 | 메인   | 김민준\n"
                " 5 | 이벤트 | 강하은\n"
                " 6 | 이벤트 | 김민준\n"
                " 7 | 공지   | NULL\n"
                " 8 | 이벤트 | 강하은\n"
                " 9 | 메인   | NULL\n"
                "10 | 메인   | 박지훈"
            ),
            "output": "",
        }],
        hints=[
            "행 수를 세는 것과 서로 다른 값을 세는 것은 다른 집계다. NULL 처리도 서로 다르다.",
            "COUNT(*) 는 NULL 행도 세지만 COUNT(DISTINCT visitor) 는 NULL 을 제외하고 중복 없이 센다.",
            "SELECT page, COUNT(*) AS pv, COUNT(DISTINCT visitor) AS uv FROM VISITS "
            "GROUP BY page ORDER BY uv DESC, page ASC;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE VISITS (id INTEGER, page TEXT, visitor TEXT);\n"
                    "INSERT INTO VISITS VALUES\n"
                    "(1,'메인','김민준'),(2,'메인','이서연'),(3,'공지','이서연'),\n"
                    "(4,'메인','김민준'),(5,'이벤트','강하은'),(6,'이벤트','김민준'),\n"
                    "(7,'공지',NULL),(8,'이벤트','강하은'),(9,'메인',NULL),(10,'메인','박지훈');"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE VISITS (id INTEGER, page TEXT, visitor TEXT);\n"
                    "INSERT INTO VISITS VALUES\n"
                    "(1,'상품목록','한지민'),(2,'장바구니','한지민'),(3,'상품목록',NULL),\n"
                    "(4,'상품목록','한지민'),(5,'결제','문가영'),(6,'장바구니','서준호'),\n"
                    "(7,'결제',NULL),(8,'상품목록','배성우');"
                ),
                "output": "",
            },
        ],
        reference_sql=(
            "SELECT page, COUNT(*) AS pv, COUNT(DISTINCT visitor) AS uv FROM VISITS "
            "GROUP BY page ORDER BY uv DESC, page ASC;"
        ),
        tier="S2",
        freq=2,
    ),

    # ------------------------------------------------------------------
    # sql-26 : INNER JOIN — 고아 행과 NULL 키가 탈락하는 성질
    # ------------------------------------------------------------------
    Problem(
        id="sql-26",
        rank="Silver",
        title="회원 확인이 가능한 주문만 조회",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "주문 테이블에는 비회원 주문(customer_id 가 NULL)과, 탈퇴한 회원의 주문"
            "(고객 테이블에 없는 번호)이 섞여 있다.\n"
            "고객 테이블과 매칭되는 주문만 남겨, 주문 번호·고객 이름·금액을 조회하라.\n"
            "INNER JOIN 은 짝이 없는 행과 NULL 키를 자동으로 탈락시킨다는 성질을 이용한다.\n\n"
            "CUSTOMERS 테이블:\n"
            "  id INTEGER — 고객 번호\n"
            "  name TEXT — 고객 이름\n\n"
            "ORDERS 테이블:\n"
            "  id INTEGER — 주문 번호\n"
            "  customer_id INTEGER — 주문 고객 번호(비회원이면 NULL, 탈퇴 회원 번호일 수도 있음)\n"
            "  amount INTEGER — 주문 금액(원)\n"
        ),
        input_desc="CUSTOMERS(id, name), ORDERS(id, customer_id, amount)",
        output_desc=(
            "매칭된 주문의 주문 번호 id, 고객 이름 name, 금액 amount 를 주문 번호 오름차순으로 출력한다."
        ),
        examples=[{
            "input": (
                "CUSTOMERS\n"
                "id | name\n"
                " 1 | 김하늘\n"
                " 2 | 박세영\n"
                " 3 | 이준호\n"
                " 4 | 최다인\n"
                " 5 | 정우진\n\n"
                "ORDERS\n"
                "id | customer_id | amount\n"
                " 1 | 3           | 42000\n"
                " 2 | NULL        | 15000\n"
                " 3 | 5           |  8000\n"
                " 4 | 99          | 23000\n"
                " 5 | 3           | 31000\n"
                " 6 | 4           | 56000\n"
                " 7 | NULL        | 12000\n"
                " 8 | 1           |  9000"
            ),
            "output": "",
        }],
        hints=[
            "NULL 은 어떤 값과도 = 로 매칭되지 않으므로 INNER JOIN 에서 저절로 빠진다.",
            "ORDERS o JOIN CUSTOMERS c ON o.customer_id = c.id 만으로 비회원·탈퇴 회원 주문이 걸러진다.",
            "SELECT o.id, c.name, o.amount FROM ORDERS o "
            "JOIN CUSTOMERS c ON o.customer_id = c.id ORDER BY o.id;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE CUSTOMERS (id INTEGER, name TEXT);\n"
                    "INSERT INTO CUSTOMERS VALUES (1,'김하늘'),(2,'박세영'),(3,'이준호'),(4,'최다인'),(5,'정우진');\n"
                    "CREATE TABLE ORDERS (id INTEGER, customer_id INTEGER, amount INTEGER);\n"
                    "INSERT INTO ORDERS VALUES\n"
                    "(1,3,42000),(2,NULL,15000),(3,5,8000),(4,99,23000),\n"
                    "(5,3,31000),(6,4,56000),(7,NULL,12000),(8,1,9000);"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE CUSTOMERS (id INTEGER, name TEXT);\n"
                    "INSERT INTO CUSTOMERS VALUES (1,'한소희'),(2,'오세훈'),(3,'임나연'),(4,'송민호'),(5,'유지아');\n"
                    "CREATE TABLE ORDERS (id INTEGER, customer_id INTEGER, amount INTEGER);\n"
                    "INSERT INTO ORDERS VALUES\n"
                    "(1,2,9900),(2,77,120000),(3,1,4500),(4,5,67000),\n"
                    "(5,2,18000),(6,NULL,30000),(7,4,22000);"
                ),
                "output": "",
            },
        ],
        reference_sql=(
            "SELECT o.id, c.name, o.amount FROM ORDERS o "
            "JOIN CUSTOMERS c ON o.customer_id = c.id ORDER BY o.id;"
        ),
        tier="S3",
        freq=3,
    ),

    # ------------------------------------------------------------------
    # sql-27 : INNER JOIN + WHERE — NULL 비교는 조건에 걸리지 않음
    # ------------------------------------------------------------------
    Problem(
        id="sql-27",
        rank="Silver",
        title="서울 근무 직원 명단",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "직원 테이블과 부서 테이블을 연결해, 근무지가 '서울' 인 부서 소속 직원만 조회한다.\n"
            "주의할 점 두 가지:\n"
            "  1) 소속 부서가 없는 직원(dept_id 가 NULL)은 JOIN 단계에서 탈락한다.\n"
            "  2) 근무지가 미정(NULL)인 부서는 location = '서울' 비교가 참이 되지 않아 제외된다.\n\n"
            "DEPARTMENTS 테이블:\n"
            "  id INTEGER — 부서 번호\n"
            "  name TEXT — 부서 이름\n"
            "  location TEXT — 근무지(미정이면 NULL)\n\n"
            "EMPLOYEES 테이블:\n"
            "  id INTEGER — 사번\n"
            "  name TEXT — 직원 이름\n"
            "  dept_id INTEGER — 소속 부서 번호(무소속이면 NULL)\n"
        ),
        input_desc="DEPARTMENTS(id, name, location), EMPLOYEES(id, name, dept_id)",
        output_desc=(
            "근무지가 '서울' 인 부서 소속 직원의 사번 id, 직원 이름 name, 부서 이름 dept_name 을 "
            "사번 오름차순으로 출력한다."
        ),
        examples=[{
            "input": (
                "DEPARTMENTS\n"
                "id | name     | location\n"
                " 1 | 개발팀   | 서울\n"
                " 2 | 영업팀   | 부산\n"
                " 3 | 디자인팀 | 서울\n"
                " 4 | 물류팀   | NULL\n"
                " 5 | 인사팀   | 서울\n\n"
                "EMPLOYEES\n"
                "id | name   | dept_id\n"
                " 1 | 김민준 | 1\n"
                " 2 | 이서연 | 2\n"
                " 3 | 박지훈 | NULL\n"
                " 4 | 최수아 | 3\n"
                " 5 | 정도윤 | 4\n"
                " 6 | 강하은 | 5\n"
                " 7 | 윤시우 | 2\n"
                " 8 | 임서준 | 3\n"
                " 9 | 한지민 | NULL"
            ),
            "output": "",
        }],
        hints=[
            "부서 번호로 두 테이블을 잇고, 이어진 결과에서 근무지 조건을 건다. NULL 은 알아서 빠진다.",
            "JOIN ... ON e.dept_id = d.id 뒤에 WHERE d.location = '서울' 을 붙인다.",
            "SELECT e.id, e.name, d.name AS dept_name FROM EMPLOYEES e "
            "JOIN DEPARTMENTS d ON e.dept_id = d.id WHERE d.location = '서울' ORDER BY e.id;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE DEPARTMENTS (id INTEGER, name TEXT, location TEXT);\n"
                    "INSERT INTO DEPARTMENTS VALUES\n"
                    "(1,'개발팀','서울'),(2,'영업팀','부산'),(3,'디자인팀','서울'),\n"
                    "(4,'물류팀',NULL),(5,'인사팀','서울');\n"
                    "CREATE TABLE EMPLOYEES (id INTEGER, name TEXT, dept_id INTEGER);\n"
                    "INSERT INTO EMPLOYEES VALUES\n"
                    "(1,'김민준',1),(2,'이서연',2),(3,'박지훈',NULL),(4,'최수아',3),\n"
                    "(5,'정도윤',4),(6,'강하은',5),(7,'윤시우',2),(8,'임서준',3),(9,'한지민',NULL);"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE DEPARTMENTS (id INTEGER, name TEXT, location TEXT);\n"
                    "INSERT INTO DEPARTMENTS VALUES\n"
                    "(1,'회계팀','대전'),(2,'마케팅팀','서울'),(3,'품질팀',NULL),\n"
                    "(4,'연구팀','서울'),(5,'총무팀','광주');\n"
                    "CREATE TABLE EMPLOYEES (id INTEGER, name TEXT, dept_id INTEGER);\n"
                    "INSERT INTO EMPLOYEES VALUES\n"
                    "(1,'한지민',2),(2,'서준호',1),(3,'문가영',4),(4,'배성우',3),\n"
                    "(5,'신유나',2),(6,'권민재',NULL),(7,'조은채',4);"
                ),
                "output": "",
            },
        ],
        reference_sql=(
            "SELECT e.id, e.name, d.name AS dept_name FROM EMPLOYEES e "
            "JOIN DEPARTMENTS d ON e.dept_id = d.id WHERE d.location = '서울' ORDER BY e.id;"
        ),
        tier="S3",
        freq=3,
    ),

    # ------------------------------------------------------------------
    # sql-28 : LEFT JOIN — ON 절 추가 조건 vs WHERE 조건
    # ------------------------------------------------------------------
    Problem(
        id="sql-28",
        rank="Silver",
        title="모든 고객의 완료 주문 현황",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "모든 고객을 한 명도 빠뜨리지 않고, 각자의 '완료' 주문 금액을 나란히 조회하려고 한다.\n"
            "완료 주문이 없는 고객(주문 자체가 없거나 취소 주문만 있는 고객)은 금액이 NULL 로 "
            "한 줄 나와야 한다.\n"
            "핵심: 상태 조건을 WHERE 에 쓰면 완료 주문이 없는 고객이 결과에서 사라진다. "
            "LEFT JOIN 의 ON 절에 조건을 추가해야 모든 고객이 유지된다.\n\n"
            "CUSTOMERS 테이블:\n"
            "  id INTEGER — 고객 번호\n"
            "  name TEXT — 고객 이름\n\n"
            "ORDERS 테이블:\n"
            "  id INTEGER — 주문 번호\n"
            "  customer_id INTEGER — 주문 고객 번호(CUSTOMERS.id 참조)\n"
            "  amount INTEGER — 주문 금액(원)\n"
            "  status TEXT — 주문 상태('완료' 또는 '취소')\n"
        ),
        input_desc="CUSTOMERS(id, name), ORDERS(id, customer_id, amount, status)",
        output_desc=(
            "고객 이름 name, 완료 주문 금액 amount(완료 주문이 없으면 NULL) 를 "
            "고객 번호 오름차순, 같은 고객 안에서는 주문 번호 오름차순으로 출력한다."
        ),
        examples=[{
            "input": (
                "CUSTOMERS\n"
                "id | name\n"
                " 1 | 김하늘\n"
                " 2 | 박세영\n"
                " 3 | 이준호\n"
                " 4 | 최다인\n"
                " 5 | 정우진\n\n"
                "ORDERS\n"
                "id | customer_id | amount | status\n"
                " 1 | 1           | 25000  | 완료\n"
                " 2 | 3           | 18000  | 취소\n"
                " 3 | 1           |  9000  | 완료\n"
                " 4 | 4           | 52000  | 완료\n"
                " 5 | 3           |  7500  | 취소\n"
                " 6 | 4           | 11000  | 취소\n"
                " 7 | 2           | 30000  | 완료"
            ),
            "output": "",
        }],
        hints=[
            "LEFT JOIN 뒤 WHERE o.status = '완료' 를 쓰면 NULL 행이 걸러져 INNER JOIN 과 같아진다.",
            "조건을 ON 절에 함께 쓴다: LEFT JOIN ORDERS o ON c.id = o.customer_id AND o.status = '완료'.",
            "SELECT c.name, o.amount FROM CUSTOMERS c "
            "LEFT JOIN ORDERS o ON c.id = o.customer_id AND o.status = '완료' ORDER BY c.id, o.id;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE CUSTOMERS (id INTEGER, name TEXT);\n"
                    "INSERT INTO CUSTOMERS VALUES (1,'김하늘'),(2,'박세영'),(3,'이준호'),(4,'최다인'),(5,'정우진');\n"
                    "CREATE TABLE ORDERS (id INTEGER, customer_id INTEGER, amount INTEGER, status TEXT);\n"
                    "INSERT INTO ORDERS VALUES\n"
                    "(1,1,25000,'완료'),(2,3,18000,'취소'),(3,1,9000,'완료'),\n"
                    "(4,4,52000,'완료'),(5,3,7500,'취소'),(6,4,11000,'취소'),(7,2,30000,'완료');"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE CUSTOMERS (id INTEGER, name TEXT);\n"
                    "INSERT INTO CUSTOMERS VALUES\n"
                    "(1,'한소희'),(2,'오세훈'),(3,'임나연'),(4,'송민호'),(5,'유지아'),(6,'차백호');\n"
                    "CREATE TABLE ORDERS (id INTEGER, customer_id INTEGER, amount INTEGER, status TEXT);\n"
                    "INSERT INTO ORDERS VALUES\n"
                    "(1,2,33000,'완료'),(2,5,14000,'취소'),(3,2,8800,'취소'),\n"
                    "(4,6,27000,'완료'),(5,1,45000,'완료'),(6,5,19000,'취소');"
                ),
                "output": "",
            },
        ],
        reference_sql=(
            "SELECT c.name, o.amount FROM CUSTOMERS c "
            "LEFT JOIN ORDERS o ON c.id = o.customer_id AND o.status = '완료' ORDER BY c.id, o.id;"
        ),
        tier="S1",
        freq=3,
    ),

    # ------------------------------------------------------------------
    # sql-29 : LEFT JOIN + ON 조건 + IS NULL — 완료 주문 없는 고객
    # ------------------------------------------------------------------
    Problem(
        id="sql-29",
        rank="Silver",
        title="완료 주문이 없는 고객 찾기",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "재구매 쿠폰을 보내기 위해 '완료된 주문이 한 건도 없는' 고객을 찾으려고 한다.\n"
            "주문 자체가 없는 고객뿐 아니라, 취소 주문만 있는 고객도 대상에 포함해야 한다.\n"
            "단순히 주문 테이블과 LEFT JOIN 후 IS NULL 만 확인하면 취소 주문만 있는 고객을 "
            "놓친다 — 완료 조건을 ON 절에 넣어야 한다.\n\n"
            "CUSTOMERS 테이블:\n"
            "  id INTEGER — 고객 번호\n"
            "  name TEXT — 고객 이름\n\n"
            "ORDERS 테이블:\n"
            "  id INTEGER — 주문 번호\n"
            "  customer_id INTEGER — 주문 고객 번호(CUSTOMERS.id 참조)\n"
            "  amount INTEGER — 주문 금액(원)\n"
            "  status TEXT — 주문 상태('완료' 또는 '취소')\n"
        ),
        input_desc="CUSTOMERS(id, name), ORDERS(id, customer_id, amount, status)",
        output_desc=(
            "완료 주문이 없는 고객의 번호 id 와 이름 name 을 고객 번호 오름차순으로 출력한다."
        ),
        examples=[{
            "input": (
                "CUSTOMERS\n"
                "id | name\n"
                " 1 | 김도현\n"
                " 2 | 이유진\n"
                " 3 | 박찬희\n"
                " 4 | 최연서\n"
                " 5 | 정하람\n"
                " 6 | 문세윤\n\n"
                "ORDERS\n"
                "id | customer_id | amount | status\n"
                " 1 | 1           | 12000  | 완료\n"
                " 2 | 3           |  5000  | 취소\n"
                " 3 | 1           |  7000  | 완료\n"
                " 4 | 6           | 90000  | 완료\n"
                " 5 | 3           |  3000  | 취소\n"
                " 6 | 4           | 15000  | 완료\n"
                " 7 | 5           | 20000  | 취소"
            ),
            "output": "",
        }],
        hints=[
            "완료 주문과만 짝을 지어 보고, 짝이 하나도 안 생긴 고객을 남기면 된다.",
            "LEFT JOIN ... ON c.id = o.customer_id AND o.status = '완료' 후 WHERE o.id IS NULL.",
            "SELECT c.id, c.name FROM CUSTOMERS c "
            "LEFT JOIN ORDERS o ON c.id = o.customer_id AND o.status = '완료' "
            "WHERE o.id IS NULL ORDER BY c.id;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE CUSTOMERS (id INTEGER, name TEXT);\n"
                    "INSERT INTO CUSTOMERS VALUES\n"
                    "(1,'김도현'),(2,'이유진'),(3,'박찬희'),(4,'최연서'),(5,'정하람'),(6,'문세윤');\n"
                    "CREATE TABLE ORDERS (id INTEGER, customer_id INTEGER, amount INTEGER, status TEXT);\n"
                    "INSERT INTO ORDERS VALUES\n"
                    "(1,1,12000,'완료'),(2,3,5000,'취소'),(3,1,7000,'완료'),\n"
                    "(4,6,90000,'완료'),(5,3,3000,'취소'),(6,4,15000,'완료'),(7,5,20000,'취소');"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE CUSTOMERS (id INTEGER, name TEXT);\n"
                    "INSERT INTO CUSTOMERS VALUES\n"
                    "(1,'홍서연'),(2,'감우재'),(3,'남지현'),(4,'류하진'),(5,'표민수');\n"
                    "CREATE TABLE ORDERS (id INTEGER, customer_id INTEGER, amount INTEGER, status TEXT);\n"
                    "INSERT INTO ORDERS VALUES\n"
                    "(1,2,10000,'완료'),(2,2,20000,'취소'),(3,5,15000,'취소'),\n"
                    "(4,1,8000,'완료'),(5,5,6000,'취소'),(6,1,9000,'완료');"
                ),
                "output": "",
            },
        ],
        reference_sql=(
            "SELECT c.id, c.name FROM CUSTOMERS c "
            "LEFT JOIN ORDERS o ON c.id = o.customer_id AND o.status = '완료' "
            "WHERE o.id IS NULL ORDER BY c.id;"
        ),
        tier="S1",
        freq=3,
    ),

    # ------------------------------------------------------------------
    # sql-30 : LEFT JOIN + GROUP BY — COUNT(*) 가 아니라 COUNT(컬럼)
    # ------------------------------------------------------------------
    Problem(
        id="sql-30",
        rank="Silver",
        title="신청 0명 강의까지 포함한 수강 인원",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "모든 강의의 수강 인원을 집계하되, 신청자가 한 명도 없는 강의도 0명으로 결과에 "
            "포함해야 한다.\n"
            "함정: LEFT JOIN 후 COUNT(*) 를 쓰면 신청자가 없는 강의도 NULL 행 1개가 "
            "세어져 1명으로 나온다. NULL 을 세지 않는 집계를 골라야 한다.\n\n"
            "COURSES 테이블:\n"
            "  id INTEGER — 강의 번호\n"
            "  title TEXT — 강의 이름\n\n"
            "ENROLLMENTS 테이블:\n"
            "  id INTEGER — 신청 번호\n"
            "  course_id INTEGER — 신청한 강의 번호(COURSES.id 참조)\n"
            "  student TEXT — 수강생 이름\n"
        ),
        input_desc="COURSES(id, title), ENROLLMENTS(id, course_id, student)",
        output_desc=(
            "강의 이름 title 과 수강 인원 cnt(신청 없으면 0) 를 "
            "인원 내림차순, 인원이 같으면 강의 이름 오름차순으로 출력한다."
        ),
        examples=[{
            "input": (
                "COURSES\n"
                "id | title\n"
                " 1 | 파이썬 입문\n"
                " 2 | SQL 첫걸음\n"
                " 3 | 자바 기초\n"
                " 4 | 웹 개발 실전\n"
                " 5 | 알고리즘 특강\n\n"
                "ENROLLMENTS\n"
                "id | course_id | student\n"
                " 1 | 1         | 김민준\n"
                " 2 | 1         | 이서연\n"
                " 3 | 2         | 박지훈\n"
                " 4 | 5         | 최수아\n"
                " 5 | 1         | 정도윤\n"
                " 6 | 5         | 강하은\n"
                " 7 | 3         | 윤시우\n"
                " 8 | 2         | 임서준\n"
                " 9 | 5         | 한지민"
            ),
            "output": "",
        }],
        hints=[
            "강의를 왼쪽에 두고 LEFT JOIN 해야 신청 0명 강의가 살아남는다.",
            "COUNT(e.id) 는 NULL 을 세지 않으므로 신청 없는 강의가 정확히 0으로 나온다.",
            "SELECT co.title, COUNT(e.id) AS cnt FROM COURSES co "
            "LEFT JOIN ENROLLMENTS e ON co.id = e.course_id GROUP BY co.id, co.title "
            "ORDER BY cnt DESC, co.title ASC;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE COURSES (id INTEGER, title TEXT);\n"
                    "INSERT INTO COURSES VALUES\n"
                    "(1,'파이썬 입문'),(2,'SQL 첫걸음'),(3,'자바 기초'),(4,'웹 개발 실전'),(5,'알고리즘 특강');\n"
                    "CREATE TABLE ENROLLMENTS (id INTEGER, course_id INTEGER, student TEXT);\n"
                    "INSERT INTO ENROLLMENTS VALUES\n"
                    "(1,1,'김민준'),(2,1,'이서연'),(3,2,'박지훈'),(4,5,'최수아'),\n"
                    "(5,1,'정도윤'),(6,5,'강하은'),(7,3,'윤시우'),(8,2,'임서준'),(9,5,'한지민');"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE COURSES (id INTEGER, title TEXT);\n"
                    "INSERT INTO COURSES VALUES\n"
                    "(1,'데이터 분석'),(2,'머신러닝 기초'),(3,'통계 입문'),(4,'엑셀 활용'),(5,'프레젠테이션');\n"
                    "CREATE TABLE ENROLLMENTS (id INTEGER, course_id INTEGER, student TEXT);\n"
                    "INSERT INTO ENROLLMENTS VALUES\n"
                    "(1,2,'서준호'),(2,2,'문가영'),(3,1,'배성우'),(4,4,'신유나'),\n"
                    "(5,2,'권민재'),(6,1,'조은채'),(7,3,'한소희'),(8,4,'오세훈');"
                ),
                "output": "",
            },
        ],
        reference_sql=(
            "SELECT co.title, COUNT(e.id) AS cnt FROM COURSES co "
            "LEFT JOIN ENROLLMENTS e ON co.id = e.course_id GROUP BY co.id, co.title "
            "ORDER BY cnt DESC, co.title ASC;"
        ),
        tier="S1",
        freq=3,
    ),

    # ------------------------------------------------------------------
    # sql-31 : SELF JOIN 계층 + 비교 조건
    # ------------------------------------------------------------------
    Problem(
        id="sql-31",
        rank="Silver",
        title="상사보다 급여가 높은 직원",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "직원 테이블의 manager_id 는 같은 테이블 안의 다른 행(직속 상사)을 가리킨다.\n"
            "자기 직속 상사보다 급여가 높은 직원을 모두 찾아라.\n"
            "최상위 직원(manager_id 가 NULL)은 비교 대상이 없으므로 자동으로 제외된다.\n\n"
            "EMPLOYEES 테이블:\n"
            "  id INTEGER — 사번\n"
            "  name TEXT — 직원 이름\n"
            "  salary INTEGER — 월 급여(만원)\n"
            "  manager_id INTEGER — 직속 상사의 사번(EMPLOYEES.id 참조, 없으면 NULL)\n"
        ),
        input_desc="EMPLOYEES(id, name, salary, manager_id)",
        output_desc=(
            "직원 이름 employee, 직원 급여 emp_salary, 상사 이름 manager, 상사 급여 mgr_salary 를 "
            "직원 사번 오름차순으로 출력한다."
        ),
        examples=[{
            "input": (
                "EMPLOYEES\n"
                "id | name   | salary | manager_id\n"
                " 1 | 김부장 | 7000   | NULL\n"
                " 2 | 이과장 | 5200   | 1\n"
                " 3 | 박과장 | 5500   | 1\n"
                " 4 | 최대리 | 5600   | 2\n"
                " 5 | 정대리 | 4300   | 3\n"
                " 6 | 강사원 | 3600   | 4\n"
                " 7 | 윤사원 | 5900   | 3"
            ),
            "output": "",
        }],
        hints=[
            "같은 테이블을 직원 역할과 상사 역할로 두 번 사용한다. 별칭을 다르게 붙이는 게 핵심.",
            "EMPLOYEES e JOIN EMPLOYEES m ON e.manager_id = m.id 뒤에 급여 비교 조건을 WHERE 로 건다.",
            "SELECT e.name AS employee, e.salary AS emp_salary, m.name AS manager, "
            "m.salary AS mgr_salary FROM EMPLOYEES e JOIN EMPLOYEES m ON e.manager_id = m.id "
            "WHERE e.salary > m.salary ORDER BY e.id;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE EMPLOYEES (id INTEGER, name TEXT, salary INTEGER, manager_id INTEGER);\n"
                    "INSERT INTO EMPLOYEES VALUES\n"
                    "(1,'김부장',7000,NULL),(2,'이과장',5200,1),(3,'박과장',5500,1),\n"
                    "(4,'최대리',5600,2),(5,'정대리',4300,3),(6,'강사원',3600,4),\n"
                    "(7,'윤사원',5900,3);"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE EMPLOYEES (id INTEGER, name TEXT, salary INTEGER, manager_id INTEGER);\n"
                    "INSERT INTO EMPLOYEES VALUES\n"
                    "(1,'한이사',9000,NULL),(2,'서팀장',6000,1),(3,'문팀장',6500,1),\n"
                    "(4,'배주임',6200,2),(5,'신주임',4800,2),(6,'권사원',4000,3),\n"
                    "(7,'조사원',5100,5),(8,'허사원',6600,3);"
                ),
                "output": "",
            },
        ],
        reference_sql=(
            "SELECT e.name AS employee, e.salary AS emp_salary, m.name AS manager, "
            "m.salary AS mgr_salary FROM EMPLOYEES e JOIN EMPLOYEES m ON e.manager_id = m.id "
            "WHERE e.salary > m.salary ORDER BY e.id;"
        ),
        tier="S1",
        freq=2,
    ),

    # ------------------------------------------------------------------
    # sql-32 : 3개 테이블 JOIN + GROUP BY 집계
    # ------------------------------------------------------------------
    Problem(
        id="sql-32",
        rank="Silver",
        title="주문별 결제 총액 계산",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "주문 상세 테이블에는 상품 번호와 수량만 있고 가격은 상품 테이블에 있다.\n"
            "세 테이블을 연결해 주문마다 결제 총액(각 상품 수량 × 단가의 합)을 구하라.\n\n"
            "ORDERS 테이블:\n"
            "  id INTEGER — 주문 번호\n"
            "  customer TEXT — 주문 고객 이름\n\n"
            "ORDER_ITEMS 테이블:\n"
            "  id INTEGER — 상세 번호\n"
            "  order_id INTEGER — 주문 번호(ORDERS.id 참조)\n"
            "  product_id INTEGER — 상품 번호(PRODUCTS.id 참조)\n"
            "  qty INTEGER — 주문 수량\n\n"
            "PRODUCTS 테이블:\n"
            "  id INTEGER — 상품 번호\n"
            "  name TEXT — 상품 이름\n"
            "  price INTEGER — 단가(원)\n"
        ),
        input_desc="ORDERS(id, customer), ORDER_ITEMS(id, order_id, product_id, qty), PRODUCTS(id, name, price)",
        output_desc=(
            "주문 번호 id, 고객 이름 customer, 결제 총액 total 을 "
            "총액 내림차순, 총액이 같으면 주문 번호 오름차순으로 출력한다."
        ),
        examples=[{
            "input": (
                "ORDERS\n"
                "id | customer\n"
                " 1 | 김하늘\n"
                " 2 | 박세영\n"
                " 3 | 이준호\n"
                " 4 | 최다인\n"
                " 5 | 정우진\n\n"
                "ORDER_ITEMS\n"
                "id | order_id | product_id | qty\n"
                " 1 | 1        | 1          | 2\n"
                " 2 | 1        | 4          | 1\n"
                " 3 | 2        | 3          | 1\n"
                " 4 | 3        | 2          | 1\n"
                " 5 | 3        | 5          | 3\n"
                " 6 | 4        | 1          | 1\n"
                " 7 | 5        | 4          | 2\n"
                " 8 | 5        | 5          | 1\n\n"
                "PRODUCTS\n"
                "id | name        | price\n"
                " 1 | 무선 마우스 |  25000\n"
                " 2 | 키보드      |  60000\n"
                " 3 | 모니터      | 200000\n"
                " 4 | 허브        |  15000\n"
                " 5 | 파우치      |  12000"
            ),
            "output": "",
        }],
        hints=[
            "상세 테이블을 가운데 두고 주문·상품 양쪽으로 JOIN 을 두 번 건다.",
            "행마다 qty * price 를 만든 뒤 주문 단위로 GROUP BY 해서 SUM 한다.",
            "SELECT o.id, o.customer, SUM(oi.qty * p.price) AS total FROM ORDERS o "
            "JOIN ORDER_ITEMS oi ON oi.order_id = o.id JOIN PRODUCTS p ON oi.product_id = p.id "
            "GROUP BY o.id, o.customer ORDER BY total DESC, o.id ASC;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE ORDERS (id INTEGER, customer TEXT);\n"
                    "INSERT INTO ORDERS VALUES (1,'김하늘'),(2,'박세영'),(3,'이준호'),(4,'최다인'),(5,'정우진');\n"
                    "CREATE TABLE ORDER_ITEMS (id INTEGER, order_id INTEGER, product_id INTEGER, qty INTEGER);\n"
                    "INSERT INTO ORDER_ITEMS VALUES\n"
                    "(1,1,1,2),(2,1,4,1),(3,2,3,1),(4,3,2,1),(5,3,5,3),(6,4,1,1),(7,5,4,2),(8,5,5,1);\n"
                    "CREATE TABLE PRODUCTS (id INTEGER, name TEXT, price INTEGER);\n"
                    "INSERT INTO PRODUCTS VALUES\n"
                    "(1,'무선 마우스',25000),(2,'키보드',60000),(3,'모니터',200000),(4,'허브',15000),(5,'파우치',12000);"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE ORDERS (id INTEGER, customer TEXT);\n"
                    "INSERT INTO ORDERS VALUES (1,'한소희'),(2,'오세훈'),(3,'임나연'),(4,'송민호'),(5,'유지아');\n"
                    "CREATE TABLE ORDER_ITEMS (id INTEGER, order_id INTEGER, product_id INTEGER, qty INTEGER);\n"
                    "INSERT INTO ORDER_ITEMS VALUES\n"
                    "(1,1,1,1),(2,2,2,3),(3,2,4,1),(4,3,3,2),(5,4,5,4),(6,5,1,1),(7,5,4,2);\n"
                    "CREATE TABLE PRODUCTS (id INTEGER, name TEXT, price INTEGER);\n"
                    "INSERT INTO PRODUCTS VALUES\n"
                    "(1,'텀블러',18000),(2,'에코백',9000),(3,'다이어리',12000),(4,'볼펜 세트',7000),(5,'머그컵',11000);"
                ),
                "output": "",
            },
        ],
        reference_sql=(
            "SELECT o.id, o.customer, SUM(oi.qty * p.price) AS total FROM ORDERS o "
            "JOIN ORDER_ITEMS oi ON oi.order_id = o.id JOIN PRODUCTS p ON oi.product_id = p.id "
            "GROUP BY o.id, o.customer ORDER BY total DESC, o.id ASC;"
        ),
        tier="S1",
        freq=2,
    ),

    # ------------------------------------------------------------------
    # sql-33 : JOIN + HAVING 복수 조건 + NULL 평점
    # ------------------------------------------------------------------
    Problem(
        id="sql-33",
        rank="Silver",
        title="신뢰할 수 있는 고평점 상품",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "리뷰 중에는 별점 없이 텍스트만 남긴 리뷰(rating 이 NULL)가 있다.\n"
            "'별점이 입력된 리뷰가 2건 이상'이면서 '별점 평균이 4.0 이상'인 상품만 골라라.\n"
            "함정 두 가지:\n"
            "  1) 리뷰 건수를 COUNT(*) 로 세면 별점 없는 리뷰까지 포함된다.\n"
            "  2) 별점 1건짜리 5점 상품은 평균이 높아도 신뢰 부족으로 탈락해야 한다.\n"
            "평균 별점은 소수 첫째 자리까지 반올림해 표시한다.\n\n"
            "PRODUCTS 테이블:\n"
            "  id INTEGER — 상품 번호\n"
            "  name TEXT — 상품 이름\n\n"
            "REVIEWS 테이블:\n"
            "  id INTEGER — 리뷰 번호\n"
            "  product_id INTEGER — 리뷰 대상 상품 번호(PRODUCTS.id 참조)\n"
            "  rating INTEGER — 별점(1~5, 텍스트만 남긴 리뷰는 NULL)\n"
        ),
        input_desc="PRODUCTS(id, name), REVIEWS(id, product_id, rating)",
        output_desc=(
            "조건을 만족하는 상품의 이름 name, 별점 입력 리뷰 수 rating_cnt, "
            "평균 별점 avg_rating(소수 첫째 자리 반올림) 을 "
            "평균 별점 내림차순, 같으면 상품 이름 오름차순으로 출력한다."
        ),
        examples=[{
            "input": (
                "PRODUCTS\n"
                "id | name\n"
                " 1 | 무선 마우스\n"
                " 2 | 기계식 키보드\n"
                " 3 | 모니터 받침대\n"
                " 4 | USB 허브\n"
                " 5 | 노트북 파우치\n\n"
                "REVIEWS\n"
                "id | product_id | rating\n"
                " 1 | 1          | 5\n"
                " 2 | 1          | 4\n"
                " 3 | 2          | 3\n"
                " 4 | 3          | 5\n"
                " 5 | 1          | NULL\n"
                " 6 | 2          | 4\n"
                " 7 | 3          | NULL\n"
                " 8 | 4          | 2\n"
                " 9 | 5          | 4\n"
                "10 | 5          | 4\n"
                "11 | 5          | 4\n"
                "12 | 1          | 4"
            ),
            "output": "",
        }],
        hints=[
            "AVG(rating) 은 NULL 을 빼고 평균 내므로, 건수도 같은 기준(NULL 제외)으로 세어야 짝이 맞는다.",
            "HAVING COUNT(r.rating) >= 2 AND AVG(r.rating) >= 4.0 — COUNT(*) 가 아니라 COUNT(r.rating) 이다.",
            "SELECT p.name, COUNT(r.rating) AS rating_cnt, ROUND(AVG(r.rating), 1) AS avg_rating "
            "FROM REVIEWS r JOIN PRODUCTS p ON r.product_id = p.id GROUP BY p.id, p.name "
            "HAVING COUNT(r.rating) >= 2 AND AVG(r.rating) >= 4.0 "
            "ORDER BY avg_rating DESC, p.name ASC;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE PRODUCTS (id INTEGER, name TEXT);\n"
                    "INSERT INTO PRODUCTS VALUES\n"
                    "(1,'무선 마우스'),(2,'기계식 키보드'),(3,'모니터 받침대'),(4,'USB 허브'),(5,'노트북 파우치');\n"
                    "CREATE TABLE REVIEWS (id INTEGER, product_id INTEGER, rating INTEGER);\n"
                    "INSERT INTO REVIEWS VALUES\n"
                    "(1,1,5),(2,1,4),(3,2,3),(4,3,5),(5,1,NULL),(6,2,4),\n"
                    "(7,3,NULL),(8,4,2),(9,5,4),(10,5,4),(11,5,4),(12,1,4);"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE PRODUCTS (id INTEGER, name TEXT);\n"
                    "INSERT INTO PRODUCTS VALUES\n"
                    "(1,'텀블러'),(2,'에코백'),(3,'다이어리'),(4,'볼펜 세트'),(5,'머그컵');\n"
                    "CREATE TABLE REVIEWS (id INTEGER, product_id INTEGER, rating INTEGER);\n"
                    "INSERT INTO REVIEWS VALUES\n"
                    "(1,1,4),(2,2,3),(3,1,5),(4,3,4),(5,2,3),(6,3,NULL),(7,4,5),(8,2,4),(9,3,4);"
                ),
                "output": "",
            },
        ],
        reference_sql=(
            "SELECT p.name, COUNT(r.rating) AS rating_cnt, ROUND(AVG(r.rating), 1) AS avg_rating "
            "FROM REVIEWS r JOIN PRODUCTS p ON r.product_id = p.id GROUP BY p.id, p.name "
            "HAVING COUNT(r.rating) >= 2 AND AVG(r.rating) >= 4.0 "
            "ORDER BY avg_rating DESC, p.name ASC;"
        ),
        tier="S1",
        freq=2,
    ),

    # ------------------------------------------------------------------
    # sql-34 : GROUP BY 다중 컬럼 + COUNT(DISTINCT) 함정
    # ------------------------------------------------------------------
    Problem(
        id="sql-34",
        rank="Silver",
        title="지역·상품별 매출과 판매 지점 수",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "판매 기록을 지역과 상품 두 기준으로 동시에 묶어, 조합마다 매출 합계와 "
            "'판매가 일어난 지점 수'를 구하려고 한다.\n"
            "같은 지점에서 같은 상품이 여러 번 팔린 기록이 있으므로, 지점 수는 중복을 "
            "제거하고 세야 한다. COUNT(store) 로 세면 판매 건수가 되어 버린다.\n\n"
            "SALES 테이블:\n"
            "  id INTEGER — 판매 번호\n"
            "  region TEXT — 판매 지역\n"
            "  product TEXT — 상품 이름\n"
            "  store TEXT — 판매 지점 이름\n"
            "  amount INTEGER — 판매 금액(원)\n"
        ),
        input_desc="SALES(id, region, product, store, amount)",
        output_desc=(
            "지역 region, 상품 product, 매출 합계 total, 판매 지점 수 store_cnt 를 "
            "지역 이름 오름차순, 같은 지역 안에서는 상품 이름 오름차순으로 출력한다."
        ),
        examples=[{
            "input": (
                "SALES\n"
                "id | region | product | store    | amount\n"
                " 1 | 서울   | 노트북  | 강남점   | 1200000\n"
                " 2 | 부산   | 노트북  | 해운대점 |  800000\n"
                " 3 | 서울   | 모니터  | 강남점   |  300000\n"
                " 4 | 서울   | 노트북  | 홍대점   |  950000\n"
                " 5 | 부산   | 모니터  | 해운대점 |  280000\n"
                " 6 | 대구   | 키보드  | 동성로점 |   90000\n"
                " 7 | 서울   | 모니터  | 강남점   |  310000\n"
                " 8 | 부산   | 노트북  | 서면점   |  760000\n"
                " 9 | 서울   | 노트북  | 강남점   |  400000"
            ),
            "output": "",
        }],
        hints=[
            "GROUP BY 에 컬럼 두 개를 나열하면 (지역, 상품) 조합별로 묶인다.",
            "지점 수는 COUNT(DISTINCT store) — DISTINCT 없이는 같은 지점이 판매 건수만큼 세어진다.",
            "SELECT region, product, SUM(amount) AS total, COUNT(DISTINCT store) AS store_cnt "
            "FROM SALES GROUP BY region, product ORDER BY region ASC, product ASC;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE SALES (id INTEGER, region TEXT, product TEXT, store TEXT, amount INTEGER);\n"
                    "INSERT INTO SALES VALUES\n"
                    "(1,'서울','노트북','강남점',1200000),(2,'부산','노트북','해운대점',800000),\n"
                    "(3,'서울','모니터','강남점',300000),(4,'서울','노트북','홍대점',950000),\n"
                    "(5,'부산','모니터','해운대점',280000),(6,'대구','키보드','동성로점',90000),\n"
                    "(7,'서울','모니터','강남점',310000),(8,'부산','노트북','서면점',760000),\n"
                    "(9,'서울','노트북','강남점',400000);"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE SALES (id INTEGER, region TEXT, product TEXT, store TEXT, amount INTEGER);\n"
                    "INSERT INTO SALES VALUES\n"
                    "(1,'경기','원두','수원점',52000),(2,'경기','티백','수원점',18000),\n"
                    "(3,'인천','원두','부평점',47000),(4,'경기','원두','성남점',33000),\n"
                    "(5,'인천','티백','부평점',22000),(6,'인천','원두','부평점',51000),\n"
                    "(7,'경기','머그컵','수원점',15000),(8,'경기','원두','수원점',21000);"
                ),
                "output": "",
            },
        ],
        reference_sql=(
            "SELECT region, product, SUM(amount) AS total, COUNT(DISTINCT store) AS store_cnt "
            "FROM SALES GROUP BY region, product ORDER BY region ASC, product ASC;"
        ),
        tier="S2",
        freq=2,
    ),
]
