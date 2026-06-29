"""JavaScript 문법 학습 (기초·중급·고급, 각 3개씩 총 9개).

각 Lesson 의 code 는 Node.js 로 그대로 실행되는 완전한 스크립트다.
표준입력 없이 고정값으로 시연하며 console.log 로 결과를 출력한다.
"""

from engine.models import Lesson

LESSONS = [

    # ===================== 기초 =====================
    Lesson(
        id="js-basic-01-var",
        lang="javascript", level="기초",
        title="변수(let/const)와 자료형",
        summary="let·const · typeof · 형변환",
        explanation=(
            "변수는 let(재할당 가능)과 const(재할당 불가)로 선언한다. var 는 함수 스코프라 권장하지 않는다.\n"
            "기본 자료형은 number, string, boolean, undefined, null, symbol, bigint 이다.\n"
            "typeof x 로 타입을 확인하고, Number()/String()/parseInt() 로 형변환한다."
        ),
        usage="값 저장의 기본. 코딩테스트에서 입력 문자열을 Number()/parseInt() 로 숫자로 바꿀 때 핵심.",
        cons="== 는 느슨한 비교라 타입을 자동 변환하니 항상 === 를 쓴다. const 객체는 내부 속성은 바뀔 수 있다.",
        code=(
            "const a = 10;          // number\n"
            "let b = 3.14;          // number (정수/실수 구분 없음)\n"
            "const name = '홍길동';  // string\n"
            "const flag = true;     // boolean\n"
            "console.log(typeof a, typeof name, typeof flag);\n"
            "console.log(a + Number('5'));   // 형변환 후 덧셈 -> 15\n"
            "console.log(name.repeat(2));    // 문자열 반복 -> 홍길동홍길동\n"
            "console.log(1 === 1, 1 == '1', 1 === '1'); // true true false\n"
        ),
    ),

    Lesson(
        id="js-basic-02-array",
        lang="javascript", level="기초",
        title="배열과 메서드(map/filter/forEach)",
        summary="배열 · map · filter · forEach",
        explanation=(
            "배열은 [] 로 만들고 push/pop 으로 끝에서 추가·제거한다.\n"
            "map 은 각 원소를 변환한 새 배열을, filter 는 조건을 통과한 원소만 모은 새 배열을 반환한다.\n"
            "forEach 는 반환값 없이 각 원소에 대해 부수효과(출력 등)를 실행한다."
        ),
        usage="배열 변환·선별에 가장 많이 쓴다. map/filter 는 반복문보다 의도가 분명해 가독성이 좋다.",
        cons="map/filter 는 매번 새 배열을 만들어 메모리를 더 쓴다. 대용량은 단순 for 가 더 빠를 수 있다.",
        code=(
            "const a = [5, 2, 9, 1];\n"
            "a.push(7);\n"
            "console.log(a, a.slice(1, 3), [...a].reverse());\n"
            "const squares = [1, 2, 3, 4, 5].map(x => x * x);\n"
            "console.log(squares);                 // [1,4,9,16,25]\n"
            "const evens = a.filter(x => x % 2 === 0);\n"
            "console.log(evens);                   // [2]\n"
            "a.forEach((v, i) => console.log(i, v));\n"
        ),
    ),

    Lesson(
        id="js-basic-03-object",
        lang="javascript", level="기초",
        title="객체와 구조분해",
        summary="객체 리터럴 · 구조분해 · 단축 속성",
        explanation=(
            "객체는 { 키: 값 } 형태의 키-값 묶음이다. obj.key 또는 obj['key'] 로 접근한다.\n"
            "구조분해 const { a, b } = obj 로 속성을 한 번에 변수로 꺼낸다(기본값·이름변경 가능).\n"
            "Object.keys/values/entries 로 키·값·쌍 목록을 배열로 얻는다."
        ),
        usage="데이터 묶음 표현과 함수 인자 전달에 필수. 구조분해는 코드량을 크게 줄여준다.",
        cons="객체 키 순회 순서는 보장이 약하다(숫자 키는 오름차순). 깊은 복사는 직접 처리해야 한다.",
        code=(
            "const user = { name: '김철수', age: 20, city: '서울' };\n"
            "const { name, age } = user;        // 구조분해\n"
            "console.log(name, age);            // 김철수 20\n"
            "const score = 95;\n"
            "const result = { name, score };    // 단축 속성\n"
            "console.log(result);\n"
            "console.log(Object.keys(user));    // ['name','age','city']\n"
            "console.log(Object.entries(user));\n"
        ),
    ),

    # ===================== 중급 =====================
    Lesson(
        id="js-mid-01-func",
        lang="javascript", level="중급",
        title="함수·화살표함수·클로저",
        summary="함수 선언 · 화살표 · 클로저",
        explanation=(
            "함수는 function 선언식 또는 화살표함수 (a, b) => a + b 로 만든다.\n"
            "화살표함수는 자신만의 this 가 없어 콜백에 적합하고 문법이 짧다.\n"
            "클로저: 함수가 바깥 스코프의 변수를 기억해, 호출 사이에 상태를 유지한다."
        ),
        usage="콜백·고차함수에 화살표함수, 상태를 감추는 카운터·메모이제이션에 클로저를 쓴다.",
        cons="화살표함수는 this/arguments 가 없어 메서드나 생성자로는 부적합하다. 클로저는 변수를 붙잡아 메모리 누수가 될 수 있다.",
        code=(
            "function add(a, b = 10) { return a + b; }\n"
            "const mul = (a, b) => a * b;\n"
            "console.log(add(5), mul(3, 4));   // 15 12\n"
            "function makeCounter() {\n"
            "  let count = 0;                  // 클로저로 보존되는 상태\n"
            "  return () => ++count;\n"
            "}\n"
            "const next = makeCounter();\n"
            "console.log(next(), next(), next()); // 1 2 3\n"
        ),
    ),

    Lesson(
        id="js-mid-02-mapset",
        lang="javascript", level="중급",
        title="Map과 Set",
        summary="Map 해시맵 · Set 중복제거",
        explanation=(
            "Map 은 임의 타입의 키를 가지는 키-값 저장소로 set/get/has/size 를 쓴다.\n"
            "Set 은 중복 없는 값의 집합으로 add/has/delete 와 size 를 제공한다.\n"
            "둘 다 삽입 순서를 유지하며 for...of 로 순회한다(객체보다 키 관리에 안전)."
        ),
        usage="빈도수 세기·중복 제거·존재 여부 확인에 핵심. 배열 중복 제거는 [...new Set(arr)] 가 간단하다.",
        cons="JSON 으로 직렬화하면 일반 객체/배열로 변환해야 한다. 작은 데이터는 일반 객체가 더 가벼울 수 있다.",
        code=(
            "const freq = new Map();\n"
            "for (const ch of 'banana') {\n"
            "  freq.set(ch, (freq.get(ch) || 0) + 1);\n"
            "}\n"
            "console.log([...freq.entries()]);   // [['b',1],['a',3],['n',2]]\n"
            "const s = new Set([1, 2, 2, 3, 3, 3]);\n"
            "console.log(s.size, s.has(2));       // 3 true\n"
            "console.log([...new Set([5, 5, 1, 1, 9])]); // [5,1,9]\n"
        ),
    ),

    Lesson(
        id="js-mid-03-string",
        lang="javascript", level="중급",
        title="문자열 처리와 정규식",
        summary="문자열 메서드 · 정규식 · match",
        explanation=(
            "문자열은 불변이며 split/join/slice/replace/trim 등으로 다룬다.\n"
            "정규식 /패턴/플래그 로 검색·치환한다. g(전역), i(대소문자 무시) 플래그가 흔하다.\n"
            "match/matchAll 로 일치 부분을, replace 로 패턴 치환을, test 로 일치 여부를 확인한다."
        ),
        usage="입력 파싱(split), 출력 조립(join), 숫자/단어 추출 같은 패턴 처리에 필수.",
        cons="문자열 += 반복 연결은 느릴 수 있어 배열에 모아 join 하는 게 낫다. 복잡한 정규식은 가독성을 해친다.",
        code=(
            "const s = '  Hello, World  ';\n"
            "console.log(s.trim().toUpperCase());     // 'HELLO, WORLD'\n"
            "console.log('a,b,c'.split(','));         // ['a','b','c']\n"
            "console.log(['2024','01','15'].join('-')); // '2024-01-15'\n"
            "const text = '주문 12개, 재고 345개';\n"
            "const nums = text.match(/\\d+/g).map(Number);\n"
            "console.log(nums);                       // [12, 345]\n"
            "console.log('banana'.replace(/a/g, '*')); // 'b*n*n*'\n"
        ),
    ),

    # ===================== 고급 =====================
    Lesson(
        id="js-adv-01-async",
        lang="javascript", level="고급",
        title="비동기 처리(async/await·Promise)",
        summary="Promise · async/await · 즉시실행",
        explanation=(
            "Promise 는 미래에 완료될 작업을 나타낸다. resolve 로 성공값을 전달한다.\n"
            "async 함수 안에서 await 로 Promise 가 끝날 때까지 기다려 값을 받는다(동기처럼 작성).\n"
            "최상위에서 await 를 쓰려면 (async () => { ... })() 즉시실행 함수로 감싼다."
        ),
        usage="네트워크 요청·타이머·파일 입출력 등 시간이 걸리는 작업을 막힘 없이 처리할 때 쓴다.",
        cons="에러는 try/catch 로 잡아야 한다(미처리 시 unhandled rejection). 순차 await 남용은 느려질 수 있어 Promise.all 로 병렬화한다.",
        code=(
            "function delay(value, ms) {\n"
            "  return new Promise(resolve => setTimeout(() => resolve(value), ms));\n"
            "}\n"
            "(async () => {\n"
            "  const a = await delay('첫번째', 10);\n"
            "  console.log(a);\n"
            "  const [x, y] = await Promise.all([delay(1, 5), delay(2, 5)]); // 병렬\n"
            "  console.log('합:', x + y);   // 합: 3\n"
            "})();\n"
        ),
    ),

    Lesson(
        id="js-adv-02-spread",
        lang="javascript", level="고급",
        title="구조분해·스프레드·고차함수",
        summary="스프레드(...) · rest · 고차함수",
        explanation=(
            "스프레드 ...arr 는 배열/객체를 펼쳐 복사·병합하고, rest 매개변수는 나머지 인자를 배열로 모은다.\n"
            "구조분해에 기본값·나머지를 결합하면 데이터를 유연하게 꺼낸다.\n"
            "고차함수는 함수를 인자로 받거나 함수를 반환한다(map/filter 콜백, 함수 합성)."
        ),
        usage="불변 복사·배열 병합, 가변 인자 함수, 함수 합성/커링 등 함수형 패턴에 두루 쓴다.",
        cons="스프레드 복사는 얕은 복사라 중첩 객체는 공유된다. 큰 배열을 매번 펼치면 비용이 든다.",
        code=(
            "const a = [1, 2], b = [3, 4];\n"
            "console.log([...a, ...b]);          // [1,2,3,4]\n"
            "const base = { x: 1, y: 2 };\n"
            "console.log({ ...base, y: 20, z: 3 }); // {x:1,y:20,z:3}\n"
            "const sum = (...nums) => nums.reduce((s, n) => s + n, 0);\n"
            "console.log(sum(1, 2, 3, 4));        // 10\n"
            "const apply = (fn, ...args) => fn(...args); // 고차함수\n"
            "console.log(apply(Math.max, 3, 9, 1)); // 9\n"
        ),
    ),

    Lesson(
        id="js-adv-03-reduce",
        lang="javascript", level="고급",
        title="reduce·sort 비교자와 입력 읽기",
        summary="reduce 누적 · sort 비교함수 · readFileSync",
        explanation=(
            "reduce(콜백, 초기값) 는 배열을 하나의 값(합계·객체·그룹)으로 누적한다.\n"
            "sort 는 기본이 문자열 정렬이라 숫자는 sort((a,b)=>a-b) 처럼 비교자를 넘겨야 한다.\n"
            "코딩테스트 입력은 require('fs').readFileSync(0, 'utf8') 로 표준입력 전체를 한 번에 읽는다."
        ),
        usage="합계·빈도 집계는 reduce, 다중 기준 정렬은 sort 비교자. 백준식 입력은 readFileSync 로 빠르게 읽는다.",
        cons="sort 비교자가 number 가 아닌 boolean 을 반환하면 정렬이 깨진다(반드시 음수/0/양수). reduce 초기값 누락은 버그의 흔한 원인이다.",
        code=(
            "const arr = [5, 2, 9, 1, 7];\n"
            "const total = arr.reduce((s, n) => s + n, 0);\n"
            "console.log('합계', total);          // 합계 24\n"
            "console.log([...arr].sort((a, b) => a - b)); // 오름차순 [1,2,5,7,9]\n"
            "const people = [{n:'A',age:30},{n:'B',age:20},{n:'C',age:30}];\n"
            "people.sort((p, q) => q.age - p.age || p.n.localeCompare(q.n));\n"
            "console.log(people.map(p => p.n));   // 나이 내림차순, 동률은 이름순\n"
            "// 실전 입력 예시(데모는 고정 문자열로 대체):\n"
            "// const input = require('fs').readFileSync(0, 'utf8').trim().split('\\n');\n"
            "const input = '3\\n10 20 30'.split('\\n');\n"
            "const n = Number(input[0]);\n"
            "const nums = input[1].split(' ').map(Number);\n"
            "console.log(n, nums, nums.reduce((s, v) => s + v, 0)); // 3 [10,20,30] 60\n"
        ),
    ),
]
