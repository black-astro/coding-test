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
            "[개요]\n"
            "변수는 값을 저장하고 이름으로 재사용할 수 있는 식별자이다.\n"
            "동일한 값(예: 색상 #3498db)이 버튼, 카드, 링크 등 여러 곳에서 쓰일 때,\n"
            "값을 직접 반복 기입하면 수정 시 모든 사용처를 찾아 고쳐야 하며 누락 위험이 있다.\n"
            "변수를 사용하면 한 곳의 정의만 변경해도 전체가 일괄 반영된다.\n"
            "\n"
            "[문법]\n"
            "• 선언 형식: '$이름: 값;'\n"
            "• 달러 기호($)로 시작하고, 콜론(:) 뒤에 값을 적은 뒤 세미콜론(;)으로 종료한다.\n"
            "\n"
            "[코드 분석]\n"
            "• $primary: #3498db;          → $primary 변수에 파란색을 저장한다.\n"
            "• $gap: 16px;                 → $gap 변수에 여백 크기 16px 을 저장한다.\n"
            "• $radius: 8px;               → $radius 변수에 모서리 둥글기 8px 을 저장한다.\n"
            "• background-color: $primary; → 배경색으로 $primary 값을 사용한다.\n"
            "• padding: $gap;              → 안쪽 여백으로 $gap 값을 사용한다.\n"
            "• border-radius: $radius;     → 모서리 둥글기로 $radius 값을 사용한다.\n"
            "\n"
            "[용어]\n"
            "• padding: 요소 내부의 여백(콘텐츠와 테두리 사이 공간)이다.\n"
            "• border-radius: 사각형 모서리를 둥글게 처리하는 정도이다.\n"
            "\n"
            "[컴파일 동작]\n"
            "컴파일 후 변수는 제거되고 $primary 자리에는 실제 값 #3498db 가 치환된다.\n"
            "변수는 작성 편의를 위한 도구이며, 최종 CSS 결과물에는 실제 값만 남는다.\n"
            "\n"
            "[유의 사항]\n"
            "• $ 변수는 컴파일 시점에 값이 고정된다. 페이지 실행 중 사용자 조작으로\n"
            "  값을 동적으로 변경하는 런타임 변경은 불가능하다.\n"
            "• 런타임 변경이 필요하면 순수 CSS 변수(--name)를 사용해야 한다."
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
            "[개요]\n"
            "중첩은 스타일 규칙 안에 또 다른 규칙을 포함시켜 선택자 계층을 표현하는 기능이다.\n"
            "HTML 은 태그가 서로 감싸는 계층 구조를 가진다\n"
            "(예: nav 안에 ul, ul 안에 li, li 안에 a).\n"
            "\n"
            "[배경]\n"
            "• 순수 CSS 에서는 이 관계를 '.nav ul li a' 처럼 한 줄로 길게 기술해야 한다.\n"
            "• 규칙이 많아지면 '.nav' 를 반복 기입하게 되고, 계층 관계가 한눈에 드러나지 않는다.\n"
            "• 중첩을 사용하면 HTML 의 포함 구조를 들여쓰기로 동일하게 표현할 수 있어\n"
            "  가독성이 높아진다.\n"
            "\n"
            "[코드 구조]\n"
            "• .nav { ... }   → 메뉴 전체 영역을 지정한다.\n"
            "• ul { ... }     → .nav 내부의 목록을 지정한다.\n"
            "• li { ... }     → 목록 내부의 각 항목을 지정한다.\n"
            "• a { ... }      → 항목 내부의 링크를 지정한다.\n"
            "\n"
            "[속성 분석]\n"
            "• background: #ecf0f1;   → 메뉴 배경을 연회색으로 지정한다.\n"
            "• margin: 0; padding: 0; → 목록의 바깥/안쪽 기본 여백을 제거한다\n"
            "                           (브라우저 기본 여백 제거).\n"
            "• list-style: none;      → 목록 앞의 점(•) 표시를 제거한다.\n"
            "• display: inline-block; → 항목을 세로 배치가 아닌 가로 배치로 나열한다.\n"
            "• text-decoration: none; → 링크 밑줄을 제거한다.\n"
            "\n"
            "[컴파일 동작]\n"
            "컴파일 시 중첩은 '.nav ul li a' 형태의 단일 선택자로 전개된다.\n"
            "결과 CSS 는 순수 CSS 방식과 동일하며, 작성 편의를 위한 구조화일 뿐이다.\n"
            "속성 이름도 중첩 가능하다(예: font: { size: 14px; }).\n"
            "\n"
            "[유의 사항]\n"
            "• 3~4단계 이상 깊게 중첩하면 선택자가 지나치게 길고 무거워진다.\n"
            "• 이 경우 다른 곳에서 스타일을 덮어쓰기 어렵고 성능에도 불리하다.\n"
            "• 2~3단계 정도로 얕게 유지하는 것이 바람직하다."
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
            "[개요]\n"
            "& 기호는 중첩 블록 안에서 현재 감싸고 있는 선택자 자신을 가리킨다.\n"
            "요소는 상태에 따라 표현이 달라진다\n"
            "(예: 기본, 마우스 오버(hover), 비활성(disabled)).\n"
            "CSS 로는 '.btn:hover', '.btn.is-disabled' 처럼 기술한다.\n"
            "\n"
            "[& 가 필요한 이유]\n"
            "• 일반 중첩은 규칙 사이에 공백을 삽입하여 전개된다\n"
            "  (.btn 안의 span → '.btn span').\n"
            "• :hover 같은 상태는 '.btn:hover' 처럼 공백 없이 붙여야 한다.\n"
            "• & 를 사용하면 공백 없이 자기 자신에 바로 이어 붙일 수 있다.\n"
            "\n"
            "[코드 분석]\n"
            "• .btn { ... }          → 버튼의 기본 상태를 지정한다.\n"
            "• &:hover { ... }       → '.btn:hover' 로 전개된다 = 마우스 오버 상태이다.\n"
            "• &--primary { ... }    → '.btn--primary' 로 전개된다 = 강조 변형 버튼이다.\n"
            "• &.is-disabled { ... } → '.btn.is-disabled' 로 전개된다 = 비활성 상태이다.\n"
            "\n"
            "[속성 분석]\n"
            "• padding: 8px 16px;   → 안쪽 여백을 상하 8px, 좌우 16px 로 지정한다.\n"
            "• border: none;        → 버튼 테두리 선을 제거한다.\n"
            "• cursor: pointer;     → 마우스 오버 시 손가락 모양 커서로 변경한다\n"
            "                         (클릭 가능 신호).\n"
            "• opacity: 0.8;        → 약간 투명하게 처리한다(1: 불투명, 0: 완전 투명).\n"
            "• cursor: not-allowed; → 금지 모양 커서로 클릭 불가를 표시한다.\n"
            "\n"
            "[BEM 명명]\n"
            "• '&--primary' 같은 명명 방식을 BEM 이라 한다.\n"
            "• 두 줄표(--)는 동일 컴포넌트의 변형 버전을 나타내는 약속된 표기이다.\n"
            "• 관련 상태와 변형을 .btn 블록 한곳에 모아 관리할 수 있다.\n"
            "\n"
            "[유의 사항]\n"
            "• '.selected &' 처럼 & 를 뒤에 두는 역참조도 가능하나, 남용하면\n"
            "  최종 선택자 조합을 추적하기 어려워진다.\n"
            "• 초기에는 &:hover, &--변형 같은 기본 패턴만 사용할 것을 권장한다."
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
            "[개요]\n"
            "믹스인(@mixin)은 자주 쓰는 스타일 선언 묶음을 이름으로 정의해두고,\n"
            "@include 로 필요한 곳에 끼워 넣어 재사용하는 기능이다.\n"
            "\n"
            "[필요성]\n"
            "• 가운데 정렬 3종 세트처럼 여러 줄이 항상 함께 쓰이는 경우가 많다.\n"
            "• 매번 복사·붙여넣기하면 방식 변경 시 모든 사용처를 수정해야 한다.\n"
            "• 해당 묶음에 이름을 부여해 정의하고 이름으로 호출하면 관리가 단순해진다.\n"
            "\n"
            "[코드 분석]\n"
            "• @mixin flex-center { ... }      → 'flex-center' 스타일 묶음을 정의한다.\n"
            "  - display: flex;               → 자식 요소를 유연 배치하는 모드를 활성화한다.\n"
            "  - justify-content: center;     → 자식을 가로 방향 가운데로 정렬한다.\n"
            "  - align-items: center;         → 자식을 세로 방향 가운데로 정렬한다.\n"
            "    (세 선언이 합쳐져 완전 중앙 정렬이 된다.)\n"
            "• @mixin box($bg, $r: 4px) { ... } → 인자를 받는 믹스인을 정의한다.\n"
            "  - $bg                          → 배경색을 외부에서 받는 매개변수이다.\n"
            "  - $r: 4px                      → 둥글기 값이며, 미지정 시 기본값 4px 을 사용한다.\n"
            "• @include flex-center;          → 정의한 flex-center 묶음을 삽입한다.\n"
            "• @include box(#fff, 10px);      → box 에 흰색·10px 을 전달해 적용한다.\n"
            "• @include box(#eee);            → box 에 회색만 전달하며, 둥글기는 기본 4px 이 된다.\n"
            "\n"
            "[인자(매개변수)]\n"
            "• 괄호 안의 $bg, $r 을 인자(파라미터)라 한다.\n"
            "• 동일한 믹스인이라도 전달 값에 따라 결과가 달라진다\n"
            "  (box(#fff, 10px)는 흰 상자, box(#eee)는 회색 상자).\n"
            "\n"
            "[함수와의 차이]\n"
            "• @function 은 계산된 값 하나를 반환한다(예: 색 하나).\n"
            "• @mixin 은 여러 줄의 CSS 선언 묶음을 통째로 삽입한다.\n"
            "\n"
            "[유의 사항]\n"
            "• @include 는 호출할 때마다 코드가 복제되어 삽입된다.\n"
            "• 100군데에서 호출하면 동일 코드가 100번 출력되어 CSS 파일이 커질 수 있다.\n"
            "• 값 없이 공통 스타일만 공유할 때는 % placeholder(@extend)도 함께 고려한다."
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
            "[개요]\n"
            "SCSS 는 값을 직접 계산할 수 있다. 고정 숫자 대신 '8 * 2 = 16' 같은\n"
            "식을 그대로 기술할 수 있다.\n"
            "\n"
            "[필요성]\n"
            "• 디자인에는 기준값의 배수로 정해지는 값이 많다\n"
            "  (기본 간격 8px → 여백 8·16·24px).\n"
            "• 계산 결과를 직접 기입하면 기준값 변경 시 모든 값을 다시 계산해야 한다.\n"
            "• '$base * 2' 처럼 관계로 기술하면 $base 만 바꿔도 전부 자동 재계산된다.\n"
            "\n"
            "[숫자 연산]\n"
            "• $base * 2  → 기준값(8px)의 2배 = 16px\n"
            "• $base * 3  → 기준값의 3배 = 24px\n"
            "• 900px / 3  → 900을 3으로 나눔 = 300px\n"
            "• 사용 가능 연산자: + 더하기, - 빼기, * 곱하기, / 나누기\n"
            "\n"
            "[색 연산]\n"
            "색을 조절하는 내장 함수가 제공된다.\n"
            "• darken($brand, 10%)    → 기준 색을 10% 어둡게 한다\n"
            "                           (호버 시 색을 진하게 할 때 사용).\n"
            "• lighten($brand, 25%)   → 기준 색을 25% 밝게 한다.\n"
            "• mix($brand, #fff, 50%) → 기준 색과 흰색을 50% 비율로 혼합한다.\n"
            "\n"
            "[속성 맥락]\n"
            "• padding: $base * 2;       → 안쪽 여백을 16px 로 지정한다.\n"
            "• margin-bottom: $base * 3; → 아래쪽 바깥 여백을 24px 로 지정한다\n"
            "                              (margin 은 요소 바깥 여백).\n"
            "• width: 900px / 3;         → 너비를 300px 로 지정한다.\n"
            "\n"
            "기준 색(brand) 하나만 정의하면 기본 색·진한 색·연한 색이 자동으로\n"
            "조화롭게 파생되어 색 조합의 일관성이 유지된다.\n"
            "\n"
            "[유의 사항]\n"
            "• 단위가 다른 값끼리 계산할 수 없다('10px + 2em' 은 에러가 발생한다).\n"
            "• 최신 dart-sass 에서는 나눗셈(/) 사용 시 경고가 발생하며,\n"
            "  math.div($w, 3) 형태를 권장한다(기존 방식은 폐기 예정)."
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
            "[개요]\n"
            "큰 스타일 파일을 역할별 작은 파일 여러 개로 분리하고, @use 로 가져와\n"
            "조합하는 모듈화 방법이다.\n"
            "\n"
            "[필요성]\n"
            "• 스타일 코드가 수천 줄이 되면 한 파일에서 특정 부분을 찾기 어렵다.\n"
            "• 색·크기 같은 값은 _variables.scss, 재사용 묶음은 _mixins.scss 처럼\n"
            "  역할별로 파일을 분리한다.\n"
            "• 협업 시 서로 다른 파일을 수정하므로 충돌이 줄어든다.\n"
            "\n"
            "[핵심 규칙]\n"
            "• _파일이름.scss → 이름 앞에 밑줄(_)을 붙이면 부분 파일(partial)이 된다.\n"
            "  이는 재료용 파일로 단독으로는 CSS 로 컴파일되지 않고, 다른 파일이\n"
            "  가져다 쓸 때만 사용된다(밑줄은 조각 파일임을 나타내는 표시).\n"
            "• @use 'variables';  → variables 부분 파일을 가져온다.\n"
            "• variables.$primary → 가져온 파일의 변수는 '파일이름.$변수' 형태로 참조한다.\n"
            "\n"
            "[네임스페이스]\n"
            "'파일이름.변수' 형태로 접두어를 붙이는 이유는 여러 파일을 가져왔을 때\n"
            "해당 변수의 출처를 명확히 하여 이름 충돌과 혼동을 방지하기 위함이다.\n"
            "\n"
            "[예시 코드 분석]\n"
            "(학습 도구 특성상 실제로는 한 파일로 시연한다.)\n"
            "• $color-text, $color-bg, $space → 글자색·배경색·여백 토큰을 정의한다.\n"
            "• @mixin surface { ... }         → 표면 스타일 묶음을 정의한다.\n"
            "• @include surface;              → .article 과 .sidebar 가 이 묶음을 공유한다.\n"
            "• line-height: 1.6;              → 줄 간격을 글자 높이의 1.6배로 지정해\n"
            "                                   가독성을 높인다.\n"
            "\n"
            "값과 묶음을 토큰 파일 한곳에 모아두면, 디자인 변경 시 해당 파일만\n"
            "수정해도 전체가 일관되게 반영된다.\n"
            "\n"
            "[유의 사항]\n"
            "• @use 는 최신 도구(dart-sass) 전용 문법으로, 구형 도구(libsass)에서는\n"
            "  동작하지 않을 수 있다. 본 예시는 파일을 실제 분리하지 않고 한 파일 안에서\n"
            "  동일 효과를 시연한다.\n"
            "• 과거에는 @import 를 사용했으나 폐기 예정이므로 @use 를 권장한다."
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
            "[개요]\n"
            "반복문은 동일한 형태의 규칙을 자동으로 여러 번 생성하는 제어문이다.\n"
            ".col-1 ~ .col-4 를 개별 작성하는 대신 범위만 지정해 일괄 생성한다.\n"
            "\n"
            "[필요성]\n"
            "• 그리드, 여백 유틸리티(.mt-1, .mt-2 ...), 색상 클래스처럼 번호만 다르고\n"
            "  형태가 동일한 규칙이 다수 필요한 경우가 많다.\n"
            "• 수십 개를 수작업으로 작성하면 비효율적이며 오타 위험이 있다.\n"
            "• 규칙만 지정하면 반복문이 정확하게 생성한다.\n"
            "\n"
            "[세 반복문 비교]\n"
            "• @for   → 숫자 범위를 순회할 때(1부터 4까지).\n"
            "• @each  → 목록의 항목을 하나씩 꺼낼 때(빨강, 초록, 파랑).\n"
            "• @while → 조건이 참인 동안 반복할 때(i가 3 이하인 동안).\n"
            "\n"
            "[@for 분석]\n"
            "• @for $i from 1 through 4 → $i 를 1,2,3,4 로 바꿔가며 4회 반복한다\n"
            "                             (through 는 끝값 포함).\n"
            "• .col-#{$i}              → #{$i} 자리에 현재 숫자가 삽입되어\n"
            "                             .col-1 ~ .col-4 가 생성된다.\n"
            "• percentage($i / 4)      → $i/4 를 퍼센트로 변환한다(1/4 → 25%).\n"
            "\n"
            "[보간(interpolation)]\n"
            "#{...} 를 보간이라 한다. 값을 문자열이나 선택자 안에 삽입하는 기능이며,\n"
            "#{$i} 는 해당 위치에 현재 숫자를 삽입한다.\n"
            "\n"
            "[@each 분석]\n"
            "• @each $name, $color in (info: #3498db, ok: ..., warn: ...)\n"
            "  → 목록을 하나씩 꺼내 $name 에 이름(info), $color 에 색을 담는다.\n"
            "• .text-#{$name} → .text-info, .text-ok, .text-warn 클래스를 생성한다.\n"
            "• color: $color; → 각 클래스의 글자색을 해당 색으로 지정한다.\n"
            "\n"
            "[@while 분석]\n"
            "• $i: 1;                → 카운터를 1로 초기화한다.\n"
            "• @while $i <= 3        → $i 가 3 이하인 동안 반복한다.\n"
            "• .mt-#{$i}             → .mt-1, .mt-2, .mt-3 을 생성한다(mt=위쪽 여백).\n"
            "• margin-top: 8px * $i; → 여백을 8·16·24px 로 증가시킨다.\n"
            "• $i: $i + 1;           → 카운터를 1 증가시킨다\n"
            "                          (생략 시 무한 루프가 발생한다).\n"
            "\n"
            "[유의 사항]\n"
            "• 반복 횟수가 많으면 CSS 규칙이 대량 생성되어 파일이 급격히 커진다.\n"
            "• 실제로 사용하지 않는 범위까지 생성하면 낭비이므로 필요한 범위만 생성한다.\n"
            "• @while 은 카운터 증가 구문($i: $i + 1)을 반드시 포함해 무한 루프를 방지한다."
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
            "[개요]\n"
            "함수(@function)는 입력값을 받아 계산된 값 하나를 반환하는 기능이다.\n"
            "@if / @else 는 조건에 따라 처리를 분기하는 제어문이다.\n"
            "\n"
            "[믹스인과의 차이]\n"
            "• @mixin    → 여러 줄의 CSS 스타일 묶음을 통째로 삽입한다.\n"
            "• @function → 계산된 값 하나만 반환한다.\n"
            "즉 함수는 색 하나, 숫자 하나 등 단일 값을 생성하는 데 사용한다.\n"
            "\n"
            "[@if / @else]\n"
            "조건에 따라 결과를 다르게 결정한다.\n"
            "• @if (조건) { A } → 조건이 참이면 A 를 수행한다.\n"
            "• @else { B }      → 그 외의 경우 B 를 수행한다.\n"
            "• @else if 로 중간 조건을 추가할 수 있다.\n"
            "\n"
            "[예시 목적]\n"
            "본 예시는 배경색에 어울리는 글자색을 자동 선택하는 함수이다.\n"
            "밝은 배경에는 검은 글자, 어두운 배경에는 흰 글자가 가독성이 높다.\n"
            "이 판단을 함수가 대신 수행한다.\n"
            "\n"
            "[코드 분석]\n"
            "• @function ideal-text($bg) → 'ideal-text' 함수를 정의하고 배경색($bg)을 받는다.\n"
            "• lightness($bg) > 60%      → 배경색의 밝기가 60%보다 높은지 검사한다\n"
            "                              (lightness 는 색 밝기를 측정하는 내장 함수).\n"
            "• @return #000;             → 밝은 배경이면 검정(#000)을 반환한다.\n"
            "• @return #fff;             → 어두운 배경이면 흰색(#fff)을 반환한다\n"
            "                              (@return 은 결과값을 반환하라는 지시).\n"
            "\n"
            "[사용부 분석]\n"
            "• $light: #f1c40f;           → 밝은 노란색을 정의한다.\n"
            "• $dark: #2c3e50;            → 어두운 남색을 정의한다.\n"
            "• color: ideal-text($light); → 노란 배경을 전달하면 검정 글자가 반환된다.\n"
            "• color: ideal-text($dark);  → 남색 배경을 전달하면 흰색 글자가 반환된다.\n"
            "\n"
            "배경색을 변경해도 글자색이 자동으로 가독성 있게 맞춰지므로,\n"
            "글자가 보이지 않는 실수를 방지할 수 있다.\n"
            "\n"
            "[유의 사항]\n"
            "• 함수 내부 로직이 복잡해지면 디버깅이 어려워진다.\n"
            "• 함수는 값 계산·반환만 담당하게 하고, 스타일을 직접 그리는 부수효과는\n"
            "  넣지 않는다. 그래야 예측 가능하고 재사용성이 높다."
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
            "[개요]\n"
            "맵(map)은 이름(키)과 값을 짝지어 하나로 담는 자료구조이다.\n"
            "예를 들어 'primary 에는 파란색, danger 에는 빨간색' 식으로\n"
            "이름과 값을 짝지어 한곳에 모아 관리한다.\n"
            "\n"
            "[필요성]\n"
            "• 변수를 개별로 정의($primary, $success, $danger ...)하면 관련 값이\n"
            "  흩어져 관리가 어렵다.\n"
            "• 맵을 사용하면 관련 값을 하나로 묶고, 이름으로 개별 조회하거나\n"
            "  전체를 한 번에 순회할 수 있다.\n"
            "\n"
            "[맵 생성과 조회]\n"
            "• $colors: ( primary: #3498db, ... ) → 이름:값 짝들을 담은 맵을 정의한다\n"
            "                                       (소괄호 안에 콤마로 나열).\n"
            "• map-get($colors, primary)          → 맵에서 'primary' 키의 값을 조회한다.\n"
            "• border-bottom: 2px solid ...;      → 헤더 아래에 2px 파란 선을 지정한다.\n"
            "\n"
            "[맵 전체 순회]\n"
            "@each 와 결합해 순회한다.\n"
            "• @each $name, $color in $colors → 맵의 짝을 하나씩 꺼내\n"
            "                                   $name 에 이름, $color 에 색을 담는다.\n"
            "• .btn-#{$name}                  → .btn-primary, .btn-success, .btn-danger 를\n"
            "                                   생성한다(#{...} 는 이름을 선택자에 삽입하는 보간).\n"
            "• background: $color;            → 각 버튼 배경을 해당 색으로 지정한다.\n"
            "• &:hover { background: darken($color, 8%); }\n"
            "                                 → 마우스 오버 시 색을 8% 어둡게 한다\n"
            "                                   (& 는 현재 버튼 자신).\n"
            "\n"
            "색 3개짜리 맵에서 버튼 3종류가 자동 생성된다. 맵에 한 줄을 추가하면\n"
            "버튼도 자동으로 추가되므로, 테마 변경과 색 추가/삭제가 용이하다.\n"
            "\n"
            "[유의 사항]\n"
            "• 맵이 커지고 맵 안에 맵이 중첩되면 가독성이 떨어진다.\n"
            "• map-get 에서 키를 오타 내면(예: 'primry') 에러 없이 빈 값이 반환될 수\n"
            "  있어 원인 파악이 어렵다. 키 이름은 정확히 기입하고 오타에 주의한다."
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
