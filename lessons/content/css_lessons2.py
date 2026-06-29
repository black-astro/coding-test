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
            "CSS 에서 색은 여러 방식으로 적을 수 있고, 모두 같은 색을 가리킬 수 있다.\n"
            "- 16진수(hex): #rrggbb 또는 줄여서 #rgb. 예) #3498db, 흰색 #fff.\n"
            "  뒤에 두 자리를 더하면(#rrggbbaa) 투명도까지 표현한다.\n"
            "- rgb(): rgb(52, 152, 219) 처럼 빨강·초록·파랑을 0~255 로. rgba(...,0.5) 는 투명도.\n"
            "- hsl(): hsl(204, 70%, 53%) 처럼 색상(0~360도)·채도(%)·명도(%)로. 사람이 직관적으로 조절하기 좋다.\n"
            "hsl 은 '같은 색에서 더 밝게/연하게'를 명도·채도만 바꿔 쉽게 만들 수 있어 색 팔레트 설계에 유리하다.\n"
            "아래를 적용하면 세 박스가 모두 같은 파란색으로 칠해지고, 마지막 박스만 반투명해진 화면이 된다."
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
            "글꼴은 font-family 로 지정하며, 쉼표로 여러 개를 적으면 앞에서부터 사용 가능한 것을 쓴다(폰트 스택).\n"
            "맨 끝에는 sans-serif/serif 같은 '일반 계열'을 넣어, 앞 글꼴이 모두 없을 때 대체되게 한다.\n"
            "사용자 PC 에 없는 글꼴은 @font-face 로 폰트 파일을 직접 불러오거나, 외부 CSS(예: 구글폰트)를 link 한다.\n"
            "- font-family: 글꼴 이름, - font-weight: 굵기(400 보통, 700 굵게), - font-style: italic 기울임.\n"
            "여러 굵기를 쓸 땐 굵기별 폰트 파일을 각각 @font-face 로 등록해야 또렷하게 나온다.\n"
            "아래를 적용하면 본문은 시스템 기본 산세리프로, 제목은 불러온 'MyFont' 로 표시되는 화면이 된다."
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
            "목록(ul/ol)은 list-style 로 꾸민다.\n"
            "- list-style-type: disc(●)/circle(○)/square(■)/decimal(1.) 등 마커 모양.\n"
            "- list-style: none 으로 마커를 없애면 메뉴 같은 목록을 만들 수 있다.\n"
            "표(table)는 칸 사이 테두리가 기본적으로 떨어져 있는데,\n"
            "- border-collapse: collapse 를 주면 인접한 테두리가 하나로 합쳐져 깔끔해진다.\n"
            "- th/td 에 padding, text-align 으로 칸 안 여백·정렬을 맞추고,\n"
            "- tr:nth-child(even) 으로 줄무늬(zebra) 표를 만든다.\n"
            "아래를 적용하면 마커 없는 가로 메뉴와, 테두리가 합쳐지고 머리행이 강조된 표가 나오는 화면이 된다."
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
            "display 는 요소가 화면에서 자리를 차지하는 기본 방식을 정한다.\n"
            "- block: 한 줄을 통째로 차지(위아래로 쌓임). width/height/margin 상하 모두 적용. 예) div, p, h1.\n"
            "- inline: 글자처럼 줄 안에 흐름. width/height 와 상하 margin 이 먹지 않음. 예) span, a.\n"
            "- inline-block: 줄 안에 흐르되(inline) 크기·여백은 block 처럼 지정 가능. 버튼 나열에 유용.\n"
            "- none: 화면에서 완전히 사라짐(자리도 안 차지). visibility:hidden 과 달리 공간도 없앤다.\n"
            "아래를 적용하면 인라인이던 링크가 크기 지정 가능한 버튼처럼 나란히 놓이고,\n"
            "'숨김' 클래스가 붙은 요소는 화면에서 완전히 사라진 화면이 된다."
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
            "고정 크기 상자에 내용이 넘칠 때 어떻게 보일지 overflow 로 정한다.\n"
            "- visible(기본): 상자 밖으로 그대로 삐져나옴.\n"
            "- hidden: 넘친 부분을 잘라서 감춤.\n"
            "- scroll: 항상 스크롤바를 표시, - auto: 넘칠 때만 스크롤바.\n"
            "overflow-x / overflow-y 로 가로·세로를 따로 지정할 수도 있다.\n"
            "한 줄 말줄임(…)은 white-space: nowrap; overflow: hidden; text-overflow: ellipsis; 세 줄을 함께 쓴다.\n"
            "아래를 적용하면 높이가 고정된 영역은 세로 스크롤이 생기고,\n"
            "긴 제목은 끝이 '…' 로 잘려 한 줄로 보이는 화면이 된다."
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
            "float 은 요소를 좌(left)나 우(right)로 띄워, 뒤따르는 인라인 내용이 그 주위를 감싸 흐르게 한다.\n"
            "원래는 글 안에 그림을 끼워 글이 둘러싸게 하는 용도였다.\n"
            "- float: left/right 로 띄우고, - clear: both 로 '더 이상 감싸지 말고 아래로 내려가라'고 지시한다.\n"
            "떠 있는 자식 때문에 부모 높이가 0 으로 찌그러지는 문제는,\n"
            "부모에 '::after { content:''; display:block; clear:both; }'(clearfix) 를 줘서 해결한다.\n"
            "아래를 적용하면 썸네일이 왼쪽에 뜨고 글이 그 오른쪽을 감싸며,\n"
            "다음 섹션은 clear 로 아래로 내려가 겹치지 않는 화면이 된다."
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
            "화면에서 요소가 겹칠 때 무엇이 위에 보일지는 z-index 로 정한다. 값이 클수록 앞(위)에 온다.\n"
            "단, z-index 는 position 이 static 이 아닐 때(relative/absolute/fixed/sticky)만 동작한다.\n"
            "중요한 개념은 '쌓임 맥락(stacking context)'이다. 어떤 요소가 새 맥락을 만들면,\n"
            "그 자식들의 z-index 는 그 맥락 '안에서만' 비교되고, 바깥 요소와는 부모 단위로 겨룬다.\n"
            "position+z-index 외에 opacity(1 미만), transform, filter 등도 새 쌓임 맥락을 만든다.\n"
            "그래서 z-index: 9999 를 줬는데도 다른 요소에 가려지는 일이 생긴다(부모 맥락에 갇힘).\n"
            "아래를 적용하면 모달 뒷배경(overlay) 위에 모달 창이 또렷이 올라오는 화면이 된다."
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
            "background 는 여러 속성을 묶은 단축 속성이다.\n"
            "- background-color: 배경색, - background-image: url(...) 또는 그라데이션.\n"
            "- background-repeat: repeat/no-repeat, - background-position: center 등 위치.\n"
            "- background-size: cover(영역을 꽉 채움)/contain(잘리지 않게 맞춤).\n"
            "그라데이션도 이미지로 취급한다.\n"
            "- linear-gradient(방향, 색1, 색2): 직선 방향 색 변화.\n"
            "- radial-gradient(색1, 색2): 가운데서 바깥으로 퍼지는 원형 변화.\n"
            "쉼표로 여러 배경을 겹쳐 쌓을 수도 있다(앞에 적은 것이 위에 옴).\n"
            "아래를 적용하면 히어로 영역은 사진 위에 어두운 그라데이션이 덮여 글자가 잘 보이는 화면이 된다."
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
            "화면(viewport) 크기에 비례하는 단위가 있다.\n"
            "- vw: 화면 너비의 1%, - vh: 화면 높이의 1%. 100vh 면 화면 높이 전체.\n"
            "- vmin/vmax: 너비·높이 중 작은/큰 쪽의 1%. 정사각 비율 요소에 유용.\n"
            "calc() 는 단위가 다른 값끼리도 사칙연산으로 섞을 수 있게 해준다.\n"
            "- width: calc(100% - 240px) → 사이드바 240px 를 뺀 나머지 전부.\n"
            "- height: calc(100vh - 60px) → 헤더 높이를 뺀 화면 가득.\n"
            "연산자(+ -) 양옆에는 반드시 공백이 있어야 한다(곱셈·나눗셈은 한쪽이 숫자여야 함).\n"
            "아래를 적용하면 첫 화면을 꽉 채우는 섹션과, 고정 헤더를 뺀 나머지를 차지하는 본문이 만들어진다."
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
            "cursor 는 요소 위에서 마우스 포인터 모양을 바꾼다.\n"
            "- pointer(손가락, 클릭 가능), text(글자 선택), not-allowed(금지), move/grab, wait 등.\n"
            "클릭 가능한 요소엔 cursor: pointer 를 줘서 '눌러진다'는 신호를 주는 게 좋다.\n"
            "outline 은 테두리(border)와 비슷하지만 박스 크기(레이아웃)에 영향을 주지 않고 바깥에 그려진다.\n"
            "특히 키보드로 이동할 때 지금 어디에 포커스가 있는지 보여주는 'focus ring' 으로 중요하다.\n"
            "- outline: none 으로 없앨 수 있지만, 그러면 키보드 사용자가 위치를 못 봐 접근성이 나빠진다.\n"
            "- outline-offset 으로 외곽선을 요소에서 살짝 떨어뜨릴 수 있다.\n"
            "아래를 적용하면 버튼 위에서 손가락 커서가 뜨고, 키보드로 포커스하면 또렷한 파란 외곽선이 생긴다."
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
            "Flex 자식의 크기는 flex 단축 속성 = flex-grow flex-shrink flex-basis 세 값으로 정해진다.\n"
            "- flex-basis: 늘리기/줄이기 전의 '기준 크기'(예: 200px, 또는 auto=내용 크기).\n"
            "- flex-grow: 남는 공간을 나눠 가질 비율. 0 이면 안 커지고, 값이 크면 더 많이 가져간다.\n"
            "- flex-shrink: 공간이 모자랄 때 줄어드는 비율. 0 이면 안 줄어든다.\n"
            "자주 쓰는 축약: flex: 1 = '1 1 0'(남는 공간 균등 분배), flex: none = '0 0 auto'(고정).\n"
            "예) 사이드바는 flex: 0 0 240px(고정), 본문은 flex: 1(나머지 전부)로 두는 패턴이 흔하다.\n"
            "아래를 적용하면 고정 너비 사이드바 옆에서 본문이 남는 공간을 모두 차지하고,\n"
            "두 카드는 2:1 비율로 공간을 나눠 갖는 화면이 된다."
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
            "grid-template-areas 는 격자 칸에 이름을 붙여, 레이아웃을 '그림처럼' 표현하는 방법이다.\n"
            "부모에서 각 행을 문자열로 그린다. 예) \"header header\" \"sidebar main\" \"footer footer\".\n"
            "같은 이름을 가로/세로로 이어 적으면 그 칸들이 합쳐져 하나의 영역이 된다. 빈 칸은 점(.)으로 둔다.\n"
            "자식에는 grid-area: header 처럼 이름만 지정하면 해당 영역에 자동 배치된다.\n"
            "행/열 크기는 grid-template-rows / grid-template-columns 로 함께 정한다.\n"
            "@media 안에서 areas 문자열만 바꾸면, 같은 HTML 로 모바일·데스크톱 레이아웃을 손쉽게 전환할 수 있다.\n"
            "아래를 적용하면 헤더·사이드바·본문·푸터가 의도한 자리에 배치된 전형적인 앱 레이아웃이 된다."
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
            "CSS 자체의 변수다. --이름: 값; 으로 선언하고 var(--이름) 으로 꺼내 쓴다.\n"
            "보통 :root 에 전역으로 선언해 색·간격 같은 디자인 토큰을 한곳에서 관리한다.\n"
            "SCSS 변수($)와 달리 '브라우저에서 실시간으로 살아 있어' JS 로 바꾸거나, 특정 영역에서 다시 정의해 덮을 수 있다.\n"
            "- var(--gap, 16px) 처럼 두 번째 인자로 기본값(폴백)을 줄 수 있다.\n"
            "- 상속되므로, 부모에서 --color 를 바꾸면 그 안쪽 모든 var(--color) 가 따라 바뀐다.\n"
            "이 성질을 이용해 다크모드 등 테마 전환을 클래스 하나로 구현할 수 있다.\n"
            "아래를 적용하면 .theme-dark 가 붙은 영역만 변수 값이 바뀌어 색이 통째로 어두워지는 화면이 된다."
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
            "filter 는 요소 자체에 그래픽 효과를 입힌다(여러 개를 공백으로 이어 적용).\n"
            "- blur(4px) 흐림, - brightness(1.2) 밝기, - contrast(120%) 대비,\n"
            "- grayscale(100%) 흑백, - drop-shadow(...) 모양을 따라가는 그림자.\n"
            "backdrop-filter 는 '요소 뒤(배경)'를 흐리게 한다. 반투명 패널 뒤를 블러 처리하는\n"
            "'유리 느낌(글래스모피즘)' UI 에 쓰며, 보통 반투명 배경색과 함께 쓴다.\n"
            "filter 가 요소(와 내용)에 효과를 준다면, backdrop-filter 는 그 요소가 덮고 있는 뒷부분에 효과를 준다.\n"
            "아래를 적용하면 흑백이던 썸네일이 호버 시 컬러로 또렷해지고,\n"
            "반투명 헤더 뒤 내용이 흐릿하게 비치는 유리 느낌 화면이 된다."
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
            "clip-path 는 요소를 정해진 도형 모양으로 '오려서' 보여준다. 도형 밖은 잘려 안 보인다.\n"
            "- circle(50%) 원형, - ellipse(타원), - inset(안쪽 사각 잘라내기, 둥근 모서리도 가능),\n"
            "- polygon(x y, x y, ...) 점들을 이어 만든 다각형(삼각형·평행사변형·말풍선 등).\n"
            "좌표는 보통 % 로 적으며, 왼쪽 위가 0% 0%, 오른쪽 아래가 100% 100% 다.\n"
            "transition 과 함께 쓰면 모양이 부드럽게 변하는 효과도 만들 수 있다.\n"
            "(글자가 도형 주위로 흐르게 하려면 shape-outside 를 float 요소에 함께 쓴다.)\n"
            "아래를 적용하면 정사각 이미지가 원형 아바타로 보이고, 배너 아래쪽이 비스듬히 잘린 화면이 된다."
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
