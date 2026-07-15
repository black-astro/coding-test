# -*- coding: utf-8 -*-
"""SQL 기초 문제 sql-01 ~ sql-17 (SQLD 대비 수준).

단순 조회가 아니라 SQLD 시험에서 자주 나오는 함정을 문제마다 심었다:
NULL 3값 논리(비교/NOT IN/산술·연결 전파), AND/OR 괄호 우선순위,
NOT BETWEEN 경계값, LIKE 의 '_' vs '%', DISTINCT 와 WHERE 의 처리 순서,
ASC/DESC 혼합 다중 정렬, LIMIT+OFFSET 페이지네이션, WHERE 절 별칭 불가.
"""
from engine.models import Problem

PROBLEMS_PART = [
    # ------------------------------------------------------------------
    # sql-01 : 산술 연산과 NULL 전파
    # ------------------------------------------------------------------
    Problem(
        id="sql-01",
        rank="Bronze",
        title="재고 금액 계산과 NULL 전파",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "상품별 재고 금액(가격 x 재고 수량)을 계산해 보고서를 만들려 한다.\n"
            "아직 재고 실사를 하지 않은 상품은 stock 이 NULL 이며,\n"
            "이 경우 재고 금액도 계산 불가이므로 NULL 그대로 출력해야 한다.\n"
            "(NULL 과의 산술 연산 결과는 항상 NULL 이다 — 값을 치환하지 말 것)\n\n"
            "PRODUCT 테이블:\n"
            "  id INTEGER — 상품 번호\n"
            "  name TEXT — 상품명\n"
            "  price INTEGER — 가격(원)\n"
            "  stock INTEGER — 재고 수량(실사 전이면 NULL)\n"
        ),
        input_desc="PRODUCT(id, name, price, stock)",
        output_desc="모든 상품의 name 과 price*stock 값(별칭 stock_value)을 id 오름차순으로 조회한다. stock 이 NULL 인 상품은 stock_value 가 NULL 로 나와야 한다.",
        examples=[{
            "input": (
                "PRODUCT:\n"
                "id | name | price | stock\n"
                "1 | 무선마우스 | 15000 | 20\n"
                "2 | 텀블러 | 12000 | NULL\n"
                "3 | 노트 | 2500 | 100\n"
                "4 | 보조배터리 | 22000 | 15\n"
                "5 | 물티슈 | 3000 | NULL\n"
                "6 | 볼펜 | 1200 | 250"
            ),
            "output": "",
        }],
        hints=[
            "힌트1: 행을 걸러내는 문제가 아니다. SELECT 절에서 두 컬럼을 곱해 새 이름으로 출력하면 된다. NULL 이 낀 곱셈은 어떻게 되는지가 핵심이다.",
            "힌트2: SELECT price * stock AS 별칭 형태로 산술 + AS 를 쓴다. NULL 과의 사칙연산 결과는 항상 NULL 이므로 IFNULL 로 치환하면 오히려 오답이다.",
            "힌트3: SELECT name, price * stock AS stock_value FROM PRODUCT ORDER BY id;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE PRODUCT(id INTEGER, name TEXT, price INTEGER, stock INTEGER);\n"
                    "INSERT INTO PRODUCT VALUES (1,'무선마우스',15000,20);\n"
                    "INSERT INTO PRODUCT VALUES (2,'텀블러',12000,NULL);\n"
                    "INSERT INTO PRODUCT VALUES (3,'노트',2500,100);\n"
                    "INSERT INTO PRODUCT VALUES (4,'보조배터리',22000,15);\n"
                    "INSERT INTO PRODUCT VALUES (5,'물티슈',3000,NULL);\n"
                    "INSERT INTO PRODUCT VALUES (6,'볼펜',1200,250);"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE PRODUCT(id INTEGER, name TEXT, price INTEGER, stock INTEGER);\n"
                    "INSERT INTO PRODUCT VALUES (1,'키보드',45000,NULL);\n"
                    "INSERT INTO PRODUCT VALUES (2,'모니터암',68000,8);\n"
                    "INSERT INTO PRODUCT VALUES (3,'마스크',5000,300);\n"
                    "INSERT INTO PRODUCT VALUES (4,'스탠드조명',27000,NULL);\n"
                    "INSERT INTO PRODUCT VALUES (5,'핸드크림',8500,45);"
                ),
                "output": "",
            },
        ],
        reference_sql="SELECT name, price * stock AS stock_value FROM PRODUCT ORDER BY id;",
        tier="B3",
        freq=4,
    ),

    # ------------------------------------------------------------------
    # sql-02 : NULL 비교의 3값 논리 (WHERE 비교)
    # ------------------------------------------------------------------
    Problem(
        id="sql-02",
        rank="Bronze",
        title="연봉 5000 미만 직원 (NULL 3값 논리)",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "연봉이 5000만원 미만인 직원 명단을 뽑으려 한다.\n"
            "일부 직원은 연봉 협상 전이라 salary 가 NULL 이다.\n"
            "NULL 과의 비교(salary < 5000)는 TRUE 도 FALSE 도 아닌 UNKNOWN 이므로,\n"
            "연봉 미확정 직원은 결과에 포함되지 않아야 한다.\n\n"
            "EMPLOYEE 테이블:\n"
            "  id INTEGER — 직원 번호\n"
            "  name TEXT — 이름\n"
            "  dept TEXT — 부서\n"
            "  salary INTEGER — 연봉(만원, 미확정이면 NULL)\n"
        ),
        input_desc="EMPLOYEE(id, name, dept, salary)",
        output_desc="salary 가 5000 미만인 직원의 name, salary 를 salary 오름차순, 같으면 id 오름차순으로 조회한다. salary 가 NULL 인 직원은 제외된다.",
        examples=[{
            "input": (
                "EMPLOYEE:\n"
                "id | name | dept | salary\n"
                "1 | 김민준 | 개발 | 5200\n"
                "2 | 이서연 | 기획 | 4800\n"
                "3 | 박도윤 | 영업 | NULL\n"
                "4 | 최지우 | 인사 | 4500\n"
                "5 | 정하은 | 개발 | 6100\n"
                "6 | 강시우 | 마케팅 | NULL\n"
                "7 | 조유리 | 회계 | 3900"
            ),
            "output": "",
        }],
        hints=[
            "힌트1: 단순한 < 비교지만, NULL 행이 어떻게 처리되는지 알아야 한다. WHERE 는 결과가 TRUE 인 행만 통과시킨다 (UNKNOWN 은 탈락).",
            "힌트2: WHERE salary < 5000 하나면 충분하다. NULL 은 < 비교에서 UNKNOWN 이 되어 자동으로 걸러지므로 IS NOT NULL 을 덧붙일 필요가 없다.",
            "힌트3: SELECT name, salary FROM EMPLOYEE WHERE salary < 5000 ORDER BY salary ASC, id ASC;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE EMPLOYEE(id INTEGER, name TEXT, dept TEXT, salary INTEGER);\n"
                    "INSERT INTO EMPLOYEE VALUES (1,'김민준','개발',5200);\n"
                    "INSERT INTO EMPLOYEE VALUES (2,'이서연','기획',4800);\n"
                    "INSERT INTO EMPLOYEE VALUES (3,'박도윤','영업',NULL);\n"
                    "INSERT INTO EMPLOYEE VALUES (4,'최지우','인사',4500);\n"
                    "INSERT INTO EMPLOYEE VALUES (5,'정하은','개발',6100);\n"
                    "INSERT INTO EMPLOYEE VALUES (6,'강시우','마케팅',NULL);\n"
                    "INSERT INTO EMPLOYEE VALUES (7,'조유리','회계',3900);"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE EMPLOYEE(id INTEGER, name TEXT, dept TEXT, salary INTEGER);\n"
                    "INSERT INTO EMPLOYEE VALUES (1,'오세훈','개발',NULL);\n"
                    "INSERT INTO EMPLOYEE VALUES (2,'신유나','기획',4600);\n"
                    "INSERT INTO EMPLOYEE VALUES (3,'임재현','영업',5100);\n"
                    "INSERT INTO EMPLOYEE VALUES (4,'배수지','회계',4200);\n"
                    "INSERT INTO EMPLOYEE VALUES (5,'문지호','개발',4900);\n"
                    "INSERT INTO EMPLOYEE VALUES (6,'남하늘','인사',NULL);"
                ),
                "output": "",
            },
        ],
        reference_sql="SELECT name, salary FROM EMPLOYEE WHERE salary < 5000 ORDER BY salary ASC, id ASC;",
        tier="B3",
        freq=5,
    ),

    # ------------------------------------------------------------------
    # sql-03 : AND/OR 괄호 우선순위
    # ------------------------------------------------------------------
    Problem(
        id="sql-03",
        rank="Bronze",
        title="개발·기획 고연봉자 (괄호 우선순위)",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "부서가 '개발' 또는 '기획' 이면서 연봉이 5000만원 이상인 직원을 찾으려 한다.\n"
            "SQL 에서 AND 는 OR 보다 우선순위가 높다. 괄호 없이\n"
            "dept='개발' OR dept='기획' AND salary>=5000 이라고 쓰면\n"
            "'개발 전원 + 연봉 5000 이상 기획' 이라는 전혀 다른 뜻이 되므로 주의하라.\n\n"
            "EMPLOYEE 테이블:\n"
            "  id INTEGER — 직원 번호\n"
            "  name TEXT — 이름\n"
            "  dept TEXT — 부서\n"
            "  salary INTEGER — 연봉(만원)\n"
        ),
        input_desc="EMPLOYEE(id, name, dept, salary)",
        output_desc="dept 가 '개발' 또는 '기획' 이고 salary 가 5000 이상인 직원의 name, dept, salary 를 salary 내림차순, 같으면 id 오름차순으로 조회한다.",
        examples=[{
            "input": (
                "EMPLOYEE:\n"
                "id | name | dept | salary\n"
                "1 | 김태양 | 개발 | 4300\n"
                "2 | 이보라 | 개발 | 6100\n"
                "3 | 박찬희 | 기획 | 5300\n"
                "4 | 최아린 | 기획 | 4700\n"
                "5 | 정우석 | 영업 | 7200\n"
                "6 | 한소미 | 개발 | 5000"
            ),
            "output": "",
        }],
        hints=[
            "힌트1: '(개발 또는 기획) 그리고 연봉 조건' 이다. OR 묶음을 하나의 덩어리로 만들고 나서 AND 를 걸어야 한다. 예제에서 김태양(개발, 4300)이 포함되면 괄호를 잘못 쓴 것이다.",
            "힌트2: WHERE (dept = '개발' OR dept = '기획') AND salary >= 5000 — AND 가 OR 보다 먼저 결합하므로 괄호가 필수다.",
            "힌트3: SELECT name, dept, salary FROM EMPLOYEE WHERE (dept = '개발' OR dept = '기획') AND salary >= 5000 ORDER BY salary DESC, id ASC;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE EMPLOYEE(id INTEGER, name TEXT, dept TEXT, salary INTEGER);\n"
                    "INSERT INTO EMPLOYEE VALUES (1,'김태양','개발',4300);\n"
                    "INSERT INTO EMPLOYEE VALUES (2,'이보라','개발',6100);\n"
                    "INSERT INTO EMPLOYEE VALUES (3,'박찬희','기획',5300);\n"
                    "INSERT INTO EMPLOYEE VALUES (4,'최아린','기획',4700);\n"
                    "INSERT INTO EMPLOYEE VALUES (5,'정우석','영업',7200);\n"
                    "INSERT INTO EMPLOYEE VALUES (6,'한소미','개발',5000);"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE EMPLOYEE(id INTEGER, name TEXT, dept TEXT, salary INTEGER);\n"
                    "INSERT INTO EMPLOYEE VALUES (1,'노해준','기획',5900);\n"
                    "INSERT INTO EMPLOYEE VALUES (2,'구하린','영업',6500);\n"
                    "INSERT INTO EMPLOYEE VALUES (3,'황민서','개발',4800);\n"
                    "INSERT INTO EMPLOYEE VALUES (4,'심규원','개발',5200);\n"
                    "INSERT INTO EMPLOYEE VALUES (5,'변지아','인사',5600);\n"
                    "INSERT INTO EMPLOYEE VALUES (6,'표건우','기획',4900);\n"
                    "INSERT INTO EMPLOYEE VALUES (7,'설다연','개발',6800);"
                ),
                "output": "",
            },
        ],
        reference_sql="SELECT name, dept, salary FROM EMPLOYEE WHERE (dept = '개발' OR dept = '기획') AND salary >= 5000 ORDER BY salary DESC, id ASC;",
        tier="B3",
        freq=5,
    ),

    # ------------------------------------------------------------------
    # sql-04 : NOT IN 과 NULL (3값 논리)
    # ------------------------------------------------------------------
    Problem(
        id="sql-04",
        rank="Bronze",
        title="영업·인사 제외 직원 (NOT IN 과 NULL)",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "부서가 '영업' 도 '인사' 도 아닌 직원을 찾으려 한다.\n"
            "일부 직원은 아직 부서 미배정 상태(dept 가 NULL)다.\n"
            "dept NOT IN ('영업','인사') 는 dept<>'영업' AND dept<>'인사' 와 같은데,\n"
            "NULL 은 <> 비교가 UNKNOWN 이 되어 결과에 포함되지 않는다.\n"
            "즉 부서 미배정 직원은 '영업·인사가 아닌데도' 결과에서 빠져야 한다.\n\n"
            "EMPLOYEE 테이블:\n"
            "  id INTEGER — 직원 번호\n"
            "  name TEXT — 이름\n"
            "  dept TEXT — 부서(미배정이면 NULL)\n"
            "  salary INTEGER — 연봉(만원)\n"
        ),
        input_desc="EMPLOYEE(id, name, dept, salary)",
        output_desc="dept 가 '영업' 도 '인사' 도 아닌(그리고 NULL 도 아닌) 직원의 name, dept 를 id 오름차순으로 조회한다.",
        examples=[{
            "input": (
                "EMPLOYEE:\n"
                "id | name | dept | salary\n"
                "1 | 김도현 | 개발 | 5600\n"
                "2 | 이수민 | 영업 | 4900\n"
                "3 | 박정우 | NULL | 4100\n"
                "4 | 최하윤 | 기획 | 5100\n"
                "5 | 정서준 | 인사 | 4700\n"
                "6 | 강예린 | 회계 | 5300"
            ),
            "output": "",
        }],
        hints=[
            "힌트1: 여러 값을 한꺼번에 제외하는 부정 조건이다. NULL 부서가 결과에 어떻게 되는지가 이 문제의 함정이다.",
            "힌트2: WHERE dept NOT IN ('영업', '인사') 를 쓴다. NULL 은 비교 자체가 UNKNOWN 이라 NOT IN 으로도 통과하지 못한다 — 별도 조건 없이 자동 제외된다.",
            "힌트3: SELECT name, dept FROM EMPLOYEE WHERE dept NOT IN ('영업', '인사') ORDER BY id;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE EMPLOYEE(id INTEGER, name TEXT, dept TEXT, salary INTEGER);\n"
                    "INSERT INTO EMPLOYEE VALUES (1,'김도현','개발',5600);\n"
                    "INSERT INTO EMPLOYEE VALUES (2,'이수민','영업',4900);\n"
                    "INSERT INTO EMPLOYEE VALUES (3,'박정우',NULL,4100);\n"
                    "INSERT INTO EMPLOYEE VALUES (4,'최하윤','기획',5100);\n"
                    "INSERT INTO EMPLOYEE VALUES (5,'정서준','인사',4700);\n"
                    "INSERT INTO EMPLOYEE VALUES (6,'강예린','회계',5300);"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE EMPLOYEE(id INTEGER, name TEXT, dept TEXT, salary INTEGER);\n"
                    "INSERT INTO EMPLOYEE VALUES (1,'장미래',NULL,4400);\n"
                    "INSERT INTO EMPLOYEE VALUES (2,'김소연','개발',5800);\n"
                    "INSERT INTO EMPLOYEE VALUES (3,'윤재원','영업',5000);\n"
                    "INSERT INTO EMPLOYEE VALUES (4,'김태오','마케팅',5200);\n"
                    "INSERT INTO EMPLOYEE VALUES (5,'송하경',NULL,6100);\n"
                    "INSERT INTO EMPLOYEE VALUES (6,'백지헌','기획',4800);"
                ),
                "output": "",
            },
        ],
        reference_sql="SELECT name, dept FROM EMPLOYEE WHERE dept NOT IN ('영업', '인사') ORDER BY id;",
        tier="B3",
        freq=5,
    ),

    # ------------------------------------------------------------------
    # sql-05 : NOT BETWEEN 경계값
    # ------------------------------------------------------------------
    Problem(
        id="sql-05",
        rank="Bronze",
        title="보충·심화 대상자 (NOT BETWEEN 경계)",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "점수가 '보통 구간(60점 이상 79점 이하)' 을 벗어난 학생을 뽑아\n"
            "보충반(낮은 쪽) 또는 심화반(높은 쪽)에 배정하려 한다.\n"
            "BETWEEN a AND b 는 양 끝값을 포함하므로,\n"
            "NOT BETWEEN 60 AND 79 에서는 60점과 79점이 '제외' 된다는 점에 주의하라.\n\n"
            "STUDENT 테이블:\n"
            "  id INTEGER — 학번\n"
            "  name TEXT — 이름\n"
            "  grade INTEGER — 학년\n"
            "  score INTEGER — 점수\n"
        ),
        input_desc="STUDENT(id, name, grade, score)",
        output_desc="score 가 60 이상 79 이하 구간을 벗어난 학생의 name, score 를 score 내림차순, 같으면 id 오름차순으로 조회한다. 60점·79점 학생은 구간에 포함되므로 결과에 나오면 안 된다.",
        examples=[{
            "input": (
                "STUDENT:\n"
                "id | name | grade | score\n"
                "1 | 김하늘 | 1 | 59\n"
                "2 | 이준서 | 2 | 60\n"
                "3 | 박서연 | 2 | 72\n"
                "4 | 최민재 | 3 | 79\n"
                "5 | 정다인 | 2 | 80\n"
                "6 | 강윤호 | 1 | 95\n"
                "7 | 조은채 | 3 | 45"
            ),
            "output": "",
        }],
        hints=[
            "힌트1: '구간 밖' 조건이다. 59점과 80점은 포함되고 60점과 79점은 빠지는지 경계값을 따져 보라.",
            "힌트2: WHERE score NOT BETWEEN 60 AND 79 를 쓴다. BETWEEN 은 양 끝 포함이므로 NOT BETWEEN 은 score < 60 OR score > 79 와 같다.",
            "힌트3: SELECT name, score FROM STUDENT WHERE score NOT BETWEEN 60 AND 79 ORDER BY score DESC, id ASC;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE STUDENT(id INTEGER, name TEXT, grade INTEGER, score INTEGER);\n"
                    "INSERT INTO STUDENT VALUES (1,'김하늘',1,59);\n"
                    "INSERT INTO STUDENT VALUES (2,'이준서',2,60);\n"
                    "INSERT INTO STUDENT VALUES (3,'박서연',2,72);\n"
                    "INSERT INTO STUDENT VALUES (4,'최민재',3,79);\n"
                    "INSERT INTO STUDENT VALUES (5,'정다인',2,80);\n"
                    "INSERT INTO STUDENT VALUES (6,'강윤호',1,95);\n"
                    "INSERT INTO STUDENT VALUES (7,'조은채',3,45);"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE STUDENT(id INTEGER, name TEXT, grade INTEGER, score INTEGER);\n"
                    "INSERT INTO STUDENT VALUES (1,'홍서준',3,60);\n"
                    "INSERT INTO STUDENT VALUES (2,'안유진',1,58);\n"
                    "INSERT INTO STUDENT VALUES (3,'서지호',2,81);\n"
                    "INSERT INTO STUDENT VALUES (4,'남도현',2,79);\n"
                    "INSERT INTO STUDENT VALUES (5,'유채원',3,100);\n"
                    "INSERT INTO STUDENT VALUES (6,'백현우',1,66);"
                ),
                "output": "",
            },
        ],
        reference_sql="SELECT name, score FROM STUDENT WHERE score NOT BETWEEN 60 AND 79 ORDER BY score DESC, id ASC;",
        tier="B3",
        freq=4,
    ),

    # ------------------------------------------------------------------
    # sql-06 : LIKE '_' vs '%'
    # ------------------------------------------------------------------
    Problem(
        id="sql-06",
        rank="Bronze",
        title="세 글자 김씨 직원 (LIKE '_' vs '%')",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "사내 시스템에서 '이름이 정확히 세 글자이면서 김씨인 직원' 을 찾으려 한다.\n"
            "LIKE 패턴에서 % 는 0글자 이상 아무 문자열, _ 는 '정확히 한 글자' 를 뜻한다.\n"
            "'김%' 로 검색하면 두 글자 이름 '김온' 이나 네 글자 이름 '김새로미' 까지\n"
            "걸리므로 요구사항과 다르다.\n\n"
            "EMPLOYEE 테이블:\n"
            "  id INTEGER — 직원 번호\n"
            "  name TEXT — 이름\n"
            "  dept TEXT — 부서\n"
            "  salary INTEGER — 연봉(만원)\n"
        ),
        input_desc="EMPLOYEE(id, name, dept, salary)",
        output_desc="name 이 '김' 으로 시작하는 세 글자 이름인 직원의 name, dept 를 id 오름차순으로 조회한다.",
        examples=[{
            "input": (
                "EMPLOYEE:\n"
                "id | name | dept | salary\n"
                "1 | 김도현 | 개발 | 5600\n"
                "2 | 김온 | 기획 | 4900\n"
                "3 | 박김호 | 영업 | 5100\n"
                "4 | 김새로미 | 인사 | 4700\n"
                "5 | 김하윤 | 개발 | 6000\n"
                "6 | 이수민 | 회계 | 5300"
            ),
            "output": "",
        }],
        hints=[
            "힌트1: '시작 글자' 와 '전체 길이' 두 조건을 패턴 하나로 표현한다. % 로는 길이를 고정할 수 없다.",
            "힌트2: _ 는 정확히 한 글자와 대응한다. '김' 뒤에 _ 를 두 개 붙이면 '김 + 두 글자' 즉 세 글자 김씨만 매칭된다.",
            "힌트3: SELECT name, dept FROM EMPLOYEE WHERE name LIKE '김__' ORDER BY id;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE EMPLOYEE(id INTEGER, name TEXT, dept TEXT, salary INTEGER);\n"
                    "INSERT INTO EMPLOYEE VALUES (1,'김도현','개발',5600);\n"
                    "INSERT INTO EMPLOYEE VALUES (2,'김온','기획',4900);\n"
                    "INSERT INTO EMPLOYEE VALUES (3,'박김호','영업',5100);\n"
                    "INSERT INTO EMPLOYEE VALUES (4,'김새로미','인사',4700);\n"
                    "INSERT INTO EMPLOYEE VALUES (5,'김하윤','개발',6000);\n"
                    "INSERT INTO EMPLOYEE VALUES (6,'이수민','회계',5300);"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE EMPLOYEE(id INTEGER, name TEXT, dept TEXT, salary INTEGER);\n"
                    "INSERT INTO EMPLOYEE VALUES (1,'김솔','마케팅',4600);\n"
                    "INSERT INTO EMPLOYEE VALUES (2,'김태오','기획',5200);\n"
                    "INSERT INTO EMPLOYEE VALUES (3,'남궁김','개발',5900);\n"
                    "INSERT INTO EMPLOYEE VALUES (4,'김아라','영업',5000);\n"
                    "INSERT INTO EMPLOYEE VALUES (5,'김보라미','회계',4800);\n"
                    "INSERT INTO EMPLOYEE VALUES (6,'정김민','개발',5500);"
                ),
                "output": "",
            },
        ],
        reference_sql="SELECT name, dept FROM EMPLOYEE WHERE name LIKE '김__' ORDER BY id;",
        tier="B2",
        freq=4,
    ),

    # ------------------------------------------------------------------
    # sql-07 : WHERE → DISTINCT 처리 순서 + ORDER BY DESC
    # ------------------------------------------------------------------
    Problem(
        id="sql-07",
        rank="Bronze",
        title="3만원 이상 주문 고객 명단 (WHERE 와 DISTINCT 순서)",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "3만원 이상 주문을 '한 번이라도' 한 고객 명단을 중복 없이 만들려 한다.\n"
            "처리 순서가 핵심이다: 먼저 WHERE 로 3만원 이상 주문 행만 남기고,\n"
            "그 다음 남은 행에서 고객명 중복을 제거한다.\n"
            "소액 주문만 있는 고객은 명단에 없어야 하고, 소액·고액을 섞어 주문한\n"
            "고객은 고액 주문 덕분에 명단에 있어야 한다.\n\n"
            "ORDERS 테이블:\n"
            "  id INTEGER — 주문 번호\n"
            "  customer TEXT — 고객명\n"
            "  product TEXT — 주문 상품\n"
            "  amount INTEGER — 결제 금액(원)\n"
        ),
        input_desc="ORDERS(id, customer, product, amount)",
        output_desc="amount 가 30000 이상인 주문을 한 고객명(customer)을 중복 없이 customer 내림차순으로 조회한다.",
        examples=[{
            "input": (
                "ORDERS:\n"
                "id | customer | product | amount\n"
                "1 | 김민지 | 노트북 | 1200000\n"
                "2 | 이현수 | 마우스 | 25000\n"
                "3 | 김민지 | 키보드 | 89000\n"
                "4 | 박세영 | 모니터 | 330000\n"
                "5 | 이현수 | 이어폰 | 129000\n"
                "6 | 박세영 | 케이블 | 9000"
            ),
            "output": "",
        }],
        hints=[
            "힌트1: '조건을 만족하는 주문' 을 먼저 거르고 나서 고객명 중복을 없앤다. 이현수처럼 25000원 주문이 있어도 129000원 주문이 있으면 명단에 포함된다.",
            "힌트2: SELECT DISTINCT customer ... WHERE amount >= 30000 — WHERE 가 DISTINCT 보다 먼저 적용된다. 정렬은 ORDER BY customer DESC.",
            "힌트3: SELECT DISTINCT customer FROM ORDERS WHERE amount >= 30000 ORDER BY customer DESC;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE ORDERS(id INTEGER, customer TEXT, product TEXT, amount INTEGER);\n"
                    "INSERT INTO ORDERS VALUES (1,'김민지','노트북',1200000);\n"
                    "INSERT INTO ORDERS VALUES (2,'이현수','마우스',25000);\n"
                    "INSERT INTO ORDERS VALUES (3,'김민지','키보드',89000);\n"
                    "INSERT INTO ORDERS VALUES (4,'박세영','모니터',330000);\n"
                    "INSERT INTO ORDERS VALUES (5,'이현수','이어폰',129000);\n"
                    "INSERT INTO ORDERS VALUES (6,'박세영','케이블',9000);"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE ORDERS(id INTEGER, customer TEXT, product TEXT, amount INTEGER);\n"
                    "INSERT INTO ORDERS VALUES (1,'최도훈','책상',250000);\n"
                    "INSERT INTO ORDERS VALUES (2,'정예린','볼펜',4000);\n"
                    "INSERT INTO ORDERS VALUES (3,'최도훈','조명',42000);\n"
                    "INSERT INTO ORDERS VALUES (4,'한지우','선반',65000);\n"
                    "INSERT INTO ORDERS VALUES (5,'정예린','커튼',38000);\n"
                    "INSERT INTO ORDERS VALUES (6,'오나래','시계',29000);"
                ),
                "output": "",
            },
        ],
        reference_sql="SELECT DISTINCT customer FROM ORDERS WHERE amount >= 30000 ORDER BY customer DESC;",
        tier="B2",
        freq=4,
    ),

    # ------------------------------------------------------------------
    # sql-08 : ASC/DESC 혼합 다중 정렬 (3차 키까지)
    # ------------------------------------------------------------------
    Problem(
        id="sql-08",
        rank="Bronze",
        title="학년별 성적 순위표 (혼합 다중 정렬)",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "전교생 성적표를 학년 오름차순으로 묶고, 같은 학년 안에서는 점수가 높은\n"
            "학생이 먼저, 학년과 점수가 모두 같으면 학번이 빠른 학생이 먼저 오도록\n"
            "정렬하려 한다. 정렬 키마다 ASC/DESC 방향이 다르다는 점,\n"
            "그리고 3차 키까지 지정해야 순서가 유일하게 결정된다는 점이 핵심이다.\n\n"
            "STUDENT 테이블:\n"
            "  id INTEGER — 학번\n"
            "  name TEXT — 이름\n"
            "  grade INTEGER — 학년\n"
            "  score INTEGER — 점수\n"
        ),
        input_desc="STUDENT(id, name, grade, score)",
        output_desc="모든 학생의 name, grade, score 를 grade 오름차순, 같은 학년은 score 내림차순, 점수까지 같으면 id 오름차순으로 조회한다.",
        examples=[{
            "input": (
                "STUDENT:\n"
                "id | name | grade | score\n"
                "1 | 김로운 | 2 | 88\n"
                "2 | 이설아 | 1 | 95\n"
                "3 | 박준영 | 2 | 92\n"
                "4 | 최나윤 | 1 | 78\n"
                "5 | 정시온 | 3 | 85\n"
                "6 | 강예람 | 2 | 88\n"
                "7 | 조하람 | 3 | 91"
            ),
            "output": "",
        }],
        hints=[
            "힌트1: 정렬 기준이 세 개다. 1차 기준이 같은 행끼리만 2차 기준이 적용되고, 2차까지 같으면 3차 기준으로 순서를 확정한다.",
            "힌트2: ORDER BY 뒤에 쉼표로 키를 나열하고 키마다 ASC/DESC 를 따로 붙인다. DESC 는 붙인 키에만 적용된다 (전체에 적용되지 않는다).",
            "힌트3: SELECT name, grade, score FROM STUDENT ORDER BY grade ASC, score DESC, id ASC;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE STUDENT(id INTEGER, name TEXT, grade INTEGER, score INTEGER);\n"
                    "INSERT INTO STUDENT VALUES (1,'김로운',2,88);\n"
                    "INSERT INTO STUDENT VALUES (2,'이설아',1,95);\n"
                    "INSERT INTO STUDENT VALUES (3,'박준영',2,92);\n"
                    "INSERT INTO STUDENT VALUES (4,'최나윤',1,78);\n"
                    "INSERT INTO STUDENT VALUES (5,'정시온',3,85);\n"
                    "INSERT INTO STUDENT VALUES (6,'강예람',2,88);\n"
                    "INSERT INTO STUDENT VALUES (7,'조하람',3,91);"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE STUDENT(id INTEGER, name TEXT, grade INTEGER, score INTEGER);\n"
                    "INSERT INTO STUDENT VALUES (1,'문세아',3,72);\n"
                    "INSERT INTO STUDENT VALUES (2,'양도경',1,84);\n"
                    "INSERT INTO STUDENT VALUES (3,'홍주원',1,84);\n"
                    "INSERT INTO STUDENT VALUES (4,'전하율',2,96);\n"
                    "INSERT INTO STUDENT VALUES (5,'서보검',3,89);\n"
                    "INSERT INTO STUDENT VALUES (6,'임소율',2,67);\n"
                    "INSERT INTO STUDENT VALUES (7,'천서진',1,90);\n"
                    "INSERT INTO STUDENT VALUES (8,'맹주하',2,96);"
                ),
                "output": "",
            },
        ],
        reference_sql="SELECT name, grade, score FROM STUDENT ORDER BY grade ASC, score DESC, id ASC;",
        tier="B2",
        freq=4,
    ),

    # ------------------------------------------------------------------
    # sql-09 : LIMIT + OFFSET
    # ------------------------------------------------------------------
    Problem(
        id="sql-09",
        rank="Bronze",
        title="가격 3~5위 상품 (LIMIT + OFFSET)",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "쇼핑몰 기획전에 '가격 3위부터 5위까지' 의 상품을 올리려 한다.\n"
            "1·2위는 이미 다른 코너에 배치됐다.\n"
            "정렬 후 앞의 2건을 건너뛰고 3건을 가져와야 한다 — LIMIT 만으로는 안 되고\n"
            "OFFSET 으로 건너뛸 개수를 지정해야 한다.\n\n"
            "PRODUCT 테이블:\n"
            "  id INTEGER — 상품 번호\n"
            "  name TEXT — 상품명\n"
            "  category TEXT — 분류\n"
            "  price INTEGER — 가격(원)\n"
        ),
        input_desc="PRODUCT(id, name, category, price)",
        output_desc="price 내림차순(같으면 id 오름차순)으로 정렬했을 때 3번째부터 5번째까지 3개 상품의 name, price 를 조회한다.",
        examples=[{
            "input": (
                "PRODUCT:\n"
                "id | name | category | price\n"
                "1 | 게이밍모니터 | 전자 | 350000\n"
                "2 | 머그컵 | 생활 | 8000\n"
                "3 | 기계식키보드 | 전자 | 120000\n"
                "4 | 무선청소기 | 가전 | 420000\n"
                "5 | 에코백 | 패션 | 15000\n"
                "6 | 스마트워치 | 전자 | 280000\n"
                "7 | 담요 | 생활 | 23000"
            ),
            "output": "",
        }],
        hints=[
            "힌트1: 먼저 가격 내림차순으로 정렬하고, 상위 2건을 건너뛴 뒤 3건을 자른다. '몇 건 가져올지' 와 '몇 건 건너뛸지' 는 서로 다른 키워드다.",
            "힌트2: LIMIT 가져올개수 OFFSET 건너뛸개수 를 ORDER BY 뒤에 쓴다. 3~5위이므로 OFFSET 2, LIMIT 3 이다.",
            "힌트3: SELECT name, price FROM PRODUCT ORDER BY price DESC, id ASC LIMIT 3 OFFSET 2;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE PRODUCT(id INTEGER, name TEXT, category TEXT, price INTEGER);\n"
                    "INSERT INTO PRODUCT VALUES (1,'게이밍모니터','전자',350000);\n"
                    "INSERT INTO PRODUCT VALUES (2,'머그컵','생활',8000);\n"
                    "INSERT INTO PRODUCT VALUES (3,'기계식키보드','전자',120000);\n"
                    "INSERT INTO PRODUCT VALUES (4,'무선청소기','가전',420000);\n"
                    "INSERT INTO PRODUCT VALUES (5,'에코백','패션',15000);\n"
                    "INSERT INTO PRODUCT VALUES (6,'스마트워치','전자',280000);\n"
                    "INSERT INTO PRODUCT VALUES (7,'담요','생활',23000);"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE PRODUCT(id INTEGER, name TEXT, category TEXT, price INTEGER);\n"
                    "INSERT INTO PRODUCT VALUES (1,'전기포트','가전',39000);\n"
                    "INSERT INTO PRODUCT VALUES (2,'노트북거치대','전자',52000);\n"
                    "INSERT INTO PRODUCT VALUES (3,'커피머신','가전',390000);\n"
                    "INSERT INTO PRODUCT VALUES (4,'수납박스','생활',12000);\n"
                    "INSERT INTO PRODUCT VALUES (5,'태블릿','전자',520000);\n"
                    "INSERT INTO PRODUCT VALUES (6,'가습기','가전',87000);"
                ),
                "output": "",
            },
        ],
        reference_sql="SELECT name, price FROM PRODUCT ORDER BY price DESC, id ASC LIMIT 3 OFFSET 2;",
        tier="B2",
        freq=4,
    ),

    # ------------------------------------------------------------------
    # sql-10 : LIKE 와 NULL 자동 제외 (3값 논리)
    # ------------------------------------------------------------------
    Problem(
        id="sql-10",
        rank="Bronze",
        title="휴대폰 번호 보유 회원 (LIKE 와 NULL)",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "게시판 회원 중 '010-' 으로 시작하는 휴대폰 번호를 등록한 회원에게만\n"
            "인증 문자를 보내려 한다. 번호 미등록 회원은 phone 이 NULL 이고,\n"
            "유선 번호(02-, 031- 등)를 등록한 회원도 있다.\n"
            "NULL 에 대한 LIKE 결과는 UNKNOWN 이므로, 미등록 회원은 별도 조건 없이\n"
            "자동으로 걸러진다 — IS NOT NULL 을 덧붙일 필요가 없다.\n\n"
            "MEMBER 테이블:\n"
            "  id INTEGER — 회원 번호\n"
            "  name TEXT — 이름\n"
            "  email TEXT — 이메일\n"
            "  phone TEXT — 전화번호(미등록이면 NULL)\n"
        ),
        input_desc="MEMBER(id, name, email, phone)",
        output_desc="phone 이 '010-' 으로 시작하는 회원의 name, phone 을 id 오름차순으로 조회한다. phone 이 NULL 이거나 유선 번호인 회원은 제외된다.",
        examples=[{
            "input": (
                "MEMBER:\n"
                "id | name | email | phone\n"
                "1 | 김수아 | sua@example.com | 010-1111-2222\n"
                "2 | 이도윤 | doyun@example.com | NULL\n"
                "3 | 박예준 | yejun@example.com | 02-333-4444\n"
                "4 | 최서현 | seohyun@example.com | 010-5555-6666\n"
                "5 | 정지훈 | jihun@example.com | NULL\n"
                "6 | 한별이 | byeol@example.com | 031-777-8888"
            ),
            "output": "",
        }],
        hints=[
            "힌트1: '특정 문자열로 시작' 은 패턴 매칭이다. NULL 인 행이 LIKE 조건에서 어떻게 되는지 생각해 보라 — WHERE 는 TRUE 인 행만 통과시킨다.",
            "힌트2: WHERE phone LIKE '010-%' 하나면 된다. NULL LIKE '010-%' 는 UNKNOWN 이라 자동 탈락하므로 IS NOT NULL 은 불필요하다.",
            "힌트3: SELECT name, phone FROM MEMBER WHERE phone LIKE '010-%' ORDER BY id;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE MEMBER(id INTEGER, name TEXT, email TEXT, phone TEXT);\n"
                    "INSERT INTO MEMBER VALUES (1,'김수아','sua@example.com','010-1111-2222');\n"
                    "INSERT INTO MEMBER VALUES (2,'이도윤','doyun@example.com',NULL);\n"
                    "INSERT INTO MEMBER VALUES (3,'박예준','yejun@example.com','02-333-4444');\n"
                    "INSERT INTO MEMBER VALUES (4,'최서현','seohyun@example.com','010-5555-6666');\n"
                    "INSERT INTO MEMBER VALUES (5,'정지훈','jihun@example.com',NULL);\n"
                    "INSERT INTO MEMBER VALUES (6,'한별이','byeol@example.com','031-777-8888');"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE MEMBER(id INTEGER, name TEXT, email TEXT, phone TEXT);\n"
                    "INSERT INTO MEMBER VALUES (1,'오세아','sea@example.com','02-1234-5678');\n"
                    "INSERT INTO MEMBER VALUES (2,'서강준','kang@example.com','010-2222-3333');\n"
                    "INSERT INTO MEMBER VALUES (3,'남주혁','juhyuk@example.com',NULL);\n"
                    "INSERT INTO MEMBER VALUES (4,'유해나','hana@example.com','010-4444-5555');\n"
                    "INSERT INTO MEMBER VALUES (5,'백도희','dohee@example.com',NULL);\n"
                    "INSERT INTO MEMBER VALUES (6,'문가영','gayoung@example.com','070-8888-9999');\n"
                    "INSERT INTO MEMBER VALUES (7,'홍시아','sia@example.com','010-6666-7777');"
                ),
                "output": "",
            },
        ],
        reference_sql="SELECT name, phone FROM MEMBER WHERE phone LIKE '010-%' ORDER BY id;",
        tier="B2",
        freq=4,
    ),

    # ------------------------------------------------------------------
    # sql-11 : IFNULL/COALESCE + 산술 (NULL 전파 방지)
    # ------------------------------------------------------------------
    Problem(
        id="sql-11",
        rank="Bronze",
        title="총보수 순위 (IFNULL 로 NULL 전파 차단)",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "직원별 총보수(연봉 + 보너스)를 계산해 높은 순으로 정렬하려 한다.\n"
            "보너스 미지급 직원은 bonus 가 NULL 인데,\n"
            "salary + bonus 로 계산하면 NULL 이 전파되어 총보수 전체가 NULL 이 된다.\n"
            "미지급은 0원으로 간주하고 계산해야 한다.\n\n"
            "EMPLOYEE 테이블:\n"
            "  id INTEGER — 직원 번호\n"
            "  name TEXT — 이름\n"
            "  salary INTEGER — 연봉(만원)\n"
            "  bonus INTEGER — 보너스(만원, 미지급이면 NULL)\n"
        ),
        input_desc="EMPLOYEE(id, name, salary, bonus)",
        output_desc="모든 직원의 name 과 총보수(salary + 보너스, 보너스 NULL 은 0 취급, 별칭 total_pay)를 total_pay 내림차순, 같으면 id 오름차순으로 조회한다.",
        examples=[{
            "input": (
                "EMPLOYEE:\n"
                "id | name | salary | bonus\n"
                "1 | 김주원 | 5200 | 300\n"
                "2 | 이가온 | 6100 | NULL\n"
                "3 | 박시현 | 4800 | 150\n"
                "4 | 최이안 | 5900 | NULL\n"
                "5 | 정라엘 | 5000 | 200"
            ),
            "output": "",
        }],
        hints=[
            "힌트1: salary + bonus 를 그대로 쓰면 보너스 미지급자의 총보수가 NULL 이 되어 순위에서 사라진다. 더하기 전에 NULL 을 0 으로 바꿔야 한다.",
            "힌트2: IFNULL(bonus, 0) 또는 COALESCE(bonus, 0) 로 치환한 뒤 salary 와 더한다. ORDER BY 에서는 SELECT 별칭을 그대로 쓸 수 있다.",
            "힌트3: SELECT name, salary + IFNULL(bonus, 0) AS total_pay FROM EMPLOYEE ORDER BY total_pay DESC, id ASC;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE EMPLOYEE(id INTEGER, name TEXT, salary INTEGER, bonus INTEGER);\n"
                    "INSERT INTO EMPLOYEE VALUES (1,'김주원',5200,300);\n"
                    "INSERT INTO EMPLOYEE VALUES (2,'이가온',6100,NULL);\n"
                    "INSERT INTO EMPLOYEE VALUES (3,'박시현',4800,150);\n"
                    "INSERT INTO EMPLOYEE VALUES (4,'최이안',5900,NULL);\n"
                    "INSERT INTO EMPLOYEE VALUES (5,'정라엘',5000,200);"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE EMPLOYEE(id INTEGER, name TEXT, salary INTEGER, bonus INTEGER);\n"
                    "INSERT INTO EMPLOYEE VALUES (1,'노윤성',4700,NULL);\n"
                    "INSERT INTO EMPLOYEE VALUES (2,'구본아',5300,400);\n"
                    "INSERT INTO EMPLOYEE VALUES (3,'황도영',6200,250);\n"
                    "INSERT INTO EMPLOYEE VALUES (4,'심채린',5800,NULL);\n"
                    "INSERT INTO EMPLOYEE VALUES (5,'변우주',4900,350);\n"
                    "INSERT INTO EMPLOYEE VALUES (6,'표민아',5100,NULL);"
                ),
                "output": "",
            },
        ],
        reference_sql="SELECT name, salary + IFNULL(bonus, 0) AS total_pay FROM EMPLOYEE ORDER BY total_pay DESC, id ASC;",
        tier="B2",
        freq=5,
    ),

    # ------------------------------------------------------------------
    # sql-12 : 문자열 연결(||)과 NULL 전파
    # ------------------------------------------------------------------
    Problem(
        id="sql-12",
        rank="Bronze",
        title="닉네임 표시명 만들기 (|| 와 NULL)",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "게시판 회원 표시명을 '이름(닉네임)' 형식으로 만들려 한다.\n"
            "닉네임을 설정하지 않은 회원은 nickname 이 NULL 인데,\n"
            "|| 연결에 NULL 이 하나라도 끼면 결과 전체가 NULL 이 되어 버린다.\n"
            "닉네임 미설정 회원은 '미설정' 이라는 글자로 대신 표시해야 한다.\n"
            "예: 이름 '김수아', 닉네임 NULL → '김수아(미설정)'\n\n"
            "MEMBER 테이블:\n"
            "  id INTEGER — 회원 번호\n"
            "  name TEXT — 이름\n"
            "  nickname TEXT — 닉네임(미설정이면 NULL)\n"
        ),
        input_desc="MEMBER(id, name, nickname)",
        output_desc="모든 회원에 대해 '이름(닉네임)' 형식 문자열(닉네임 NULL 은 '미설정' 으로 치환, 별칭 display)을 id 오름차순으로 조회한다.",
        examples=[{
            "input": (
                "MEMBER:\n"
                "id | name | nickname\n"
                "1 | 김수아 | NULL\n"
                "2 | 이도윤 | 바람돌이\n"
                "3 | 박예준 | 코딩왕\n"
                "4 | 최서현 | NULL\n"
                "5 | 정지훈 | 밤하늘"
            ),
            "output": "",
        }],
        hints=[
            "힌트1: name || '(' || nickname || ')' 를 그대로 쓰면 닉네임 미설정 회원의 표시명이 통째로 NULL 이 된다. 연결하기 전에 NULL 을 문자로 치환해야 한다.",
            "힌트2: SQLite 의 문자열 연결은 || 연산자, NULL 치환은 IFNULL(nickname, '미설정') 이다. (CONCAT 함수가 아니다)",
            "힌트3: SELECT name || '(' || IFNULL(nickname, '미설정') || ')' AS display FROM MEMBER ORDER BY id;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE MEMBER(id INTEGER, name TEXT, nickname TEXT);\n"
                    "INSERT INTO MEMBER VALUES (1,'김수아',NULL);\n"
                    "INSERT INTO MEMBER VALUES (2,'이도윤','바람돌이');\n"
                    "INSERT INTO MEMBER VALUES (3,'박예준','코딩왕');\n"
                    "INSERT INTO MEMBER VALUES (4,'최서현',NULL);\n"
                    "INSERT INTO MEMBER VALUES (5,'정지훈','밤하늘');"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE MEMBER(id INTEGER, name TEXT, nickname TEXT);\n"
                    "INSERT INTO MEMBER VALUES (1,'한별이','샛별');\n"
                    "INSERT INTO MEMBER VALUES (2,'오세아',NULL);\n"
                    "INSERT INTO MEMBER VALUES (3,'서강준','달리기왕');\n"
                    "INSERT INTO MEMBER VALUES (4,'남주혁',NULL);\n"
                    "INSERT INTO MEMBER VALUES (5,'유해나','해바라기');\n"
                    "INSERT INTO MEMBER VALUES (6,'백도희',NULL);"
                ),
                "output": "",
            },
        ],
        reference_sql="SELECT name || '(' || IFNULL(nickname, '미설정') || ')' AS display FROM MEMBER ORDER BY id;",
        tier="B1",
        freq=4,
    ),

    # ------------------------------------------------------------------
    # sql-13 : WHERE 절에서 별칭 사용 불가 + 산술 조건
    # ------------------------------------------------------------------
    Problem(
        id="sql-13",
        rank="Bronze",
        title="할인가 3만원 이하 상품 (WHERE 와 별칭)",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "전 상품 10% 할인 행사에서, 할인가(price 의 90%)가 30000원 이하인\n"
            "상품만 '3만원 코너' 에 진열하려 한다.\n"
            "SQL 실행 순서상 WHERE 는 SELECT 보다 먼저 처리되므로,\n"
            "SELECT 에서 붙인 별칭(sale_price)을 WHERE 에서는 쓸 수 없다 —\n"
            "WHERE 에는 계산식을 다시 써야 한다. (ORDER BY 에서는 별칭 사용 가능)\n\n"
            "PRODUCT 테이블:\n"
            "  id INTEGER — 상품 번호\n"
            "  name TEXT — 상품명\n"
            "  price INTEGER — 정가(원)\n"
        ),
        input_desc="PRODUCT(id, name, price)",
        output_desc="할인가(price * 90 / 100)가 30000 이하인 상품의 name 과 할인가(별칭 sale_price)를 sale_price 내림차순, 같으면 id 오름차순으로 조회한다.",
        examples=[{
            "input": (
                "PRODUCT:\n"
                "id | name | price\n"
                "1 | 무선마우스 | 15000\n"
                "2 | 키보드 | 45000\n"
                "3 | 텀블러 | 12000\n"
                "4 | 스탠드조명 | 27000\n"
                "5 | 모니터암 | 68000\n"
                "6 | 이어폰 | 33000"
            ),
            "output": "",
        }],
        hints=[
            "힌트1: 조건 기준이 원래 컬럼이 아니라 '계산된 할인가' 다. WHERE 절이 SELECT 별칭보다 먼저 실행된다는 순서(FROM → WHERE → SELECT → ORDER BY)를 떠올려라.",
            "힌트2: WHERE sale_price <= 30000 은 오류다. WHERE 에는 price * 90 / 100 <= 30000 처럼 식을 그대로 쓰고, ORDER BY 에서만 별칭을 쓴다.",
            "힌트3: SELECT name, price * 90 / 100 AS sale_price FROM PRODUCT WHERE price * 90 / 100 <= 30000 ORDER BY sale_price DESC, id ASC;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE PRODUCT(id INTEGER, name TEXT, price INTEGER);\n"
                    "INSERT INTO PRODUCT VALUES (1,'무선마우스',15000);\n"
                    "INSERT INTO PRODUCT VALUES (2,'키보드',45000);\n"
                    "INSERT INTO PRODUCT VALUES (3,'텀블러',12000);\n"
                    "INSERT INTO PRODUCT VALUES (4,'스탠드조명',27000);\n"
                    "INSERT INTO PRODUCT VALUES (5,'모니터암',68000);\n"
                    "INSERT INTO PRODUCT VALUES (6,'이어폰',33000);"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE PRODUCT(id INTEGER, name TEXT, price INTEGER);\n"
                    "INSERT INTO PRODUCT VALUES (1,'가습기',33300);\n"
                    "INSERT INTO PRODUCT VALUES (2,'커피머신',390000);\n"
                    "INSERT INTO PRODUCT VALUES (3,'수납박스',12000);\n"
                    "INSERT INTO PRODUCT VALUES (4,'전기포트',33400);\n"
                    "INSERT INTO PRODUCT VALUES (5,'담요',23000);\n"
                    "INSERT INTO PRODUCT VALUES (6,'밥솥',215000);"
                ),
                "output": "",
            },
        ],
        reference_sql="SELECT name, price * 90 / 100 AS sale_price FROM PRODUCT WHERE price * 90 / 100 <= 30000 ORDER BY sale_price DESC, id ASC;",
        tier="B1",
        freq=4,
    ),

    # ------------------------------------------------------------------
    # sql-14 : NOT (A OR B) 부정 논리 + NULL
    # ------------------------------------------------------------------
    Problem(
        id="sql-14",
        rank="Bronze",
        title="소설·시가 아닌 책 (부정 논리와 NULL)",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "도서관에서 장르가 '소설' 도 '시' 도 아닌 책만 골라 비문학 코너를 만들려 한다.\n"
            "장르 미분류 도서는 genre 가 NULL 이다.\n"
            "NOT (genre='소설' OR genre='시') 에서 genre 가 NULL 이면\n"
            "안쪽이 UNKNOWN → NOT UNKNOWN 도 UNKNOWN 이므로 미분류 도서는 제외된다.\n"
            "또한 NOT genre='소설' OR genre='시' 처럼 괄호를 빼면\n"
            "완전히 다른 조건이 되므로 주의하라.\n\n"
            "BOOK 테이블:\n"
            "  id INTEGER — 도서 번호\n"
            "  title TEXT — 제목\n"
            "  genre TEXT — 장르(미분류면 NULL)\n"
        ),
        input_desc="BOOK(id, title, genre)",
        output_desc="genre 가 '소설' 도 '시' 도 아닌(NULL 도 아닌) 책의 title, genre 를 id 오름차순으로 조회한다.",
        examples=[{
            "input": (
                "BOOK:\n"
                "id | title | genre\n"
                "1 | 별의노래 | 소설\n"
                "2 | 알고리즘첫걸음 | IT\n"
                "3 | 마음의정원 | 에세이\n"
                "4 | 겨울편지 | 시\n"
                "5 | 데이터베이스입문 | IT\n"
                "6 | 이름없는책 | NULL\n"
                "7 | 여행의기록 | 에세이"
            ),
            "output": "",
        }],
        hints=[
            "힌트1: '소설 또는 시' 라는 묶음 전체를 부정한다. 드모르간 법칙대로 genre <> '소설' AND genre <> '시' 와 같고, NOT IN ('소설','시') 로도 쓸 수 있다.",
            "힌트2: WHERE NOT (genre = '소설' OR genre = '시') — OR 묶음에 괄호가 필수다. NULL 장르는 UNKNOWN 이 되어 자동 제외된다.",
            "힌트3: SELECT title, genre FROM BOOK WHERE NOT (genre = '소설' OR genre = '시') ORDER BY id;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE BOOK(id INTEGER, title TEXT, genre TEXT);\n"
                    "INSERT INTO BOOK VALUES (1,'별의노래','소설');\n"
                    "INSERT INTO BOOK VALUES (2,'알고리즘첫걸음','IT');\n"
                    "INSERT INTO BOOK VALUES (3,'마음의정원','에세이');\n"
                    "INSERT INTO BOOK VALUES (4,'겨울편지','시');\n"
                    "INSERT INTO BOOK VALUES (5,'데이터베이스입문','IT');\n"
                    "INSERT INTO BOOK VALUES (6,'이름없는책',NULL);\n"
                    "INSERT INTO BOOK VALUES (7,'여행의기록','에세이');"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE BOOK(id INTEGER, title TEXT, genre TEXT);\n"
                    "INSERT INTO BOOK VALUES (1,'바다일기','에세이');\n"
                    "INSERT INTO BOOK VALUES (2,'그림자도시','소설');\n"
                    "INSERT INTO BOOK VALUES (3,'무제',NULL);\n"
                    "INSERT INTO BOOK VALUES (4,'봄의언어','시');\n"
                    "INSERT INTO BOOK VALUES (5,'요리의기술','실용');\n"
                    "INSERT INTO BOOK VALUES (6,'파이썬완성','IT');"
                ),
                "output": "",
            },
        ],
        reference_sql="SELECT title, genre FROM BOOK WHERE NOT (genre = '소설' OR genre = '시') ORDER BY id;",
        tier="B1",
        freq=4,
    ),

    # ------------------------------------------------------------------
    # sql-15 : WHERE + 다중 정렬 + LIMIT/OFFSET 페이지네이션 종합
    # ------------------------------------------------------------------
    Problem(
        id="sql-15",
        rank="Bronze",
        title="고액 주문 2페이지 조회 (페이지네이션 종합)",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "관리자 화면에서 2만원 이상 주문을 금액 큰 순으로 페이지당 3건씩 보여준다.\n"
            "지금 필요한 것은 '2페이지', 즉 정렬 결과의 4번째부터 6번째 주문이다.\n"
            "걸러내기(WHERE) → 정렬(ORDER BY) → 건너뛰고 자르기(LIMIT/OFFSET) 의\n"
            "실행 순서를 정확히 조합해야 한다.\n\n"
            "ORDERS 테이블:\n"
            "  id INTEGER — 주문 번호\n"
            "  customer TEXT — 고객명\n"
            "  product TEXT — 주문 상품\n"
            "  amount INTEGER — 결제 금액(원)\n"
        ),
        input_desc="ORDERS(id, customer, product, amount)",
        output_desc="amount 가 20000 이상인 주문을 amount 내림차순(같으면 id 오름차순)으로 정렬한 뒤, 4번째부터 최대 3건의 customer, amount 를 조회한다.",
        examples=[{
            "input": (
                "ORDERS:\n"
                "id | customer | product | amount\n"
                "1 | 김하진 | 청소기 | 189000\n"
                "2 | 이로운 | 물티슈 | 12000\n"
                "3 | 박세리 | 에어프라이어 | 99000\n"
                "4 | 최운재 | 커피머신 | 275000\n"
                "5 | 정보름 | 마우스패드 | 8000\n"
                "6 | 강다현 | 전기장판 | 64000\n"
                "7 | 조민규 | 공기청정기 | 210000\n"
                "8 | 윤설희 | 텀블러 | 45000\n"
                "9 | 홍이안 | 무릎담요 | 33000"
            ),
            "output": "",
        }],
        hints=[
            "힌트1: 2만원 미만 주문을 먼저 제외하고 정렬해야 페이지가 올바르게 잘린다. 2페이지 = 앞의 3건(1페이지)을 건너뛴 다음 3건이다.",
            "힌트2: WHERE amount >= 20000, ORDER BY amount DESC (동률은 id ASC), 그리고 LIMIT 3 OFFSET 3 을 이 순서대로 쓴다.",
            "힌트3: SELECT customer, amount FROM ORDERS WHERE amount >= 20000 ORDER BY amount DESC, id ASC LIMIT 3 OFFSET 3;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE ORDERS(id INTEGER, customer TEXT, product TEXT, amount INTEGER);\n"
                    "INSERT INTO ORDERS VALUES (1,'김하진','청소기',189000);\n"
                    "INSERT INTO ORDERS VALUES (2,'이로운','물티슈',12000);\n"
                    "INSERT INTO ORDERS VALUES (3,'박세리','에어프라이어',99000);\n"
                    "INSERT INTO ORDERS VALUES (4,'최운재','커피머신',275000);\n"
                    "INSERT INTO ORDERS VALUES (5,'정보름','마우스패드',8000);\n"
                    "INSERT INTO ORDERS VALUES (6,'강다현','전기장판',64000);\n"
                    "INSERT INTO ORDERS VALUES (7,'조민규','공기청정기',210000);\n"
                    "INSERT INTO ORDERS VALUES (8,'윤설희','텀블러',45000);\n"
                    "INSERT INTO ORDERS VALUES (9,'홍이안','무릎담요',33000);"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE ORDERS(id INTEGER, customer TEXT, product TEXT, amount INTEGER);\n"
                    "INSERT INTO ORDERS VALUES (1,'홍바다','블렌더',72000);\n"
                    "INSERT INTO ORDERS VALUES (2,'안누리','수세미',3500);\n"
                    "INSERT INTO ORDERS VALUES (3,'서초원','전자레인지',134000);\n"
                    "INSERT INTO ORDERS VALUES (4,'남기람','행주',4200);\n"
                    "INSERT INTO ORDERS VALUES (5,'유가람','식기세척기',560000);\n"
                    "INSERT INTO ORDERS VALUES (6,'백시원','밥솥',215000);\n"
                    "INSERT INTO ORDERS VALUES (7,'문새봄','도마세트',26000);\n"
                    "INSERT INTO ORDERS VALUES (8,'구슬아','컵받침',6000);"
                ),
                "output": "",
            },
        ],
        reference_sql="SELECT customer, amount FROM ORDERS WHERE amount >= 20000 ORDER BY amount DESC, id ASC LIMIT 3 OFFSET 3;",
        tier="B1",
        freq=5,
    ),

    # ------------------------------------------------------------------
    # sql-16 : 날짜 문자열 BETWEEN 경계값
    # ------------------------------------------------------------------
    Problem(
        id="sql-16",
        rank="Bronze",
        title="상반기 가입 회원 (날짜 문자열 BETWEEN)",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "2024년 상반기(2024-01-01 ~ 2024-06-30)에 가입한 회원을 조회하려 한다.\n"
            "가입일은 'YYYY-MM-DD' 형식의 문자열로 저장돼 있어\n"
            "문자열 사전순 비교가 곧 날짜 비교가 된다.\n"
            "BETWEEN 은 양 끝을 포함하므로 1월 1일과 6월 30일 가입자도 포함해야 하고,\n"
            "2023-12-31 이나 2024-07-01 가입자는 빠져야 한다.\n\n"
            "MEMBER 테이블:\n"
            "  id INTEGER — 회원 번호\n"
            "  name TEXT — 이름\n"
            "  join_date TEXT — 가입일('YYYY-MM-DD')\n"
        ),
        input_desc="MEMBER(id, name, join_date)",
        output_desc="join_date 가 '2024-01-01' 이상 '2024-06-30' 이하인 회원의 name, join_date 를 join_date 오름차순, 같으면 id 오름차순으로 조회한다.",
        examples=[{
            "input": (
                "MEMBER:\n"
                "id | name | join_date\n"
                "1 | 김수아 | 2023-12-31\n"
                "2 | 이도윤 | 2024-01-01\n"
                "3 | 박예준 | 2024-03-15\n"
                "4 | 최서현 | 2024-06-30\n"
                "5 | 정지훈 | 2024-07-01\n"
                "6 | 한별이 | 2024-05-02"
            ),
            "output": "",
        }],
        hints=[
            "힌트1: 'YYYY-MM-DD' 는 자릿수가 고정된 형식이라 문자열 대소 비교가 날짜 순서와 일치한다. 경계일(1/1, 6/30)이 포함되는지가 채점 포인트다.",
            "힌트2: WHERE join_date BETWEEN '2024-01-01' AND '2024-06-30' — BETWEEN 은 양 끝 포함이다. 상한을 '2024-07-01' 로 쓰면 7월 1일 가입자가 잘못 포함된다.",
            "힌트3: SELECT name, join_date FROM MEMBER WHERE join_date BETWEEN '2024-01-01' AND '2024-06-30' ORDER BY join_date ASC, id ASC;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE MEMBER(id INTEGER, name TEXT, join_date TEXT);\n"
                    "INSERT INTO MEMBER VALUES (1,'김수아','2023-12-31');\n"
                    "INSERT INTO MEMBER VALUES (2,'이도윤','2024-01-01');\n"
                    "INSERT INTO MEMBER VALUES (3,'박예준','2024-03-15');\n"
                    "INSERT INTO MEMBER VALUES (4,'최서현','2024-06-30');\n"
                    "INSERT INTO MEMBER VALUES (5,'정지훈','2024-07-01');\n"
                    "INSERT INTO MEMBER VALUES (6,'한별이','2024-05-02');"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE MEMBER(id INTEGER, name TEXT, join_date TEXT);\n"
                    "INSERT INTO MEMBER VALUES (1,'오세아','2024-02-14');\n"
                    "INSERT INTO MEMBER VALUES (2,'서강준','2023-11-20');\n"
                    "INSERT INTO MEMBER VALUES (3,'남주혁','2024-06-30');\n"
                    "INSERT INTO MEMBER VALUES (4,'유해나','2024-08-09');\n"
                    "INSERT INTO MEMBER VALUES (5,'백도희','2024-01-01');\n"
                    "INSERT INTO MEMBER VALUES (6,'문가영','2024-04-25');\n"
                    "INSERT INTO MEMBER VALUES (7,'홍시아','2025-01-01');"
                ),
                "output": "",
            },
        ],
        reference_sql="SELECT name, join_date FROM MEMBER WHERE join_date BETWEEN '2024-01-01' AND '2024-06-30' ORDER BY join_date ASC, id ASC;",
        tier="B1",
        freq=5,
    ),

    # ------------------------------------------------------------------
    # sql-17 : 종합 (괄호 우선순위 + IS NOT NULL + 정렬 + LIMIT)
    # ------------------------------------------------------------------
    Problem(
        id="sql-17",
        rank="Bronze",
        title="특가전 상위 3종 (조건·NULL·정렬 종합)",
        style="대기업",
        topic="SQL",
        type="sql",
        description=(
            "특가전에 올릴 상품 3종을 고르려 한다. 선정 조건은 다음과 같다.\n"
            "  - 분류가 '전자' 또는 '가전' 이고\n"
            "  - 가격이 50000원 미만이며\n"
            "  - 재고 확인이 끝난 상품(stock 이 NULL 이 아닌 상품)\n"
            "조건을 만족하는 상품 중 가격이 높은 순으로 3개만 뽑는다.\n"
            "OR 묶음에 괄호를 빼먹으면 AND 가 먼저 결합해 다른 결과가 나오고,\n"
            "stock 조건은 = 이 아니라 IS NOT NULL 로 검사해야 한다.\n\n"
            "PRODUCT 테이블:\n"
            "  id INTEGER — 상품 번호\n"
            "  name TEXT — 상품명\n"
            "  category TEXT — 분류\n"
            "  price INTEGER — 가격(원)\n"
            "  stock INTEGER — 재고 수량(미확인이면 NULL)\n"
        ),
        input_desc="PRODUCT(id, name, category, price, stock)",
        output_desc="category 가 '전자' 또는 '가전' 이고 price 가 50000 미만이며 stock 이 NULL 이 아닌 상품을 price 내림차순(같으면 id 오름차순)으로 정렬해 상위 3개의 name, price, stock 을 조회한다.",
        examples=[{
            "input": (
                "PRODUCT:\n"
                "id | name | category | price | stock\n"
                "1 | 무선이어폰 | 전자 | 45000 | 30\n"
                "2 | 세탁기 | 가전 | 690000 | 5\n"
                "3 | 유선마우스 | 전자 | 12000 | NULL\n"
                "4 | 미니선풍기 | 가전 | 19000 | 80\n"
                "5 | 샴푸 | 생활 | 9000 | 200\n"
                "6 | 전기면도기 | 가전 | 48000 | 12\n"
                "7 | 웹캠 | 전자 | 38000 | 25\n"
                "8 | 양말세트 | 패션 | 7000 | 300\n"
                "9 | 휴대폰케이스 | 전자 | 15000 | NULL"
            ),
            "output": "",
        }],
        hints=[
            "힌트1: 조건 세 개를 AND 로 엮되 '(전자 OR 가전)' 은 하나의 덩어리로 괄호에 넣는다. 재고 미확인(NULL)은 stock <> NULL 같은 비교로는 못 거른다.",
            "힌트2: WHERE (category = '전자' OR category = '가전') AND price < 50000 AND stock IS NOT NULL 을 만든 뒤 ORDER BY price DESC 와 LIMIT 3 을 붙인다.",
            "힌트3: SELECT name, price, stock FROM PRODUCT WHERE (category = '전자' OR category = '가전') AND price < 50000 AND stock IS NOT NULL ORDER BY price DESC, id ASC LIMIT 3;",
        ],
        testcases=[
            {
                "input": (
                    "CREATE TABLE PRODUCT(id INTEGER, name TEXT, category TEXT, price INTEGER, stock INTEGER);\n"
                    "INSERT INTO PRODUCT VALUES (1,'무선이어폰','전자',45000,30);\n"
                    "INSERT INTO PRODUCT VALUES (2,'세탁기','가전',690000,5);\n"
                    "INSERT INTO PRODUCT VALUES (3,'유선마우스','전자',12000,NULL);\n"
                    "INSERT INTO PRODUCT VALUES (4,'미니선풍기','가전',19000,80);\n"
                    "INSERT INTO PRODUCT VALUES (5,'샴푸','생활',9000,200);\n"
                    "INSERT INTO PRODUCT VALUES (6,'전기면도기','가전',48000,12);\n"
                    "INSERT INTO PRODUCT VALUES (7,'웹캠','전자',38000,25);\n"
                    "INSERT INTO PRODUCT VALUES (8,'양말세트','패션',7000,300);\n"
                    "INSERT INTO PRODUCT VALUES (9,'휴대폰케이스','전자',15000,NULL);"
                ),
                "output": "",
            },
            {
                "input": (
                    "CREATE TABLE PRODUCT(id INTEGER, name TEXT, category TEXT, price INTEGER, stock INTEGER);\n"
                    "INSERT INTO PRODUCT VALUES (1,'토스터','가전',32000,40);\n"
                    "INSERT INTO PRODUCT VALUES (2,'냉장고','가전',1250000,3);\n"
                    "INSERT INTO PRODUCT VALUES (3,'웹캠프로','전자',49000,NULL);\n"
                    "INSERT INTO PRODUCT VALUES (4,'핸드크림','뷰티',8500,90);\n"
                    "INSERT INTO PRODUCT VALUES (5,'미니가습기','가전',28000,55);\n"
                    "INSERT INTO PRODUCT VALUES (6,'블루투스스피커','전자',44000,18);\n"
                    "INSERT INTO PRODUCT VALUES (7,'수건세트','생활',21000,60);\n"
                    "INSERT INTO PRODUCT VALUES (8,'마우스패드','전자',6000,500);"
                ),
                "output": "",
            },
        ],
        reference_sql=(
            "SELECT name, price, stock FROM PRODUCT "
            "WHERE (category = '전자' OR category = '가전') AND price < 50000 AND stock IS NOT NULL "
            "ORDER BY price DESC, id ASC LIMIT 3;"
        ),
        tier="B1",
        freq=5,
    ),
]
