"""CSS 문제/레슨 (랭크 없이 기초·중급·고급 각 3개, 총 9개).

CSS는 실행 채점이 아니라 코드/설명을 제공하는 학습 자료다.
각 레슨의 code 에는 예시 CSS 와 "실습" 과제, 모범 CSS 가 함께 들어 있다.
"""

from engine.models import Lesson

LESSONS = [

    # ===================== 기초 =====================
    Lesson(
        id="css-basic-01-selector",
        lang="css", level="기초",
        title="선택자(태그·class·id·후손)",
        summary="요소를 골라 스타일을 적용하는 규칙",
        explanation=(
            "CSS는 '어떤 요소를(선택자) 어떻게(속성) 꾸밀지'를 적는다.\n"
            "- 태그 선택자: p { } → 모든 <p>에 적용.\n"
            "- class 선택자: .box { } → class=\"box\" 인 요소들에 적용(여러 개 가능).\n"
            "- id 선택자: #title { } → id=\"title\" 인 단 하나의 요소에 적용.\n"
            "- 후손 선택자: nav a { } → <nav> 안에 있는 모든 <a> 에만 적용.\n"
            "우선순위는 id > class > 태그 순이라, 겹치면 더 구체적인 선택자가 이긴다.\n"
            "아래 예시를 적용하면, 제목 글자는 파란색, 'box' 카드들은 회색 배경,\n"
            "메뉴(nav) 안의 링크만 글자에 밑줄이 사라진 화면이 된다."
        ),
        usage="모든 스타일링의 출발점. 재사용할 디자인은 class, 페이지에 하나뿐인 요소는 id 로 지정한다.",
        cons="id 와 인라인 스타일을 남발하면 우선순위가 꼬여 나중에 덮어쓰기가 어려워진다. 보통 class 위주로 작성한다.",
        code=(
            "/* 예시 HTML 기준\n"
            "<h1 id=\"title\">제목</h1>\n"
            "<div class=\"box\">카드1</div>\n"
            "<div class=\"box\">카드2</div>\n"
            "<nav><a href=\"#\">메뉴</a></nav>\n"
            "*/\n\n"
            "/* 태그 선택자 */\n"
            "p { color: #333; }\n\n"
            "/* id 선택자: 하나뿐인 제목 */\n"
            "#title { color: blue; }\n\n"
            "/* class 선택자: 여러 카드에 공통 적용 */\n"
            ".box { background: #eee; padding: 10px; }\n\n"
            "/* 후손 선택자: nav 안의 a 만 */\n"
            "nav a { text-decoration: none; }\n\n"
            "/* ===== 실습 =====\n"
            "   class=\"btn\" 버튼은 초록 배경,\n"
            "   id=\"logo\" 요소는 글자 크기 24px,\n"
            "   footer 안의 a 는 회색으로 만들어보세요. */\n\n"
            "/* 모범 답안 */\n"
            ".btn   { background: green; color: white; }\n"
            "#logo  { font-size: 24px; }\n"
            "footer a { color: gray; }\n"
        ),
    ),

    Lesson(
        id="css-basic-02-boxmodel",
        lang="css", level="기초",
        title="박스모델(margin·padding·border)",
        summary="모든 요소는 내용+안쪽여백+테두리+바깥여백 상자",
        explanation=(
            "모든 HTML 요소는 사각형 상자다. 안쪽부터 바깥으로:\n"
            "- content(내용) → padding(안쪽 여백) → border(테두리) → margin(바깥 여백).\n"
            "padding 은 테두리 안쪽 공간을 넓혀 내용과 테두리를 띄우고,\n"
            "margin 은 다른 요소와의 바깥 간격을 만든다.\n"
            "기본값(content-box)에서는 width 가 내용만의 너비라, padding·border 만큼 실제 크기가 커진다.\n"
            "box-sizing: border-box 로 바꾸면 width 안에 padding·border 가 포함되어 크기 계산이 쉬워진다.\n"
            "아래를 적용하면, 흰 카드 둘레에 회색 테두리가 있고 내부 글자는 안쪽으로 20px 떨어지며,\n"
            "카드끼리는 위아래로 16px 간격이 벌어진 화면이 된다."
        ),
        usage="간격·여백 조절의 핵심. 레이아웃이 빽빽하거나 너무 붙어 보일 때 padding/margin 으로 숨통을 틔운다.",
        cons="margin 은 위아래가 서로 합쳐지는 '마진 상쇄'가 있어 예상과 다르게 보일 수 있다. box-sizing 을 안 맞추면 width 계산이 어긋난다.",
        code=(
            "/* 박스모델 기본 */\n"
            ".card {\n"
            "  width: 200px;\n"
            "  padding: 20px;          /* 내용과 테두리 사이 안쪽 여백 */\n"
            "  border: 1px solid #ccc; /* 테두리 */\n"
            "  margin: 16px 0;         /* 위아래 16px 바깥 여백 */\n"
            "  background: white;\n"
            "}\n\n"
            "/* 크기 계산을 직관적으로: width 에 padding/border 포함 */\n"
            "* { box-sizing: border-box; }\n\n"
            "/* ===== 실습 =====\n"
            "   class=\"profile\" 박스를 만들어보세요.\n"
            "   - 안쪽 여백 24px, 둥근 테두리(2px, 파란색),\n"
            "   - 모서리 둥글게 8px, 바깥 여백은 위아래 12px */\n\n"
            "/* 모범 답안 */\n"
            ".profile {\n"
            "  padding: 24px;\n"
            "  border: 2px solid blue;\n"
            "  border-radius: 8px;\n"
            "  margin: 12px 0;\n"
            "}\n"
        ),
    ),

    Lesson(
        id="css-basic-03-text",
        lang="css", level="기초",
        title="색·단위·텍스트 스타일",
        summary="color/background · px·em·rem·% · font 속성",
        explanation=(
            "색은 이름(red), 16진수(#3498db), rgb/rgba(0,0,0,0.5) 로 지정한다. rgba 의 마지막 값은 투명도다.\n"
            "단위는 px(고정 픽셀), %(부모 기준 비율), em(현재 글자 크기 기준), rem(루트 글자 크기 기준)이 대표적이다.\n"
            "rem 은 html 의 글꼴 크기를 기준으로 해서 전체 크기를 한 곳에서 조절하기 좋다.\n"
            "텍스트는 font-size(크기), font-weight(굵기), line-height(줄간격),\n"
            "text-align(정렬), color 로 꾸민다.\n"
            "아래를 적용하면, 본문 글자는 16px·줄간격 1.6 으로 읽기 편하고,\n"
            "제목은 진한 파란색·굵게·가운데 정렬된 화면이 된다."
        ),
        usage="가독성의 기본. 본문은 line-height 1.5~1.7, 단위는 rem/em 으로 통일하면 반응형·확대에 유리하다.",
        cons="px 만 쓰면 사용자가 글꼴을 키워도 안 커져 접근성이 떨어진다. 색 대비가 약하면 글씨가 잘 안 보인다.",
        code=(
            "/* 루트 기준 크기(rem 의 기준이 됨) */\n"
            "html { font-size: 16px; }\n\n"
            "body {\n"
            "  color: #333;            /* 진회색 본문 */\n"
            "  font-size: 1rem;        /* = 16px */\n"
            "  line-height: 1.6;       /* 줄간격 넉넉하게 */\n"
            "}\n\n"
            "h1 {\n"
            "  color: #2c3e50;\n"
            "  font-size: 2rem;        /* = 32px */\n"
            "  font-weight: bold;\n"
            "  text-align: center;\n"
            "}\n\n"
            ".muted { color: rgba(0, 0, 0, 0.5); }  /* 반투명 회색 */\n\n"
            "/* ===== 실습 =====\n"
            "   class=\"price\" 가격 글자를 만들어보세요.\n"
            "   - 글자 크기 1.5rem, 굵게, 빨간색(#e74c3c), 오른쪽 정렬 */\n\n"
            "/* 모범 답안 */\n"
            ".price {\n"
            "  font-size: 1.5rem;\n"
            "  font-weight: bold;\n"
            "  color: #e74c3c;\n"
            "  text-align: right;\n"
            "}\n"
        ),
    ),

    # ===================== 중급 =====================
    Lesson(
        id="css-mid-01-flexbox",
        lang="css", level="중급",
        title="Flexbox 레이아웃",
        summary="가로/세로 한 줄 정렬을 쉽게: justify·align",
        explanation=(
            "display: flex 를 부모에 주면 자식들이 한 줄(기본은 가로)로 늘어서고 정렬이 쉬워진다.\n"
            "- flex-direction: row(가로) / column(세로) → 주축 방향 결정.\n"
            "- justify-content: 주축 정렬(flex-start, center, space-between, space-around).\n"
            "- align-items: 교차축 정렬(stretch, center, flex-start, flex-end).\n"
            "- gap: 자식 사이 간격.\n"
            "자식에 flex: 1 을 주면 남는 공간을 나눠 가져 가변 너비가 된다.\n"
            "아래를 적용하면, 헤더 안에서 로고는 왼쪽, 메뉴는 오른쪽으로 밀려나고\n"
            "세로로는 가운데 정렬되며, 카드 3개가 같은 간격으로 나란히 놓인 화면이 된다."
        ),
        usage="네비게이션 바, 카드 나열, 가운데 정렬 등 1차원(한 방향) 정렬에 최적. 가운데 정렬의 정석.",
        cons="행과 열을 동시에 다루는 복잡한 2차원 배치는 Grid 가 더 적합하다. flex-wrap 을 안 주면 줄바꿈이 안 돼 좁은 화면에서 넘친다.",
        code=(
            "/* 가로 양끝 배치 + 세로 가운데 */\n"
            ".header {\n"
            "  display: flex;\n"
            "  justify-content: space-between;  /* 로고-메뉴 양끝으로 */\n"
            "  align-items: center;             /* 세로 가운데 */\n"
            "  padding: 12px 20px;\n"
            "}\n\n"
            "/* 카드 3개를 같은 간격으로 나란히, 좁으면 줄바꿈 */\n"
            ".cards {\n"
            "  display: flex;\n"
            "  gap: 16px;\n"
            "  flex-wrap: wrap;\n"
            "}\n"
            ".cards > .card { flex: 1; }   /* 남는 공간 균등 분배 */\n\n"
            "/* ===== 실습 =====\n"
            "   class=\"center-box\" 안의 내용을\n"
            "   가로·세로 모두 정중앙에 오도록 만들어보세요. */\n\n"
            "/* 모범 답안 */\n"
            ".center-box {\n"
            "  display: flex;\n"
            "  justify-content: center;\n"
            "  align-items: center;\n"
            "  height: 200px;\n"
            "}\n"
        ),
    ),

    Lesson(
        id="css-mid-02-position",
        lang="css", level="중급",
        title="position(relative·absolute·fixed)",
        summary="요소를 흐름에서 떼어 원하는 위치에 배치",
        explanation=(
            "position 은 요소의 배치 기준을 바꾼다.\n"
            "- static: 기본값, 문서 흐름 그대로.\n"
            "- relative: 원래 자리를 기준으로 top/left 만큼 살짝 이동(자리는 유지).\n"
            "- absolute: 가장 가까운 'position 이 static 이 아닌 조상'을 기준으로 배치(흐름에서 빠짐).\n"
            "- fixed: 화면(viewport) 기준 고정. 스크롤해도 그 자리에 붙어 있음.\n"
            "흔한 패턴: 부모에 position: relative, 자식에 position: absolute 를 줘서\n"
            "부모 안의 특정 위치(예: 우상단 배지)에 자식을 고정한다.\n"
            "아래를 적용하면, 카드 우상단에 'NEW' 배지가 겹쳐 붙고,\n"
            "화면 오른쪽 아래에는 스크롤해도 따라다니는 '맨 위로' 버튼이 생긴 화면이 된다."
        ),
        usage="배지·툴팁·모달, 항상 떠 있는 버튼/헤더 등 겹치거나 고정해야 하는 요소에 사용.",
        cons="absolute/fixed 는 흐름에서 빠져 다른 요소와 겹칠 수 있고, z-index 관리가 까다롭다. 남용하면 반응형이 깨지기 쉽다.",
        code=(
            "/* 부모를 기준점으로 만들기 */\n"
            ".card {\n"
            "  position: relative;\n"
            "  padding: 20px;\n"
            "  border: 1px solid #ccc;\n"
            "}\n\n"
            "/* 부모 카드의 우상단에 배지 고정 */\n"
            ".card .badge {\n"
            "  position: absolute;\n"
            "  top: 8px;\n"
            "  right: 8px;\n"
            "  background: #e74c3c;\n"
            "  color: white;\n"
            "  padding: 2px 6px;\n"
            "  border-radius: 4px;\n"
            "}\n\n"
            "/* 화면에 고정되는 '맨 위로' 버튼 */\n"
            ".to-top {\n"
            "  position: fixed;\n"
            "  bottom: 20px;\n"
            "  right: 20px;\n"
            "}\n\n"
            "/* ===== 실습 =====\n"
            "   class=\"navbar\" 를 화면 상단에 항상 붙어 있게 만들어보세요.\n"
            "   (스크롤해도 위에 고정) */\n\n"
            "/* 모범 답안 */\n"
            ".navbar {\n"
            "  position: fixed;\n"
            "  top: 0;\n"
            "  left: 0;\n"
            "  width: 100%;\n"
            "  z-index: 100;\n"
            "}\n"
        ),
    ),

    Lesson(
        id="css-mid-03-pseudo",
        lang="css", level="중급",
        title="가상클래스·가상요소(:hover, ::before)",
        summary="상태(:hover)와 가짜 요소(::before)로 동적 표현",
        explanation=(
            "가상클래스(:)는 요소의 '상태'에 따라 스타일을 준다.\n"
            "- :hover 마우스를 올렸을 때, :focus 입력칸에 포커스됐을 때,\n"
            "- :first-child / :last-child / :nth-child(2n) 위치에 따라.\n"
            "가상요소(::)는 HTML에 없는 '가짜 요소'를 만들어 꾸민다.\n"
            "- ::before 내용 앞, ::after 내용 뒤에 content 로 글자/아이콘을 삽입.\n"
            "아래를 적용하면, 버튼에 마우스를 올리면 색이 진해지고,\n"
            "목록의 짝수 줄만 배경이 칠해지며, 필수 입력 라벨 앞에 빨간 '*' 가 붙는 화면이 된다."
        ),
        usage="버튼/링크 호버 효과, 줄무늬 표(zebra), 아이콘·말풍선 꼬리 등 JS 없이 시각 효과를 줄 때 사용.",
        cons="::before/::after 는 content 가 반드시 있어야 보이고, 빈 가상요소는 화면낭독기(스크린리더)가 못 읽어 접근성 정보로는 부적합하다.",
        code=(
            "/* 호버 상태 */\n"
            ".btn {\n"
            "  background: #3498db;\n"
            "  color: white;\n"
            "  padding: 10px 16px;\n"
            "}\n"
            ".btn:hover { background: #217dbb; }  /* 올리면 진하게 */\n\n"
            "/* 짝수 줄만 배경색(줄무늬) */\n"
            "li:nth-child(2n) { background: #f2f2f2; }\n\n"
            "/* 필수 라벨 앞에 빨간 별 삽입 */\n"
            ".required::before {\n"
            "  content: '*';\n"
            "  color: red;\n"
            "  margin-right: 4px;\n"
            "}\n\n"
            "/* ===== 실습 =====\n"
            "   링크(a)에 마우스를 올리면 밑줄이 생기게 하고,\n"
            "   class=\"new\" 항목 뒤에 ' (신규)' 글자가 붙도록 만들어보세요. */\n\n"
            "/* 모범 답안 */\n"
            "a { text-decoration: none; }\n"
            "a:hover { text-decoration: underline; }\n"
            ".new::after { content: ' (신규)'; color: #27ae60; }\n"
        ),
    ),

    # ===================== 고급 =====================
    Lesson(
        id="css-adv-01-grid",
        lang="css", level="고급",
        title="Grid 레이아웃",
        summary="행·열 2차원 격자 배치: template·gap·span",
        explanation=(
            "display: grid 는 화면을 행(row)과 열(column)의 격자로 나눠 2차원 배치를 한다.\n"
            "- grid-template-columns: 1fr 1fr 1fr → 동일 너비 3열(fr 은 남는 공간의 비율 단위).\n"
            "- grid-template-columns: 200px 1fr → 고정 200px 사이드바 + 나머지 본문.\n"
            "- gap: 셀 사이 간격.\n"
            "- repeat(3, 1fr) 로 반복을, grid-column: span 2 로 한 칸이 두 열을 차지하게 할 수 있다.\n"
            "- repeat(auto-fit, minmax(200px, 1fr)) 은 화면 너비에 맞춰 열 개수를 자동 조절한다.\n"
            "아래를 적용하면, 카드들이 200px 이상을 유지하며 화면 폭에 맞춰\n"
            "자동으로 2열·3열·4열로 재배치되는 반응형 갤러리 화면이 된다."
        ),
        usage="갤러리·대시보드·전체 페이지 레이아웃 등 행과 열을 함께 다루는 복잡한 배치에 최적.",
        cons="단순한 한 줄 정렬에는 Flexbox 가 더 간단하다. template 문법이 익숙해지기 전엔 다소 어렵게 느껴진다.",
        code=(
            "/* 화면 폭에 맞춰 열 개수가 자동 조절되는 갤러리 */\n"
            ".gallery {\n"
            "  display: grid;\n"
            "  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));\n"
            "  gap: 16px;\n"
            "}\n\n"
            "/* 사이드바 + 본문 2단 레이아웃 */\n"
            ".layout {\n"
            "  display: grid;\n"
            "  grid-template-columns: 200px 1fr;\n"
            "  gap: 20px;\n"
            "}\n\n"
            "/* 특정 카드만 두 열 차지 */\n"
            ".gallery .wide { grid-column: span 2; }\n\n"
            "/* ===== 실습 =====\n"
            "   class=\"grid3\" 안에 항목들을 항상 3열로,\n"
            "   셀 간격 12px 로 배치해보세요. */\n\n"
            "/* 모범 답안 */\n"
            ".grid3 {\n"
            "  display: grid;\n"
            "  grid-template-columns: repeat(3, 1fr);\n"
            "  gap: 12px;\n"
            "}\n"
        ),
    ),

    Lesson(
        id="css-adv-02-responsive",
        lang="css", level="고급",
        title="반응형(@media)",
        summary="화면 크기에 따라 다른 스타일: 미디어 쿼리",
        explanation=(
            "@media 쿼리는 화면 너비 등 조건에 맞을 때만 스타일을 적용해 기기별로 다른 레이아웃을 만든다.\n"
            "- @media (max-width: 768px) { } → 화면 폭이 768px 이하(모바일/태블릿)일 때.\n"
            "- @media (min-width: 1024px) { } → 1024px 이상(데스크톱)일 때.\n"
            "'모바일 퍼스트'는 기본을 모바일로 짠 뒤 min-width 로 넓은 화면을 더해 나가는 방식이다.\n"
            "반응형의 짝꿍으로 <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"> 가 필요하다.\n"
            "아래를 적용하면, 넓은 화면에서는 메뉴가 가로로 펼쳐지고 본문이 2단이지만,\n"
            "768px 이하 화면에서는 메뉴와 본문이 세로 1단으로 쌓이는 화면이 된다."
        ),
        usage="PC·태블릿·모바일을 하나의 CSS로 대응. 좁은 화면에서 가로 배치를 세로로 바꾸거나 글자 크기를 줄일 때 사용.",
        cons="중단점(breakpoint)이 많아지면 관리가 복잡해진다. 가능하면 flex/grid 의 자동 줄바꿈으로 쿼리 수를 줄이는 게 좋다.",
        code=(
            "/* 기본(넓은 화면): 가로 메뉴 + 2단 본문 */\n"
            ".menu { display: flex; gap: 20px; }\n"
            ".content {\n"
            "  display: grid;\n"
            "  grid-template-columns: 1fr 1fr;\n"
            "  gap: 20px;\n"
            "}\n\n"
            "/* 좁은 화면(768px 이하): 세로 1단으로 전환 */\n"
            "@media (max-width: 768px) {\n"
            "  .menu { flex-direction: column; }\n"
            "  .content { grid-template-columns: 1fr; }\n"
            "  body { font-size: 14px; }\n"
            "}\n\n"
            "/* ===== 실습 =====\n"
            "   class=\"box\" 의 너비를 기본 50% 로 두고,\n"
            "   600px 이하 화면에서는 100% 로 넓어지게 만들어보세요. */\n\n"
            "/* 모범 답안 */\n"
            ".box { width: 50%; }\n"
            "@media (max-width: 600px) {\n"
            "  .box { width: 100%; }\n"
            "}\n"
        ),
    ),

    Lesson(
        id="css-adv-03-animation",
        lang="css", level="고급",
        title="트랜지션·애니메이션(transition, @keyframes)",
        summary="부드러운 변화(transition)와 반복 동작(@keyframes)",
        explanation=(
            "transition 은 속성 값이 바뀔 때 그 변화를 부드럽게 이어준다.\n"
            "- transition: background 0.3s ease; → 배경색이 0.3초에 걸쳐 천천히 변함.\n"
            "  주로 :hover 같은 상태 변화와 함께 써서 자연스러운 효과를 낸다.\n"
            "@keyframes 는 0%~100% 구간별 스타일을 정의한 '애니메이션 대본'이다.\n"
            "- animation: 이름 2s infinite; 로 요소에 적용하며 반복·지속시간을 정한다.\n"
            "transform(translate/scale/rotate)은 이동·확대·회전을 GPU로 부드럽게 처리한다.\n"
            "아래를 적용하면, 버튼에 마우스를 올리면 살짝 커지며 색이 부드럽게 변하고,\n"
            "로딩 아이콘은 계속 빙글빙글 도는 화면이 된다."
        ),
        usage="버튼 호버 효과, 모달 등장, 로딩 스피너 등 사용자 피드백을 부드럽게 줄 때. transform+transition 조합이 성능에 좋다.",
        cons="동작이 과하거나 길면 오히려 답답하고 산만하다. width/top 같은 속성 애니메이션은 느릴 수 있어 transform/opacity 사용이 권장된다.",
        code=(
            "/* 부드러운 호버 전환 */\n"
            ".btn {\n"
            "  background: #3498db;\n"
            "  color: white;\n"
            "  padding: 10px 16px;\n"
            "  transition: background 0.3s ease, transform 0.2s ease;\n"
            "}\n"
            ".btn:hover {\n"
            "  background: #217dbb;\n"
            "  transform: scale(1.05);   /* 살짝 커짐 */\n"
            "}\n\n"
            "/* 반복 회전 애니메이션(로딩 스피너) */\n"
            "@keyframes spin {\n"
            "  from { transform: rotate(0deg); }\n"
            "  to   { transform: rotate(360deg); }\n"
            "}\n"
            ".spinner {\n"
            "  width: 32px; height: 32px;\n"
            "  border: 4px solid #eee;\n"
            "  border-top-color: #3498db;\n"
            "  border-radius: 50%;\n"
            "  animation: spin 1s linear infinite;\n"
            "}\n\n"
            "/* ===== 실습 =====\n"
            "   class=\"fade-in\" 요소가 나타날 때\n"
            "   투명(0)에서 불투명(1)으로 0.6초간 서서히 나타나는\n"
            "   애니메이션을 만들어보세요. */\n\n"
            "/* 모범 답안 */\n"
            "@keyframes fadeIn {\n"
            "  from { opacity: 0; }\n"
            "  to   { opacity: 1; }\n"
            "}\n"
            ".fade-in { animation: fadeIn 0.6s ease forwards; }\n"
        ),
    ),
]
