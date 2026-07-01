"""JavaScript 문법 학습 보강 (기초·중급·고급, 각 5개씩 총 15개).

기존 js_lessons.py(9개)와 주제가 겹치지 않는 새 꼭지들이다.
각 Lesson 의 code 는 Node.js 로 그대로 실행되는 완전한 스크립트이며,
표준입력 없이 고정값으로 시연하고 console.log 로 결과를 출력한다.
"""

from engine.models import Lesson

LESSONS = [

    # ===================== 기초 =====================
    Lesson(
        id="js-basic-04",
        lang="javascript", level="기초",
        title="조건문(if·else·삼항)과 논리연산자",
        summary="if·else if·else · 삼항 · &&·||·??",
        explanation=(
            "[개요]\n"
            "조건문은 프로그램이 상황에 따라 서로 다른 동작을 수행하도록 제어하는 구문이다. if 는 조건이 참일 때, else 는 거짓일 때 실행될 코드를 지정한다.\n"
            "\n"
            "[핵심 개념]\n"
            "• 삼항 연산자는 `조건 ? 참일 때 값 : 거짓일 때 값` 형태로, 한 줄로 값을 선택할 때 사용한다.\n"
            "• || 는 왼쪽 값이 falsy 이면 오른쪽 값을 반환한다.\n"
            "• ?? 는 왼쪽 값이 null 또는 undefined 일 때만 오른쪽 값을 반환한다.\n"
            "• && 는 두 조건이 모두 참일 때만 true 를 반환한다.\n"
            "\n"
            "[코드 분석]\n"
            "• const score = 82;                       → score 변수에 판단 대상 값 82 를 저장한다.\n"
            "• let grade;                              → grade 변수를 선언한다. 초기값은 undefined 이다.\n"
            "• if (score >= 90) grade = 'A';           → score 가 90 이상이면 grade 를 'A' 로 설정한다.\n"
            "• else if (score >= 80) grade = 'B';      → 앞 조건이 거짓이고 80 이상이면 grade 를 'B' 로 설정한다.\n"
            "• else grade = 'C';                       → 앞의 두 조건이 모두 거짓이면 grade 는 'C' 이다.\n"
            "• console.log('학점:', grade);            → score 가 82 이므로 grade 는 'B'. '학점: B' 가 출력된다.\n"
            "• const pass = score >= 60 ? '합격' : '불합격';  → 삼항 연산자로 60 이상이면 '합격', 아니면 '불합격' 을 pass 에 저장한다.\n"
            "• console.log(pass);                      → 82 >= 60 이므로 '합격' 이 출력된다.\n"
            "• const input = 0;                        → input 변수에 0 을 저장한다.\n"
            "• console.log(input || 100);              → 왼쪽 0 이 falsy 이므로 오른쪽 100 을 반환한다. 결과는 100 이다.\n"
            "• console.log(input ?? 100);              → 0 은 null/undefined 가 아니므로 0 을 반환한다. 결과는 0 이다.\n"
            "• console.log(score >= 80 && score < 90); → 82 는 80 이상이며 90 미만이므로 true 를 반환한다.\n"
            "\n"
            "[|| 와 ?? 의 구분]\n"
            "사용자가 나이를 0 으로 입력했을 때 `age || 18` 은 0 을 falsy 로 간주하여 18 로 대체한다. 반면 `age ?? 18` 은 0 을 유효한 값으로 취급하여 0 을 유지하므로 더 안전하다.\n"
            "\n"
            "[유의 사항]\n"
            "• if-else if-else 의 조건은 위에서 아래로 순차 검사하며 첫 일치 지점에서 평가를 멈춘다.\n"
            "• 삼항 연산자는 단순한 선택에만 사용하고, 복잡한 조건은 if-else 가 가독성이 높다."
        ),
        usage="입력 값에 따른 처리 분기, 기본값 지정(a ?? 기본값), 짧은 값 선택(삼항)에 두루 쓴다.",
        cons="중첩 if 가 깊어지면 가독성이 나빠진다. || 는 0/''/false 도 거짓으로 보아 의도와 다를 수 있어 ?? 가 안전하다.",
        code=(
            "const score = 82;\n"
            "let grade;\n"
            "if (score >= 90) grade = 'A';\n"
            "else if (score >= 80) grade = 'B';\n"
            "else grade = 'C';\n"
            "console.log('학점:', grade);            // 학점: B\n"
            "const pass = score >= 60 ? '합격' : '불합격';\n"
            "console.log(pass);                       // 합격\n"
            "const input = 0;\n"
            "console.log(input || 100);               // 100 (0을 거짓으로 봄)\n"
            "console.log(input ?? 100);               // 0  (null/undefined만 대체)\n"
            "console.log(score >= 80 && score < 90);  // true\n"
        ),
    ),

    Lesson(
        id="js-basic-05",
        lang="javascript", level="기초",
        title="반복문(for·while·for...of)",
        summary="for · while · for...of · break·continue",
        explanation=(
            "[개요]\n"
            "반복문은 동일하거나 유사한 작업을 여러 번 실행하도록 제어하는 구문이다. 예를 들어 1 부터 100 까지의 합산을 사람이 직접 계산하지 않고 반복문으로 처리한다.\n"
            "\n"
            "[핵심 개념]\n"
            "• for 문: 반복 횟수가 정해진 경우에 사용한다.\n"
            "• while 문: 조건이 참인 동안 반복하며, 종료 시점을 조건으로 정한다.\n"
            "• for...of 문: 배열 등 이터러블의 각 항목을 순서대로 처리할 때 사용한다.\n"
            "• break 는 반복문 전체를 즉시 종료하고, continue 는 현재 회차만 건너뛴다.\n"
            "\n"
            "[코드 분석]\n"
            "• let sum = 0;                        → 합계를 저장할 변수를 0 으로 초기화한다.\n"
            "• for (let i = 1; i <= 5; i++)        → i 를 1 부터 시작해 5 이하인 동안 매 반복마다 1 씩 증가시킨다.\n"
            "• sum += i;                           → sum 에 i 를 누적한다. 1+2+3+4+5 = 15 이다.\n"
            "• console.log('1~5 합:', sum);        → 결과 15 를 출력한다.\n"
            "• let n = 8, cnt = 0;                 → n 은 8, 반감 횟수 cnt 는 0 으로 초기화한다.\n"
            "• while (n > 1) {                     → n 이 1 보다 크면 반복한다.\n"
            "• n = Math.floor(n / 2);              → n 을 절반으로 나누고 소수점을 버린다. 8→4→2→1 순으로 변한다.\n"
            "• cnt++;                              → 반복 횟수를 1 증가시킨다.\n"
            "• console.log('반감 횟수:', cnt);     → 3 회 반감했으므로 3 을 출력한다.\n"
            "• for (const ch of 'abc')             → 문자열 'abc' 에서 문자를 순서대로 꺼낸다. ch 는 'a', 'b', 'c' 순이다.\n"
            "• process.stdout.write(ch + ' ');     → 줄바꿈 없이 한 줄에 이어서 출력한다.\n"
            "• for (let i = 0; i < 5; i++) {       → 0 부터 4 까지 반복한다.\n"
            "• if (i === 3) break;                 → i 가 3 이면 반복문 전체를 즉시 종료한다.\n"
            "• if (i % 2 === 0) continue;          → i 가 짝수이면 현재 회차를 건너뛰고 다음 반복으로 이동한다.\n"
            "• console.log('홀수 i:', i);          → 홀수 i=1 만 출력되고 i=3 에서 break 된다.\n"
            "\n"
            "[break·continue 의 용도]\n"
            "• break: 더 이상 반복이 불필요할 때 조기에 종료하여 실행 시간을 절약한다.\n"
            "• continue: 특정 조건의 항목을 제외하고 나머지만 처리할 때 사용한다.\n"
            "\n"
            "[유의 사항]\n"
            "while 문에서 조건이 결코 false 가 되지 않으면 무한 루프에 빠진다. `while (true) { }` 형태를 사용할 때는 반드시 탈출 조건을 포함해야 한다."
        ),
        usage="누적 합·카운팅 같은 반복 처리의 기본. 인덱스가 필요하면 for, 값만 필요하면 for...of 가 읽기 쉽다.",
        cons="for...of 는 인덱스를 직접 주지 않는다(필요하면 entries() 사용). 무한 while 은 종료 조건을 빠뜨리기 쉽다.",
        code=(
            "let sum = 0;\n"
            "for (let i = 1; i <= 5; i++) sum += i;\n"
            "console.log('1~5 합:', sum);            // 1~5 합: 15\n"
            "let n = 8, cnt = 0;\n"
            "while (n > 1) { n = Math.floor(n / 2); cnt++; }\n"
            "console.log('반감 횟수:', cnt);          // 반감 횟수: 3\n"
            "for (const ch of 'abc') process.stdout.write(ch + ' ');\n"
            "console.log();                           // a b c\n"
            "for (let i = 0; i < 5; i++) {\n"
            "  if (i === 3) break;                    // 3에서 멈춤\n"
            "  if (i % 2 === 0) continue;             // 짝수 건너뜀\n"
            "  console.log('홀수 i:', i);             // 1\n"
            "}\n"
        ),
    ),

    Lesson(
        id="js-basic-06",
        lang="javascript", level="기초",
        title="switch 문",
        summary="switch · case · break · default",
        explanation=(
            "[개요]\n"
            "switch 문은 하나의 값이 여러 후보(case) 중 어디에 해당하는지 구분하는 분기 구문이다. 여러 개의 if-else if 사슬을 각 case 로 정돈하여 표현할 수 있다.\n"
            "\n"
            "[핵심 개념]\n"
            "• 각 case 실행 후 break 를 명시해야 한다. break 를 생략하면 아래 case 로 계속 실행되며, 이를 fall-through 라고 한다.\n"
            "• fall-through 는 여러 case 를 동일한 동작으로 묶을 때 의도적으로 활용할 수 있다.\n"
            "• switch 는 === (완전 일치) 비교를 사용하므로 '80'(문자열)과 80(숫자)은 다른 값으로 취급한다.\n"
            "\n"
            "[코드 분석]\n"
            "• function dayName(d) {         → 요일 번호를 받아 이름을 반환하는 함수를 정의한다.\n"
            "• switch (d) {                  → d 의 값을 각 case 와 비교한다.\n"
            "• case 0: return '일';          → d 가 0 이면 '일' 을 반환한다. === 비교를 사용한다.\n"
            "• case 6: return '토';          → d 가 6 이면 '토' 를 반환한다.\n"
            "• default: return '평일';       → 어느 case 에도 일치하지 않으면 기본값 '평일' 을 반환한다.\n"
            "• console.log(dayName(0), dayName(3), dayName(6));  → 0 은 '일', 3 은 default 인 '평일', 6 은 '토' 를 반환한다.\n"
            "• const fruit = 'apple';        → fruit 변수에 문자열 'apple' 을 저장한다.\n"
            "• switch (fruit) {              → fruit 의 값을 case 들과 비교한다.\n"
            "• case 'apple':                 → fruit 가 'apple' 이면 여기로 진입하며, break 가 없어 아래 case 로 이어진다.\n"
            "• case 'pear':                  → fruit 가 'pear' 여도 동일한 동작을 수행한다(fall-through 활용).\n"
            "• console.log('포미과 과일');   → apple 또는 pear 이면 이 줄이 실행된다.\n"
            "• break;                        → 여기서 종료하며 default 로 진행하지 않는다.\n"
            "• default: console.log('기타'); → apple 도 pear 도 아니면 '기타' 를 출력한다.\n"
            "\n"
            "[switch 사용의 이점]\n"
            "동일 변수를 여러 값과 비교하는 긴 if-else if 사슬을 case 단위로 정돈하여 가독성을 높인다.\n"
            "\n"
            "[유의 사항]\n"
            "• break 누락은 다음 case 까지 실행되는 흔한 버그의 원인이다.\n"
            "• switch 는 완전 일치 비교를 사용하므로 점수 80~89 같은 범위 비교에는 부적합하며, 이 경우 if-else 가 적절하다."
        ),
        usage="하나의 값이 여러 고정 후보 중 하나일 때(요일·메뉴·상태 코드) if-else 사슬보다 깔끔하다.",
        cons="break 누락은 흔한 버그다. 범위 비교(예: 점수 80~89)에는 부적합해 if-else 가 낫다.",
        code=(
            "function dayName(d) {\n"
            "  switch (d) {\n"
            "    case 0: return '일';\n"
            "    case 6: return '토';\n"
            "    default: return '평일';\n"
            "  }\n"
            "}\n"
            "console.log(dayName(0), dayName(3), dayName(6)); // 일 평일 토\n"
            "const fruit = 'apple';\n"
            "switch (fruit) {\n"
            "  case 'apple':\n"
            "  case 'pear':\n"
            "    console.log('포미과 과일');           // fall-through로 묶음\n"
            "    break;\n"
            "  default:\n"
            "    console.log('기타');\n"
            "}\n"
        ),
    ),

    Lesson(
        id="js-basic-07",
        lang="javascript", level="기초",
        title="템플릿 리터럴",
        summary="백틱 · ${} 표현식 · 여러 줄 문자열",
        explanation=(
            "[개요]\n"
            "템플릿 리터럴은 변수와 표현식을 문자열 안에 직접 삽입하는 문자열 표기법이다. 기존 `+` 연결 방식(\"안녕하세요, \" + name + \"님!\")을 `` `안녕하세요, ${name}님!` `` 형태로 간결하게 대체한다.\n"
            "\n"
            "[핵심 개념]\n"
            "• 백틱(`)으로 문자열을 감싼다. 작은따옴표(')나 큰따옴표(\")와 구분해야 한다.\n"
            "• ${} 안에는 변수뿐 아니라 계산식과 함수 호출도 넣을 수 있다.\n"
            "• 줄바꿈을 그대로 포함할 수 있어 여러 줄 문자열 작성이 용이하다.\n"
            "\n"
            "[코드 분석]\n"
            "• const name = '홍길동', age = 20;   → 이름과 나이 변수를 선언한다.\n"
            "• console.log(`${name}님은 ${age}살, 내년엔 ${age + 1}살`);  → 백틱으로 감싸고 ${} 안에 변수와 계산식을 넣는다. ${age + 1} 은 21 로 계산되어 삽입된다.\n"
            "• const items = ['사과', '바나나'];  → 과일 이름 배열을 선언한다.\n"
            "• const msg = `장바구니(${items.length}개):\\n- ${items.join('\\n- ')}`;  → items.length 는 2, items.join('\\n- ') 은 '사과\\n- 바나나' 이며, 결과는 여러 줄 문자열이다.\n"
            "• console.log(msg);  → 장바구니 목록이 여러 줄로 출력된다.\n"
            "• const t = 75;  → 온도 또는 점수 변수 t 에 75 를 저장한다.\n"
            "• console.log(`상태: ${t >= 70 ? '높음' : '낮음'}`);  → ${} 안에 삼항 연산자를 사용한다. t 가 70 이상이므로 '높음' 이 삽입된다.\n"
            "\n"
            "[템플릿 리터럴 사용의 이점]\n"
            "• + 연결 방식: '이름: ' + name + ', 나이: ' + age + '살'\n"
            "• 템플릿 리터럴: `이름: ${name}, 나이: ${age}살`\n"
            "변수가 많을수록 가독성 차이가 커진다.\n"
            "\n"
            "[유의 사항]\n"
            "• 반드시 백틱(`)을 사용해야 한다. 작은따옴표나 큰따옴표로는 동작하지 않는다.\n"
            "• ${} 안에 복잡한 계산을 다수 포함하면 가독성이 저하되므로, 긴 계산은 사전에 변수로 분리한다."
        ),
        usage="로그 메시지·HTML·SQL 조립 등 변수 섞인 문자열을 + 연결 없이 읽기 쉽게 만든다.",
        cons="${} 안에 복잡한 로직을 넣으면 가독성이 떨어진다. 외부 입력을 그대로 끼우면 인젝션 위험이 있다.",
        code=(
            "const name = '홍길동', age = 20;\n"
            "console.log(`${name}님은 ${age}살, 내년엔 ${age + 1}살`);\n"
            "const items = ['사과', '바나나'];\n"
            "const msg = `장바구니(${items.length}개):\n"
            "- ${items.join('\\n- ')}`;\n"
            "console.log(msg);\n"
            "const t = 75;\n"
            "console.log(`상태: ${t >= 70 ? '높음' : '낮음'}`); // 상태: 높음\n"
        ),
    ),

    Lesson(
        id="js-basic-08",
        lang="javascript", level="기초",
        title="형변환과 truthy/falsy",
        summary="Number·String·Boolean · falsy 값 · !!",
        explanation=(
            "[개요]\n"
            "형변환(Type Conversion)은 값의 타입을 다른 타입으로 바꾸는 작업이다. 예를 들어 사용자 입력은 항상 문자열('25')로 들어오므로, 계산을 위해서는 숫자(25)로 변환해야 한다.\n"
            "\n"
            "[핵심 개념]\n"
            "• truthy/falsy 는 조건문에서 값을 참/거짓으로 해석하는 규칙이다.\n"
            "• JavaScript 에서 falsy 로 간주되는 값은 6 가지이다: false, 0, '' (빈 문자열), null, undefined, NaN.\n"
            "• 위 6 가지를 제외한 모든 값은 truthy 이며, '0'(문자열 영)도 truthy 이다.\n"
            "\n"
            "[코드 분석]\n"
            "• console.log(Number('42'), parseInt('12px', 10));  → '42' 를 숫자 42 로 변환하고, '12px' 에서 앞의 숫자 12 만 추출한다. parseInt 의 두 번째 인자 10 은 10 진수 기준이다.\n"
            "• console.log(Number(''), Number('abc'));           → 빈 문자열은 0 으로, 숫자가 아닌 문자열은 NaN(Not a Number)으로 변환된다.\n"
            "• console.log(String(123) + '!', Boolean(0));       → 123 을 문자열 '123' 으로 변환해 '!' 를 붙이고, Boolean(0) 은 0 이 falsy 이므로 false 이다.\n"
            "• const falsy = [false, 0, '', null, undefined, NaN];  → 6 가지 falsy 값을 배열로 구성한다.\n"
            "• console.log(falsy.map(v => Boolean(v)));          → 각 값을 Boolean 으로 변환하며 모두 false 를 반환한다.\n"
            "• console.log(!!'0', !!0);                          → '0' 은 문자열이므로 truthy 이고 !!'0' 은 true, 0 은 falsy 이므로 !!0 은 false 이다.\n"
            "• const userInput = '';                             → 사용자가 아무것도 입력하지 않은 상태를 빈 문자열로 표현한다.\n"
            "• console.log(userInput ? '입력됨' : '비어있음');   → 빈 문자열은 falsy 이므로 '비어있음' 이 출력된다.\n"
            "\n"
            "[!! 연산자의 용도]\n"
            "• !x 는 값을 반전한 boolean 을 반환한다.\n"
            "• !!x 는 두 번 반전하여 원래의 truthy/falsy 를 명시적 boolean 으로 변환한다.\n"
            "• 예: !!0 → !true → false, !!'hello' → !false → true.\n"
            "\n"
            "[유의 사항]\n"
            "• '0'(문자열 영)은 truthy 이므로 숫자 0 과 혼동하지 않아야 한다.\n"
            "• 사용자 입력에 || 로 기본값을 지정할 때 0 이 유효한 값이라면 ?? 를 사용해야 한다."
        ),
        usage="입력 문자열을 숫자로 바꾸기(Number), 값 존재 여부 확인(if (x)), 기본값 처리 판단에 핵심.",
        cons="Number('') 은 0, Number('12px') 은 NaN 처럼 결과가 헷갈린다. '0'(문자열)은 truthy 라 숫자 0과 다르게 동작한다.",
        code=(
            "console.log(Number('42'), parseInt('12px', 10)); // 42 12\n"
            "console.log(Number(''), Number('abc'));          // 0 NaN\n"
            "console.log(String(123) + '!', Boolean(0));      // '123!' false\n"
            "const falsy = [false, 0, '', null, undefined, NaN];\n"
            "console.log(falsy.map(v => Boolean(v)));         // 모두 false\n"
            "console.log(!!'0', !!0);                         // true false\n"
            "const userInput = '';\n"
            "console.log(userInput ? '입력됨' : '비어있음');   // 비어있음\n"
        ),
    ),

    # ===================== 중급 =====================
    Lesson(
        id="js-mid-04",
        lang="javascript", level="중급",
        title="객체 메서드와 this",
        summary="메서드 단축 · this · 화살표 차이",
        explanation=(
            "[개요]\n"
            "객체 안에 정의된 함수를 메서드라고 한다. 메서드 안에서 같은 객체의 다른 속성에 접근하려면 this 를 사용한다. this 는 메서드를 호출한 객체를 가리키는 키워드이다.\n"
            "\n"
            "[핵심 개념]\n"
            "• this 는 호출 대상 객체를 참조한다. 동일한 메서드라도 어떤 객체가 호출했는지에 따라 this 가 달라진다.\n"
            "• 일반 함수(function): this 는 호출한 객체를 가리킨다.\n"
            "• 화살표 함수(=>): 자신만의 this 를 갖지 않으며, 함수가 정의된 위치의 this 를 그대로 사용한다.\n"
            "\n"
            "[코드 분석]\n"
            "• const counter = {          → counter 객체를 선언한다.\n"
            "• count: 0,                  → count 속성을 0 으로 초기화한다.\n"
            "• inc() {                    → inc 메서드이다. { inc: function() { ... } } 의 단축 문법이다.\n"
            "• this.count++;              → 호출한 객체(counter)의 count 를 1 증가시킨다.\n"
            "• return this.count;         → 증가된 count 값을 반환한다.\n"
            "• label: 'C',                → label 속성에 'C' 를 저장한다.\n"
            "• show() {                   → show 메서드이다.\n"
            "• return `${this.label}=${this.count}`;  → 이 객체의 label 과 count 를 결합해 문자열로 반환한다.\n"
            "• console.log(counter.inc(), counter.inc());  → inc() 를 두 번 호출하여 1, 2 를 반환한다. count 는 0→1→2 로 변한다.\n"
            "• console.log(counter.show());  → label 이 'C', count 가 2 이므로 'C=2' 를 출력한다.\n"
            "• const obj = { vals: [1, 2, 3], factor: 10, ... }  → 값 배열과 배율을 가진 객체이다.\n"
            "• scaled() {                 → scaled 메서드이다.\n"
            "• return this.vals.map(v => v * this.factor);  → 배열의 각 값에 factor 를 곱한다. 콜백이 화살표 함수이므로 this 는 바깥 obj 를 가리킨다.\n"
            "• console.log(obj.scaled());  → [10, 20, 30] 을 출력한다.\n"
            "\n"
            "[화살표 함수를 map 콜백으로 쓰는 이유]\n"
            "map 의 콜백을 일반 함수로 작성하면 this 가 obj 가 아닌 undefined 가 된다. 화살표 함수는 바깥 this(=obj)를 그대로 사용하므로 this.factor 가 정상적으로 10 을 참조한다.\n"
            "\n"
            "[유의 사항]\n"
            "메서드를 변수에 담아 분리 호출하면(const greet = counter.show; greet();) this 가 counter 를 가리키지 못한다(undefined). 메서드는 항상 객체를 통해 호출해야 한다."
        ),
        usage="데이터와 그 데이터를 다루는 동작을 한 객체로 묶을 때. 콜백에서 this 가 풀리면 화살표로 바깥 this 를 유지한다.",
        cons="일반 함수의 this 는 호출 방식에 따라 바뀌어 헷갈린다(분리 호출 시 undefined). 객체 메서드를 화살표로 쓰면 this 가 객체를 가리키지 않는다.",
        code=(
            "const counter = {\n"
            "  count: 0,\n"
            "  inc() { this.count++; return this.count; },  // 메서드, this=counter\n"
            "  label: 'C',\n"
            "  show() { return `${this.label}=${this.count}`; },\n"
            "};\n"
            "console.log(counter.inc(), counter.inc()); // 1 2\n"
            "console.log(counter.show());               // C=2\n"
            "const obj = {\n"
            "  vals: [1, 2, 3], factor: 10,\n"
            "  scaled() { return this.vals.map(v => v * this.factor); }, // 화살표가 바깥 this 사용\n"
            "};\n"
            "console.log(obj.scaled());                 // [10,20,30]\n"
        ),
    ),

    Lesson(
        id="js-mid-05",
        lang="javascript", level="중급",
        title="예외 처리(try·catch·throw)",
        summary="try·catch·finally · throw · Error",
        explanation=(
            "[개요]\n"
            "예외 처리는 실행 중 예상치 못한 오류가 발생했을 때 프로그램이 중단되지 않도록 오류를 포착하여 처리하는 메커니즘이다.\n"
            "\n"
            "[핵심 개념]\n"
            "• try: 오류가 발생할 수 있는 코드를 감싼다.\n"
            "• catch: try 블록에서 오류가 발생하면 실행되며, 오류 객체를 인자로 받는다.\n"
            "• finally: 오류 발생 여부와 무관하게 항상 실행된다.\n"
            "• throw: 오류를 직접 생성하여 던진다. 예를 들어 0 으로 나누는 입력이 들어왔을 때 명시적으로 오류를 발생시킬 수 있다.\n"
            "\n"
            "[코드 분석]\n"
            "• function divide(a, b) {              → 나눗셈 함수를 정의한다.\n"
            "• if (b === 0)                         → 나누는 수가 0 이면\n"
            "• throw new Error('0으로 나눌 수 없음');  → 오류를 생성해 던진다. 이 시점에 함수 실행이 중단된다.\n"
            "• return a / b;                        → b 가 0 이 아니면 정상 계산 결과를 반환한다.\n"
            "• try {                                → 오류가 발생할 수 있는 코드를 이 블록에 작성한다.\n"
            "• console.log(divide(10, 2));          → 10 ÷ 2 = 5 를 정상 출력한다.\n"
            "• console.log(divide(10, 0));          → b=0 이므로 throw 가 실행되어 오류가 던져진다.\n"
            "• } catch (e) {                        → try 블록에서 오류가 발생하면 진입하며, e 에 오류 객체가 담긴다.\n"
            "• console.log('에러:', e.message);     → 오류 메시지 '0으로 나눌 수 없음' 을 출력한다.\n"
            "• } finally {                          → 오류 발생 여부와 관계없이 실행된다.\n"
            "• console.log('계산 종료');            → '계산 종료' 가 항상 출력된다.\n"
            "• try { JSON.parse('{bad}'); }         → 잘못된 JSON 문자열을 파싱하여 오류를 발생시킨다.\n"
            "• catch (e) { console.log('파싱 실패:', e.name); }  → SyntaxError 가 포착된다.\n"
            "\n"
            "[예외 처리의 필요성]\n"
            "오류 처리가 없으면 오류 발생 시점에 프로그램이 완전히 중단된다. try-catch 를 사용하면 오류를 catch 에서 처리하고 이후 코드를 계속 실행할 수 있다.\n"
            "\n"
            "[유의 사항]\n"
            "catch 블록을 비워 두면 오류가 무시되어 이후 디버깅이 어려워진다. 최소한 console.error 로 오류 내용을 기록해야 한다."
        ),
        usage="JSON 파싱·형 검증·외부 입력 처리처럼 실패 가능성이 있는 곳을 감싸 프로그램이 죽지 않게 한다.",
        cons="try/catch 남용은 흐름을 숨겨 디버깅을 어렵게 한다. catch 에서 오류를 무시하면(빈 블록) 버그를 놓친다.",
        code=(
            "function divide(a, b) {\n"
            "  if (b === 0) throw new Error('0으로 나눌 수 없음');\n"
            "  return a / b;\n"
            "}\n"
            "try {\n"
            "  console.log(divide(10, 2));      // 5\n"
            "  console.log(divide(10, 0));      // 예외 발생\n"
            "} catch (e) {\n"
            "  console.log('에러:', e.message); // 에러: 0으로 나눌 수 없음\n"
            "} finally {\n"
            "  console.log('계산 종료');         // 항상 실행\n"
            "}\n"
            "try { JSON.parse('{bad}'); }\n"
            "catch (e) { console.log('파싱 실패:', e.name); } // 파싱 실패: SyntaxError\n"
        ),
    ),

    Lesson(
        id="js-mid-06",
        lang="javascript", level="중급",
        title="JSON 다루기",
        summary="JSON.stringify · JSON.parse · 들여쓰기",
        explanation=(
            "[개요]\n"
            "JSON(JavaScript Object Notation)은 데이터를 주고받을 때 사용하는 표준 문자열 형식이다. 웹에서 서버와 클라이언트 간 데이터 교환에 널리 사용된다.\n"
            "\n"
            "[핵심 개념]\n"
            "• JSON.stringify: 객체를 JSON 문자열로 변환한다(직렬화).\n"
            "• JSON.parse: JSON 문자열을 객체로 복원한다(역직렬화).\n"
            "• 객체는 직접 전송할 수 없으므로 문자열로 변환해야 네트워크로 전달할 수 있다. JSON 은 Python, Java, C++ 등 대부분의 언어에서 해석 가능한 범용 형식이다.\n"
            "\n"
            "[코드 분석]\n"
            "• const user = { name: '김철수', age: 20, tags: ['a', 'b'] };  → JavaScript 객체를 선언한다.\n"
            "• const json = JSON.stringify(user);  → 객체를 JSON 문자열 {\"name\":\"김철수\",\"age\":20,\"tags\":[\"a\",\"b\"]} 로 변환한다.\n"
            "• console.log(json);                  → JSON 문자열을 출력한다.\n"
            "• console.log(JSON.stringify(user, null, 2));  → 세 번째 인자 2 는 들여쓰기 칸 수이며, 정렬된 형태로 출력한다.\n"
            "• const back = JSON.parse(json);      → JSON 문자열을 JavaScript 객체로 복원한다.\n"
            "• console.log(back.name, back.tags[1]);  → 복원된 객체에서 속성을 꺼내 '김철수' 와 'b' 를 출력한다.\n"
            "• const skip = { id: 1, fn: () => 1, u: undefined };  → 함수와 undefined 를 포함한 객체이다.\n"
            "• console.log(JSON.stringify(skip));  → JSON 은 함수와 undefined 를 지원하지 않으므로 {\"id\":1} 만 남는다.\n"
            "\n"
            "[JSON 형식 규칙]\n"
            "• 키(속성 이름)는 반드시 큰따옴표로 감싼다: {\"name\": \"값\"}.\n"
            "• 문자열 값도 큰따옴표로 감싼다: {\"city\": \"서울\"}.\n"
            "• 숫자는 따옴표 없이 표기한다: {\"age\": 20}.\n"
            "• null, true, false 는 사용 가능하나 undefined, 함수, 심볼은 사용할 수 없다.\n"
            "\n"
            "[유의 사항]\n"
            "• JSON.parse 는 형식이 잘못되면 SyntaxError 를 던지므로, 외부에서 받은 JSON 은 try-catch 로 감싸야 한다.\n"
            "• 순환 참조(obj.self = obj)가 있는 객체는 stringify 가 오류를 던진다."
        ),
        usage="API 요청/응답, 설정 파일, localStorage 저장 등 데이터를 문자열로 주고받을 때 표준 형식이다.",
        cons="순환 참조 객체는 stringify 가 실패한다. parse 는 잘못된 JSON 에서 예외를 던지므로 try/catch 가 필요하다.",
        code=(
            "const user = { name: '김철수', age: 20, tags: ['a', 'b'] };\n"
            "const json = JSON.stringify(user);\n"
            "console.log(json);                       // {\"name\":\"김철수\",...}\n"
            "console.log(JSON.stringify(user, null, 2)); // 들여쓰기 출력\n"
            "const back = JSON.parse(json);\n"
            "console.log(back.name, back.tags[1]);    // 김철수 b\n"
            "const skip = { id: 1, fn: () => 1, u: undefined };\n"
            "console.log(JSON.stringify(skip));       // {\"id\":1} (함수·undefined 제외)\n"
        ),
    ),

    Lesson(
        id="js-mid-07",
        lang="javascript", level="중급",
        title="날짜와 타이머(Date·setTimeout)",
        summary="Date · 날짜 연산 · setTimeout",
        explanation=(
            "[개요]\n"
            "Date 객체는 날짜와 시간을 다루는 도구로, 현재 날짜 조회나 두 날짜 간 경과 일수 계산 등에 사용한다. setTimeout 은 지정한 밀리초 후에 특정 작업을 실행하도록 예약하는 함수이다.\n"
            "\n"
            "[핵심 개념]\n"
            "• setTimeout 은 비동기로 동작한다. 타이머 대기 중에도 다른 코드가 계속 실행된다.\n"
            "• Date 의 월은 0 부터 시작한다(0=1월, 11=12월).\n"
            "• getTime() 은 1970년 1월 1일 자정을 기준으로 한 밀리초 값을 반환한다.\n"
            "\n"
            "[코드 분석]\n"
            "• const start = new Date(2024, 0, 1);  → 2024년 1월 1일 날짜 객체를 생성한다. 월은 0 부터 시작하므로 0 이 1월이다.\n"
            "• const end = new Date(2024, 0, 11);   → 2024년 1월 11일 날짜 객체를 생성한다.\n"
            "• const days = (end.getTime() - start.getTime()) / (1000 * 60 * 60 * 24);\n"
            "  → 두 날짜의 밀리초 차이를 구한 뒤 1초=1000ms, 1분=60초, 1시간=60분, 1일=24시간으로 나누어 일수를 산출한다.\n"
            "• console.log('경과 일수:', days);     → 1월 1일부터 11일까지 10 일이 출력된다.\n"
            "• console.log(start.getFullYear(), start.getMonth() + 1);  → getFullYear() 는 연도(2024)를, getMonth() 는 0 을 반환하므로 +1 하여 1월을 표시한다.\n"
            "• setTimeout(() => { ... }, 0);        → 화살표 함수를 0 밀리초 후에 실행하도록 예약한다.\n"
            "• console.log('1초 후처럼 동작(데모는 0ms)');  → 예약된 콜백에서 나중에 실행되는 출력이다.\n"
            "• console.log('타이머 등록 완료(먼저 출력)');  → setTimeout 콜백보다 이 줄이 먼저 출력된다.\n"
            "\n"
            "[getMonth() 가 0 부터 시작하는 이유]\n"
            "역사적 설계에 기인하며, 사람이 읽는 월 번호를 얻으려면 항상 getMonth() + 1 로 표기해야 한다.\n"
            "\n"
            "[유의 사항]\n"
            "setTimeout 은 비동기이므로 이후의 동기 코드가 먼저 실행되고, 타이머가 만료되면 콜백이 실행된다. 지연을 0ms 로 지정해도 현재 코드가 모두 끝난 뒤에 실행된다."
        ),
        usage="기간 계산(D-day), 지연 실행, 디바운스/스로틀 등 시간 관련 처리에 쓴다.",
        cons="setTimeout 의 지연은 정확히 보장되지 않는다(최소 지연). Date 의 월 0-기반은 실수의 단골이다.",
        code=(
            "const start = new Date(2024, 0, 1);   // 2024-01-01 (월 0=1월)\n"
            "const end = new Date(2024, 0, 11);\n"
            "const days = (end.getTime() - start.getTime()) / (1000 * 60 * 60 * 24);\n"
            "console.log('경과 일수:', days);       // 경과 일수: 10\n"
            "console.log(start.getFullYear(), start.getMonth() + 1); // 2024 1\n"
            "setTimeout(() => {\n"
            "  console.log('1초 후처럼 동작(데모는 0ms)');\n"
            "}, 0);\n"
            "console.log('타이머 등록 완료(먼저 출력)');\n"
        ),
    ),

    Lesson(
        id="js-mid-08",
        lang="javascript", level="중급",
        title="배열 검색(find·includes·some·every)",
        summary="find · findIndex · includes · some · every",
        explanation=(
            "[개요]\n"
            "배열 검색 메서드는 배열에서 특정 항목을 찾거나 조건 충족 여부를 확인하는 함수들이다. for 문으로 직접 순회하지 않아도 되어 코드가 간결해진다.\n"
            "\n"
            "[핵심 개념]\n"
            "• find: 조건에 맞는 첫 번째 항목 자체를 반환한다(없으면 undefined).\n"
            "• findIndex: 조건에 맞는 첫 번째 항목의 인덱스를 반환한다.\n"
            "• includes: 특정 값의 존재 여부를 true/false 로 반환한다.\n"
            "• some: 조건을 만족하는 항목이 하나라도 있으면 true 를 반환한다.\n"
            "• every: 모든 항목이 조건을 만족해야 true 를 반환한다.\n"
            "\n"
            "[코드 분석]\n"
            "• const nums = [4, 9, 12, 7, 20];       → 숫자 배열을 선언한다.\n"
            "• console.log(nums.find(n => n > 10));  → 10 보다 큰 첫 번째 값을 찾는다. 4, 9 는 조건 불일치, 12 에서 일치하므로 12 를 반환한다.\n"
            "• console.log(nums.findIndex(n => n > 10));  → 10 보다 큰 첫 번째 값의 인덱스를 반환한다. 12 는 인덱스 2 이므로 2 를 반환한다.\n"
            "• console.log(nums.includes(7), nums.includes(3));  → 7 은 존재하므로 true, 3 은 없으므로 false 를 반환한다.\n"
            "• console.log(nums.some(n => n % 2 === 0));  → 짝수가 하나라도 있는지 검사한다. 4 가 짝수이므로 true 를 반환한다.\n"
            "• console.log(nums.every(n => n > 0));  → 모든 항목이 0 보다 큰지 검사한다. 전부 양수이므로 true 를 반환한다.\n"
            "• const users = [{id:1,name:'A'},{id:2,name:'B'}];  → 객체 배열을 선언한다.\n"
            "• console.log(users.find(u => u.id === 2).name);  → id 가 2 인 객체를 찾아 그 name 을 꺼낸다. 'B' 를 출력한다.\n"
            "\n"
            "[find 와 filter 의 차이]\n"
            "• find: 처음 일치하는 항목 하나만 반환한다(없으면 undefined).\n"
            "• filter: 조건에 맞는 모든 항목을 새 배열로 반환한다(없으면 빈 배열).\n"
            "\n"
            "[유의 사항]\n"
            "• 빈 배열에서 some 은 false, every 는 true 를 반환한다. 이는 '공집합에 대한 전칭 명제는 참'이라는 논리에 따른 것이다.\n"
            "• find 가 아무것도 찾지 못하면 undefined 를 반환하므로, 반환값에 바로 .name 처럼 접근하면 오류가 발생한다. 존재 여부를 확인한 후 사용해야 한다."
        ),
        usage="조건에 맞는 항목 찾기, 존재 여부 검사, 유효성 검증(전부/일부 만족) 등에 반복문 없이 쓴다.",
        cons="find 는 첫 일치만 반환한다(여러 개는 filter). some/every 는 빈 배열에서 각각 false/true 라 경계 처리에 주의한다.",
        code=(
            "const nums = [4, 9, 12, 7, 20];\n"
            "console.log(nums.find(n => n > 10));      // 12\n"
            "console.log(nums.findIndex(n => n > 10)); // 2\n"
            "console.log(nums.includes(7), nums.includes(3)); // true false\n"
            "console.log(nums.some(n => n % 2 === 0)); // true (짝수 존재)\n"
            "console.log(nums.every(n => n > 0));      // true (모두 양수)\n"
            "const users = [{id:1,name:'A'},{id:2,name:'B'}];\n"
            "console.log(users.find(u => u.id === 2).name); // B\n"
        ),
    ),

    # ===================== 고급 =====================
    Lesson(
        id="js-adv-04",
        lang="javascript", level="고급",
        title="클래스와 상속(prototype)",
        summary="class · constructor · extends · super",
        explanation=(
            "[개요]\n"
            "클래스는 동일한 구조의 객체를 다수 생성하기 위한 설계도이다. 상속(extends)은 기존 클래스를 기반으로 더 특화된 클래스를 정의하는 기법으로, 공통 부분은 부모 클래스에, 특화 부분은 자식 클래스에 나누어 관리한다.\n"
            "\n"
            "[핵심 개념]\n"
            "• constructor: new 키워드로 객체를 생성할 때 자동 실행되는 초기화 함수이다.\n"
            "• extends: 부모 클래스의 속성과 메서드를 물려받는다.\n"
            "• super: 부모 클래스의 constructor 또는 메서드를 호출한다.\n"
            "• 자식 클래스에서 부모의 메서드를 재정의하는 것을 오버라이드라고 한다.\n"
            "\n"
            "[코드 분석]\n"
            "• class Animal {                        → Animal 클래스를 정의한다.\n"
            "• constructor(name) {                   → new Animal('개') 처럼 객체를 생성할 때 자동 실행된다.\n"
            "• this.name = name;                     → 전달받은 name 값을 이 객체의 name 속성에 저장한다.\n"
            "• speak() {                             → speak 메서드를 정의한다. 모든 Animal 객체가 공유한다.\n"
            "• return `${this.name}가 소리낸다`;     → 이 객체의 name 을 사용해 문자열을 생성한다.\n"
            "• class Dog extends Animal {            → Dog 클래스가 Animal 을 상속하여 모든 속성과 메서드를 물려받는다.\n"
            "• speak() {                             → 부모의 speak() 를 오버라이드한다.\n"
            "• return `${this.name}: 멍멍`;          → Dog 에 특화된 동작이다.\n"
            "• intro() {                             → 새로운 메서드를 추가한다.\n"
            "• return super.speak();                 → super 로 부모 클래스(Animal)의 speak() 를 호출한다.\n"
            "• const d = new Dog('바둑이');          → Dog 클래스로 '바둑이' 객체를 생성하며 Animal 의 constructor 가 실행된다.\n"
            "• console.log(d.speak());               → Dog 의 speak() 가 실행되어 '바둑이: 멍멍' 을 출력한다.\n"
            "• console.log(d.intro());               → Animal 의 speak() 가 호출되어 '바둑이가 소리낸다' 를 출력한다.\n"
            "• console.log(d instanceof Animal);     → d 가 Animal 의 인스턴스인지 확인한다. 상속받았으므로 true 이다.\n"
            "\n"
            "[프로토타입]\n"
            "메서드는 각 객체가 개별로 보유하지 않고 클래스의 prototype 에 한 번만 저장된다. 따라서 인스턴스를 100 개 생성해도 speak 함수는 메모리에 하나만 존재하여 효율적이다.\n"
            "\n"
            "[유의 사항]\n"
            "extends 로 상속 계층을 지나치게 깊게 구성하면 특정 메서드의 출처를 파악하기 어려워진다. 일반적으로 2~3 단계 이상은 지양하고, 필요한 기능을 조합하는 방식을 선호한다."
        ),
        usage="동일한 구조의 객체를 여러 개 찍어낼 때, 공통 동작을 부모에 두고 확장할 때 쓴다.",
        cons="과도한 상속 계층은 유지보수를 어렵게 한다(합성 선호). this 바인딩이 풀리는 콜백 사용에 주의해야 한다.",
        code=(
            "class Animal {\n"
            "  constructor(name) { this.name = name; }\n"
            "  speak() { return `${this.name}가 소리낸다`; }\n"
            "}\n"
            "class Dog extends Animal {\n"
            "  speak() { return `${this.name}: 멍멍`; }  // 오버라이드\n"
            "  intro() { return super.speak(); }          // 부모 호출\n"
            "}\n"
            "const d = new Dog('바둑이');\n"
            "console.log(d.speak());    // 바둑이: 멍멍\n"
            "console.log(d.intro());    // 바둑이가 소리낸다\n"
            "console.log(d instanceof Animal); // true\n"
        ),
    ),

    Lesson(
        id="js-adv-05",
        lang="javascript", level="고급",
        title="제너레이터(function*·yield)",
        summary="function* · yield · 지연 평가 · next()",
        explanation=(
            "[개요]\n"
            "일반 함수는 호출되면 끝까지 실행되고 결과를 반환한다. 제너레이터는 실행 도중 yield 로 멈췄다가 필요할 때 next() 호출로 다시 이어서 실행할 수 있는 특수한 함수이다.\n"
            "\n"
            "[핵심 개념]\n"
            "• function 옆에 * 를 붙여 제너레이터 함수를 정의한다.\n"
            "• yield 는 값을 하나 내보내고 실행을 일시정지하며, 다음 next() 호출 시 그 지점부터 재개한다.\n"
            "• 지연 평가(lazy evaluation): 값을 미리 모두 생성하지 않고 필요할 때 하나씩 생성한다. 1 부터 1 억까지의 수열도 배열로 미리 만들지 않아 메모리 사용을 최소화한다.\n"
            "\n"
            "[코드 분석]\n"
            "• function* range(start, end) {        → * 를 붙여 제너레이터 함수를 정의한다.\n"
            "• for (let i = start; i <= end; i++)   → start 부터 end 까지 반복한다.\n"
            "• yield i;                             → 값을 하나 내보내고 일시정지한다. next() 가 올 때까지 대기한다.\n"
            "• console.log([...range(1, 5)]);       → 스프레드로 제너레이터의 모든 값을 배열 [1,2,3,4,5] 로 수집한다.\n"
            "• function* fib() {                    → 피보나치 수열을 생성하는 무한 제너레이터이다.\n"
            "• let [a, b] = [0, 1];                 → 시작값 a=0, b=1 을 설정한다.\n"
            "• while (true) {                       → 무한 반복하지만 yield 로 멈추므로 메모리 문제가 없다.\n"
            "• yield a;                             → 현재 a 값을 내보내고 멈춘다.\n"
            "• [a, b] = [b, a + b];                 → 다음 피보나치 수를 계산한다. (0,1)→(1,1)→(1,2)→(2,3) 순이다.\n"
            "• const g = fib();                     → 제너레이터 객체를 생성한다. 이 시점에는 아직 실행되지 않는다.\n"
            "• const first6 = [];                   → 처음 6 개를 담을 배열이다.\n"
            "• for (let i = 0; i < 6; i++)          → 6 회 반복한다.\n"
            "• first6.push(g.next().value);         → g.next() 는 {value: 다음값, done: 완료여부} 를 반환하며 .value 로 값을 꺼낸다.\n"
            "• console.log(first6);                 → 처음 6 개의 피보나치 수 [0,1,1,2,3,5] 를 출력한다.\n"
            "\n"
            "[yield 와 return 의 차이]\n"
            "• return: 함수를 완전히 종료하고 값을 반환한다.\n"
            "• yield: 값을 반환하고 일시정지하며, 다음 next() 호출 시 그 지점부터 재개한다.\n"
            "\n"
            "[유의 사항]\n"
            "제너레이터는 일반 함수 흐름보다 직관성이 낮다. 단순히 배열을 순회하는 용도라면 for 문이나 배열 메서드가 더 읽기 쉽다."
        ),
        usage="무한/거대 수열을 메모리 없이 다루기, 단계적 상태 머신, 커스텀 이터레이터 구현에 쓴다.",
        cons="동기 코드보다 흐름이 직관적이지 않다. 단순 반복에는 과한 도구라 일반 배열/반복문이 낫다.",
        code=(
            "function* range(start, end) {\n"
            "  for (let i = start; i <= end; i++) yield i;\n"
            "}\n"
            "console.log([...range(1, 5)]);     // [1,2,3,4,5]\n"
            "function* fib() {\n"
            "  let [a, b] = [0, 1];\n"
            "  while (true) { yield a; [a, b] = [b, a + b]; }\n"
            "}\n"
            "const g = fib();\n"
            "const first6 = [];\n"
            "for (let i = 0; i < 6; i++) first6.push(g.next().value);\n"
            "console.log(first6);               // [0,1,1,2,3,5]\n"
        ),
    ),

    Lesson(
        id="js-adv-06",
        lang="javascript", level="고급",
        title="모듈(import·export)",
        summary="export · import · default · CommonJS 비교",
        explanation=(
            "[개요]\n"
            "모듈은 코드를 여러 파일로 분리하여 관리하는 방식이다. 모든 코드를 하나의 파일에 작성하면 규모가 커질수록 유지보수가 어려워지므로, 기능별로 파일을 나누고(export) 필요한 파일에서 가져다 쓴다(import).\n"
            "\n"
            "[핵심 개념]\n"
            "• 이름 내보내기(named export): `export const add = ...` → `import { add } from './파일'`.\n"
            "• 기본 내보내기(default export): `export default PI` → `import PI from './파일'` (이름은 임의로 지정 가능).\n"
            "\n"
            "[코드 분석]\n"
            "다음 예시는 실제로는 파일이 분리되는 모듈 동작을 한 파일에서 흉내낸 것이다.\n"
            "• // math.js  ->  export const add = (a,b)=>a+b;  export default PI;\n"
            "• // main.js  ->  import PI, { add } from './math.js';\n"
            "• const mathModule = (() => {          → 즉시실행함수(IIFE)로 모듈 캡슐화를 모사한다.\n"
            "• const add = (a, b) => a + b;         → 내부에서 사용하는 add 함수이다(export 대상).\n"
            "• const PI = 3.14;                     → 내부에서 사용하는 PI 상수이다(default export 대상).\n"
            "• return { add, default: PI };         → 외부에 공개할 항목을 반환한다. export 를 모사한 부분이다.\n"
            "• })();                                → 즉시 실행하여 결과를 mathModule 에 저장한다.\n"
            "• const { add, default: PI } = mathModule;  → mathModule 에서 add 와 PI(default 를 이름 변경)를 꺼낸다. import 를 모사한 부분이다.\n"
            "• console.log(add(2, 3), PI);          → 5 와 3.14 를 출력한다.\n"
            "• console.log('모듈 = 파일 단위 캡슐화 + 재사용');  → 모듈의 핵심 개념을 출력한다.\n"
            "\n"
            "[실제 파일에서의 작성]\n"
            "• // math.js\n"
            "  export const add = (a, b) => a + b;  // 이름 내보내기\n"
            "  export default 3.14;                 // 기본 내보내기\n"
            "• // main.js\n"
            "  import PI, { add } from './math.js'; // PI 는 default, add 는 이름으로 가져온다\n"
            "\n"
            "[유의 사항]\n"
            "• ES 모듈(.mjs 또는 package.json 의 type:\"module\" 설정)과 CommonJS(require)를 혼용하면 오류가 발생한다.\n"
            "• 모듈이 서로 순환 참조(A 가 B 를, B 가 A 를 가져옴)하면 값이 undefined 가 될 수 있다."
        ),
        usage="코드를 기능 단위 파일로 분리해 재사용·테스트·협업하기 쉽게 만든다. 라이브러리는 대부분 모듈로 배포된다.",
        cons="ESM 과 CommonJS 혼용은 설정 충돌을 일으킨다(.mjs/type:module). 순환 import 는 일부가 undefined 가 될 수 있다.",
        code=(
            "// 실제로는 파일이 나뉘지만, 데모는 한 파일에서 동작을 흉내냅니다.\n"
            "// math.js  ->  export const add = (a,b)=>a+b;  export default PI;\n"
            "// main.js  ->  import PI, { add } from './math.js';\n"
            "const mathModule = (() => {\n"
            "  const add = (a, b) => a + b;\n"
            "  const PI = 3.14;\n"
            "  return { add, default: PI };   // export 흉내\n"
            "})();\n"
            "const { add, default: PI } = mathModule; // import 흉내\n"
            "console.log(add(2, 3), PI);       // 5 3.14\n"
            "console.log('모듈 = 파일 단위 캡슐화 + 재사용');\n"
        ),
    ),

    Lesson(
        id="js-adv-07",
        lang="javascript", level="고급",
        title="이터러블과 심볼(Symbol.iterator)",
        summary="Symbol · 이터러블 프로토콜 · for...of 직접 구현",
        explanation=(
            "[개요]\n"
            "이터러블(Iterable)은 for...of 로 순회할 수 있는 객체를 의미한다. 배열·문자열·Map·Set 은 기본적으로 이터러블이며, 사용자가 정의한 객체도 이터러블로 만들 수 있다.\n"
            "\n"
            "[핵심 개념]\n"
            "• 심볼(Symbol)은 절대 중복되지 않는 유일한 값이다.\n"
            "• Symbol.iterator 는 JavaScript 가 미리 정의한 특별한 심볼로, 객체에 구현하면 for...of, 스프레드, 구조분해를 사용할 수 있다.\n"
            "• 이터레이터 프로토콜: 객체에 [Symbol.iterator]() 메서드를 구현하고, 이 메서드는 next() 를 가진 객체를 반환하며, next() 는 { value: 현재값, done: 완료여부 } 를 반환한다. done 이 true 가 되면 반복이 종료된다.\n"
            "\n"
            "[코드 분석]\n"
            "• const sym = Symbol('id');            → 'id' 라는 설명을 가진 유일한 심볼을 생성한다. 호출할 때마다 다른 값이 된다.\n"
            "• const obj = { [sym]: 100, name: 'x' };  → 심볼을 키로 사용해 속성을 정의한다. 대괄호 [sym] 로 감싸야 한다.\n"
            "• console.log(obj[sym]);               → 심볼 키로 값을 읽어 100 을 출력한다.\n"
            "• const countTo = {                    → 이터러블 객체를 정의한다.\n"
            "• limit: 3,                            → 3 까지 세는 객체이다.\n"
            "• [Symbol.iterator]() {                → Symbol.iterator 메서드를 구현하며, 이것이 객체를 이터러블로 만드는 핵심이다.\n"
            "• let i = 0, limit = this.limit;       → 현재 카운터 i 와 최대값 limit 를 설정한다.\n"
            "• return { next: () => i < limit       → 이터레이터 객체를 반환한다. i 가 limit 보다 작으면\n"
            "• ? { value: ++i, done: false }        → i 를 1 증가시켜 그 값을 내보내며 done: false 로 미완료를 표시한다.\n"
            "• : { value: undefined, done: true }   → 모두 세었으면 done: true 로 종료를 알린다.\n"
            "• console.log([...countTo]);           → 스프레드 연산자가 이터러블을 순회하여 배열 [1,2,3] 으로 만든다.\n"
            "• for (const v of countTo)             → for...of 로 순회한다.\n"
            "• process.stdout.write(v + ' ');       → 1 2 3 이 차례로 출력된다.\n"
            "\n"
            "[심볼을 키로 사용하는 이유]\n"
            "일반 문자열 키는 다른 코드와 충돌할 수 있으나, Symbol 은 항상 유일하므로 충돌 없이 내부 동작을 정의할 수 있다.\n"
            "\n"
            "[유의 사항]\n"
            "• 심볼 키는 Object.keys(), JSON.stringify() 에서 제외되므로 의도적으로 숨기는 용도로 활용할 수 있다.\n"
            "• Symbol.iterator 를 직접 구현하는 것은 복잡하므로, 제너레이터(function*)를 사용하면 훨씬 간단하게 대체할 수 있다."
        ),
        usage="커스텀 컬렉션을 표준 반복 문법으로 순회하게 하거나, 충돌 없는 메타 속성 키를 만들 때 쓴다.",
        cons="직접 구현은 보일러플레이트가 많다(대개 제너레이터로 간단히 대체). 심볼 키는 일반 순회/JSON 에서 빠진다.",
        code=(
            "const sym = Symbol('id');\n"
            "const obj = { [sym]: 100, name: 'x' };\n"
            "console.log(obj[sym]);                 // 100\n"
            "const countTo = {\n"
            "  limit: 3,\n"
            "  [Symbol.iterator]() {\n"
            "    let i = 0, limit = this.limit;\n"
            "    return { next: () => i < limit\n"
            "      ? { value: ++i, done: false }\n"
            "      : { value: undefined, done: true } };\n"
            "  },\n"
            "};\n"
            "console.log([...countTo]);             // [1,2,3]\n"
            "for (const v of countTo) process.stdout.write(v + ' ');\n"
            "console.log();                         // 1 2 3\n"
        ),
    ),

    Lesson(
        id="js-adv-08",
        lang="javascript", level="고급",
        title="함수형 패턴(compose·pipe·curry)",
        summary="함수 합성 · pipe · 커링 · 부분적용",
        explanation=(
            "[개요]\n"
            "함수형 프로그래밍은 작은 함수들을 조합하여 복잡한 작업을 처리하는 스타일이다. pipe, compose, curry 는 그 대표적인 패턴이다.\n"
            "\n"
            "[핵심 개념]\n"
            "• pipe: 데이터가 여러 함수를 왼쪽에서 오른쪽 순서로 통과한다.\n"
            "• compose: pipe 와 동일하나 오른쪽에서 왼쪽 순서로 함수를 적용한다. 수학의 합성함수와 같다.\n"
            "• curry(커링): 여러 인자를 받는 함수를 인자 하나씩 받는 함수들로 분리한다. add(1, 2, 3) 을 add(1)(2)(3) 형태로 호출한다.\n"
            "\n"
            "[코드 분석]\n"
            "• const pipe = (...fns) => x => fns.reduce((acc, fn) => fn(acc), x);\n"
            "  → fns 는 함수 배열, x 는 초기값이다. reduce 로 함수를 왼쪽에서 오른쪽 순으로 적용한다.\n"
            "• const compose = (...fns) => x => fns.reduceRight((acc, fn) => fn(acc), x);\n"
            "  → reduceRight 로 오른쪽에서 왼쪽 순으로 적용한다.\n"
            "• const inc = n => n + 1;               → n 에 1 을 더하는 함수이다.\n"
            "• const dbl = n => n * 2;               → n 을 2 배 하는 함수이다.\n"
            "• console.log(pipe(inc, dbl)(5));        → inc(5)=6 후 dbl(6)=12. 왼→오 순서이므로 inc 를 먼저 적용한다.\n"
            "• console.log(compose(inc, dbl)(5));     → dbl(5)=10 후 inc(10)=11. 오→왼 순서이므로 dbl 을 먼저 적용한다.\n"
            "• const curry = a => b => c => a + b + c;  → a 를 받으면 b 를, b 를 받으면 c 를 기다리는 함수를 반환한다.\n"
            "• const add10 = curry(10);              → a=10 으로 고정한 함수를 만든다. b, c 가 아직 필요하다.\n"
            "• console.log(add10(20)(3));             → add10(20) 은 a=10, b=20, 이어서 (3) 은 c=3. 10+20+3=33 이다.\n"
            "• const nums = [1, 2, 3, 4];            → 처리할 숫자 배열이다.\n"
            "• arr => arr.filter(n => n % 2 === 0),  → 짝수만 선택한다: [2, 4].\n"
            "• arr => arr.map(dbl),                  → 각 항목을 2 배 한다: [4, 8].\n"
            "• )(nums)                               → 배열이 두 단계 변환을 거쳐 [4, 8] 이 출력된다.\n"
            "\n"
            "[함수형 패턴의 이점]\n"
            "• 작은 함수(inc, dbl, filter 등)는 독립적이어서 개별 테스트가 용이하다.\n"
            "• pipe/compose 로 조합하면 복잡한 변환도 순서대로 이해할 수 있다.\n"
            "• 커링으로 설정을 미리 고정한 특화 함수를 만들 수 있다(add10, add20 등).\n"
            "\n"
            "[유의 사항]\n"
            "• 화살표 함수가 중첩되면 처음에는 가독성이 떨어지므로 한 단계씩 분석해야 한다.\n"
            "• 단순한 작업에 함수형 패턴을 억지로 적용하면 오히려 코드가 복잡해진다."
        ),
        usage="데이터 변환 파이프라인을 작은 순수 함수의 조합으로 표현할 때. 설정을 미리 고정한 특화 함수를 만들 때(부분적용).",
        cons="합성 단계가 많으면 디버깅이 어렵다(중간값이 안 보임). 과한 추상화는 오히려 가독성을 해친다.",
        code=(
            "const pipe = (...fns) => x => fns.reduce((acc, fn) => fn(acc), x);\n"
            "const compose = (...fns) => x => fns.reduceRight((acc, fn) => fn(acc), x);\n"
            "const inc = n => n + 1;\n"
            "const dbl = n => n * 2;\n"
            "console.log(pipe(inc, dbl)(5));     // (5+1)*2 = 12\n"
            "console.log(compose(inc, dbl)(5));  // (5*2)+1 = 11\n"
            "const curry = a => b => c => a + b + c;\n"
            "const add10 = curry(10);\n"
            "console.log(add10(20)(3));          // 33\n"
            "const nums = [1, 2, 3, 4];\n"
            "console.log(pipe(\n"
            "  arr => arr.filter(n => n % 2 === 0),\n"
            "  arr => arr.map(dbl),\n"
            ")(nums));                            // [4,8]\n"
        ),
    ),
]
