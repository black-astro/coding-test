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
            "━━ SCSS 의 '숫자' 란? ━━\n"
            "일반 프로그래밍에서 숫자는 그냥 3, 5 같은 값이에요. 그런데 웹 화면에서는 \"3이 뭐 3cm? 3픽셀?\" 처럼 '단위'가 중요해요.\n"
            "그래서 SCSS 의 숫자는 자(cm) 눈금처럼 단위를 함께 달고 다녀요. 16px(픽셀 16), 1.5rem, 50%, 그리고 단위가 아예 없는 3 도 있어요.\n"
            "쉽게 말해 '16px' 는 \"16이라는 숫자 + px 라는 이름표\" 가 붙어 있는 한 덩어리예요.\n\n"
            "━━ 왜 단위가 중요할까? ━━\n"
            "요리 레시피에서 \"설탕 2\" 라고만 적으면 2스푼인지 2컵인지 몰라요. \"2스푼\" 처럼 단위가 있어야 정확하죠.\n"
            "웹도 똑같아서, 화면에 그리려면 반드시 단위가 필요해요. SCSS 는 이 단위를 계산할 때 자동으로 챙겨줘요.\n\n"
            "속성(연산 규칙) 하나씩 읽기:\n"
            "  16px + 4px = 20px      →  같은 단위(px)끼리는 그냥 더하고 뺄 수 있어요. 20센티 자에 4센티를 더하면 24센티인 것처럼요.\n"
            "  8px * 2 = 16px         →  단위 있는 숫자에 '단위 없는 숫자'를 곱하면 단위는 그대로 유지돼요. \"8픽셀짜리를 2배로\" = 16픽셀.\n"
            "  16px * $scale          →  변수에 담긴 1.5 를 곱하면 24px. 배율(몇 배)은 단위 없는 숫자로 두는 게 자연스러워요.\n"
            "  percentage(0.25) = 25% →  0.25 라는 비율(4분의 1)을 사람이 읽기 좋은 % 로 바꿔주는 내장 도구예요.\n\n"
            "━━ 왜 변수에 기준값을 담을까? ━━\n"
            "$base: 8px 처럼 기준 간격을 하나 정해두고, 8px·16px·24px 를 '기준의 배수'로 만들면 화면 전체가 8의 리듬으로 딱딱 맞아 정돈돼 보여요.\n"
            "나중에 8px 을 10px 로 바꾸면 배수들이 전부 같이 바뀌니, 한 곳만 고쳐도 되죠. 이게 변수를 쓰는 진짜 이유예요.\n\n"
            "주의할 점:\n"
            "  서로 다른 단위(예: px + em)를 더하면 컴파일 에러가 나요. cm 와 인치를 그냥 더할 수 없는 것과 같아요 — 단위를 먼저 맞춰야 해요.\n"
            "  '단위 있는 숫자'(8px)와 '단위 없는 숫자'(2)를 헷갈리면 결과 단위가 이상해지니, 배율은 단위 없이 두는 습관을 들이세요.\n"
            "  참고로 컴파일(SCSS→CSS 변환)하면 위 식들은 전부 미리 계산돼서, 결과 CSS 에는 20px 같은 '진짜 숫자'만 남아요."
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
            "━━ '문자열' 이란? ━━\n"
            "문자열은 쉽게 말해 '글자들의 묶음'이에요. 'hello', 'Noto Sans', 'new' 처럼 사람이 읽는 글자죠.\n"
            "SCSS 에서는 이 글자 묶음을 두 가지 방식으로 적을 수 있어요.\n"
            "  따옴표가 있는 글자:  'hello'  (택배 상자에 이름표를 '따옴표 리본'으로 딱 묶어둔 느낌)\n"
            "  따옴표가 없는 글자:  bold     (그냥 맨몸으로 놓인 단어)\n\n"
            "━━ 따옴표가 있고 없고 무슨 차이일까? ━━\n"
            "따옴표 없는 단어(bold, sans-serif)는 '키워드' 처럼 동작해요. CSS 속성 값으로 곧바로 쓰기 좋아요 (font-weight: bold 처럼요).\n"
            "따옴표 있는 글자('NEW')는 '진짜 텍스트'로 취급돼서, 화면에 글자를 찍어내는 content 같은 곳에 필요해요.\n\n"
            "속성(문자열 도구) 하나씩 읽기:\n"
            "  quote(x)              →  글자에 따옴표 리본을 '붙여줘요'. quote(Noto Sans) → 'Noto Sans'\n"
            "  unquote('x')          →  반대로 따옴표 리본을 '떼줘요'. 값으로 쓰고 싶을 때 벗겨요.\n"
            "  to-upper-case('new')  →  전부 대문자로 → 'NEW'. (소문자로는 to-lower-case)\n"
            "  str-length('new')     →  글자 개수를 세줘요. 'new' 는 3글자니까 3.\n\n"
            "━━ 보간(#{}) 으로 글자 합치기 ━━\n"
            "#{$var} 는 변수 안의 값을 글자 사이에 '끼워 넣는' 도구예요. 편지 양식의 빈칸에 이름을 채워 넣는 것과 같아요.\n"
            "예를 들어 url('/img/' + $label + '.svg') 는 여러 글자 조각을 이어붙여 '/img/new.svg' 라는 완성된 경로를 만들어요.\n"
            "이렇게 하면 아이콘 경로나 클래스 이름을 변수로 자동으로 만들 수 있어서 편해요.\n\n"
            "주의할 점:\n"
            "  content 값에는 보통 '따옴표가 있는 글자'를 써야 의도대로 글자가 나와요. 따옴표를 빼먹으면 엉뚱하게 동작할 수 있어요.\n"
            "  따옴표가 있냐 없냐에 따라 '텍스트냐, 키워드냐' 의미가 달라지니, 값으로 쓸 땐 unquote, 글자로 보여줄 땐 quote 를 기억하세요.\n"
            "  컴파일된 결과 CSS 에는 함수가 다 적용된 '최종 글자'만 남아요 (to-upper-case 를 썼으면 'NEW' 로 이미 바뀐 채로요)."
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
            "━━ SCSS 의 '색' 이란? ━━\n"
            "SCSS 는 색깔을 그냥 글자로 보지 않고 '색이라는 특별한 타입'으로 다뤄요. 마치 물감 팔레트에 담긴 진짜 물감처럼요.\n"
            "같은 파란색을 적는 방법이 여러 가지예요 — 이건 같은 색을 세 가지 언어로 부르는 것과 같아요.\n"
            "  #3498db          →  16진수(hex) 표기. 색약속 코드예요.\n"
            "  rgb(52,152,219)  →  빨강·초록·파랑 물감을 각각 얼마씩 섞을지 (0~255)\n"
            "  hsl(...)         →  색상(어떤 색)·채도(선명함)·명도(밝기)로 표현\n"
            "셋 다 결국 똑같은 파란색이 될 수 있어요. 표기 방식만 다른 거예요.\n\n"
            "━━ 색에서 성분을 꺼내는 도구 ━━\n"
            "물감을 다시 빨강·초록·파랑으로 분리하듯, 색에서 각 성분만 뽑아내는 내장 함수가 있어요.\n"
            "  red($c) / green($c) / blue($c)             →  빨강·초록·파랑 값을 꺼내요 (0~255 사이 숫자)\n"
            "  hue($c) / saturation($c) / lightness($c)   →  색상·채도·명도를 꺼내요\n"
            "  rgba($color, 0.5)                          →  기존 색에 '투명도'를 입혀요. 0.5 면 반투명 유리처럼 뒤가 비쳐요\n\n"
            "━━ 왜 이렇게 색을 다룰까? ━━\n"
            "브랜드 색(예: 회사 대표 파랑) 하나를 변수 $brand 에 딱 정해두면, 그 색을 기준으로 연한 배경·반투명 테두리·그림자 색을 '자동으로' 만들 수 있어요.\n"
            "만약 브랜드 색을 나중에 초록으로 바꿔도, 변수 한 줄만 고치면 파생된 색들이 전부 같이 바뀌어요. 페인트 원액 하나 바꾸면 섞은 색이 전부 바뀌는 것과 같죠.\n\n"
            "예시 읽기:\n"
            "  rgba($brand, 0.4)                     →  브랜드색 그대로인데 40%만 불투명 (60%는 투명). 은은한 테두리에 좋아요\n"
            "  hsl(hue($brand), 70%, 92%)            →  브랜드색과 '같은 색상'인데 아주 밝게(92%) → 연한 배경색이 돼요\n\n"
            "주의할 점:\n"
            "  hsl 방식과 rgb 방식을 머릿속에서 섞어 직접 계산하려 하면 헷갈려요. 예를 들어 '조금 더 어둡게' 같은 변형은 손으로 계산하지 말고 전용 함수에 맡기는 게 안전해요.\n"
            "  컴파일하면 이 색 함수들은 전부 계산돼서, 결과 CSS 에는 #ffffff 나 rgba(52,152,219,0.4) 같은 '최종 색 값'만 남아요."
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
            "━━ '불리언(boolean)' 이란? ━━\n"
            "불리언은 딱 두 가지 값만 갖는 타입이에요 — true(참, 예) 또는 false(거짓, 아니요).\n"
            "전등 스위치를 떠올리면 쉬워요. 켜짐(true) 아니면 꺼짐(false), 그 사이는 없어요.\n"
            "예를 들어 $dark-mode: true 는 \"다크모드 스위치를 켰다\" 는 뜻이에요.\n\n"
            "불리언 관련 도구:\n"
            "  비교 연산 (>, <, ==)      →  두 값을 견줘서 참/거짓을 내놔요. 5 > 3 은 true\n"
            "  and / or / not           →  조건을 조합해요. '이것 그리고 저것', '이것 또는 저것', '이것이 아님'\n"
            "  if($조건, 참값, 거짓값)   →  스위치가 켜져 있으면 참값을, 꺼져 있으면 거짓값을 골라줘요. 갈림길에서 표지판 보고 길 고르는 것과 같아요\n"
            "  예) if($dark-mode, #1e1e1e, #ffffff) → 다크모드면 어두운 배경, 아니면 흰 배경\n\n"
            "━━ '리스트(list)' 란? ━━\n"
            "리스트는 여러 값을 한 줄에 나란히 담은 '목록'이에요. 장바구니에 물건 여러 개 담는 것과 같아요.\n"
            "구분하는 방법이 두 가지예요.\n"
            "  공백으로 구분:  10px 20px 30px     (사이에 띄어쓰기)\n"
            "  쉼표로 구분:    red, green, blue   (사이에 콤마)\n"
            "재미있는 사실: margin: 4px 8px 처럼 우리가 흔히 쓰는 CSS 축약값도 사실은 리스트예요! 이미 알던 개념이었던 거죠.\n\n"
            "리스트에서 값 꺼내기:\n"
            "  nth($list, 2)      →  '몇 번째' 값을 꺼내요. 2 를 주면 두 번째 값. (주의: 프로그래밍과 달리 1부터 세요!)\n"
            "  length($list)      →  목록에 값이 몇 개인지 세줘요. 장바구니 물건 개수 세기\n\n"
            "주의할 점:\n"
            "  다른 언어와 달리 SCSS 에서는 0, 빈 글자(''), 빈 리스트도 전부 '참(true)'으로 쳐요! 거짓으로 취급되는 건 오직 false 와 null 둘 뿐이에요.\n"
            "  그래서 '값이 있으면 참' 같은 감으로 조건을 짜면 함정에 빠질 수 있으니, 조건은 명확하게 true/false 로 판단되게 쓰세요.\n"
            "  nth() 는 1부터 세니까, 두 번째 값을 원하면 2 를 넣어야 해요 (0 이 아니에요)."
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
            "━━ '주석(comment)' 이란? ━━\n"
            "주석은 컴퓨터가 실행하지 않고 그냥 넘어가는 '사람을 위한 메모'예요. 코드 옆에 붙이는 포스트잇 같은 거죠.\n"
            "\"이 코드가 왜 있는지\" 같은 설명을 적어두면 나중에 나나 동료가 코드를 읽기 훨씬 편해요.\n\n"
            "SCSS 주석은 두 종류예요:\n"
            "  // 한 줄 주석       →  이 줄만 메모. 컴파일된 CSS 에는 '남지 않아요'. 나만 보는 개발 메모용이에요\n"
            "  /* 여러 줄 주석 */  →  여러 줄 메모. 컴파일된 CSS 에도 '그대로 남아요'. 저작권/라이선스 표기처럼 최종 결과에 꼭 남겨야 할 때 써요\n"
            "즉, // 는 '개발할 때만 보이는 연필 메모', /* */ 는 '지워지지 않는 도장' 같은 느낌이에요.\n\n"
            "━━ '!default' 란? ━━\n"
            "!default 는 '이 변수에 아직 값이 없을 때만 이걸 써라' 는 표시예요.\n"
            "비유하면, 새로 이사한 집에 이미 소파가 있으면 안 사고, 없을 때만 기본 소파를 들이는 것과 같아요.\n"
            "  $color: blue !default;  →  $color 가 이미 정해져 있으면 이 줄은 '무시'되고, 없을 때만 blue 가 돼요.\n\n"
            "━━ 왜 !default 를 쓸까? ━━\n"
            "내가 만든 컴포넌트(버튼 같은 부품)를 남이 가져다 쓸 때를 위해서예요.\n"
            "부품에는 '안전한 기본값'을 !default 로 넣어두고, 쓰는 사람이 미리 자기 값을 정해뒀다면 그 값을 존중해 덮어쓰지 않아요.\n"
            "덕분에 '기본은 제공하되, 원하면 바꿀 수 있는' 유연한 부품이 돼요.\n\n"
            "예시 흐름 읽기 (순서가 중요해요!):\n"
            "  $primary: #e74c3c;           →  사용처에서 먼저 빨강을 정해둠\n"
            "  $primary: #3498db !default;  →  이미 값이 있으니 이 줄은 '무시' → 여전히 빨강(#e74c3c) 유지\n"
            "  $radius: 6px !default;       →  radius 는 정해둔 적 없으니 → 6px 이 채택됨\n\n"
            "주의할 점:\n"
            "  !default 는 '값이 없을 때만' 적용되므로 '선언 순서'가 정말 중요해요. 기본값 줄을 먼저 쓰고 내 값을 나중에 쓰면, 내 값으로 덮어써지니 반대가 되지 않게 조심하세요.\n"
            "  // 주석이 결과 CSS 에 안 남는다는 걸 모르면, \"분명 적었는데 왜 없지?\" 하고 디버깅할 때 헷갈릴 수 있어요."
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
            "━━ '@extend' 란? ━━\n"
            "@extend 는 한 스타일이 다른 스타일을 '통째로 물려받게' 하는 도구예요.\n"
            "비유하면, 형이 입던 교복을 동생이 그대로 물려 입고 자기 이름표만 새로 다는 것과 같아요.\n"
            "  .error { @extend .message; }  →  .error 는 .message 의 스타일을 전부 물려받고, 자기만의 색만 추가로 다는 거예요.\n\n"
            "━━ @include(믹스인) 와 뭐가 다를까? ━━\n"
            "이게 핵심이에요. 두 가지 방식이 결과가 달라요.\n"
            "  @include  →  스타일 코드를 '복사해서 붙여넣기' 해요. 같은 규칙이 여러 번 중복돼요.\n"
            "  @extend   →  코드를 복사하는 대신, 선택자들을 '한 군데로 모아' 쉼표로 묶어요.\n"
            "예를 들어 @extend 는 이렇게 출력돼요:\n"
            "  .message, .success, .error { 공통 규칙 }   ← 세 이름이 한 규칙을 같이 씀\n"
            "  .success { color: 초록 }                    ← 자기만의 색은 따로\n"
            "이렇게 공통 규칙을 한 번만 쓰니, 복사보다 결과 CSS 크기가 작아져요.\n\n"
            "━━ 왜 쓸까? ━━\n"
            "메시지 박스, 버튼 뼈대처럼 '공통 골격'을 여러 변형(성공/경고/에러)이 같이 쓸 때 좋아요.\n"
            "패딩·테두리·둥근 모서리 같은 공통 부분은 한 번만 정의하고, 각자 색만 다르게 하면 코드가 깔끔해져요.\n\n"
            "예시 읽기:\n"
            "  .message  →  공통 뼈대 (패딩, 테두리, 둥근 모서리)\n"
            "  .success  →  @extend .message 로 뼈대 물려받고 + 초록색\n"
            "  .error    →  @extend .message 로 뼈대 물려받고 + 빨간색\n\n"
            "주의할 점:\n"
            "  @extend 는 같은 규칙에 선택자 이름이 줄줄이 붙어서, 결과가 생각보다 복잡하고 예측하기 어려워질 수 있어요.\n"
            "  그래서 실무에서는 보통 다음 레슨에서 배울 % placeholder(출력 안 되는 전용 뼈대)와 함께 쓰는 게 더 깔끔해요."
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
            "━━ 'placeholder 선택자(%)' 란? ━━\n"
            "%이름 으로 만드는 placeholder 는 '남에게 물려주기 위해서만 존재하는 스타일 틀'이에요.\n"
            "비유하면, 붕어빵 '틀'과 같아요. 틀 자체는 손님에게 팔지 않지만(= CSS 에 출력 안 됨), 틀로 찍어낸 붕어빵(= @extend 로 쓴 클래스)은 손님에게 나가요.\n"
            "그래서 %card 는 그 자체로는 결과 CSS 에 절대 안 나오고, 오직 @extend %card 로 가져다 쓸 때만 그 스타일이 사용처에 합쳐져요.\n\n"
            "━━ 일반 클래스 @extend 와 뭐가 다를까? ━━\n"
            "앞 레슨의 @extend 는 '진짜 클래스(.message)'를 물려받았어요. 그럼 .message 규칙 자체도 결과에 남아요 — 안 쓰더라도요.\n"
            "반면 placeholder(%card)는 '누가 물려받지 않으면 흔적도 없이 사라져요'. 그래서 군더더기 없는 순수 재사용 틀로 딱이에요.\n"
            "  일반 클래스 → 안 써도 결과에 남음 (자리 차지)\n"
            "  % placeholder → 안 쓰면 사라짐 (깔끔)\n\n"
            "━━ 왜 쓸까? ━━\n"
            "버튼·카드·메시지의 '공통 뼈대'를 %base 로 딱 정의해두고, 여러 변형이 @extend 로 물려받는 패턴이 정석이에요.\n"
            "라이브러리를 만들 때 특히 좋아요 — 뼈대는 제공하되, 아무도 안 쓰면 결과에 쓸데없는 코드를 안 남기니까요.\n\n"
            "예시 읽기:\n"
            "  %card                →  카드 공통 뼈대(패딩, 둥근 모서리, 그림자). 이 자체는 결과에 안 나와요\n"
            "  .card-light          →  @extend %card + 흰 배경. '밝은 카드'\n"
            "  .card-dark           →  @extend %card + 어두운 배경. '어두운 카드'\n"
            "  결과적으로 .card-light, .card-dark 만 공통 규칙을 나눠 쓰며 출력돼요\n\n"
            "주의할 점:\n"
            "  placeholder 는 @media(반응형) 같은 다른 맥락을 '넘나드는' @extend 에는 제약이 있어요. 서로 다른 미디어 안팎을 이어붙이지는 못해요.\n"
            "  그리고 placeholder 는 '고정된 스타일 덩어리'라서, 값을 인자로 받아 매번 다르게 만들고 싶다면 이건 못 해요 — 그럴 땐 믹스인(@mixin)을 쓰는 게 맞아요."
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
            "━━ '중첩 속성' 이란? ━━\n"
            "CSS 속성 중에는 앞부분(접두어)이 똑같이 반복되는 것들이 많아요.\n"
            "예: font-family, font-size, font-weight → 'font-' 가 세 번이나 반복돼요. margin-top, margin-bottom → 'margin-' 반복.\n"
            "중첩 속성은 이 반복되는 앞부분을 '한 번만 쓰고 묶는' 문법이에요.\n"
            "비유하면, 편지 봉투에 주소를 쓸 때 '서울시 강남구' 를 매 줄 반복하지 않고, 위에 한 번 쓰고 그 아래에 세부 주소만 적는 것과 같아요.\n\n"
            "━━ 어떻게 쓸까? ━━\n"
            "'접두어: { ... }' 형태로 접두어를 딱 한 번 쓰고, 중괄호 안에는 '뒷부분만' 적어요.\n"
            "  font: {\n"
            "    family: serif;   →  이건 font-family: serif 가 돼요\n"
            "    size: 14px;      →  이건 font-size: 14px 가 돼요\n"
            "  }\n"
            "축약값과 세부값을 함께 줄 수도 있어요:\n"
            "  border: 1px solid #ccc { radius: 6px; }  →  border 는 축약으로, border-radius 는 세부로 한 번에\n\n"
            "━━ 왜 쓸까? ━━\n"
            "font- 나 margin- 처럼 같은 계열 속성이 여러 개 모여 있을 때, 시각적으로 딱 묶어주면 '아, 이건 다 글꼴 설정이구나' 하고 한눈에 알아보기 좋아요.\n"
            "코드를 읽는 사람의 눈이 편해지는 게 목적이에요. margin/padding/border/background 등 접두어를 공유하는 속성군에 두루 쓸 수 있어요.\n\n"
            "주의할 점:\n"
            "  이건 순전히 '보기 좋으라고' 있는 문법 설탕(sugar)이에요. 컴파일하면 결국 font-family, font-size 처럼 평범한 CSS 로 풀어져 나와요 — 성능이나 결과에는 아무 차이가 없어요.\n"
            "  그러니 속성이 한두 개뿐이라면 굳이 묶지 말고 그냥 font-size: 14px 처럼 펴서 쓰는 게 오히려 더 간단해요. 3개 이상 모일 때 진가를 발휘해요."
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
            "━━ '보간(interpolation) #{}' 이란? ━━\n"
            "보간 #{$변수} 는 변수 안의 값을 코드 아무 자리에나 '끼워 넣는' 도구예요.\n"
            "비유하면, 편지 양식의 '____ 님께' 라는 빈칸에 실제 이름을 채워 넣는 것과 같아요. #{} 가 바로 그 빈칸이에요.\n\n"
            "━━ 그냥 변수 쓰는 거랑 뭐가 다를까? ━━\n"
            "이게 헷갈리는 부분이에요. 정리하면:\n"
            "  단순히 '값'으로 쓸 때        →  보간 필요 없어요. 그냥 color: $brand 처럼 변수만 쓰면 돼요\n"
            "  '이름'을 동적으로 만들 때    →  보간이 꼭 필요해요. 변수가 그냥은 못 들어가는 자리거든요\n"
            "변수가 그냥은 못 들어가는 자리란: 선택자 이름, 속성 이름, 미디어 조건 같은 곳이에요. 이런 자리에는 #{} 로 감싸야 값이 끼워져요.\n\n"
            "어디에 끼울 수 있나 하나씩:\n"
            "  선택자 이름:  .icon-#{$name} { }    →  $name 이 home 이면 → .icon-home 이라는 클래스가 만들어져요\n"
            "  속성 이름:    margin-#{$side}: 8px  →  $side 가 left 면 → margin-left: 8px 가 돼요\n"
            "  값 합성:      content: 'v#{$n}'     →  $n 이 3 이면 → 'v3' 이라는 글자가 돼요\n"
            "  숫자+단위:    width: #{$n * 10}px   →  계산한 30 에 px 를 붙여 → 30px\n\n"
            "━━ 왜 쓸까? ━━\n"
            "반복문(@each, @for)과 짝을 이루면 진가를 발휘해요. 방향(left/right/top/bottom)마다 margin-left, margin-right... 를 자동으로 쭉 만들어내는 식이죠.\n"
            "손으로 하나하나 안 적고, 변수만 바꿔가며 이름을 찍어낼 수 있어서 반복 작업이 확 줄어요.\n\n"
            "주의할 점:\n"
            "  '값이 들어가도 되는 자리'(예: color 값)에까지 굳이 보간을 쓰면, 따옴표 처리나 값의 타입이 꼬여서 오히려 문제가 생길 수 있어요.\n"
            "  보간은 '이름을 만들어야 할 때만' 쓰고, 단순 값은 그냥 변수를 쓰세요. 꼭 필요한 곳에만 쓰는 게 요령이에요."
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
            "━━ '색 함수' 란? ━━\n"
            "색 함수는 기존 색을 '조금씩 변형해서 새 색을 만들어내는' 도구예요.\n"
            "물감 하나에 흰색을 섞어 연하게, 검정을 섞어 진하게 만드는 것처럼, 함수로 색을 밝게·어둡게·선명하게 조절해요.\n"
            "가장 기본인 lighten(밝게)/darken(어둡게) 외에도 정교한 변형 함수가 많아요.\n\n"
            "함수 하나씩 읽기:\n"
            "  adjust-hue($c, 30deg)             →  색상환(무지개 원판)을 30도 돌려서 다른 색조로. 파랑을 돌리면 보라 쪽으로 가요\n"
            "  saturate($c, 20%)                 →  채도를 올려요 = 색을 더 '쨍하고 선명하게'. desaturate 는 반대로 칙칙하게\n"
            "  complement($c)                    →  보색을 줘요 = 색상환에서 '정반대편 색'. 파랑의 보색은 주황이에요. 강조 포인트에 좋아요\n"
            "  scale-color($c, $lightness: -20%) →  현재 밝기를 기준으로 '남은 여유의 20%만큼' 부드럽게 어둡게. 과하지 않아요\n"
            "  transparentize($c, 0.85)          →  투명도를 더해 더 비치게. opacify 는 반대로 더 불투명하게\n\n"
            "━━ scale-color 가 왜 자연스러울까? ━━\n"
            "이게 중요한 포인트예요. lighten 은 '무조건 고정량(예: 20%)'을 더해요. 그래서 이미 밝은 색에 쓰면 하얗게 떠버릴 수 있어요.\n"
            "반면 scale-color 는 '남은 여유 공간의 비율'만큼만 조절해요. 컵에 물이 이미 80% 찼으면 '남은 20%의 절반'만 채우는 식이라, 넘치지 않고 자연스러워요.\n\n"
            "━━ 왜 쓸까? ━━\n"
            "기준색 하나만 정해두면, 마우스 올렸을 때 색(hover)·눌렀을 때 색(active)·강조색(보색) 등을 '자동으로' 파생시킬 수 있어요.\n"
            "덕분에 색끼리 통일감이 생기고, 기준색만 바꾸면 파생색이 전부 따라 바뀌어서 관리가 쉬워요.\n\n"
            "주의할 점:\n"
            "  함수 종류가 많아서, 결과 색을 머릿속으로 미리 그려보기 어려워요. 처음엔 조금씩 값을 바꿔가며 눈으로 확인하는 게 좋아요.\n"
            "  참고로 최신 dart-sass 에서는 이 함수들이 color.adjust / color.scale 같은 '모듈 함수' 형태로 바뀌었어요. 여기 libsass 환경에서는 위의 전역 함수 이름을 그대로 쓰면 돼요."
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
            "━━ '@function' 이란? ━━\n"
            "@function 은 '값을 계산해서 돌려주는 나만의 계산기'예요. 재료(인자)를 넣으면, 계산해서 결과 하나를 @return 으로 뱉어줘요.\n"
            "비유하면 자판기 같아요 — 동전(입력)을 넣으면 음료(결과)가 나오죠. space(2) 를 넣으면 16px 이 나오는 식이에요.\n\n"
            "인자를 정교하게 다루는 방법:\n"
            "  기본값:      @function space($n, $unit: 8px)   →  $unit 을 안 넘기면 자동으로 8px 을 써요. '옵션 생략 시 기본 세팅' 같은 거예요\n"
            "  이름 인자:   space($n: 3)                       →  인자에 이름표를 붙여 넘겨요. 순서를 신경 안 써도 되고, 뭘 넘기는지 명확해져요\n"
            "  분기:        함수 안에서 @if / @else 로 경우를 나눠 다르게 계산할 수 있어요\n"
            "  재귀:        함수가 '자기 자신을 다시 부르는' 것. 거듭제곱처럼 같은 계산을 반복할 때 써요\n\n"
            "━━ 재귀가 뭐예요? ━━\n"
            "재귀는 함수가 자기 자신을 부르며 반복하는 기법이에요. 여기 예시의 pow(거듭제곱)는 @for 반복으로 base 를 exp 번 곱해요.\n"
            "  pow(2, 5)  →  2를 5번 곱함 → 2×2×2×2×2 = 32\n"
            "거울 두 개를 마주 보게 하면 상이 계속 반복되는 것처럼, 같은 계산을 정해진 횟수만큼 되풀이하는 거예요.\n\n"
            "━━ 왜 쓸까? ━━\n"
            "간격 스케일, 단위 변환, 거듭제곱 같은 '입력을 넣으면 값이 딱 나오는' 계산 로직을 함수로 포장해두면, 여기저기서 재사용할 수 있어요.\n"
            "매번 손으로 8×2, 8×3 계산하는 대신 space(2), space(3) 이라고 부르면 되니 실수도 줄고 의도도 명확해져요.\n\n"
            "예시 읽기:\n"
            "  space(2)        →  2 × 8px = 16px (기본 단위 8px 사용)\n"
            "  space($n: 3)    →  이름 인자로 3 → 24px\n"
            "  space(2, 10px)  →  단위를 10px 로 지정 → 20px\n"
            "  pow(2, 5)       →  재귀/반복으로 → 32\n\n"
            "주의할 점:\n"
            "  재귀나 복잡한 @if 분기는 흐름을 따라가기 어려워서 디버깅이 힘들어요. 함수는 '값만 계산하는 순수한 일'에만 쓰세요.\n"
            "  중요: 함수는 '값 하나'만 돌려줘요. 여러 CSS 선언(색·테두리 여러 줄)을 한꺼번에 끼워 넣고 싶다면 함수가 아니라 믹스인(@mixin)을 써야 해요. 둘의 역할이 달라요."
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
            "━━ '리스트' 와 '맵' 이란? ━━\n"
            "먼저 두 자료 그릇을 구분해 볼게요.\n"
            "  리스트(list)  →  값을 '순서대로 줄 세운' 목록. 예: 12px 16px 20px. 번호(순서)로 꺼내요\n"
            "  맵(map)       →  '이름표: 값' 짝으로 묶은 사전. 예: (primary: 파랑, danger: 빨강). 이름으로 꺼내요\n"
            "비유하면 리스트는 '번호표 뽑는 대기줄'(몇 번째로 접근), 맵은 '이름표 붙은 사물함'(이름으로 접근)이에요.\n\n"
            "리스트 다루는 함수:\n"
            "  length($l)        →  목록에 값이 몇 개인지 세요\n"
            "  nth($l, 2)        →  '2번째' 값을 꺼내요 (1부터 셈 주의!)\n"
            "  index($l, 값)     →  그 값이 '몇 번째'에 있는지 위치를 알려줘요\n"
            "  append($l, 값)    →  목록 끝에 값을 '하나 추가'해요\n"
            "  join($a, $b)      →  두 목록을 '이어 붙여' 하나로 만들어요\n\n"
            "맵 다루는 함수:\n"
            "  map-get($m, primary)   →  'primary' 라는 이름표의 값을 꺼내요. 사물함 번호로 물건 찾기\n"
            "  map-has-key($m, 키)    →  그 이름표가 '있는지' 확인해요 (참/거짓)\n"
            "  map-keys / map-values  →  모든 이름표들 / 모든 값들의 목록을 줘요\n"
            "  map-merge($a, $b)      →  두 사전을 '합쳐서' 하나로 만들어요\n\n"
            "━━ 왜 쓸까? ━━\n"
            "디자인 토큰(색·간격 같은 규칙 값 모음)을 맵에 담아두고, @each/@for 반복문과 결합하면 유틸리티 클래스를 '대량으로 자동 생성'할 수 있어요.\n"
            "예를 들어 색 맵을 한 바퀴 돌면서 .bg-primary, .bg-danger, .bg-success 를 손 안 대고 쭉 찍어낼 수 있죠. 손으로 100개 쓸 걸 몇 줄로 끝내요.\n\n"
            "예시 흐름 읽기:\n"
            "  map-merge($base-colors, $extra)   →  기본 색 사전에 success 를 추가로 합침\n"
            "  @each $name, $color in $colors    →  합친 사전을 한 바퀴 돌며 .bg-이름 클래스를 자동 생성\n"
            "  append($sizes, 24px)              →  크기 목록 끝에 24px 추가 → 이제 4개\n\n"
            "주의할 점:\n"
            "  없는 이름표를 map-get 으로 꺼내려 하면, 에러를 내지 않고 조용히 null(빈 값)을 줘요! 그래서 키(이름표)에 오타가 있어도 눈치 못 채고 값이 텅 빈 채로 넘어갈 수 있어요.\n"
            "  이런 조용한 실수를 막으려면, 꺼내기 전에 map-has-key 로 '있는지 먼저 확인'하는 습관이 안전해요."
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
            "━━ '조건 믹스인' 이란? ━━\n"
            "믹스인(@mixin)은 '스타일 묶음을 찍어내는 도장'이에요. 그런데 여기에 @if / @else 를 넣으면, 넘긴 값에 따라 '다른 도장'을 찍을 수 있어요.\n"
            "비유하면 자판기 버튼 같아요 — '콜라' 버튼을 누르면 콜라가, '사이다' 버튼을 누르면 사이다가 나오죠. 같은 자판기(믹스인)인데 입력에 따라 결과가 달라져요.\n"
            "예) button(primary) 를 부르면 파란 채움 버튼, button(ghost) 를 부르면 테두리만 있는 투명 버튼이 나와요.\n\n"
            "조건 도구 하나씩:\n"
            "  @if $type == primary     →  '만약 type 이 primary 라면' 이 안의 스타일을 써요\n"
            "  @else if $type == ghost  →  '아니고 만약 ghost 라면' 다른 스타일을 써요\n"
            "  @else                    →  '위 어느 것도 아니라면' 이 스타일을 써요 (기본값 처리)\n"
            "  not / and / or           →  조건을 뒤집거나 조합해요\n"
            "  @error                   →  잘못된 값이 들어오면 컴파일을 '멈춰서' 실수를 바로 알려줘요\n\n"
            "━━ 함수랑 뭐가 달라요? ━━\n"
            "이게 핵심 차이예요.\n"
            "  @function       →  '값 하나'를 골라서 돌려줘요 (예: 24px 한 개)\n"
            "  조건 @mixin     →  '여러 줄의 CSS 선언'을 골라서 통째로 끼워 넣어요 (배경+색+테두리 세트)\n"
            "즉, 결과가 값 하나면 함수, 스타일 여러 줄이면 믹스인이라고 기억하면 돼요.\n\n"
            "━━ 왜 쓸까? ━━\n"
            "버튼·배지처럼 '종류/크기/상태만 다른 여러 변형'을 만들 때 최고예요. 인자 하나만 바꿔서 button(primary), button(ghost) 로 부르면 각기 다른 버튼이 나오죠.\n"
            "디자인 시스템(통일된 UI 부품 모음)을 만들 때 이 패턴이 정석이에요. 변형마다 코드를 복붙하지 않아도 되니까요.\n\n"
            "주의할 점:\n"
            "  분기(@if 갈래)가 많아지면 믹스인 하나가 너무 커지고 복잡해져요. 관리하기 어려워지죠.\n"
            "  경우의 수가 폭발적으로 늘면, 변형별로 믹스인을 쪼개거나, 앞에서 배운 '맵(map)'에 설정을 담아 처리하는 방식으로 바꾸는 게 더 깔끔해요."
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
            "━━ '@content' 란? ━━\n"
            "보통 믹스인은 '정해진 스타일'을 찍어내요. 그런데 @content 를 쓰면, 믹스인을 부를 때 '내가 원하는 스타일 블록'을 함께 넘겨서 믹스인 안에 끼워 넣을 수 있어요.\n"
            "비유하면 '내용물을 내가 채우는 택배 상자'예요. 상자(믹스인)의 겉포장은 정해져 있고, 안에 뭘 넣을지는 보내는 사람(호출자)이 정하는 거죠.\n"
            "  @include respond(mobile) { color: red; }   →  { color: red } 부분이 바로 내가 넣은 '내용물'이에요\n"
            "이 내용물이 믹스인 안의 @content 자리에 그대로 펼쳐져요.\n\n"
            "━━ 대표 활용: 미디어쿼리(반응형) 래퍼 ━━\n"
            "이게 가장 유명한 쓰임이에요. 화면 크기별로 스타일을 바꾸는 @media 조건은 길고 외우기 귀찮아요.\n"
            "그래서 복잡한 @media (max-width: ...) 부분을 믹스인이 대신 감춰주고, 쓰는 사람은 '안에 들어갈 규칙'만 적게 해요.\n"
            "  복잡한 방식:  @media (max-width: 600px) { .container { padding: 0 12px; } }\n"
            "  깔끔한 방식:  @include respond(mobile) { padding: 0 12px; }   ← @media 는 믹스인이 알아서!\n"
            "이러면 화면 크기 기준(600px 등)을 한 곳에서 관리하고, 코드도 훨씬 읽기 좋아져요.\n\n"
            "예시 흐름 읽기:\n"
            "  $breakpoints                 →  화면 크기 기준을 이름으로 정리한 맵 (mobile: 600px 등)\n"
            "  map-get($breakpoints, $name) →  넘어온 이름(tablet)으로 해당 픽셀(900px)을 꺼냄\n"
            "  @content                     →  호출할 때 넘긴 { width: 100% } 같은 블록이 이 자리에 끼워짐\n"
            "결과적으로 각 블록이 알맞은 @media 안에 쏙 들어가 출력돼요.\n\n"
            "━━ 또 어디에 쓸까? ━━\n"
            ":hover 같은 상태 래퍼, 다크/라이트 테마 스코프 래퍼처럼 '바깥 틀은 똑같고 안 내용만 다른' 모든 패턴에 잘 맞아요.\n\n"
            "주의할 점:\n"
            "  @content 로 넘긴 블록 안에서는 믹스인 '내부 변수'(예: $w)를 직접 보기 어려워요. 스코프(변수가 보이는 범위)가 분리돼 있거든요. 넘기는 블록은 자기 바깥의 변수를 쓴다고 생각하세요.\n"
            "  이런 래퍼 안에 또 래퍼를 넣는 식으로 중첩이 깊어지면, 최종 결과가 어디에 어떻게 들어갔는지 추적하기 힘들어지니 적당히 쓰세요."
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
            "━━ '수학 함수' 란? ━━\n"
            "수학 함수는 숫자를 '깔끔하게 다듬거나 골라주는' 계산 도구예요. 계산기의 특수 버튼들이라고 보면 돼요.\n"
            "화면 계산을 하다 보면 333.3333px 같은 지저분한 소수가 나오는데, 이걸 정수 픽셀로 정리해야 화면이 흐릿하지 않고 또렷해요.\n\n"
            "함수 하나씩 읽기:\n"
            "  floor(333.9)      →  '내림'. 소수점을 뚝 잘라 무조건 아래로 → 333. 계단을 내려가듯\n"
            "  ceil(333.1)       →  '올림'. 무조건 위로 → 334. 계단을 올라가듯\n"
            "  round(15.5)       →  '반올림'. 가까운 정수로 → 16. 학교에서 배운 그 반올림이에요\n"
            "  abs(-12px)        →  '절댓값'. 마이너스를 떼고 크기만 → 12px. 음수든 양수든 거리로 보기\n"
            "  min(300px, 240px) →  여러 값 중 '가장 작은' 것 → 240px\n"
            "  max(80px, 120px)  →  여러 값 중 '가장 큰' 것 → 120px\n"
            "  percentage(0.25)  →  비율(0.25)을 사람이 읽기 좋은 '%'로 → 25%\n\n"
            "━━ 왜 쓸까? ━━\n"
            "예를 들어 화면을 3칸으로 나누면 1000 ÷ 3 = 333.333... 처럼 딱 안 떨어져요. 이걸 그대로 두면 픽셀이 어긋나 화면이 지저분해요.\n"
            "그래서 floor 로 333px 로 정리해요. 또 '너무 크지도 작지도 않게' 값을 제한할 때 min/max 로 한계를 걸어요.\n"
            "그리드 칸 너비 계산, 반응형 글자 크기 상한/하한, 정수 픽셀 보정 등에 두루 쓰여요.\n\n"
            "예시 읽기:\n"
            "  floor($total / $cols)   →  1000/3 = 333.33... → 내림 → 333px (딱 떨어지는 정수 픽셀)\n"
            "  percentage(2 / $cols)   →  2/3 = 0.666... → 66.6667% (비율을 % 너비로)\n"
            "  min(300px, 240px)       →  둘 중 작은 240px (최대 너비 제한 같은 데 활용)\n\n"
            "주의할 점:\n"
            "  여기 libsass 환경에서는 위 전역 함수(floor, ceil, round...)와 / 나눗셈을 '그대로' 쓰면 돼요.\n"
            "  하지만 최신 dart-sass 로 옮기면 규칙이 바뀌어요 — 나눗셈은 a / b 대신 math.div(a, b) 로, 수학 함수들은 @use 'sass:math'; 를 불러온 뒤 math.floor(...) 처럼 'math.' 을 앞에 붙여 써야 해요. 나중에 환경이 바뀌면 이 부분을 고쳐야 한다는 걸 기억하세요."
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
