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
            "[개요]\n"
            "CSS는 웹 페이지의 시각적 표현을 정의하는 언어이다. 스타일을 적용하려면 먼저 대상 요소를 지정해야 하며, "
            "이 지정 방법을 선택자(Selector)라고 한다.\n\n"
            "[기본 문법]\n"
            "CSS 규칙의 기본 구조는 다음과 같다.\n"
            "  선택자 { 속성: 값; }\n"
            "  → 지정한 대상에 대해 특정 속성 값을 설정하라는 의미이다.\n"
            "  예: p { color: red; } 는 모든 문단 글자를 빨간색으로 설정한다.\n\n"
            "[선택자 종류]\n"
            "  • p { }        → 태그 선택자. <p> 태그(문단) 전체를 선택한다. 태그 이름을 그대로 쓰면 해당 종류 전체가 선택된다.\n"
            "  • .box { }     → class 선택자. 앞에 점(.)이 붙으며, class=\"box\"로 지정된 요소를 모두 선택한다. "
            "동일한 class를 여러 요소에 부여할 수 있다.\n"
            "  • #title { }   → id 선택자. 앞에 우물정(#)이 붙으며, id=\"title\"인 요소 하나만 선택한다. "
            "id는 한 페이지에 하나만 존재해야 한다.\n"
            "  • nav a { }    → 후손 선택자. 선택자를 공백으로 구분하며, <nav> 내부에 포함된 <a>만 선택하여 범위를 좁힌다.\n\n"
            "[class와 id의 구분 기준]\n"
            "  • 버튼처럼 반복되는 요소는 class로 묶어 일괄 적용하는 것이 효율적이다.\n"
            "  • 로고나 제목처럼 페이지에 하나뿐인 요소는 id로 지정하여 명확히 식별한다.\n\n"
            "[우선순위]\n"
            "동일한 요소에 여러 규칙이 겹칠 경우, 더 구체적으로 지정한 규칙이 적용된다.\n"
            "  • 우선순위: id(#) > class(.) > 태그 순서이다.\n\n"
            "[적용 결과]\n"
            "아래 예시를 적용하면 제목 글자는 파란색, 'box' 카드는 회색 배경으로 표시되며, "
            "메뉴(nav) 안의 링크는 밑줄이 제거된다.\n\n"
            "[유의 사항]\n"
            "  • 선택자 뒤 중괄호 { } 를 누락하거나 속성 끝에 세미콜론(;)을 붙이지 않으면 스타일이 적용되지 않는다.\n"
            "  • 점(.)은 class, 우물정(#)은 id를 의미하므로 혼동하지 않도록 한다."
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
            "[개요]\n"
            "화면에 표시되는 모든 요소(글자, 버튼, 이미지)는 사각형 상자 형태로 구성되며, 이를 박스 모델(Box Model)이라고 한다. "
            "CSS 박스는 안쪽부터 바깥으로 네 개의 영역으로 이루어진다.\n\n"
            "[네 영역 구조]\n"
            "  • content (내용)     → 실제 글자나 이미지가 들어가는 영역이다.\n"
            "  • padding (안쪽 여백) → 내용과 테두리 사이의 공간으로, 내용을 안쪽으로 밀어 여유를 준다.\n"
            "  • border (테두리)     → 상자를 둘러싼 선이며, 두께·색·모양을 지정할 수 있다.\n"
            "  • margin (바깥 여백)  → 해당 상자와 인접 상자 사이의 간격이다.\n\n"
            "[padding과 margin의 차이]\n"
            "  • padding은 상자 내부를 넓혀 글자가 테두리에 붙어 답답해 보이지 않게 한다.\n"
            "  • margin은 상자 외부를 띄워 인접 요소와의 간격을 확보한다.\n"
            "  • 둘 다 여백이지만 적용 위치가 안쪽과 바깥쪽으로 서로 다르다.\n\n"
            "[속성 분석]\n"
            "  • width: 200px;            → 내용 너비를 200픽셀로 지정한다.\n"
            "  • padding: 20px;           → 사방(위/아래/좌/우) 안쪽 여백을 각 20픽셀로 지정한다.\n"
            "  • border: 1px solid #ccc;  → 1픽셀 두께의 실선(solid), 회색(#ccc) 테두리를 지정한다.\n"
            "  • margin: 16px 0;          → 위아래 16픽셀, 좌우 0으로 지정한다. (값 두 개는 '위아래 / 좌우' 순서이다.)\n\n"
            "[box-sizing의 중요성]\n"
            "기본 설정에서 width는 내용만의 너비를 의미한다. 따라서 padding 20px, border 1px를 더하면 "
            "실제 상자 크기는 200 + 20 + 20 + 1 + 1 = 242픽셀로 커진다.\n"
            "box-sizing: border-box; 로 변경하면 width 200px 안에 padding과 border가 포함되어 "
            "겉 상자가 200픽셀로 유지된다. 계산이 단순해지므로 통상 초기에 이 설정을 적용한다.\n\n"
            "[적용 결과]\n"
            "아래를 적용하면 흰 카드 둘레에 회색 테두리가 표시되고, 내부 글자는 안쪽으로 20px 떨어지며, "
            "카드 간에는 위아래 16px 간격이 형성된다.\n\n"
            "[유의 사항]\n"
            "  • margin은 위아래 값이 서로 겹쳐 합쳐지는 '마진 상쇄' 현상이 있다. "
            "위 상자의 아래 margin 20px와 아래 상자의 위 margin 20px가 겹치면 40px가 아니라 20px만 적용된다.\n"
            "  • 간격이 예상보다 좁게 보인다면 이 마진 상쇄가 원인인 경우가 많다."
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
            "[개요]\n"
            "글자에 색을 입히고 크기, 굵기, 줄 간격을 조절하면 가독성과 시각적 완성도가 향상된다. "
            "본 레슨은 색, 단위, 글자 스타일 세 가지 도구를 다룬다.\n\n"
            "[색(color) 지정 방법]\n"
            "  • color: red;              → 색 이름을 직접 사용한다. 간단하지만 표현 가능한 색이 제한적이다.\n"
            "  • color: #3498db;          → 16진수 코드로, # 뒤 여섯 글자가 빨강/초록/파랑 값을 나타낸다.\n"
            "  • color: rgba(0,0,0,0.5);  → 빨강0·초록0·파랑0(검정)에 마지막 0.5는 투명도를 의미한다. "
            "0.5는 반투명, 1은 완전 불투명, 0은 완전 투명이다.\n\n"
            "[단위(크기 기준)]\n"
            "  • px   → 화면의 점 하나 크기로, 고정 단위이다. 16px는 항상 16점이다.\n"
            "  • %    → 부모(상위 상자) 크기를 기준으로 한 비율이다. 부모가 커지면 함께 커진다.\n"
            "  • em   → 현재 요소의 글자 크기를 1로 본 배수이다. 2em은 현재 글자의 두 배이다.\n"
            "  • rem  → 최상위(html) 글자 크기를 1로 본 배수이다. 기준이 한 곳이라 예측이 용이하다.\n"
            "  rem을 선호하는 이유는 html의 글자 크기 한 줄만 변경하면 rem으로 지정한 모든 크기가 일괄 조정되기 때문이다.\n\n"
            "[글자 스타일 속성]\n"
            "  • font-size: 1rem;      → 글자 크기. 1rem은 기준(통상 16px)과 동일한 크기이다.\n"
            "  • font-weight: bold;    → 글자 굵기. bold는 진하게, normal은 보통이다.\n"
            "  • line-height: 1.6;     → 줄 간격. 글자 높이의 1.6배로 설정한다.\n"
            "  • text-align: center;   → 글자 정렬. center(가운데), left(왼쪽), right(오른쪽)를 지정한다.\n\n"
            "[줄 간격의 역할]\n"
            "줄 간격이 좁으면 다음 줄을 찾기 어려워 가독성이 떨어진다. 1.5~1.7 정도로 설정하면 문단이 읽기 편해진다.\n\n"
            "[적용 결과]\n"
            "아래를 적용하면 본문 글자는 16px에 줄 간격 1.6으로 표시되고, 제목은 진한 파란색·굵게·가운데 정렬로 표시된다.\n\n"
            "[유의 사항]\n"
            "  • px만 사용하면 사용자가 브라우저에서 글씨를 확대해도 크기가 변하지 않아 접근성이 저하된다. "
            "글자 크기는 rem/em으로 지정하는 것이 바람직하다.\n"
            "  • 배경색과 글자색의 대비가 약하면 글씨가 잘 보이지 않으므로 옅은 회색 글씨는 주의한다."
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
            "[개요]\n"
            "여러 요소를 가로로 나란히 배치하거나 정중앙에 정렬하는 작업은 과거에는 까다로웠다. "
            "Flexbox는 이를 간단히 처리하는 정렬 도구이다. 부모 상자를 flex로 지정하면 그 안의 자식 요소가 자동으로 정렬된다. "
            "핵심은 부모에 명령을 지정하면 자식이 정렬된다는 점이다.\n\n"
            "[두 개의 축]\n"
            "  • 주축   → 요소들이 배열되는 기본 방향이다. 기본값은 가로(왼쪽→오른쪽)이다.\n"
            "  • 교차축 → 주축과 직각인 방향이다. 주축이 가로이면 교차축은 세로이다.\n"
            "  이 두 축을 기준으로 가로 정렬과 세로 정렬을 각각 조절한다.\n\n"
            "[속성 분석]\n"
            "  • display: flex;                    → 부모를 플렉스 상자로 변환한다. 모든 정렬의 시작이다.\n"
            "  • flex-direction: row;              → 자식을 가로로 배열한다. column으로 지정하면 세로로 쌓인다.\n"
            "  • justify-content: space-between;   → 주축(가로) 방향 정렬. space-between은 양끝으로 밀고 사이를 균등히 벌린다. "
            "center(가운데 모으기), flex-start(왼쪽 붙이기) 등도 있다.\n"
            "  • align-items: center;              → 교차축(세로) 방향 정렬. center는 높이 가운데에 맞춘다.\n"
            "  • gap: 16px;                        → 자식 간 간격을 16px로 지정한다.\n\n"
            "[자식 요소 속성]\n"
            "  • flex: 1;  → 남는 공간을 나눠 갖도록 지정한다. 자식 셋에 모두 적용하면 화면을 균등하게 3등분하는 가변 너비가 된다.\n\n"
            "[Flexbox 사용 이유]\n"
            "가운데 정렬은 초보자가 어려워하는 부분이나, flex에서는 justify-content: center;와 align-items: center; "
            "두 줄로 가로·세로 정중앙 정렬을 구현할 수 있다. 이것이 정중앙 정렬의 기본 방식이다.\n\n"
            "[적용 결과]\n"
            "아래를 적용하면 헤더 안에서 로고는 왼쪽, 메뉴는 오른쪽 끝으로 배치되고 세로로는 가운데에 정렬되며, "
            "카드 3개가 같은 간격으로 나란히 배치된다.\n\n"
            "[유의 사항]\n"
            "  • flex-wrap을 지정하지 않으면 자식들이 줄바꿈 없이 한 줄에 배치되어 좁은 화면에서 넘칠 수 있다. "
            "좁아질 때 아래로 접히게 하려면 flex-wrap: wrap; 을 지정한다.\n"
            "  • 행과 열을 동시에 격자로 다루는 복잡한 배치는 Flexbox보다 Grid가 적합하다."
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
            "[개요]\n"
            "기본적으로 요소는 위에서 아래로 순서대로 쌓이며, 이를 '문서 흐름'이라고 한다. "
            "position은 이 흐름에서 요소를 분리하여 원하는 위치에 배치하는, 즉 배치 기준을 변경하는 도구이다.\n\n"
            "[네 가지 값]\n"
            "  • position: static;    → 기본값이다. 별도 지정 없이 순서대로 배치된다.\n"
            "  • position: relative;  → 원래 자리를 기준으로 top/left만큼 이동한다. "
            "이동해도 원래 자리는 그대로 비워둔다.\n"
            "  • position: absolute;  → 문서 흐름에서 완전히 벗어나며, 가장 가까운 static이 아닌 조상 상자를 기준으로 배치된다.\n"
            "  • position: fixed;     → 화면(브라우저 창) 자체를 기준으로 고정된다. 스크롤해도 같은 자리에 유지된다.\n\n"
            "[대표 패턴]\n"
            "가장 흔한 조합은 부모에 position: relative;, 자식에 position: absolute;를 지정하는 것이다.\n"
            "  • 이 경우 자식은 부모 상자 안을 기준으로 top/right 위치에 배치된다.\n"
            "  • 카드 우상단 'NEW' 배지, 사진 위 글자 표시 등에 활용된다.\n"
            "  • absolute는 static이 아닌 가장 가까운 조상을 기준으로 삼으므로, 부모에 relative를 지정하면 "
            "그 부모가 기준점이 되어 자식이 부모 안에 안정적으로 배치된다.\n\n"
            "[속성 값 분석]\n"
            "  • top: 8px; right: 8px;       → 기준 상자의 위에서 8px, 오른쪽에서 8px 떨어진 위치(우상단 근처)에 배치한다.\n"
            "  • bottom: 20px; right: 20px;  → 화면 오른쪽 아래 구석에서 각 20px 떨어진 위치로, '맨 위로' 버튼 배치에 적합하다.\n\n"
            "[적용 결과]\n"
            "아래를 적용하면 카드 우상단에 'NEW' 빨간 배지가 겹쳐 표시되고, "
            "화면 오른쪽 아래에는 스크롤과 무관하게 고정되는 '맨 위로' 버튼이 생성된다.\n\n"
            "[유의 사항]\n"
            "  • absolute와 fixed는 흐름에서 벗어나 자리를 차지하지 않으므로 다른 요소와 겹칠 수 있다.\n"
            "  • 요소가 겹칠 때 표시 순서는 z-index 값으로 정하며, 값이 많아지면 관리가 복잡해진다.\n"
            "  • 과도하게 사용하면 화면 크기 변경 시 레이아웃이 쉽게 깨지므로 필요한 곳에만 사용한다."
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
            "[개요]\n"
            "고정된 모습뿐 아니라, 마우스를 올릴 때 버튼 색이 바뀌거나 입력칸 클릭 시 테두리가 강조되는 등 "
            "상태에 따른 표현이 필요하다. 특정 상황에서만 스타일을 적용하거나 HTML에 없던 가짜 요소를 생성하는 것이 "
            "본 레슨의 주제이다. 핵심은 자바스크립트 없이 CSS만으로 이러한 효과를 구현할 수 있다는 점이다.\n\n"
            "[가상클래스 — 콜론 하나(:) — 상태 기반 스타일]\n"
            "요소의 현재 상태나 위치가 조건에 맞을 때만 스타일이 적용된다.\n"
            "  • :hover              → 마우스 커서를 요소 위에 올린 상태일 때 적용된다.\n"
            "  • :focus              → 입력칸을 클릭하여 커서가 들어간(포커스된) 상태일 때 적용된다.\n"
            "  • :first-child        → 형제 중 첫 번째 요소일 때 적용된다. :last-child는 마지막 요소이다.\n"
            "  • :nth-child(2n)      → 2n번째, 즉 짝수 번째(2,4,6...) 요소마다 적용된다. 표 줄무늬 처리에 적합하다.\n\n"
            "[가상요소 — 콜론 둘(::) — 가짜 요소 생성]\n"
            "HTML에는 없지만 CSS로 새 조각을 생성하여 삽입하는 장식용 요소이다.\n"
            "  • ::before  → 요소 내용 앞에 새 조각을 삽입한다. content로 삽입할 글자/기호를 지정한다.\n"
            "  • ::after   → 요소 내용 뒤에 새 조각을 삽입한다.\n"
            "  • content: '*';  → 가짜 조각에 별표(*) 문자를 삽입한다. 가상요소는 content가 있어야 표시된다.\n\n"
            "[활용 목적]\n"
            "  • 필수 입력칸 라벨 앞에 빨간 '*'를 붙일 때 HTML을 개별 수정하는 대신 ::before로 CSS에서 일괄 처리할 수 있다. "
            "이로써 HTML은 깔끔하게 유지하고 장식은 CSS가 담당한다.\n"
            "  • 마우스 호버 효과도 JS 없이 :hover 한 줄로 구현할 수 있어 간단하다.\n\n"
            "[적용 결과]\n"
            "아래를 적용하면 버튼에 마우스를 올릴 때 파란색이 진해지고, 목록의 짝수 줄만 회색 배경으로 줄무늬가 형성되며, "
            "필수 입력 라벨 앞에 빨간 '*'가 자동으로 추가된다.\n\n"
            "[유의 사항]\n"
            "  • ::before/::after는 content 속성이 없으면 화면에 표시되지 않는다. 빈 content라도 content: '';로 지정해야 한다.\n"
            "  • 가상요소로 삽입한 글자는 스크린리더가 제대로 읽지 못할 수 있다. "
            "따라서 필수 안내 등 중요한 정보는 가상요소에만 의존하지 말고 실제 텍스트로도 제공해야 접근성이 확보된다."
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
            "[개요]\n"
            "Flexbox가 한 줄 정렬에 강점이 있다면, Grid는 표(격자) 배치에 강점이 있다. "
            "가로줄(행)과 세로줄(열)로 칸을 나누고 각 칸에 요소를 배치하는 방식이다. "
            "가로와 세로를 동시에 다루므로 갤러리, 대시보드, 페이지 전체 뼈대 같은 복잡한 배치에 적합하다.\n\n"
            "[단위 'fr']\n"
            "fr은 남는 공간을 나누는 비율 단위이다. 1fr 1fr 1fr이면 남은 공간을 1:1:1로 3등분하여 세 칸이 같은 너비가 된다.\n\n"
            "[속성 분석]\n"
            "  • display: grid;                          → 상자를 격자판으로 변환한다. Grid의 시작이다.\n"
            "  • grid-template-columns: 1fr 1fr 1fr;     → 열을 3개 만들고 너비를 균등하게 나눈다. (값 개수 = 열 개수)\n"
            "  • grid-template-columns: 200px 1fr;       → 첫 열은 200px 고정, 둘째 열은 나머지 전부이다. 사이드바+본문 배치에 사용한다.\n"
            "  • gap: 16px;                              → 칸 사이 간격을 16px로 지정한다.\n"
            "  • repeat(3, 1fr)                          → '1fr을 3번 반복'의 축약이며, 1fr 1fr 1fr과 동일하다.\n"
            "  • grid-column: span 2;                    → 해당 요소가 한 칸이 아닌 두 열을 차지하게 한다. 넓은 카드용이다.\n\n"
            "[핵심 표현: 반응형 자동 배치]\n"
            "  repeat(auto-fit, minmax(200px, 1fr))\n"
            "  → 칸은 최소 200px을 유지하되 화면 폭에 맞춰 열 개수를 자동으로 조절하라는 의미이다.\n"
            "     minmax(200px, 1fr)은 최소 200px, 최대는 남는 만큼이며, auto-fit은 들어갈 수 있는 만큼 자동으로 채우라는 뜻이다.\n"
            "     이로써 화면이 넓으면 4열, 좁으면 2열로 바뀌는 반응형 갤러리를 미디어 쿼리 없이 구현할 수 있다.\n\n"
            "[Flexbox와의 비교]\n"
            "  • 요소를 가로 또는 세로 한 방향으로만 배열할 때는 Flexbox가 간단하다.\n"
            "  • '가로 3칸 × 세로 여러 줄'처럼 표 형태로 정확히 맞춰야 할 때는 Grid가 적합하다.\n"
            "  • Flex는 한 줄 정렬, Grid는 격자 배치로 구분할 수 있다.\n\n"
            "[적용 결과]\n"
            "아래를 적용하면 카드들이 각각 200px 이상 너비를 유지하면서 화면 폭에 맞춰 "
            "자동으로 2열·3열·4열로 재배치되는 반응형 갤러리가 구성된다.\n\n"
            "[유의 사항]\n"
            "  • 단순한 한 줄 정렬(메뉴 나열 등)에 Grid를 사용하면 문법이 오히려 복잡하므로 Flexbox가 적합하다.\n"
            "  • grid-template 문법은 초기에 낯설 수 있으므로 fr과 repeat부터 순차적으로 익히는 것이 좋다."
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
            "[개요]\n"
            "사용자는 큰 모니터와 작은 스마트폰 등 다양한 크기의 화면으로 동일한 웹사이트를 이용한다. "
            "PC용으로 넓게 만든 화면을 폰에서 그대로 보면 글씨가 작아지고 메뉴가 넘친다. "
            "반응형은 화면 크기에 따라 레이아웃을 변경하는 기술이며, @media 쿼리가 핵심 도구로 "
            "특정 화면 크기 조건에서만 스타일을 적용하도록 한다.\n\n"
            "[조건 속성 분석]\n"
            "  • @media (max-width: 768px) { ... }  → 화면 폭이 768px 이하일 때만 중괄호 안 스타일을 적용한다. "
            "max(최대) 768은 768보다 작거나 같은 좁은 화면, 즉 폰/태블릿을 의미한다.\n"
            "  • @media (min-width: 1024px) { ... } → 화면 폭이 1024px 이상일 때만 적용한다. "
            "min(최소) 1024는 1024보다 크거나 같은 넓은 화면, 즉 데스크톱을 의미한다.\n"
            "  이 기준이 되는 폭 숫자를 중단점(breakpoint)이라고 한다.\n\n"
            "[모바일 퍼스트 방식]\n"
            "기본 스타일은 좁은 폰 화면 기준으로 먼저 작성하고, min-width로 넓어질 때의 변경 사항을 덧붙이는 방식이다. "
            "작은 화면부터 구성하고 큰 화면에 요소를 추가하는 방식으로, 실무에서 권장된다.\n\n"
            "[필수 설정]\n"
            "반응형이 정상 작동하려면 HTML의 <head> 안에 다음 한 줄이 반드시 있어야 한다.\n"
            "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
            "  • 이 설정이 없으면 폰이 화면을 강제로 축소하여, @media가 무시되는 것처럼 보인다.\n"
            "  • 폰 화면 폭을 실제 기기 폭으로 인식하도록 지정하는 필수 설정이다.\n\n"
            "[적용 결과]\n"
            "아래를 적용하면 넓은 화면에서는 메뉴가 가로로 펼쳐지고 본문이 2단으로 나뉘지만, "
            "768px 이하 좁은 화면에서는 메뉴와 본문이 세로 1단으로 쌓이고 글자 크기도 축소된다.\n\n"
            "[유의 사항]\n"
            "  • 중단점을 과도하게 만들면(예: 400, 600, 768, 900, 1200...) 관리가 복잡해지고 수정 지점을 파악하기 어려워진다.\n"
            "  • flex-wrap이나 grid의 auto-fit처럼 자동으로 접히는 기능을 먼저 활용하면 미디어 쿼리 개수를 줄일 수 있다. "
            "쿼리는 필요한 경우에만 최소한으로 사용하는 것이 바람직하다."
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
            "[개요]\n"
            "버튼 색이 즉시 바뀌면 어색하지만 0.3초에 걸쳐 서서히 바뀌면 자연스럽다. "
            "또한 로딩 중 아이콘이 회전하면 대기 상태를 시각적으로 전달할 수 있다. "
            "본 레슨은 화면에 움직임을 부여하는 두 도구, transition(부드러운 전환)과 @keyframes(반복 동작)를 다룬다.\n\n"
            "[transition — 부드러운 전환]\n"
            "속성 값이 변할 때 그 사이 과정을 부드럽게 채워준다.\n"
            "  transition: background 0.3s ease;\n"
            "    • background  → '배경색'이 변할 때만 부드럽게 처리하도록 대상을 지정한다.\n"
            "    • 0.3s        → 변화에 걸리는 시간으로 0.3초이다.\n"
            "    • ease        → 속도 곡선이다. ease는 '처음 느리게-중간 빠르게-끝 느리게'로 가장 자연스럽다.\n"
            "  transition은 단독으로는 작동하지 않으며, :hover 같은 값이 변하는 상황과 결합해야 효과가 나타난다.\n\n"
            "[@keyframes — 반복 동작의 시나리오]\n"
            "0%에서 100%까지 구간별로 각 시점의 모습을 미리 정의한 애니메이션 시나리오이다.\n"
            "  @keyframes spin { from { ... } to { ... } }\n"
            "    • from  → 시작(0%) 모습. to → 끝(100%) 모습.\n"
            "  animation: spin 1s linear infinite;\n"
            "    • spin      → 위에서 정의한 시나리오 이름이다.\n"
            "    • 1s        → 한 주기(시작→끝)에 걸리는 시간으로 1초이다.\n"
            "    • linear    → 일정한 속도이다. 회전은 속도 변화 없이 도는 것이 자연스럽다.\n"
            "    • infinite  → 무한 반복이다. 로딩이 끝날 때까지 계속 회전한다.\n\n"
            "[transform — 이동·확대·회전]\n"
            "  • transform: scale(1.05);    → 크기를 1.05배로 확대한다. (강조 효과)\n"
            "  • transform: rotate(360deg); → 360도 회전한다. (회전)\n"
            "  • transform: translate(...)  → 위치를 이동한다. (이동)\n"
            "  transform은 GPU가 처리하여 부드럽고 빠르게 동작한다.\n\n"
            "[적용 결과]\n"
            "아래를 적용하면 버튼에 마우스를 올릴 때 색이 부드럽게 진해지면서 약간 확대되고, "
            "로딩 아이콘(spinner)은 지속적으로 회전한다.\n\n"
            "[유의 사항]\n"
            "  • 움직임이 과도하거나 길면 오히려 산만하므로 짧고 은은하게 구성하는 것이 좋다.\n"
            "  • width나 top 같은 속성을 애니메이션하면 화면이 버벅일 수 있다. "
            "대신 transform(이동/확대/회전)과 opacity(투명도)를 사용하면 더 매끄러우며, 성능을 위해 이 둘을 우선 사용한다."
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
