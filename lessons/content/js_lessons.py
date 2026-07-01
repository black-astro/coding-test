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
            "━━ 변수(let/const)와 자료형 이란? ━━\n"
            "\n"
            "변수란 '값을 담아두는 이름 붙은 상자'예요.\n"
            "마치 책상 위에 '나이'라고 라벨을 붙인 서랍을 만들고, 거기에 숫자 25를 넣어두는 것처럼요.\n"
            "JavaScript에서 상자를 만드는 방법은 두 가지예요:\n"
            "  - let  → 나중에 값을 바꿀 수 있는 상자 (예: 점수, 상태)\n"
            "  - const → 한 번 넣으면 절대 못 바꾸는 잠긴 상자 (예: 이름, 고정 설정값)\n"
            "  - var   → 옛날 방식. 범위(스코프)가 이상하게 동작해서 요즘은 거의 안 써요.\n"
            "\n"
            "자료형이란 '상자 안에 넣을 수 있는 값의 종류'예요:\n"
            "  - number  → 숫자 (정수도, 소수도 전부 number예요. 파이썬처럼 int/float 구분 없어요)\n"
            "  - string  → 글자, 문자열 ('안녕' 처럼 따옴표로 감싸요)\n"
            "  - boolean → 참(true) 또는 거짓(false) 딱 두 가지만\n"
            "  - undefined → 상자를 만들었는데 아무것도 안 넣은 상태\n"
            "  - null → 의도적으로 '비었다'고 표시한 상태 (undefined와 미묘하게 달라요)\n"
            "\n"
            "코드 한 줄씩 읽기:\n"
            "  const a = 10;           →  잠긴 상자 'a'를 만들고 숫자 10을 넣어요. 나중에 a = 20 하면 에러!\n"
            "  let b = 3.14;           →  바꿀 수 있는 상자 'b'에 소수 3.14를 넣어요\n"
            "  const name = '홍길동';   →  문자열 '홍길동'을 name 상자에 넣어요\n"
            "  const flag = true;      →  참(true) 값을 flag 상자에 넣어요\n"
            "  typeof a                →  'a 상자 안에 뭐가 들어 있어?' 물어보면 'number'라고 알려줘요\n"
            "  Number('5')             →  문자열 '5'를 숫자 5로 바꿔줘요. 문자 + 숫자 계산할 때 꼭 필요해요\n"
            "  a + Number('5')         →  10 + 5 = 15 가 돼요. Number() 없이 a + '5' 하면 '105'(문자연결)!\n"
            "  name.repeat(2)          →  '홍길동'을 2번 반복해서 '홍길동홍길동'을 만들어요\n"
            "  1 === '1'               →  숫자 1과 문자 '1'은 값은 같아 보여도 타입이 달라서 false예요\n"
            "  1 == '1'                →  ==는 타입을 자동으로 맞춰서 비교하니까 true가 돼요 (헷갈리니 쓰지 마세요!)\n"
            "\n"
            "주의할 점:\n"
            "  코딩테스트에서 입력을 받으면 항상 '문자열'로 들어와요.\n"
            "  '10' + '20' = '1020' (문자 연결!) 이 돼서 틀리기 쉬워요.\n"
            "  그래서 Number() 또는 parseInt() 로 숫자로 바꿔줘야 해요.\n"
            "  항상 == 대신 === 를 쓰는 습관을 들이세요. 타입까지 비교해서 안전해요."
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
            "━━ 배열(Array) 이란? ━━\n"
            "\n"
            "배열은 '여러 개의 값을 순서대로 담는 목록'이에요.\n"
            "마치 번호가 매겨진 사물함이 여러 개 나란히 붙어 있는 것처럼요.\n"
            "1번 사물함, 2번 사물함... 이렇게 번호(인덱스)로 꺼낼 수 있어요.\n"
            "JavaScript에서 인덱스는 0부터 시작해요. 첫 번째 항목은 arr[0]이에요!\n"
            "\n"
            "배열을 다루는 핵심 메서드 세 가지:\n"
            "  - map    → '변환': 모든 항목을 바꿔서 새 배열을 만들어요 (예: 점수 전부 2배)\n"
            "  - filter → '선별': 조건에 맞는 항목만 골라 새 배열을 만들어요 (예: 짝수만 골라내기)\n"
            "  - forEach→ '반복': 각 항목에 대해 무언가를 실행해요. 새 배열은 안 만들어요 (예: 전부 출력)\n"
            "\n"
            "왜 for문 대신 map/filter를 쓰나요?\n"
            "  for문: '배열을 돌면서 새 배열에 넣어야지...' → 코드가 길어져요\n"
            "  map:   '각 원소를 이렇게 바꿔줘' → 의도가 한눈에 보여요\n"
            "\n"
            "코드 한 줄씩 읽기:\n"
            "  const a = [5, 2, 9, 1];  →  숫자 4개를 가진 배열 'a'를 만들어요\n"
            "  a.push(7);               →  배열 끝에 7을 추가해요. 이제 [5,2,9,1,7]이 돼요\n"
            "  a.slice(1, 3)            →  인덱스 1부터 3 직전(2)까지만 잘라서 [2,9]를 돌려줘요\n"
            "  [...a].reverse()         →  a를 복사(...)한 뒤 뒤집어요. 원본 a는 그대로예요\n"
            "  [1,2,3,4,5].map(x => x * x)  →  각 숫자를 제곱해서 새 배열 [1,4,9,16,25]를 만들어요\n"
            "  a.filter(x => x % 2 === 0)   →  짝수인 것만 골라서 새 배열을 만들어요\n"
            "  a.forEach((v, i) => ...)      →  v는 값(value), i는 인덱스(index)예요. 각 항목을 순서대로 처리해요\n"
            "\n"
            "주의할 점:\n"
            "  map과 filter는 항상 '새 배열'을 만들어요. 원본 배열은 바뀌지 않아요.\n"
            "  배열 인덱스는 0부터 시작해요. 4개짜리 배열의 마지막은 arr[3]이에요.\n"
            "  push는 원본을 바꾸지만, map/filter는 원본을 안 바꿔요. 이 차이를 기억하세요!"
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
            "━━ 객체(Object) 이란? ━━\n"
            "\n"
            "객체는 '이름표(키)가 붙은 값들의 묶음'이에요.\n"
            "예를 들어 사람 한 명의 정보를 표현하고 싶을 때:\n"
            "  배열: [\"김철수\", 20, \"서울\"]  → 순서로 구분, 뭐가 뭔지 모호해요\n"
            "  객체: { name: \"김철수\", age: 20, city: \"서울\" }  → 이름표(키)가 있어서 명확해요\n"
            "\n"
            "마치 개인 신상카드처럼 각 항목에 이름이 붙어 있어요.\n"
            "obj.name 또는 obj['name'] 두 가지 방법으로 꺼낼 수 있어요.\n"
            "\n"
            "구조분해(Destructuring)란?\n"
            "  객체에서 값을 꺼낼 때 보통은:\n"
            "    const name = user.name;   // 이렇게 한 줄씩 꺼내야 해요\n"
            "    const age = user.age;\n"
            "  구조분해를 쓰면:\n"
            "    const { name, age } = user;  // 한 줄로 여러 개를 한꺼번에 꺼내요!\n"
            "\n"
            "코드 한 줄씩 읽기:\n"
            "  const user = { name: '김철수', age: 20, city: '서울' };\n"
            "    →  세 가지 정보를 가진 user 객체를 만들어요. 키-값 쌍이에요\n"
            "  const { name, age } = user;\n"
            "    →  user 객체에서 name과 age만 꺼내서 변수로 만들어요. 구조분해예요\n"
            "  console.log(name, age);\n"
            "    →  '김철수 20' 이 출력돼요\n"
            "  const score = 95;\n"
            "    →  score라는 변수에 95를 넣어요\n"
            "  const result = { name, score };\n"
            "    →  단축 속성이에요! { name: name, score: score } 와 똑같아요.\n"
            "       변수 이름과 키 이름이 같으면 줄여 쓸 수 있어요\n"
            "  Object.keys(user)\n"
            "    →  user 객체의 키(이름표)들을 배열로 꺼내요: ['name', 'age', 'city']\n"
            "  Object.entries(user)\n"
            "    →  [키, 값] 쌍을 배열로 꺼내요: [['name','김철수'], ['age',20], ...]\n"
            "\n"
            "주의할 점:\n"
            "  const로 선언한 객체는 '재할당'은 못 하지만 '내부 값 변경'은 가능해요.\n"
            "    const user = { age: 20 };\n"
            "    user.age = 21;   // 이건 OK! 객체 내부 변경은 허용돼요\n"
            "    user = {};       // 이건 에러! 객체 자체를 다시 할당하면 안 돼요\n"
            "  객체를 복사할 때 { ...obj } 를 쓰면 얕은 복사예요. 중첩된 객체는 공유돼요."
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
            "━━ 함수·화살표함수·클로저 이란? ━━\n"
            "\n"
            "[1] 함수(Function)\n"
            "함수는 '반복해서 쓸 코드 묶음에 이름을 붙인 것'이에요.\n"
            "김밥 만드는 레시피를 한 번 적어두면 언제든 꺼내 쓸 수 있잖아요?\n"
            "함수도 마찬가지예요. 코드를 한 번 작성하고 이름으로 여러 번 불러 써요.\n"
            "\n"
            "선언 방법 두 가지:\n"
            "  방법 1: function 선언식\n"
            "    function add(a, b) { return a + b; }\n"
            "  방법 2: 화살표 함수 (Arrow Function)\n"
            "    const add = (a, b) => a + b;\n"
            "  → 화살표 함수가 더 짧게 쓸 수 있어요. return과 중괄호 {}를 생략할 수도 있어요\n"
            "\n"
            "[2] 기본값 매개변수\n"
            "  function add(a, b = 10) { return a + b; }\n"
            "  add(5) 처럼 b를 안 넣으면 자동으로 b = 10 이 돼요.\n"
            "  '디폴트 값'이라고 불러요. 자주 쓰는 값을 미리 정해두는 거예요.\n"
            "\n"
            "[3] 클로저(Closure)\n"
            "클로저는 '함수가 바깥 변수를 기억하는 것'이에요.\n"
            "비유: 은행 계좌처럼요. 통장(변수)은 밖에 있고,\n"
            "입금/출금 함수는 그 통장을 계속 기억하고 접근할 수 있어요.\n"
            "makeCounter() 함수는 count 변수를 가진 '공간'을 만들고,\n"
            "그 공간을 기억하는 작은 함수를 반환해요.\n"
            "next()를 부를 때마다 그 count가 1씩 늘어요.\n"
            "\n"
            "코드 한 줄씩 읽기:\n"
            "  function add(a, b = 10) { return a + b; }\n"
            "    →  add 함수를 선언해요. b는 기본값 10. add(5)하면 5+10=15가 돼요\n"
            "  const mul = (a, b) => a * b;\n"
            "    →  화살표 함수로 곱셈을 해요. mul(3, 4) = 12\n"
            "  console.log(add(5), mul(3, 4));\n"
            "    →  15와 12를 출력해요\n"
            "  function makeCounter() {\n"
            "    →  카운터를 만드는 함수예요. 호출하면 '카운터 하나'가 생겨요\n"
            "  let count = 0;\n"
            "    →  카운터의 현재 숫자예요. 처음엔 0이에요\n"
            "  return () => ++count;\n"
            "    →  count를 1 증가시키고 반환하는 함수를 돌려줘요. 이게 클로저예요!\n"
            "       이 함수는 바깥의 count 변수를 계속 기억해요\n"
            "  const next = makeCounter();\n"
            "    →  카운터를 하나 만들어서 next 변수에 저장해요\n"
            "  console.log(next(), next(), next());\n"
            "    →  next()를 세 번 부르면 1, 2, 3이 출력돼요\n"
            "\n"
            "주의할 점:\n"
            "  화살표 함수는 this가 없어요. 그래서 객체의 메서드나 클래스 생성자에는 쓰면 안 돼요.\n"
            "  클로저는 변수를 계속 붙잡고 있어서, 잊으면 메모리를 차지할 수 있어요.\n"
            "  하지만 코딩테스트에서는 상태를 유지하는 패턴으로 자주 활용돼요."
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
            "━━ Map과 Set 이란? ━━\n"
            "\n"
            "[1] Map (맵)\n"
            "Map은 '전화번호부'처럼 이름(키)으로 번호(값)를 찾는 자료구조예요.\n"
            "일반 객체({})와 비슷하지만 몇 가지 차이가 있어요:\n"
            "  - 키로 문자열 외에 숫자, 객체, 함수도 쓸 수 있어요\n"
            "  - 넣은 순서가 보장돼요\n"
            "  - size로 개수를 바로 알 수 있어요\n"
            "\n"
            "Map 주요 기능:\n"
            "  map.set(키, 값)    → 저장\n"
            "  map.get(키)        → 꺼내기\n"
            "  map.has(키)        → 있는지 확인 (true/false)\n"
            "  map.size           → 저장된 개수\n"
            "  map.entries()      → [키, 값] 쌍을 전부 꺼내기\n"
            "\n"
            "[2] Set (셋)\n"
            "Set은 '중복 없는 값들의 집합'이에요.\n"
            "비유: 출석부에 이미 있는 이름은 다시 안 적는 것처럼요.\n"
            "같은 값을 아무리 많이 넣어도 한 개만 남아요.\n"
            "\n"
            "Set 주요 기능:\n"
            "  set.add(값)    → 추가\n"
            "  set.has(값)    → 있는지 확인\n"
            "  set.delete(값) → 삭제\n"
            "  set.size       → 고유한 항목 개수\n"
            "\n"
            "코드 한 줄씩 읽기:\n"
            "  const freq = new Map();\n"
            "    →  빈 Map을 만들어요. 글자 빈도수를 셀 거예요\n"
            "  for (const ch of 'banana') {\n"
            "    →  'banana' 문자열을 한 글자씩 꺼내서 ch에 담아요\n"
            "  freq.set(ch, (freq.get(ch) || 0) + 1);\n"
            "    →  ch 글자의 현재 개수를 꺼내서(없으면 0) 1을 더해서 저장해요\n"
            "       예: 'a'가 처음 나오면 0+1=1, 두 번째엔 1+1=2로 저장돼요\n"
            "  console.log([...freq.entries()]);\n"
            "    →  Map을 배열로 변환해서 출력해요: [['b',1],['a',3],['n',2]]\n"
            "  const s = new Set([1, 2, 2, 3, 3, 3]);\n"
            "    →  Set에 넣으면 중복이 자동으로 제거돼요. {1, 2, 3}만 남아요\n"
            "  console.log(s.size, s.has(2));\n"
            "    →  크기는 3, 2가 있는지 확인하면 true예요\n"
            "  [...new Set([5, 5, 1, 1, 9])]\n"
            "    →  배열의 중복을 제거하는 가장 간단한 방법이에요! [5, 1, 9]가 돼요\n"
            "\n"
            "주의할 점:\n"
            "  Map/Set은 JSON.stringify()로 변환하면 내용이 사라져요.\n"
            "  네트워크로 보내거나 저장할 땐 일반 객체/배열로 변환해야 해요.\n"
            "  코딩테스트에서 글자/단어 빈도 세기, 중복 체크, 방문 여부 확인에 자주 써요!"
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
            "━━ 문자열 처리와 정규식 이란? ━━\n"
            "\n"
            "[1] 문자열 기본\n"
            "JavaScript에서 문자열은 작은따옴표('')나 큰따옴표(\"\")로 만들어요.\n"
            "문자열은 '불변(immutable)'이에요. 한 번 만들면 그 안의 글자를 직접 바꿀 수 없어요.\n"
            "대신 변환된 새 문자열을 만들어 반환하는 메서드들을 써요.\n"
            "\n"
            "자주 쓰는 문자열 메서드:\n"
            "  s.trim()        → 양쪽 공백 제거 ('  hello  ' → 'hello')\n"
            "  s.toUpperCase() → 전부 대문자로\n"
            "  s.toLowerCase() → 전부 소문자로\n"
            "  s.split(',')    → 쉼표로 나눠서 배열로 만들기\n"
            "  arr.join('-')   → 배열을 -로 이어서 문자열 만들기\n"
            "  s.slice(1, 4)   → 인덱스 1~3 부분만 잘라내기\n"
            "  s.replace(a, b) → a를 b로 바꾸기\n"
            "  s.includes('x') → 'x'가 포함되어 있는지 확인 (true/false)\n"
            "\n"
            "[2] 정규식(Regular Expression)\n"
            "정규식은 '문자열에서 특정 패턴을 찾는 규칙'이에요.\n"
            "예를 들어 '숫자가 연속으로 나타나는 부분'을 찾고 싶을 때 쓰는 특수한 문법이에요.\n"
            "/\\d+/g 처럼 슬래시(/) 사이에 패턴을 적어요.\n"
            "  \\d   → 숫자 한 글자 (0~9)\n"
            "  +    → 앞의 것이 1개 이상 (\\d+는 '숫자 여러 개 연속')\n"
            "  g    → 플래그. 전체에서 다 찾기 (g 없으면 처음 발견한 것만)\n"
            "  i    → 플래그. 대소문자 무시\n"
            "\n"
            "코드 한 줄씩 읽기:\n"
            "  const s = '  Hello, World  ';\n"
            "    →  양쪽에 공백이 있는 문자열을 만들어요\n"
            "  s.trim().toUpperCase()\n"
            "    →  먼저 trim()으로 공백을 제거하고, 그 결과에 toUpperCase()를 적용해요\n"
            "       'Hello, World' → 'HELLO, WORLD'\n"
            "  'a,b,c'.split(',')\n"
            "    →  쉼표 기준으로 나눠서 ['a', 'b', 'c'] 배열을 만들어요\n"
            "  ['2024','01','15'].join('-')\n"
            "    →  배열 원소들을 '-'로 이어서 '2024-01-15' 문자열을 만들어요\n"
            "  const text = '주문 12개, 재고 345개';\n"
            "    →  숫자가 섞인 문자열이에요\n"
            "  text.match(/\\d+/g)\n"
            "    →  숫자 덩어리들을 전부 찾아서 배열로 반환해요: ['12', '345']\n"
            "  .map(Number)\n"
            "    →  문자열 배열을 숫자 배열로 변환해요: [12, 345]\n"
            "  'banana'.replace(/a/g, '*')\n"
            "    →  'a'를 전부 '*'로 바꿔요. g 플래그가 있어서 전부 바뀌어요: 'b*n*n*'\n"
            "\n"
            "주의할 점:\n"
            "  replace()에 문자열을 넣으면 처음 발견한 것만 바뀌어요.\n"
            "  전부 바꾸려면 /패턴/g 정규식 + g 플래그를 써야 해요.\n"
            "  코딩테스트에서 입력 파싱에 split()이 가장 자주 나오고,\n"
            "  숫자 추출에 match(/\\d+/g)가 자주 쓰여요.\n"
            "  문자열을 += 로 이어 붙이는 걸 수천 번 반복하면 느려져요.\n"
            "  배열에 push() 해두고 마지막에 join()으로 합치는 게 훨씬 빨라요."
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
            "━━ 비동기 처리(async/await·Promise) 이란? ━━\n"
            "\n"
            "[1] 왜 비동기가 필요한가?\n"
            "JavaScript는 기본적으로 한 번에 한 가지 일만 해요 (싱글 스레드).\n"
            "그런데 서버에서 데이터를 받아오는 건 시간이 걸려요.\n"
            "만약 기다리는 동안 아무것도 못 하면 화면이 멈춰버려요!\n"
            "\n"
            "비유: 라면을 끓일 때 물 끓는 동안 멍하니 서있지 않고 다른 준비를 하잖아요?\n"
            "비동기도 마찬가지예요. '나중에 완료되면 이걸 해줘'라고 예약하고 다른 일을 해요.\n"
            "\n"
            "[2] Promise\n"
            "Promise는 '미래에 완료될 작업을 나타내는 객체'예요.\n"
            "마치 식당에서 번호표를 받는 것처럼요.\n"
            "  - resolve(값) → '주문 완료! 여기 음식이요' (성공)\n"
            "  - reject(에러) → '죄송해요, 재료가 떨어졌어요' (실패)\n"
            "\n"
            "[3] async/await\n"
            "async/await는 Promise를 더 읽기 쉽게 쓰는 방법이에요.\n"
            "await를 쓰면 '이 작업이 끝날 때까지 기다렸다가 다음 줄로 가요'.\n"
            "복잡한 .then().then().then() 체인 대신 일반 코드처럼 위에서 아래로 읽혀요.\n"
            "\n"
            "코드 한 줄씩 읽기:\n"
            "  function delay(value, ms) {\n"
            "    →  value를 ms 밀리초 후에 돌려주는 함수예요. 비동기 작업을 흉내 내요\n"
            "  return new Promise(resolve => setTimeout(() => resolve(value), ms));\n"
            "    →  Promise를 만들어요. ms 후에 resolve(value)를 호출해서 '완료!'를 알려요\n"
            "       setTimeout은 타이머예요. ms 후에 콜백을 실행해요\n"
            "  (async () => {\n"
            "    →  즉시실행 async 함수예요. async 함수 안에서만 await를 쓸 수 있어서\n"
            "       최상위에서 await를 쓰려면 이렇게 감싸요\n"
            "  const a = await delay('첫번째', 10);\n"
            "    →  delay가 완료될 때까지 기다렸다가, 결과값을 a에 저장해요\n"
            "       await 없이 쓰면 Promise 객체 자체가 저장돼요!\n"
            "  console.log(a);\n"
            "    →  '첫번째'가 출력돼요\n"
            "  const [x, y] = await Promise.all([delay(1, 5), delay(2, 5)]);\n"
            "    →  두 작업을 '동시에' 시작하고, 둘 다 끝나면 결과를 받아요\n"
            "       순차적으로 await 두 번 하면 10ms 걸리지만, Promise.all은 5ms만 걸려요!\n"
            "  console.log('합:', x + y);\n"
            "    →  '합: 3' 이 출력돼요\n"
            "  })();\n"
            "    →  즉시실행 함수를 호출해요. 마지막의 ()가 '지금 당장 실행해!'예요\n"
            "\n"
            "주의할 점:\n"
            "  await는 반드시 async 함수 안에서만 쓸 수 있어요.\n"
            "  에러가 나면 try { ... } catch (e) { ... } 로 잡아야 해요.\n"
            "  여러 작업을 순서대로 await하면 느려요. 동시에 시작해도 되면 Promise.all을 쓰세요.\n"
            "  코딩테스트에서는 비동기보다 동기 코드를 주로 쓰지만,\n"
            "  Node.js로 파일 읽기를 할 때 readFileSync(동기 버전)를 쓰면 await 불필요해요."
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
            "━━ 구조분해·스프레드·고차함수 이란? ━━\n"
            "\n"
            "[1] 스프레드 연산자(...)\n"
            "스프레드(...)는 '배열이나 객체를 펼치는' 연산자예요.\n"
            "비유: 선물 상자(배열)를 열어서 안의 물건들을 탁자 위에 전부 꺼내는 것처럼요.\n"
            "\n"
            "활용 방법:\n"
            "  배열 복사: const b = [...a]       → a를 복사한 새 배열 b\n"
            "  배열 합치기: [...a, ...b]          → a와 b를 합친 새 배열\n"
            "  객체 복사: const c = { ...obj }   → obj를 복사한 새 객체\n"
            "  객체 덮어쓰기: { ...base, y: 20 } → base를 복사하되 y만 20으로 바꾸기\n"
            "\n"
            "[2] rest 매개변수(...)\n"
            "rest는 스프레드와 같은 기호(...)지만, '남은 것을 모아서 배열로' 만들어요.\n"
            "  function sum(...nums) { ... }\n"
            "  sum(1, 2, 3, 4)를 호출하면 nums = [1, 2, 3, 4]가 돼요\n"
            "  인자 개수가 얼마나 올지 모를 때 유용해요!\n"
            "\n"
            "[3] 고차함수(Higher-Order Function)\n"
            "고차함수는 '함수를 인자로 받거나 함수를 반환하는 함수'예요.\n"
            "우리가 이미 배운 map, filter, forEach가 모두 고차함수예요!\n"
            "함수를 값처럼 전달할 수 있다는 JavaScript의 강력한 특징이에요.\n"
            "\n"
            "코드 한 줄씩 읽기:\n"
            "  const a = [1, 2], b = [3, 4];\n"
            "    →  두 개의 배열을 만들어요\n"
            "  console.log([...a, ...b]);\n"
            "    →  a를 펼치고 b를 펼쳐서 합친 [1,2,3,4]를 출력해요\n"
            "  const base = { x: 1, y: 2 };\n"
            "    →  기본 객체를 만들어요\n"
            "  console.log({ ...base, y: 20, z: 3 });\n"
            "    →  base를 복사하는데 y는 20으로 덮어쓰고 z는 새로 추가해요: {x:1, y:20, z:3}\n"
            "       뒤에 나온 y:20이 앞의 y:2를 덮어씌워요!\n"
            "  const sum = (...nums) => nums.reduce((s, n) => s + n, 0);\n"
            "    →  rest 매개변수로 모든 인자를 nums 배열로 받아요\n"
            "       reduce로 전부 더해서 반환해요\n"
            "  console.log(sum(1, 2, 3, 4));\n"
            "    →  1+2+3+4 = 10이 출력돼요\n"
            "  const apply = (fn, ...args) => fn(...args);\n"
            "    →  fn은 함수, args는 나머지 인자들이에요. 고차함수예요!\n"
            "       fn 함수에 args를 펼쳐서 전달해요\n"
            "  console.log(apply(Math.max, 3, 9, 1));\n"
            "    →  Math.max(3, 9, 1) 을 호출해서 9가 출력돼요\n"
            "\n"
            "주의할 점:\n"
            "  스프레드 복사는 '얕은 복사'예요!\n"
            "  배열 안에 배열이 있거나, 객체 안에 객체가 있으면 내부는 공유돼요.\n"
            "    const a = { inner: { x: 1 } };\n"
            "    const b = { ...a };         // b는 a의 복사본\n"
            "    b.inner.x = 999;            // a.inner.x도 999로 바뀌어요! 같은 객체를 가리켜요\n"
            "  깊은 복사가 필요하면 JSON.parse(JSON.stringify(obj))를 쓰거나 structuredClone()을 써요."
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
            "━━ reduce·sort 비교자·입력 읽기 이란? ━━\n"
            "\n"
            "[1] reduce - 배열을 하나의 값으로 줄이기\n"
            "reduce는 '배열의 모든 원소를 하나씩 처리해서 결과 하나를 만드는' 메서드예요.\n"
            "비유: 영수증 여러 장을 하나씩 꺼내서 계속 더해 최종 합계를 구하는 것처럼요.\n"
            "\n"
            "형태: arr.reduce((누적값, 현재값) => 새로운 누적값, 초기값)\n"
            "  - 콜백은 각 원소에 대해 실행돼요\n"
            "  - 첫 번째 인자(누적값): 이전 단계까지의 결과\n"
            "  - 두 번째 인자(현재값): 지금 처리 중인 원소\n"
            "  - 초기값: 누적값의 시작 값 (생략 가능하지만 안 쓰면 버그 위험!)\n"
            "\n"
            "예시: [1, 2, 3].reduce((s, n) => s + n, 0)\n"
            "  1단계: s=0, n=1 → 0+1=1\n"
            "  2단계: s=1, n=2 → 1+2=3\n"
            "  3단계: s=3, n=3 → 3+3=6\n"
            "  최종 결과: 6\n"
            "\n"
            "[2] sort - 정렬할 때 비교 함수\n"
            "JavaScript의 기본 sort()는 모든 것을 '문자열'로 변환해서 비교해요.\n"
            "그래서 [10, 2, 1].sort() 하면 [1, 10, 2]가 돼버려요! (문자열 '10' < '2' 이니까)\n"
            "숫자를 올바르게 정렬하려면 비교 함수를 넘겨야 해요:\n"
            "  sort((a, b) => a - b)   → 오름차순 (a-b가 음수면 a가 앞으로)\n"
            "  sort((a, b) => b - a)   → 내림차순\n"
            "\n"
            "[3] 코딩테스트 입력 읽기\n"
            "코딩테스트(백준 등)에서는 표준 입력(stdin)으로 데이터가 들어와요.\n"
            "Node.js에서 가장 빠른 방법:\n"
            "  require('fs').readFileSync(0, 'utf8')\n"
            "  → 0은 표준 입력(stdin)을 의미해요. 모든 입력을 한 번에 문자열로 읽어요\n"
            "  그 다음 .trim().split('\\n')으로 줄 단위로 나눠서 사용해요\n"
            "\n"
            "코드 한 줄씩 읽기:\n"
            "  const arr = [5, 2, 9, 1, 7];\n"
            "    →  숫자 배열을 만들어요\n"
            "  const total = arr.reduce((s, n) => s + n, 0);\n"
            "    →  s는 누적합(초기값 0), n은 각 원소예요. 전부 더해서 24가 돼요\n"
            "  console.log('합계', total);\n"
            "    →  '합계 24'가 출력돼요\n"
            "  [...arr].sort((a, b) => a - b)\n"
            "    →  arr를 복사한 후(원본 보호!) 오름차순 정렬해요: [1,2,5,7,9]\n"
            "  const people = [{n:'A',age:30},{n:'B',age:20},{n:'C',age:30}];\n"
            "    →  나이와 이름을 가진 객체 배열이에요\n"
            "  people.sort((p, q) => q.age - p.age || p.n.localeCompare(q.n));\n"
            "    →  복잡한 정렬이에요! 먼저 나이 내림차순(q.age - p.age)으로 정렬하고,\n"
            "       나이가 같으면(0이면) || 뒤의 조건: 이름 오름차순으로 정렬해요\n"
            "       localeCompare는 문자열을 사전 순으로 비교해요\n"
            "  const input = '3\\n10 20 30'.split('\\n');\n"
            "    →  실제 입력 대신 고정 문자열로 시연해요. 줄 단위로 나눠요\n"
            "  const n = Number(input[0]);\n"
            "    →  첫 번째 줄('3')을 숫자로 변환해요\n"
            "  const nums = input[1].split(' ').map(Number);\n"
            "    →  두 번째 줄을 공백으로 나눠서 각각 숫자로 변환해요: [10, 20, 30]\n"
            "  nums.reduce((s, v) => s + v, 0)\n"
            "    →  10+20+30 = 60이에요\n"
            "\n"
            "주의할 점:\n"
            "  sort()는 원본 배열을 직접 바꿔요! 원본을 유지하고 싶으면 [...arr].sort()처럼 복사 후 정렬하세요.\n"
            "  sort 비교 함수는 반드시 음수/0/양수 숫자를 반환해야 해요.\n"
            "  true/false를 반환하면 정렬이 제대로 안 돼요!\n"
            "  reduce의 초기값(두 번째 인자)을 빠뜨리면 빈 배열일 때 에러가 나요. 항상 써주세요."
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
