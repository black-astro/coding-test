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
            "if / else if / else 로 조건에 따라 분기한다. 조건에는 비교(===, <, > 등) 결과가 들어간다.\n"
            "삼항 연산자 조건 ? a : b 는 값 하나를 고르는 짧은 분기에 쓴다.\n"
            "논리연산자 &&(그리고)·||(또는)·!(부정)와, 좌변이 null/undefined 일 때만 우변을 쓰는 ??(널 병합)가 있다."
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
            "for (초기식; 조건; 증감) 는 횟수가 정해진 반복에, while 은 조건이 참인 동안 반복할 때 쓴다.\n"
            "for...of 는 배열·문자열 같은 이터러블의 값을 순서대로 꺼낸다(인덱스가 필요 없을 때 깔끔).\n"
            "break 로 반복을 즉시 멈추고, continue 로 현재 회차만 건너뛴다."
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
            "switch(값) 는 값을 각 case 와 === 로 비교해 일치하는 분기를 실행한다.\n"
            "각 case 끝에 break 가 없으면 다음 case 로 흘러내린다(fall-through). 의도적으로 묶을 때 활용한다.\n"
            "어느 case 와도 맞지 않으면 default 가 실행된다."
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
            "백틱(`)으로 감싼 문자열 안에서 ${표현식} 으로 변수·연산 결과를 끼워 넣는다.\n"
            "줄바꿈을 그대로 포함할 수 있어 여러 줄 문자열을 작은따옴표 \\n 없이 작성한다.\n"
            "${} 안에는 변수뿐 아니라 함수 호출·삼항 등 어떤 표현식도 넣을 수 있다."
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
            "Number(x)·String(x)·Boolean(x) 로 명시적으로 타입을 바꾼다. parseInt/parseFloat 는 앞부분 숫자만 파싱한다.\n"
            "조건문에서 값은 자동으로 boolean 으로 평가된다. falsy 값은 false, 0, '', null, undefined, NaN 6가지뿐이고 나머지는 truthy 다.\n"
            "!!x 는 값을 boolean 으로 빠르게 변환하는 관용구다."
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
            "객체 안에 함수를 넣으면 메서드가 된다. { greet() { ... } } 단축 문법을 쓴다.\n"
            "메서드 안의 this 는 그 메서드를 '호출한 객체'를 가리킨다(obj.method() 이면 this===obj).\n"
            "화살표함수는 자신의 this 가 없어 바깥 this 를 그대로 쓴다 — 메서드 본체로는 부적합하다."
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
            "오류가 날 수 있는 코드를 try 블록에 넣고, 발생한 예외를 catch(e) 에서 받아 처리한다.\n"
            "throw new Error('메시지') 로 직접 예외를 던질 수 있다. e.message 로 내용을 읽는다.\n"
            "finally 블록은 성공·실패와 상관없이 항상 실행된다(자원 정리에 사용)."
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
            "JSON.stringify(값) 는 객체·배열을 JSON 문자열로 직렬화한다. 세 번째 인자로 들여쓰기 칸 수를 준다.\n"
            "JSON.parse(문자열) 는 JSON 문자열을 다시 객체로 되돌린다(역직렬화).\n"
            "함수·undefined·심볼은 직렬화에서 빠지고, Map/Set 은 일반 객체/배열로 변환해야 한다."
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
            "Date 객체로 날짜·시간을 다룬다. new Date(연,월,일) 에서 월은 0부터 시작(0=1월)한다.\n"
            "getTime() 은 1970년 기준 밀리초 값이라, 두 날짜의 차를 빼서 경과 시간을 계산한다.\n"
            "setTimeout(콜백, ms) 는 지정한 시간 뒤에 콜백을 한 번 실행한다(비동기)."
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
            "find 는 조건을 처음 만족하는 '원소'를, findIndex 는 그 '인덱스'를 반환한다(없으면 undefined / -1).\n"
            "includes 는 특정 값이 배열에 있는지 boolean 으로 알려준다(indexOf 보다 의도가 분명).\n"
            "some 은 하나라도 조건을 만족하면 true, every 는 모두 만족해야 true 다."
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
            "class 는 프로토타입 기반 상속을 더 읽기 쉽게 감싼 문법이다. constructor 에서 인스턴스 속성을 초기화한다.\n"
            "메서드는 프로토타입에 한 번만 저장돼 모든 인스턴스가 공유한다(메모리 효율적).\n"
            "extends 로 상속하고 super(...) 로 부모 생성자/메서드를 호출한다."
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
            "function* 로 정의한 제너레이터는 yield 에서 멈췄다가 next() 호출 때마다 다음 값을 내놓는다.\n"
            "값을 한 번에 다 만들지 않고 필요할 때 하나씩 생성하므로(지연 평가) 무한 수열도 표현할 수 있다.\n"
            "제너레이터는 이터러블이라 for...of, 스프레드(...)와 함께 쓸 수 있다."
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
            "ES 모듈은 export 로 값을 공개하고 import 로 다른 파일에서 가져온다. 파일마다 독립 스코프를 가진다.\n"
            "이름 내보내기 export const x 는 import { x } 로, 기본 내보내기 export default 는 import 임의이름 으로 받는다.\n"
            "Node 의 전통 방식 CommonJS 는 module.exports 와 require() 를 쓴다(아래는 한 파일 내 시뮬레이션)."
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
            "Symbol 은 유일무이한 값으로, 충돌하지 않는 키나 내장 동작 지정에 쓴다(Symbol.iterator 등).\n"
            "객체에 [Symbol.iterator]() 메서드를 정의해 { next() { value, done } } 를 반환하면 그 객체는 이터러블이 된다.\n"
            "이터러블이 되면 for...of, 스프레드(...), 구조분해를 그대로 쓸 수 있다."
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
            "함수 합성(compose) 은 여러 함수를 하나로 엮어, 오른쪽 함수의 결과를 왼쪽 함수에 넘긴다.\n"
            "pipe 는 반대로 왼쪽에서 오른쪽으로 데이터를 흘려보내 읽는 순서대로 변환한다.\n"
            "커링(curry) 은 다중 인자 함수를 인자 하나씩 받는 함수들로 쪼개, 일부만 적용한 함수를 만들 수 있게 한다."
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
