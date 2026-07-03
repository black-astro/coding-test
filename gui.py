"""code T — 코딩테스트 풀이 GUI (PySide6 · VSCode Dracula).

실행:  python gui.py

- PySide6(Qt) + QSS 로 VSCode Dracula 테마를 재현
- 라운드 버튼 · 커스텀 라운드 스크롤바 · 드래그 가능한 스플리터
- 코드 에디터: 라인넘버 + 구문 강조(QSyntaxHighlighter) + 자동 들여쓰기
- ▶ 채점(F5) → 케이스별 시간/메모리 + 정답/오답, 통과 시 🎉 성공
"""

import os
import sys
import re
import html
import time
import random
import shutil
import dataclasses
from pathlib import Path

from PySide6.QtCore import (Qt, QRect, QSize, QRegularExpression, Signal, QThread, QTimer,
                            QObject, QEvent)
from PySide6.QtGui import (QColor, QFont, QPainter, QTextCharFormat, QTextCursor,
                           QSyntaxHighlighter, QTextFormat, QTextOption, QAction,
                           QKeySequence, QShortcut, QIcon, QPixmap, QCursor, QPalette)
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QFrame, QLabel,
                               QPushButton, QButtonGroup, QHBoxLayout, QVBoxLayout,
                               QSplitter, QTreeWidget, QTreeWidgetItem, QTextBrowser,
                               QTextEdit, QPlainTextEdit, QSizePolicy, QMenu, QMessageBox,
                               QDialog, QProgressBar, QCheckBox, QComboBox,
                               QStackedWidget, QScrollArea, QSystemTrayIcon, QSlider,
                               QStyle, QStyleOptionSlider, QLineEdit,
                               QStyledItemDelegate, QStyleOptionViewItem, QGraphicsBlurEffect,
                               QTabWidget)

APP_VERSION = "1.1.11"

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))


def resource(*parts) -> Path:
    """리소스 경로. PyInstaller 빌드 시엔 _MEIPASS 에서 찾는다."""
    base = Path(getattr(sys, "_MEIPASS", ROOT))
    return base.joinpath(*parts)


ICON_ICO = resource("img", "app.ico")     # 멀티사이즈(작업표시줄/프로그램 아이콘)
ICON_PNG = resource("img", "logo_clean.png")


def apply_caption_color(widget):
    """위젯(다이얼로그 등) 네이티브 타이틀바를 메인 헤더색(CAPTION_COLOR)으로 동기화."""
    if sys.platform != "win32":
        return
    try:
        import ctypes
        hwnd = int(widget.winId())
        dwm = ctypes.windll.dwmapi
        one = ctypes.c_int(1)
        if dwm.DwmSetWindowAttribute(hwnd, 20, ctypes.byref(one), 4) != 0:
            dwm.DwmSetWindowAttribute(hwnd, 19, ctypes.byref(one), 4)

        def cref(hexc):
            hexc = hexc.lstrip("#")
            r, g, b = int(hexc[0:2], 16), int(hexc[2:4], 16), int(hexc[4:6], 16)
            return ctypes.c_int((b << 16) | (g << 8) | r)

        dwm.DwmSetWindowAttribute(hwnd, 35, ctypes.byref(cref(CAPTION_COLOR)), 4)  # 배경
        dwm.DwmSetWindowAttribute(hwnd, 36, ctypes.byref(cref(FG)), 4)             # 글자
        dwm.DwmSetWindowAttribute(hwnd, 34, ctypes.byref(cref(BG3)), 4)            # 테두리
    except Exception:
        pass


class _DialogCaptionFilter(QObject):
    """모든 QDialog 가 뜰 때 타이틀바 색을 메인 헤더색과 똑같이 맞춘다."""

    def eventFilter(self, obj, event):
        from PySide6.QtWidgets import QDialog as _QDialog
        if event.type() == QEvent.Show and isinstance(obj, _QDialog):
            QTimer.singleShot(0, lambda o=obj: apply_caption_color(o))
        return False


def app_icon():
    """프로그램/트레이 공용 아이콘. 멀티사이즈 .ico 우선, 없으면 png."""
    from PySide6.QtGui import QIcon
    for f in (ICON_ICO, ICON_PNG):
        if f.exists():
            ic = QIcon(str(f))
            if not ic.isNull():
                return ic
    return QIcon()

import problems
import practice
import lessons
import vocab
from vocab.progress import VocabDB
from engine.settings import SettingsDB
from engine.judge import judge as judge_problem, VERDICT_KR, effective_limits
from engine import runner, profile, topics, variants, exam
from engine.runner import compile_solution, run_process

try:
    import qtawesome as qta
except Exception:
    qta = None

# 빌드(PyInstaller) 시에는 실행 파일 옆에 쓰기 가능한 폴더를 사용
APP_DIR = Path(sys.executable).resolve().parent if getattr(sys, "frozen", False) else ROOT
SOLUTIONS_DIR = APP_DIR / "solutions"
PROGRESS_FILE = SOLUTIONS_DIR / "progress.json"

import json

# ───────────────────────── Dracula 팔레트 ─────────────────────────

BG      = "#282a36"
BG2     = "#21222c"
BG3     = "#191a21"
HILITE  = "#323443"
CUR     = "#44475a"
FG      = "#f8f8f2"
COMMENT = "#6272a4"
CYAN    = "#8be9fd"
GREEN   = "#50fa7b"
GREEN_D = "#3fb866"
ORANGE  = "#ffb86c"
PINK    = "#ff79c6"
PURPLE  = "#bd93f9"
PURPLE_D = "#9d6fe0"
RED     = "#ff5555"
YELLOW  = "#f1fa8c"
BORDER  = "#34374a"   # 카드 테두리(은은하게)
GAP     = "#0e0f13"   # 가장 진한색 — 여백/헤더/스플리터
SIDE    = "#171922"   # 사이드바 — 카드보다 어두움(VSCode 스타일)
CARD    = "#262834"   # 카드(문제/콘솔) — 여백보다 밝아 또렷이 구분
TERM_BG = "#1d1f29"   # 터미널 카드 — 콘솔보다 살짝 더 진하게

CODE_FAMILY = "Cascadia Code"
MONO_FAMILY = "Consolas"

# 티어(5~1) 색상 — 1이 가장 높고 눈에 띄게(빨강), 5가 가장 낮음(회색).
# 초록(해결 표시)과 겹치지 않도록 4=연한 하늘색, 3=하늘색(4와 연결되는 파랑 계열).
TIER_COLOR = {5: "#8a93b3", 4: "#9bd6ff", 3: "#ffe46b", 2: "#ff9e42", 1: "#ff5555"}

# ─────────────────────────────────────────────────────────────────
#  테마 커스터마이즈 — 여기 값만 바꾸면 프로그램 헤더 색이 바뀐다.
# ─────────────────────────────────────────────────────────────────
HEADER_BG    = "#262834"  # 헤더 색(=카드색). 여기 값만 바꾸면 헤더/네이티브 타이틀바 색이 바뀐다.
DIALOG_BG    = "#2c2f3e"  # 다이얼로그 배경 — 헤더와 같은 계열로 동기화(살짝 밝게)
HEADER_FG    = FG       # 헤더 글자색(브랜드 'code')
BADGE_BG     = PINK     # 'T' 뱃지 배경색
CAPTION_COLOR = HEADER_BG  # Windows 네이티브 타이틀바 색 (Win11 22000+ 에서 정확히 적용)

# 위장(stealth): 랭크를 이니셜로, 채점 결과를 테스트 러너 용어로 표시
RANK_INITIAL = {"Bronze": "B", "Silver": "S", "Gold": "G", "Platinum": "P"}
VERDICT_TXT = {"AC": "PASS", "WA": "FAIL", "TLE": "TIMEOUT",
               "MLE": "MEM", "RE": "ERROR", "CE": "BUILD ERR"}


# ───────────────────────── 전역 스타일시트 ─────────────────────────

QSS = f"""
* {{ font-family: 'Segoe UI'; color: {FG}; }}
QMainWindow, QWidget {{ background: {GAP}; }}
QLabel {{ background: transparent; }}   /* 타이틀/라벨은 뒤 카드색이 그대로 비치도록 */
QSplitter {{ background: {GAP}; }}
#TitleBar {{ background: {HEADER_BG}; }}
#Panel {{ background: {TERM_BG}; border-radius: 9px; }}
#PanelBG {{ background: {CARD}; border-radius: 9px; }}
#Side {{ background: {SIDE}; border-radius: 9px; }}
#Body {{ background: {GAP}; }}
#Rank {{ color:{FG}; font-size:13px; font-weight:bold; }}
QProgressBar#RankBar {{ background:{CUR}; border:none; border-radius:5px; }}
QProgressBar#RankBar::chunk {{ background:{PURPLE}; border-radius:5px; }}
#Brand {{ font-family:'{CODE_FAMILY}'; font-size:13px; font-weight:bold; color:{HEADER_FG}; }}
#Badge {{ background:{BADGE_BG}; color:{BG3}; font-family:'{CODE_FAMILY}';
          font-size:11px; font-weight:bold; border-radius:5px; padding:0px 5px; }}
#PanelTitle {{ color:{COMMENT}; font-size:10px; font-weight:bold; letter-spacing:1px; }}
#FileLabel {{ color:{COMMENT}; font-family:'{MONO_FAMILY}'; font-size:12px; }}
#Status {{ font-size:12px; font-weight:bold; }}

QPushButton {{
    background:{CUR}; color:{FG}; border:none; border-radius:6px;
    padding:5px 10px; font-size:11px; font-weight:bold;
}}
QPushButton:hover {{ background:{COMMENT}; }}
QPushButton:pressed {{ background:{PURPLE}; color:{BG3}; }}
QPushButton:disabled {{ background:{BG2}; color:{COMMENT}; }}
QPushButton#Run {{ background:{PURPLE}; color:{BG3}; }}
QPushButton#Run:hover {{ background:{PURPLE_D}; }}
QPushButton#Ghost {{ background:{BG2}; }}
QPushButton#Ghost:hover {{ background:{CUR}; }}
QPushButton#ManageBtn {{ background:{BG2}; color:{FG}; border:1px solid {CUR};
    border-radius:6px; padding:8px 12px; text-align:left; }}
QPushButton#ManageBtn:hover {{ background:{CUR}; border-color:{PURPLE}; color:{CYAN}; }}
QPushButton#ManageBtn:pressed {{ background:{PURPLE}; color:{BG3}; }}

QPushButton#Seg {{ background:{BG2}; border-radius:0; padding:4px 11px; font-size:11px; }}
QPushButton#Seg:hover {{ background:{CUR}; }}
QPushButton#Seg:checked {{ background:{PURPLE}; color:{BG3}; }}
QPushButton#SegL {{ border-top-left-radius:8px; border-bottom-left-radius:8px; }}
QPushButton#SegR {{ border-top-right-radius:8px; border-bottom-right-radius:8px; }}

QComboBox {{ background:{BG2}; color:{FG}; border:1px solid {BORDER}; border-radius:5px; padding:3px 8px; font-size:11px; }}
QComboBox:hover {{ border-color:{CUR}; }}
QComboBox::drop-down {{ border:none; width:18px; }}
QComboBox QAbstractItemView {{ background:{BG2}; color:{FG}; border:1px solid {CUR};
    selection-background-color:{CUR}; selection-color:{CYAN}; outline:0; }}
QTreeWidget {{ background:{SIDE}; border:none; outline:0; font-size:11px; }}
QTreeWidget::item {{ padding:3px 2px; }}
QTreeWidget::item:selected {{ background:{CUR}; color:{CYAN}; }}
QTreeWidget::item:hover {{ background:{HILITE}; }}
QTreeView::branch {{ background:transparent; }}

QTextBrowser, QTextEdit, QPlainTextEdit {{
    background:{CARD}; border:none; selection-background-color:{CUR};
    selection-color:{FG};
}}
#Output {{ background:{TERM_BG}; }}
#ProblemView, #ProblemBody {{ background:{CARD}; border:none; }}
#CodeBox {{ background:{CARD}; border:1px solid {BORDER}; border-radius:6px; }}
#DrillCard {{ background:{CARD}; border:1px solid {BORDER}; border-radius:10px; }}
#OpacityBar {{ background:{BG2}; border:1px solid {BORDER}; border-radius:8px; }}
#OpacityBar QLabel {{ background:transparent; }}
QSlider#OpacitySlider {{ background:transparent; }}
QSlider#OpacitySlider::groove:horizontal {{ height:4px; background:{CUR}; border-radius:2px; }}
QSlider#OpacitySlider::add-page:horizontal {{ background:{CUR}; border-radius:2px; }}
QSlider#OpacitySlider::sub-page:horizontal {{ background:{PURPLE}; border-radius:2px; }}
QSlider#OpacitySlider::handle:horizontal {{ width:12px; height:12px; margin:-5px 0; background:{PURPLE}; border-radius:6px; }}
QSlider#OpacitySlider::handle:horizontal:hover {{ background:{PURPLE_D}; }}

QScrollBar:vertical {{ background:transparent; width:11px; margin:4px 2px 4px 0; }}
QScrollBar::handle:vertical {{ background:{CUR}; border-radius:5px; min-height:36px; }}
QScrollBar::handle:vertical:hover {{ background:{COMMENT}; }}
QScrollBar::handle:vertical:pressed {{ background:{PURPLE}; }}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{ height:0; }}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{ background:transparent; }}
QScrollBar:horizontal {{ background:transparent; height:11px; margin:0 4px 2px 4px; }}
QScrollBar::handle:horizontal {{ background:{CUR}; border-radius:5px; min-width:36px; }}
QScrollBar::handle:horizontal:hover {{ background:{COMMENT}; }}
QScrollBar::handle:horizontal:pressed {{ background:{PURPLE}; }}
QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{ width:0; }}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {{ background:transparent; }}

/* 콘솔/터미널 사이 드래그 핸들 — 눈에 띄게(가운데 그립) */
QSplitter::handle {{ background:{GAP}; }}
QSplitter::handle:horizontal {{ width:7px; }}
QSplitter::handle:vertical {{ height:7px; }}
QSplitter::handle:hover {{ background:{CUR}; }}
QSplitter::handle:pressed {{ background:{PURPLE}; }}
QToolTip {{ background:{BG3}; color:{FG}; border:1px solid {CUR}; }}

QMenu {{ background:{BG2}; color:{FG}; border:1px solid {CUR}; padding:4px; }}
QMenu::item {{ padding:6px 22px; border-radius:5px; }}
QMenu::item:selected {{ background:{CUR}; color:{CYAN}; }}
QMenu::separator {{ height:1px; background:{CUR}; margin:4px 8px; }}

/* 다이얼로그/메시지 — 프로그램 헤더 색과 동기화(헤더보다 살짝 밝게 '연하게') */
QDialog {{ background:{DIALOG_BG}; }}
QTabWidget::pane {{ border:1px solid {BORDER}; border-radius:6px; background:transparent; top:-1px; }}
QTabBar {{ background:transparent; }}
QTabBar::tab {{ background:{BG2}; color:{COMMENT}; padding:7px 16px; border:1px solid {BORDER};
    border-bottom:none; border-top-left-radius:6px; border-top-right-radius:6px; margin-right:2px; }}
QTabBar::tab:selected {{ background:{DIALOG_BG}; color:{CYAN}; }}
QTabBar::tab:hover {{ color:{FG}; }}
QMessageBox {{ background:{DIALOG_BG}; }}
QMessageBox QLabel {{ background:transparent; color:{FG}; }}
"""


# ───────────────────────── 구문 강조 ─────────────────────────

KEYWORDS = {
    "python": """def class return if elif else for while import from as in is not and or pass
        break continue with try except finally lambda yield global nonlocal del raise assert async await""".split(),
    "java": """public private protected class static void int long double float boolean char byte short
        String new return if else for while do switch case default break continue import package final this
        super try catch finally throw throws extends implements interface abstract enum instanceof""".split(),
    "cpp": """include using namespace int long double float char bool short unsigned signed void return if else
        for while do switch case default break continue new delete class struct public private protected const auto
        template typename static virtual override this sizeof""".split(),
}
LITERALS = {"python": "None True False".split(), "java": "null true false".split(), "cpp": "true false nullptr".split()}
PY_BUILTINS = """print len range int str list dict set tuple map filter sorted reversed input sum max min abs
    enumerate zip float bool any all round divmod pow ord chr isinstance type open format""".split()


def _fmt(color, bold=False, italic=False):
    f = QTextCharFormat()
    f.setForeground(QColor(color))
    if bold:
        f.setFontWeight(QFont.Bold)
    if italic:
        f.setFontItalic(True)
    return f


class Highlighter(QSyntaxHighlighter):
    def __init__(self, document, lang="python"):
        super().__init__(document)
        self.lang = lang
        self._build()

    def set_language(self, lang):
        self.lang = lang
        self._build()
        self.rehighlight()

    def _build(self):
        self.rules = []
        kw = KEYWORDS.get(self.lang, [])
        lits = LITERALS.get(self.lang, [])
        if kw:
            self.rules.append((QRegularExpression(r"\b(" + "|".join(kw) + r")\b"), _fmt(PINK, bold=True)))
        if lits:
            self.rules.append((QRegularExpression(r"\b(" + "|".join(lits) + r")\b"), _fmt(PURPLE)))
        if self.lang == "python":
            self.rules.append((QRegularExpression(r"\b(" + "|".join(PY_BUILTINS) + r")\b"), _fmt(CYAN)))
        self.rules.append((QRegularExpression(r"\b\d+\.?\d*\b"), _fmt(PURPLE)))
        self.rules.append((QRegularExpression(r'"([^"\\]|\\.)*"'), _fmt(YELLOW)))
        self.rules.append((QRegularExpression(r"'([^'\\]|\\.)*'"), _fmt(YELLOW)))
        # 주석은 마지막(우선 적용)
        com = r"#[^\n]*" if self.lang == "python" else r"//[^\n]*"
        self.com_rule = (QRegularExpression(com), _fmt(COMMENT, italic=True))

    def highlightBlock(self, text):
        for rx, fmt in self.rules:
            it = rx.globalMatch(text)
            while it.hasNext():
                m = it.next()
                self.setFormat(m.capturedStart(), m.capturedLength(), fmt)
        rx, fmt = self.com_rule
        it = rx.globalMatch(text)
        while it.hasNext():
            m = it.next()
            self.setFormat(m.capturedStart(), m.capturedLength(), fmt)


# ───────────────────────── 라인넘버 코드 에디터 ─────────────────────────

class LineNumberArea(QWidget):
    def __init__(self, editor):
        super().__init__(editor)
        self.editor = editor

    def sizeHint(self):
        return QSize(self.editor.line_number_width(), 0)

    def paintEvent(self, event):
        self.editor.paint_line_numbers(event)


class CodeEditor(QPlainTextEdit):
    def __init__(self):
        super().__init__()
        font = QFont(CODE_FAMILY, 10)
        font.setStyleHint(QFont.Monospace)
        self.setFont(font)
        self.setTabStopDistance(4 * self.fontMetrics().horizontalAdvance(" "))
        self.setWordWrapMode(QTextOption.NoWrap)
        self.lna = LineNumberArea(self)
        self.highlighter = Highlighter(self.document(), "python")
        self.run_callback = None

        self.blockCountChanged.connect(lambda _: self._update_margins())
        self.updateRequest.connect(self._update_lna)
        self.cursorPositionChanged.connect(self._highlight_current_line)
        self._update_margins()
        self._highlight_current_line()

    def line_number_width(self):
        digits = max(2, len(str(self.blockCount())))
        return 22 + self.fontMetrics().horizontalAdvance("9") * digits

    def _update_margins(self):
        self.setViewportMargins(self.line_number_width(), 0, 0, 0)

    def _update_lna(self, rect, dy):
        if dy:
            self.lna.scroll(0, dy)
        else:
            self.lna.update(0, rect.y(), self.lna.width(), rect.height())
        if rect.contains(self.viewport().rect()):
            self._update_margins()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        cr = self.contentsRect()
        self.lna.setGeometry(QRect(cr.left(), cr.top(), self.line_number_width(), cr.height()))

    def paint_line_numbers(self, event):
        painter = QPainter(self.lna)
        painter.fillRect(event.rect(), QColor(CARD))
        block = self.firstVisibleBlock()
        num = block.blockNumber()
        top = self.blockBoundingGeometry(block).translated(self.contentOffset()).top()
        bottom = top + self.blockBoundingRect(block).height()
        cur_line = self.textCursor().blockNumber()
        h = self.fontMetrics().height()
        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                painter.setPen(QColor(FG if num == cur_line else COMMENT))
                painter.drawText(0, int(top), self.lna.width() - 10, h,
                                 Qt.AlignRight | Qt.AlignVCenter, str(num + 1))
            block = block.next()
            top = bottom
            bottom = top + self.blockBoundingRect(block).height()
            num += 1

    def _highlight_current_line(self):
        sel = QTextEdit.ExtraSelection()
        sel.format.setBackground(QColor(HILITE))
        sel.format.setProperty(QTextFormat.FullWidthSelection, True)
        sel.cursor = self.textCursor()
        sel.cursor.clearSelection()
        self.setExtraSelections([sel])
        self.lna.update()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Tab:
            self.insertPlainText("    ")
            return
        if e.key() in (Qt.Key_Return, Qt.Key_Enter):
            line = self.textCursor().block().text()
            indent = len(line) - len(line.lstrip(" "))
            extra = "    " if line.rstrip().endswith((":", "{")) else ""
            super().keyPressEvent(e)
            self.insertPlainText(" " * indent + extra)
            return
        super().keyPressEvent(e)

    def set_language(self, lang):
        self.highlighter.set_language(lang)

    def set_code(self, code, lang):
        self.set_language(lang)
        self.setPlainText(code)

    def contextMenuEvent(self, event):
        menu = self.createStandardContextMenu()
        menu.addSeparator()
        act = menu.addAction("▶ 실행 (F5)")
        act.triggered.connect(lambda: self.run_callback() if self.run_callback else None)
        menu.exec(event.globalPos())


# ───────────────────────── 네이티브 문제 뷰 ─────────────────────────

def make_label(text, color=FG, size=13, bold=False, wrap=True):
    """문제 화면용 텍스트 라벨 (HTML 아님 · 순수 QLabel)."""
    w = QLabel(str(text))
    w.setWordWrap(wrap)
    w.setTextInteractionFlags(Qt.TextSelectableByMouse)
    weight = "bold" if bold else "normal"
    w.setStyleSheet(f"color:{color}; font-family:'Segoe UI'; font-size:{size}px;"
                    f" font-weight:{weight}; background:transparent;")
    return w


def make_codebox(text):
    """예제/코드 블록 — 배경은 카드색과 동일, 테두리로만 구분."""
    box = QFrame()
    box.setObjectName("CodeBox")
    lay = QVBoxLayout(box)
    lay.setContentsMargins(10, 7, 10, 7)
    lab = QLabel(str(text).rstrip())
    lab.setFont(QFont(MONO_FAMILY, 11))
    lab.setStyleSheet(f"color:{YELLOW}; background:transparent;")
    lab.setTextInteractionFlags(Qt.TextSelectableByMouse)
    lay.addWidget(lab)
    return box


# 품사(pos) 약어 → 한국어. 초보자가 'n/v/adj' 같은 약어를 모르므로 한글로 보여준다.
POS_KR = {
    "n": "명사", "v": "동사", "adj": "형용사", "adv": "부사", "pron": "대명사",
    "prep": "전치사", "conj": "접속사", "int": "감탄사", "interj": "감탄사",
    "art": "관사", "det": "한정사", "num": "수사", "aux": "조동사", "kw": "키워드",
    "idiom": "관용어", "phrase": "표현", "phrasal v": "구동사",
}


def pos_kr(pos):
    """'pron' → '대명사', 'v/n' → '동사·명사'. 이미 한국어면 그대로 둔다."""
    if not pos:
        return ""
    return " · ".join(POS_KR.get(x.strip(), x.strip()) for x in str(pos).split("/"))


def weighted_pick(words, n, db=None):
    """n개 추출 — db 가 있으면 틀린 적 많고 덜 외운 단어를 우선 뽑는다(가중치 무작위)."""
    pool = list(words)
    n = min(n, len(pool))
    if db is None or n == len(pool):
        return random.sample(pool, n)
    try:
        wm = db.weight_map()
    except Exception:
        return random.sample(pool, n)
    weights = [max(0.1, wm.get(w.word, 1.0)) for w in pool]
    picked = []
    for _ in range(n):
        total = sum(weights)
        r = random.random() * total
        acc = 0.0
        for i, wt in enumerate(weights):
            acc += wt
            if r <= acc or i == len(pool) - 1:
                picked.append(pool.pop(i))
                weights.pop(i)
                break
    return picked


def drill_sample(words, cap=30, db=None):
    """학습 문항 추출 — 50개 이하면 전부(셔플), 초과(전체 레벨 등)면 cap 개.
    db 를 주면 오답이 많은 단어가 우선 출제된다."""
    pool = list(words)
    if len(pool) <= 50:
        random.shuffle(pool)
        return pool
    return weighted_pick(pool, cap, db)


# 트리 아이템 커스텀 데이터 롤
ROLE_TIER = Qt.UserRole + 2      # 티어 번호(1~5) 또는 None
ROLE_SOLVED = Qt.UserRole + 3    # 해결 여부
ROLE_LOCKED = Qt.UserRole + 4    # 상위 랭크 잠김 여부
ROLE_TIERCODE = Qt.UserRole + 5  # 티어 코드(랭크+티어, 예: "G3")


class TierDelegate(QStyledItemDelegate):
    """문제 항목: 앞의 'T{n}'만 티어 색으로, 타이틀은 기본색, 해결 시 우측에 작은 초록 체크."""

    def paint(self, painter, option, index):
        tnum = index.data(ROLE_TIER)
        if not tnum:
            super().paint(painter, option, index)
            return
        opt = QStyleOptionViewItem(option)
        self.initStyleOption(opt, index)
        opt.text = ""                                   # 텍스트는 직접 그림
        style = opt.widget.style() if opt.widget else QApplication.style()
        style.drawControl(QStyle.CE_ItemViewItem, opt, painter, opt.widget)   # 배경 + 아이콘

        r = style.subElementRect(QStyle.SE_ItemViewItemText, opt, opt.widget)
        painter.save()
        painter.setFont(opt.font)
        fm = painter.fontMetrics()
        selected = bool(opt.state & QStyle.State_Selected)

        locked = bool(index.data(ROLE_LOCKED))
        tag = index.data(ROLE_TIERCODE) or f"T{tnum}"   # 랭크+티어 (예: G3)
        tag_w = fm.horizontalAdvance(tag)
        tcol = QColor(TIER_COLOR.get(tnum, FG))
        if locked:
            tcol.setAlpha(110)
        painter.setPen(tcol)
        painter.drawText(QRect(r.left(), r.top(), tag_w + 4, r.height()),
                         Qt.AlignVCenter | Qt.AlignLeft, tag)

        x = r.left() + tag_w + 8
        lock_w = 16 if locked else 0
        avail = max(0, r.right() - x - lock_w - 2)
        title = index.data(Qt.DisplayRole) or ""
        painter.setPen(QColor(COMMENT if locked else (CYAN if selected else FG)))
        painter.drawText(QRect(x, r.top(), avail, r.height()),
                         Qt.AlignVCenter | Qt.AlignLeft,
                         fm.elidedText(str(title), Qt.ElideRight, avail))
        if locked:
            painter.setPen(QColor(COMMENT))
            painter.drawText(QRect(r.right() - lock_w, r.top(), lock_w, r.height()),
                             Qt.AlignVCenter | Qt.AlignRight, "🔒")
        painter.restore()


class ClickSlider(QSlider):
    """그루브 아무 곳이나 클릭하면 그 위치 값으로 즉시 이동.
    (기본 QSlider 는 그루브 클릭 시 페이지 스텝만큼만 이동해 클릭 위치와 어긋남)"""

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton and self.maximum() > self.minimum():
            opt = QStyleOptionSlider()
            self.initStyleOption(opt)
            groove = self.style().subControlRect(QStyle.CC_Slider, opt, QStyle.SC_SliderGroove, self)
            handle = self.style().subControlRect(QStyle.CC_Slider, opt, QStyle.SC_SliderHandle, self)
            if self.orientation() == Qt.Horizontal:
                span = groove.width() - handle.width()
                pos = int(e.position().x()) - groove.x() - handle.width() // 2
                val = QStyle.sliderValueFromPosition(self.minimum(), self.maximum(), pos, span)
            else:
                span = groove.height() - handle.height()
                pos = int(e.position().y()) - groove.y() - handle.height() // 2
                val = QStyle.sliderValueFromPosition(self.minimum(), self.maximum(), pos, span, True)
            self.setValue(val)
        super().mousePressEvent(e)


class ProblemView(QScrollArea):
    """문제 화면을 QTextBrowser(HTML) 대신 네이티브 위젯으로 구성하는 스크롤 영역."""

    def __init__(self):
        super().__init__()
        self.setObjectName("ProblemView")
        self.setWidgetResizable(True)
        self.setFrameShape(QFrame.NoFrame)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        body = QWidget()
        body.setObjectName("ProblemBody")
        self.vbox = QVBoxLayout(body)
        self.vbox.setContentsMargins(2, 2, 8, 8)
        self.vbox.setSpacing(3)
        self.vbox.addStretch(1)            # 항상 맨 끝에 유지 → 위에서부터 쌓임
        self.setWidget(body)

    def clear(self):
        while self.vbox.count() > 1:        # 마지막 stretch 보존
            it = self.vbox.takeAt(0)
            w = it.widget()
            if w:
                w.setParent(None)
                w.deleteLater()

    def add(self, w, top=0):
        if top:
            self.vbox.insertSpacing(self.vbox.count() - 1, top)
        self.vbox.insertWidget(self.vbox.count() - 1, w)


# ───────────────────────── 채점 스레드 ─────────────────────────

class JudgeThread(QThread):
    done = Signal(object, object, object)   # problem, lang, result(or Exception)

    def __init__(self, p, lang, path):
        super().__init__()
        self.p, self.lang, self.path = p, lang, path

    def run(self):
        try:
            res = judge_problem(self.p, self.path, self.lang)
            self.done.emit(self.p, self.lang, res)
        except Exception as e:  # noqa
            self.done.emit(self.p, self.lang, e)


class RunThread(QThread):
    """채점 없이 그냥 실행(컴파일+실행). stdin 을 넣을 수 있고, cmd 를 직접 줄 수도 있다."""
    done = Signal(object)   # ("CE", msg) | ("OK", RunResult)

    def __init__(self, lang, path, stdin="", cmd=None):
        super().__init__()
        self.lang, self.path, self.stdin, self.cmd = lang, path, stdin, cmd

    def run(self):
        try:
            if self.cmd is not None:
                r = run_process(self.cmd, self.stdin, 10)
                self.done.emit(("OK", r))
                return
            comp = compile_solution(self.lang, self.path)
            if not comp.ok:
                self.done.emit(("CE", comp.error))
                return
            r = run_process(comp.run_cmd, self.stdin, 10, cwd=comp.workdir)
            self.done.emit(("OK", r))
        except Exception as e:  # noqa
            self.done.emit(("CE", str(e)))


# ───────────────────────── 영단어 퀴즈 ─────────────────────────

class QuizDialog(QDialog):
    def __init__(self, parent, words, pool, db):
        super().__init__(parent)
        self.setWindowTitle("영단어 퀴즈")
        self.resize(480, 360)
        self.words, self.pool, self.db = words, pool, db
        self.idx, self.score = 0, 0
        lay = QVBoxLayout(self)
        lay.setContentsMargins(18, 18, 18, 18)
        lay.setSpacing(10)
        self.prompt = QLabel("")
        self.prompt.setWordWrap(True)
        self.prompt.setAlignment(Qt.AlignCenter)
        self.prompt.setStyleSheet(f"color:{PURPLE}; font-size:22px; font-weight:bold; padding:8px;")
        lay.addWidget(self.prompt)
        self.btns = []
        for _ in range(4):
            b = QPushButton("")
            b.setObjectName("Ghost")
            b.clicked.connect(lambda _=False, bb=None: self._answer())
            lay.addWidget(b)
            self.btns.append(b)
        # 버튼별 핸들러(현재 텍스트로 판정)
        for b in self.btns:
            b.clicked.disconnect()
            b.clicked.connect(lambda _=False, bb=b: self._answer(bb.text()))
        self.info = QLabel("")
        self.info.setStyleSheet(f"color:{COMMENT};")
        lay.addWidget(self.info)
        self._show()

    def _show(self):
        if self.idx >= len(self.words):
            self._finish()
            return
        w = self.words[self.idx]
        self.prompt.setText(f"{self.idx + 1} / {len(self.words)}\n\n{w.word}"
                            + (f"   ({w.pos})" if w.pos else ""))
        opts = [w.meaning]
        others = [x.meaning for x in self.pool if x.meaning != w.meaning]
        random.shuffle(others)
        opts += others[:3]
        random.shuffle(opts)
        for i, b in enumerate(self.btns):
            if i < len(opts):
                b.setText(opts[i])
                b.setVisible(True)
                b.setEnabled(True)
            else:
                b.setVisible(False)
        self.info.setText(f"점수 {self.score}")

    def _answer(self, chosen=None):
        if chosen is None or self.idx >= len(self.words):
            return
        w = self.words[self.idx]
        ok = (chosen == w.meaning)
        if ok:
            self.score += 1
        self.db.record(w.word, ok)
        self.idx += 1
        self._show()

    def _finish(self):
        for b in self.btns:
            b.setVisible(False)
        n = len(self.words)
        self.prompt.setText(f"퀴즈 종료!\n\n{self.score} / {n} 정답")
        self.info.setText("창을 닫으세요.")


class TypingDrillWidget(QWidget):
    """단어 암기 — 단어/뜻을 몇 번 깜빡여 보여준 뒤, 뜻을 보고 영어 단어를 타이핑해 맞춘다.
    '그만하기'를 누르면 정답/오답 결과가 쭉 나온다. 다이얼로그/인라인 양쪽에서 재사용."""

    finished = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.db = None
        self.words = []
        self.idx = 0
        self.score = 0
        self.results = []          # (word, typed, ok)
        self._timer = None

        lay = QVBoxLayout(self)
        lay.setContentsMargins(20, 18, 20, 16)
        lay.setSpacing(10)

        self.progress = QLabel("")
        self.progress.setAlignment(Qt.AlignCenter)
        self.progress.setStyleSheet(f"color:{COMMENT}; font-size:12px;")
        lay.addWidget(self.progress)

        self.card = QFrame()
        self.card.setObjectName("DrillCard")
        cl = QVBoxLayout(self.card)
        cl.setContentsMargins(16, 20, 16, 20)
        cl.setSpacing(12)
        cl.addStretch(1)
        self.word_label = QLabel("")
        self.word_label.setAlignment(Qt.AlignCenter)
        self.word_label.setStyleSheet(f"color:{CYAN}; font-size:30px; font-weight:bold;")
        self.word_label.setFixedHeight(52)      # 상태 전환 시 카드가 출렁이지 않게 높이 고정
        self.meaning_label = QLabel("")
        self.meaning_label.setAlignment(Qt.AlignCenter)
        self.meaning_label.setWordWrap(True)
        self.meaning_label.setStyleSheet(f"color:{FG}; font-size:16px;")
        cl.addWidget(self.word_label)
        cl.addWidget(self.meaning_label)
        cl.addStretch(1)
        lay.addWidget(self.card, 1)

        self.feedback = QLabel("")
        self.feedback.setAlignment(Qt.AlignCenter)
        self.feedback.setStyleSheet(f"color:{COMMENT}; font-size:13px; font-weight:bold;")
        lay.addWidget(self.feedback)

        self.input = QLineEdit()
        self.input.setPlaceholderText("뜻을 보고 영어 단어를 입력 후 Enter")
        self.input.setStyleSheet(f"background:{BG2}; color:{FG}; border:1px solid {BORDER};"
                                 f" border-radius:6px; padding:8px; font-size:15px;")
        self.input.returnPressed.connect(self._submit)
        lay.addWidget(self.input)

        self.result_view = QTextBrowser()
        self.result_view.setVisible(False)
        self.result_view.setStyleSheet(f"background:{CARD}; border:none;")
        pal = self.result_view.palette()
        pal.setColor(QPalette.Base, QColor(CARD))
        self.result_view.setPalette(pal)
        lay.addWidget(self.result_view, 1)

        row = QHBoxLayout()
        self.skip_btn = QPushButton("건너뛰기")
        self.skip_btn.setObjectName("Ghost")
        self.skip_btn.clicked.connect(self._skip)
        self.stop_btn = QPushButton("그만하기 (결과 보기)")
        self.stop_btn.setObjectName("Run")
        self.stop_btn.clicked.connect(self._finish)
        self.quit_btn = QPushButton("종료")
        self.quit_btn.setObjectName("Ghost")
        self.quit_btn.clicked.connect(self._quit)
        self.close_btn = QPushButton("닫기")
        self.close_btn.setObjectName("Run")
        self.close_btn.clicked.connect(self._quit)
        self.close_btn.setVisible(False)
        row.addWidget(self.skip_btn)
        row.addStretch(1)
        row.addWidget(self.stop_btn)
        row.addWidget(self.quit_btn)
        row.addWidget(self.close_btn)
        lay.addLayout(row)
        # 우측 하단 투명도 바에 버튼이 가리지 않도록 아래 여백 확보
        lay.addSpacing(34)

    def _quit(self):
        self._stop_timer()
        self.finished.emit()

    def start(self, words, db):
        """단어 묶음으로 드릴 시작/재시작."""
        self.db = db
        self.words = drill_sample(words, db=db)   # 오답 많은 단어 우선
        self.idx = 0
        self.score = 0
        self.results = []
        self.card.setVisible(True)
        self.feedback.setVisible(True)
        self.result_view.setVisible(False)
        self.skip_btn.setVisible(True)
        self.stop_btn.setVisible(True)
        self.quit_btn.setVisible(True)
        self.close_btn.setVisible(False)
        self._next()

    def _stop_timer(self):
        if self._timer is not None:
            self._timer.stop()
            self._timer = None

    def _next(self):
        self._stop_timer()
        if self.idx >= len(self.words):
            self._finish()
            return
        w = self.words[self.idx]
        self.progress.setText(f"{self.idx + 1} / {len(self.words)}   ·   점수 {self.score}")
        self.feedback.setText("")
        self.input.clear()
        self.input.setEnabled(False)
        self.input.setVisible(False)
        self.word_label.setText(w.word)
        self.meaning_label.setText(w.meaning + (f"   [{pos_kr(w.pos)}]" if w.pos else ""))
        # 단어를 몇 번 깜빡여 보여준 뒤 타이핑 단계로
        self._blink_left = 6       # 3번 깜빡
        self._blink_on = True
        self._timer = QTimer(self)
        self._timer.timeout.connect(self._blink_tick)
        self._timer.start(260)

    def _blink_tick(self):
        self._blink_on = not self._blink_on
        col = CYAN if self._blink_on else "transparent"
        self.word_label.setStyleSheet(f"color:{col}; font-size:30px; font-weight:bold;")
        self._blink_left -= 1
        if self._blink_left <= 0:
            self._stop_timer()
            self.word_label.setStyleSheet(f"color:{COMMENT}; font-size:22px; font-weight:bold;")
            self.word_label.setText("✏  타이핑하세요")
            self.input.setVisible(True)
            self.input.setEnabled(True)
            self.input.setFocus()

    def _submit(self):
        if self.idx >= len(self.words) or not self.input.isEnabled():
            return
        typed = self.input.text().strip()
        if not typed:
            return
        w = self.words[self.idx]
        ok = typed.lower() == w.word.lower()
        if ok:
            self.score += 1
        self.db.record(w.word, ok)
        self.results.append((w, typed, ok))
        self.input.setEnabled(False)
        self.feedback.setStyleSheet(f"color:{GREEN if ok else RED}; font-size:14px; font-weight:bold;")
        self.feedback.setText("정답!" if ok else f"오답 — 정답: {w.word}")
        self.word_label.setStyleSheet(f"color:{GREEN if ok else RED}; font-size:30px; font-weight:bold;")
        self.word_label.setText(w.word)
        self.idx += 1
        QTimer.singleShot(950, self._next)

    def _skip(self):
        if self.idx >= len(self.words):
            return
        self._stop_timer()
        w = self.words[self.idx]
        self.db.record(w.word, False)
        self.results.append((w, "", False))
        self.idx += 1
        self._next()

    def _finish(self):
        self._stop_timer()
        self.card.setVisible(False)
        self.input.setVisible(False)
        self.feedback.setVisible(False)
        self.skip_btn.setVisible(False)
        self.stop_btn.setVisible(False)
        self.quit_btn.setVisible(False)
        self.close_btn.setVisible(True)
        n = len(self.results)
        correct = sum(1 for _, _, ok in self.results if ok)
        self.progress.setText("타이핑 암기 종료")
        h = [f"<div style='font-family:Segoe UI;color:{FG};font-size:13px;line-height:1.6;'>"]
        h.append(f"<div style='color:{PURPLE};font-size:18px;font-weight:bold;'>결과 — {correct} / {n} 정답</div><br>")
        if not self.results:
            h.append(f"<div style='color:{COMMENT};'>푼 단어가 없습니다.</div>")
        for w, typed, ok in self.results:
            mark = "✅" if ok else "❌"
            extra = "" if ok else f" <span style='color:{COMMENT};'>(입력: {html.escape(typed) if typed else '—'})</span>"
            h.append(f"<div style='margin:3px 0;'>{mark} <b style='color:{CYAN};'>{html.escape(w.word)}</b> "
                     f"<span style='color:{COMMENT};'>{html.escape(w.meaning)}</span>{extra}</div>")
        h.append("</div>")
        self.result_view.setHtml("".join(h))
        self.result_view.setVisible(True)


class SentenceDrillWidget(QWidget):
    """문장 완성 — 빈칸이 있는 예문을 주고 알맞은 단어를 타이핑.
    엔터로 채점(O/X), 정답이면 '다음'으로 넘어갈지 묻고, 오답이면 맞출 때까지 재시도."""

    finished = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.db = None
        self.items = []            # (word, prompt or None)
        self.idx = 0
        self.results = []          # (word, ok)
        self.solved_current = False

        lay = QVBoxLayout(self)
        lay.setContentsMargins(20, 18, 20, 16)
        lay.setSpacing(10)

        self.progress = QLabel("")
        self.progress.setAlignment(Qt.AlignCenter)
        self.progress.setStyleSheet(f"color:{COMMENT}; font-size:12px;")
        lay.addWidget(self.progress)

        self.card = QFrame()
        self.card.setObjectName("DrillCard")
        cl = QVBoxLayout(self.card)
        cl.setContentsMargins(18, 20, 18, 20)
        cl.setSpacing(12)
        cl.addStretch(1)
        self.mark = QLabel("")
        self.mark.setAlignment(Qt.AlignCenter)
        self.mark.setStyleSheet("font-size:40px; font-weight:bold;")
        # 한글 번역문 — 이걸 보고 빈칸에 들어갈 단어를 떠올린다
        self.translation = QLabel("")
        self.translation.setAlignment(Qt.AlignCenter)
        self.translation.setWordWrap(True)
        self.translation.setStyleSheet(f"color:{FG}; font-size:18px; font-weight:bold;")
        self.sentence = QLabel("")
        self.sentence.setAlignment(Qt.AlignCenter)
        self.sentence.setWordWrap(True)
        self.sentence.setStyleSheet(f"color:{CYAN}; font-size:15px;")
        self.hint = QLabel("")
        self.hint.setAlignment(Qt.AlignCenter)
        self.hint.setWordWrap(True)
        self.hint.setStyleSheet(f"color:{COMMENT}; font-size:13px;")
        # 힌트로 드러나는 단어 일부 — 약한 블러로 희미하게
        self.reveal = QLabel("")
        self.reveal.setAlignment(Qt.AlignCenter)
        self.reveal.setStyleSheet(f"color:{CYAN}; font-size:22px; font-weight:bold; letter-spacing:3px;")
        self._reveal_blur = QGraphicsBlurEffect(self)
        self._reveal_blur.setBlurRadius(2.2)
        self.reveal.setGraphicsEffect(self._reveal_blur)
        cl.addWidget(self.mark)
        cl.addWidget(self.translation)
        cl.addWidget(self.sentence)
        cl.addWidget(self.reveal)
        cl.addWidget(self.hint)
        cl.addStretch(1)
        lay.addWidget(self.card, 1)

        self.input = QLineEdit()
        self.input.setPlaceholderText("빈칸에 들어갈 영어 단어를 입력 후 Enter")
        self.input.setStyleSheet(f"background:{BG2}; color:{FG}; border:1px solid {BORDER};"
                                 f" border-radius:6px; padding:8px; font-size:15px;")
        self.input.returnPressed.connect(self._enter)
        lay.addWidget(self.input)

        self.result_view = QTextBrowser()
        self.result_view.setVisible(False)
        self.result_view.setStyleSheet(f"background:{CARD}; border:none;")
        pal = self.result_view.palette()
        pal.setColor(QPalette.Base, QColor(CARD))
        self.result_view.setPalette(pal)
        lay.addWidget(self.result_view, 1)

        row = QHBoxLayout()
        self.hint_btn = QPushButton("힌트")
        self.hint_btn.setObjectName("Ghost")
        self.hint_btn.clicked.connect(self._show_hint)
        self.skip_btn = QPushButton("건너뛰기")
        self.skip_btn.setObjectName("Ghost")
        self.skip_btn.clicked.connect(self._skip)
        self.next_btn = QPushButton("다음 ▶")
        self.next_btn.setObjectName("Run")
        self.next_btn.clicked.connect(self._go_next)
        self.next_btn.setVisible(False)
        self.quit_btn = QPushButton("종료")
        self.quit_btn.setObjectName("Ghost")
        self.quit_btn.clicked.connect(self._quit)
        self.close_btn = QPushButton("닫기")
        self.close_btn.setObjectName("Run")
        self.close_btn.clicked.connect(self._quit)
        self.close_btn.setVisible(False)
        row.addWidget(self.hint_btn)
        row.addWidget(self.skip_btn)
        row.addStretch(1)
        row.addWidget(self.next_btn)
        row.addWidget(self.quit_btn)
        row.addWidget(self.close_btn)
        lay.addLayout(row)
        lay.addSpacing(34)

    def _quit(self):
        self.finished.emit()

    def _show_hint(self):
        """단어 일부를 단계적으로(약 1/3씩) 드러낸다 — 약한 블러로 희미하게."""
        if self.solved_current or self.idx >= len(self.items):
            return
        word = self.items[self.idx][0].word
        self.hint_level = min(3, getattr(self, "hint_level", 0) + 1)
        k = max(1, round(len(word) * self.hint_level / 3))
        shown = word[:k]
        rest = "·" * (len(word) - k)
        pct = round(k / len(word) * 100)
        self.reveal.setText(shown + rest)
        self.hint_btn.setText(f"힌트 ({pct}%)")
        # 더 드러날수록 블러를 살짝 옅게
        self._reveal_blur.setBlurRadius(max(0.6, 2.6 - self.hint_level * 0.7))

    @staticmethod
    def _blank(word, example):
        if example:
            pat = re.compile(r"\b" + re.escape(word) + r"\b", re.IGNORECASE)
            if pat.search(example):
                return pat.sub("_____", example, count=1)
        return None

    def start(self, words, db):
        self.db = db
        self.items = [(w, self._blank(w.word, w.example))
                      for w in drill_sample(words, db=db)]
        self.idx = 0
        self.results = []
        self.card.setVisible(True)
        self.input.setVisible(True)
        self.result_view.setVisible(False)
        self.skip_btn.setVisible(True)
        self.hint_btn.setVisible(True)
        self.quit_btn.setVisible(True)
        self.next_btn.setVisible(False)
        self.close_btn.setVisible(False)
        self._next()

    def _next(self):
        if self.idx >= len(self.items):
            self._finish()
            return
        self.solved_current = False
        w, prompt = self.items[self.idx]
        self.progress.setText(f"{self.idx + 1} / {len(self.items)}")
        self.mark.setText("")
        if prompt:
            # 한글 번역(맥락)을 보고, 영어 빈칸 문장을 완성
            self.translation.setText(w.example_kr or "")
            self.sentence.setText(prompt)
            self.hint.setText("한글 뜻을 보고 빈칸에 들어갈 영어 단어를 입력하세요"
                              if w.example_kr else "빈칸에 들어갈 영어 단어를 입력하세요")
        else:
            self.translation.setText(f"“{w.meaning}”")
            self.sentence.setText("위 뜻에 해당하는 영어 단어를 입력하세요")
            self.hint.setText("")
        self.input.clear()
        self.input.setEnabled(True)
        self.input.setFocus()
        self.skip_btn.setVisible(True)
        self.hint_btn.setVisible(True)
        self.hint_btn.setText("힌트")
        self.hint_level = 0
        self.reveal.setText("")
        self.next_btn.setVisible(False)

    def _enter(self):
        if self.solved_current or self.idx >= len(self.items):
            return
        typed = self.input.text().strip()
        if not typed:
            return
        w, _ = self.items[self.idx]
        if typed.lower() == w.word.lower():
            self.solved_current = True
            self.mark.setStyleSheet(f"color:{GREEN}; font-size:40px; font-weight:bold;")
            self.mark.setText("O")
            self.input.setEnabled(False)
            self.hint.setText("정답!  다음 문제로 넘어갈까요?  (Enter 또는 '다음')")
            self.reveal.setText("")
            self.skip_btn.setVisible(False)
            self.hint_btn.setVisible(False)
            self.next_btn.setVisible(True)
            self.next_btn.setFocus()
        else:
            self.mark.setStyleSheet(f"color:{RED}; font-size:40px; font-weight:bold;")
            self.mark.setText("X")
            self.input.selectAll()           # 맞출 때까지 다시 입력
            self.input.setFocus()

    def _go_next(self):
        if self.idx < len(self.items):
            w, _ = self.items[self.idx]
            if self.db:
                self.db.record(w.word, True)
            self.results.append((w, True))
        self.idx += 1
        self._next()

    def _skip(self):
        if self.idx < len(self.items):
            w, _ = self.items[self.idx]
            if self.db:
                self.db.record(w.word, False)
            self.results.append((w, False))
        self.idx += 1
        self._next()

    def _finish(self):
        self.card.setVisible(False)
        self.input.setVisible(False)
        self.skip_btn.setVisible(False)
        self.hint_btn.setVisible(False)
        self.next_btn.setVisible(False)
        self.quit_btn.setVisible(False)
        self.close_btn.setVisible(True)
        n = len(self.results)
        correct = sum(1 for _, ok in self.results if ok)
        self.progress.setText("문장 완성 종료")
        h = [f"<div style='font-family:Segoe UI;color:{FG};font-size:13px;line-height:1.6;'>"]
        h.append(f"<div style='color:{PURPLE};font-size:18px;font-weight:bold;'>결과 — {correct} / {n} 맞춤</div><br>")
        if not self.results:
            h.append(f"<div style='color:{COMMENT};'>푼 문제가 없습니다.</div>")
        for w, ok in self.results:
            mark = "✅" if ok else "⏭"
            h.append(f"<div style='margin:3px 0;'>{mark} <b style='color:{CYAN};'>{html.escape(w.word)}</b> "
                     f"<span style='color:{COMMENT};'>{html.escape(w.meaning)}</span></div>")
        h.append("</div>")
        self.result_view.setHtml("".join(h))
        self.result_view.setVisible(True)


class DrillDialog(QDialog):
    """영단어 학습(깜빡임/문장 완성)을 독립 창(모달)으로 — 트레이/메인창 숨김 상태에서 단독 실행용.
    창 투명도 조절 슬라이더 포함."""

    def __init__(self, parent, drill, words, db, title="영단어 학습"):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setWindowIcon(app_icon())
        self.resize(440, 400)
        lay = QVBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)

        top = QHBoxLayout()
        top.setContentsMargins(10, 6, 12, 0)
        top.addStretch(1)
        cap = QLabel("투명도")
        cap.setStyleSheet(f"color:{COMMENT}; font-size:10px; background:transparent;")
        top.addWidget(cap)
        self.op = ClickSlider(Qt.Horizontal)
        self.op.setObjectName("OpacitySlider")
        self.op.setRange(20, 100)
        self.op.setValue(100)
        self.op.setFixedWidth(92)
        self.op.valueChanged.connect(lambda v: self.setWindowOpacity(max(0.2, v / 100.0)))
        top.addWidget(self.op)
        lay.addLayout(top)

        self.drill = drill
        self.drill.finished.connect(self.accept)
        lay.addWidget(self.drill, 1)
        self.drill.start(words, db)


# ───────────────────────── 설정 다이얼로그 ─────────────────────────

class SettingsDialog(QDialog):
    def __init__(self, parent, settings):
        super().__init__(parent)
        self.setWindowTitle("설정")
        self.resize(640, 540)
        self.s = settings
        self.win = parent
        self._checks = {}      # key -> QCheckBox

        outer = QVBoxLayout(self)
        outer.setContentsMargins(12, 12, 12, 8)
        outer.setSpacing(8)
        tabs = QTabWidget()
        outer.addWidget(tabs, 1)

        def page():
            host = QWidget()
            host.setStyleSheet("background:transparent;")
            hl = QVBoxLayout(host)
            hl.setContentsMargins(0, 0, 0, 0)
            sc = QScrollArea()
            sc.setWidgetResizable(True)
            sc.setFrameShape(QFrame.NoFrame)
            sc.setStyleSheet("background:transparent;")
            sc.viewport().setStyleSheet("background:transparent;")
            inner = QWidget()
            inner.setStyleSheet("background:transparent;")
            l = QVBoxLayout(inner)
            l.setContentsMargins(18, 16, 18, 16)
            l.setSpacing(7)
            sc.setWidget(inner)
            hl.addWidget(sc)
            return host, l

        def desc(l, t):
            x = QLabel(t)
            x.setWordWrap(True)
            x.setStyleSheet(f"color:{COMMENT};font-size:11px;")
            x.setContentsMargins(2, 0, 0, 6)
            l.addWidget(x)

        def check(l, key, label):
            cb = QCheckBox(label)
            cb.setChecked(settings.get_bool(key))
            self._checks[key] = cb
            l.addWidget(cb)
            return cb

        def combo(l, label, key, items, default):
            r = QHBoxLayout()
            r.addWidget(QLabel(label))
            c = QComboBox()
            c.addItems(items)
            c.setCurrentText(settings.get(key, default))
            r.addWidget(c)
            r.addStretch(1)
            l.addLayout(r)
            return c

        # 탭: 화면 / 표시
        p1, l1 = page()
        check(l1, "dark_titlebar", "Windows 다크 타이틀바")
        desc(l1, "창 상단 제목 표시줄을 어두운 색으로 표시합니다 (Windows 10/11).")
        check(l1, "show_stdin", "터미널에 입력(stdin) 칸 표시")
        desc(l1, "Run 실행 시 직접 입력값을 넣는 칸. 끄면 숨겨집니다.")
        self.combo_font = combo(l1, "에디터 글자 크기 (pt)", "editor_font_size",
                                ["8", "9", "10", "11", "12", "13", "14", "16", "18"], "11")
        desc(l1, "코드 에디터와 터미널의 글자 크기.")
        l1.addStretch(1)
        tabs.addTab(p1, "화면 / 표시")

        # 탭: 풀이 / 학습
        p2, l2 = page()
        check(l2, "reset_on_start", "시작할 때 작성한 코드·터미널 초기화")
        desc(l2, "프로그램을 켤 때마다 에디터를 기본 템플릿으로 되돌리고 터미널을 비웁니다. "
                 "(푼 문제 기록·랭크·영단어 진행은 유지됩니다.)")
        check(l2, "autofill_stdin", "Run 시 입력칸이 비어 있으면 예제 입력 자동 사용")
        desc(l2, "입력값을 직접 넣지 않아도 그 문제의 첫 예제 입력으로 바로 실행해 봅니다.")
        check(l2, "keep_solutions", "작성한 풀이 파일 보관")
        desc(l2, "끄면 종료 시 풀이 코드 파일을 정리해 디스크 용량을 아낍니다.")
        check(l2, "rank_unlock", "랭크 잠금 해제 (모든 랭크 문제 풀기)")
        desc(l2, "기본은 현재 랭크까지만 풀 수 있고 상위 랭크 문제는 잠겨 있습니다. "
                 "이 옵션을 켜면 브론즈여도 플래티넘 문제까지 바로 풀 수 있습니다.")
        l2.addStretch(1)
        tabs.addTab(p2, "풀이 / 학습")

        # 탭: 영단어
        p3, l3 = page()
        self.combo = combo(l3, "퀴즈 문항 수", "quiz_size", ["10", "15", "20", "30"], "10")
        desc(l3, "Run 또는 우클릭으로 푸는 단어 퀴즈의 문제 수.")
        l3.addStretch(1)
        tabs.addTab(p3, "영단어")

        # 탭: 종료
        p4, l4 = page()
        cr = QHBoxLayout()
        cr.addWidget(QLabel("닫기(X) 버튼 동작"))
        self.combo_close = QComboBox()
        for label, data in [("프로그램 종료", "quit"), ("트레이로 보내기", "tray"), ("물어보기", "ask")]:
            self.combo_close.addItem(label, data)
        ci = self.combo_close.findData(settings.get("close_action", "quit") or "quit")
        self.combo_close.setCurrentIndex(ci if ci >= 0 else 0)
        cr.addWidget(self.combo_close)
        cr.addStretch(1)
        l4.addLayout(cr)
        desc(l4, "창의 X를 눌렀을 때 종료할지, 트레이로 보낼지, 매번 물어볼지 선택합니다. "
                 "종료 시에는 한 번 더 확인합니다(‘트레이로 보내기’면 트레이 종료는 바로 실행).")
        l4.addStretch(1)
        tabs.addTab(p4, "종료")

        # 탭: 관리
        p5, l5 = page()
        for label, fn in [("문제 변형 리셋 (변수 문제 새 값으로)", parent._on_reset),
                          ("내 티어 초기화 (푼 기록 삭제)", parent._reset_tier),
                          ("환경 점검 (JDK / g++ / Node)", parent._env_check)]:
            b = QPushButton(label)
            b.setObjectName("ManageBtn")
            b.clicked.connect(lambda _=False, fn=fn: (self.accept(), fn()))
            l5.addWidget(b)
        l5.addStretch(1)
        tabs.addTab(p5, "관리")

        save = QPushButton("저장")
        save.setObjectName("Run")
        save.clicked.connect(self._save)
        bar = QHBoxLayout()
        bar.setContentsMargins(4, 0, 4, 4)
        bar.addStretch(1)
        bar.addWidget(save)
        outer.addLayout(bar)

    def _save(self):
        for key, cb in self._checks.items():
            self.s.set(key, "1" if cb.isChecked() else "0")
        self.s.set("editor_font_size", self.combo_font.currentText())
        self.s.set("quiz_size", self.combo.currentText())
        self.s.set("close_action", self.combo_close.currentData())
        self.win._apply_settings()
        self.accept()


# ───────────────────────── 사용법 다이얼로그 ─────────────────────────

HELP_HTML = f"""
<div style='font-family:Segoe UI; color:{FG}; font-size:13px; line-height:1.6;'>
<div style='color:{PURPLE}; font-size:18px; font-weight:bold;'>code T 사용법</div>

<div style='color:{CYAN}; font-size:14px; font-weight:bold; margin-top:14px;'>1. 문제 풀이</div>
① 왼쪽 사이드바에서 <b>문제</b>를 고릅니다 (랭크 / 실전 / 종목).<br>
② 상단에서 풀 <b>언어</b>(Python·Java·C++·JS)를 선택합니다.<br>
③ 오른쪽 <b>console</b>(에디터)에 코드를 작성합니다.<br>
④ <b>Run</b>으로 직접 실행해 보거나, <b>제출</b>로 채점합니다.

<div style='color:{CYAN}; font-size:14px; font-weight:bold; margin-top:14px;'>2. Run 과 제출의 차이</div>
<b>▶ Run (F5)</b> — 내가 <b>직접 넣은 입력</b>으로 코드를 실행해 출력만 확인합니다. (채점 아님)<br>
<b>제출 (Ctrl+Enter)</b> — 문제의 <b>테스트케이스</b>로 정답/오답을 채점합니다.

<div style='color:{CYAN}; font-size:14px; font-weight:bold; margin-top:14px;'>3. 입력(stdin) — 값 구분</div>
하단 터미널 오른쪽 위 <b>입력(stdin)</b> 칸에 값을 직접 넣습니다.<br>
입력값은 <b>공백</b> 또는 <b>줄바꿈</b>으로 구분됩니다. 둘 다 됩니다.<br>
예) <span style='color:{YELLOW};'>1 2</span> (한 줄, 공백 구분) 또는 <span style='color:{YELLOW};'>1</span>↵<span style='color:{YELLOW};'>2</span> (두 줄).<br>
→ Java <code>Scanner.nextInt()</code>, Python <code>input().split()</code>, C++ <code>cin&gt;&gt;</code> 모두 공백·줄바꿈을 똑같이 구분자로 읽습니다.<br>
<span style='color:{COMMENT};'>여러 줄 입력이 필요한 문제는 칸에 여러 줄로 그대로 넣으면 됩니다.</span>

<div style='color:{CYAN}; font-size:14px; font-weight:bold; margin-top:14px;'>4. 채점 결과 (합격 / 불합격)</div>
모든 테스트케이스를 통과하면 <b style='color:{GREEN};'>정답(all passed)</b> → 진행도·랭크에 반영됩니다.<br>
하나라도 틀리면 <b style='color:{RED};'>오답</b>이며, 케이스별로 아래처럼 표시됩니다:<br>
PASS(정답) · FAIL(출력 다름) · TIMEOUT(시간 초과) · MEM(메모리 초과) · ERROR(런타임 에러) · BUILD ERR(컴파일 에러)<br>
<span style='color:{COMMENT};'>시간·메모리 제한은 문제마다 다르고, 언어별로 차등 적용됩니다(C++이 가장 빡빡).</span>

<div style='color:{CYAN}; font-size:14px; font-weight:bold; margin-top:14px;'>5. 힌트</div>
문제 설명 영역에서 <b>우클릭</b> → 힌트 1·2·3·정답 순서로 단계별로 볼 수 있습니다.<br>
막혔을 때만 한 단계씩 열어 스스로 푸는 연습을 권장합니다.

<div style='color:{CYAN}; font-size:14px; font-weight:bold; margin-top:14px;'>6. 모의고사 (시험)</div>
사이드바 <b>시험</b>에서 시작하면 여러 문제가 제한 시간 안에 출제됩니다(플래티넘 1~2문제 필수).<br>
합격은 <b>합산 점수</b> 기준 — 난이도 높은 문제일수록 배점이 큽니다. 쉬운 문제 몇 개로는 합격하지 못합니다.

<div style='color:{CYAN}; font-size:14px; font-weight:bold; margin-top:14px;'>7. 영단어</div>
사이드바 <b>영단어 → 레벨 → 일반/IT → 50개 묶음</b>을 고릅니다.<br>
단어 옆 <b>[명사·동사…]</b>는 품사입니다. <b>Run</b> 또는 <b>우클릭 → 퀴즈</b>로 그 묶음을 테스트합니다.

<div style='color:{CYAN}; font-size:14px; font-weight:bold; margin-top:14px;'>8. 편의 기능</div>
<b>집중 모드</b> (Ctrl+H): 문제 설명을 숨기고 코딩+터미널만, 창도 작게.<br>
<b>투명도</b>: 오른쪽 아래 슬라이더로 창 전체 투명도 조절(10~100%).<br>
<b>트레이</b>: 창 X를 누르면 종료/트레이로 보내기 선택. 트레이 아이콘으로 다시 열기.

<div style='color:{CYAN}; font-size:14px; font-weight:bold; margin-top:14px;'>단축키</div>
F5 / Ctrl+R 실행 · Ctrl+Enter 제출 · Ctrl+S 저장 · Ctrl+B 사이드바 · Ctrl+H 집중 모드
</div>
"""


class HelpDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("사용법")
        self.resize(580, 660)
        lay = QVBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        view = QTextBrowser()
        view.setOpenExternalLinks(True)
        view.setStyleSheet(f"background:{CARD}; border:none; padding:16px;")
        view.setHtml(HELP_HTML)
        lay.addWidget(view)


# ───────────────────────── 메인 윈도우 ─────────────────────────

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(f"code T  v{APP_VERSION}")
        self.setWindowIcon(app_icon())              # 프로그램/작업표시줄 아이콘
        self.resize(1500, 900)
        self.setMinimumSize(1160, 720)

        self.lang = "python"
        self.current = None
        self.solved = self._load_progress()
        self.item_problem = {}
        self.problem_item = {}
        self._threads = []
        self._reveal = 0          # 현재 문제에서 공개된 힌트 단계(0=없음, 4=정답코드)

        # 아이콘 (qtawesome) — 없으면 텍스트 화살표로 폴백
        if qta:
            self._ic_right = qta.icon("fa5s.chevron-right", color=COMMENT)
            self._ic_down = qta.icon("fa5s.chevron-down", color=COMMENT)
            self._ic_file = qta.icon("fa5s.file-code", color=COMMENT)
            self._ic_done = qta.icon("fa5s.file-code", color=GREEN)   # 해결: 파일 아이콘 초록색
        else:
            self._ic_right = self._ic_down = self._ic_file = self._ic_done = None

        # 점수/랭크 계산용 전체 문제 목록(랭크 + 실전)
        self._all_problems = list(problems.BY_ID.values()) + list(practice.BY_ID.values())
        self._unlocked_index = 0      # 해금된 최고 랭크(0=Bronze) — 상위는 잠김

        # 문제 변형(리셋) 상태
        self.variant_seed = None      # None=원본, 정수=변형 시드
        self.variant_cache = {}       # id -> 생성된 변형 데이터
        self._cur_active = None       # 현재 화면에 적용된 문제(변형 반영본)

        # 학습(레슨) 모드
        self._mode = "problem"        # "problem" | "lesson"
        self.current_lesson = None
        self.item_lesson = {}         # id(item) -> Lesson

        # 실전 모의고사 상태
        self.exam = None              # {preset, problems, ids, solved, deadline, group_item}
        self.item_exam = {}           # id(item) -> preset

        # 영단어
        self.item_vocab = {}          # id(item) -> level
        self.vocab_db = VocabDB(SOLUTIONS_DIR / "vocab.db")

        # 설정 (sqlite)
        self.settings = SettingsDB(SOLUTIONS_DIR / "app.db")
        # 시작 시 작성 코드·터미널 초기화 — 풀이 코드 폴더만 제거(진행기록·DB는 유지)
        if self.settings.get_bool("reset_on_start"):
            for d in SOLUTIONS_DIR.glob("*"):
                if d.is_dir():
                    shutil.rmtree(d, ignore_errors=True)
        self.exam_timer = QTimer(self)
        self.exam_timer.setInterval(1000)
        self.exam_timer.timeout.connect(self._tick_exam)

        central = QWidget()
        self._central = central
        self.setCentralWidget(central)
        outer = QVBoxLayout(central)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(0)
        outer.addWidget(self._build_titlebar())
        outer.addWidget(self._build_body(), 1)
        self._build_opacity_overlay(central)

        # 앱 전역 단축키 (에디터에 포커스가 있어도 동작)
        self._shortcuts = []
        for seq in ("F5", "Ctrl+R"):          # 실행
            sc = QShortcut(QKeySequence(seq), self)
            sc.setContext(Qt.ApplicationShortcut)
            sc.activated.connect(self.on_run)
            self._shortcuts.append(sc)
        for seq in ("Ctrl+Return", "Ctrl+Enter"):   # 제출(채점)
            sc = QShortcut(QKeySequence(seq), self)
            sc.setContext(Qt.ApplicationShortcut)
            sc.activated.connect(self.on_submit)
            self._shortcuts.append(sc)
        save_sc = QShortcut(QKeySequence("Ctrl+S"), self)
        save_sc.setContext(Qt.ApplicationShortcut)
        save_sc.activated.connect(lambda: self._save_editor(force=True))   # 명시적 저장은 항상 기록
        self._shortcuts.append(save_sc)
        side_sc = QShortcut(QKeySequence("Ctrl+B"), self)   # 사이드바 접기/펴기
        side_sc.setContext(Qt.ApplicationShortcut)
        side_sc.activated.connect(self._toggle_sidebar)
        self._shortcuts.append(side_sc)
        hide_sc = QShortcut(QKeySequence("Ctrl+H"), self)   # 하이드(집중) 모드
        hide_sc.setContext(Qt.ApplicationShortcut)
        hide_sc.activated.connect(self._toggle_hide_mode)
        self._shortcuts.append(hide_sc)

        self._hidden_mode = False
        self._saved_geometry = None
        self._tray_hinted = False
        self._build_tree()
        self._populate_hide_combo()
        self._build_tray()
        self._update_profile()
        self._apply_settings()
        # 저장된 투명도 적용
        op = self.settings.get_int("opacity", 100)
        op = min(100, max(10, op))
        self.opacity_slider.setValue(op)
        self._set_opacity(op)
        self._native_applied = False

    def closeEvent(self, event):
        # X 버튼: 기본은 종료(컨펌), 설정에 따라 트레이/물어보기
        action = self.settings.get("close_action", "quit") or "quit"
        if action == "ask":
            action = self._ask_close_action()
            if action is None:                  # 취소
                event.ignore()
                return
            # ask 에서 고른 대로 바로 처리(추가 컨펌 없음)
            if action == "tray" and getattr(self, "tray", None) is not None:
                event.ignore()
                self.hide()
                self.tray.show()
                return
            self._do_quit(event)
            return
        if action == "tray" and getattr(self, "tray", None) is not None:
            event.ignore()
            self.hide()
            self.tray.show()
            return
        # action == "quit" → 컨펌 후 종료
        if not self._confirm_quit():
            event.ignore()
            return
        self._do_quit(event)

    def _confirm_quit(self):
        return QMessageBox.question(self, "종료", "프로그램을 종료할까요?",
                                    QMessageBox.Yes | QMessageBox.No,
                                    QMessageBox.No) == QMessageBox.Yes

    def _do_quit(self, event=None):
        self._cleanup_solutions()
        if getattr(self, "tray", None) is not None:
            self.tray.hide()
        if event is not None:
            event.accept()
        QApplication.instance().quit()

    def _cleanup_solutions(self):
        # 풀이 파일 보관 끄면 종료 시 문제 풀이 폴더 정리(용량 절약). db/진행상황은 유지.
        if not self.settings.get_bool("keep_solutions"):
            for d in SOLUTIONS_DIR.glob("*"):
                if d.is_dir():
                    shutil.rmtree(d, ignore_errors=True)

    def _ask_close_action(self):
        """X 클릭 시 종료/트레이 선택. None=취소. '기억' 체크 시 설정에 저장."""
        box = QMessageBox(self)
        box.setWindowTitle("종료")
        box.setText("프로그램을 어떻게 할까요?")
        quit_b = box.addButton("프로그램 종료", QMessageBox.AcceptRole)
        tray_b = box.addButton("트레이로 보내기", QMessageBox.ActionRole)
        box.addButton("취소", QMessageBox.RejectRole)
        remember = QCheckBox("다음부터 이 선택 기억")
        box.setCheckBox(remember)
        box.exec()
        clicked = box.clickedButton()
        if clicked is quit_b:
            action = "quit"
        elif clicked is tray_b:
            action = "tray"
        else:
            return None
        if remember.isChecked():
            self.settings.set("close_action", action)
        return action

    # ---- 시스템 트레이 ----
    def _build_tray(self):
        if not QSystemTrayIcon.isSystemTrayAvailable():
            self.tray = None
            return
        self.tray = QSystemTrayIcon(self)
        self.tray.setIcon(app_icon())
        self.tray.setToolTip("code T")
        self._tray_menu = QMenu()
        self._tray_menu.addAction("열기", self._show_normal)
        self._tray_menu.addAction("하이드 모드", self._tray_hide_mode)
        # 영단어 학습 — 레벨(기초/중급/고급) 선택 → 메인창 없이 단독 다이얼로그로 진행
        m_type = self._tray_menu.addMenu("깜빡임 암기")
        for lv in vocab.LEVELS:
            m_type.addAction(lv, lambda _=False, l=lv: self._tray_vocab_drill(l, "typing"))
        m_sent = self._tray_menu.addMenu("문장 완성")
        for lv in vocab.LEVELS:
            m_sent.addAction(lv, lambda _=False, l=lv: self._tray_vocab_drill(l, "sentence"))
        m_rev = self._tray_menu.addMenu("🔁 오답 복습")
        for lv in vocab.LEVELS:
            m_rev.addAction(lv, lambda _=False, l=lv: self._tray_vocab_drill(l, "review"))
        self._tray_menu.addSeparator()
        self._tray_menu.addAction("종료", self._quit_app)
        self.tray.setContextMenu(self._tray_menu)
        self.tray.activated.connect(self._tray_activated)
        self.tray.show()

    def _tray_vocab_drill(self, level, mode):
        """트레이에서 영단어 학습 — 레벨 전체에서 랜덤 추출, 메인창 없이 모달 다이얼로그로."""
        words = vocab.BY_LEVEL.get(level, [])
        if not words:
            return
        if mode == "review":
            # 오답 복습 — 이 레벨에서 틀린 적 있는(못 외운) 단어만
            wrong = self.vocab_db.wrong_set()
            words = [w for w in words if w.word in wrong]
            if not words:
                if self.tray:
                    self.tray.showMessage("code T", f"{level} 레벨에 복습할 오답 단어가 없어요!",
                                          QSystemTrayIcon.Information, 3000)
                return
            DrillDialog(self, TypingDrillWidget(), words, self.vocab_db,
                        f"오답 복습 · {level} ({len(words)}개)").exec()
        elif mode == "sentence":
            DrillDialog(self, SentenceDrillWidget(), words, self.vocab_db,
                        f"문장 완성 · {level}").exec()
        else:
            DrillDialog(self, TypingDrillWidget(), words, self.vocab_db,
                        f"깜빡임 암기 · {level}").exec()

    def _tray_activated(self, reason):
        if reason in (QSystemTrayIcon.DoubleClick, QSystemTrayIcon.Trigger):
            self._show_normal()

    def _show_normal(self):
        self.showNormal()
        self._force_foreground()

    def _force_foreground(self):
        """창을 최상위로 올리고 포커스를 가져온다.

        Windows 는 다른 앱이 포커스를 쥐고 있으면 SetForegroundWindow 를 막는다
        (새로 실행한 창이 뒤에 깔리는 현상). 포그라운드 스레드에 입력을 잠시
        붙였다 떼는 표준 우회로 확실히 앞으로 가져온다."""
        self.setWindowState((self.windowState() & ~Qt.WindowMinimized) | Qt.WindowActive)
        self.raise_()
        self.activateWindow()
        if sys.platform != "win32":
            return
        try:
            import ctypes
            user32 = ctypes.windll.user32
            hwnd = int(self.winId())
            if user32.GetForegroundWindow() == hwnd:
                return
            # 1) ALT 키를 살짝 눌렀다 떼면 포그라운드 잠금이 풀린다 (고전적 우회)
            KEYUP = 0x0002
            VK_MENU = 0x12
            user32.keybd_event(VK_MENU, 0, 0, 0)
            user32.keybd_event(VK_MENU, 0, KEYUP, 0)
            user32.SetForegroundWindow(hwnd)
            # 2) 포그라운드 스레드에 입력을 붙였다 떼는 우회
            if user32.GetForegroundWindow() != hwnd:
                fg = user32.GetForegroundWindow()
                cur = ctypes.windll.kernel32.GetCurrentThreadId()
                fg_thread = user32.GetWindowThreadProcessId(fg, None)
                if fg and fg_thread != cur and user32.AttachThreadInput(fg_thread, cur, True):
                    user32.BringWindowToTop(hwnd)
                    user32.SetForegroundWindow(hwnd)
                    user32.AttachThreadInput(fg_thread, cur, False)
            # 3) 그래도 안 되면 TOPMOST 토글로 Z순서만이라도 최상위 보장
            if user32.GetForegroundWindow() != hwnd:
                SWP = 0x0001 | 0x0002 | 0x0010      # NOSIZE|NOMOVE|NOACTIVATE
                user32.SetWindowPos(hwnd, -1, 0, 0, 0, 0, SWP)   # HWND_TOPMOST
                user32.SetWindowPos(hwnd, -2, 0, 0, 0, 0, SWP)   # HWND_NOTOPMOST
        except Exception:
            pass

    def _tray_hide_mode(self):
        self._show_normal()
        self._set_hide_mode(True)

    def _quit_app(self):
        # 트레이 '종료': X가 '트레이로 보내기'로 설정돼 있으면 바로 종료,
        # 그 외(종료/물어보기)면 메인창 띄우고 컨펌 후 종료.
        if self.settings.get("close_action", "quit") != "tray":
            self._show_normal()
            if not self._confirm_quit():
                return
        self._do_quit()

    # ---- 하이드(집중) 모드 ----
    def _populate_hide_combo(self):
        self.hide_combo.blockSignals(True)
        self.hide_combo.clear()
        self.hide_combo.addItem("— 문제 선택 —", None)
        for p in self._all_problems:
            tier = p.tier or RANK_INITIAL.get(p.rank, p.rank)
            self.hide_combo.addItem(f"[{tier}] {p.title}", p.id)
        self.hide_combo.blockSignals(False)

    def _sync_hide_combo(self):
        pid = self.current.id if self.current else None
        idx = self.hide_combo.findData(pid) if pid else 0
        self.hide_combo.setCurrentIndex(idx if idx >= 0 else 0)

    def _on_hide_combo(self, index):
        pid = self.hide_combo.itemData(index)
        if not pid:
            return
        items = self.problem_item.get(pid)
        if items:
            self.tree.setCurrentItem(items[0])      # → on_tree_select 로 로드

    def _toggle_hide_mode(self):
        # 레슨 모드는 하이드 콤보(문제 전용)와 호환되지 않음 — 진입 차단
        if not self._hidden_mode and self._mode == "lesson":
            self._set_status("하이드 모드는 문제/영단어에서만 사용할 수 있어요", ORANGE)
            return
        self._set_hide_mode(not self._hidden_mode)

    def _apply_hide_visibility(self):
        """하이드 모드 가시성 — 문제 모드: 코딩+터미널만 / 영단어 모드: 단어 카드만."""
        on = self._hidden_mode
        is_vocab = self._mode == "vocab"
        self.side.setVisible(not on)
        self.probp.setVisible((not on) or is_vocab)   # 영단어면 카드 유지(작은 창에 단어 표시)
        self.hide_combo.setVisible(on and not is_vocab)
        self.rank_label.setVisible(not on)
        self.rank_bar.setVisible(not on)
        self.side_toggle.setVisible(not on)

    def _set_hide_mode(self, on):
        """on: 사이드바 숨기고 컴팩트 창. 문제 모드는 에디터+터미널, 영단어 모드는 단어 카드만."""
        if on and not self._hidden_mode:
            self._saved_geometry = self.geometry()      # 들어가기 전 창 크기/위치 기억
        self._hidden_mode = on
        self._apply_hide_visibility()
        if qta:
            self.hide_btn.setIcon(qta.icon("fa5s.expand" if on else "fa5s.compress", color=FG))
        else:
            self.hide_btn.setText("해제" if on else "집중")
        self._set_compact_header(on)
        if on:
            self.setMinimumSize(420, 360)                # 작게 줄일 수 있도록 최소치 완화
            self.resize(540, 600)                        # width 는 약 1/4 축소(720→540)
            self._sync_hide_combo()
            self._set_status("하이드 모드 — 코딩 + 터미널만 (Ctrl+H 또는 우측 버튼으로 해제)", CYAN)
        else:
            self.setMinimumSize(1160, 720)               # 원래 최소 크기 복원
            if self._saved_geometry is not None:
                self.setGeometry(self._saved_geometry)   # 원래 창 크기/위치 복원
        self._position_overlay()

    def _set_compact_header(self, on):
        """좁은 하이드 모드용 반응형 헤더 — Run은 'R', 제출은 아이콘만, 콤보·버튼 축소."""
        if on:
            self.hide_combo.setMinimumWidth(140)
            self.run_btn.setText("R")
            self.run_btn.setFixedWidth(32)
            self.run_btn.setToolTip("실행 (F5)")
            self.submit_btn.setFixedWidth(34)
            if qta:
                self.submit_btn.setText("")
                self.submit_btn.setIcon(qta.icon("fa5s.paper-plane", color=BG3))
            else:
                self.submit_btn.setText("↑")
            self.submit_btn.setToolTip("제출 — 채점 (Ctrl+Enter)")
        else:
            self.hide_combo.setMinimumWidth(240)
            self.run_btn.setText("▶ Run")
            self.run_btn.setFixedWidth(80)
            self.submit_btn.setFixedWidth(74)
            self.submit_btn.setIcon(QIcon())
            self.submit_btn.setText("제출")

    # ---- 전체 투명도 오버레이 (우측 하단, 상시) ----
    def _build_opacity_overlay(self, parent):
        bar = QFrame(parent)
        bar.setObjectName("OpacityBar")
        bar.setFixedSize(206, 30)
        lay = QHBoxLayout(bar)
        lay.setContentsMargins(10, 0, 10, 0)
        lay.setSpacing(7)
        cap = QLabel("투명도")
        cap.setStyleSheet(f"color:{COMMENT}; font-size:10px; font-weight:bold; background:transparent;")
        lay.addWidget(cap)
        self.opacity_slider = ClickSlider(Qt.Horizontal)
        self.opacity_slider.setObjectName("OpacitySlider")
        self.opacity_slider.setRange(10, 100)
        self.opacity_slider.setValue(100)
        self.opacity_slider.setFixedWidth(104)
        self.opacity_slider.setToolTip("프로그램 전체 투명도")
        self.opacity_slider.valueChanged.connect(self._on_opacity_changed)
        lay.addWidget(self.opacity_slider)
        self.opacity_label = QLabel("100%")
        self.opacity_label.setStyleSheet(f"color:{FG}; font-size:10px; background:transparent;")
        self.opacity_label.setFixedWidth(32)
        lay.addWidget(self.opacity_label)
        self.opacity_bar = bar
        bar.raise_()

    def _on_opacity_changed(self, v):
        self._set_opacity(v)
        self.settings.set("opacity", v)

    def _set_opacity(self, v):
        self.setWindowOpacity(max(0.10, min(1.0, v / 100.0)))
        if hasattr(self, "opacity_label"):
            self.opacity_label.setText(f"{v}%")

    def _position_overlay(self):
        bar = getattr(self, "opacity_bar", None)
        if bar is None or self._central is None:
            return
        m = 14
        bar.move(max(0, self._central.width() - bar.width() - m),
                 max(0, self._central.height() - bar.height() - m))
        bar.raise_()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._position_overlay()

    # ---- 네이티브 타이틀바(캡션) 다크/색상 ----
    def showEvent(self, event):
        super().showEvent(event)
        self._position_overlay()
        if not self._native_applied:
            self._native_applied = True
            self._apply_native_titlebar()

    def _apply_native_titlebar(self):
        """Windows 네이티브 타이틀바를 설정에 따라 다크/기본으로 (설정 변경 시 즉시 반영)."""
        if sys.platform != "win32":
            return
        dark = self.settings.get_bool("dark_titlebar")
        try:
            import ctypes
            hwnd = int(self.winId())
            dwm = ctypes.windll.dwmapi
            # 다크 모드 캡션 (Win10 2004+/Win11) — attr 20, 구버전 19 폴백
            def cref(hexc):
                hexc = hexc.lstrip("#")
                r, g, b = int(hexc[0:2], 16), int(hexc[2:4], 16), int(hexc[4:6], 16)
                return ctypes.c_int((b << 16) | (g << 8) | r)
            flag = ctypes.c_int(1 if dark else 0)
            if dwm.DwmSetWindowAttribute(hwnd, 20, ctypes.byref(flag), 4) != 0:
                dwm.DwmSetWindowAttribute(hwnd, 19, ctypes.byref(flag), 4)
            if dark:
                # Win11 22000+ : 캡션/텍스트/테두리 색을 VSCode 테마에 맞춤 (그 외 버전은 무시)
                cap, txt, bdr = cref(CAPTION_COLOR), cref(FG), cref(BG3)
                dwm.DwmSetWindowAttribute(hwnd, 35, ctypes.byref(cap), 4)  # caption
                dwm.DwmSetWindowAttribute(hwnd, 36, ctypes.byref(txt), 4)  # text
                dwm.DwmSetWindowAttribute(hwnd, 34, ctypes.byref(bdr), 4)  # border
            else:
                # OFF → 시스템 기본색 복원 (DWMWA_COLOR_DEFAULT)
                default = ctypes.c_uint(0xFFFFFFFF)
                for attr in (35, 36, 34):
                    dwm.DwmSetWindowAttribute(hwnd, attr, ctypes.byref(default), 4)
        except Exception:
            pass

    # ---- 진행 상황 ----
    def _load_progress(self):
        if PROGRESS_FILE.exists():
            try:
                return set(json.loads(PROGRESS_FILE.read_text(encoding="utf-8")))
            except Exception:
                return set()
        return set()

    def _save_progress(self):
        try:
            SOLUTIONS_DIR.mkdir(exist_ok=True)
            PROGRESS_FILE.write_text(json.dumps(sorted(self.solved), ensure_ascii=False), encoding="utf-8")
        except OSError as e:
            self._set_status(f"진행 저장 실패: {e}", RED)

    # ---- 타이틀바 ----
    def _build_titlebar(self):
        bar = QFrame()
        bar.setObjectName("TitleBar")
        bar.setFixedHeight(38)
        lay = QHBoxLayout(bar)
        lay.setContentsMargins(10, 0, 10, 0)
        lay.setSpacing(6)

        # 사이드바 접기/펴기
        self.side_toggle = QPushButton()
        self.side_toggle.setObjectName("Ghost")
        self.side_toggle.setFixedWidth(34)
        self.side_toggle.setToolTip("사이드바 접기/펴기 (Ctrl+B)")
        if qta:
            self.side_toggle.setIcon(qta.icon("fa5s.bars", color=FG))
        else:
            self.side_toggle.setText("☰")
        self.side_toggle.clicked.connect(self._toggle_sidebar)
        lay.addWidget(self.side_toggle)

        # 하이드(집중) 모드용 문제 선택 콤보 — 평소 숨김
        self.hide_combo = QComboBox()
        self.hide_combo.setObjectName("HideCombo")
        self.hide_combo.setMinimumWidth(240)
        self.hide_combo.setToolTip("문제 선택")
        self.hide_combo.setVisible(False)
        self.hide_combo.activated.connect(self._on_hide_combo)
        lay.addWidget(self.hide_combo)

        # 내 랭크/점수 (작게)
        self.rank_label = QLabel("—")
        self.rank_label.setObjectName("Rank")
        lay.addWidget(self.rank_label)
        self.rank_bar = QProgressBar()
        self.rank_bar.setObjectName("RankBar")
        self.rank_bar.setFixedSize(96, 10)
        self.rank_bar.setTextVisible(False)
        self.rank_bar.setRange(0, 100)
        lay.addWidget(self.rank_bar)
        lay.addSpacing(12)

        # 언어 세그먼트
        self.lang_group = QButtonGroup(self)
        self.lang_group.setExclusive(True)
        self.lang_buttons = {}
        radius = {
            "SegL": "border-top-left-radius:8px;border-bottom-left-radius:8px;",
            "SegR": "border-top-right-radius:8px;border-bottom-right-radius:8px;",
        }
        for label, code, edge in [("Python", "python", "SegL"), ("Java", "java", ""),
                                  ("C++", "cpp", ""), ("JS", "javascript", "SegR")]:
            b = QPushButton(label)
            b.setObjectName("Seg")          # 배경/hover/checked 스타일
            b.setCheckable(True)
            if edge:                         # 양 끝만 모서리 라운드
                b.setStyleSheet(radius[edge])
            if code == "python":
                b.setChecked(True)
            b.clicked.connect(lambda _=False, c=code: self._set_lang(c))
            self.lang_group.addButton(b)
            self.lang_buttons[code] = b
            lay.addWidget(b)

        lay.addStretch(1)

        def mkbtn(text, cb, obj="Ghost", w=None, tip=None):
            b = QPushButton(text)
            b.setObjectName(obj)
            b.clicked.connect(cb)
            if w:
                b.setFixedWidth(w)
            if tip:
                b.setToolTip(tip)
            return b

        # 시험 컨트롤 (평소 숨김)
        self.exam_label = QLabel("")
        self.exam_label.setObjectName("Rank")
        self.exam_label.setVisible(False)
        lay.addWidget(self.exam_label)
        self.giveup_btn = mkbtn("포기", self._giveup_exam, tip="시험 포기")
        self.giveup_btn.setVisible(False)
        lay.addWidget(self.giveup_btn)
        self.exam_end_btn = mkbtn("시험 제출", lambda: self._submit_exam(), tip="시험 채점(합격/불합격)")
        self.exam_end_btn.setVisible(False)
        lay.addWidget(self.exam_end_btn)

        # 합격 후 다음 문제 (평소 숨김)
        self.next_btn = mkbtn("다음 문제 ▶", self._next_problem, tip="다음 문제 풀기")
        self.next_btn.setVisible(False)
        lay.addWidget(self.next_btn)

        # 하이드(집중) 모드 토글
        self.hide_btn = mkbtn("집중" if not qta else "", self._toggle_hide_mode,
                              tip="하이드(집중) 모드 — 문제 설명 숨기고 코딩만 (Ctrl+H)")
        self.hide_btn.setFixedWidth(40)
        if qta:
            self.hide_btn.setIcon(qta.icon("fa5s.compress", color=FG))
        lay.addWidget(self.hide_btn)

        # 설정 메뉴
        menu_btn = mkbtn("" if qta else "⚙", self._open_settings, tip="설정")
        menu_btn.setFixedWidth(40)
        if qta:
            menu_btn.setIcon(qta.icon("fa5s.cog", color=FG))
        lay.addWidget(menu_btn)

        # 힌트 (우클릭 메뉴와 동일 — 눈에 보이는 진입점)
        self.hint_btn = mkbtn("💡 힌트", self._open_hint_menu, obj="Ghost", w=80,
                              tip="힌트 1~3단계 · 정답 코드 보기 (문제 설명 우클릭과 동일)")
        lay.addWidget(self.hint_btn)

        # 실행(출력 확인) / 제출(채점)
        self.run_btn = mkbtn("▶ Run", self.on_run, obj="Ghost", w=80, tip="실행만 — 내 입력으로 출력 확인 (F5)")
        lay.addWidget(self.run_btn)
        self.submit_btn = mkbtn("✔ 제출", self.on_submit, obj="Run", w=80, tip="채점 — 정답 판정 (Ctrl+Enter)")
        lay.addWidget(self.submit_btn)
        return bar

    def _open_hint_menu(self):
        """헤더 '힌트' 버튼 — 힌트 단계 선택 메뉴를 버튼 아래에 펼친다."""
        if self._mode != "problem" or not self.current:
            self._set_status("문제를 선택하면 힌트를 볼 수 있어요", ORANGE)
            return
        m = QMenu(self)
        a1 = m.addAction("힌트 1  ·  접근 방향")
        a2 = m.addAction("힌트 2  ·  자료구조 / 알고리즘")
        a3 = m.addAction("힌트 3  ·  거의 정답")
        m.addSeparator()
        al = m.addAction("힌트 last  ·  정답 코드 + 풀이")
        act = m.exec(self.hint_btn.mapToGlobal(self.hint_btn.rect().bottomLeft()))
        if act == a1:
            self._reveal_hint(1)
        elif act == a2:
            self._reveal_hint(2)
        elif act == a3:
            self._reveal_hint(3)
        elif act == al:
            self._reveal_hint(4)

    def _toggle_sidebar(self):
        """사이드바(탐색기)를 접거나 편다 — 접으면 나머지 카드가 그 공간을 채운다."""
        show = not self.side.isVisible()
        if not show:
            self._side_sizes = self.split.sizes()      # 접기 직전 너비 기억
        self.side.setVisible(show)
        if show and getattr(self, "_side_sizes", None):
            self.split.setSizes(self._side_sizes)      # 펼 때 이전 비율 복원

    # ---- 설정(모달) / 티어 초기화 / 환경 점검 ----
    def _open_settings(self):
        SettingsDialog(self, self.settings).exec()

    def _open_help(self):
        HelpDialog(self).exec()

    def _apply_settings(self):
        self.stdin_box.setVisible(self.settings.get_bool("show_stdin"))
        self._apply_native_titlebar()          # 다크 타이틀바 즉시 반영 (ON/OFF 모두)
        # 에디터/터미널 글자 크기
        size = self.settings.get_int("editor_font_size", 11)
        for w in (self.editor, self.out, self.stdin_box):
            f = w.font()
            f.setPointSize(size)
            w.setFont(f)
        # 랭크 잠금 해제 변경 반영(잠금 표시 새로고침)
        if hasattr(self, "_all_problems"):
            self._update_profile()
            if self.current and self._mode == "problem":
                self._render_problem(self._cur_active or self.current)

    def _reset_tier(self):
        if not self._confirm("내 티어/진행상황을 모두 초기화할까요?\n(푼 문제 기록이 삭제됩니다 · 작성한 코드는 유지)"):
            return
        ids = list(self.solved)
        self.solved.clear()
        self._save_progress()
        for pid in ids:
            p = problems.BY_ID.get(pid) or practice.BY_ID.get(pid)
            if p:
                self._refresh_item(p)
        self._update_profile()
        self._set_status("내 티어 초기화됨", CYAN)

    def _env_check(self):
        import subprocess
        import shutil

        no_window = subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0

        def ver(cmd):
            try:
                r = subprocess.run(cmd, capture_output=True, text=True, timeout=10,
                                   creationflags=no_window)
                t = (r.stdout or r.stderr).strip().splitlines()
                return t[0] if t else ""
            except Exception:
                return ""

        self.out.clear()
        self._append("== 환경 점검 ==\n\n", CYAN, bold=True)
        self._append(f"  Python (필수)    : {sys.version.split()[0]}   ✓\n", GREEN)
        if runner.compiler_available("java"):
            _, ja = runner._java_tools()
            self._append(f"  Java (JDK)       : {ver([ja, '-version'])}   ✓\n", GREEN)
        else:
            self._append("  Java (JDK)       : 미설치  ✗   → 가이드 'Java(JDK) 설치'\n", RED)
        if runner.compiler_available("cpp"):
            g = shutil.which("g++") or shutil.which("clang++")
            self._append(f"  C++ (g++)        : {ver([g, '--version'])}   ✓\n", GREEN)
        else:
            self._append("  C++ (g++)        : 미설치  ✗   → 가이드 'C++(g++) 설치'\n", RED)
        if runner.compiler_available("javascript"):
            self._append(f"  JavaScript(Node) : {ver([shutil.which('node'), '--version'])}   ✓\n", GREEN)
        else:
            self._append("  JavaScript(Node) : 미설치  ✗\n", RED)
        ok = runner.compiler_available("scss")
        self._append(f"  SCSS (libsass)   : {'사용 가능 ✓' if ok else '미설치 ✗'}\n", GREEN if ok else RED)
        self._set_status("환경 점검 완료", CYAN)

    # ---- 문제 변형(리셋) ----
    def _apply_variant(self, p):
        if self.variant_seed is None or not variants.has(p.id):
            return p
        data = self.variant_cache.get(p.id)
        if data is None:
            data = variants.make(p.id, self.variant_seed)
            self.variant_cache[p.id] = data
        kw = {k: data[k] for k in ("description", "input_desc", "output_desc", "examples", "testcases")
              if k in data}
        return dataclasses.replace(p, **kw)

    def _on_reset(self):
        ids = variants.variantable_ids()
        ok = QMessageBox.question(
            self, "문제 리셋",
            f"변수 문제 {len(ids)}개를 새 랜덤 값으로 바꾸고 다시 풀 수 있게 할까요?\n"
            "(해당 문제들의 진행 상황과 작성한 코드가 초기화됩니다)",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if ok != QMessageBox.Yes:
            return
        self.variant_seed = random.randrange(1, 10 ** 9)
        self.variant_cache.clear()
        for pid in ids:
            self.solved.discard(pid)
            d = SOLUTIONS_DIR / pid
            if d.exists():
                shutil.rmtree(d, ignore_errors=True)
            pobj = problems.BY_ID.get(pid) or practice.BY_ID.get(pid)
            if pobj:
                self._refresh_item(pobj)
        self._save_progress()
        self._update_profile()
        if self.current:
            self._cur_active = self._apply_variant(self.current)
            self._reveal = 0
            self._render_problem(self._cur_active)
            self._load_editor()
        self._set_status("리셋됨 · 새 값으로 다시 풀어보세요", CYAN)

    def _update_profile(self):
        info = profile.compute(self.solved, self._all_problems)
        self._profile_info = info
        self.rank_label.setText(f"{info['emoji']} {info['code']}")
        self.rank_bar.setValue(info["progress"])
        tip = (f"내 랭크: {info['tier_kr']}   ·   경험치 {info['score']}/{info['max_score']}   ·   {info['n_solved']}문제 해결\n"
               + "   ".join(f"{profile.RANK_EMOJI[r]} {info['solved'].get(r,0)}/{info['total'].get(r,0)}"
                            for r in profile.RANK_ORDER))
        if info.get("next_goal"):
            tip += f"\n다음 목표: {info['next_goal']}"
        unlocked_rank = profile.RANK_KR[profile.RANK_ORDER[info["rank_index"]]]
        tip += f"\n해금: {unlocked_rank}까지 풀 수 있음 (상위는 잠김 · 설정에서 해제 가능)"
        self.rank_label.setToolTip(tip)
        self.rank_bar.setToolTip(tip)
        # 해금 랭크 갱신 → 바뀌면 트리 잠금 표시 새로고침
        new_unlocked = 3 if self.settings.get_bool("rank_unlock") else info["rank_index"]
        if new_unlocked != getattr(self, "_unlocked_index", None):
            self._unlocked_index = new_unlocked
            if getattr(self, "tree", None) is not None:
                self._refresh_all_items()

    # ---- 본문 ----
    def _build_body(self):
        split = QSplitter(Qt.Horizontal)
        split.setHandleWidth(6)
        split.setContentsMargins(8, 8, 8, 8)

        self.split = split
        # 1) 탐색기
        side = QFrame()
        side.setObjectName("Side")
        self.side = side
        side.setMinimumWidth(170)
        sl = QVBoxLayout(side)
        sl.setContentsMargins(10, 10, 6, 10)
        t = QLabel("탐색기")
        t.setObjectName("PanelTitle")
        sl.addWidget(t)

        # 검색(디바운싱) — 입력 멈추고 잠시 뒤 트리 필터
        self.search_box = QLineEdit()
        self.search_box.setObjectName("SearchBox")
        self.search_box.setPlaceholderText("문제·단어·레슨 검색…")
        self.search_box.setClearButtonEnabled(True)
        self.search_box.setStyleSheet(
            f"background:{BG2}; color:{FG}; border:1px solid {BORDER}; border-radius:6px; padding:4px 8px;")
        self._search_timer = QTimer(self)
        self._search_timer.setSingleShot(True)
        self._search_timer.setInterval(250)
        self._search_timer.timeout.connect(self._apply_search)
        self.search_box.textChanged.connect(lambda _: self._search_timer.start())
        sl.addWidget(self.search_box)

        self.tree = QTreeWidget()
        self.tree.setItemDelegate(TierDelegate(self.tree))   # 티어 색/체크 커스텀 렌더
        self.tree.setHeaderHidden(True)
        self.tree.setIndentation(14)
        self.tree.setRootIsDecorated(False)          # 기본 분기 화살표 숨김(직접 ▸/▾ 표시)
        self.tree.setExpandsOnDoubleClick(False)     # 더블클릭 펼침 끔
        self.tree.setTextElideMode(Qt.ElideNone)     # 긴 제목 → 가로 스크롤
        self.tree.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tree.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tree.currentItemChanged.connect(self.on_tree_select)
        self.tree.itemClicked.connect(self._on_tree_clicked)       # 한 번 클릭으로 토글
        self.tree.itemExpanded.connect(self._set_group_arrow)
        self.tree.itemCollapsed.connect(self._set_group_arrow)
        self.tree.setContextMenuPolicy(Qt.CustomContextMenu)       # 문제 우클릭 메뉴
        self.tree.customContextMenuRequested.connect(self._tree_menu)
        sl.addWidget(self.tree, 1)

        # 사이드바 하단 고정 버튼 — 사용법 / 설정
        botrow = QHBoxLayout()
        botrow.setSpacing(6)
        help_b = QPushButton("  사용법" if qta else "사용법")
        help_b.setObjectName("Ghost")
        help_b.setToolTip("사용법 · 단축키 안내")
        if qta:
            help_b.setIcon(qta.icon("fa5s.question-circle", color=FG))
        help_b.clicked.connect(self._open_help)
        set_b = QPushButton("  설정" if qta else "설정")
        set_b.setObjectName("Ghost")
        set_b.setToolTip("설정")
        if qta:
            set_b.setIcon(qta.icon("fa5s.cog", color=FG))
        set_b.clicked.connect(self._open_settings)
        botrow.addWidget(help_b, 1)
        botrow.addWidget(set_b, 1)
        sl.addLayout(botrow)
        split.addWidget(side)

        # 2) 문제 설명
        probp = QFrame()
        self.probp = probp
        probp.setObjectName("PanelBG")
        pl = QVBoxLayout(probp)
        pl.setContentsMargins(10, 10, 10, 10)
        pt = QLabel("문제")
        pt.setObjectName("PanelTitle")
        pl.addWidget(pt)

        # 콘텐츠 영역: 0=네이티브 문제 뷰, 1=HTML 뷰(레슨/가이드/시험/영단어)
        self.content = QStackedWidget()
        self.prob_view = ProblemView()
        self.prob_view.setContextMenuPolicy(Qt.CustomContextMenu)   # 우클릭 → 힌트 메뉴
        self.prob_view.customContextMenuRequested.connect(
            lambda pos: self._prob_menu(pos, self.prob_view))
        self.content.addWidget(self.prob_view)
        self.prob = QTextBrowser()
        self.prob.setOpenExternalLinks(False)
        self.prob.setContextMenuPolicy(Qt.CustomContextMenu)
        self.prob.customContextMenuRequested.connect(
            lambda pos: self._prob_menu(pos, self.prob))
        self.content.addWidget(self.prob)
        pl.addWidget(self.content, 1)
        split.addWidget(probp)

        # 3) 에디터 + 결과
        right = QSplitter(Qt.Vertical)
        self.right = right
        right.setHandleWidth(6)

        editp = QFrame()
        editp.setObjectName("PanelBG")
        el = QVBoxLayout(editp)
        el.setContentsMargins(10, 8, 10, 10)
        ehead = QHBoxLayout()
        ct = QLabel("console")
        ct.setObjectName("PanelTitle")
        self.file_label = QLabel("solution.py")
        self.file_label.setObjectName("FileLabel")
        self.status = QLabel("문제를 선택하세요")
        self.status.setObjectName("Status")
        self.status.setStyleSheet(f"color:{COMMENT};")
        ehead.addWidget(ct)
        ehead.addSpacing(10)
        ehead.addWidget(self.file_label)
        ehead.addStretch(1)
        ehead.addWidget(self.status)
        el.addLayout(ehead)
        self.editor = CodeEditor()
        self.editor.run_callback = self.on_run          # console 우클릭 → 실행
        el.addWidget(self.editor, 1)
        right.addWidget(editp)

        outp = QFrame()
        outp.setObjectName("Panel")
        ol = QVBoxLayout(outp)
        ol.setContentsMargins(10, 10, 6, 10)
        ohead = QHBoxLayout()
        ot = QLabel("terminal")
        ot.setObjectName("PanelTitle")
        ohead.addWidget(ot)
        ohead.addStretch(1)
        sl = QLabel("입력(stdin)")
        sl.setObjectName("PanelTitle")
        ohead.addWidget(sl)
        ol.addLayout(ohead)
        self.stdin_box = QPlainTextEdit()
        self.stdin_box.setFont(QFont(MONO_FAMILY, 9))
        self.stdin_box.setFixedHeight(46)
        self.stdin_box.setPlaceholderText(
            "Run(실행) 시 직접 넣는 입력값. 공백 또는 줄바꿈으로 구분 (예: 1 2). 제출(채점) 땐 무시됩니다.")
        ol.addWidget(self.stdin_box)
        self.out = QTextEdit()
        self.out.setObjectName("Output")
        self.out.setReadOnly(True)
        self.out.setFont(QFont(MONO_FAMILY, 9))
        ol.addWidget(self.out, 1)
        right.addWidget(outp)
        right.setSizes([560, 250])
        # 우측을 스택으로: 0=코드+터미널, 1=타이핑 암기(영단어 학습 중 인라인)
        self.right_stack = QStackedWidget()
        self.right_stack.addWidget(right)
        self.typing_widget = TypingDrillWidget()
        self.typing_widget.finished.connect(self._end_inline_typing)
        self.right_stack.addWidget(self.typing_widget)
        self.sentence_widget = SentenceDrillWidget()
        self.sentence_widget.finished.connect(self._end_inline_typing)
        self.right_stack.addWidget(self.sentence_widget)
        split.addWidget(self.right_stack)

        # 텍스트 영역(문제/console/terminal/입력)의 viewport 배경을 카드색과 정확히 일치
        # (QSS 'background'는 viewport 까지 적용 안 되어 팔레트 Base 색이 새어 나오는 걸 방지)
        for w in (self.prob, self.editor, self.out, self.stdin_box):
            bg = TERM_BG if w in (self.out, self.stdin_box) else CARD
            pal = w.palette()
            pal.setColor(QPalette.Base, QColor(bg))
            pal.setColor(QPalette.Window, QColor(bg))
            w.setPalette(pal)
            w.viewport().setAutoFillBackground(True)

        # 반응형: 창/사이드바 변화 시 문제·에디터 영역이 비율대로 늘어나도록
        probp.setMinimumWidth(240)
        right.setMinimumWidth(320)
        split.setStretchFactor(0, 0)   # 사이드바: 고정폭 유지
        split.setStretchFactor(1, 3)   # 문제 카드
        split.setStretchFactor(2, 5)   # 에디터+터미널
        split.setSizes([260, 420, 660])
        return split

    # ---- 트리 ----
    def _group_item(self, parent, base, top=False):
        it = QTreeWidgetItem(parent, [base])
        it.setData(0, Qt.UserRole + 1, base)        # 화살표 토글용 원본 라벨
        f = it.font(0)
        f.setBold(True)
        if top:
            it.setForeground(0, QColor(PURPLE))
            f.setPointSize(f.pointSize() + 1)
        else:
            it.setForeground(0, QColor(CYAN))
        it.setFont(0, f)
        self._set_group_arrow(it)
        return it

    def _set_group_arrow(self, it):
        base = it.data(0, Qt.UserRole + 1)
        if base is None:
            return
        if self._ic_right is not None:
            it.setText(0, base)
            it.setIcon(0, self._ic_down if it.isExpanded() else self._ic_right)
        else:
            it.setText(0, ("▾  " if it.isExpanded() else "▸  ") + base)

    def _on_tree_clicked(self, it, col):
        if it.childCount() > 0:                      # 그룹이면 한 번 클릭으로 펼침/접힘
            it.setExpanded(not it.isExpanded())

    def _build_tree(self):
        # 1) 언어 문법 학습 (최상단)
        lg = self._group_item(self.tree, "언어", top=True)
        for lang in lessons.LANGS:
            if not sum(len(lessons.ALL[lang][lv]) for lv in lessons.LEVELS):
                continue
            ln = self._group_item(lg, lessons.LANG_KR[lang])
            for lv in lessons.LEVELS:
                items = lessons.ALL[lang][lv]
                if not items:
                    continue
                lvnode = self._group_item(ln, f"{lv} ({len(items)})")
                for les in items:
                    self._add_lesson(lvnode, les)

        # 2) 랭크 (랭크별 문제 — 실전 문제도 난이도에 맞게 포함)
        rk = self._group_item(self.tree, "랭크", top=True)
        rank_groups = {r: [] for r in problems.RANKS}
        for p in self._all_problems:
            if p.rank in rank_groups:
                rank_groups[p.rank].append(p)
        for r in problems.RANKS:
            lst = sorted(rank_groups[r], key=lambda x: (profile.problem_points(x), x.id))
            node = self._group_item(rk, f"{profile.RANK_EMOJI[r]} {profile.RANK_KR[r]} ({len(lst)})")
            for p in lst:
                self._add_problem(node, p)
        rk.setExpanded(True)        # 랭크만 상시 펼침(하위 브론즈~플래티넘은 닫힌 채로)

        # 4) 실전 (유형별)
        pr = self._group_item(self.tree, "실전", top=True)
        for cat in practice.CATEGORIES:
            plist = practice.ALL.get(cat, [])
            if not plist:
                continue
            node = self._group_item(pr, f"{cat}")
            for p in plist:
                self._add_problem(node, p)

        # 5) 종목별 (기초→고급)
        ptg = self._group_item(self.tree, "종목", top=True)
        for tname in topics.TOPIC_ORDER:
            plist = topics.build(self._all_problems).get(tname, [])
            if not plist:
                continue
            node = self._group_item(ptg, f"{tname} ({len(plist)})")
            for p in plist:
                self._add_problem(node, p)

        # 6) 시험 — 대표 도전 + 프리셋 5종
        ex = self._group_item(self.tree, "시험", top=True)
        it = QTreeWidgetItem(ex, ["🏁 실전 코딩테스트 도전"])
        if self._ic_file is not None:
            it.setIcon(0, self._ic_file)
        self.item_exam[id(it)] = exam.CHALLENGE
        for preset in exam.PRESETS:
            pit = QTreeWidgetItem(ex, [preset["title"]])
            if self._ic_file is not None:
                pit.setIcon(0, self._ic_file)
            self.item_exam[id(pit)] = preset

        # 6) 가이드
        if lessons.GUIDES:
            gd = self._group_item(self.tree, "가이드", top=True)
            for les in lessons.GUIDES:
                self._add_lesson(gd, les)

        # 7) 영단어 (최하단) — 레벨 > 카테고리(일반/IT) > 50개 묶음
        if vocab.total():
            vg = self._group_item(self.tree, "영단어", top=True)
            CHUNK = 50
            for lv in vocab.LEVELS:
                words = vocab.BY_LEVEL.get(lv, [])
                if not words:
                    continue
                lvnode = self._group_item(vg, f"{lv} ({len(words)})")
                # 레벨 전체에서 테스트
                allit = QTreeWidgetItem(lvnode, [f"⭐ 전체 테스트 ({len(words)})"])
                if self._ic_file is not None:
                    allit.setIcon(0, self._ic_file)
                self.item_vocab[id(allit)] = {
                    "title": f"{lv} 전체", "words": words, "level": lv,
                }
                for cat in vocab.CATEGORIES:
                    cwords = [w for w in words if w.category == cat]
                    if not cwords:
                        continue
                    catnode = self._group_item(lvnode, f"{cat} ({len(cwords)})")
                    for i in range(0, len(cwords), CHUNK):
                        chunk = cwords[i:i + CHUNK]
                        label = f"{i + 1}–{i + len(chunk)}"
                        it = QTreeWidgetItem(catnode, [label])
                        if self._ic_file is not None:
                            it.setIcon(0, self._ic_file)
                        self.item_vocab[id(it)] = {
                            "title": f"{lv} · {cat} · {label}", "words": chunk, "level": lv,
                        }

    def _add_lesson(self, parent, les):
        it = QTreeWidgetItem(parent, [les.title])
        if self._ic_file is not None:
            it.setIcon(0, self._ic_file)
        self.item_lesson[id(it)] = les

    @staticmethod
    def _tier_num(p):
        t = getattr(p, "tier", "") or ""
        return int(t[-1]) if t[-1:].isdigit() else None

    def _apply_item_style(self, it, p, solved):
        """티어/해결/잠금 정보를 데이터로 저장 → TierDelegate 가 렌더.
        해결=앞 파일 아이콘 초록색, 잠김(상위 랭크)=흐리게 + 🔒."""
        it.setText(0, p.title)
        if self._ic_file is not None:
            it.setIcon(0, self._ic_done if solved else self._ic_file)
        it.setData(0, ROLE_TIER, self._tier_num(p))
        it.setData(0, ROLE_TIERCODE, getattr(p, "tier", "") or "")
        it.setData(0, ROLE_SOLVED, solved)
        it.setData(0, ROLE_LOCKED, self._is_locked(p))
        it.setForeground(0, QColor(FG))

    def _is_locked(self, p):
        """현재 해금된 랭크보다 높은 랭크의 문제는 잠김(설정 '랭크 잠금 해제' 시 항상 풀림)."""
        if self.settings.get_bool("rank_unlock"):
            return False
        try:
            return profile.RANK_ORDER.index(p.rank) > self._unlocked_index
        except (ValueError, AttributeError):
            return False

    def _refresh_all_items(self):
        for p in self._all_problems:
            self._refresh_item(p)

    def _blocked_locked(self, p):
        """잠긴(상위 랭크) 문제면 안내 후 True. 풀 수 있으면 False."""
        if not self._is_locked(p):
            return False
        need = profile.RANK_KR.get(p.rank, p.rank)
        cur = profile.RANK_KR[profile.RANK_ORDER[self._unlocked_index]]
        self.out.clear()
        self._append(f"🔒 아직 잠긴 문제예요 — {need} 랭크에 도달해야 풀 수 있어요. (현재 해금: {cur})\n", ORANGE)
        self._append("  더 낮은 랭크 문제를 풀어 경험치를 올리면 해금됩니다.\n"
                     "  (설정 → 풀이/학습 → '랭크 잠금 해제'를 켜면 바로 풀 수 있어요)\n", COMMENT)
        self._set_status("🔒 잠김 — 랭크업 필요", ORANGE)
        return True

    def _add_problem(self, parent, p):
        solved = p.id in self.solved
        it = QTreeWidgetItem(parent, [""])
        self._apply_item_style(it, p, solved)
        it.setData(0, Qt.UserRole, p.id)
        self.item_problem[id(it)] = p
        self.problem_item.setdefault(p.id, []).append(it)   # 같은 문제가 여러 섹션에 나옴

    def _refresh_item(self, p):
        solved = p.id in self.solved
        for it in self.problem_item.get(p.id, []):
            self._apply_item_style(it, p, solved)

    def _apply_search(self):
        """검색어로 트리 필터(디바운싱). 그룹은 하위에 매칭이 있으면 펼쳐서 보여준다."""
        q = self.search_box.text().strip().lower()

        def visit(item):
            if item.childCount() > 0:
                child_match = False
                for i in range(item.childCount()):
                    if visit(item.child(i)):
                        child_match = True
                vis = child_match or (q in item.text(0).lower())
                item.setHidden(bool(q) and not vis)
                if q and child_match:
                    item.setExpanded(True)
                return vis
            match = (not q) or (q in item.text(0).lower())
            item.setHidden(not match)
            return match

        for i in range(self.tree.topLevelItemCount()):
            visit(self.tree.topLevelItem(i))

    # ───────────────────────── 동작 ─────────────────────────

    def _set_lang(self, code):
        if self.current:
            self._save_editor()
        self.lang = code
        if self.current:
            self._load_editor()

    def on_tree_select(self, cur, prev):
        if cur is None:
            return
        if self._mode == "problem" and self.current:
            self._save_editor()
        self.next_btn.setVisible(False)
        self._cur_item = cur
        preset = self.item_exam.get(id(cur))
        if preset is not None:
            self._start_exam(preset)
            return
        lv = self.item_vocab.get(id(cur))
        if lv is not None:
            self._open_vocab(lv)
            return
        les = self.item_lesson.get(id(cur))
        if les is not None:
            self._open_lesson(les)
            return
        p = self.item_problem.get(id(cur))
        if p is None:
            return
        self._mode = "problem"
        self.current_lesson = None
        self.current = p
        self._cur_active = self._apply_variant(p)
        self._reveal = 0          # 새 문제 → 힌트 숨김 상태로
        self._show_code_panel(True)
        if self._hidden_mode:
            self._apply_hide_visibility()       # 문제 모드: 설명 숨기고 코딩+터미널
        self._update_lang_buttons_for(p)        # func 문제면 Python 외 언어 잠금
        self._render_problem(self._cur_active)
        self._load_editor()
        self._prefill_stdin(self._cur_active)
        self.out.clear()

    def _next_sibling_problem(self):
        it = getattr(self, "_cur_item", None)
        if it is None:
            return None
        parent = it.parent()
        if parent is None:
            return None
        idx = parent.indexOfChild(it)
        for j in range(idx + 1, parent.childCount()):
            nxt = parent.child(j)
            if id(nxt) in self.item_problem:
                return nxt
        return None

    def _has_next_problem(self):
        return self._mode == "problem" and self._next_sibling_problem() is not None

    def _next_problem(self):
        nxt = self._next_sibling_problem()
        if nxt is not None:
            self.tree.setCurrentItem(nxt)   # → on_tree_select 로 로드

    # ───────────────────────── 학습(레슨) ─────────────────────────

    def _sync_lang_buttons(self):
        for code, b in self.lang_buttons.items():
            b.setChecked(code == self.lang)

    def _update_lang_buttons_for(self, p):
        """함수 구현형(func) 문제는 Python 전용 — 다른 언어 버튼을 잠가 헛수고를 막는다.
        (레슨의 전체 잠금 등 이전 모드 상태도 여기서 복구)"""
        is_func = getattr(p, "type", "") == "func"
        for code, b in self.lang_buttons.items():
            if code == "python":
                b.setEnabled(True)          # 이전 모드(레슨 등)에서 잠긴 상태 복구
                b.setToolTip("")
                continue
            b.setEnabled(not is_func)
            b.setToolTip("함수 구현형 문제는 Python 으로만 채점됩니다." if is_func else "")
        if is_func and self.lang != "python":
            self.lang = "python"
            self._sync_lang_buttons()

    def _open_lesson(self, les):
        self._mode = "lesson"
        self.current_lesson = les
        self.current = None
        self._cur_active = None
        self._show_code_panel(True)
        self._render_lesson(les)
        self.out.clear()
        ext_map = {"python": "py", "java": "java", "cpp": "cpp", "javascript": "js",
                   "css": "css", "scss": "scss"}
        lang = les.lang if les.lang in ext_map else "python"
        self.lang = lang
        self._sync_lang_buttons()
        # 레슨은 예시 코드의 언어로만 실행 — 언어 전환 잠금 (코드/언어 불일치 방지)
        for _b in self.lang_buttons.values():
            _b.setEnabled(False)
            _b.setToolTip("레슨은 예시 코드의 언어로 실행됩니다")
        self.stdin_box.clear()                  # 이전 문제의 입력 잔존 제거
        self.editor.set_code(les.code or "", lang if lang in ("python", "java", "cpp", "javascript") else "python")
        self.file_label.setText(f"{les.id}.{ext_map[lang]}")
        if les.lang == "guide" or not les.code:
            self._set_status("가이드 · 읽기", COMMENT)
        else:
            self._set_status("학습 · Run 으로 실행", CYAN)

    def _render_lesson(self, l):
        def esc(s):
            return html.escape(str(s)).replace("\n", "<br>")

        def sec(t):
            return f"<div style='color:{CYAN};font-size:13px;font-weight:bold;margin:14px 0 4px;'>{t}</div>"

        kr = {"python": "Python", "java": "Java", "cpp": "C++", "guide": "가이드"}.get(l.lang, l.lang)
        h = [f"<div style='font-family:Segoe UI;color:{FG};font-size:13px;line-height:1.6;'>"]
        h.append(f"<div style='color:{PURPLE};font-size:18px;font-weight:bold;'>{esc(l.title)}</div>")
        h.append(f"<div style='color:{COMMENT};font-size:11px;margin-top:3px;'>{kr} · {esc(l.level)}</div>")
        if l.summary:
            h.append(f"<div style='color:{CYAN};margin-top:5px;'>{esc(l.summary)}</div>")
        if l.usage:
            h.append(sec("어디에 · 어떻게 쓰나") + f"<div style='color:{GREEN};'>{esc(l.usage)}</div>")
        if l.cons:
            h.append(sec("단점 · 주의점") + f"<div style='color:{ORANGE};'>{esc(l.cons)}</div>")
        if l.code:
            h.append(sec("예시 코드"))
            h.append(f"<pre style='background:{CARD};color:{YELLOW};padding:8px 10px;"
                     f"border:1px solid {BORDER};border-radius:6px;"
                     f"font-family:{MONO_FAMILY};font-size:12px;white-space:pre-wrap;'>"
                     f"{html.escape(l.code.rstrip())}</pre>")
            if l.lang in ("python", "java", "cpp"):
                h.append(f"<div style='color:{COMMENT};font-size:11px;margin-top:4px;'>"
                         f"→ 아래 console 에 코드가 올라가 있어요. Run(F5) 으로 직접 실행해 보세요.</div>")
        # 상세 설명은 최하단에 배치 — 더 알고 싶은 사람만 스크롤해서 읽도록
        if l.explanation:
            h.append(f"<div style='border-top:1px solid {BORDER};margin:24px 0 0;'></div>")
            h.append(sec("상세 설명 (더 알고 싶다면 ↓)"))
            h.append(self._format_explanation(l.explanation))
        h.append("</div>")
        self._show_html(h)

    @staticmethod
    def _format_explanation(text):
        """상세 설명(explanation)을 읽기 좋게 HTML 로 변환.

        [섹션] 줄은 구분 박스로, • 불릿은 들여쓰기로, 'code → 해설' 줄은
        고정폭+색 구분으로 렌더링해 통짜 텍스트의 가독성 문제를 해소한다."""
        out = []
        for raw in str(text).split("\n"):
            line = raw.rstrip()
            s = line.strip()
            if not s:                                    # 빈 줄 → 여백
                out.append("<div style='height:7px;'></div>")
                continue
            if s.startswith("[") and s.endswith("]"):    # [개요] 같은 섹션 헤더
                out.append(
                    f"<div style='color:{PURPLE};font-weight:bold;font-size:13px;"
                    f"margin:14px 0 6px;padding:4px 10px;background:{CARD};"
                    f"border-left:3px solid {PURPLE};border-radius:3px;'>"
                    f"{html.escape(s[1:-1])}</div>")
                continue
            if s.startswith("•"):                        # 불릿 항목
                out.append(
                    f"<div style='margin:2px 0 2px 12px;'>"
                    f"<span style='color:{CYAN};'>•</span> "
                    f"{html.escape(s[1:].strip())}</div>")
                continue
            if "→" in line:                              # 코드 → 해설 줄
                code_part, _, desc = html.escape(line).partition("→")
                out.append(
                    f"<div style='font-family:{MONO_FAMILY};font-size:12px;"
                    f"margin:1px 0 1px 12px;white-space:pre-wrap;'>"
                    f"<span style='color:{YELLOW};'>{code_part.rstrip()}</span>"
                    f"<span style='color:{COMMENT};'> → </span>"
                    f"<span style='color:{FG};'>{desc.strip()}</span></div>")
                continue
            if line.startswith("      "):                # 깊은 들여쓰기 → 해설 연속 줄
                out.append(
                    f"<div style='font-family:{MONO_FAMILY};font-size:12px;color:{COMMENT};"
                    f"margin:1px 0 1px 12px;white-space:pre-wrap;'>{html.escape(line)}</div>")
                continue
            out.append(f"<div style='margin:2px 0;white-space:pre-wrap;'>{html.escape(line)}</div>")
        return "".join(out)

    def _run_lesson(self):
        l = self.current_lesson
        if l is None or not self.editor.toPlainText().strip():
            self.out.clear()
            self._append("이 항목은 읽기 전용입니다(실행할 코드가 없어요).\n", COMMENT)
            return
        # CSS: 그대로 보여줌 / SCSS: CSS 로 컴파일해서 보여줌
        if l.lang == "css":
            self.out.clear()
            self._append("/* CSS — 그대로 적용되는 스타일 */\n", COMMENT)
            self._append(self.editor.toPlainText() + "\n", FG)
            self._set_status("css", GREEN)
            return
        if l.lang == "scss":
            self.out.clear()
            self._append("$ sass  (SCSS → CSS)\n", CYAN)
            ok, css, err = runner.run_scss(self.editor.toPlainText())
            if ok:
                self._append(css + "\n", FG)
                self._set_status("compiled", GREEN)
            else:
                self._append((err or "컴파일 실패") + "\n", RED)
                self._set_status("error", RED)
            return
        if l.lang not in ("python", "java", "cpp", "javascript"):
            self.out.clear()
            self._append("실행할 수 없는 항목입니다.\n", COMMENT)
            return
        lang = self.lang
        if not runner.compiler_available(lang):
            self.out.clear()
            self._append(f"{runner.LANGUAGES[lang]['name']} toolchain not found.\n", ORANGE)
            self._append("  (guide 섹션의 설치 안내 참고)\n", COMMENT)
            return
        path = SOLUTIONS_DIR / "_lesson" / l.id / runner.LANGUAGES[lang]["filename"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(self.editor.toPlainText(), encoding="utf-8")
        self.out.clear()
        self._append(f"$ run {runner.LANGUAGES[lang]['name']}\n", CYAN)
        self._set_status("running…", YELLOW)
        self.run_btn.setEnabled(False)
        # 입력칸(stdin) 내용을 레슨 실행에도 전달 — input()/Scanner 예시 코드 대응
        stdin_text = self.stdin_box.toPlainText()
        if stdin_text.strip():
            self._append(f"  stdin> {stdin_text.strip()}\n", COMMENT)
        th = RunThread(lang, path, stdin=stdin_text)
        th.done.connect(self._on_lesson_done)
        th.finished.connect(lambda t=th: self._threads.remove(t) if t in self._threads else None)
        self._threads.append(th)
        th.start()

    def _on_lesson_done(self, payload):
        self.run_btn.setEnabled(True)
        kind, data = payload
        if kind == "CE":
            self._append("\n✗ BUILD ERR\n", RED, bold=True)
            self._append(str(data) + "\n", RED)
            self._set_status("build err", RED)
            return
        r = data
        if r.stdout:
            self._append(r.stdout if r.stdout.endswith("\n") else r.stdout + "\n", FG)
        if r.stderr:
            self._append(r.stderr + "\n", RED)
        self._append(f"\n[exit {r.returncode}]  ⏱ {r.time_ms:.0f}ms\n", COMMENT)
        self._set_status("done" if r.returncode == 0 else "error", GREEN if r.returncode == 0 else RED)
        # 실행만 한 것 — 다음 단계(채점) 안내로 초보자 혼동 방지
        if self._mode == "problem" and r.returncode == 0:
            self._append("  → 정답 판정을 받으려면 상단 '제출' (Ctrl+Enter)\n", CYAN)

    # ───────────────────────── 영단어 ─────────────────────────

    def _show_code_panel(self, visible):
        """영단어 학습 중엔 코드 에디터+터미널(우측)을 숨기고 단어 카드만 본다."""
        self._blur_content(False)
        if hasattr(self, "right_stack"):
            self.right_stack.setCurrentWidget(self.right)
            self.right_stack.setVisible(visible)

    def _blur_content(self, on):
        """가운데 문제/단어 카드에 블러 효과(타이핑 암기 인라인 시 뒤를 흐리게)."""
        if not hasattr(self, "content"):
            return
        if on:
            eff = QGraphicsBlurEffect(self)
            eff.setBlurRadius(8)
            self.content.setGraphicsEffect(eff)
        else:
            self.content.setGraphicsEffect(None)

    def _end_inline_typing(self):
        self._blur_content(False)
        self.right_stack.setCurrentWidget(self.right)
        self.right_stack.setVisible(False)
        if self._mode == "vocab":
            self._render_vocab(self.vocab_entry)
            self._set_status("단어 학습 · Run → 타이핑 암기 · 우클릭 → 퀴즈/오답 복습", CYAN)

    def _open_vocab(self, entry):
        self._mode = "vocab"
        self.vocab_entry = entry
        self.vocab_level = entry["level"]
        self.vocab_words = entry["words"]
        self.current = None
        self.current_lesson = None
        self._update_lang_buttons_for(None)     # 이전 모드의 언어 버튼 잠금 해제
        self.stdin_box.clear()                  # 이전 문제의 입력 잔존 제거
        self._show_code_panel(False)            # 에디터·터미널 숨김
        if self._hidden_mode:
            self._apply_hide_visibility()       # 하이드 중이면 단어 카드는 보이게
        self._render_vocab(entry)
        self.out.clear()
        self._set_status("단어 학습 · Run → 타이핑 암기 · 우클릭 → 퀴즈/오답 복습", CYAN)

    def _render_vocab(self, entry):
        words = entry["words"]
        title = entry.get("title", entry["level"])
        known = self.vocab_db.known_set()
        st = self.vocab_db.stats()
        h = [f"<div style='font-family:Segoe UI;color:{FG};font-size:13px;line-height:1.5;'>"]
        h.append(f"<div style='color:{PURPLE};font-size:18px;font-weight:bold;'>영단어 · {html.escape(title)} "
                 f"<span style='color:{COMMENT};font-size:12px;'>({len(words)}개)</span></div>")
        wrong = self.vocab_db.wrong_set()
        n_wrong = sum(1 for w in words if w.word in wrong)
        wrong_html = (f" · <span style='color:{ORANGE};'>이 묶음 복습할 오답 {n_wrong}개</span>"
                      if n_wrong else "")
        h.append(f"<div style='color:{COMMENT};font-size:11px;'>누적 — 정답 {st['correct']} · 오답 {st['wrong']} · 외운 단어 {st['known']}{wrong_html}</div>")
        h.append(f"<div style='color:{GREEN};font-size:11px;margin-bottom:8px;'>"
                 f"▶ Run → 깜빡임 암기 · 우클릭 → 깜빡임 암기 / 문장 완성 / 객관식 / 🔁 오답 복습</div>")
        DISPLAY_CAP = 120
        for w in words[:DISPLAY_CAP]:
            mark = " ✅" if w.word in known else ""
            pkr = pos_kr(w.pos)
            pos_html = (f" <span style='color:{COMMENT};font-size:11px;'>[{html.escape(pkr)}]</span>"
                        if pkr else "")
            h.append(f"<div style='margin:7px 0;border-left:2px solid {CUR};padding-left:8px;'>"
                     f"<b style='color:{CYAN};font-size:15px;'>{html.escape(w.word)}</b>{pos_html}{mark}<br>"
                     f"<span style='color:{FG};'>뜻: {html.escape(w.meaning)}</span>")
            if w.example:
                h.append(f"<br><span style='color:{YELLOW};font-family:{MONO_FAMILY};font-size:12px;'>예: {html.escape(w.example)}</span>")
                if w.example_kr:
                    h.append(f"<br><span style='color:{COMMENT};font-size:12px;'>{html.escape(w.example_kr)}</span>")
            h.append("</div>")
        if len(words) > DISPLAY_CAP:
            h.append(f"<div style='color:{COMMENT};margin-top:10px;'>… 외 {len(words) - DISPLAY_CAP}개 "
                     f"— Run/우클릭으로 이 묶음 전체에서 무작위로 테스트됩니다.</div>")
        h.append("</div>")
        self._show_html(h)

    def _vocab_quiz(self):
        words = getattr(self, "vocab_words", None) or vocab.BY_LEVEL.get(self.vocab_level, [])
        if len(words) < 4:
            self._set_status("퀴즈를 보려면 단어가 더 필요합니다", ORANGE)
            return
        n = self.settings.get_int("quiz_size", 10)
        quiz = weighted_pick(words, min(n, len(words)), db=self.vocab_db)   # 오답 우선
        QuizDialog(self, quiz, words, self.vocab_db).exec()
        self._render_vocab(self.vocab_entry)

    def _vocab_typing(self):
        """메인창: 가운데 단어 카드를 블러 처리하고 우측에 타이핑 암기 카드를 띄워 진행."""
        words = getattr(self, "vocab_words", None) or vocab.BY_LEVEL.get(self.vocab_level, [])
        if not words:
            self._set_status("단어가 없습니다", ORANGE)
            return
        self._blur_content(True)
        self.right_stack.setCurrentWidget(self.typing_widget)
        self.right_stack.setVisible(True)
        self.typing_widget.start(words, self.vocab_db)
        self._set_status("깜빡임 암기 중 — 단어 깜빡 후 입력 · '그만하기'로 결과", CYAN)

    def _vocab_sentence(self):
        """문장 완성 — 가운데 단어 카드 블러 + 우측에 문장 완성 카드."""
        words = getattr(self, "vocab_words", None) or vocab.BY_LEVEL.get(self.vocab_level, [])
        if not words:
            self._set_status("단어가 없습니다", ORANGE)
            return
        self._blur_content(True)
        self.right_stack.setCurrentWidget(self.sentence_widget)
        self.right_stack.setVisible(True)
        self.sentence_widget.start(words, self.vocab_db)
        self._set_status("문장 완성 중 — 빈칸에 단어 입력 후 Enter", CYAN)

    def _vocab_review(self):
        """오답 복습 — 이 묶음에서 틀린 적 있는(아직 못 외운) 단어만 다시 암기."""
        words = getattr(self, "vocab_words", None) or vocab.BY_LEVEL.get(self.vocab_level, [])
        wrong = self.vocab_db.wrong_set()
        review = [w for w in words if w.word in wrong]
        if not review:
            self._set_status("복습할 오답 단어가 없어요 — 먼저 암기/퀴즈를 해보세요", ORANGE)
            return
        self._blur_content(True)
        self.right_stack.setCurrentWidget(self.typing_widget)
        self.right_stack.setVisible(True)
        self.typing_widget.start(review, self.vocab_db)
        self._set_status(f"오답 복습 중 — 틀린 단어 {len(review)}개만 다시!", CYAN)

    # ───────────────────────── 실전 모의고사 ─────────────────────────

    def _confirm(self, msg):
        return QMessageBox.question(self, "확인", msg,
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No) == QMessageBox.Yes

    def _clear_exam_group(self):
        if not self.exam or not self.exam.get("group"):
            return
        grp = self.exam["group"]
        for i in range(grp.childCount()):
            child = grp.child(i)
            p = self.item_problem.pop(id(child), None)
            if p:
                self.problem_item[p.id] = [it for it in self.problem_item.get(p.id, []) if it is not child]
        idx = self.tree.indexOfTopLevelItem(grp)
        if idx >= 0:
            self.tree.takeTopLevelItem(idx)

    def _start_exam(self, preset):
        # 확인(모달) 후 시작 — 누르자마자 자동 시작 X
        msg = (f"[{preset['title']}]\n\n{preset['desc']}\n\n"
               f"제한시간 {preset['minutes']}분 · 합격: 총 배점의 {int(preset.get('pass_ratio', 0.55) * 100)}% 이상.\n"
               "(난이도가 높은 문제일수록 배점이 큽니다 · 플래티넘 1~2문제 포함)\n"
               "시험을 시작하시겠습니까? (시작하면 문제가 출제됩니다)")
        if self.exam:
            msg = "진행 중인 시험을 끝내고 새로 시작할까요?"
        if not self._confirm(msg):
            return
        if self.exam:
            self.exam_timer.stop()
            self._clear_exam_group()
            self.exam = None
        seed = random.randrange(1, 10 ** 9)
        probs = exam.assemble(preset, seed, self._all_problems)
        grp = self._group_item(self.tree, f"▶ 시험 진행중 ({len(probs)}문제)", top=True)
        for p in probs:
            self._add_problem(grp, p)
        grp.setExpanded(True)
        self.exam = {
            "preset": preset, "problems": probs, "ids": {p.id for p in probs},
            "solved": set(), "deadline": time.time() + preset["minutes"] * 60, "group": grp,
        }
        self.exam_label.setVisible(True)
        self.exam_end_btn.setVisible(True)
        self.giveup_btn.setVisible(True)
        self.exam_timer.start()
        self._tick_exam()
        self._mode = "problem"
        self.current = None
        self._update_lang_buttons_for(None)     # 이전 모드의 언어 버튼 잠금 해제
        self._show_code_panel(True)
        self._render_exam_dashboard()
        self._set_status("시험 시작! 사이드바 '▶ 시험 진행중'에서 문제를 푸세요", CYAN)

    def _giveup_exam(self):
        if not self.exam:
            return
        if not self._confirm("시험을 포기할까요? (채점 없이 종료됩니다)"):
            return
        self.exam_timer.stop()
        self.exam_label.setVisible(False)
        self.exam_end_btn.setVisible(False)
        self.giveup_btn.setVisible(False)
        self._clear_exam_group()
        self.exam = None
        self.out.clear()
        self._append("시험을 포기했습니다.\n", COMMENT)
        self._set_status("시험 포기", COMMENT)

    def _tick_exam(self):
        if not self.exam:
            return
        try:
            rem = int(self.exam["deadline"] - time.time())
            if rem <= 0:
                self.exam_label.setText("⏳ 00:00")
                self._submit_exam(auto=True)
                return
            m, s = divmod(rem, 60)
            n, tot = len(self.exam["solved"]), len(self.exam["problems"])
            self.exam_label.setText(f"⏳ {m:02d}:{s:02d}  ·  {n}/{tot}")
        except Exception:
            # 1초 반복 타이머에서 예외가 반복 폭주하지 않도록 정지
            self.exam_timer.stop()
            import traceback
            traceback.print_exc()

    def _render_exam_dashboard(self):
        ex = self.exam
        preset = ex["preset"]

        def sec(t):
            return f"<div style='color:{CYAN};font-size:13px;font-weight:bold;margin:12px 0 4px;'>{t}</div>"

        h = [f"<div style='font-family:Segoe UI;color:{FG};font-size:13px;line-height:1.6;'>"]
        h.append(f"<div style='color:{PURPLE};font-size:18px;font-weight:bold;'>📝 {html.escape(preset['title'])}</div>")
        h.append(f"<div style='color:{COMMENT};font-size:12px;margin-top:3px;'>{html.escape(preset['desc'])}</div>")
        need_score = exam.pass_score(preset, ex["problems"])
        total_score = sum(profile.problem_points(p) for p in ex["problems"])
        got_score = sum(profile.problem_points(p) for p in ex["problems"] if p.id in ex["solved"])
        h.append(f"<div style='color:{ORANGE};font-weight:bold;margin-top:5px;'>"
                 f"제한시간 {preset['minutes']}분 · 합격 {need_score}점 이상 / 총 {total_score}점"
                 f" · 현재 {got_score}점</div>")
        h.append(sec("출제 문제 (난이도 높을수록 배점↑)"))
        for i, p in enumerate(ex["problems"], 1):
            done = p.id in ex["solved"]
            mark = "✅" if done else "⬜"
            tier = p.tier or p.rank[0]
            pts = profile.problem_points(p)
            h.append(f"<div style='margin:3px 0;'>{mark} {i}. {html.escape(p.title)} "
                     f"<span style='color:{COMMENT};'>[{tier} · {pts}점]</span></div>")
        h.append(f"<div style='color:{COMMENT};margin-top:12px;'>← 사이드바 '▶ 시험' 그룹에서 문제를 골라 풀고, "
                 f"상단 <b>제출</b> 로 채점하세요. 시간이 끝나면 자동 채점됩니다.</div>")
        h.append("</div>")
        self._show_html(h)

    def _submit_exam(self, auto=False):
        if not self.exam:
            return
        self.exam_timer.stop()
        ex = self.exam
        preset = ex["preset"]
        res = exam.grade(preset, ex["problems"], ex["solved"])
        title = "합격 🎉" if res["passed"] else "불합격 😢"
        color = GREEN if res["passed"] else RED

        self.out.clear()
        self._append("== 모의고사 결과 ==\n", CYAN, bold=True)
        if auto:
            self._append("(시간 종료 · 자동 채점)\n", COMMENT)
        for p in ex["problems"]:
            ok = p.id in ex["solved"]
            self._append(f"  {'✓' if ok else '✗'} {p.title}\n", GREEN if ok else RED)
        self._append(f"\n  {title}   점수 {res['got_score']}/{res['total_score']} "
                     f"(합격 {res['need_score']}점 이상)  ·  {res['n_solved']}/{res['n_total']}문제 정답\n",
                     color, bold=True)
        self._set_status(title, color)

        # 대시보드도 결과로 갱신
        self._render_exam_dashboard()
        # 정리
        self.exam_label.setVisible(False)
        self.exam_end_btn.setVisible(False)
        self.giveup_btn.setVisible(False)
        self._clear_exam_group()
        self.exam = None

    def _sol_path(self, p, lang):
        return SOLUTIONS_DIR / p.id / runner.LANGUAGES[lang]["filename"]

    def _template(self, p, lang):
        if lang == "python":
            return p.template_py or "def solution():\n    pass\n"
        if lang == "java":
            return ("import java.util.*;\nimport java.io.*;\n\n"
                    "public class Main {\n"
                    "    public static void main(String[] args) throws IOException {\n"
                    "        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n"
                    "        // TODO: 표준입력을 읽고 정답을 표준출력으로 출력하세요.\n"
                    "    }\n}\n")
        if lang == "cpp":
            return ("#include <bits/stdc++.h>\nusing namespace std;\n\n"
                    "int main() {\n"
                    "    ios_base::sync_with_stdio(false);\n    cin.tie(nullptr);\n"
                    "    // TODO: 표준입력을 읽고 정답을 표준출력으로 출력하세요.\n"
                    "    return 0;\n}\n")
        if lang == "javascript":
            return ("// 표준입력 전체 읽기 (Node.js)\n"
                    "const data = require('fs').readFileSync(0, 'utf8').trim();\n"
                    "const lines = data.split('\\n');\n"
                    "// TODO: lines 로 입력을 읽고 console.log 로 출력하세요.\n")
        return ""

    def _load_editor(self):
        p = self.current
        path = self._sol_path(p, self.lang)
        try:
            code = (path.read_text(encoding="utf-8", errors="replace")
                    if path.exists() else self._template(p, self.lang))
        except OSError:
            code = self._template(p, self.lang)
        self.editor.set_code(code, self.lang)
        self.file_label.setText(runner.LANGUAGES[self.lang]["filename"])
        if p.type == "func" and self.lang != "python":
            self._set_status("fn: python only", ORANGE)
        else:
            self._set_status("ready", COMMENT)

    def _save_editor(self, force=False):
        if not self.current:
            return
        try:
            path = self._sol_path(self.current, self.lang)
            text = self.editor.toPlainText()
            # 손대지 않은 템플릿 그대로면 폴더/파일을 만들지 않는다
            # (문제를 구경만 해도 solutions/ 에 폴더가 쌓이는 문제 방지)
            if not force and not path.exists() \
                    and text == self._template(self.current, self.lang):
                return
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        except OSError as e:
            self._set_status(f"저장 실패: {e}", RED)

    def _prefill_stdin(self, p):
        """문제 선택 시 입력(stdin) 칸에 첫 예제를 미리 채운다.
        표준입력형=예제 입력, 함수형=예제 호출식(수정해서 Run 가능)."""
        ptype = getattr(p, "type", "")
        if ptype == "stdin" and p.examples:
            self.stdin_box.setPlainText(str(p.examples[0].get("input", "")).rstrip())
        elif ptype == "func" and p.examples:
            args = p.examples[0].get("args", [])
            self.stdin_box.setPlainText(f"{p.func_name}({', '.join(map(repr, args))})")
        else:
            self.stdin_box.clear()

    @staticmethod
    def _parse_func_args(p, text):
        """입력칸 텍스트 → 함수 인자 리스트.
        비어 있으면 None(예제 인자 사용), 해석 불가면 "ERROR".
        허용 형식: 6 · 1, 2 · [1, 2], "abc" · solution(6) 같은 호출식."""
        import ast
        import json
        s = (text or "").strip()
        if not s:
            return None
        m = re.match(r"^\w+\s*\((.*)\)\s*$", s, re.S)   # solution(...) 껍데기 벗기기
        if m:
            s = m.group(1).strip()
            if not s:
                return []
        try:
            val = ast.literal_eval(f"({s},)")
            args = [list(a) if isinstance(a, tuple) else a for a in val]
            json.dumps(args)                             # 하니스 전달 가능 여부 확인
            return args
        except Exception:
            return "ERROR"

    def _set_status(self, text, color):
        self.status.setText(text)
        self.status.setStyleSheet(f"color:{color};")

    # 문제 렌더링 (네이티브 위젯)
    def _render_problem(self, p):
        self.content.setCurrentWidget(self.prob_view)
        v = self.prob_view
        v.clear()

        # 위장: 랭크 이니셜/티어 + 주제만. 출처(style)·BOJ·'코딩테스트' 단어 제거
        meta = [m for m in (p.tier or RANK_INITIAL.get(p.rank, p.rank), p.topic) if m]
        io = "stdin · stdout" if p.type == "stdin" else f"fn {p.func_name}()"
        langs = "py · java · cpp · js" if p.type == "stdin" else "py"

        def section(title):
            v.add(make_label(title, CYAN, 13, bold=True), top=10)

        v.add(make_label(p.title, PURPLE, 18, bold=True))
        v.add(make_label(" · ".join(str(m) for m in meta), COMMENT, 11))
        v.add(make_label(f"{io}  ·  {langs}", COMMENT, 11))
        if self._is_locked(p):
            cur = profile.RANK_KR[profile.RANK_ORDER[self._unlocked_index]]
            v.add(make_label(f"🔒 잠긴 문제 — {profile.RANK_KR.get(p.rank, p.rank)} 랭크 도달 시 풀 수 있어요 "
                             f"(현재 해금: {cur} · 설정에서 잠금 해제 가능)", ORANGE, 12, bold=True), top=6)

        # 제한 — ⏱ 시간 / 💾 메모리
        lim = QWidget()
        lim.setStyleSheet("background:transparent;")
        lh = QHBoxLayout(lim)
        lh.setContentsMargins(0, 3, 0, 0)
        lh.setSpacing(4)
        for w in (make_label("⏱", ORANGE, 11, wrap=False), make_label("시간", COMMENT, 11, wrap=False),
                  make_label(f"{p.time_limit_ms}ms", FG, 11, bold=True, wrap=False)):
            lh.addWidget(w)
        lh.addSpacing(14)
        for w in (make_label("💾", CYAN, 11, wrap=False), make_label("메모리", COMMENT, 11, wrap=False),
                  make_label(f"{p.memory_limit_mb}MB", FG, 11, bold=True, wrap=False)):
            lh.addWidget(w)
        lh.addStretch(1)
        v.add(lim)

        section("Description")
        v.add(make_label(p.description, FG, 13))
        if p.input_desc:
            section("Input")
            v.add(make_label(p.input_desc, FG, 13))
        if p.output_desc:
            section("Output")
            v.add(make_label(p.output_desc, FG, 13))

        section("Examples")
        for i, ex in enumerate(p.examples, 1):
            if p.type == "stdin":
                v.add(make_label(f"in {i}", COMMENT, 11))
                v.add(make_codebox(ex["input"]))
                v.add(make_label(f"out {i}", COMMENT, 11))
                v.add(make_codebox(ex["output"]))
            else:
                args_repr = ", ".join(repr(a) for a in ex["args"])
                v.add(make_codebox(f"{p.func_name}({args_repr})  ->  {ex['output']!r}"))

        # 힌트 — 우클릭으로 단계별 공개(누적), 스크롤해서 봄
        rv = self._reveal
        if rv >= 1:
            names = ["접근 방향", "자료구조 · 알고리즘", "거의 정답"]
            section("힌트")
            for i in range(min(rv, 3)):
                if i < len(p.hints):
                    v.add(make_label(f"힌트 {i+1} · {names[i]}", PURPLE, 13, bold=True), top=6)
                    v.add(make_label(p.hints[i], FG, 13))
        if rv >= 4:
            lang = self.lang
            sol = {"python": p.reference_py, "java": p.reference_java, "cpp": p.reference_cpp}[lang]
            if not sol.strip():
                lang, sol = "python", p.reference_py
            section("풀이 · 정답 코드")
            v.add(make_label(f"힌트 1→2→3이 ‘접근 → 알고리즘 → 핵심 구현’ 풀이이고, "
                             f"아래가 가장 정석적인 정답 코드입니다 ({runner.LANGUAGES[lang]['name']}).",
                             COMMENT, 11))
            v.add(make_codebox(sol))

    # 출력
    def _append(self, text, color=FG, bold=False):
        cur = self.out.textCursor()
        cur.movePosition(QTextCursor.End)
        fmt = QTextCharFormat()
        fmt.setForeground(QColor(color))
        if bold:
            fmt.setFontWeight(QFont.Bold)
        cur.insertText(text, fmt)
        self.out.setTextCursor(cur)
        self.out.ensureCursorVisible()

    # 힌트 / 정답
    def _reveal_hint(self, level):
        if not self.current:
            return
        self._reveal = max(self._reveal, level)
        self._render_problem(self._cur_active or self.current)
        QTimer.singleShot(0, self._scroll_prob_bottom)

    def _show_html(self, h):
        """HTML 화면(레슨/가이드/시험/영단어)으로 전환 + 내용 표시."""
        self.content.setCurrentWidget(self.prob)
        self.prob.setHtml("".join(h))

    def _scroll_prob_bottom(self):
        sb = self.prob_view.verticalScrollBar()
        sb.setValue(sb.maximum())

    def _tree_menu(self, pos):
        """사이드바 트리 우클릭 — 문제 항목이면 힌트/정답/풀이 폴더 바로가기."""
        it = self.tree.itemAt(pos)
        if it is None:
            return
        p = self.item_problem.get(id(it))
        if p is None:
            return
        m = QMenu(self.tree)
        a_h1 = m.addAction("힌트 1  ·  접근 방향")
        a_h2 = m.addAction("힌트 2  ·  자료구조 / 알고리즘")
        a_h3 = m.addAction("힌트 3  ·  거의 정답")
        a_ref = m.addAction("힌트 last  ·  정답 코드 + 풀이")
        m.addSeparator()
        sol_dir = SOLUTIONS_DIR / p.id
        a_dir = m.addAction("📁 풀이 폴더 열기")
        a_dir.setEnabled(sol_dir.exists())
        act = m.exec(self.tree.viewport().mapToGlobal(pos))
        if act is None:
            return
        self.tree.setCurrentItem(it)            # 선택 → 문제 로드 후 동작
        if act == a_h1:
            self._reveal_hint(1)
        elif act == a_h2:
            self._reveal_hint(2)
        elif act == a_h3:
            self._reveal_hint(3)
        elif act == a_ref:
            self._reveal_hint(4)
        elif act == a_dir:
            try:
                os.startfile(str(sol_dir))
            except OSError as e:
                self._set_status(f"폴더 열기 실패: {e}", RED)

    def _prob_menu(self, pos, widget=None):
        widget = widget or self.prob
        if self._mode == "vocab":
            m = QMenu(widget)
            a_type = m.addAction("깜빡임 암기 (단어 깜빡 → 입력)")
            a_sent = m.addAction("문장 완성 (빈칸 채우기)")
            a_quiz = m.addAction("객관식 퀴즈")
            m.addSeparator()
            a_rev = m.addAction("🔁 오답 복습 — 틀린 단어만 다시")
            act = m.exec(widget.mapToGlobal(pos))
            if act == a_type:
                self._vocab_typing()
            elif act == a_sent:
                self._vocab_sentence()
            elif act == a_quiz:
                self._vocab_quiz()
            elif act == a_rev:
                self._vocab_review()
            return
        if not self.current:
            return
        m = QMenu(widget)
        a1 = m.addAction("힌트 1  ·  접근 방향")
        a2 = m.addAction("힌트 2  ·  자료구조 / 알고리즘")
        a3 = m.addAction("힌트 3  ·  거의 정답")
        m.addSeparator()
        al = m.addAction("힌트 last  ·  정답 코드 + 풀이")
        act = m.exec(widget.mapToGlobal(pos))
        if act == a1:
            self._reveal_hint(1)
        elif act == a2:
            self._reveal_hint(2)
        elif act == a3:
            self._reveal_hint(3)
        elif act == al:
            self._reveal_hint(4)

    def on_reference(self):
        if not self.current:
            return
        p = self.current
        lang = self.lang
        refmap = {"python": p.reference_py, "java": p.reference_java,
                  "cpp": p.reference_cpp, "javascript": p.reference_js}
        code = refmap.get(lang, "")
        if not code.strip():                      # 현재 언어 정답이 없으면 정석(파이썬) 코드로
            lang, code = "python", p.reference_py
        dlg = QMainWindow(self)
        dlg.setWindowTitle(f"hint last · {p.title}")
        dlg.resize(800, 660)
        view = QPlainTextEdit()
        view.setReadOnly(True)
        view.setFont(QFont(CODE_FAMILY, 11))
        view.setWordWrapMode(QTextOption.NoWrap)
        if code.strip():
            view.setPlainText(code.strip())
            Highlighter(view.document(), lang)
        else:
            view.setPlainText("준비된 정답 코드가 없습니다.")
        view.setStyleSheet(f"background:{BG};border:none;padding:10px;")
        dlg.setCentralWidget(view)
        dlg.show()
        self._ref_dlg = dlg

    # 채점
    def on_run(self):
        """실행만 — 내가 넣은 입력으로 코드를 돌려 출력(print/console.log/cout)을 확인. 채점 아님."""
        if not self.run_btn.isEnabled():       # 단축키(F5) 연타로 인한 중복 실행 방지
            return
        if self._mode == "lesson":
            self._run_lesson()
            return
        if self._mode == "vocab":
            # 드릴(암기/문장) 진행 중이면 F5 재입력으로 처음부터 재시작되지 않게
            if (self.right_stack.isVisible()
                    and self.right_stack.currentWidget() in (self.typing_widget, self.sentence_widget)):
                return
            self._vocab_typing()
            return
        if not self.current:
            return
        if self._blocked_locked(self.current):
            return
        p, lang = (self._cur_active or self.current), self.lang
        if not runner.compiler_available(lang):
            self.out.clear()
            self._append(f"{runner.LANGUAGES[lang]['name']} 실행기가 없습니다. (가이드의 설치 안내 참고)\n", ORANGE)
            return
        self._save_editor(force=True)      # 실행에는 파일이 필요
        path = self._sol_path(p, lang)
        stdin_text = self.stdin_box.toPlainText()
        self.out.clear()
        self._append(f"$ run {runner.LANGUAGES[lang]['name']}   (실행만 · 채점 아님)\n", CYAN)
        self._set_status("running…", YELLOW)
        self.run_btn.setEnabled(False)
        if p.type == "func":
            # 함수형: 입력칸에 쓴 인자로 호출 — 비어 있으면 첫 예제 인자 사용
            import json
            custom = self._parse_func_args(p, stdin_text)
            if custom == "ERROR":
                self._append(f"  입력칸의 인자를 해석할 수 없습니다: {stdin_text.strip()}\n", RED)
                self._append(f"  예: 6   또는   {p.func_name}(6)   (여러 개면 쉼표로: 1, [2, 3])\n", COMMENT)
                self.run_btn.setEnabled(True)
                self._set_status("인자 형식 오류", ORANGE)
                return
            if custom is not None:
                args = custom
            else:
                args = p.examples[0]["args"] if p.examples else []
                if p.examples:
                    self._append("  (입력칸이 비어 있어 첫 예제 인자를 사용합니다)\n", COMMENT)
            # 임시 폴더 대신 풀이 폴더에 두어 폴더 누수 방지(keep_solutions 정리 대상)
            ap = path.parent / "_run_args.json"
            ap.write_text(json.dumps(args), encoding="utf-8")
            self._append(f"  {p.func_name}({', '.join(map(repr, args))}) =>\n", COMMENT)
            from engine.runner import func_cmd, FUNC_HARNESS
            th = RunThread("python", path, cmd=func_cmd(FUNC_HARNESS, path, ap, p.func_name))
        else:
            # 입력칸이 비어 있으면 첫 예제 입력을 자동 사용(설정 ON일 때 · Scanner NoSuchElement 방지)
            if self.settings.get_bool("autofill_stdin") and not stdin_text.strip() and p.examples:
                stdin_text = p.examples[0].get("input", "")
                if stdin_text.strip():
                    self._append("  (입력칸이 비어 있어 첫 예제 입력을 사용합니다)\n", COMMENT)
                    self._append(f"  stdin> {stdin_text.strip()}\n", COMMENT)
            th = RunThread(lang, path, stdin=stdin_text)
        th.done.connect(self._on_lesson_done)
        th.finished.connect(lambda t=th: self._threads.remove(t) if t in self._threads else None)
        self._threads.append(th)
        th.start()

    def on_submit(self):
        """제출 — 문제의 테스트케이스로 채점해 정답/오답 판정."""
        if not self.submit_btn.isEnabled():    # 단축키(Ctrl+Enter) 연타로 인한 중복 채점 방지
            return
        if self._mode != "problem" or not self.current:
            self._set_status("채점할 문제를 선택하세요", ORANGE)
            return
        if self._blocked_locked(self.current):
            return
        p, lang = (self._cur_active or self.current), self.lang
        if p.type == "func" and lang != "python":
            self.out.clear()
            self._append("※ 함수 구현형 문제는 Python으로만 채점됩니다.\n", ORANGE)
            return
        if not runner.compiler_available(lang):
            self.out.clear()
            self._append(f"{runner.LANGUAGES[lang]['name']} 컴파일러가 없어 채점할 수 없습니다.\n", ORANGE)
            return
        self._save_editor(force=True)      # 채점에는 파일이 필요
        path = self._sol_path(p, lang)
        self.next_btn.setVisible(False)
        eff_tl, eff_ml = effective_limits(p, lang)
        self.out.clear()
        self._append(f"$ submit {runner.LANGUAGES[lang]['name']}   "
                     f"limit  ⏱ {eff_tl}ms · 💾 {eff_ml}MB\n", CYAN)
        self._set_status("채점 중…", YELLOW)
        self.submit_btn.setEnabled(False)
        th = JudgeThread(p, lang, path)
        th.done.connect(self._on_judged)
        th.finished.connect(lambda t=th: self._threads.remove(t) if t in self._threads else None)
        self._threads.append(th)
        th.start()

    def _on_judged(self, p, lang, res):
        self.submit_btn.setEnabled(True)
        if isinstance(res, Exception):
            self._append(f"\nerror: {res}\n", RED)
            self._set_status("error", RED)
            return
        try:
            self._render_result(p, lang, res)
        except Exception as e:
            # 결과 렌더링 중 예외가 앱 크래시로 이어지지 않게 격리
            self._append(f"\n결과 표시 중 오류: {e}\n", RED)
            self._set_status("error", RED)

    @staticmethod
    def _clip(text, max_chars=400, max_lines=8):
        """대용량 입출력이 터미널을 도배하지 않도록 잘라서 표시."""
        s = str(text)
        lines = s.splitlines()
        clipped = False
        if len(lines) > max_lines:
            s = "\n".join(lines[:max_lines])
            clipped = True
        if len(s) > max_chars:
            s = s[:max_chars]
            clipped = True
        return s + (" …(생략)" if clipped else "")

    def _render_result(self, p, lang, res):
        eff_tl, eff_ml = effective_limits(p, lang)
        if res.unsupported:
            self._append(res.unsupported + "\n", ORANGE)
            self._set_status("채점 불가", ORANGE)
            return
        if res.compile_error:
            self._append("\n✗ BUILD ERR\n", RED, bold=True)
            self._append(res.compile_error + "\n", RED)
            self._set_status("build err", RED)
            return

        def memstr(kb):
            if kb is None:
                return "-"
            return f"{kb/1024:.1f}MB" if kb >= 1024 else f"{kb}KB"

        self._append("\n")
        for c in res.cases:
            txt = VERDICT_TXT.get(c.verdict, c.verdict)
            mark = "✓" if c.passed else "✗"
            self._append(f"  case {c.index}: {mark} {txt}", GREEN if c.passed else RED)
            self._append(f"    ⏱ {c.time_ms:.0f}ms · 💾 {memstr(c.peak_mem_kb)}\n", COMMENT)
            if not c.passed:
                if c.verdict == "WA":
                    self._append(f"     in : {self._clip(c.given_input)}\n", COMMENT)
                    self._append(f"     exp: {self._clip(c.expected)}\n", COMMENT)
                    self._append(f"     got: {self._clip(c.actual)}\n", COMMENT)
                elif c.verdict == "RE" and c.error:
                    self._append(f"     err: {c.error}\n", COMMENT)
                elif c.verdict == "TLE":
                    self._append(f"     > {eff_tl}ms\n", COMMENT)
                elif c.verdict == "MLE":
                    self._append(f"     > {eff_ml}MB\n", COMMENT)

        self._append("─" * 54 + "\n", COMMENT)
        if res.accepted:
            self._append(f"  ✓ all passed   {res.passed}/{res.total}\n", GREEN, bold=True)
            self._append(f"  peak  ⏱ {res.max_time_ms:.0f}ms · 💾 {memstr(res.max_mem_kb)}\n", COMMENT)
            self._set_status("passed", GREEN)
            if p.id not in self.solved:
                self.solved.add(p.id)
                self._save_progress()
                self._refresh_item(p)
                self._update_profile()
            if self.exam and p.id in self.exam["ids"]:
                self.exam["solved"].add(p.id)
                self._tick_exam()
            info = getattr(self, "_profile_info", None)
            if info and info.get("rank") and p.rank in profile.RANK_ORDER:
                if profile.RANK_ORDER.index(p.rank) < profile.RANK_ORDER.index(info["rank"]):
                    self._append(f"  ℹ 현재 티어({info['code']})보다 쉬운 난이도라 랭크 게이지는 오르지 않아요.\n"
                                 f"    더 높은 난이도 문제를 풀어야 게이지가 상승합니다.\n", ORANGE)
            # 합격 → 다음 문제 버튼 (같은 목록에 다음 문제가 있으면)
            if self._has_next_problem():
                self.next_btn.setVisible(True)
                self._append("  → 상단 '다음 문제' 로 이어서 풀 수 있어요.\n", CYAN)
        else:
            self._append(f"  ✗ failed   {res.passed}/{res.total}\n", RED, bold=True)
            self._set_status(f"failed {res.passed}/{res.total}", RED)


def _run_as_python():
    """빌드된 exe 가 파이썬 인터프리터 역할도 하도록 (무설치 Python 채점)."""
    if len(sys.argv) >= 2 and sys.argv[1] in ("--exec-py", "--func"):
        # 채점기(runner)가 UTF-8 로 읽으므로 출력 인코딩 고정 (cp949 깨짐 방지)
        try:
            sys.stdin.reconfigure(encoding="utf-8", errors="replace")
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    if len(sys.argv) >= 3 and sys.argv[1] == "--exec-py":
        import runpy
        import traceback
        target = sys.argv[2]
        sys.argv = [target] + sys.argv[3:]
        try:
            runpy.run_path(target, run_name="__main__")
        except SystemExit:
            raise
        except BaseException:
            # 사용자 코드의 예외(CE/RE 등)는 stderr 로만 내보내고 조용히 종료한다.
            # 예외를 그대로 전파하면 PyInstaller 부트로더가 크래시 다이얼로그를 띄운다.
            traceback.print_exc()
            sys.exit(1)
        return True
    if len(sys.argv) >= 5 and sys.argv[1] == "--func":
        import importlib.util
        import json as _json
        import traceback
        sol, argsp, fn = sys.argv[2], sys.argv[3], sys.argv[4]
        try:
            with open(argsp, encoding="utf-8") as f:
                a = _json.load(f)
            spec = importlib.util.spec_from_file_location("usol", sol)
            m = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(m)
            sys.stdout.write(repr(getattr(m, fn)(*a)))
        except SystemExit:
            raise
        except BaseException:
            traceback.print_exc()
            sys.exit(1)
        return True
    return False


def _install_excepthook():
    """GUI(슬롯·타이머 등)의 미처리 예외가 앱 크래시/부트로더 다이얼로그로
    이어지지 않도록 전역 훅을 설치한다. 예외는 stderr 와 로그 파일에만 남긴다."""
    import traceback

    def hook(etype, value, tb):
        if issubclass(etype, KeyboardInterrupt):
            sys.__excepthook__(etype, value, tb)
            return
        text = "".join(traceback.format_exception(etype, value, tb))
        try:
            sys.stderr.write(text)
        except Exception:
            pass
        try:
            SOLUTIONS_DIR.mkdir(exist_ok=True)
            with open(SOLUTIONS_DIR / "error.log", "a", encoding="utf-8") as f:
                f.write(text + "\n")
        except Exception:
            pass

    sys.excepthook = hook


def main():
    if _run_as_python():
        return
    _install_excepthook()
    # Windows 작업표시줄이 창 아이콘을 쓰도록 고유 AppID 지정(아이콘 그룹화)
    if sys.platform == "win32":
        try:
            import ctypes
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("blackastro.codeT")
        except Exception:
            pass
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)   # 트레이 보내기 지원 — 종료는 명시적으로만
    app.setWindowIcon(app_icon())          # 작업표시줄/전역 아이콘
    app._caption_filter = _DialogCaptionFilter()        # 모든 다이얼로그 타이틀바 색 동기화
    app.installEventFilter(app._caption_filter)
    app.setStyleSheet(QSS)
    win = MainWindow()
    win.show()
    # 실행 시 창이 다른 앱 뒤에 깔리지 않게 포그라운드로 (로딩 지연 대비 2회)
    QTimer.singleShot(0, win._force_foreground)
    QTimer.singleShot(300, win._force_foreground)
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
