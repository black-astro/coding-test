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
            "SCSS 의 숫자는 단위를 가질 수 있다(16px, 1.5rem, 50%, 그리고 단위 없는 3 도 가능).\n"
            "- 같은 단위끼리 더하고 뺄 수 있다: 16px + 4px = 20px.\n"
            "- 숫자(단위 없음)를 곱하면 단위가 유지된다: 8px * 2 = 16px.\n"
            "- percentage(0.25) 처럼 비율을 % 로 바꾸는 내장 함수도 있다.\n"
            "단, 서로 다른 단위(px + em)를 더하면 에러가 나므로 단위를 맞춰야 한다.\n"
            "기준값을 변수에 담고 배수로 간격 단계를 만들면 일관된 리듬을 얻는다.\n"
            "컴파일하면 식은 모두 계산되어 실제 수치가 박힌 CSS 가 된다."
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
            "SCSS 문자열은 따옴표가 있는 것('hello')과 없는 것(bold)이 모두 가능하다.\n"
            "- quote(x) 는 따옴표를 붙이고, unquote('x') 는 따옴표를 뗀다.\n"
            "- to-upper-case / to-lower-case 로 대소문자를 바꾸고, str-length 로 길이를 잰다.\n"
            "글꼴 이름, content 값, url 경로 등은 문자열로 다룬다.\n"
            "따옴표 없는 문자열은 keyword 처럼 동작해 속성 값(예: bold, sans-serif)으로 그대로 쓰기 좋다.\n"
            "보간 #{$var} 안에서 문자열을 합쳐 클래스 이름이나 경로를 동적으로 만들 수도 있다.\n"
            "컴파일 결과에는 함수가 적용된 최종 문자열이 들어간다."
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
            "SCSS 는 색을 하나의 '타입'으로 다룬다. #3498db, rgb(...), hsl(...) 은 모두 같은 색 값이 될 수 있다.\n"
            "색에서 성분을 꺼내는 내장 함수가 있다.\n"
            "- red()/green()/blue(): RGB 채널 값(0~255).\n"
            "- hue()/saturation()/lightness(): HSL 성분.\n"
            "- rgba($color, 0.5): 기존 색에 투명도를 입힌다.\n"
            "변수에 기준색을 담아두고, 함수로 성분을 읽거나 투명도를 조절해 일관된 색 체계를 만든다.\n"
            "컴파일하면 색 함수가 계산되어 최종 색 값(hex/rgba 등)으로 출력된다."
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
            "SCSS 에는 참/거짓을 나타내는 불리언(true/false)이 있다.\n"
            "- 비교 연산(>, <, ==)과 and/or/not 으로 조합한다.\n"
            "- if($조건, 참값, 거짓값) 함수로 조건에 따라 값을 고를 수 있다.\n"
            "리스트는 여러 값을 나열한 자료형이다.\n"
            "- 공백 구분: 10px 20px 30px, 쉼표 구분: red, green, blue.\n"
            "- nth($list, 1) 로 n 번째 값을, length($list) 로 개수를 얻는다.\n"
            "이미 margin: 4px 8px 같은 CSS 단축 값 자체가 리스트라는 점을 알면 이해가 쉽다.\n"
            "컴파일 결과에는 선택된 값/꺼낸 값이 그대로 들어간다."
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
            "SCSS 주석은 두 가지다.\n"
            "- // 한 줄 주석: 컴파일된 CSS 에는 남지 않는다(SCSS 전용).\n"
            "- /* 여러 줄 주석 */: 컴파일된 CSS 에도 그대로 남는다(라이선스 표기 등).\n"
            "!default 는 '아직 값이 없을 때만 이 값을 쓰라'는 표시다.\n"
            "- $color: blue !default; 는 $color 가 이미 정의돼 있으면 무시되고, 없을 때만 blue 가 된다.\n"
            "라이브러리/컴포넌트가 기본값을 제공하되, 사용자가 미리 정한 값이 있으면 그것을 존중하게 만들 때 쓴다.\n"
            "아래 예시는 $primary 를 먼저 정해두었으므로, !default 한 줄은 무시되고 기존 값이 유지된다."
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
            "@extend 는 한 선택자가 다른 선택자의 스타일을 통째로 물려받게 한다.\n"
            ".error { @extend .message; } 라고 하면 .message 의 규칙에 .error 가 함께 묶인다.\n"
            "@include(믹스인)가 코드를 '복제'해 넣는 것과 달리, @extend 는 선택자를 '한데 모아'\n"
            "쉼표로 나열된 규칙(.message, .error { ... })으로 출력한다. 그래서 중복 선언이 줄어든다.\n"
            "공통 베이스 스타일(메시지 박스, 버튼 골격 등)을 여러 변형이 공유할 때 효과적이다.\n"
            "아래를 컴파일하면 .message, .success, .error 가 공통 규칙을 공유하고\n"
            "각자 색만 다르게 출력된다."
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
            "%이름 으로 만드는 placeholder 선택자는 그 자체로는 CSS 에 출력되지 않는다.\n"
            "오직 @extend %이름 으로 가져다 쓸 때만 해당 규칙이 사용처 선택자에 합쳐진다.\n"
            "일반 클래스를 @extend 하면 안 쓰는 클래스 규칙까지 남지만,\n"
            "placeholder 는 '쓰이지 않으면 사라지므로' 군더더기 없는 재사용 베이스로 이상적이다.\n"
            "버튼·카드·메시지의 공통 골격을 %base 로 정의하고, 각 변형이 @extend 로 물려받는 패턴이 흔하다.\n"
            "아래를 컴파일하면 %card 자체는 나오지 않고, 이를 확장한 .card-light/.card-dark 만\n"
            "공통 규칙을 공유하며 출력된다."
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
            "font-family, font-size, font-weight 처럼 접두어(font-)가 같은 속성이 많을 때,\n"
            "SCSS 는 'font: { ... }' 형태로 접두어를 한 번만 쓰고 묶을 수 있다.\n"
            "안에서는 family: serif; size: 14px; 처럼 뒷부분만 적는다.\n"
            "축약형 값과 세부 값을 함께 줄 수도 있다: font: 14px/1.5 { family: serif; }.\n"
            "margin/padding/border/background 등 접두어를 공유하는 속성군에 두루 쓸 수 있다.\n"
            "컴파일하면 font-family, font-size … 처럼 풀어진 일반 CSS 속성으로 출력된다.\n"
            "관련 속성을 시각적으로 묶어 가독성을 높이는 문법 설탕이다."
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
            "보간 #{$변수} 는 변수의 값을 코드 문자열 속에 끼워 넣는다.\n"
            "변수가 그냥 값으로는 들어갈 수 없는 자리(선택자 이름, 속성 이름, 미디어 조건 등)에 특히 유용하다.\n"
            "- 선택자: .icon-#{$name} { } → .icon-home 처럼.\n"
            "- 속성 이름: margin-#{$side}: 8px; → margin-left 처럼.\n"
            "- 값 합성: content: 'v#{$n}'; → 'v3' 처럼.\n"
            "단순 값 계산에는 보간이 필요 없지만(그냥 $var 사용), '이름을 동적으로 만들 때'는 보간이 필수다.\n"
            "아래를 컴파일하면 변수로 만든 클래스 이름·속성 이름·값이 모두 치환되어 출력된다."
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
            "lighten/darken 외에도 색을 정교하게 변형하는 내장 함수가 많다.\n"
            "- adjust-hue($c, 30deg): 색상환을 돌려 다른 색조로.\n"
            "- saturate/desaturate($c, 20%): 채도를 올리거나 내림.\n"
            "- complement($c): 보색(색상환 반대편) 반환.\n"
            "- scale-color($c, $lightness: -20%): 현재 값을 기준으로 비율만큼 부드럽게 조정(과하지 않게).\n"
            "- transparentize/opacify: 투명도를 더하거나 줄임.\n"
            "scale-color 는 lighten 처럼 고정량을 더하는 대신 '남은 여유의 비율'로 조절해 자연스럽다.\n"
            "아래를 컴파일하면 한 기준색에서 호버색·보색·강조색 등 팔레트가 함수로 파생되어 출력된다."
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
            "@function 은 값을 계산해 @return 으로 돌려준다. 인자를 정교하게 다룰 수 있다.\n"
            "- 기본값: @function space($n, $unit: 8px) — $unit 을 생략하면 8px 사용.\n"
            "- 이름 인자 호출: space($n: 3) 처럼 인자 이름을 지정해 순서와 무관하게 넘긴다.\n"
            "- 함수 안에서 @if/@else 로 분기하거나, 자기 자신을 호출하는 재귀도 가능하다.\n"
            "값 계산 로직(간격 스케일, 단위 변환, 거듭제곱 등)을 함수로 캡슐화하면 재사용성이 높아진다.\n"
            "아래를 컴파일하면 기본값·이름 인자로 호출한 space() 와, 재귀로 거듭제곱을 구한 pow() 결과가\n"
            "실제 수치로 박혀 출력된다."
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
            "리스트와 맵을 다루는 내장 함수들이다.\n"
            "리스트: length(개수), nth($l, i)(i번째), index($l, 값)(위치), append($l, 값)(추가),\n"
            "join($a, $b)(이어붙임).\n"
            "맵: map-get($m, 키)(값 꺼내기), map-has-key($m, 키)(존재 확인),\n"
            "map-keys/map-values(키·값 목록), map-merge($a, $b)(병합).\n"
            "이 함수들을 @each/@for 와 결합하면 토큰 집합을 가공해 유틸리티를 대량 생성할 수 있다.\n"
            "아래를 컴파일하면 맵을 병합한 뒤 순회해 색 유틸리티를 만들고, 리스트에서 값을 꺼내 쓴 결과가 출력된다."
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
            "믹스인 안에서 @if / @else if / @else 로 인자에 따라 다른 선언을 출력할 수 있다.\n"
            "예) 버튼 종류(primary/ghost)에 따라 배경·테두리를 다르게 내는 믹스인.\n"
            "- @if not 조건, and/or 결합, == 비교 등을 활용한다.\n"
            "- 잘못된 인자에는 @error 로 컴파일을 멈춰 실수를 빨리 잡을 수도 있다.\n"
            "함수가 '하나의 값'을 분기해 반환한다면, 조건 믹스인은 '여러 선언'을 분기해 끼워 넣는다.\n"
            "아래를 컴파일하면 같은 믹스인 호출이 인자에 따라 서로 다른 규칙으로 펼쳐져 출력된다."
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
            "@content 는 믹스인을 호출할 때 함께 넘긴 '스타일 블록'을 믹스인 내부의 그 자리에 끼워 넣는다.\n"
            "@include 이름 { ... } 처럼 중괄호로 블록을 넘기면, 믹스인 안 @content 위치에 그대로 펼쳐진다.\n"
            "대표적 활용은 미디어쿼리 래퍼다. @include respond(mobile) { ... } 로 호출하면\n"
            "복잡한 @media 조건은 믹스인이 감추고, 사용자는 안에 들어갈 규칙만 적으면 된다.\n"
            ":hover 등 상태 래퍼, 테마 스코프 래퍼에도 쓴다.\n"
            "아래를 컴파일하면 respond 믹스인에 넘긴 블록이 알맞은 @media 안에 끼워져 출력된다."
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
            "SCSS 는 수치를 다듬는 수학 함수를 내장한다.\n"
            "- floor(내림)/ceil(올림)/round(반올림): 소수점 정리.\n"
            "- abs(절댓값), min(...)/max(...): 여러 값 중 최소·최대.\n"
            "- percentage(비율→%): 0.25 → 25%.\n"
            "그리드 컬럼 너비, 반응형 글자 크기 한계, 정수 픽셀 보정 등에 두루 쓰인다.\n"
            "참고로 최신 dart-sass 는 이 함수들을 'sass:math' 모듈로 묶어\n"
            "@use 'sass:math'; math.div(a, b) 처럼 쓰지만, 여기 libsass 환경에서는\n"
            "위의 전역 함수(floor, ceil, round 등)와 / 나눗셈을 그대로 사용한다.\n"
            "아래를 컴파일하면 각 함수의 계산 결과가 실제 수치로 박혀 출력된다."
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
