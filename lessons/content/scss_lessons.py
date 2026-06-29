"""SCSS 문법 학습 (기초·중급·고급, 랭크 없음).

SCSS 는 컴파일하면 CSS 가 되는 CSS 확장 언어다.
이 도구는 libsass(dart-sass 호환)로 각 예시를 컴파일해 결과 CSS 를 보여준다.
각 code 는 단일 .scss 파일로 컴파일되는 유효한 SCSS 이다.
"""

from engine.models import Lesson

LESSONS = [

    # ───────────────────────── 기초 ─────────────────────────

    Lesson(
        id="scss-basic-01-var",
        lang="scss", level="기초",
        title="변수($)",
        summary="$이름: 값 으로 값을 재사용",
        explanation=(
            "SCSS 는 $이름: 값; 형태로 변수를 선언한다.\n"
            "색상·여백·폰트 크기처럼 여러 곳에서 반복되는 값을 변수에 담아두면\n"
            "한 곳만 고쳐도 전체에 반영되어 유지보수가 쉬워진다.\n"
            "컴파일하면 변수는 사라지고 실제 값으로 치환된 CSS 가 된다."
        ),
        usage="브랜드 색상, 기본 여백, 폰트 스택 등 디자인 토큰을 한곳에서 관리할 때 쓴다.",
        cons="순수 CSS 변수(--name)와 달리 컴파일 시점에 고정되어, 런타임에 동적으로 바꿀 수는 없다.",
        code=(
            "// 변수 선언\n"
            "$primary: #3498db;\n"
            "$gap: 16px;\n"
            "$radius: 8px;\n"
            "\n"
            ".button {\n"
            "  color: #fff;\n"
            "  background-color: $primary;\n"
            "  padding: $gap;\n"
            "  border-radius: $radius;\n"
            "}\n"
            "\n"
            ".card {\n"
            "  border: 1px solid $primary;\n"
            "  margin: $gap;\n"
            "}\n"
        ),
    ),

    Lesson(
        id="scss-basic-02-nesting",
        lang="scss", level="기초",
        title="중첩(nesting)",
        summary="선택자 안에 선택자를 넣어 구조 표현",
        explanation=(
            "SCSS 는 선택자 안에 다른 선택자를 중첩해서 쓸 수 있다.\n"
            "HTML 의 계층 구조를 그대로 코드에 표현할 수 있어 가독성이 좋다.\n"
            "컴파일되면 .nav ul li 처럼 자손 선택자로 펼쳐진다.\n"
            "속성도 font: { ... } 처럼 중첩할 수 있다."
        ),
        usage="컴포넌트 단위(.nav, .card 등)로 관련 스타일을 묶어 정리할 때 유용하다.",
        cons="너무 깊게 중첩하면(3~4단계 이상) 선택자가 길고 무거워져 오히려 관리가 어려워진다.",
        code=(
            "$link: #2c3e50;\n"
            "\n"
            ".nav {\n"
            "  background: #ecf0f1;\n"
            "\n"
            "  ul {\n"
            "    margin: 0;\n"
            "    padding: 0;\n"
            "    list-style: none;\n"
            "\n"
            "    li {\n"
            "      display: inline-block;\n"
            "\n"
            "      a {\n"
            "        color: $link;\n"
            "        text-decoration: none;\n"
            "      }\n"
            "    }\n"
            "  }\n"
            "}\n"
        ),
    ),

    Lesson(
        id="scss-basic-03-parent",
        lang="scss", level="기초",
        title="부모 참조(&)",
        summary="& 로 현재 선택자를 가리켜 상태·변형 작성",
        explanation=(
            "& 는 중첩 안에서 '부모 선택자 자신'을 가리킨다.\n"
            ".btn 안에서 &:hover 라고 쓰면 .btn:hover 로 펼쳐진다.\n"
            "&--primary 처럼 쓰면 .btn--primary 가 되어 BEM 식 변형을 만들기 좋다.\n"
            "공백 없이 붙으므로 가상 클래스·수식어를 깔끔하게 표현할 수 있다."
        ),
        usage=":hover/:focus 같은 상태와 --modifier 변형을 한 블록 안에 모아 작성할 때 쓴다.",
        cons="& 를 남용해 .a & 같은 역참조를 섞으면 결과 선택자를 머릿속으로 추적하기 어려워진다.",
        code=(
            "$primary: #e74c3c;\n"
            "\n"
            ".btn {\n"
            "  padding: 8px 16px;\n"
            "  border: none;\n"
            "  cursor: pointer;\n"
            "\n"
            "  &:hover {\n"
            "    opacity: 0.8;\n"
            "  }\n"
            "\n"
            "  &--primary {\n"
            "    background: $primary;\n"
            "    color: #fff;\n"
            "  }\n"
            "\n"
            "  &.is-disabled {\n"
            "    cursor: not-allowed;\n"
            "  }\n"
            "}\n"
        ),
    ),

    # ───────────────────────── 중급 ─────────────────────────

    Lesson(
        id="scss-mid-01-mixin",
        lang="scss", level="중급",
        title="@mixin / @include",
        summary="스타일 묶음을 정의하고 인자로 재사용",
        explanation=(
            "@mixin 이름(인자) { ... } 으로 재사용할 스타일 묶음을 정의하고,\n"
            "@include 이름(값) 으로 어디서든 꺼내 쓴다.\n"
            "인자에 기본값($r: 4px)을 줄 수 있어 호출을 간단히 할 수 있다.\n"
            "함수와 달리 '값'이 아니라 '여러 줄의 CSS 선언'을 통째로 끼워 넣는다."
        ),
        usage="flex 가운데 정렬, 버튼 베이스, 미디어쿼리 래퍼처럼 반복되는 선언 묶음에 쓴다.",
        cons="@include 는 호출마다 코드가 복제되어 출력 CSS 가 커질 수 있다(공통화는 % placeholder 도 고려).",
        code=(
            "@mixin flex-center {\n"
            "  display: flex;\n"
            "  justify-content: center;\n"
            "  align-items: center;\n"
            "}\n"
            "\n"
            "@mixin box($bg, $r: 4px) {\n"
            "  background: $bg;\n"
            "  border-radius: $r;\n"
            "  padding: 12px;\n"
            "}\n"
            "\n"
            ".modal {\n"
            "  @include flex-center;\n"
            "  @include box(#fff, 10px);\n"
            "}\n"
            "\n"
            ".tag {\n"
            "  @include box(#eee);\n"
            "}\n"
        ),
    ),

    Lesson(
        id="scss-mid-02-operation",
        lang="scss", level="중급",
        title="연산(색·숫자)",
        summary="+,-,*,/ 와 색 함수로 값 계산",
        explanation=(
            "SCSS 는 숫자 연산(+,-,*,/)과 단위 계산을 지원한다.\n"
            "$base * 2, $w / 3 처럼 레이아웃 값을 식으로 표현할 수 있다.\n"
            "색은 lighten()/darken()/mix() 같은 내장 함수로 변형한다.\n"
            "변수와 함께 쓰면 일관된 비율·색 단계를 자동으로 만들 수 있다."
        ),
        usage="기준 여백의 배수 간격, 호버 시 어두운 색 등 '관계로 정의되는 값'에 쓴다.",
        cons="단위가 다른 값끼리(px + em) 연산하면 에러가 난다. dart-sass 에서는 / 나눗셈이 math.div 로 권장됨.",
        code=(
            "$base: 8px;\n"
            "$brand: #3498db;\n"
            "\n"
            ".panel {\n"
            "  padding: $base * 2;        // 16px\n"
            "  margin-bottom: $base * 3;  // 24px\n"
            "  width: 900px / 3;          // 300px\n"
            "  background: $brand;\n"
            "}\n"
            "\n"
            ".panel:hover {\n"
            "  background: darken($brand, 10%);\n"
            "}\n"
            "\n"
            ".panel--soft {\n"
            "  background: lighten($brand, 25%);\n"
            "  border-color: mix($brand, #fff, 50%);\n"
            "}\n"
        ),
    ),

    Lesson(
        id="scss-mid-03-partial-use",
        lang="scss", level="중급",
        title="부분 파일과 @use 개념",
        summary="_파일 분리 · @use 로 모듈 가져오기(개념)",
        explanation=(
            "큰 스타일은 _variables.scss 처럼 밑줄로 시작하는 '부분 파일(partial)'로 쪼갠다.\n"
            "밑줄 파일은 단독으로 CSS 가 생성되지 않고, 다른 파일에서 가져다 쓴다.\n"
            "최신 dart-sass 는 @use 'variables'; 로 모듈을 가져오며 변수는 variables.$x 처럼 접근한다.\n"
            "(과거 @import 는 폐기 예정.) 아래 예시는 학습 도구 특성상 단일 파일로 같은 효과를 보인다."
        ),
        usage="변수/믹스인/컴포넌트별로 파일을 나눠 협업·재사용성을 높일 때 쓴다.",
        cons="@use 는 dart-sass 전용이라 구형 libsass 에선 동작하지 않을 수 있다. 단일 파일 데모로 대체했다.",
        code=(
            "// 실제 프로젝트라면 아래를 _tokens.scss 로 분리하고\n"
            "// 다른 파일에서 @use 'tokens'; 로 가져온다(여기선 한 파일로 시연).\n"
            "$color-text: #222;\n"
            "$color-bg: #fafafa;\n"
            "$space: 12px;\n"
            "\n"
            "@mixin surface {\n"
            "  color: $color-text;\n"
            "  background: $color-bg;\n"
            "  padding: $space;\n"
            "}\n"
            "\n"
            ".article {\n"
            "  @include surface;\n"
            "  line-height: 1.6;\n"
            "}\n"
            "\n"
            ".sidebar {\n"
            "  @include surface;\n"
            "  width: 240px;\n"
            "}\n"
        ),
    ),

    # ───────────────────────── 고급 ─────────────────────────

    Lesson(
        id="scss-adv-01-loops",
        lang="scss", level="고급",
        title="반복문 @for / @each / @while",
        summary="규칙적인 클래스를 반복으로 자동 생성",
        explanation=(
            "@for $i from 1 through 4 { ... } 로 숫자 범위를 반복한다.\n"
            "@each $c in red, green { ... } 로 목록을 순회한다.\n"
            "@while 조건 { ... } 로 조건이 참인 동안 반복한다.\n"
            "반복 안에서 보간 #{$i} 를 쓰면 .col-1, .col-2 처럼 동적인 선택자·값을 만든다."
        ),
        usage="그리드 컬럼, 여백 유틸리티(.mt-1..n), 색상 팔레트 클래스를 한 번에 찍어낼 때 쓴다.",
        cons="반복 횟수가 많으면 출력 CSS 가 급격히 커진다. 정말 필요한 범위만 생성하는 것이 좋다.",
        code=(
            "// @for: 컬럼 너비 클래스 생성\n"
            "@for $i from 1 through 4 {\n"
            "  .col-#{$i} {\n"
            "    width: percentage($i / 4);\n"
            "  }\n"
            "}\n"
            "\n"
            "// @each: 색상 유틸리티 생성\n"
            "@each $name, $color in (info: #3498db, ok: #2ecc71, warn: #e67e22) {\n"
            "  .text-#{$name} {\n"
            "    color: $color;\n"
            "  }\n"
            "}\n"
            "\n"
            "// @while: 여백 단계 생성\n"
            "$i: 1;\n"
            "@while $i <= 3 {\n"
            "  .mt-#{$i} {\n"
            "    margin-top: 8px * $i;\n"
            "  }\n"
            "  $i: $i + 1;\n"
            "}\n"
        ),
    ),

    Lesson(
        id="scss-adv-02-function",
        lang="scss", level="고급",
        title="@function 과 @if / @else",
        summary="값을 계산해 반환하는 사용자 함수 + 분기",
        explanation=(
            "@function 이름(인자) { @return 값; } 으로 값을 계산해 돌려주는 함수를 만든다.\n"
            "믹스인이 'CSS 선언 묶음'을 끼워 넣는다면, 함수는 '하나의 값'을 반환한다.\n"
            "@if / @else if / @else 로 조건에 따라 다른 값을 반환할 수 있다.\n"
            "아래 함수는 배경색의 밝기에 따라 어울리는 글자색을 골라 반환한다."
        ),
        usage="간격 계산, 단위 변환, 대비 글자색 선택 등 재사용 가능한 '값 계산 로직'에 쓴다.",
        cons="로직이 복잡해지면 디버깅이 어렵다. 부수효과 없는 순수 계산에만 쓰는 것이 바람직하다.",
        code=(
            "// 배경 밝기에 따라 글자색을 반환하는 함수\n"
            "@function ideal-text($bg) {\n"
            "  @if (lightness($bg) > 60%) {\n"
            "    @return #000;\n"
            "  } @else {\n"
            "    @return #fff;\n"
            "  }\n"
            "}\n"
            "\n"
            "$light: #f1c40f;\n"
            "$dark: #2c3e50;\n"
            "\n"
            ".badge-light {\n"
            "  background: $light;\n"
            "  color: ideal-text($light);  // 밝은 배경 → 검정\n"
            "}\n"
            "\n"
            ".badge-dark {\n"
            "  background: $dark;\n"
            "  color: ideal-text($dark);   // 어두운 배경 → 흰색\n"
            "}\n"
        ),
    ),

    Lesson(
        id="scss-adv-03-map",
        lang="scss", level="고급",
        title="맵($map)과 반복",
        summary="(키: 값) 맵을 @each 로 순회해 테마 생성",
        explanation=(
            "맵은 (키: 값, 키: 값) 형태로 여러 쌍을 담는 자료구조다.\n"
            "map-get($map, 키) 로 특정 값을 꺼내고, @each $k, $v in $map 으로 전부 순회한다.\n"
            "디자인 토큰(색·간격 단계)을 맵 하나로 모아두면 관리가 깔끔하다.\n"
            "보간 #{$k} 로 키를 선택자 이름에, $v 를 속성 값에 넣어 테마 클래스를 자동 생성한다."
        ),
        usage="색 팔레트, 브레이크포인트, 간격 스케일 같은 토큰 집합을 한 곳에서 정의·전개할 때 쓴다.",
        cons="맵이 커지고 중첩되면 가독성이 떨어진다. 키 오타는 컴파일 에러 없이 빈 값이 될 수 있어 주의.",
        code=(
            "// 색상 토큰 맵\n"
            "$colors: (\n"
            "  primary: #3498db,\n"
            "  success: #2ecc71,\n"
            "  danger:  #e74c3c\n"
            ");\n"
            "\n"
            "// 특정 값 꺼내 쓰기\n"
            ".header {\n"
            "  border-bottom: 2px solid map-get($colors, primary);\n"
            "}\n"
            "\n"
            "// 맵 전체를 순회해 버튼 테마 자동 생성\n"
            "@each $name, $color in $colors {\n"
            "  .btn-#{$name} {\n"
            "    background: $color;\n"
            "    color: #fff;\n"
            "\n"
            "    &:hover {\n"
            "      background: darken($color, 8%);\n"
            "    }\n"
            "  }\n"
            "}\n"
        ),
    ),
]
