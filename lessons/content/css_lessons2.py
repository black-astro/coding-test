"""CSS 보강 레슨 (기초·중급·고급 각 5개, 총 15개).

css_lessons.py 와 주제가 겹치지 않는 새 주제들이다.
CSS 는 실행 채점이 아니라 코드/설명을 제공하는 학습 자료이며,
각 레슨의 code 에는 예시 CSS 와 "실습" 과제, 모범 CSS 가 함께 들어 있다.
"""

from engine.models import Lesson

LESSONS = [

    # ===================== 기초 =====================
    Lesson(
        id="css-basic-04-colornotation",
        lang="css", level="기초",
        title="색상 표기(hex·rgb·hsl)",
        summary="같은 색을 16진수·rgb·hsl 세 방식으로 표기",
        explanation=(
            "[개요]\n"
            "색상 표기법은 웹에서 색을 컴퓨터가 해석할 수 있는 숫자 값으로 지정하는 방법이다.\n"
            "동일한 색이라도 표기 방식은 여러 가지가 존재한다.\n\n"
            "[핵심 개념: 세 가지 표기법]\n"
            "• #3498db (hex, 16진수): '#' 뒤에 여섯 글자로 색을 지정한다. 앞 두 글자는 빨강,\n"
            "  가운데 두 글자는 초록, 뒤 두 글자는 파랑의 양을 의미한다. #fff 처럼 세 글자로 축약하면\n"
            "  흰색(#ffffff)을 뜻한다.\n"
            "• rgb(52, 152, 219): 빨강·초록·파랑을 각각 0~255 사이 숫자로 직접 지정한다.\n"
            "  0은 '전혀 없음', 255는 '최대'를 의미한다.\n"
            "• hsl(204, 70%, 53%): 색상(0~360도)·채도(선명함 %)·명도(밝기 %)로 지정한다.\n"
            "  색상환을 기준으로 값을 조절하는 방식이라 사람이 직관적으로 다루기 쉽다.\n\n"
            "[핵심 개념: 투명도(알파)]\n"
            "• #3498db80: hex 뒤에 두 글자를 더 붙이면 투명도이며, 80은 약 50% 투명 상태를 의미한다.\n"
            "• rgba(52,152,219,0.5): 맨 뒤 0.5가 투명도이다. 0은 완전 투명, 1은 완전 불투명이다.\n"
            "  뒤 배경이 비쳐 보이는 효과를 만들 때 사용한다.\n\n"
            "[hsl 의 이점]\n"
            "• 동일 색을 더 밝게 또는 더 연하게 만들 때, hsl 은 뒤의 명도 값만 변경하면 된다\n"
            "  (53% → 75% 로 밝은 파랑). hex 는 여섯 글자를 다시 계산해야 한다.\n"
            "• 버튼의 기본색·활성색·비활성색 같은 색 묶음을 만들 때 hsl 이 유리하다.\n\n"
            "[유의 사항]\n"
            "• 같은 색을 위치마다 다른 표기법으로 적으면 이후 색 변경 시 혼란이 생긴다.\n"
            "  프로젝트 내에서는 표기법을 하나로 통일하는 것이 바람직하다.\n\n"
            "[적용 결과]\n"
            "아래 코드를 적용하면 세 박스가 모두 동일한 파란색으로 칠해지고, 알파를 지정한 박스만 반투명해진다."
        ),
        usage="브랜드 색은 hex 로 고정해 쓰고, 명암 단계를 만들 땐 hsl 의 명도(L)만 조절하면 편하다.",
        cons="hex 는 사람이 명암을 가늠하기 어렵고, 같은 색을 표기법마다 다르게 적어두면 통일성이 깨진다.",
        code=(
            "/* 아래 셋은 모두 같은 파란색이다 */\n"
            ".by-hex { background: #3498db; }\n"
            ".by-rgb { background: rgb(52, 152, 219); }\n"
            ".by-hsl { background: hsl(204, 70%, 53%); }\n\n"
            "/* 투명도(알파) 표기 */\n"
            ".alpha-hex { background: #3498db80; }      /* 약 50% 투명 */\n"
            ".alpha-rgb { background: rgba(52, 152, 219, 0.5); }\n\n"
            "/* hsl 로 명도만 바꿔 밝은/어두운 변형 만들기 */\n"
            ".light { background: hsl(204, 70%, 75%); }  /* 더 밝게 */\n"
            ".dark  { background: hsl(204, 70%, 35%); }  /* 더 어둡게 */\n\n"
            "/* ===== 실습 =====\n"
            "   class=\"brand\" 에 #e74c3c 를 rgb() 와 hsl() 두 방식으로\n"
            "   같은 색이 나오도록 적어보세요. */\n\n"
            "/* 모범 답안 */\n"
            ".brand-rgb { color: rgb(231, 76, 60); }\n"
            ".brand-hsl { color: hsl(6, 78%, 57%); }\n"
        ),
    ),

    Lesson(
        id="css-basic-05-font",
        lang="css", level="기초",
        title="폰트·웹폰트(@font-face)",
        summary="font-family 우선순위와 외부 폰트 불러오기",
        explanation=(
            "[개요]\n"
            "폰트(글꼴)는 글자의 모양을 정의한다. 동일한 문자라도 둥근 형태, 각진 형태, 손글씨 형태 등으로\n"
            "다르게 표현될 수 있으며, 그 형태를 결정하는 것이 폰트이다.\n"
            "제작자 환경에 있는 글꼴이 방문자 환경에는 없을 수 있으므로, CSS 는 대체 계획을 함께 지정한다.\n\n"
            "[핵심 개념: 폰트 지정 속성]\n"
            "• font-family: 'A', 'B', sans-serif; : 글꼴 후보를 쉼표로 여러 개 지정하며, 앞에서부터\n"
            "  사용 가능한 글꼴을 순서대로 적용한다.\n"
            "• 맨 끝의 sans-serif: '일반 계열'을 의미하며, 앞 글꼴이 모두 없을 때 방문자 환경의\n"
            "  유사한 종류(삐침 없는 반듯한 글씨)로 표시하도록 하는 최종 안전망이다.\n"
            "  (serif=삐침 있는 글씨, sans-serif=삐침 없는 글씨)\n"
            "• font-weight: 700; : 글자의 굵기이다. 400은 보통, 700은 굵게(bold)이며 숫자가 클수록 두꺼워진다.\n"
            "• font-style: italic; : 글자를 오른쪽으로 기울인다. 인용문이나 강조에 사용한다.\n\n"
            "[핵심 개념: 외부 폰트 등록(@font-face)]\n"
            "• @font-face { ... } : 글꼴 파일을 인터넷에서 내려받아 사용하도록 브라우저에 알리는 선언이다.\n"
            "• font-family: 'MyFont'; : 내려받은 글꼴에 부여할 이름이며, 이후 이 이름으로 참조한다.\n"
            "• src: url(...) format... : 글꼴 파일의 주소이다. woff2는 웹에 최적화된 경량 글꼴 파일 형식이다.\n"
            "• font-display: swap; : 글꼴이 도착하기 전까지 기본 글꼴로 먼저 표시하도록 지정한다.\n"
            "  이 설정이 없으면 글꼴 다운로드가 끝날 때까지 글자가 표시되지 않는다.\n\n"
            "[유의 사항]\n"
            "• 웹폰트 파일은 용량이 크므로, 굵기(400·700 등)마다 파일을 모두 불러오면 페이지 로딩이 느려진다.\n"
            "  실제 사용하는 굵기만 선별해 불러오는 것이 바람직하다.\n"
            "• 로딩 중 글자가 잠깐 다른 글꼴로 표시되었다가 바뀌는 깜빡임(FOUT)이 발생할 수 있으며,\n"
            "  font-display: swap 이 이를 자연스럽게 처리한다.\n\n"
            "[적용 결과]\n"
            "아래 코드를 적용하면 본문은 시스템 기본 산세리프로, 제목은 불러온 'MyFont' 로 표시된다."
        ),
        usage="브랜드용 글꼴, 한글 웹폰트(예: Pretendard) 적용 시 @font-face 또는 외부 CSS 를 사용한다.",
        cons="웹폰트는 파일이 커서 로딩 중 글자가 늦게 보이거나(FOUT) 깜빡일 수 있다. 꼭 필요한 굵기만 불러오는 게 좋다.",
        code=(
            "/* 외부 폰트 파일 등록 */\n"
            "@font-face {\n"
            "  font-family: 'MyFont';\n"
            "  src: url('/fonts/myfont.woff2') format('woff2');\n"
            "  font-weight: 400;\n"
            "  font-display: swap;   /* 로딩 동안 기본 글꼴로 먼저 보여줌 */\n"
            "}\n\n"
            "/* 폰트 스택: 앞에서부터 가능한 글꼴 사용 */\n"
            "body {\n"
            "  font-family: 'Helvetica Neue', Arial, 'Apple SD Gothic Neo', sans-serif;\n"
            "}\n\n"
            "h1 {\n"
            "  font-family: 'MyFont', sans-serif;\n"
            "  font-weight: 700;\n"
            "}\n\n"
            "/* ===== 실습 =====\n"
            "   class=\"quote\" 글자를 기울임꼴(italic)에\n"
            "   serif 계열 글꼴 스택으로 표시해보세요. */\n\n"
            "/* 모범 답안 */\n"
            ".quote {\n"
            "  font-family: Georgia, 'Times New Roman', serif;\n"
            "  font-style: italic;\n"
            "}\n"
        ),
    ),

    Lesson(
        id="css-basic-06-list-table",
        lang="css", level="기초",
        title="목록·표 스타일(list·table)",
        summary="list-style 와 border-collapse 로 목록·표 꾸미기",
        explanation=(
            "[개요]\n"
            "목록(list)은 항목을 위아래로 나열한 구조이며, 각 줄 앞에 붙는 기호를 '마커'라고 한다.\n"
            "표(table)는 가로줄·세로줄이 교차해 칸을 이루는 격자 구조로, 가격표나 성적표에 사용한다.\n"
            "CSS 로 두 구조의 형태를 조정할 수 있다.\n\n"
            "[핵심 개념: 목록 속성]\n"
            "• list-style-type: square; : 줄 앞 마커 모양을 지정한다. disc(●), circle(○), square(■),\n"
            "  decimal(1. 2. 3.) 등에서 선택한다.\n"
            "• list-style: none; : 마커를 제거한다. 가로 메뉴(홈·소개·연락처)를 만들 때 줄 앞 기호를\n"
            "  없애 깔끔하게 정리하기 위해 사용한다.\n"
            "• display: inline-block; : 목록 항목을 세로가 아니라 가로로 나란히 배치한다.\n\n"
            "[핵심 개념: 표 속성]\n"
            "• border-collapse: collapse; : 칸 사이 테두리를 하나로 합친다. 기본 상태에서는 칸마다\n"
            "  테두리가 따로 있어 이중선처럼 보이는데, 이 설정으로 선이 겹쳐 단일 선으로 정리된다.\n"
            "• padding: 8px 12px; : 칸 안쪽 여백이다. 글자가 테두리에 붙지 않도록 공간을 확보한다.\n"
            "• text-align: left; : 칸 안 글자의 정렬(왼쪽/가운데/오른쪽)을 지정한다.\n"
            "• tr:nth-child(even) : 짝수 번째 줄만 선택해 색을 지정한다. 한 줄 걸러 색을 넣으면\n"
            "  줄무늬(zebra) 형태가 되어 행을 눈으로 따라가기 쉬워진다.\n\n"
            "[활용 목적]\n"
            "• 숫자(가격)를 오른쪽 정렬하면 자릿수가 맞아 비교가 쉬워진다.\n"
            "• 머리행(제목 줄)에 배경색을 주면 데이터의 시작 위치가 명확해진다.\n\n"
            "[유의 사항]\n"
            "• 표(table)를 화면 배치(레이아웃) 용도로 사용해서는 안 된다. 표는 데이터 표현에만 쓰고,\n"
            "  화면 배치는 flex 나 grid 를 사용해야 모바일 환경에서도 유연하게 대응된다.\n\n"
            "[적용 결과]\n"
            "아래 코드를 적용하면 마커 없는 가로 메뉴와, 테두리가 합쳐지고 머리행이 강조된 줄무늬 표가 생성된다."
        ),
        usage="네비게이션 메뉴(목록), 가격표·데이터 표 등 정형 데이터를 보기 좋게 정리할 때 쓴다.",
        cons="레이아웃 목적의 표(table) 남용은 반응형에 약하다. 데이터 표에만 쓰고 배치는 flex/grid 를 쓰는 게 좋다.",
        code=(
            "/* 마커 없는 가로 메뉴 */\n"
            ".menu {\n"
            "  list-style: none;\n"
            "  margin: 0; padding: 0;\n"
            "}\n"
            ".menu li { display: inline-block; margin-right: 12px; }\n\n"
            "/* 깔끔한 데이터 표 */\n"
            ".grid-table {\n"
            "  border-collapse: collapse;\n"
            "  width: 100%;\n"
            "}\n"
            ".grid-table th, .grid-table td {\n"
            "  border: 1px solid #ddd;\n"
            "  padding: 8px 12px;\n"
            "  text-align: left;\n"
            "}\n"
            ".grid-table th { background: #f4f4f4; }\n"
            ".grid-table tr:nth-child(even) { background: #fafafa; }\n\n"
            "/* ===== 실습 =====\n"
            "   ol 목록의 마커를 소문자 알파벳(a, b, c)으로 바꾸고,\n"
            "   표의 가격 칸(.price)은 오른쪽 정렬해보세요. */\n\n"
            "/* 모범 답안 */\n"
            "ol.alpha { list-style-type: lower-alpha; }\n"
            ".grid-table td.price { text-align: right; }\n"
        ),
    ),

    Lesson(
        id="css-basic-07-display",
        lang="css", level="기초",
        title="display(block·inline·inline-block·none)",
        summary="요소가 줄을 차지하는 방식 바꾸기",
        explanation=(
            "[개요]\n"
            "display 는 화면 속 요소가 공간을 차지하는 방식을 결정하는 속성이다.\n"
            "한 요소가 한 줄을 통째로 차지하게 할 수도 있고, 여러 요소를 한 줄에 나란히 배치할 수도 있다.\n\n"
            "[핵심 개념: 네 가지 값]\n"
            "• display: block; : 한 줄을 통째로 차지하여 위아래로 쌓인다. 폭·높이·상하 여백을 지정할 수\n"
            "  있다. div, p, h1 이 기본적으로 이 성질을 가진다.\n"
            "• display: inline; : 글자처럼 줄 안에서 옆으로 흐른다. 폭(width)·높이(height)와 상하 여백을\n"
            "  지정해도 적용되지 않는다. 이는 글자 흐름을 유지하기 위한 것이며, span, a(링크)가 이 성질을 가진다.\n"
            "• display: inline-block; : 옆으로 나란히 흐르면서(inline) 크기·여백은 지정 가능한(block)\n"
            "  두 성질을 결합한다. 버튼 여러 개를 한 줄에 배치하면서 각각 크기를 지정할 때 적합하다.\n"
            "• display: none; : 화면에서 완전히 제거되며 차지하던 공간까지 사라진다.\n"
            "  (visibility: hidden 은 보이지 않아도 공간이 남지만, none 은 공간까지 제거한다는 점이 다르다.)\n\n"
            "[inline-block 의 활용]\n"
            "• 링크(a)는 기본적으로 inline 이라 크기를 지정할 수 없다. 링크를 버튼처럼 크게 만들어야 할 때\n"
            "  inline-block 으로 바꾸면 옆으로 나란히 배치하면서 폭·여백을 지정할 수 있다.\n\n"
            "[유의 사항]\n"
            "• display: none 은 화면 낭독기(스크린 리더)에서도 읽히지 않는다. 시각적으로만 숨기고\n"
            "  낭독기는 읽게 하려면 다른 기법을 사용해야 한다.\n"
            "• inline 요소에 width 를 지정해도 적용되지 않으므로, 크기를 지정하려면 block 또는\n"
            "  inline-block 으로 변경해야 한다.\n\n"
            "[적용 결과]\n"
            "아래 코드를 적용하면 inline 이던 링크가 크기 지정 가능한 버튼처럼 나란히 배치되고,\n"
            "'숨김' 클래스가 붙은 요소는 화면에서 완전히 사라진다."
        ),
        usage="인라인 요소(a, span)를 버튼처럼 크게 만들거나, 특정 요소를 조건부로 감출 때(none) 쓴다.",
        cons="display:none 은 화면낭독기에서도 읽히지 않으므로, 시각적으로만 숨기려면 다른 기법이 필요하다. inline 에 width 를 줘도 안 먹는 점을 자주 헷갈린다.",
        code=(
            "/* inline 요소를 크기 지정 가능한 버튼으로 */\n"
            ".nav-link {\n"
            "  display: inline-block;\n"
            "  width: 100px;\n"
            "  padding: 8px 0;\n"
            "  text-align: center;\n"
            "  background: #3498db;\n"
            "  color: #fff;\n"
            "}\n\n"
            "/* block: 한 줄 전체 차지 */\n"
            ".banner { display: block; width: 100%; background: #eee; }\n\n"
            "/* 완전히 감추기(자리도 없앰) */\n"
            ".hidden { display: none; }\n\n"
            "/* ===== 실습 =====\n"
            "   span 으로 만든 태그(.chip)를 inline-block 으로 바꿔\n"
            "   안쪽 여백 4px 8px, 둥근 모서리 12px 를 적용해보세요. */\n\n"
            "/* 모범 답안 */\n"
            ".chip {\n"
            "  display: inline-block;\n"
            "  padding: 4px 8px;\n"
            "  border-radius: 12px;\n"
            "  background: #f0f0f0;\n"
            "}\n"
        ),
    ),

    Lesson(
        id="css-basic-08-overflow",
        lang="css", level="기초",
        title="overflow(스크롤·말줄임)",
        summary="넘치는 내용을 자르거나 스크롤로 처리",
        explanation=(
            "[개요]\n"
            "overflow 는 상자에 내용이 넘칠 때의 처리 방식을 정하는 속성이다.\n"
            "박스에 height 같은 크기를 지정하면 내용이 그 안에 다 들어가지 않을 수 있는데, 이때 이 규칙이 작동한다.\n\n"
            "[핵심 개념: overflow 값]\n"
            "• overflow: visible; : 기본값. 넘친 내용이 상자 밖으로 그대로 표시된다.\n"
            "• overflow: hidden; : 상자 밖으로 넘친 부분을 잘라 감춘다.\n"
            "• overflow: scroll; : 항상 스크롤바를 표시한다. 내용이 적어도 스크롤바가 나타난다.\n"
            "• overflow: auto; : 넘칠 때만 스크롤바를 표시한다. 일반적으로 scroll 보다 auto 를 더 많이 사용한다.\n"
            "• overflow-x / overflow-y : 가로(x)와 세로(y)를 각각 별도로 지정할 수 있다(예: 세로만 스크롤).\n\n"
            "[핵심 개념: 한 줄 말줄임(…) - 세 속성 세트]\n"
            "• white-space: nowrap; : 줄바꿈을 금지하여 글이 길어도 한 줄로 이어지게 한다.\n"
            "• overflow: hidden; : 상자 밖으로 넘친 글자를 잘라 감춘다.\n"
            "• text-overflow: ellipsis; : 잘린 자리 끝에 '…'을 붙여 뒤에 내용이 더 있음을 표시한다.\n"
            "  (세 속성을 함께 사용해야 동작한다.)\n\n"
            "[활용 목적]\n"
            "• 채팅창이나 사이드바처럼 영역 크기를 고정하고 그 안에서만 스크롤하고자 할 때 사용한다.\n"
            "  이렇게 하지 않으면 내용이 늘어날 때마다 페이지 전체가 길어진다.\n"
            "• 카드 제목의 길이가 제각각일 때 한 줄 말줄임으로 처리하면 카드 정렬이 유지된다.\n\n"
            "[유의 사항]\n"
            "• overflow: hidden 은 넘친 내용뿐 아니라 그림자·툴팁처럼 의도적으로 밖으로 나가야 하는\n"
            "  요소까지 잘라버린다.\n"
            "• 말줄임은 white-space: nowrap 을 빠뜨리면 글이 여러 줄로 내려가 '…'가 표시되지 않는다.\n"
            "  세 속성을 반드시 함께 사용해야 한다.\n\n"
            "[적용 결과]\n"
            "아래 코드를 적용하면 높이가 고정된 영역에는 세로 스크롤이 생기고, 긴 제목은 끝이 '…'로 잘려 한 줄로 표시된다."
        ),
        usage="채팅 로그·사이드바처럼 영역 크기는 고정하고 안에서 스크롤하게 하거나, 카드 제목을 한 줄로 줄일 때 쓴다.",
        cons="overflow: hidden 은 의도치 않게 그림자/툴팁까지 잘라버릴 수 있다. 말줄임은 nowrap 을 빠뜨리면 동작하지 않는다.",
        code=(
            "/* 높이 고정 + 세로 스크롤 */\n"
            ".log {\n"
            "  height: 150px;\n"
            "  overflow-y: auto;   /* 넘칠 때만 스크롤바 */\n"
            "  border: 1px solid #ccc;\n"
            "  padding: 8px;\n"
            "}\n\n"
            "/* 한 줄 말줄임(...) */\n"
            ".title {\n"
            "  width: 200px;\n"
            "  white-space: nowrap;     /* 줄바꿈 금지 */\n"
            "  overflow: hidden;        /* 넘친 부분 자름 */\n"
            "  text-overflow: ellipsis; /* 끝에 ... 표시 */\n"
            "}\n\n"
            "/* ===== 실습 =====\n"
            "   class=\"thumb\" 영역(가로 120, 세로 120)에서\n"
            "   넘치는 이미지를 잘라 감추도록 만들어보세요. */\n\n"
            "/* 모범 답안 */\n"
            ".thumb {\n"
            "  width: 120px;\n"
            "  height: 120px;\n"
            "  overflow: hidden;\n"
            "}\n"
        ),
    ),

    # ===================== 중급 =====================
    Lesson(
        id="css-mid-04-float",
        lang="css", level="중급",
        title="float·clear",
        summary="요소를 좌우로 띄우고 흐름 정리하기",
        explanation=(
            "[개요]\n"
            "float 는 요소를 왼쪽이나 오른쪽으로 띄워 붙이고, 그 옆의 글이 빈 자리를 감싸며 흐르게 하는 기능이다.\n"
            "신문·잡지에서 기사 안 사진을 글이 'ㄴ'자로 감싸며 흐르게 하는 배치가 대표적인 활용이며,\n"
            "원래 목적도 이 용도이다.\n\n"
            "[핵심 개념: 속성]\n"
            "• float: left; : 요소를 왼쪽에 띄워 붙인다. 이후 오는 글이 그 오른쪽을 감싸며 흐른다.\n"
            "• float: right; : 오른쪽에 띄워 붙인다. 글은 왼쪽을 감싼다.\n"
            "• clear: both; : 감싸기를 중단하고 떠 있는 요소들 아래로 내려가라는 지시이다.\n"
            "  감싸기를 끝내려는 지점의 요소에 지정한다.\n\n"
            "[핵심 개념: 높이 붕괴와 clearfix]\n"
            "• 자식을 float 로 띄우면 부모 상자가 자식을 크기 계산에서 제외하여 높이가 0으로 줄어드는\n"
            "  문제가 발생한다. 이를 해결하는 기법이 clearfix 이다.\n"
            "• .article::after { content:''; display:block; clear:both; } : 부모 맨 끝에 보이지 않는\n"
            "  빈 요소를 만들고 거기에 clear 를 지정하여, 부모가 자식 높이를 다시 인식하도록 한다.\n\n"
            "[레이아웃 용도로 권장하지 않는 이유]\n"
            "• float 는 본래 '글 속 이미지 감싸기'용이므로, 화면 전체 배치에 사용하면 높이 붕괴,\n"
            "  clearfix 처리 등 부가 작업이 계속 필요하다.\n"
            "• 전체 레이아웃은 flex 나 grid 를 표준으로 사용하고, float 는 원래 용도에 한정하는 것이 바람직하다.\n\n"
            "[유의 사항]\n"
            "• float 사용 시 부모 높이 붕괴를 항상 고려해야 한다.\n"
            "• clear 를 지정하지 않으면 다음 내용이 떠 있는 요소 옆에 의도치 않게 배치될 수 있다.\n\n"
            "[적용 결과]\n"
            "아래 코드를 적용하면 썸네일이 왼쪽에 뜨고 글이 그 오른쪽을 감싸며, 다음 섹션은 clear 로 아래에 배치되어 겹치지 않는다."
        ),
        usage="본문 글 안에 이미지를 끼워 텍스트가 감싸 흐르게 할 때. (전체 레이아웃은 이제 flex/grid 가 표준)",
        cons="레이아웃 전반에 float 를 쓰면 높이 붕괴·clearfix 필요 등 다루기 번거롭다. 배치 용도로는 flex/grid 를 권장한다.",
        code=(
            "/* 썸네일을 왼쪽에 띄워 글이 감싸게 */\n"
            ".thumb {\n"
            "  float: left;\n"
            "  width: 120px;\n"
            "  margin: 0 16px 8px 0;\n"
            "}\n\n"
            "/* 떠 있는 자식으로 높이가 무너지는 것 방지(clearfix) */\n"
            ".article::after {\n"
            "  content: '';\n"
            "  display: block;\n"
            "  clear: both;\n"
            "}\n\n"
            "/* 다음 섹션은 감싸지 말고 아래로 */\n"
            ".next-section { clear: both; }\n\n"
            "/* ===== 실습 =====\n"
            "   class=\"avatar\" 를 오른쪽에 띄우고,\n"
            "   그 아래 .footer 는 감싸지 않고 내려오게 만들어보세요. */\n\n"
            "/* 모범 답안 */\n"
            ".avatar { float: right; margin: 0 0 8px 16px; }\n"
            ".footer { clear: both; }\n"
        ),
    ),

    Lesson(
        id="css-mid-05-zindex",
        lang="css", level="중급",
        title="z-index·쌓임 맥락(stacking)",
        summary="겹친 요소의 앞뒤 순서 제어",
        explanation=(
            "[개요]\n"
            "z-index 는 요소들이 화면에서 겹칠 때 앞뒤 표시 순서를 정하는 속성이다.\n"
            "각 요소에 층 번호를 부여하며, 번호가 클수록 앞(위)에 표시된다.\n"
            "화면의 가로(x)·세로(y)에 대해 z 는 앞뒤 깊이를 의미한다.\n\n"
            "[핵심 개념: 속성]\n"
            "• z-index: 100; : 요소의 층 번호이다. 숫자가 큰 요소가 작은 요소 위에 표시된다.\n"
            "• position: relative(등) : z-index 는 position 이 static(기본)이 아닐 때만 작동한다.\n"
            "  relative·absolute·fixed·sticky 중 하나를 지정해야 층 번호가 적용된다.\n\n"
            "[핵심 개념: 쌓임 맥락(stacking context)]\n"
            "• 일부 요소는 내부에 독립적인 쌓임 맥락을 생성한다. 그 안의 자식들은 해당 맥락 내부에서만\n"
            "  층 번호를 비교하며, 바깥 요소와는 직접 비교되지 않는다.\n"
            "• 바깥과의 순서는 부모(맥락 전체)의 층 번호로 통째로 비교된다. 즉 낮은 순서의 부모 안에 있는\n"
            "  자식은 아무리 높은 z-index 를 가져도 그 부모 순서를 넘지 못한다.\n"
            "• position+z-index 외에도 opacity(1 미만), transform, filter 를 지정하면 새 쌓임 맥락이 생성된다.\n\n"
            "[z-index 가 적용되지 않는 흔한 원인]\n"
            "• 큰 z-index 값을 지정해도, 그 요소가 낮은 순서의 부모 맥락 안에 있으면 바깥 요소를 넘지 못한다.\n"
            "• 적용되지 않을 때는 먼저 어떤 부모 맥락에 속해 있는지 확인해야 한다.\n\n"
            "[유의 사항]\n"
            "• z-index 를 9999 같은 큰 값으로 남발하면 이후 순서 관리가 어려워진다.\n"
            "• 10, 20, 100 처럼 단계를 정해 규칙적으로 사용하는 것이 바람직하다.\n\n"
            "[적용 결과]\n"
            "아래 코드를 적용하면 모달 뒷배경(overlay) 위에 모달 창이 명확히 표시된다."
        ),
        usage="모달·드롭다운·툴팁·고정 헤더 등 겹치는 UI 의 앞뒤 순서를 정할 때 쓴다.",
        cons="z-index 값을 무작정 키우면 관리가 어려워진다. 안 먹을 땐 보통 '부모가 만든 쌓임 맥락'에 갇힌 경우다.",
        code=(
            "/* 모달 뒷배경 */\n"
            ".overlay {\n"
            "  position: fixed;\n"
            "  inset: 0;                 /* top/right/bottom/left 0 */\n"
            "  background: rgba(0,0,0,0.5);\n"
            "  z-index: 100;\n"
            "}\n\n"
            "/* 모달 창은 배경보다 앞에 */\n"
            ".modal {\n"
            "  position: fixed;\n"
            "  top: 50%; left: 50%;\n"
            "  transform: translate(-50%, -50%);\n"
            "  z-index: 101;\n"
            "  background: #fff;\n"
            "  padding: 24px;\n"
            "}\n\n"
            "/* ===== 실습 =====\n"
            "   class=\"dropdown\" 메뉴가 본문(.content)보다 항상\n"
            "   위에 보이도록 position 과 z-index 를 지정해보세요. */\n\n"
            "/* 모범 답안 */\n"
            ".content  { position: relative; z-index: 1; }\n"
            ".dropdown { position: absolute; z-index: 50; }\n"
        ),
    ),

    Lesson(
        id="css-mid-06-background",
        lang="css", level="중급",
        title="배경(background·gradient)",
        summary="배경 이미지·반복·크기·그라데이션",
        explanation=(
            "[개요]\n"
            "background 는 요소 뒤에 깔리는 배경을 지정하는 속성이다. 단색·이미지·그라데이션 등을 배치할 수 있다.\n"
            "여러 세부 설정을 한 번에 묶어 적는 단축 속성이므로, 항목별로 나누어 이해하는 것이 효율적이다.\n\n"
            "[핵심 개념: 배경 속성]\n"
            "• background-color: #eee; : 배경을 단색으로 칠한다.\n"
            "• background-image: url(...); : 배경에 이미지를 배치한다.\n"
            "• background-repeat: no-repeat; : 이미지를 반복하지 않도록 지정한다. 기본값은 타일처럼 반복이다.\n"
            "• background-position: center; : 이미지의 위치를 지정한다. center 는 중앙 정렬이다.\n"
            "• background-size: cover; : 이미지를 배경 영역에 꽉 차게 확대한다(일부가 잘려도 빈틈 없이 채움).\n"
            "• background-size: contain; : 이미지가 잘리지 않게 영역 안에 전부 맞춘다(여백이 생길 수 있음).\n"
            "  cover 는 '꽉 채워 자르기', contain 은 '전부 보이게 넣기'의 차이이다.\n\n"
            "[핵심 개념: 그라데이션]\n"
            "• 그라데이션은 CSS 에서 이미지로 취급하므로 background-image 위치에 지정한다.\n"
            "• linear-gradient(방향, 색1, 색2) : 직선을 따라 색1에서 색2로 점진적으로 변한다.\n"
            "  방향은 to bottom(위→아래), 135deg(대각선) 등으로 지정한다.\n"
            "• radial-gradient(색1, 색2) : 중심에서 바깥으로 원형으로 색이 번진다.\n\n"
            "[핵심 개념: 배경 여러 겹 쌓기]\n"
            "• 쉼표로 배경을 여러 개 지정하면 겹쳐 쌓이며, 먼저 적은 것이 위에 온다.\n"
            "• 대표 활용: 사진 위에 반투명한 검은 그라데이션을 덮으면 사진이 어두워져, 그 위의 흰 글자\n"
            "  가독성이 확보된다. 밝은 사진 위 흰 글씨가 보이지 않는 문제를 해결하는 흔한 기법이다.\n\n"
            "[유의 사항]\n"
            "• 큰 배경 이미지는 로딩이 느려지므로 적절한 용량으로 사용해야 한다.\n"
            "• 그라데이션을 과도하게 겹치면 화면이 복잡해지고 글자 가독성이 저하될 수 있다.\n\n"
            "[적용 결과]\n"
            "아래 코드를 적용하면 히어로 영역은 사진 위에 어두운 그라데이션이 덮여 글자 가독성이 확보된다."
        ),
        usage="히어로 배너, 카드 배경, 사진 위 글자 가독성용 어두운 오버레이 등에 쓴다.",
        cons="큰 배경 이미지는 로딩이 느리다. 그라데이션을 과하게 겹치면 성능·가독성이 나빠질 수 있다.",
        code=(
            "/* 사진을 꽉 채워 가운데 정렬 */\n"
            ".hero {\n"
            "  background-image: url('/img/bg.jpg');\n"
            "  background-size: cover;\n"
            "  background-position: center;\n"
            "  background-repeat: no-repeat;\n"
            "  height: 300px;\n"
            "}\n\n"
            "/* 사진 위에 어두운 그라데이션을 겹쳐 글자 가독성 확보 */\n"
            ".hero-dim {\n"
            "  background:\n"
            "    linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)),\n"
            "    url('/img/bg.jpg') center / cover no-repeat;\n"
            "}\n\n"
            "/* 단색 대신 부드러운 그라데이션 버튼 */\n"
            ".btn-grad {\n"
            "  background: linear-gradient(135deg, #6a11cb, #2575fc);\n"
            "  color: #fff;\n"
            "}\n\n"
            "/* ===== 실습 =====\n"
            "   class=\"sunset\" 박스에 위→아래로 #ff7e5f 에서 #feb47b 로\n"
            "   바뀌는 직선 그라데이션을 넣어보세요. */\n\n"
            "/* 모범 답안 */\n"
            ".sunset {\n"
            "  background: linear-gradient(to bottom, #ff7e5f, #feb47b);\n"
            "}\n"
        ),
    ),

    Lesson(
        id="css-mid-07-units-calc",
        lang="css", level="중급",
        title="뷰포트 단위·calc()",
        summary="vw·vh·vmin/vmax 와 식 계산 calc()",
        explanation=(
            "[개요: 뷰포트 단위]\n"
            "'뷰포트'는 웹페이지가 표시되는 화면 창을 의미한다. 뷰포트 단위는 그 화면 크기에 비례해\n"
            "커지고 작아지는 단위이다. px 은 고정된 길이지만, 뷰포트 단위는 화면 크기에 맞춰 변한다.\n\n"
            "[핵심 개념: 뷰포트 단위]\n"
            "• vw : 화면 너비의 1%. 100vw 는 화면 가로 전체를 의미한다(view width).\n"
            "• vh : 화면 높이의 1%. 100vh 는 화면 세로 전체를 의미한다(view height).\n"
            "  height: 100vh 는 스크롤 없이 첫 화면을 꽉 채우는 섹션을 만든다.\n"
            "• vmin : 화면의 가로·세로 중 더 짧은 쪽의 1%. 정사각형을 만들 때 유용하다.\n"
            "• vmax : 화면의 가로·세로 중 더 긴 쪽의 1%.\n\n"
            "[개요: calc()]\n"
            "calc() 는 CSS 안에서 계산을 수행하는 기능이다. 서로 다른 단위(예: % 와 px)를 더하거나 빼서\n"
            "크기를 지정할 수 있다. CSS 는 'width: 100% - 240px' 를 직접 지정할 수 없으나 calc() 로 감싸면 계산된다.\n\n"
            "[핵심 개념: calc() 활용]\n"
            "• calc(100% - 240px) : 전체 너비에서 사이드바 240px 를 뺀 나머지 전부를 계산한다.\n"
            "• calc(100vh - 60px) : 화면 높이에서 헤더 60px 를 뺀 나머지이다. 헤더 아래를 화면 끝까지 채울 때 사용한다.\n"
            "• calc(16px + 2vw) : 최소 16px 를 보장하면서 화면이 커질수록 조금씩 커지는 글자 크기이다.\n\n"
            "[활용 목적]\n"
            "• 실제 화면은 고정된 부분(헤더·사이드바)과 나머지를 채우는 부분이 혼재한다.\n"
            "  고정 부분은 px 로, 나머지는 % 나 vh 로 표현되며, 이 둘을 빼서 나머지를 정확히 구할 때 calc() 가 필요하다.\n"
            "• 계산을 수동으로 하면 화면 크기 변화에 대응할 수 없으므로 브라우저에 계산을 위임한다.\n\n"
            "[유의 사항]\n"
            "• calc() 의 더하기·빼기(+ -) 기호 양옆에는 반드시 공백이 있어야 한다. calc(100%-240px) 처럼\n"
            "  붙여 쓰면 무시되므로 calc(100% - 240px) 처럼 띄어 써야 한다.\n"
            "• 모바일에서 100vh 는 주소창이 나타났다 사라지면서 실제보다 크게 잡힐 수 있다.\n\n"
            "[적용 결과]\n"
            "아래 코드를 적용하면 첫 화면을 꽉 채우는 섹션과, 고정 헤더를 뺀 나머지를 차지하는 본문이 생성된다."
        ),
        usage="첫 화면 풀스크린 섹션(100vh), 고정 헤더/사이드바를 제외한 영역 계산(calc) 등에 쓴다.",
        cons="모바일에서 100vh 는 주소창 때문에 실제보다 커 보일 수 있다. calc 의 + - 양옆 공백을 빼면 무시된다.",
        code=(
            "/* 첫 화면을 꽉 채우는 섹션 */\n"
            ".fullscreen {\n"
            "  width: 100vw;\n"
            "  height: 100vh;\n"
            "}\n\n"
            "/* 고정 헤더(60px)를 뺀 나머지 높이 */\n"
            ".main {\n"
            "  height: calc(100vh - 60px);\n"
            "}\n\n"
            "/* 사이드바(240px)를 뺀 본문 너비 */\n"
            ".content {\n"
            "  width: calc(100% - 240px);\n"
            "}\n\n"
            "/* 화면 크기에 비례하는 글자 크기(최소 16 + 화면비례) */\n"
            ".fluid-title {\n"
            "  font-size: calc(16px + 2vw);\n"
            "}\n\n"
            "/* ===== 실습 =====\n"
            "   class=\"square\" 를 화면 짧은 변의 50% 크기인\n"
            "   정사각형으로 만들어보세요. */\n\n"
            "/* 모범 답안 */\n"
            ".square {\n"
            "  width: 50vmin;\n"
            "  height: 50vmin;\n"
            "}\n"
        ),
    ),

    Lesson(
        id="css-mid-08-cursor-outline",
        lang="css", level="중급",
        title="cursor·outline",
        summary="마우스 커서 모양과 포커스 외곽선",
        explanation=(
            "[개요: cursor]\n"
            "cursor 는 마우스를 요소 위에 올렸을 때 표시되는 포인터 모양을 지정하는 속성이다.\n"
            "커서 모양은 사용자에게 해당 위치에서 가능한 동작을 알려주는 신호 역할을 한다.\n\n"
            "[핵심 개념: cursor 값]\n"
            "• cursor: pointer; : 손가락 모양으로, 클릭 가능함을 의미한다. 버튼·링크에 지정한다.\n"
            "• cursor: text; : I자 모양으로, 글자를 선택/입력할 수 있음을 의미한다.\n"
            "• cursor: not-allowed; : 금지 표시(⊘)로, 현재 클릭할 수 없음을 의미한다. 비활성 버튼에 사용한다.\n"
            "• cursor: move / grab; : 끌어서 옮길 수 있음을 의미한다.\n"
            "• cursor: wait; : 처리 중이니 대기하라는 의미이다.\n\n"
            "[개요: outline]\n"
            "outline 은 요소 바깥에 그려지는 테두리 선으로, border 와 결정적 차이가 있다.\n"
            "• outline 은 요소의 크기(레이아웃)에 영향을 주지 않는다. 요소 바깥에 겹쳐 그려지므로\n"
            "  선이 생겨도 요소가 커지거나 옆 요소가 밀리지 않는다. border 는 두께만큼 요소를 밀어낸다.\n"
            "• 주요 용도는 포커스 링(focus ring)이다. 키보드 Tab 키로 이동할 때 현재 위치를 테두리로 표시한다.\n"
            "  마우스 없이 키보드만 사용하는 사용자에게 이 표시는 필수적이다.\n\n"
            "[핵심 개념: outline 값]\n"
            "• outline: 2px solid #3498db; : 두께 2px, 실선, 파란색 외곽선을 그린다.\n"
            "• outline: none; : 외곽선을 제거한다(단, 주의 사항 참고).\n"
            "• outline-offset: 2px; : 외곽선을 요소에서 바깥으로 떨어뜨려 틈을 만든다.\n"
            "• :focus-visible : 키보드로 이동했을 때만 외곽선을 표시하는 상태이다. 마우스 클릭 시에는\n"
            "  표시하지 않고 키보드 사용자에게만 링을 표시하는 방식이다.\n\n"
            "[유의 사항]\n"
            "• 디자인을 이유로 outline: none 으로 포커스 링을 제거하면 키보드 사용자가 현재 위치를 알 수 없어\n"
            "  접근성 문제가 발생한다.\n"
            "• 제거하려면 반드시 :focus-visible 등으로 대체 표시를 제공해야 한다.\n\n"
            "[적용 결과]\n"
            "아래 코드를 적용하면 버튼 위에서 손가락 커서가 표시되고, 키보드로 포커스하면 파란 외곽선이 나타난다."
        ),
        usage="클릭 가능한 요소(cursor:pointer)와 키보드 포커스 표시(outline) 등 사용성·접근성 신호에 쓴다.",
        cons="디자인을 이유로 outline: none 만 주고 대체 표시를 안 하면 키보드 사용자가 길을 잃는다. 꼭 :focus-visible 등으로 대체하라.",
        code=(
            "/* 클릭 가능 신호 */\n"
            ".btn { cursor: pointer; }\n"
            ".disabled { cursor: not-allowed; }\n\n"
            "/* 기본 외곽선을 없애되, 또렷한 커스텀 포커스 링으로 대체 */\n"
            ".input:focus {\n"
            "  outline: 2px solid #3498db;\n"
            "  outline-offset: 2px;   /* 요소에서 살짝 띄움 */\n"
            "}\n\n"
            "/* 키보드 포커스에만 외곽선 표시(마우스 클릭 땐 X) */\n"
            ".btn:focus-visible {\n"
            "  outline: 3px solid #f39c12;\n"
            "}\n\n"
            "/* ===== 실습 =====\n"
            "   class=\"link-card\" 에 마우스를 올리면 손가락 커서가 되고,\n"
            "   포커스되면 2px 회색 외곽선이 4px 떨어져 그려지게 만들어보세요. */\n\n"
            "/* 모범 답안 */\n"
            ".link-card { cursor: pointer; }\n"
            ".link-card:focus {\n"
            "  outline: 2px solid #888;\n"
            "  outline-offset: 4px;\n"
            "}\n"
        ),
    ),

    # ===================== 고급 =====================
    Lesson(
        id="css-adv-04-flex-grow",
        lang="css", level="고급",
        title="Flex 심화(grow·shrink·basis)",
        summary="자식이 공간을 늘리고 줄이는 규칙",
        explanation=(
            "[개요]\n"
            "Flex 는 상자 안의 자식들을 한 줄로 배치하는 기능이며, 본 주제에서는 자식들이 남는 공간을\n"
            "어떻게 나눠 갖고 공간이 부족할 때 어떻게 줄어드는지를 다룬다.\n"
            "이 규칙은 flex 속성 하나에 세 값을 지정해 정한다: flex: [grow] [shrink] [basis]\n\n"
            "[핵심 개념: 세 값]\n"
            "• flex-basis (기준 크기) : 늘거나 줄기 전의 출발 크기이다. 예를 들어 200px 면 200px 로 시작한다.\n"
            "  auto 면 내용물 크기를 기준으로 삼는다.\n"
            "• flex-grow (커지는 비율) : 남는 공간이 있을 때 얼마나 더 차지할지의 비율이다.\n"
            "  0 이면 커지지 않고, 2면 1인 형제보다 두 배 더 많이 차지한다.\n"
            "• flex-shrink (줄어드는 비율) : 공간이 부족할 때 얼마나 줄어들지의 비율이다.\n"
            "  0 이면 줄어들지 않는다.\n\n"
            "[핵심 개념: 자주 쓰는 축약형]\n"
            "• flex: 1 : '1 1 0' 의 축약형. 형제들과 남는 공간을 균등하게 나눈다.\n"
            "• flex: none : '0 0 auto' 의 축약형. 커지지도 줄어들지도 않는 고정 크기가 된다.\n"
            "• flex: 0 0 240px : 커지지도 줄어들지도 않고 240px 를 유지한다. 사이드바처럼 폭을 고정할 때 사용한다.\n\n"
            "[대표 패턴: 사이드바 + 본문]\n"
            "• 사이드바는 flex: 0 0 240px (항상 240px 고정), 본문은 flex: 1 (남는 공간 전부 차지)로 지정한다.\n"
            "• 화면 크기가 바뀌어도 사이드바는 유지되고 본문만 늘고 줄어드는, 흔히 쓰이는 구조이다.\n\n"
            "[유의 사항]\n"
            "1) grow·shrink·basis 세 값이 서로 얽혀 예상과 다른 크기가 나오는 경우가 잦으므로,\n"
            "   하나씩 변경하며 확인하는 것이 좋다.\n"
            "2) flex 자식 안에 긴 텍스트가 있으면, 자식이 줄어들어야 하는데도 줄어들지 않아 옆으로\n"
            "   넘칠 수 있다. 이때 해당 자식에 min-width: 0 을 지정하면 비로소 줄어든다.\n\n"
            "[적용 결과]\n"
            "아래 코드를 적용하면 고정 너비 사이드바 옆에서 본문이 남는 공간을 모두 차지하고, 두 카드는 2:1 비율로 공간을 나눈다."
        ),
        usage="고정 영역 + 가변 영역(사이드바/본문), 비율로 나누는 카드 등 정교한 1차원 분배에 쓴다.",
        cons="grow/shrink/basis 의 상호작용이 직관적이지 않아 의도와 다른 크기가 나오기 쉽다. min-width:0 을 안 주면 내용이 안 줄어드는 함정도 있다.",
        code=(
            ".layout { display: flex; gap: 16px; }\n\n"
            "/* 사이드바: 240px 고정(안 커지고 안 줄어듦) */\n"
            ".layout .sidebar { flex: 0 0 240px; }\n\n"
            "/* 본문: 남는 공간 전부 차지 */\n"
            ".layout .main { flex: 1; }\n\n"
            "/* 두 카드를 2 : 1 비율로 분배 */\n"
            ".row { display: flex; gap: 12px; }\n"
            ".row .big   { flex: 2 1 0; }\n"
            ".row .small { flex: 1 1 0; }\n\n"
            "/* 긴 텍스트가 자식을 안 줄어들게 막는 경우 방지 */\n"
            ".row .main { min-width: 0; }\n\n"
            "/* ===== 실습 =====\n"
            "   세 항목 중 가운데(.center)만 남는 공간을 차지하고\n"
            "   양옆(.side)은 100px 로 고정되게 flex 값을 정해보세요. */\n\n"
            "/* 모범 답안 */\n"
            ".side   { flex: 0 0 100px; }\n"
            ".center { flex: 1 1 0; }\n"
        ),
    ),

    Lesson(
        id="css-adv-05-grid-areas",
        lang="css", level="고급",
        title="grid-template-areas",
        summary="이름 붙인 영역으로 레이아웃 그리기",
        explanation=(
            "[개요]\n"
            "grid-template-areas 는 격자(grid)의 칸들에 이름을 부여해, 화면 배치를 설계도처럼 문자열로\n"
            "표현하는 방법이다. 숫자로 위치를 세는 대신 이름으로 직관적으로 배치할 수 있다.\n\n"
            "[핵심 개념: 속성]\n"
            "• display: grid; : 상자를 격자로 만든다.\n"
            "• grid-template-columns: 200px 1fr; : 열을 나누는 방식이다. '왼쪽 200px 고정, 오른쪽은\n"
            "  나머지 전부(1fr)'를 의미하며, 1fr 은 '남는 공간 한 몫'을 뜻한다.\n"
            "• grid-template-rows: 60px 1fr 40px; : 행을 나눈다. '위 60px(헤더), 가운데 나머지, 아래 40px(푸터)'.\n"
            "• grid-template-areas: 각 행을 문자열로 표현하는 핵심 속성이다.\n"
            "    'header  header'   한 줄에 같은 이름을 두 번 적으면 두 칸이 합쳐져 하나의 넓은 영역이 된다.\n"
            "    'sidebar main'     (header 가 가로 두 칸을 모두 차지해 맨 위를 가로지른다.)\n"
            "    'footer  footer'   빈 칸으로 두려면 점(.)을 적는다.\n"
            "• grid-area: header; : 자식에 지정한다. 해당 자식을 header 라고 이름 붙인 영역에 배치한다.\n\n"
            "[반응형 대응이 쉬운 이유]\n"
            "• @media 안에서 areas 문자열만 세로로 쌓이도록 다시 그리면 된다.\n"
            "• HTML 은 그대로 두고 배치만 바꾸므로, 데스크톱은 '사이드바+본문' 나란히, 모바일은\n"
            "  '위아래로 쌓기'로 손쉽게 전환할 수 있다.\n\n"
            "[유의 사항]\n"
            "• areas 문자열의 칸 개수는 grid-template-columns 로 정한 열 개수와 일치해야 한다.\n"
            "  한 줄에 이름을 2개 적었으면 열도 2개여야 하며, 불일치하면 오류가 발생한다.\n"
            "• 항목 개수가 계속 변하는 목록(예: 상품 카드 여러 개)에는 부적합하며, 이 경우 areas 없이\n"
            "  자동 배치를 사용한다.\n\n"
            "[적용 결과]\n"
            "아래 코드를 적용하면 헤더·사이드바·본문·푸터가 의도한 자리에 배치된 전형적인 앱 레이아웃이 생성된다."
        ),
        usage="헤더/사이드바/본문/푸터 같은 페이지 골격을 직관적으로 잡고, 반응형으로 배치를 바꿀 때 쓴다.",
        cons="areas 문자열의 칸 수가 열 정의와 어긋나면 오류가 난다. 동적으로 항목 수가 변하는 목록에는 부적합하다.",
        code=(
            ".app {\n"
            "  display: grid;\n"
            "  grid-template-columns: 200px 1fr;\n"
            "  grid-template-rows: 60px 1fr 40px;\n"
            "  grid-template-areas:\n"
            "    'header  header'\n"
            "    'sidebar main'\n"
            "    'footer  footer';\n"
            "  gap: 8px;\n"
            "  height: 100vh;\n"
            "}\n"
            ".app > .head { grid-area: header; }\n"
            ".app > .side { grid-area: sidebar; }\n"
            ".app > .body { grid-area: main; }\n"
            ".app > .foot { grid-area: footer; }\n\n"
            "/* 좁은 화면에선 한 줄로 쌓기 */\n"
            "@media (max-width: 700px) {\n"
            "  .app {\n"
            "    grid-template-columns: 1fr;\n"
            "    grid-template-areas:\n"
            "      'header'\n"
            "      'main'\n"
            "      'sidebar'\n"
            "      'footer';\n"
            "  }\n"
            "}\n\n"
            "/* ===== 실습 =====\n"
            "   'nav' 와 'content' 두 영역을 좌우로 두는\n"
            "   grid-template-areas 를 작성해보세요(nav 150px, content 나머지). */\n\n"
            "/* 모범 답안 */\n"
            ".two {\n"
            "  display: grid;\n"
            "  grid-template-columns: 150px 1fr;\n"
            "  grid-template-areas: 'nav content';\n"
            "}\n"
        ),
    ),

    Lesson(
        id="css-adv-06-custom-properties",
        lang="css", level="고급",
        title="CSS 변수(custom properties·var())",
        summary="--이름 변수와 var() 로 런타임 값 공유",
        explanation=(
            "[개요]\n"
            "CSS 변수는 자주 쓰는 값(색·간격 등)에 이름을 부여해 저장하고, 필요할 때 그 이름으로 참조하는 기능이다.\n"
            "브랜드 색을 변수에 저장해 두면 색을 변경할 때 변수 한 줄만 수정해 사이트 전체에 반영할 수 있다.\n\n"
            "[핵심 개념: 문법]\n"
            "• --color-bg: #ffffff; : 변수를 선언한다. 이름은 반드시 '--'로 시작한다.\n"
            "• var(--color-bg) : 저장된 값을 참조해 사용한다.\n"
            "• :root { ... } : 변수를 최상위(문서 전체)에 선언하는 위치이다. 여기 선언하면 어디서든 참조할 수 있으며,\n"
            "  색·간격 같은 디자인 기본값(토큰)을 한곳에 모아두는 자리이다.\n"
            "• var(--space, 8px) : 두 번째 값은 기본값(폴백)이다. --space 가 없으면 대신 8px 를 사용한다.\n\n"
            "[핵심 개념: SCSS 변수($)와의 차이]\n"
            "• SCSS 의 $변수는 파일을 컴파일해 내보낼 때 값이 확정되므로, 완성된 화면에서는 변경할 수 없다.\n"
            "• CSS 변수는 브라우저에서 살아 있어, JavaScript 로 실시간 변경하거나 특정 영역 안에서 값을\n"
            "  재정의해 덮어쓸 수 있다. 이것이 컴파일 타임(SCSS) vs 런타임(CSS 변수)의 결정적 차이이다.\n\n"
            "[핵심 개념: 상속을 이용한 테마 전환]\n"
            "• CSS 변수는 부모에서 자식으로 상속된다. 어떤 영역에 .theme-dark 를 붙이고 그 안에서\n"
            "  --color-bg 를 어두운 색으로 재정의하면, 그 영역 안의 모든 var(--color-bg) 가 함께 어두워진다.\n"
            "• 클래스 하나를 붙이고 떼는 것만으로 다크모드를 구현할 수 있다.\n\n"
            "[유의 사항]\n"
            "• 매우 오래된 브라우저(IE)는 CSS 변수를 지원하지 않는다.\n"
            "• SCSS 변수($)와 CSS 변수(--)를 혼동하기 쉬우며, 실시간으로 바뀌어야 하는 값은 CSS 변수를 사용한다.\n\n"
            "[적용 결과]\n"
            "아래 코드를 적용하면 .theme-dark 가 붙은 영역만 변수 값이 바뀌어 색이 통째로 어두워진다."
        ),
        usage="테마(다크모드)·간격 스케일 등 런타임에 바뀌어야 하는 값, JS 와 연동하는 동적 스타일에 쓴다.",
        cons="구형 브라우저(IE)는 지원하지 않는다. SCSS 변수와 혼동하기 쉬우니 '컴파일 타임(SCSS) vs 런타임(CSS변수)' 차이를 기억해야 한다.",
        code=(
            "/* 전역 토큰 선언 */\n"
            ":root {\n"
            "  --color-bg: #ffffff;\n"
            "  --color-text: #222222;\n"
            "  --gap: 16px;\n"
            "}\n\n"
            ".page {\n"
            "  background: var(--color-bg);\n"
            "  color: var(--color-text);\n"
            "  padding: var(--gap);\n"
            "}\n\n"
            "/* 특정 영역에서 변수만 다시 정의 → 다크 테마 */\n"
            ".theme-dark {\n"
            "  --color-bg: #1e1e1e;\n"
            "  --color-text: #f0f0f0;\n"
            "}\n\n"
            "/* 폴백 기본값 사용 */\n"
            ".box { margin: var(--space, 8px); }\n\n"
            "/* ===== 실습 =====\n"
            "   --radius 변수를 :root 에 12px 로 선언하고,\n"
            "   .card 의 border-radius 에 var() 로 적용해보세요. */\n\n"
            "/* 모범 답안 */\n"
            ":root { --radius: 12px; }\n"
            ".card { border-radius: var(--radius); }\n"
        ),
    ),

    Lesson(
        id="css-adv-07-filter",
        lang="css", level="고급",
        title="filter·backdrop-filter",
        summary="흐림·밝기 등 그래픽 효과와 배경 블러",
        explanation=(
            "[개요: filter]\n"
            "filter 는 요소에 흐림·밝기·흑백 등 그래픽 효과를 적용하는 기능이다. 사진 편집 앱의 필터와 유사하며,\n"
            "여러 효과를 공백으로 이어 적으면 한꺼번에 적용된다.\n\n"
            "[핵심 개념: filter 효과]\n"
            "• filter: blur(4px); : 4px 만큼 흐리게 처리한다. 숫자가 클수록 더 흐려진다.\n"
            "• filter: brightness(1.2); : 밝기를 조절한다. 1이 원본, 1.2면 20% 더 밝게, 0.8이면 어둡게 한다.\n"
            "• filter: contrast(120%); : 대비(명암 차이)를 키운다. 밝은 곳은 더 밝게, 어두운 곳은 더 어둡게 한다.\n"
            "• filter: grayscale(100%); : 색을 완전히 제거해 흑백으로 만든다. 0%면 원래 컬러이다.\n"
            "• filter: drop-shadow(...); : 요소의 모양을 따라가는 그림자이다. 투명 PNG 아이콘의 실제 모양대로\n"
            "  그림자가 생기며, 사각 상자 그림자인 box-shadow 와 다르다.\n\n"
            "[개요: backdrop-filter]\n"
            "backdrop-filter 는 요소 자신이 아니라, 요소 뒤에 비치는 배경에 효과를 적용하는 기능이다.\n"
            "• filter : 요소와 그 내용에 효과를 적용한다(대상 자체가 변함).\n"
            "• backdrop-filter : 요소가 덮고 있는 뒤쪽 배경에 효과를 적용한다(뒤 배경이 변함).\n"
            "• 반투명 유리 너머 풍경이 흐려 보이는 젖빛 유리 효과(글래스모피즘)를 만들며, 반투명 헤더·모달에 사용한다.\n"
            "• 유리 느낌을 제대로 내려면 보통 반투명 배경색(rgba)과 함께 사용한다.\n\n"
            "[활용 목적]\n"
            "• 흑백 썸네일에 마우스를 올리면 컬러로 전환(호버 효과)하거나, 반투명 헤더 뒤 내용을 흐리게 해\n"
            "  유리 느낌을 주는 등, 별도 이미지 파일 없이 CSS 만으로 시각 효과를 낼 수 있다.\n\n"
            "[유의 사항]\n"
            "• blur 나 backdrop-filter 는 GPU 가 실시간으로 계산하므로, 많은 요소에 적용하면 화면이 느려진다.\n"
            "  꼭 필요한 곳에만 사용해야 한다.\n"
            "• backdrop-filter 는 일부 브라우저에서 지원이 제한적이라 대비책이 필요할 수 있다.\n\n"
            "[적용 결과]\n"
            "아래 코드를 적용하면 흑백이던 썸네일이 호버 시 컬러로 표시되고, 반투명 헤더 뒤 내용이 흐릿하게 비치는 유리 느낌이 된다."
        ),
        usage="이미지 보정(흑백/호버 컬러), 글래스모피즘 헤더·모달, 비활성 영역 흐림 처리 등에 쓴다.",
        cons="blur/backdrop-filter 는 GPU 부담이 커 많은 요소에 쓰면 느려진다. backdrop-filter 는 일부 브라우저 지원이 제한적이다.",
        code=(
            "/* 흑백 → 호버 시 컬러 */\n"
            ".thumb {\n"
            "  filter: grayscale(100%);\n"
            "  transition: filter 0.3s ease;\n"
            "}\n"
            ".thumb:hover { filter: grayscale(0%) brightness(1.05); }\n\n"
            "/* 여러 필터 동시 적용 */\n"
            ".dim { filter: brightness(0.7) blur(1px); }\n\n"
            "/* 유리 느낌 헤더: 뒤 배경을 흐리게 */\n"
            ".glass {\n"
            "  background: rgba(255, 255, 255, 0.4);\n"
            "  backdrop-filter: blur(8px);\n"
            "}\n\n"
            "/* ===== 실습 =====\n"
            "   class=\"avatar\" 이미지에 4px 흐림과\n"
            "   80% 밝기를 동시에 적용해보세요. */\n\n"
            "/* 모범 답안 */\n"
            ".avatar {\n"
            "  filter: blur(4px) brightness(0.8);\n"
            "}\n"
        ),
    ),

    Lesson(
        id="css-adv-08-clip-path",
        lang="css", level="고급",
        title="clip-path·도형 자르기",
        summary="다각형·원으로 요소를 임의 모양으로 오리기",
        explanation=(
            "[개요]\n"
            "clip-path 는 요소를 지정된 도형 모양으로 오려내는 기능이다. 지정한 도형 안쪽만 보이고 바깥은 잘려\n"
            "표시되지 않는다. 네모난 이미지를 원형 프로필 사진으로 만들거나, 배너 아래를 비스듬히 자를 때 사용한다.\n\n"
            "[핵심 개념: 도형 함수]\n"
            "• clip-path: circle(50%); : 원 모양으로 오린다. 50%면 요소에 꽉 차는 가장 큰 원이 되어\n"
            "  네모 사진이 원형 아바타가 된다.\n"
            "• clip-path: ellipse(...); : 타원 모양으로 오린다.\n"
            "• clip-path: inset(...); : 바깥쪽을 네모나게 잘라 안쪽 사각형만 남긴다. 둥근 모서리도 지정할 수 있다.\n"
            "• clip-path: polygon(x y, x y, ...); : 여러 점을 순서대로 이어 만든 다각형으로 오린다.\n"
            "  삼각형·평행사변형·육각형·말풍선 등 원하는 모양을 자유롭게 만들 수 있다.\n\n"
            "[핵심 개념: 좌표 읽는 법]\n"
            "• 좌표는 보통 % 로 지정한다. 요소의 왼쪽 위 구석이 0% 0%, 오른쪽 아래 구석이 100% 100% 이다.\n"
            "• polygon(0 0, 100% 0, 100% 85%, 0 100%) 은 왼쪽위 → 오른쪽위 → 오른쪽 85% 지점 → 왼쪽아래를\n"
            "  이어, 아래쪽이 비스듬히 기울어진 배너 모양을 만든다.\n\n"
            "[활용 목적]\n"
            "• 원형 아바타, 비스듬한 배너, 삼각형 화살표, 말풍선 등 비정형 모양을 만들 때, 별도 이미지 파일 없이\n"
            "  CSS 만으로 요소를 오릴 수 있어 색 변경이나 반응형 조절이 용이하다.\n"
            "• transition 과 함께 사용하면 모양이 점진적으로 변하는 효과도 구현할 수 있다.\n\n"
            "[유의 사항]\n"
            "• 잘려 나간 부분은 보이지 않을 뿐 아니라 클릭도 되지 않고 내용도 사라지므로, 중요한 버튼이\n"
            "  잘리지 않도록 주의해야 한다.\n"
            "• 복잡한 polygon 은 화면 크기가 바뀌면 % 좌표가 어긋나 모양이 틀어질 수 있어 반응형 확인이 필요하다.\n\n"
            "[적용 결과]\n"
            "아래 코드를 적용하면 정사각 이미지가 원형 아바타로 표시되고, 배너 아래쪽이 비스듬히 잘린다."
        ),
        usage="원형 아바타, 비스듬한 배너, 삼각형 화살표·말풍선 같은 비정형 모양을 이미지 추가 없이 만들 때 쓴다.",
        cons="잘린 영역은 클릭·내용도 사라지므로 주의해야 한다. 복잡한 polygon 은 반응형에서 좌표가 어긋나기 쉽다.",
        code=(
            "/* 정사각 이미지를 원형 아바타로 */\n"
            ".avatar {\n"
            "  width: 96px; height: 96px;\n"
            "  clip-path: circle(50%);\n"
            "}\n\n"
            "/* 아래쪽이 비스듬히 잘린 배너 */\n"
            ".banner {\n"
            "  clip-path: polygon(0 0, 100% 0, 100% 85%, 0 100%);\n"
            "}\n\n"
            "/* 오른쪽을 향한 삼각형 */\n"
            ".arrow {\n"
            "  width: 0; height: 0;\n"
            "  clip-path: polygon(0 0, 100% 50%, 0 100%);\n"
            "  background: #3498db;\n"
            "  width: 20px; height: 20px;\n"
            "}\n\n"
            "/* ===== 실습 =====\n"
            "   class=\"hexa\" 박스를 육각형으로 오려보세요\n"
            "   (polygon 의 여섯 점을 이용). */\n\n"
            "/* 모범 답안 */\n"
            ".hexa {\n"
            "  clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%);\n"
            "}\n"
        ),
    ),
]
