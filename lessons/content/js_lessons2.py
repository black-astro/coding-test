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
            "━━ 조건문(if·else)이란? ━━\n"
            "\n"
            "프로그램이 어떤 상황에 따라 다른 일을 하게 만드는 장치예요.\n"
            "마치 신호등처럼: 빨간불이면 멈추고(if), 초록불이면 가는(else) 거예요.\n"
            "우리 일상에서도 \"만약 비가 오면 우산을 챙기고, 아니면 그냥 나간다\"는 조건 판단을 항상 하잖아요?\n"
            "그걸 코드로 쓰는 게 바로 if/else 예요.\n"
            "\n"
            "삼항 연산자는 조건 ? '참일 때 값' : '거짓일 때 값' 형태로,\n"
            "마치 \"버튼을 누르면 A가 나오고, 안 누르면 B가 나오는 자판기\"처럼\n"
            "짧게 한 줄로 값을 고를 때 써요.\n"
            "\n"
            "코드 한 줄씩 읽기:\n"
            "  const score = 82;         →  score라는 변수에 82라는 값을 넣어요. 이게 판단의 재료예요.\n"
            "  let grade;                →  grade라는 변수를 만들어요. 아직 값은 없어요(undefined).\n"
            "  if (score >= 90) grade = 'A';       →  score가 90 이상이면 grade를 'A'로 정해요.\n"
            "  else if (score >= 80) grade = 'B';  →  앞 조건이 아니고 80 이상이면 grade를 'B'로 정해요.\n"
            "  else grade = 'C';                   →  앞 조건 둘 다 아니면 grade는 'C'예요.\n"
            "  console.log('학점:', grade);        →  score가 82이므로 grade는 'B'. '학점: B'가 출력돼요.\n"
            "  const pass = score >= 60 ? '합격' : '불합격';  →  삼항: 60 이상이면 '합격', 아니면 '불합격'을 pass에 넣어요.\n"
            "  console.log(pass);                  →  82 >= 60 이므로 '합격'이 출력돼요.\n"
            "  const input = 0;                    →  input 변수에 0을 넣어요.\n"
            "  console.log(input || 100);          →  || 는 왼쪽이 falsy(0)이면 오른쪽 100을 써요. 결과: 100.\n"
            "  console.log(input ?? 100);          →  ?? 는 왼쪽이 null/undefined일 때만 오른쪽을 써요. 0은 null이 아니므로 결과: 0.\n"
            "  console.log(score >= 80 && score < 90);  →  && 는 \"그리고\". 둘 다 참이어야 true. 82는 80 이상이고 90 미만이므로 true.\n"
            "\n"
            "왜 || 와 ?? 를 구분해야 하나요?\n"
            "  사용자가 나이를 0으로 입력했을 때, age || 18 이면 0을 \"없음\"으로 보고 18로 바꿔버려요.\n"
            "  age ?? 18 이면 0은 진짜 값이므로 그냥 0을 씁니다. 훨씬 안전해요.\n"
            "\n"
            "주의할 점:\n"
            "  if-else if-else 의 조건은 위에서 아래로 차례로 검사하고 첫 일치에서 딱 멈춰요.\n"
            "  삼항은 짧고 간단한 선택에만 써요. 복잡한 조건엔 if-else 가 훨씬 읽기 쉬워요."
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
            "━━ 반복문이란? ━━\n"
            "\n"
            "\"같은 일을 여러 번 하라\"는 명령이에요.\n"
            "예를 들어 1부터 100까지 숫자를 더하려면 손으로 100번 더해야 할까요?\n"
            "아니요! 반복문에 \"1부터 100까지 더해\" 하고 시키면 컴퓨터가 알아서 해줘요.\n"
            "\n"
            "for 문은 몇 번 반복할지 횟수가 정해질 때 써요.\n"
            "while 문은 \"조건이 참인 동안\" 계속 반복해요. 언제 멈출지 조건으로 정해요.\n"
            "for...of 는 배열의 각 항목을 하나씩 꺼내서 처리할 때 가장 편해요.\n"
            "\n"
            "비유:\n"
            "  for  → \"10번 팔굽혀펴기\"처럼 횟수가 정해진 것\n"
            "  while → \"배부를 때까지 먹어\"처럼 조건이 될 때까지 하는 것\n"
            "  for...of → \"접시에 있는 음식을 하나씩 다 먹어\"처럼 목록을 순서대로 처리하는 것\n"
            "\n"
            "코드 한 줄씩 읽기:\n"
            "  let sum = 0;                    →  합계를 저장할 변수를 0으로 시작해요.\n"
            "  for (let i = 1; i <= 5; i++)    →  i를 1로 시작해서, i가 5 이하인 동안, 매 반복마다 i를 1씩 늘려요.\n"
            "    sum += i;                     →  sum에 i를 더해요. 1+2+3+4+5 = 15.\n"
            "  console.log('1~5 합:', sum);    →  결과 15를 출력해요.\n"
            "  let n = 8, cnt = 0;             →  n은 8, 반감 횟수 cnt는 0으로 시작해요.\n"
            "  while (n > 1) {                 →  n이 1보다 크면 계속 반복해요.\n"
            "    n = Math.floor(n / 2);        →  n을 절반으로 나누고 소수점은 버려요. 8→4→2→1 순서로 변해요.\n"
            "    cnt++;                        →  횟수를 1 늘려요.\n"
            "  }                              →  n이 1이 되면 반복을 멈춰요.\n"
            "  console.log('반감 횟수:', cnt); →  3번 반감했으므로 3을 출력해요.\n"
            "  for (const ch of 'abc')         →  문자열 'abc'에서 문자를 하나씩 꺼내요. ch = 'a', 'b', 'c' 순서로.\n"
            "    process.stdout.write(ch + ' ');  →  한 줄에 이어서 출력해요. (줄바꿈 없이)\n"
            "  for (let i = 0; i < 5; i++) {   →  0부터 4까지 반복해요.\n"
            "    if (i === 3) break;            →  i가 3이면 즉시 반복문 전체를 끝내요.\n"
            "    if (i % 2 === 0) continue;     →  i가 짝수면 이번 회차만 건너뛰고 다음 반복으로 가요.\n"
            "    console.log('홀수 i:', i);     →  홀수인 i=1 만 출력되고, i=3에서 break돼요.\n"
            "  }\n"
            "\n"
            "왜 break 와 continue 를 쓰나요?\n"
            "  break: 더 이상 반복이 필요 없을 때 빨리 빠져나와서 시간을 아껴요.\n"
            "  continue: 특정 조건의 항목은 건너뛰고 나머지만 처리할 때 써요.\n"
            "\n"
            "주의할 점:\n"
            "  while 문에서 조건이 절대 false가 되지 않으면 무한루프에 빠져요!\n"
            "  while (true) { } 처럼 쓰면 프로그램이 영원히 안 끝나요. 반드시 탈출 조건을 넣으세요."
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
            "━━ switch 문이란? ━━\n"
            "\n"
            "하나의 값이 여러 경우 중 어디에 해당하는지 구분할 때 쓰는 분기 도구예요.\n"
            "마치 엘리베이터 버튼처럼: 1층을 누르면 1층으로, 5층을 누르면 5층으로, 눌리지 않은 층은 무시해요.\n"
            "if-else if-else if-else 를 여러 번 쓰면 복잡해지는데,\n"
            "switch 를 쓰면 각 경우를 case 로 깔끔하게 정리할 수 있어요.\n"
            "\n"
            "중요한 규칙: 각 case 실행 후 break 를 반드시 써야 해요.\n"
            "break 를 안 쓰면 아래 case 까지 계속 흘러 내려가요(fall-through 라고 해요).\n"
            "이건 버그처럼 보이지만, 의도적으로 여러 case 를 같은 동작으로 묶을 때 활용할 수도 있어요.\n"
            "\n"
            "코드 한 줄씩 읽기:\n"
            "  function dayName(d) {         →  요일 번호를 받아서 이름을 반환하는 함수를 만들어요.\n"
            "    switch (d) {                →  d 의 값을 각 case 와 비교해요.\n"
            "      case 0: return '일';      →  d 가 정확히 0 이면 '일'을 반환해요. === (완전 일치) 비교를 써요.\n"
            "      case 6: return '토';      →  d 가 6 이면 '토'를 반환해요.\n"
            "      default: return '평일';   →  어느 case 에도 안 맞으면 기본값인 '평일'을 반환해요.\n"
            "    }\n"
            "  }\n"
            "  console.log(dayName(0), dayName(3), dayName(6));  →  0은 '일', 3은 '평일'(default), 6은 '토'가 나와요.\n"
            "  const fruit = 'apple';        →  fruit 변수에 'apple' 문자열을 넣어요.\n"
            "  switch (fruit) {              →  fruit 의 값을 case 들과 비교해요.\n"
            "    case 'apple':               →  fruit 가 'apple' 이면 여기로 와요. break 가 없으므로 아래로 내려가요!\n"
            "    case 'pear':                →  fruit 가 'pear' 여도 같은 동작을 해요. (fall-through 활용)\n"
            "      console.log('포미과 과일');  →  apple 이든 pear 든 이 줄이 실행돼요.\n"
            "      break;                    →  여기서 멈춰요. default 로 안 가요.\n"
            "    default:\n"
            "      console.log('기타');      →  apple 도 pear 도 아닌 과일이면 '기타'가 나와요.\n"
            "  }\n"
            "\n"
            "왜 switch 를 쓰나요?\n"
            "  if (d===0) { ... } else if (d===1) { ... } else if (d===2) { ... } ...\n"
            "  이렇게 쓰면 줄이 너무 길어져요. switch 를 쓰면 훨씬 정돈되어 보여요.\n"
            "\n"
            "주의할 점:\n"
            "  break 를 깜빡하면 다음 case 까지 실행돼요! 아주 흔한 실수예요.\n"
            "  switch 는 === (완전 일치) 비교를 써요. '80'(문자열)과 80(숫자)는 다른 값으로 봐요."
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
            "━━ 템플릿 리터럴이란? ━━\n"
            "\n"
            "변수를 문자열 안에 쉽게 끼워 넣는 방법이에요.\n"
            "예전에는 \"안녕하세요, \" + name + \"님!\" 이렇게 + 로 붙여야 했어요. 불편하죠?\n"
            "템플릿 리터럴을 쓰면 `안녕하세요, ${name}님!` 처럼 훨씬 자연스럽게 쓸 수 있어요.\n"
            "마치 빈칸 채우기 문제처럼: \"___님은 ___살입니다\" 의 빈칸에 변수 값이 들어가는 거예요.\n"
            "\n"
            "백틱(`)은 키보드에서 Tab 키 위에 있는 기호예요. 작은따옴표(')와 달라요!\n"
            "${} 안에는 변수뿐 아니라 계산식이나 함수 호출도 넣을 수 있어요.\n"
            "그리고 줄바꿈을 그대로 써도 되므로 여러 줄 문자열이 훨씬 쉬워져요.\n"
            "\n"
            "코드 한 줄씩 읽기:\n"
            "  const name = '홍길동', age = 20;   →  이름과 나이 변수를 만들어요.\n"
            "  console.log(`${name}님은 ${age}살, 내년엔 ${age + 1}살`);  →  백틱으로 감싸고 ${} 안에 변수와 계산식을 넣어요. ${age + 1}은 21을 자동 계산해서 끼워 넣어요.\n"
            "  const items = ['사과', '바나나'];  →  과일 이름 배열을 만들어요.\n"
            "  const msg = `장바구니(${items.length}개):\\n- ${items.join('\\n- ')}`;  →  items.length 는 2, items.join('\\n- ') 은 '사과\\n- 바나나' 가 돼요. 여러 줄 문자열이에요.\n"
            "  console.log(msg);  →  장바구니 목록이 여러 줄로 출력돼요.\n"
            "  const t = 75;  →  온도(또는 점수) 변수 t 에 75 를 넣어요.\n"
            "  console.log(`상태: ${t >= 70 ? '높음' : '낮음'}`);  →  ${} 안에 삼항 연산자를 넣었어요. t 가 70 이상이므로 '높음'이 들어가요.\n"
            "\n"
            "왜 템플릿 리터럴을 쓰나요?\n"
            "  + 연결 방식: '이름: ' + name + ', 나이: ' + age + '살'\n"
            "  템플릿 리터럴: `이름: ${name}, 나이: ${age}살`\n"
            "  훨씬 읽기 쉽죠? 변수가 많을수록 차이가 더 커요.\n"
            "\n"
            "주의할 점:\n"
            "  반드시 백틱(`)을 써야 해요. 작은따옴표(')나 큰따옴표(\")를 쓰면 작동 안 해요.\n"
            "  ${} 안에 복잡한 계산을 많이 넣으면 오히려 읽기 어려워져요. 긴 계산은 미리 변수에 넣어두세요."
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
            "━━ 형변환(Type Conversion)이란? ━━\n"
            "\n"
            "JavaScript 에서 값에는 종류(타입)가 있어요: 숫자, 문자열, 불리언(참/거짓) 등.\n"
            "형변환은 이 종류를 바꾸는 거예요.\n"
            "예를 들어 사용자가 나이를 입력하면 항상 문자열('25')로 들어와요.\n"
            "계산하려면 숫자(25)로 바꿔야 해요 — 이게 형변환이에요!\n"
            "\n"
            "truthy/falsy 는 조건문에서 값을 참/거짓으로 해석하는 규칙이에요.\n"
            "JavaScript 에서 딱 6가지 값만 거짓(falsy)으로 봐요:\n"
            "  false, 0, '' (빈 문자열), null, undefined, NaN\n"
            "이 6가지를 제외한 모든 값은 참(truthy)이에요. '0'(문자열 영)도 truthy 예요!\n"
            "\n"
            "코드 한 줄씩 읽기:\n"
            "  console.log(Number('42'), parseInt('12px', 10));  →  '42'(문자열)을 42(숫자)로, '12px'에서 앞의 숫자 12만 뽑아요. parseInt 두 번째 인자 10은 10진수 기준이에요.\n"
            "  console.log(Number(''), Number('abc'));            →  빈 문자열을 숫자로 바꾸면 0, 숫자가 없는 문자열은 NaN(Not a Number)이에요.\n"
            "  console.log(String(123) + '!', Boolean(0));       →  123을 문자열 '123'으로 바꾸고 '!'를 붙여요. Boolean(0)은 0이 falsy라 false예요.\n"
            "  const falsy = [false, 0, '', null, undefined, NaN];  →  6가지 falsy 값을 배열로 모았어요.\n"
            "  console.log(falsy.map(v => Boolean(v)));           →  각각을 Boolean으로 변환해요. 모두 false가 나와요.\n"
            "  console.log(!!'0', !!0);                           →  '0'은 문자열이라 truthy, 그래서 !!'0'은 true. 0은 falsy라 !!0은 false예요.\n"
            "  const userInput = '';                              →  빈 문자열(사용자가 아무것도 안 입력)을 시뮬레이션해요.\n"
            "  console.log(userInput ? '입력됨' : '비어있음');    →  빈 문자열은 falsy이므로 '비어있음'이 출력돼요.\n"
            "\n"
            "!! (느낌표 두 개)는 왜 쓰나요?\n"
            "  !x 는 값을 반전한 boolean 으로 만들어요.\n"
            "  !!x 는 두 번 반전해서 원래 truthy/falsy 를 boolean 으로 확실하게 만들어요.\n"
            "  !!0 → !true → false,  !!'hello' → !false → true 이런 식이에요.\n"
            "\n"
            "주의할 점:\n"
            "  '0'(문자열 영)은 truthy 예요! 숫자 0 과 헷갈리면 안 돼요.\n"
            "  사용자 입력을 받아 || 로 기본값을 설정할 때, 0 이 유효한 값이라면 꼭 ?? 를 쓰세요."
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
            "━━ 객체 메서드와 this 란? ━━\n"
            "\n"
            "객체 안에 함수를 넣으면 그 함수를 \"메서드\"라고 불러요.\n"
            "예를 들어 은행 계좌 객체가 있다면, 계좌 번호(데이터)와 함께 입금하기·출금하기(메서드)도 함께 담겨 있어요.\n"
            "메서드 안에서 같은 객체의 다른 속성을 쓰려면 this 를 써요.\n"
            "this 는 \"나를 호출한 그 객체\"를 가리키는 특별한 키워드예요.\n"
            "\n"
            "비유: 내가 \"철수의 나이를 알려줘\" 라고 하면 철수 객체의 메서드가 실행되고,\n"
            "그 안에서 this.age 는 철수의 나이를 가리켜요.\n"
            "만약 영희가 같은 메서드를 호출하면 this.age 는 영희의 나이가 돼요.\n"
            "\n"
            "화살표 함수 vs 일반 함수:\n"
            "  일반 함수(function): this = \"호출한 객체\"\n"
            "  화살표 함수(=>): this = \"함수가 만들어진 곳의 this\" (자신만의 this 가 없어요)\n"
            "\n"
            "코드 한 줄씩 읽기:\n"
            "  const counter = {          →  counter 라는 객체를 만들어요.\n"
            "    count: 0,                →  count 속성을 0 으로 초기화해요.\n"
            "    inc() {                  →  inc 라는 메서드예요. { inc: function() { ... } } 의 단축 문법이에요.\n"
            "      this.count++;          →  이 메서드를 호출한 객체(counter)의 count 를 1 늘려요.\n"
            "      return this.count;     →  늘어난 count 값을 반환해요.\n"
            "    },\n"
            "    label: 'C',              →  label 속성에 'C' 를 넣어요.\n"
            "    show() {                 →  show 메서드예요.\n"
            "      return `${this.label}=${this.count}`;  →  이 객체의 label 과 count 를 합쳐 문자열로 반환해요.\n"
            "    },\n"
            "  };\n"
            "  console.log(counter.inc(), counter.inc());  →  inc() 를 두 번 호출하면 1, 2 가 나와요. count 가 0→1→2 로 바뀌어요.\n"
            "  console.log(counter.show());               →  label='C', count=2 이므로 'C=2' 가 출력돼요.\n"
            "  const obj = {\n"
            "    vals: [1, 2, 3], factor: 10,  →  값 배열과 배율을 넣은 객체예요.\n"
            "    scaled() {                    →  scaled 메서드예요.\n"
            "      return this.vals.map(v => v * this.factor);  →  배열의 각 값에 factor 를 곱해요. 화살표 함수이므로 this 는 바깥(obj)을 가리켜요!\n"
            "    },\n"
            "  };\n"
            "  console.log(obj.scaled());  →  [10, 20, 30] 이 출력돼요.\n"
            "\n"
            "왜 화살표 함수가 map 콜백으로 좋나요?\n"
            "  map 안의 콜백이 일반 함수라면 this 가 obj 가 아닌 undefined 가 돼요!\n"
            "  화살표 함수는 바깥 this(=obj) 를 그대로 쓰므로 this.factor 가 제대로 10 이 돼요.\n"
            "\n"
            "주의할 점:\n"
            "  const greet = counter.show; 처럼 메서드를 변수에 담아서 greet() 로 따로 호출하면\n"
            "  this 가 counter 를 가리키지 않아요(undefined). 메서드는 항상 객체를 통해 호출해야 해요."
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
            "━━ 예외 처리(try·catch·throw)란? ━━\n"
            "\n"
            "프로그램이 실행 중에 예상치 못한 오류가 생길 때,\n"
            "프로그램이 그냥 죽지 않도록 오류를 \"잡아서\" 처리하는 방법이에요.\n"
            "\n"
            "비유: 요리사가 칼을 사용하다 다칠 수 있어요(오류 발생).\n"
            "보건실에 가서 치료받고 요리를 계속 할 수 있어요(catch 에서 처리 후 계속).\n"
            "finally 는 다쳤든 안 다쳤든 요리가 끝나면 반드시 칼을 씻는 것(항상 실행)이에요.\n"
            "\n"
            "throw 는 직접 오류를 만들어 던지는 거예요.\n"
            "예를 들어 0 으로 나누면 안 되는데 0 이 들어왔을 때,\n"
            "우리가 직접 \"이건 안 돼!\" 라고 오류를 만들 수 있어요.\n"
            "\n"
            "코드 한 줄씩 읽기:\n"
            "  function divide(a, b) {              →  나누기 함수를 만들어요.\n"
            "    if (b === 0)                       →  나누는 수가 0 이면...\n"
            "      throw new Error('0으로 나눌 수 없음');  →  오류를 만들어서 던져요. 이 순간 함수 실행이 멈춰요.\n"
            "    return a / b;                      →  0 이 아니면 정상 계산 결과를 반환해요.\n"
            "  }\n"
            "  try {                                →  오류가 날 수 있는 코드를 여기 안에 써요.\n"
            "    console.log(divide(10, 2));        →  10 ÷ 2 = 5. 정상 실행, 5 가 출력돼요.\n"
            "    console.log(divide(10, 0));        →  b=0 이므로 throw 가 실행돼요! 이 줄에서 오류가 던져져요.\n"
            "  } catch (e) {                        →  try 블록에서 오류가 생기면 여기로 와요. e 에 오류 객체가 담겨요.\n"
            "    console.log('에러:', e.message);  →  오류 메시지를 출력해요. '0으로 나눌 수 없음'이 나와요.\n"
            "  } finally {                          →  오류가 났든 안 났든 무조건 실행돼요.\n"
            "    console.log('계산 종료');          →  '계산 종료'가 항상 출력돼요.\n"
            "  }\n"
            "  try { JSON.parse('{bad}'); }         →  잘못된 JSON 문자열을 파싱하려고 해요. 반드시 오류가 나요.\n"
            "  catch (e) { console.log('파싱 실패:', e.name); }  →  SyntaxError 오류가 잡혀요.\n"
            "\n"
            "왜 예외 처리가 필요한가요?\n"
            "  오류 처리가 없으면 오류가 생기는 순간 프로그램이 완전히 멈춰버려요.\n"
            "  try-catch 가 있으면 오류가 생겨도 catch 에서 처리하고 프로그램이 계속 실행돼요.\n"
            "\n"
            "주의할 점:\n"
            "  catch 블록을 비워두면 오류를 무시하게 돼요 — 나중에 버그를 찾기 매우 어려워져요.\n"
            "  최소한 console.error 로 오류 내용을 남겨두세요."
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
            "━━ JSON 이란? ━━\n"
            "\n"
            "JSON(JavaScript Object Notation)은 데이터를 주고받을 때 쓰는 표준 문자열 형식이에요.\n"
            "웹에서 서버와 브라우저가 데이터를 주고받을 때 거의 항상 JSON 을 써요.\n"
            "마치 택배 상자처럼: 물건(객체)을 상자(JSON 문자열)에 담아서 보내고,\n"
            "받는 쪽에서 상자를 열어(parse) 물건을 꺼내요.\n"
            "\n"
            "JSON.stringify = 객체 → 문자열 (포장)\n"
            "JSON.parse     = 문자열 → 객체 (개봉)\n"
            "\n"
            "코드 한 줄씩 읽기:\n"
            "  const user = { name: '김철수', age: 20, tags: ['a', 'b'] };  →  JavaScript 객체를 만들어요.\n"
            "  const json = JSON.stringify(user);  →  객체를 JSON 문자열로 변환해요. {\"name\":\"김철수\",\"age\":20,\"tags\":[\"a\",\"b\"]} 가 돼요.\n"
            "  console.log(json);                  →  JSON 문자열을 출력해요.\n"
            "  console.log(JSON.stringify(user, null, 2));  →  세 번째 인자 2 는 들여쓰기 칸 수예요. 보기 좋게 정렬되어 출력돼요.\n"
            "  const back = JSON.parse(json);      →  JSON 문자열을 다시 JavaScript 객체로 복원해요.\n"
            "  console.log(back.name, back.tags[1]);  →  복원된 객체에서 속성을 꺼내요. '김철수' 와 'b' 가 출력돼요.\n"
            "  const skip = { id: 1, fn: () => 1, u: undefined };  →  함수와 undefined 를 포함한 객체예요.\n"
            "  console.log(JSON.stringify(skip));  →  JSON 은 함수와 undefined 를 지원 안 해요. 그래서 id 만 남아요: {\"id\":1}\n"
            "\n"
            "JSON 형식 규칙:\n"
            "  키(속성 이름)는 반드시 큰따옴표로 감싸야 해요: {\"name\": \"값\"}\n"
            "  문자열 값도 큰따옴표: {\"city\": \"서울\"}\n"
            "  숫자는 따옴표 없이: {\"age\": 20}\n"
            "  null, true, false 사용 가능. undefined, 함수, 심볼은 불가능.\n"
            "\n"
            "왜 JSON 을 쓰나요?\n"
            "  객체를 그대로 전송할 수 없어요. 문자열로 바꿔야 네트워크로 전달할 수 있어요.\n"
            "  JSON 은 모든 언어(Python, Java, C++ 등)에서 다 읽을 수 있는 범용 형식이에요.\n"
            "\n"
            "주의할 점:\n"
            "  JSON.parse 는 잘못된 형식이면 SyntaxError 를 던져요. 외부에서 받은 JSON 은 try-catch 로 감싸세요.\n"
            "  순환 참조(obj.self = obj 처럼 자기 자신을 참조)는 stringify 가 오류를 던져요."
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
            "━━ Date 와 타이머란? ━━\n"
            "\n"
            "Date 객체는 날짜와 시간을 다루는 도구예요.\n"
            "\"오늘 날짜가 뭐야?\", \"두 날짜 사이에 며칠이 지났어?\" 같은 걸 계산할 때 써요.\n"
            "\n"
            "타이머(setTimeout)는 \"몇 밀리초 후에 이 작업을 해줘\"라고 예약하는 기능이에요.\n"
            "비유: 요리할 때 타이머를 3분으로 맞춰두고 다른 일을 하다가,\n"
            "타이머가 울리면 요리를 꺼내는 것과 같아요.\n"
            "JavaScript 는 타이머 시간 동안 다른 코드를 계속 실행해요(비동기).\n"
            "\n"
            "코드 한 줄씩 읽기:\n"
            "  const start = new Date(2024, 0, 1);  →  2024년 1월 1일 날짜 객체를 만들어요.\n"
            "                                           주의: 월은 0부터 시작해요! 0=1월, 11=12월.\n"
            "  const end = new Date(2024, 0, 11);   →  2024년 1월 11일 날짜 객체를 만들어요.\n"
            "  const days = (end.getTime() - start.getTime()) / (1000 * 60 * 60 * 24);\n"
            "    →  getTime() 은 1970년 1월 1일 자정부터의 밀리초예요.\n"
            "       두 날짜 차이를 밀리초로 구하고, 1초=1000ms, 1분=60초, 1시간=60분, 1일=24시간으로 나눠서 일수를 구해요.\n"
            "  console.log('경과 일수:', days);     →  10 이 출력돼요. 1월 1일부터 1월 11일까지 10일이에요.\n"
            "  console.log(start.getFullYear(), start.getMonth() + 1);  →  getFullYear() 는 연도(2024), getMonth() 는 0 을 반환하므로 +1 해서 1월을 표시해요.\n"
            "  setTimeout(() => {                   →  화살표 함수를 0 밀리초 후에 실행해요.\n"
            "    console.log('1초 후처럼 동작(데모는 0ms)');  →  이 줄이 나중에 실행돼요.\n"
            "  }, 0);                               →  0ms 지연 — 현재 코드 다 실행 후에 실행돼요.\n"
            "  console.log('타이머 등록 완료(먼저 출력)');  →  setTimeout 보다 이 줄이 먼저 출력돼요!\n"
            "\n"
            "왜 getMonth() 가 0 부터 시작하나요?\n"
            "  역사적인 이유로 그렇게 설계됐어요. 일관성이 없어서 많은 프로그래머들이 헷갈려요.\n"
            "  그래서 항상 getMonth() + 1 로 써야 사람이 읽는 월 번호가 나와요.\n"
            "\n"
            "주의할 점:\n"
            "  setTimeout 은 비동기예요. setTimeout 이후의 코드가 먼저 실행되고, 타이머가 끝나면 콜백이 실행돼요.\n"
            "  \"0ms 후에 실행\"도 현재 코드가 다 끝난 후에야 실행돼요."
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
            "━━ 배열 검색 메서드란? ━━\n"
            "\n"
            "배열에서 특정 항목을 찾거나, 조건을 만족하는 항목이 있는지 확인하는 메서드들이에요.\n"
            "for 문으로 직접 순회하지 않아도 되므로 코드가 훨씬 짧고 읽기 쉬워요.\n"
            "\n"
            "각각의 용도:\n"
            "  find      → 조건에 맞는 첫 번째 \"항목 자체\"를 반환해요\n"
            "  findIndex → 조건에 맞는 첫 번째 항목의 \"위치(인덱스)\"를 반환해요\n"
            "  includes  → 특정 값이 배열에 있는지 true/false 로 알려줘요\n"
            "  some      → 조건을 만족하는 항목이 하나라도 있으면 true\n"
            "  every     → 모든 항목이 조건을 만족해야 true\n"
            "\n"
            "비유:\n"
            "  find      = 교실에서 안경 쓴 학생 한 명 데려오기\n"
            "  findIndex = 교실에서 안경 쓴 학생이 몇 번째 자리인지 알기\n"
            "  includes  = 교실에 홍길동이라는 학생이 있는지 확인하기\n"
            "  some      = 교실에 키 180cm 넘는 학생이 한 명이라도 있는지\n"
            "  every     = 교실 학생 모두가 교복을 입고 있는지\n"
            "\n"
            "코드 한 줄씩 읽기:\n"
            "  const nums = [4, 9, 12, 7, 20];       →  숫자 배열을 만들어요.\n"
            "  console.log(nums.find(n => n > 10));  →  10 보다 큰 첫 번째 숫자를 찾아요. 순서대로 보면 4(아님), 9(아님), 12(맞음!). 12 를 반환해요.\n"
            "  console.log(nums.findIndex(n => n > 10));  →  10 보다 큰 첫 번째 숫자의 위치를 찾아요. 12 는 인덱스 2 에 있으므로 2 를 반환해요.\n"
            "  console.log(nums.includes(7), nums.includes(3));  →  7 은 배열에 있으므로 true, 3 은 없으므로 false 예요.\n"
            "  console.log(nums.some(n => n % 2 === 0));  →  짝수인 항목이 하나라도 있나요? 4 가 짝수이므로 바로 true 를 반환해요.\n"
            "  console.log(nums.every(n => n > 0));       →  모든 항목이 0 보다 큰가요? 4,9,12,7,20 모두 양수이므로 true 예요.\n"
            "  const users = [{id:1,name:'A'},{id:2,name:'B'}];  →  객체 배열을 만들어요.\n"
            "  console.log(users.find(u => u.id === 2).name);    →  id 가 2 인 객체를 찾고, 그 객체의 name 을 꺼내요. 'B' 가 출력돼요.\n"
            "\n"
            "find vs filter 차이:\n"
            "  find   → 처음 찾은 항목 하나만 반환 (없으면 undefined)\n"
            "  filter → 조건에 맞는 모든 항목을 새 배열로 반환 (없으면 빈 배열)\n"
            "\n"
            "주의할 점:\n"
            "  빈 배열에서 some 은 false, every 는 true 를 반환해요. \"아무것도 없으면 모두 만족\"이라는 수학 논리 때문이에요.\n"
            "  find 가 아무것도 못 찾으면 undefined 를 반환해요. 바로 .name 처럼 속성에 접근하면 오류가 나요. 확인 후 사용하세요."
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
            "━━ 클래스(class)와 상속(extends)이란? ━━\n"
            "\n"
            "클래스는 같은 구조의 객체를 여러 개 만들 수 있는 \"설계도\"예요.\n"
            "비유: 붕어빵 틀(class)로 붕어빵(객체)을 여러 개 찍어낼 수 있는 것처럼요.\n"
            "각 붕어빵은 같은 모양이지만 팥소가 다를 수 있어요(= 같은 구조, 다른 데이터).\n"
            "\n"
            "상속(extends)은 기존 클래스를 기반으로 더 특화된 클래스를 만드는 거예요.\n"
            "비유: 동물(Animal) 설계도에서 강아지(Dog)는 동물의 특성을 다 물려받으면서 짖는 기능이 추가돼요.\n"
            "코드 중복 없이 \"공통 부분은 부모 클래스에, 특화 부분은 자식 클래스에\" 나눠 관리해요.\n"
            "\n"
            "constructor 는 객체를 만들 때(new 키워드 사용 시) 자동으로 실행되는 초기화 함수예요.\n"
            "super() 는 부모 클래스의 constructor 를 호출하는 거예요.\n"
            "\n"
            "코드 한 줄씩 읽기:\n"
            "  class Animal {                        →  Animal 이라는 클래스(설계도)를 만들어요.\n"
            "    constructor(name) {                 →  new Animal('개')처럼 객체를 만들 때 이 함수가 자동 실행돼요.\n"
            "      this.name = name;                 →  이 객체의 name 속성에 전달받은 name 값을 저장해요.\n"
            "    }\n"
            "    speak() {                           →  speak 메서드를 정의해요. 모든 Animal 객체가 이 메서드를 공유해요.\n"
            "      return `${this.name}가 소리낸다`; →  이 객체의 name 을 써서 문자열을 만들어요.\n"
            "    }\n"
            "  }\n"
            "  class Dog extends Animal {            →  Dog 클래스가 Animal 클래스를 상속해요. Animal 의 모든 것을 물려받아요.\n"
            "    speak() {                           →  부모의 speak() 를 \"덮어써요\"(오버라이드). Dog 만의 짖는 소리로 바꿔요.\n"
            "      return `${this.name}: 멍멍`;      →  강아지 특화 동작이에요.\n"
            "    }\n"
            "    intro() {                           →  새로운 메서드를 추가해요.\n"
            "      return super.speak();             →  super 는 부모 클래스(Animal)예요. 부모의 speak() 를 호출해요.\n"
            "    }\n"
            "  }\n"
            "  const d = new Dog('바둑이');          →  Dog 설계도로 '바둑이'라는 강아지 객체를 만들어요. Animal 의 constructor 가 실행돼요.\n"
            "  console.log(d.speak());               →  Dog 의 speak() 가 실행돼요. '바둑이: 멍멍'\n"
            "  console.log(d.intro());               →  Animal 의 speak() 가 실행돼요. '바둑이가 소리낸다'\n"
            "  console.log(d instanceof Animal);     →  d 가 Animal 의 인스턴스인지 확인해요. 상속받았으므로 true 예요.\n"
            "\n"
            "프로토타입이란?\n"
            "  메서드는 각 객체가 따로 갖지 않고 클래스의 prototype 에 한 번만 저장돼요.\n"
            "  강아지 100 마리를 만들어도 speak 함수는 메모리에 하나만 있어요. 효율적이에요!\n"
            "\n"
            "주의할 점:\n"
            "  extends 로 상속 계층을 너무 깊게 만들면 어느 클래스에서 어떤 메서드가 왔는지 파악하기 어려워요.\n"
            "  대개 2~3 단계 이상은 지양해요. 대신 필요한 기능을 직접 조합하는 방식을 선호해요."
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
            "━━ 제너레이터(Generator)란? ━━\n"
            "\n"
            "일반 함수는 호출하면 끝까지 실행되고 결과를 반환해요.\n"
            "제너레이터는 중간에 멈췄다가(yield), 필요할 때 다시 이어서 실행할 수 있는 특별한 함수예요.\n"
            "\n"
            "비유: 일반 함수는 자판기처럼 동전 넣으면 음료가 바로 나오는 것,\n"
            "제너레이터는 편의점 직원처럼 — 물건 하나 건네주고(yield) 기다리다가,\n"
            "다음 요청(next()) 이 오면 또 하나 건네주는 것과 같아요.\n"
            "\n"
            "왜 유용한가요?\n"
            "1 부터 1 억까지 숫자가 필요할 때, 미리 배열에 다 만들면 메모리가 폭발해요!\n"
            "제너레이터는 \"필요할 때 하나씩\" 만들어 주므로 메모리를 거의 안 써요.\n"
            "이걸 지연 평가(lazy evaluation)라고 해요.\n"
            "\n"
            "코드 한 줄씩 읽기:\n"
            "  function* range(start, end) {        →  function 옆에 * 를 붙이면 제너레이터 함수예요.\n"
            "    for (let i = start; i <= end; i++)  →  start 부터 end 까지 반복해요.\n"
            "      yield i;                          →  yield 는 값을 하나 내보내고 \"잠깐 멈춰요\". next() 가 올 때까지 기다려요.\n"
            "  }\n"
            "  console.log([...range(1, 5)]);        →  스프레드(...) 로 제너레이터의 모든 값을 배열로 모아요. [1,2,3,4,5]\n"
            "  function* fib() {                     →  피보나치 수열을 만드는 무한 제너레이터예요!\n"
            "    let [a, b] = [0, 1];                →  시작값 a=0, b=1 이에요.\n"
            "    while (true) {                      →  영원히 반복해요. 하지만 yield 로 멈추므로 메모리 폭발 없어요!\n"
            "      yield a;                          →  현재 a 값을 내보내고 멈춰요.\n"
            "      [a, b] = [b, a + b];              →  다음 피보나치 수를 계산해요. (0,1)→(1,1)→(1,2)→(2,3)...\n"
            "    }\n"
            "  }\n"
            "  const g = fib();                      →  제너레이터 객체를 만들어요. 아직 실행 안 해요.\n"
            "  const first6 = [];                    →  처음 6 개를 담을 배열이에요.\n"
            "  for (let i = 0; i < 6; i++)           →  6 번 반복해요.\n"
            "    first6.push(g.next().value);        →  g.next() 는 {value: 다음값, done: 완료여부} 객체를 반환해요. .value 로 숫자만 꺼내요.\n"
            "  console.log(first6);                  →  [0,1,1,2,3,5] 처음 6 개의 피보나치 수가 출력돼요.\n"
            "\n"
            "yield 와 return 차이:\n"
            "  return: 함수를 완전히 끝내고 값을 반환해요\n"
            "  yield:  값을 반환하고 \"일시정지\"해요. 다시 next() 를 부르면 거기서부터 계속돼요.\n"
            "\n"
            "주의할 점:\n"
            "  제너레이터는 일반적인 함수 흐름보다 직관적이지 않아요. 처음엔 헷갈릴 수 있어요.\n"
            "  단순히 배열을 순회하는 용도라면 그냥 for 문이나 배열 메서드가 더 읽기 쉬워요."
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
            "━━ 모듈(Module)이란? ━━\n"
            "\n"
            "코드를 여러 파일로 나눠서 관리하는 방법이에요.\n"
            "모든 코드를 하나의 파일에 다 써넣으면 파일이 수천 줄이 돼서 찾고 수정하기가 너무 힘들어요.\n"
            "기능별로 파일을 나누고(모듈화), 필요한 파일에서 가져다 쓰는(import) 방식이에요.\n"
            "\n"
            "비유: 레시피북처럼요. 파스타 레시피(파일1), 디저트 레시피(파일2)로 나눠두고,\n"
            "파티 메뉴 계획(파일3)에서 필요한 레시피를 가져다 써요.\n"
            "\n"
            "두 가지 내보내기 방법:\n"
            "  1. 이름 내보내기(named export): export const add = ...  →  import { add } from './파일'\n"
            "  2. 기본 내보내기(default export): export default PI      →  import PI from './파일' (이름은 마음대로)\n"
            "\n"
            "코드 한 줄씩 읽기(아래는 한 파일에서 모듈 동작을 흉내낸 코드예요):\n"
            "  // 실제로는 파일이 나뉘지만, 데모는 한 파일에서 동작을 흉내냅니다.\n"
            "  // math.js  ->  export const add = (a,b)=>a+b;  export default PI;\n"
            "  // main.js  ->  import PI, { add } from './math.js';\n"
            "  const mathModule = (() => {          →  즉시실행함수(IIFE)로 모듈 캡슐화를 흉내내요.\n"
            "    const add = (a, b) => a + b;       →  내부에서만 쓰는 add 함수예요 (export 될 것)\n"
            "    const PI = 3.14;                   →  내부에서만 쓰는 PI 상수예요 (default export 될 것)\n"
            "    return { add, default: PI };       →  외부에 공개할 것들을 반환해요. 이게 export 흉내예요.\n"
            "  })();                                →  즉시 실행해서 mathModule 에 결과를 저장해요.\n"
            "  const { add, default: PI } = mathModule;  →  mathModule 에서 add 와 PI(default 로 이름 바꿔)를 꺼내요. import 흉내예요.\n"
            "  console.log(add(2, 3), PI);          →  5 와 3.14 가 출력돼요.\n"
            "  console.log('모듈 = 파일 단위 캡슐화 + 재사용');  →  모듈의 핵심 개념을 출력해요.\n"
            "\n"
            "실제 파일에서는 이렇게 써요:\n"
            "  // math.js\n"
            "  export const add = (a, b) => a + b;  // 이름 내보내기\n"
            "  export default 3.14;                  // 기본 내보내기\n"
            "\n"
            "  // main.js\n"
            "  import PI, { add } from './math.js'; // PI 는 default, add 는 이름으로 가져와요\n"
            "\n"
            "주의할 점:\n"
            "  ES 모듈(.mjs 또는 package.json 에 type:\"module\" 설정)과 CommonJS(require) 는 섞어 쓰면 오류가 나요.\n"
            "  모듈이 서로 순환 참조(A 가 B 를 가져오고, B 가 A 를 가져오면)하면 값이 undefined 가 될 수 있어요."
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
            "━━ 이터러블(Iterable)과 심볼(Symbol)이란? ━━\n"
            "\n"
            "이터러블은 \"for...of 로 순회할 수 있는 객체\"를 말해요.\n"
            "배열, 문자열, Map, Set 은 기본적으로 이터러블이에요.\n"
            "우리가 직접 만든 객체도 이터러블로 만들 수 있어요!\n"
            "\n"
            "심볼(Symbol)은 절대로 겹치지 않는 유일한 값이에요.\n"
            "비유: 세상 모든 사람의 지문이 다르듯, Symbol() 로 만든 값은 각각 유일해요.\n"
            "Symbol.iterator 는 JavaScript 가 미리 정해놓은 특별한 심볼이에요.\n"
            "이걸 객체에 구현하면 for...of, 스프레드, 구조분해를 모두 쓸 수 있어요.\n"
            "\n"
            "이터레이터 프로토콜:\n"
            "  객체에 [Symbol.iterator]() 메서드를 만들어야 해요.\n"
            "  이 메서드는 { next() } 를 가진 객체를 반환해야 해요.\n"
            "  next() 는 { value: 현재값, done: 완료여부 } 형태의 객체를 반환해야 해요.\n"
            "  done 이 true 가 되면 반복이 끝나요.\n"
            "\n"
            "코드 한 줄씩 읽기:\n"
            "  const sym = Symbol('id');              →  'id' 라는 설명을 가진 유일한 심볼을 만들어요. 매번 다른 값이 돼요.\n"
            "  const obj = { [sym]: 100, name: 'x' };  →  심볼을 키로 사용해서 속성을 만들어요. [sym] 이라고 대괄호로 감싸야 해요.\n"
            "  console.log(obj[sym]);                  →  심볼 키로 값을 읽어요. 100 이 출력돼요.\n"
            "  const countTo = {                       →  이터러블 객체를 만들어요.\n"
            "    limit: 3,                             →  3 까지 세는 객체예요.\n"
            "    [Symbol.iterator]() {                 →  Symbol.iterator 메서드를 구현해요. 이 객체를 이터러블로 만드는 핵심이에요.\n"
            "      let i = 0, limit = this.limit;      →  현재 카운터 i 와 최대값 limit 를 설정해요.\n"
            "      return {                            →  이터레이터 객체를 반환해요.\n"
            "        next: () => i < limit             →  i 가 limit 보다 작으면...\n"
            "          ? { value: ++i, done: false }   →  i 를 1 늘리고 그 값을 내보내요. done: false 는 아직 안 끝났다는 뜻이에요.\n"
            "          : { value: undefined, done: true }  →  다 셌으면 done: true 로 끝을 알려요.\n"
            "      };\n"
            "    },\n"
            "  };\n"
            "  console.log([...countTo]);             →  스프레드 연산자가 이터러블을 다 순회해서 배열로 만들어요. [1,2,3]\n"
            "  for (const v of countTo)              →  for...of 로 순회해요.\n"
            "    process.stdout.write(v + ' ');       →  1 2 3 이 차례로 출력돼요.\n"
            "\n"
            "왜 심볼을 키로 쓰나요?\n"
            "  일반 키 이름은 다른 코드와 충돌할 수 있어요.\n"
            "  Symbol 은 절대 같은 값이 없으므로, 충돌 걱정 없이 내부 동작을 정의할 수 있어요.\n"
            "\n"
            "주의할 점:\n"
            "  Symbol 키는 Object.keys(), JSON.stringify() 에서 빠져요. 의도적으로 숨기는 용도로 활용해요.\n"
            "  직접 Symbol.iterator 를 구현하는 건 복잡해요. 제너레이터(function*) 를 쓰면 훨씬 간단해요."
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
            "━━ 함수형 패턴이란? ━━\n"
            "\n"
            "함수형 프로그래밍은 작은 함수들을 레고 블록처럼 조합해서 복잡한 작업을 처리하는 스타일이에요.\n"
            "\n"
            "pipe (파이프):\n"
            "  데이터가 여러 함수를 \"왼쪽에서 오른쪽으로\" 차례로 통과해요.\n"
            "  비유: 공장의 컨베이어 벨트처럼 — 원자재가 단계1 → 단계2 → 단계3 을 거쳐 완제품이 돼요.\n"
            "\n"
            "compose (컴포즈):\n"
            "  pipe 와 같지만 \"오른쪽에서 왼쪽으로\" 함수가 적용돼요. 수학의 합성함수와 같아요.\n"
            "\n"
            "curry (커링):\n"
            "  인자가 여러 개인 함수를 인자 하나씩 받는 함수들로 분리하는 거예요.\n"
            "  비유: 커피숍에서 \"아이스 → 아메리카노 → 샷 추가\"처럼 단계적으로 옵션을 선택하는 것과 같아요.\n"
            "  add(1, 2, 3) 대신 add(1)(2)(3) 처럼 하나씩 넣는 거예요.\n"
            "\n"
            "코드 한 줄씩 읽기:\n"
            "  const pipe = (...fns) => x => fns.reduce((acc, fn) => fn(acc), x);\n"
            "    →  fns 는 함수 배열, x 는 초기값. reduce 로 함수를 차례로 적용해요. 왼→오 순서예요.\n"
            "  const compose = (...fns) => x => fns.reduceRight((acc, fn) => fn(acc), x);\n"
            "    →  reduceRight 로 오른쪽부터 적용해요. 오→왼 순서예요.\n"
            "  const inc = n => n + 1;               →  n 에 1 을 더하는 함수예요.\n"
            "  const dbl = n => n * 2;               →  n 을 2 배 하는 함수예요.\n"
            "  console.log(pipe(inc, dbl)(5));        →  pipe: 먼저 inc(5)=6, 그다음 dbl(6)=12. 왼→오이므로 inc 먼저 실행해요.\n"
            "  console.log(compose(inc, dbl)(5));     →  compose: 먼저 dbl(5)=10, 그다음 inc(10)=11. 오→왼이므로 dbl 먼저 실행해요.\n"
            "  const curry = a => b => c => a + b + c;  →  a 를 받으면 b 를 기다리는 함수를, b 를 받으면 c 를 기다리는 함수를 반환해요.\n"
            "  const add10 = curry(10);              →  a=10 으로 고정한 함수를 만들어요. 아직 b, c 가 필요해요.\n"
            "  console.log(add10(20)(3));             →  add10(20) 은 a=10, b=20. 그다음 (3) 은 c=3. 10+20+3=33 이에요.\n"
            "  const nums = [1, 2, 3, 4];            →  처리할 숫자 배열이에요.\n"
            "  console.log(pipe(\n"
            "    arr => arr.filter(n => n % 2 === 0),  →  짝수만 골라요: [2, 4]\n"
            "    arr => arr.map(dbl),                   →  각 항목을 2 배 해요: [4, 8]\n"
            "  )(nums));                               →  [4, 8] 이 출력돼요. 배열이 두 단계 변환을 거쳐요.\n"
            "\n"
            "왜 함수형 패턴을 쓰나요?\n"
            "  작은 함수들(inc, dbl, filter...)은 독립적이라 각각 테스트하기 쉬워요.\n"
            "  pipe/compose 로 조합하면 복잡한 변환도 읽는 순서대로 이해할 수 있어요.\n"
            "  커링으로 미리 설정을 고정한 특화 함수를 만들 수 있어요 (add10, add20 등).\n"
            "\n"
            "주의할 점:\n"
            "  처음 보면 화살표 함수가 중첩되어 있어서 읽기 어려워요. 천천히 한 단계씩 풀어서 이해하세요.\n"
            "  단순한 작업에 함수형 패턴을 억지로 쓰면 오히려 코드가 더 복잡해져요."
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
