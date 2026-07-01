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
            "[개요]\n"
            "변수는 값을 저장하는, 이름이 부여된 메모리 공간이다.\n"
            "JavaScript에서 변수를 선언하는 방식은 세 가지이다.\n"
            "  • let   → 이후 값을 재할당할 수 있는 변수 (예: 점수, 상태)\n"
            "  • const → 한 번 할당하면 재할당할 수 없는 상수 (예: 이름, 고정 설정값)\n"
            "  • var   → 구식 방식으로, 스코프 동작이 비직관적이어서 현재는 거의 사용하지 않는다.\n"
            "\n"
            "[핵심 개념]\n"
            "자료형은 변수에 저장할 수 있는 값의 종류를 의미한다.\n"
            "  • number    → 숫자. 정수와 실수를 구분하지 않고 모두 number로 취급한다(파이썬의 int/float 구분이 없다).\n"
            "  • string    → 문자, 문자열. 따옴표로 감싼다.\n"
            "  • boolean   → 참(true) 또는 거짓(false) 두 가지 값만 가진다.\n"
            "  • undefined → 변수를 선언했으나 값을 할당하지 않은 상태.\n"
            "  • null      → 의도적으로 '비어 있음'을 표시한 상태(undefined와는 구분된다).\n"
            "\n"
            "[코드 분석]\n"
            "  • const a = 10;           → 상수 a를 선언하고 숫자 10으로 초기화한다. 이후 a = 20으로 재할당하면 오류가 발생한다.\n"
            "  • let b = 3.14;           → 재할당 가능한 변수 b에 실수 3.14를 할당한다.\n"
            "  • const name = '홍길동';   → 문자열 '홍길동'을 name에 할당한다.\n"
            "  • const flag = true;      → 참(true) 값을 flag에 할당한다.\n"
            "  • typeof a                → a에 저장된 값의 자료형을 반환한다. 결과는 'number'이다.\n"
            "  • Number('5')             → 문자열 '5'를 숫자 5로 변환한다. 문자와 숫자를 연산할 때 필요하다.\n"
            "  • a + Number('5')         → 10 + 5 = 15가 된다. Number() 없이 a + '5'를 수행하면 '105'(문자열 연결)가 된다.\n"
            "  • name.repeat(2)          → '홍길동'을 2회 반복하여 '홍길동홍길동'을 생성한다.\n"
            "  • 1 === '1'               → 숫자 1과 문자열 '1'은 타입이 다르므로 false를 반환한다.\n"
            "  • 1 == '1'                → ==는 타입을 자동 변환하여 비교하므로 true를 반환한다(혼동을 유발하므로 사용을 지양한다).\n"
            "\n"
            "[유의 사항]\n"
            "  • 코딩테스트에서 입력값은 항상 문자열로 들어온다.\n"
            "  • '10' + '20'은 '1020'(문자열 연결)이 되어 오답의 원인이 된다.\n"
            "  • 따라서 Number() 또는 parseInt()로 숫자로 변환해야 한다.\n"
            "  • == 대신 === 사용을 습관화한다. 타입까지 비교하므로 더 안전하다."
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
            "[개요]\n"
            "배열(Array)은 여러 개의 값을 순서대로 저장하는 자료구조이다.\n"
            "각 항목은 인덱스(번호)로 접근하며, JavaScript의 인덱스는 0부터 시작한다. 첫 번째 항목은 arr[0]이다.\n"
            "\n"
            "[핵심 개념]\n"
            "배열을 다루는 대표 메서드는 다음과 같다.\n"
            "  • map     → 변환. 모든 항목을 변환하여 새 배열을 생성한다(예: 모든 점수를 2배로).\n"
            "  • filter  → 선별. 조건에 맞는 항목만 골라 새 배열을 생성한다(예: 짝수만 추출).\n"
            "  • forEach → 반복. 각 항목에 대해 특정 작업을 실행하며, 새 배열을 생성하지 않는다(예: 전체 출력).\n"
            "\n"
            "for문 대신 map/filter를 사용하는 이유는 의도가 명확하게 드러나 가독성이 높기 때문이다.\n"
            "for문은 배열을 순회하며 새 배열에 값을 채우는 절차가 길어지지만, map은 각 원소의 변환 규칙만 기술하면 된다.\n"
            "\n"
            "[코드 분석]\n"
            "  • const a = [5, 2, 9, 1];      → 숫자 4개를 가진 배열 a를 생성한다.\n"
            "  • a.push(7);                   → 배열 끝에 7을 추가한다. 결과는 [5,2,9,1,7]이다.\n"
            "  • a.slice(1, 3)                → 인덱스 1부터 3 직전(2)까지를 잘라 [2,9]를 반환한다.\n"
            "  • [...a].reverse()             → a를 복사(...)한 뒤 뒤집는다. 원본 a는 변경되지 않는다.\n"
            "  • [1,2,3,4,5].map(x => x * x)  → 각 숫자를 제곱하여 새 배열 [1,4,9,16,25]를 생성한다.\n"
            "  • a.filter(x => x % 2 === 0)   → 짝수인 항목만 골라 새 배열을 생성한다.\n"
            "  • a.forEach((v, i) => ...)     → v는 값(value), i는 인덱스(index)이다. 각 항목을 순서대로 처리한다.\n"
            "\n"
            "[유의 사항]\n"
            "  • map과 filter는 항상 새 배열을 생성하며 원본 배열을 변경하지 않는다.\n"
            "  • 배열 인덱스는 0부터 시작하므로, 4개짜리 배열의 마지막 원소는 arr[3]이다.\n"
            "  • push는 원본을 변경하지만 map/filter는 원본을 변경하지 않는다. 이 차이에 유의한다."
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
            "[개요]\n"
            "객체(Object)는 키(이름표)와 값의 쌍으로 데이터를 묶어 표현하는 자료구조이다.\n"
            "예를 들어 한 사람의 정보를 표현할 때 배열과 객체를 비교하면 다음과 같다.\n"
            "  • 배열: [\"김철수\", 20, \"서울\"]                        → 순서로 구분하므로 각 값의 의미가 모호하다.\n"
            "  • 객체: { name: \"김철수\", age: 20, city: \"서울\" }  → 키가 있어 각 값의 의미가 명확하다.\n"
            "값은 obj.name 또는 obj['name'] 두 가지 방식으로 접근한다.\n"
            "\n"
            "[핵심 개념]\n"
            "구조분해(Destructuring)는 객체에서 여러 값을 한 번에 꺼내는 문법이다.\n"
            "  • 일반 방식:\n"
            "      const name = user.name;   // 한 줄씩 개별 추출\n"
            "      const age = user.age;\n"
            "  • 구조분해:\n"
            "      const { name, age } = user;  // 한 줄로 여러 값을 동시에 추출\n"
            "\n"
            "[코드 분석]\n"
            "  • const user = { name: '김철수', age: 20, city: '서울' };\n"
            "      → 세 가지 정보를 가진 user 객체를 생성한다. 키-값 쌍으로 구성된다.\n"
            "  • const { name, age } = user;\n"
            "      → user 객체에서 name과 age를 추출하여 변수로 만든다(구조분해).\n"
            "  • console.log(name, age);\n"
            "      → '김철수 20'을 출력한다.\n"
            "  • const score = 95;\n"
            "      → score 변수에 95를 할당한다.\n"
            "  • const result = { name, score };\n"
            "      → 단축 속성이다. { name: name, score: score }와 동일하다.\n"
            "        변수명과 키명이 같으면 축약할 수 있다.\n"
            "  • Object.keys(user)\n"
            "      → user 객체의 키들을 배열로 반환한다: ['name', 'age', 'city'].\n"
            "  • Object.entries(user)\n"
            "      → [키, 값] 쌍을 배열로 반환한다: [['name','김철수'], ['age',20], ...].\n"
            "\n"
            "[유의 사항]\n"
            "  • const로 선언한 객체는 재할당은 불가능하지만 내부 값 변경은 가능하다.\n"
            "      const user = { age: 20 };\n"
            "      user.age = 21;   // 허용됨. 객체 내부 변경은 가능하다.\n"
            "      user = {};       // 오류. 객체 자체의 재할당은 금지된다.\n"
            "  • { ...obj }로 객체를 복사하면 얕은 복사가 되어 중첩된 객체는 공유된다."
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
            "[개요]\n"
            "함수는 반복 사용할 코드 묶음에 이름을 부여한 것으로, 한 번 작성한 뒤 이름으로 여러 번 호출한다.\n"
            "\n"
            "[함수 선언 방식]\n"
            "  • 방법 1: function 선언식\n"
            "      function add(a, b) { return a + b; }\n"
            "  • 방법 2: 화살표 함수(Arrow Function)\n"
            "      const add = (a, b) => a + b;\n"
            "  화살표 함수는 더 간결하게 작성할 수 있으며, return과 중괄호 {}를 생략할 수 있다.\n"
            "\n"
            "[기본값 매개변수]\n"
            "  function add(a, b = 10) { return a + b; }\n"
            "  add(5)처럼 b를 전달하지 않으면 자동으로 b = 10이 적용된다. 이를 디폴트 값이라 하며, 자주 쓰는 값을 미리 지정할 때 사용한다.\n"
            "\n"
            "[클로저]\n"
            "클로저(Closure)는 함수가 자신을 감싼 바깥 변수를 기억하는 특성이다.\n"
            "makeCounter() 함수는 count 변수를 가진 공간을 만들고, 그 공간을 기억하는 내부 함수를 반환한다.\n"
            "반환된 함수인 next()를 호출할 때마다 count가 1씩 증가한다.\n"
            "\n"
            "[코드 분석]\n"
            "  • function add(a, b = 10) { return a + b; }\n"
            "      → add 함수를 선언한다. b의 기본값은 10이므로 add(5)는 5+10=15를 반환한다.\n"
            "  • const mul = (a, b) => a * b;\n"
            "      → 화살표 함수로 곱셈을 정의한다. mul(3, 4)는 12를 반환한다.\n"
            "  • console.log(add(5), mul(3, 4));\n"
            "      → 15와 12를 출력한다.\n"
            "  • function makeCounter() {\n"
            "      → 카운터를 생성하는 함수이다. 호출하면 독립된 카운터 하나가 생성된다.\n"
            "  • let count = 0;\n"
            "      → 카운터의 현재 값이다. 초깃값은 0이다.\n"
            "  • return () => ++count;\n"
            "      → count를 1 증가시키고 반환하는 함수를 반환한다. 이 함수가 바깥의 count 변수를 계속 기억하는 클로저이다.\n"
            "  • const next = makeCounter();\n"
            "      → 카운터를 생성하여 next 변수에 저장한다.\n"
            "  • console.log(next(), next(), next());\n"
            "      → next()를 세 번 호출하면 1, 2, 3을 출력한다.\n"
            "\n"
            "[유의 사항]\n"
            "  • 화살표 함수는 자체 this가 없으므로 객체의 메서드나 클래스 생성자에는 사용하지 않는다.\n"
            "  • 클로저는 변수를 계속 참조하므로, 해제하지 않으면 메모리를 점유할 수 있다.\n"
            "  • 다만 코딩테스트에서는 상태를 유지하는 패턴으로 자주 활용된다."
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
            "[개요]\n"
            "Map과 Set은 각각 키-값 매핑과 중복 없는 집합을 표현하는 자료구조이다.\n"
            "\n"
            "[Map]\n"
            "Map은 키로 값을 조회하는 자료구조이다. 일반 객체({})와 유사하나 다음과 같은 차이가 있다.\n"
            "  • 키로 문자열 외에 숫자, 객체, 함수도 사용할 수 있다.\n"
            "  • 삽입한 순서가 보장된다.\n"
            "  • size로 항목 개수를 바로 확인할 수 있다.\n"
            "주요 기능:\n"
            "  • map.set(키, 값)  → 저장\n"
            "  • map.get(키)      → 조회\n"
            "  • map.has(키)      → 존재 여부 확인(true/false)\n"
            "  • map.size         → 저장된 개수\n"
            "  • map.entries()    → [키, 값] 쌍 전체 반환\n"
            "\n"
            "[Set]\n"
            "Set은 중복이 없는 값들의 집합이다. 같은 값을 여러 번 추가해도 하나만 유지된다.\n"
            "주요 기능:\n"
            "  • set.add(값)     → 추가\n"
            "  • set.has(값)     → 존재 여부 확인\n"
            "  • set.delete(값)  → 삭제\n"
            "  • set.size        → 고유 항목 개수\n"
            "\n"
            "[코드 분석]\n"
            "  • const freq = new Map();\n"
            "      → 빈 Map을 생성한다. 글자 빈도수를 세는 데 사용한다.\n"
            "  • for (const ch of 'banana') {\n"
            "      → 'banana' 문자열을 한 글자씩 꺼내 ch에 담는다.\n"
            "  • freq.set(ch, (freq.get(ch) || 0) + 1);\n"
            "      → ch 글자의 현재 개수를 조회하고(없으면 0) 1을 더해 저장한다.\n"
            "        예: 'a'가 처음 나오면 0+1=1, 두 번째에는 1+1=2로 저장된다.\n"
            "  • console.log([...freq.entries()]);\n"
            "      → Map을 배열로 변환하여 출력한다: [['b',1],['a',3],['n',2]].\n"
            "  • const s = new Set([1, 2, 2, 3, 3, 3]);\n"
            "      → Set에 추가하면 중복이 자동 제거되어 {1, 2, 3}만 남는다.\n"
            "  • console.log(s.size, s.has(2));\n"
            "      → 크기는 3이며, 2의 존재 여부는 true이다.\n"
            "  • [...new Set([5, 5, 1, 1, 9])]\n"
            "      → 배열의 중복을 제거하는 가장 간단한 방법이다. 결과는 [5, 1, 9]이다.\n"
            "\n"
            "[유의 사항]\n"
            "  • Map/Set은 JSON.stringify()로 변환하면 내용이 소실된다.\n"
            "  • 네트워크 전송이나 저장 시에는 일반 객체/배열로 변환해야 한다.\n"
            "  • 코딩테스트에서 글자/단어 빈도 세기, 중복 체크, 방문 여부 확인에 자주 사용한다."
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
            "[개요]\n"
            "JavaScript에서 문자열은 작은따옴표('')나 큰따옴표(\"\")로 생성한다.\n"
            "문자열은 불변(immutable)이므로, 한 번 생성하면 내부 글자를 직접 변경할 수 없다.\n"
            "대신 변환된 새 문자열을 반환하는 메서드를 사용한다.\n"
            "\n"
            "[문자열 메서드]\n"
            "  • s.trim()        → 양쪽 공백 제거 ('  hello  ' → 'hello')\n"
            "  • s.toUpperCase() → 전체 대문자 변환\n"
            "  • s.toLowerCase() → 전체 소문자 변환\n"
            "  • s.split(',')    → 쉼표 기준으로 분할하여 배열 생성\n"
            "  • arr.join('-')   → 배열을 '-'로 연결하여 문자열 생성\n"
            "  • s.slice(1, 4)   → 인덱스 1~3 부분 추출\n"
            "  • s.replace(a, b) → a를 b로 치환\n"
            "  • s.includes('x') → 'x' 포함 여부 확인(true/false)\n"
            "\n"
            "[정규식]\n"
            "정규식(Regular Expression)은 문자열에서 특정 패턴을 찾는 규칙이다.\n"
            "/\\d+/g처럼 슬래시(/) 사이에 패턴을 기술한다.\n"
            "  • \\d → 숫자 한 글자(0~9)\n"
            "  • +  → 앞의 요소가 1개 이상(\\d+는 연속된 숫자 여러 개)\n"
            "  • g  → 플래그. 전체에서 모두 탐색(없으면 첫 번째 일치만)\n"
            "  • i  → 플래그. 대소문자 무시\n"
            "\n"
            "[코드 분석]\n"
            "  • const s = '  Hello, World  ';\n"
            "      → 양쪽에 공백이 있는 문자열을 생성한다.\n"
            "  • s.trim().toUpperCase()\n"
            "      → trim()으로 공백을 제거한 뒤 toUpperCase()를 적용한다. 'Hello, World' → 'HELLO, WORLD'.\n"
            "  • 'a,b,c'.split(',')\n"
            "      → 쉼표 기준으로 분할하여 ['a', 'b', 'c'] 배열을 생성한다.\n"
            "  • ['2024','01','15'].join('-')\n"
            "      → 배열 원소를 '-'로 연결하여 '2024-01-15' 문자열을 생성한다.\n"
            "  • const text = '주문 12개, 재고 345개';\n"
            "      → 숫자가 섞인 문자열이다.\n"
            "  • text.match(/\\d+/g)\n"
            "      → 숫자 덩어리를 모두 찾아 배열로 반환한다: ['12', '345'].\n"
            "  • .map(Number)\n"
            "      → 문자열 배열을 숫자 배열로 변환한다: [12, 345].\n"
            "  • 'banana'.replace(/a/g, '*')\n"
            "      → 'a'를 모두 '*'로 치환한다. g 플래그가 있어 전부 변경된다: 'b*n*n*'.\n"
            "\n"
            "[유의 사항]\n"
            "  • replace()에 문자열을 전달하면 첫 번째 일치 항목만 치환된다.\n"
            "  • 전부 치환하려면 /패턴/g 정규식과 g 플래그를 사용해야 한다.\n"
            "  • 코딩테스트에서 입력 파싱에는 split()이, 숫자 추출에는 match(/\\d+/g)가 자주 쓰인다.\n"
            "  • += 연산으로 문자열을 수천 번 이어 붙이면 성능이 저하된다.\n"
            "  • 배열에 push()로 모아두었다가 마지막에 join()으로 합치는 방식이 훨씬 빠르다."
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
            "[개요]\n"
            "JavaScript는 기본적으로 한 번에 하나의 작업만 처리하는 싱글 스레드 언어이다.\n"
            "서버에서 데이터를 받아오는 등 시간이 걸리는 작업을 동기적으로 기다리면 화면이 멈춘다.\n"
            "비동기 처리는 '작업이 완료되면 이 코드를 실행하라'고 예약한 뒤 다른 작업을 계속 진행하는 방식이다.\n"
            "\n"
            "[Promise]\n"
            "Promise는 미래에 완료될 작업을 나타내는 객체이다.\n"
            "  • resolve(값)   → 작업 성공 및 결과 전달\n"
            "  • reject(에러)  → 작업 실패 및 오류 전달\n"
            "\n"
            "[async/await]\n"
            "async/await는 Promise를 더 읽기 쉽게 작성하는 문법이다.\n"
            "await는 해당 작업이 끝날 때까지 기다린 뒤 다음 줄로 진행한다.\n"
            "복잡한 .then().then() 체인 대신 일반 코드처럼 위에서 아래로 읽히는 형태로 작성할 수 있다.\n"
            "\n"
            "[코드 분석]\n"
            "  • function delay(value, ms) {\n"
            "      → value를 ms 밀리초 후에 반환하는 함수이다. 비동기 작업을 모사한다.\n"
            "  • return new Promise(resolve => setTimeout(() => resolve(value), ms));\n"
            "      → Promise를 생성한다. ms 후에 resolve(value)를 호출하여 완료를 알린다.\n"
            "        setTimeout은 타이머로, ms 후에 콜백을 실행한다.\n"
            "  • (async () => {\n"
            "      → 즉시실행 async 함수이다. await는 async 함수 내부에서만 사용 가능하므로,\n"
            "        최상위에서 await를 쓰려면 이처럼 감싼다.\n"
            "  • const a = await delay('첫번째', 10);\n"
            "      → delay가 완료될 때까지 기다린 뒤 결과값을 a에 저장한다.\n"
            "        await 없이 사용하면 Promise 객체 자체가 저장된다.\n"
            "  • console.log(a);\n"
            "      → '첫번째'를 출력한다.\n"
            "  • const [x, y] = await Promise.all([delay(1, 5), delay(2, 5)]);\n"
            "      → 두 작업을 동시에 시작하고, 둘 다 완료되면 결과를 받는다.\n"
            "        순차적으로 await를 두 번 하면 10ms가 걸리지만, Promise.all은 5ms만 소요된다.\n"
            "  • console.log('합:', x + y);\n"
            "      → '합: 3'을 출력한다.\n"
            "  • })();\n"
            "      → 즉시실행 함수를 호출한다. 마지막의 ()가 즉시 실행을 의미한다.\n"
            "\n"
            "[유의 사항]\n"
            "  • await는 반드시 async 함수 내부에서만 사용할 수 있다.\n"
            "  • 오류 발생 시 try { ... } catch (e) { ... }로 처리해야 한다.\n"
            "  • 여러 작업을 순서대로 await하면 느려진다. 동시에 시작 가능하면 Promise.all을 사용한다.\n"
            "  • 코딩테스트에서는 주로 동기 코드를 사용하며, Node.js로 파일을 읽을 때 readFileSync(동기 버전)를 쓰면 await가 불필요하다."
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
            "[개요]\n"
            "본 주제는 스프레드 연산자, rest 매개변수, 고차함수 세 가지를 다룬다.\n"
            "\n"
            "[스프레드 연산자(...)]\n"
            "스프레드(...)는 배열이나 객체를 펼치는 연산자이다.\n"
            "  • 배열 복사:     const b = [...a]        → a를 복사한 새 배열 b\n"
            "  • 배열 합치기:   [...a, ...b]            → a와 b를 합친 새 배열\n"
            "  • 객체 복사:     const c = { ...obj }    → obj를 복사한 새 객체\n"
            "  • 객체 덮어쓰기: { ...base, y: 20 }      → base를 복사하되 y만 20으로 변경\n"
            "\n"
            "[rest 매개변수(...)]\n"
            "rest는 스프레드와 같은 기호(...)를 쓰지만, 남은 인자를 모아 배열로 만든다.\n"
            "  function sum(...nums) { ... }\n"
            "  sum(1, 2, 3, 4)를 호출하면 nums = [1, 2, 3, 4]가 된다.\n"
            "  전달될 인자 개수를 미리 알 수 없을 때 유용하다.\n"
            "\n"
            "[고차함수]\n"
            "고차함수(Higher-Order Function)는 함수를 인자로 받거나 함수를 반환하는 함수이다.\n"
            "앞서 다룬 map, filter, forEach가 모두 고차함수이며, 함수를 값처럼 전달할 수 있다는 것은 JavaScript의 주요 특징이다.\n"
            "\n"
            "[코드 분석]\n"
            "  • const a = [1, 2], b = [3, 4];\n"
            "      → 두 개의 배열을 생성한다.\n"
            "  • console.log([...a, ...b]);\n"
            "      → a와 b를 펼쳐 합친 [1,2,3,4]를 출력한다.\n"
            "  • const base = { x: 1, y: 2 };\n"
            "      → 기본 객체를 생성한다.\n"
            "  • console.log({ ...base, y: 20, z: 3 });\n"
            "      → base를 복사하되 y는 20으로 덮어쓰고 z를 추가한다: {x:1, y:20, z:3}.\n"
            "        뒤에 나온 y:20이 앞의 y:2를 덮어쓴다.\n"
            "  • const sum = (...nums) => nums.reduce((s, n) => s + n, 0);\n"
            "      → rest 매개변수로 모든 인자를 nums 배열로 받아 reduce로 합산하여 반환한다.\n"
            "  • console.log(sum(1, 2, 3, 4));\n"
            "      → 1+2+3+4 = 10을 출력한다.\n"
            "  • const apply = (fn, ...args) => fn(...args);\n"
            "      → fn은 함수, args는 나머지 인자이다(고차함수). fn에 args를 펼쳐 전달한다.\n"
            "  • console.log(apply(Math.max, 3, 9, 1));\n"
            "      → Math.max(3, 9, 1)을 호출하여 9를 출력한다.\n"
            "\n"
            "[유의 사항]\n"
            "  • 스프레드 복사는 얕은 복사이다.\n"
            "  • 배열 안에 배열이 있거나 객체 안에 객체가 있으면 내부는 공유된다.\n"
            "      const a = { inner: { x: 1 } };\n"
            "      const b = { ...a };         // b는 a의 복사본\n"
            "      b.inner.x = 999;            // a.inner.x도 999로 변경됨. 같은 객체를 참조한다.\n"
            "  • 깊은 복사가 필요하면 JSON.parse(JSON.stringify(obj)) 또는 structuredClone()을 사용한다."
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
            "[개요]\n"
            "본 주제는 배열 누적 연산(reduce), 정렬 비교 함수(sort), 코딩테스트 입력 읽기 세 가지를 다룬다.\n"
            "\n"
            "[reduce]\n"
            "reduce는 배열의 모든 원소를 순차 처리하여 하나의 결과값으로 축약하는 메서드이다.\n"
            "형태: arr.reduce((누적값, 현재값) => 새로운 누적값, 초기값)\n"
            "  • 콜백은 각 원소에 대해 실행된다.\n"
            "  • 첫 번째 인자(누적값): 이전 단계까지의 결과\n"
            "  • 두 번째 인자(현재값): 현재 처리 중인 원소\n"
            "  • 초기값: 누적값의 시작 값(생략 가능하나 누락 시 버그 위험이 있다)\n"
            "예시: [1, 2, 3].reduce((s, n) => s + n, 0)\n"
            "  • 1단계: s=0, n=1 → 0+1=1\n"
            "  • 2단계: s=1, n=2 → 1+2=3\n"
            "  • 3단계: s=3, n=3 → 3+3=6\n"
            "  • 최종 결과: 6\n"
            "\n"
            "[sort 비교 함수]\n"
            "JavaScript의 기본 sort()는 모든 원소를 문자열로 변환하여 비교한다.\n"
            "따라서 [10, 2, 1].sort()는 [1, 10, 2]가 된다(문자열 '10' < '2'이기 때문).\n"
            "숫자를 올바르게 정렬하려면 비교 함수를 전달해야 한다.\n"
            "  • sort((a, b) => a - b)  → 오름차순(a-b가 음수면 a가 앞으로 정렬됨)\n"
            "  • sort((a, b) => b - a)  → 내림차순\n"
            "\n"
            "[입력 읽기]\n"
            "코딩테스트(백준 등)에서는 표준 입력(stdin)으로 데이터가 들어온다.\n"
            "Node.js에서 가장 빠른 방법은 다음과 같다.\n"
            "  • require('fs').readFileSync(0, 'utf8')\n"
            "    → 0은 표준 입력(stdin)을 의미하며, 모든 입력을 한 번에 문자열로 읽는다.\n"
            "  • 이후 .trim().split('\\n')으로 줄 단위로 분할하여 사용한다.\n"
            "\n"
            "[코드 분석]\n"
            "  • const arr = [5, 2, 9, 1, 7];\n"
            "      → 숫자 배열을 생성한다.\n"
            "  • const total = arr.reduce((s, n) => s + n, 0);\n"
            "      → s는 누적합(초기값 0), n은 각 원소이다. 전부 더해 24가 된다.\n"
            "  • console.log('합계', total);\n"
            "      → '합계 24'를 출력한다.\n"
            "  • [...arr].sort((a, b) => a - b)\n"
            "      → arr를 복사한 뒤(원본 보호) 오름차순 정렬한다: [1,2,5,7,9].\n"
            "  • const people = [{n:'A',age:30},{n:'B',age:20},{n:'C',age:30}];\n"
            "      → 나이와 이름을 가진 객체 배열이다.\n"
            "  • people.sort((p, q) => q.age - p.age || p.n.localeCompare(q.n));\n"
            "      → 다중 기준 정렬이다. 먼저 나이 내림차순(q.age - p.age)으로 정렬하고,\n"
            "        나이가 같으면(결과가 0이면) || 뒤의 조건인 이름 오름차순으로 정렬한다.\n"
            "        localeCompare는 문자열을 사전 순으로 비교한다.\n"
            "  • const input = '3\\n10 20 30'.split('\\n');\n"
            "      → 실제 입력 대신 고정 문자열로 시연하며, 줄 단위로 분할한다.\n"
            "  • const n = Number(input[0]);\n"
            "      → 첫 번째 줄('3')을 숫자로 변환한다.\n"
            "  • const nums = input[1].split(' ').map(Number);\n"
            "      → 두 번째 줄을 공백으로 분할하여 각각 숫자로 변환한다: [10, 20, 30].\n"
            "  • nums.reduce((s, v) => s + v, 0)\n"
            "      → 10+20+30 = 60이다.\n"
            "\n"
            "[유의 사항]\n"
            "  • sort()는 원본 배열을 직접 변경한다. 원본을 유지하려면 [...arr].sort()처럼 복사 후 정렬한다.\n"
            "  • sort 비교 함수는 반드시 음수/0/양수 숫자를 반환해야 한다. true/false를 반환하면 정렬이 올바르게 동작하지 않는다.\n"
            "  • reduce의 초기값(두 번째 인자)을 누락하면 빈 배열일 때 오류가 발생하므로 항상 지정한다."
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
