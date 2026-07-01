"""SCSS 보강 레슨 (기초·중급·고급 각 5개, 총 15개).

scss_lessons.py 와 주제가 겹치지 않는 새 주제들이다.
각 code 는 단일 .scss 파일로 libsass 에서 컴파일되는 유효한 SCSS 이다.
(@use 'sass:math' 같은 dart-sass 전용 모듈 문법은 쓰지 않는다.)
"""

from engine.models import Lesson

LESSONS = [

    # ───────────────────────── 기초 ─────────────────────────

    Lesson(
        id="scss-basic-04-number-type",
        lang="scss", level="기초",
        title="숫자 타입과 단위",
        summary="단위 있는/없는 숫자와 단위 연산 규칙",
        explanation=(
            "[개요]\n"
            "일반 프로그래밍에서 숫자는 3, 5 같은 값이지만, 웹 화면에서는 단위가 중요하다. 3이 3cm 인지 3픽셀인지에 따라 의미가 달라지기 때문이다.\n"
            "SCSS 의 숫자는 단위를 함께 가진다. 16px, 1.5rem, 50%, 그리고 단위가 없는 3 이 모두 존재한다.\n"
            "'16px' 는 16이라는 숫자와 px 라는 단위가 결합된 하나의 값이다.\n\n"
            "[단위의 의미]\n"
            "웹 화면에 요소를 그리려면 반드시 단위가 필요하다. SCSS 는 연산 시 이 단위를 자동으로 관리한다.\n\n"
            "[연산 규칙]\n"
            "• 16px + 4px = 20px  → 같은 단위(px)끼리는 그대로 더하고 뺄 수 있다.\n"
            "• 8px * 2 = 16px     → 단위 있는 숫자에 단위 없는 숫자를 곱하면 단위는 그대로 유지된다.\n"
            "• 16px * $scale      → 변수에 담긴 1.5 를 곱하면 24px 이 된다. 배율은 단위 없는 숫자로 두는 것이 자연스럽다.\n"
            "• percentage(0.25) = 25% → 0.25 라는 비율을 % 로 변환하는 내장 함수이다.\n\n"
            "[변수에 기준값을 담는 이유]\n"
            "• $base: 8px 처럼 기준 간격을 정하고 8px·16px·24px 를 기준의 배수로 구성하면 화면 전체가 일관된 리듬으로 정돈된다.\n"
            "• 기준값 8px 을 10px 로 변경하면 배수들이 모두 함께 변경되므로, 한 곳만 수정하면 된다. 이것이 변수를 사용하는 핵심 이유이다.\n\n"
            "[유의 사항]\n"
            "• 서로 다른 단위(예: px + em)를 더하면 컴파일 에러가 발생한다. 단위를 먼저 맞춰야 한다.\n"
            "• 단위 있는 숫자(8px)와 단위 없는 숫자(2)를 혼동하면 결과 단위가 잘못되므로, 배율은 단위 없이 두는 습관이 필요하다.\n"
            "• 컴파일(SCSS→CSS 변환) 시 위 식들은 미리 계산되어, 결과 CSS 에는 20px 같은 최종 숫자만 남는다."
        ),
        usage="기준 간격의 배수, 비율 기반 너비 등 '수치로 계산되는 값'을 변수와 식으로 표현할 때 쓴다.",
        cons="단위가 다른 값끼리 연산하면 컴파일 에러가 난다. 단위 없는 숫자와 단위 있는 숫자를 헷갈리지 않게 주의한다.",
        code=(
            "$base: 8px;        // 단위 있는 숫자\n"
            "$scale: 1.5;       // 단위 없는 숫자\n"
            "$ratio: 0.25;\n"
            "\n"
            ".box {\n"
            "  padding: $base * 2;           // 16px\n"
            "  margin-bottom: $base * 3;     // 24px\n"
            "  font-size: 16px * $scale;     // 24px\n"
            "  width: percentage($ratio);    // 25%\n"
            "}\n"
            "\n"
            ".gap-sm { margin: $base; }       // 8px\n"
            ".gap-lg { margin: $base + 16px; } // 24px\n"
        ),
    ),

    Lesson(
        id="scss-basic-05-string-type",
        lang="scss", level="기초",
        title="문자열 타입과 따옴표",
        summary="따옴표 유무·문자열 함수·따옴표 변환",
        explanation=(
            "[개요]\n"
            "문자열은 글자들의 묶음이다. 'hello', 'Noto Sans', 'new' 처럼 사람이 읽는 텍스트를 의미한다.\n"
            "SCSS 에서는 문자열을 두 가지 방식으로 표기할 수 있다.\n"
            "• 따옴표가 있는 문자열: 'hello'\n"
            "• 따옴표가 없는 문자열: bold\n\n"
            "[따옴표 유무의 차이]\n"
            "• 따옴표 없는 단어(bold, sans-serif)는 키워드처럼 동작하며, CSS 속성 값으로 곧바로 사용하기 적합하다(예: font-weight: bold).\n"
            "• 따옴표 있는 문자열('NEW')은 실제 텍스트로 취급되며, 화면에 글자를 출력하는 content 등에 필요하다.\n\n"
            "[문자열 함수]\n"
            "• quote(x)             → 문자열에 따옴표를 추가한다. quote(Noto Sans) → 'Noto Sans'\n"
            "• unquote('x')         → 반대로 따옴표를 제거한다. 값으로 사용할 때 쓴다.\n"
            "• to-upper-case('new') → 전부 대문자로 변환한다. → 'NEW' (소문자 변환은 to-lower-case)\n"
            "• str-length('new')    → 글자 개수를 센다. 'new' 는 3글자이므로 3.\n\n"
            "[보간(#{})을 이용한 문자열 합성]\n"
            "• #{$var} 는 변수의 값을 문자열 사이에 삽입하는 도구이다.\n"
            "• 예: url('/img/' + $label + '.svg') 는 여러 문자열 조각을 이어붙여 '/img/new.svg' 라는 경로를 생성한다.\n"
            "• 이를 통해 아이콘 경로나 클래스 이름을 변수로 자동 생성할 수 있다.\n\n"
            "[유의 사항]\n"
            "• content 값에는 일반적으로 따옴표 있는 문자열을 사용해야 의도대로 출력된다. 따옴표를 누락하면 오작동할 수 있다.\n"
            "• 따옴표 유무에 따라 텍스트인지 키워드인지 의미가 달라지므로, 값으로 쓸 때는 unquote, 텍스트로 출력할 때는 quote 를 사용한다.\n"
            "• 컴파일된 결과 CSS 에는 함수가 모두 적용된 최종 문자열만 남는다(to-upper-case 사용 시 'NEW' 로 변환된 상태)."
        ),
        usage="폰트 패밀리·경로·content 등 문자열 값을 다루거나, 보간으로 동적 이름을 만들 때 쓴다.",
        cons="따옴표 유무에 따라 값의 의미가 달라질 수 있다. content 에는 보통 따옴표 있는 문자열을 써야 의도대로 나온다.",
        code=(
            "$family: 'Noto Sans';\n"
            "$label: 'new';\n"
            "\n"
            ".title {\n"
            "  font-family: quote($family), sans-serif;\n"
            "}\n"
            "\n"
            ".badge::after {\n"
            "  content: to-upper-case($label);   // \"NEW\"\n"
            "  letter-spacing: str-length($label) * 1px; // 3px\n"
            "}\n"
            "\n"
            ".icon {\n"
            "  background-image: url('/img/' + $label + '.svg');\n"
            "}\n"
        ),
    ),

    Lesson(
        id="scss-basic-06-color-type",
        lang="scss", level="기초",
        title="색 타입",
        summary="hex·rgb·hsl 색과 채널 추출 함수",
        explanation=(
            "[개요]\n"
            "SCSS 는 색을 단순 문자열이 아닌 색 전용 타입으로 다룬다. 동일한 색을 여러 방식으로 표기할 수 있다.\n"
            "• #3498db          → 16진수(hex) 표기\n"
            "• rgb(52,152,219)  → 빨강·초록·파랑의 혼합량(0~255)으로 표기\n"
            "• hsl(...)         → 색상·채도·명도로 표기\n"
            "세 표기 모두 동일한 색을 나타낼 수 있으며, 표현 방식만 다르다.\n\n"
            "[색 성분 추출 함수]\n"
            "• red($c) / green($c) / blue($c)           → 빨강·초록·파랑 값을 추출한다(0~255).\n"
            "• hue($c) / saturation($c) / lightness($c) → 색상·채도·명도를 추출한다.\n"
            "• rgba($color, 0.5)                        → 기존 색에 투명도를 적용한다. 0.5 는 반투명을 의미한다.\n\n"
            "[색을 변수로 다루는 이유]\n"
            "• 브랜드 색 하나를 변수 $brand 에 정의하면, 그 색을 기준으로 연한 배경·반투명 테두리·그림자 색을 자동으로 파생시킬 수 있다.\n"
            "• 브랜드 색을 변경해도 변수 한 줄만 수정하면 파생된 색들이 모두 함께 변경된다.\n\n"
            "[예시 해설]\n"
            "• rgba($brand, 0.4)          → 브랜드색을 유지하며 40%만 불투명하게 만든다. 은은한 테두리에 적합하다.\n"
            "• hsl(hue($brand), 70%, 92%) → 브랜드색과 같은 색상이면서 명도를 92%로 높여 연한 배경색을 만든다.\n\n"
            "[유의 사항]\n"
            "• hsl 방식과 rgb 방식을 혼합하여 직접 계산하면 혼동하기 쉽다. '조금 더 어둡게' 같은 변형은 직접 계산하지 말고 전용 함수를 사용하는 것이 안전하다.\n"
            "• 컴파일 시 색 함수들은 모두 계산되어, 결과 CSS 에는 #ffffff 나 rgba(52,152,219,0.4) 같은 최종 색 값만 남는다."
        ),
        usage="브랜드색을 변수로 두고 투명도·성분을 조절해 테두리·그림자·반투명 배경 등을 파생시킬 때 쓴다.",
        cons="hsl 과 rgb 를 섞어 머릿속 계산을 하면 헷갈린다. 색 변형은 직접 계산보다 전용 함수를 쓰는 편이 안전하다.",
        code=(
            "$brand: #3498db;\n"
            "\n"
            ".panel {\n"
            "  background: $brand;\n"
            "  border-color: rgba($brand, 0.4);   // 같은 색, 40% 불투명\n"
            "}\n"
            "\n"
            ".shadow {\n"
            "  // 브랜드색의 RGB 성분으로 그림자 색 구성\n"
            "  box-shadow: 0 2px 6px rgba(red($brand), green($brand), blue($brand), 0.3);\n"
            "}\n"
            "\n"
            ".info {\n"
            "  // 같은 색상(hue)에 다른 명도로 연한 배경 만들기\n"
            "  background: hsl(hue($brand), 70%, 92%);\n"
            "}\n"
        ),
    ),

    Lesson(
        id="scss-basic-07-bool-list-type",
        lang="scss", level="기초",
        title="불리언·리스트 타입",
        summary="true/false 와 공백·쉼표로 구분한 리스트",
        explanation=(
            "[불리언(boolean)]\n"
            "불리언은 true(참) 또는 false(거짓) 두 가지 값만 갖는 타입이다.\n"
            "예: $dark-mode: true 는 다크모드가 활성화되었음을 의미한다.\n\n"
            "[불리언 관련 도구]\n"
            "• 비교 연산(>, <, ==)    → 두 값을 비교하여 참/거짓을 반환한다. 5 > 3 은 true.\n"
            "• and / or / not         → 조건을 조합한다. 'A 그리고 B', 'A 또는 B', 'A 가 아님'.\n"
            "• if($조건, 참값, 거짓값) → 조건이 참이면 참값을, 거짓이면 거짓값을 선택한다.\n"
            "  예: if($dark-mode, #1e1e1e, #ffffff) → 다크모드면 어두운 배경, 아니면 흰 배경.\n\n"
            "[리스트(list)]\n"
            "리스트는 여러 값을 나란히 담은 목록이다. 두 가지 구분 방식이 있다.\n"
            "• 공백 구분: 10px 20px 30px\n"
            "• 쉼표 구분: red, green, blue\n"
            "참고로 margin: 4px 8px 처럼 흔히 쓰는 CSS 축약값도 실제로는 리스트이다.\n\n"
            "[리스트에서 값 추출]\n"
            "• nth($list, 2) → 지정한 순번의 값을 추출한다. 2 는 두 번째 값이다(1부터 셈).\n"
            "• length($list) → 목록의 값 개수를 센다.\n\n"
            "[유의 사항]\n"
            "• 다른 언어와 달리 SCSS 에서는 0, 빈 문자열(''), 빈 리스트도 모두 참(true)으로 처리된다. 거짓으로 취급되는 값은 false 와 null 뿐이다.\n"
            "• '값이 있으면 참' 같은 방식으로 조건을 작성하면 오류가 발생할 수 있으므로, 조건은 명확하게 true/false 로 판단되도록 작성한다.\n"
            "• nth() 는 1부터 세므로, 두 번째 값을 원하면 2 를 입력한다(0 이 아님)."
        ),
        usage="옵션 on/off 를 불리언으로 두고 if() 로 값 분기하거나, 여러 값을 리스트로 묶어 순회·인덱싱할 때 쓴다.",
        cons="0, '', 빈 리스트도 SCSS 에선 참으로 취급되니(거짓은 false/null 뿐) 조건 작성에 주의한다.",
        code=(
            "$dark-mode: true;\n"
            "$sizes: 12px, 16px, 20px;   // 쉼표 리스트\n"
            "$inset: 4px 8px;            // 공백 리스트\n"
            "\n"
            ".page {\n"
            "  // 불리언에 따라 값 선택\n"
            "  background: if($dark-mode, #1e1e1e, #ffffff);\n"
            "  color: if($dark-mode, #f0f0f0, #222222);\n"
            "}\n"
            "\n"
            ".text {\n"
            "  font-size: nth($sizes, 2);     // 16px\n"
            "  padding: $inset;               // 4px 8px\n"
            "  // 리스트 길이를 이용한 값\n"
            "  z-index: length($sizes);       // 3\n"
            "}\n"
        ),
    ),

    Lesson(
        id="scss-basic-08-comment-default",
        lang="scss", level="기초",
        title="주석과 !default",
        summary="// 와 /* */ 차이, !default 로 기본값 지정",
        explanation=(
            "[주석(comment)]\n"
            "주석은 컴퓨터가 실행하지 않고 넘어가는, 사람을 위한 설명이다. 코드의 의도를 기록하면 유지보수에 도움이 된다.\n\n"
            "[SCSS 주석의 두 종류]\n"
            "• // 한 줄 주석      → 해당 줄만 주석 처리한다. 컴파일된 CSS 에는 남지 않는다. 개발용 메모에 사용한다.\n"
            "• /* 여러 줄 주석 */ → 여러 줄 주석 처리한다. 컴파일된 CSS 에도 그대로 남는다. 저작권·라이선스 표기 등 최종 결과에 남겨야 할 때 사용한다.\n\n"
            "[!default]\n"
            "!default 는 '해당 변수에 값이 없을 때만 이 값을 사용한다'는 표시이다.\n"
            "• $color: blue !default; → $color 가 이미 정의되어 있으면 이 줄은 무시되고, 정의되지 않은 경우에만 blue 가 적용된다.\n\n"
            "[!default 를 사용하는 이유]\n"
            "• 자신이 만든 컴포넌트를 다른 사람이 사용할 때를 위한 것이다.\n"
            "• 컴포넌트에 안전한 기본값을 !default 로 지정하되, 사용자가 미리 자신의 값을 정의했다면 그 값을 존중하여 덮어쓰지 않는다.\n"
            "• 이를 통해 기본값을 제공하면서도 필요 시 변경 가능한 유연한 컴포넌트를 만들 수 있다.\n\n"
            "[예시 흐름 (선언 순서가 중요)]\n"
            "• $primary: #e74c3c;          → 사용처에서 먼저 빨강을 정의함\n"
            "• $primary: #3498db !default; → 이미 값이 있으므로 이 줄은 무시됨 → 빨강(#e74c3c) 유지\n"
            "• $radius: 6px !default;      → radius 는 정의된 적 없으므로 → 6px 채택\n\n"
            "[유의 사항]\n"
            "• !default 는 값이 없을 때만 적용되므로 선언 순서가 중요하다. 기본값 줄을 먼저 쓰고 자신의 값을 나중에 쓰면 자신의 값으로 덮어써지므로 순서에 주의한다.\n"
            "• // 주석이 결과 CSS 에 남지 않는다는 점을 모르면 디버깅 시 혼동할 수 있다."
        ),
        usage="공유 컴포넌트의 설정값에 !default 를 달아, 사용처에서 덮어쓸 여지를 주면서 안전한 기본값을 보장할 때 쓴다.",
        cons="!default 는 '값이 없을 때만' 적용되므로 선언 순서가 중요하다. // 주석이 결과에 안 남는 점을 모르면 디버깅이 헷갈린다.",
        code=(
            "/* 이 주석은 컴파일된 CSS 에도 남는다. */\n"
            "// 이 주석은 결과 CSS 에 남지 않는다.\n"
            "\n"
            "$primary: #e74c3c;          // 사용처에서 먼저 정한 값\n"
            "$primary: #3498db !default; // 이미 있으므로 무시됨 → #e74c3c 유지\n"
            "$radius: 6px !default;      // 없었으므로 6px 적용\n"
            "\n"
            ".btn {\n"
            "  background: $primary;     // #e74c3c\n"
            "  border-radius: $radius;   // 6px\n"
            "}\n"
        ),
    ),

    # ───────────────────────── 중급 ─────────────────────────

    Lesson(
        id="scss-mid-04-extend",
        lang="scss", level="중급",
        title="@extend",
        summary="다른 선택자의 스타일을 상속받아 묶기",
        explanation=(
            "[개요]\n"
            "@extend 는 한 스타일이 다른 스타일을 상속받게 하는 도구이다.\n"
            "• .error { @extend .message; } → .error 는 .message 의 스타일을 모두 상속받고, 자신의 색만 추가로 정의한다.\n\n"
            "[@include(믹스인)와의 차이]\n"
            "두 방식은 결과가 다르다.\n"
            "• @include → 스타일 코드를 복사하여 붙여넣는다. 같은 규칙이 여러 번 중복된다.\n"
            "• @extend  → 코드를 복사하는 대신 선택자들을 한 곳으로 모아 쉼표로 묶는다.\n"
            "@extend 의 출력 예시:\n"
            "  .message, .success, .error { 공통 규칙 }   ← 세 선택자가 한 규칙을 공유\n"
            "  .success { color: 초록 }                    ← 자신만의 색은 별도\n"
            "공통 규칙을 한 번만 출력하므로, 복사 방식보다 결과 CSS 크기가 작아진다.\n\n"
            "[사용 목적]\n"
            "• 메시지 박스, 버튼 골격처럼 공통 구조를 여러 변형(성공/경고/에러)이 공유할 때 적합하다.\n"
            "• 패딩·테두리·모서리 등 공통 부분은 한 번만 정의하고 각 변형은 색만 다르게 하여 코드를 간결하게 유지한다.\n\n"
            "[예시 해설]\n"
            "• .message → 공통 골격(패딩, 테두리, 둥근 모서리)\n"
            "• .success → @extend .message 로 골격 상속 + 초록색\n"
            "• .error   → @extend .message 로 골격 상속 + 빨간색\n\n"
            "[유의 사항]\n"
            "• @extend 는 같은 규칙에 선택자 이름이 연쇄적으로 붙어, 결과가 복잡하고 예측하기 어려워질 수 있다.\n"
            "• 실무에서는 다음 레슨의 % placeholder(출력되지 않는 전용 골격)와 함께 사용하는 것이 더 간결하다."
        ),
        usage="여러 변형(성공/경고/에러)이 공통 골격을 공유할 때, 출력 크기를 줄이며 묶고 싶을 때 쓴다.",
        cons="@extend 는 같은 규칙에 선택자가 줄줄이 붙어 결과가 예상보다 복잡해질 수 있다. 보통은 % placeholder 와 함께 쓴다.",
        code=(
            ".message {\n"
            "  padding: 12px 16px;\n"
            "  border: 1px solid;\n"
            "  border-radius: 4px;\n"
            "}\n"
            "\n"
            ".success {\n"
            "  @extend .message;\n"
            "  color: #2ecc71;\n"
            "}\n"
            "\n"
            ".error {\n"
            "  @extend .message;\n"
            "  color: #e74c3c;\n"
            "}\n"
        ),
    ),

    Lesson(
        id="scss-mid-05-placeholder",
        lang="scss", level="중급",
        title="placeholder 선택자(%)",
        summary="%이름 으로 출력 안 되는 재사용 전용 베이스",
        explanation=(
            "[개요]\n"
            "%이름 으로 정의하는 placeholder 는 상속 전용으로만 존재하는 스타일 틀이다.\n"
            "%card 자체는 결과 CSS 에 출력되지 않으며, 오직 @extend %card 로 사용할 때만 해당 스타일이 사용처에 병합된다.\n\n"
            "[일반 클래스 @extend 와의 차이]\n"
            "• 일반 클래스(.message)를 @extend 하면 .message 규칙 자체도 결과에 남는다(사용하지 않아도 출력됨).\n"
            "• placeholder(%card)는 아무도 상속하지 않으면 결과에 전혀 출력되지 않는다.\n"
            "정리하면 다음과 같다.\n"
            "  일반 클래스 → 사용하지 않아도 결과에 남음\n"
            "  % placeholder → 사용하지 않으면 출력되지 않음\n\n"
            "[사용 목적]\n"
            "• 버튼·카드·메시지의 공통 골격을 %base 로 정의하고, 여러 변형이 @extend 로 상속하는 패턴이 표준이다.\n"
            "• 라이브러리 제작 시 특히 유용하다. 골격을 제공하되 사용되지 않으면 불필요한 코드가 결과에 남지 않기 때문이다.\n\n"
            "[예시 해설]\n"
            "• %card       → 카드 공통 골격(패딩, 둥근 모서리, 그림자). 자체는 결과에 출력되지 않음\n"
            "• .card-light → @extend %card + 흰 배경\n"
            "• .card-dark  → @extend %card + 어두운 배경\n"
            "결과적으로 .card-light, .card-dark 만 공통 규칙을 공유하며 출력된다.\n\n"
            "[유의 사항]\n"
            "• placeholder 는 @media(반응형) 등 다른 맥락을 넘나드는 @extend 에 제약이 있다. 서로 다른 미디어 안팎을 연결하지 못한다.\n"
            "• placeholder 는 고정된 스타일 덩어리이므로, 인자를 받아 매번 다르게 생성하려면 사용할 수 없다. 그 경우 믹스인(@mixin)을 사용해야 한다."
        ),
        usage="여러 곳에서 상속할 공통 스타일을 '클래스 출력 없이' 정의하고 싶을 때(라이브러리 베이스) 쓴다.",
        cons="placeholder 는 @media 등 다른 맥락을 넘나드는 @extend 에 제약이 있다. 동적 인자가 필요하면 믹스인이 낫다.",
        code=(
            "%card {\n"
            "  padding: 16px;\n"
            "  border-radius: 8px;\n"
            "  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.15);\n"
            "}\n"
            "\n"
            ".card-light {\n"
            "  @extend %card;\n"
            "  background: #ffffff;\n"
            "  color: #222222;\n"
            "}\n"
            "\n"
            ".card-dark {\n"
            "  @extend %card;\n"
            "  background: #2c3e50;\n"
            "  color: #ecf0f1;\n"
            "}\n"
        ),
    ),

    Lesson(
        id="scss-mid-06-nested-properties",
        lang="scss", level="중급",
        title="중첩 속성(nested properties)",
        summary="font·margin 등 접두어가 같은 속성 묶기",
        explanation=(
            "[개요]\n"
            "CSS 속성 중에는 접두어가 반복되는 것들이 많다.\n"
            "예: font-family, font-size, font-weight 는 'font-' 가 반복되고, margin-top, margin-bottom 은 'margin-' 이 반복된다.\n"
            "중첩 속성은 이 반복되는 접두어를 한 번만 쓰고 묶는 문법이다.\n\n"
            "[사용 방법]\n"
            "'접두어: { ... }' 형태로 접두어를 한 번 쓰고, 중괄호 안에는 뒷부분만 기재한다.\n"
            "  font: {\n"
            "    family: serif;   → font-family: serif 로 변환됨\n"
            "    size: 14px;      → font-size: 14px 로 변환됨\n"
            "  }\n"
            "축약값과 세부값을 함께 지정할 수도 있다.\n"
            "  border: 1px solid #ccc { radius: 6px; } → border 는 축약으로, border-radius 는 세부로 한 번에 지정\n\n"
            "[사용 목적]\n"
            "• font-, margin- 처럼 같은 계열 속성이 여러 개 모여 있을 때 시각적으로 묶어주면 가독성이 향상된다.\n"
            "• margin/padding/border/background 등 접두어를 공유하는 속성군에 두루 사용할 수 있다.\n\n"
            "[유의 사항]\n"
            "• 이 문법은 가독성을 위한 문법 설탕(syntactic sugar)이다. 컴파일 시 font-family, font-size 같은 일반 CSS 로 풀어지며, 성능이나 결과에는 차이가 없다.\n"
            "• 속성이 한두 개뿐이라면 묶지 않고 font-size: 14px 처럼 펼쳐 쓰는 편이 더 간단하다. 3개 이상 모일 때 효과적이다."
        ),
        usage="같은 접두어 속성이 여러 개일 때(font-*, margin-*) 묶어서 보기 좋게 정리할 때 쓴다.",
        cons="실제 출력은 풀어지므로 성능·결과엔 차이가 없다. 한두 개뿐이면 그냥 펴서 쓰는 게 더 간단하다.",
        code=(
            ".title {\n"
            "  font: {\n"
            "    family: 'Georgia', serif;\n"
            "    size: 20px;\n"
            "    weight: bold;\n"
            "  }\n"
            "  margin: {\n"
            "    top: 8px;\n"
            "    bottom: 16px;\n"
            "  }\n"
            "}\n"
            "\n"
            ".thumb {\n"
            "  // 축약 값 + 세부 속성 함께\n"
            "  border: 1px solid #ccc {\n"
            "    radius: 6px;\n"
            "  }\n"
            "}\n"
        ),
    ),

    Lesson(
        id="scss-mid-07-interpolation",
        lang="scss", level="중급",
        title="보간 #{}",
        summary="변수를 선택자·속성명·값 어디에나 끼워넣기",
        explanation=(
            "[개요]\n"
            "보간 #{$변수} 는 변수의 값을 코드의 임의 위치에 삽입하는 도구이다.\n\n"
            "[일반 변수 사용과의 차이]\n"
            "• 단순히 값으로 사용할 때  → 보간이 필요 없다. color: $brand 처럼 변수만 쓰면 된다.\n"
            "• 이름을 동적으로 만들 때  → 보간이 필요하다. 변수를 직접 넣을 수 없는 위치이기 때문이다.\n"
            "변수를 직접 넣을 수 없는 위치란 선택자 이름, 속성 이름, 미디어 조건 등이다. 이런 위치에는 #{} 로 감싸야 값이 삽입된다.\n\n"
            "[삽입 가능 위치]\n"
            "• 선택자 이름: .icon-#{$name} { }  → $name 이 home 이면 .icon-home 클래스가 생성됨\n"
            "• 속성 이름:   margin-#{$side}: 8px → $side 가 left 면 margin-left: 8px 가 됨\n"
            "• 값 합성:     content: 'v#{$n}'   → $n 이 3 이면 'v3' 문자열이 됨\n"
            "• 숫자+단위:   width: #{$n * 10}px → 계산한 30 에 px 를 붙여 30px 가 됨\n\n"
            "[사용 목적]\n"
            "• 반복문(@each, @for)과 결합할 때 효과적이다. 방향(left/right/top/bottom)마다 margin-left, margin-right 등을 자동으로 생성할 수 있다.\n"
            "• 각 항목을 직접 작성하지 않고 변수를 바꿔가며 이름을 생성할 수 있어 반복 작업이 크게 줄어든다.\n\n"
            "[유의 사항]\n"
            "• 값이 들어가도 되는 위치(예: color 값)에까지 보간을 사용하면, 따옴표 처리나 값의 타입이 꼬여 문제가 발생할 수 있다.\n"
            "• 보간은 이름을 생성해야 할 때만 사용하고, 단순 값은 변수를 직접 사용한다. 필요한 곳에만 사용하는 것이 요령이다."
        ),
        usage="반복문과 함께 클래스 이름·방향별 속성을 동적으로 생성하거나, 값에 단위를 합칠 때 쓴다.",
        cons="값이 들어가도 되는 자리에까지 무분별하게 보간을 쓰면 따옴표 처리·타입이 꼬일 수 있다. 필요한 곳에만 쓴다.",
        code=(
            "$name: home;\n"
            "$side: left;\n"
            "$n: 3;\n"
            "\n"
            "// 선택자 이름에 보간\n"
            ".icon-#{$name} {\n"
            "  // 속성 이름에 보간\n"
            "  margin-#{$side}: 8px;\n"
            "  // 값 문자열에 보간\n"
            "  content: 'step #{$n}';\n"
            "  // 숫자+단위 합성\n"
            "  width: #{$n * 10}px;\n"
            "}\n"
        ),
    ),

    Lesson(
        id="scss-mid-08-color-functions",
        lang="scss", level="중급",
        title="색 함수 심화",
        summary="adjust-hue·saturate·scale-color·complement",
        explanation=(
            "[개요]\n"
            "색 함수는 기존 색을 변형하여 새로운 색을 생성하는 도구이다. 색을 밝게·어둡게·선명하게 조절할 수 있다.\n"
            "가장 기본인 lighten(밝게)/darken(어둡게) 외에도 정교한 변형 함수가 여럿 있다.\n\n"
            "[주요 함수]\n"
            "• adjust-hue($c, 30deg)             → 색상환을 30도 회전하여 다른 색조로 변경한다.\n"
            "• saturate($c, 20%)                 → 채도를 높여 색을 더 선명하게 만든다. desaturate 는 반대로 채도를 낮춘다.\n"
            "• complement($c)                    → 보색(색상환의 정반대편 색)을 반환한다. 강조 포인트에 적합하다.\n"
            "• scale-color($c, $lightness: -20%) → 현재 밝기를 기준으로 남은 여유의 20%만큼 부드럽게 어둡게 만든다.\n"
            "• transparentize($c, 0.85)          → 투명도를 높인다. opacify 는 반대로 불투명도를 높인다.\n\n"
            "[scale-color 가 자연스러운 이유]\n"
            "• lighten 은 고정량(예: 20%)을 더하므로, 이미 밝은 색에 사용하면 지나치게 하얗게 될 수 있다.\n"
            "• 반면 scale-color 는 남은 여유 공간의 비율만큼만 조절한다. 이미 80% 밝은 색이면 남은 20%의 일부만 조절하므로 넘치지 않고 자연스럽다.\n\n"
            "[사용 목적]\n"
            "• 기준색 하나만 정하면 호버 색(hover)·액티브 색(active)·강조색(보색) 등을 자동으로 파생시킬 수 있다.\n"
            "• 색 간 통일감이 생기고, 기준색만 변경하면 파생색이 모두 함께 변경되어 관리가 용이하다.\n\n"
            "[유의 사항]\n"
            "• 함수 종류가 많아 결과 색을 사전에 예측하기 어렵다. 초기에는 값을 조금씩 변경하며 눈으로 확인하는 것이 좋다.\n"
            "• 최신 dart-sass 에서는 이 함수들이 color.adjust / color.scale 같은 모듈 함수 형태로 변경되었다. libsass 환경에서는 위의 전역 함수 이름을 그대로 사용한다."
        ),
        usage="기준색 하나에서 호버/액티브/보색 등 일관된 색 변형을 자동으로 만들 때 쓴다.",
        cons="함수 종류가 많아 결과를 머릿속으로 가늠하기 어렵다. dart-sass 에선 color.adjust/scale 등 모듈 함수로 대체된다.",
        code=(
            "$brand: #3498db;\n"
            "\n"
            ".btn {\n"
            "  background: $brand;\n"
            "\n"
            "  &:hover {\n"
            "    // 여유 비율만큼 자연스럽게 어둡게\n"
            "    background: scale-color($brand, $lightness: -12%);\n"
            "  }\n"
            "\n"
            "  &:active {\n"
            "    background: saturate($brand, 15%);\n"
            "  }\n"
            "}\n"
            "\n"
            ".accent {\n"
            "  color: complement($brand);        // 보색\n"
            "  border-color: adjust-hue($brand, 40deg);\n"
            "  background: transparentize($brand, 0.85);\n"
            "}\n"
        ),
    ),

    # ───────────────────────── 고급 ─────────────────────────

    Lesson(
        id="scss-adv-04-function-advanced",
        lang="scss", level="고급",
        title="@function 심화(기본값·이름인자)",
        summary="여러 인자·기본값·이름 지정 호출과 재귀",
        explanation=(
            "[개요]\n"
            "@function 은 값을 계산하여 반환하는 사용자 정의 함수이다. 인자를 입력하면 계산 결과 하나를 @return 으로 반환한다.\n"
            "예: space(2) 를 입력하면 16px 을 반환한다.\n\n"
            "[인자 처리 방법]\n"
            "• 기본값:    @function space($n, $unit: 8px) → $unit 을 전달하지 않으면 자동으로 8px 을 사용한다.\n"
            "• 이름 인자: space($n: 3)                    → 인자에 이름을 붙여 전달한다. 순서에 무관하며 의미가 명확해진다.\n"
            "• 분기:      함수 내부에서 @if / @else 로 경우를 나누어 다르게 계산할 수 있다.\n"
            "• 재귀:      함수가 자기 자신을 다시 호출하는 것. 거듭제곱처럼 같은 계산을 반복할 때 사용한다.\n\n"
            "[재귀]\n"
            "재귀는 함수가 자기 자신을 호출하며 반복하는 기법이다. 예시의 pow(거듭제곱)는 @for 반복으로 base 를 exp 번 곱한다.\n"
            "• pow(2, 5) → 2를 5번 곱함 → 2×2×2×2×2 = 32\n\n"
            "[사용 목적]\n"
            "• 간격 스케일, 단위 변환, 거듭제곱 등 '입력→값'이 명확한 계산 로직을 함수로 포장하면 여러 곳에서 재사용할 수 있다.\n"
            "• 매번 직접 8×2, 8×3 을 계산하는 대신 space(2), space(3) 으로 호출하면 실수가 줄고 의도가 명확해진다.\n\n"
            "[예시 해설]\n"
            "• space(2)       → 2 × 8px = 16px (기본 단위 8px 사용)\n"
            "• space($n: 3)   → 이름 인자로 3 → 24px\n"
            "• space(2, 10px) → 단위를 10px 로 지정 → 20px\n"
            "• pow(2, 5)      → 재귀/반복으로 → 32\n\n"
            "[유의 사항]\n"
            "• 재귀나 복잡한 @if 분기는 흐름을 추적하기 어려워 디버깅이 힘들다. 함수는 값만 계산하는 순수한 용도로만 사용한다.\n"
            "• 함수는 값 하나만 반환한다. 여러 CSS 선언(색·테두리 등 여러 줄)을 한꺼번에 삽입하려면 함수가 아니라 믹스인(@mixin)을 사용해야 한다."
        ),
        usage="간격 스케일·단위 변환·반복 계산처럼 '입력→값'이 명확한 로직을 함수로 묶어 재사용할 때 쓴다.",
        cons="재귀나 복잡한 분기는 디버깅이 어렵다. 부수효과 없는 순수 계산에만 쓰고, 선언 묶음은 믹스인을 쓴다.",
        code=(
            "// 기본값을 가진 함수\n"
            "@function space($n, $unit: 8px) {\n"
            "  @return $n * $unit;\n"
            "}\n"
            "\n"
            "// 재귀로 거듭제곱 계산\n"
            "@function pow($base, $exp) {\n"
            "  $result: 1;\n"
            "  @for $i from 1 through $exp {\n"
            "    $result: $result * $base;\n"
            "  }\n"
            "  @return $result;\n"
            "}\n"
            "\n"
            ".box {\n"
            "  padding: space(2);          // 16px\n"
            "  margin: space($n: 3);       // 이름 인자 → 24px\n"
            "  gap: space(2, 10px);        // 20px\n"
            "  z-index: pow(2, 5);         // 32\n"
            "}\n"
        ),
    ),

    Lesson(
        id="scss-adv-05-list-map-functions",
        lang="scss", level="고급",
        title="리스트·맵 함수",
        summary="length·nth·append·map-keys·map-merge",
        explanation=(
            "[개요]\n"
            "리스트와 맵은 두 가지 자료 구조이다.\n"
            "• 리스트(list) → 값을 순서대로 나열한 목록. 예: 12px 16px 20px. 순번으로 접근한다.\n"
            "• 맵(map)      → '이름표: 값' 쌍으로 묶은 사전. 예: (primary: 파랑, danger: 빨강). 이름으로 접근한다.\n\n"
            "[리스트 함수]\n"
            "• length($l)    → 목록의 값 개수를 센다.\n"
            "• nth($l, 2)    → 2번째 값을 추출한다(1부터 셈).\n"
            "• index($l, 값) → 해당 값이 몇 번째에 있는지 위치를 반환한다.\n"
            "• append($l, 값)→ 목록 끝에 값을 하나 추가한다.\n"
            "• join($a, $b)  → 두 목록을 이어 붙여 하나로 만든다.\n\n"
            "[맵 함수]\n"
            "• map-get($m, primary) → 'primary' 이름표의 값을 추출한다.\n"
            "• map-has-key($m, 키)  → 해당 이름표의 존재 여부를 확인한다(참/거짓).\n"
            "• map-keys / map-values→ 모든 이름표 / 모든 값의 목록을 반환한다.\n"
            "• map-merge($a, $b)    → 두 사전을 합쳐 하나로 만든다.\n\n"
            "[사용 목적]\n"
            "• 디자인 토큰(색·간격 등 규칙 값 모음)을 맵에 담고 @each/@for 반복문과 결합하면 유틸리티 클래스를 대량으로 자동 생성할 수 있다.\n"
            "• 예: 색 맵을 순회하며 .bg-primary, .bg-danger, .bg-success 를 자동으로 생성할 수 있다. 수동으로 여러 개를 작성할 작업을 몇 줄로 처리한다.\n\n"
            "[예시 흐름]\n"
            "• map-merge($base-colors, $extra) → 기본 색 사전에 success 를 추가로 병합\n"
            "• @each $name, $color in $colors  → 병합한 사전을 순회하며 .bg-이름 클래스를 자동 생성\n"
            "• append($sizes, 24px)            → 크기 목록 끝에 24px 추가 → 4개\n\n"
            "[유의 사항]\n"
            "• 존재하지 않는 이름표를 map-get 으로 추출하면 에러 없이 null(빈 값)을 반환한다. 따라서 키에 오타가 있어도 감지되지 않고 값이 비어버릴 수 있다.\n"
            "• 이런 오류를 방지하려면 추출 전에 map-has-key 로 존재 여부를 먼저 확인하는 것이 안전하다."
        ),
        usage="디자인 토큰(색·간격 맵)을 병합·확장하거나, 리스트를 가공해 클래스 세트를 만들 때 쓴다.",
        cons="없는 키를 map-get 하면 에러 없이 null 이 나와 조용히 빈 값이 될 수 있다. 키 오타에 주의한다.",
        code=(
            "$base-colors: (primary: #3498db, danger: #e74c3c);\n"
            "$extra: (success: #2ecc71);\n"
            "\n"
            "// 두 맵 병합\n"
            "$colors: map-merge($base-colors, $extra);\n"
            "\n"
            "// 병합된 맵을 순회해 유틸리티 생성\n"
            "@each $name, $color in $colors {\n"
            "  .bg-#{$name} { background: $color; }\n"
            "}\n"
            "\n"
            "// 리스트 함수\n"
            "$sizes: 12px 16px 20px;\n"
            "$sizes: append($sizes, 24px);   // 4개\n"
            "\n"
            ".text {\n"
            "  font-size: nth($sizes, 4);     // 24px\n"
            "  z-index: length($sizes);       // 4\n"
            "}\n"
        ),
    ),

    Lesson(
        id="scss-adv-06-conditional-mixin",
        lang="scss", level="고급",
        title="@if 조건 믹스인",
        summary="인자에 따라 다른 스타일을 내는 믹스인",
        explanation=(
            "[개요]\n"
            "믹스인(@mixin)은 스타일 묶음을 생성하는 도구이다. 여기에 @if / @else 를 추가하면 전달한 값에 따라 다른 스타일을 생성할 수 있다.\n"
            "예: button(primary) 를 호출하면 파란 채움 버튼, button(ghost) 를 호출하면 테두리만 있는 투명 버튼이 생성된다.\n\n"
            "[조건 도구]\n"
            "• @if $type == primary    → type 이 primary 이면 이 안의 스타일을 적용한다.\n"
            "• @else if $type == ghost → 그렇지 않고 ghost 이면 다른 스타일을 적용한다.\n"
            "• @else                   → 위 어느 것도 아니면 이 스타일을 적용한다(기본값 처리).\n"
            "• not / and / or          → 조건을 반전하거나 조합한다.\n"
            "• @error                  → 잘못된 값이 입력되면 컴파일을 중단하여 실수를 즉시 알린다.\n\n"
            "[함수와의 차이]\n"
            "• @function   → 값 하나를 선택하여 반환한다(예: 24px 한 개).\n"
            "• 조건 @mixin → 여러 줄의 CSS 선언을 선택하여 통째로 삽입한다(배경+색+테두리 세트).\n"
            "즉, 결과가 값 하나면 함수, 스타일 여러 줄이면 믹스인을 사용한다.\n\n"
            "[사용 목적]\n"
            "• 버튼·배지처럼 종류/크기/상태만 다른 여러 변형을 만들 때 적합하다. 인자 하나만 바꿔 button(primary), button(ghost) 로 호출하면 각기 다른 버튼이 생성된다.\n"
            "• 디자인 시스템(통일된 UI 부품 모음)을 만들 때 이 패턴이 표준이다. 변형마다 코드를 복사할 필요가 없다.\n\n"
            "[유의 사항]\n"
            "• 분기(@if 갈래)가 많아지면 믹스인 하나가 지나치게 커지고 복잡해져 관리가 어려워진다.\n"
            "• 경우의 수가 급증하면 변형별로 믹스인을 분리하거나, 맵(map)에 설정을 담아 처리하는 방식으로 전환하는 것이 더 간결하다."
        ),
        usage="버튼·배지의 변형(종류/크기/상태)을 인자 하나로 분기 생성하는 디자인 시스템 믹스인에 쓴다.",
        cons="분기가 많아지면 믹스인이 비대해진다. 경우의 수가 폭증하면 변형별로 쪼개거나 맵 기반으로 바꾸는 게 낫다.",
        code=(
            "@mixin button($type: primary) {\n"
            "  padding: 8px 16px;\n"
            "  border-radius: 4px;\n"
            "\n"
            "  @if $type == primary {\n"
            "    background: #3498db;\n"
            "    color: #fff;\n"
            "    border: none;\n"
            "  } @else if $type == ghost {\n"
            "    background: transparent;\n"
            "    color: #3498db;\n"
            "    border: 1px solid #3498db;\n"
            "  } @else {\n"
            "    background: #eee;\n"
            "    color: #333;\n"
            "  }\n"
            "}\n"
            "\n"
            ".btn-primary { @include button(primary); }\n"
            ".btn-ghost   { @include button(ghost); }\n"
            ".btn-default { @include button(default); }\n"
        ),
    ),

    Lesson(
        id="scss-adv-07-content",
        lang="scss", level="고급",
        title="@content",
        summary="믹스인에 임의의 스타일 블록을 끼워넣기",
        explanation=(
            "[개요]\n"
            "일반적으로 믹스인은 정해진 스타일을 생성한다. 그러나 @content 를 사용하면 믹스인을 호출할 때 원하는 스타일 블록을 함께 전달하여 믹스인 내부에 삽입할 수 있다.\n"
            "• @include respond(mobile) { color: red; } → { color: red } 부분이 전달한 내용이며, 믹스인 내부의 @content 위치에 그대로 펼쳐진다.\n\n"
            "[대표 활용: 미디어쿼리(반응형) 래퍼]\n"
            "가장 대표적인 용도이다. 화면 크기별 스타일을 지정하는 @media 조건은 길고 반복적이다.\n"
            "복잡한 @media (max-width: ...) 부분을 믹스인이 감추고, 사용자는 내부에 들어갈 규칙만 작성한다.\n"
            "• 복잡한 방식: @media (max-width: 600px) { .container { padding: 0 12px; } }\n"
            "• 간결한 방식: @include respond(mobile) { padding: 0 12px; }  ← @media 는 믹스인이 처리\n"
            "이를 통해 화면 크기 기준(600px 등)을 한 곳에서 관리하고 가독성도 향상된다.\n\n"
            "[예시 흐름]\n"
            "• $breakpoints                 → 화면 크기 기준을 이름으로 정리한 맵 (mobile: 600px 등)\n"
            "• map-get($breakpoints, $name) → 전달된 이름(tablet)으로 해당 픽셀(900px)을 추출\n"
            "• @content                     → 호출 시 전달한 { width: 100% } 같은 블록이 이 위치에 삽입됨\n"
            "결과적으로 각 블록이 알맞은 @media 안에 삽입되어 출력된다.\n\n"
            "[기타 활용]\n"
            "• :hover 같은 상태 래퍼, 다크/라이트 테마 스코프 래퍼처럼 바깥 틀은 동일하고 내부 내용만 다른 패턴에 두루 적합하다.\n\n"
            "[유의 사항]\n"
            "• @content 로 전달한 블록 안에서는 믹스인 내부 변수(예: $w)를 직접 참조하기 어렵다. 스코프(변수가 유효한 범위)가 분리되어 있기 때문이다. 전달하는 블록은 자기 바깥의 변수를 사용한다고 간주한다.\n"
            "• 래퍼 안에 또 래퍼를 넣는 식으로 중첩이 깊어지면 최종 결과의 위치를 추적하기 어려워지므로 적절히 사용한다."
        ),
        usage="미디어쿼리·상태·테마처럼 '바깥 틀은 같고 안 내용만 다른' 패턴을 한 줄 호출로 묶을 때 쓴다.",
        cons="@content 로 넘긴 블록 안에서 믹스인 내부 변수를 직접 보긴 어렵다(스코프 분리). 중첩이 깊어지면 추적이 힘들다.",
        code=(
            "$breakpoints: (mobile: 600px, tablet: 900px);\n"
            "\n"
            "@mixin respond($name) {\n"
            "  $w: map-get($breakpoints, $name);\n"
            "  @media (max-width: $w) {\n"
            "    @content;   // 호출 시 넘긴 블록이 여기에 들어감\n"
            "  }\n"
            "}\n"
            "\n"
            ".container {\n"
            "  width: 1080px;\n"
            "\n"
            "  @include respond(tablet) {\n"
            "    width: 100%;\n"
            "  }\n"
            "\n"
            "  @include respond(mobile) {\n"
            "    padding: 0 12px;\n"
            "  }\n"
            "}\n"
        ),
    ),

    Lesson(
        id="scss-adv-08-math-functions",
        lang="scss", level="고급",
        title="수학 함수(math)",
        summary="floor·ceil·round·abs·min·max·percentage",
        explanation=(
            "[개요]\n"
            "수학 함수는 숫자를 다듬거나 선택하는 계산 도구이다.\n"
            "화면 계산 시 333.3333px 같은 소수가 발생하는데, 이를 정수 픽셀로 정리해야 화면이 흐릿하지 않고 또렷하게 표시된다.\n\n"
            "[주요 함수]\n"
            "• floor(333.9)      → 내림. 소수점을 버리고 아래로 → 333.\n"
            "• ceil(333.1)       → 올림. 위로 → 334.\n"
            "• round(15.5)       → 반올림. 가까운 정수로 → 16.\n"
            "• abs(-12px)        → 절댓값. 부호를 제거하고 크기만 → 12px.\n"
            "• min(300px, 240px) → 여러 값 중 최솟값 → 240px.\n"
            "• max(80px, 120px)  → 여러 값 중 최댓값 → 120px.\n"
            "• percentage(0.25)  → 비율(0.25)을 % 로 변환 → 25%.\n\n"
            "[사용 목적]\n"
            "• 화면을 3칸으로 나누면 1000 ÷ 3 = 333.333... 처럼 나누어떨어지지 않는다. 이를 그대로 두면 픽셀이 어긋나 화면이 지저분해진다.\n"
            "• floor 로 333px 로 정리하고, 값의 상한/하한을 제한할 때는 min/max 로 한계를 지정한다.\n"
            "• 그리드 칸 너비 계산, 반응형 글자 크기 상한/하한, 정수 픽셀 보정 등에 두루 사용된다.\n\n"
            "[예시 해설]\n"
            "• floor($total / $cols) → 1000/3 = 333.33... → 내림 → 333px\n"
            "• percentage(2 / $cols) → 2/3 = 0.666... → 66.6667%\n"
            "• min(300px, 240px)     → 둘 중 작은 240px (최대 너비 제한 등에 활용)\n\n"
            "[유의 사항]\n"
            "• libsass 환경에서는 위 전역 함수(floor, ceil, round 등)와 / 나눗셈을 그대로 사용하면 된다.\n"
            "• 최신 dart-sass 로 이전하면 규칙이 변경된다. 나눗셈은 a / b 대신 math.div(a, b) 로, 수학 함수는 @use 'sass:math'; 를 불러온 뒤 math.floor(...) 처럼 'math.' 접두어를 붙여 사용해야 한다. 환경 변경 시 이 부분을 수정해야 한다."
        ),
        usage="컬럼 너비 반올림, 여러 값 중 최소·최대 선택(min/max), 비율의 % 변환 등 수치 가공에 쓴다.",
        cons="dart-sass 로 옮기면 나눗셈은 math.div() 로, 전역 수학 함수는 math 모듈 함수로 바꿔야 한다.",
        code=(
            "$cols: 3;\n"
            "$total: 1000px;\n"
            "\n"
            ".col {\n"
            "  // 1000 / 3 = 333.33... → 내림으로 정수 픽셀\n"
            "  width: floor($total / $cols);   // 333px\n"
            "}\n"
            "\n"
            ".bar {\n"
            "  width: percentage(2 / $cols);   // 66.6667%\n"
            "  height: round(15.5px);          // 16px\n"
            "  margin-left: abs(-12px);        // 12px\n"
            "}\n"
            "\n"
            ".limit {\n"
            "  // 여러 값 중 최소·최대 선택\n"
            "  width: min(300px, 240px);   // 240px\n"
            "  height: max(80px, 120px);   // 120px\n"
            "}\n"
        ),
    ),
]
