"""code T — 코딩테스트 풀이 GUI (PySide6 · VSCode Dracula).

실행:  python gui.py

- PySide6(Qt) + QSS 로 VSCode Dracula 테마를 재현
- 라운드 버튼 · 커스텀 라운드 스크롤바 · 드래그 가능한 스플리터
- 코드 에디터: 라인넘버 + 구문 강조(QSyntaxHighlighter) + 자동 들여쓰기
- ▶ 채점(F5) → 케이스별 시간/메모리 + 정답/오답, 통과 시 🎉 성공
"""

import sys
import html
import time
import random
import shutil
import dataclasses
from pathlib import Path

from PySide6.QtCore import Qt, QRect, QSize, QRegularExpression, Signal, QThread, QTimer
from PySide6.QtGui import (QColor, QFont, QPainter, QTextCharFormat, QTextCursor,
                           QSyntaxHighlighter, QTextFormat, QTextOption, QAction,
                           QKeySequence, QShortcut, QIcon, QPixmap, QCursor, QPalette)
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QFrame, QLabel,
                               QPushButton, QButtonGroup, QHBoxLayout, QVBoxLayout,
                               QSplitter, QTreeWidget, QTreeWidgetItem, QTextBrowser,
                               QTextEdit, QPlainTextEdit, QSizePolicy, QMenu, QMessageBox,
                               QDialog, QProgressBar, QCheckBox, QComboBox,
                               QStackedWidget, QScrollArea, QSystemTrayIcon, QSlider,
                               QStyle, QStyleOptionSlider)

APP_VERSION = "1.1.1"

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))


def resource(*parts) -> Path:
    """리소스 경로. PyInstaller 빌드 시엔 _MEIPASS 에서 찾는다."""
    base = Path(getattr(sys, "_MEIPASS", ROOT))
    return base.joinpath(*parts)


ICON_ICO = resource("img", "app.ico")     # 멀티사이즈(작업표시줄/프로그램 아이콘)
ICON_PNG = resource("img", "logo_clean.png")


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
CARD    = "#262834"   # 카드(문제/콘솔/터미널) — 여백보다 밝아 또렷이 구분

CODE_FAMILY = "Cascadia Code"
MONO_FAMILY = "Consolas"

# ─────────────────────────────────────────────────────────────────
#  테마 커스터마이즈 — 여기 값만 바꾸면 프로그램 헤더 색이 바뀐다.
# ─────────────────────────────────────────────────────────────────
HEADER_BG    = "#262834"  # 헤더 색(=카드색). 여기 값만 바꾸면 헤더/네이티브 타이틀바 색이 바뀐다.
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
#Panel {{ background: {CARD}; border-radius: 9px; }}
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
#Output {{ background:{CARD}; }}
#ProblemView, #ProblemBody {{ background:{CARD}; border:none; }}
#CodeBox {{ background:{CARD}; border:1px solid {BORDER}; border-radius:6px; }}
#OpacityBar {{ background:{BG2}; border:1px solid {BORDER}; border-radius:8px; }}
#OpacityBar QLabel {{ background:transparent; }}
QSlider#OpacitySlider {{ background:transparent; }}
QSlider#OpacitySlider::groove:horizontal {{ height:4px; background:{CUR}; border-radius:2px; }}
QSlider#OpacitySlider::add-page:horizontal {{ background:{CUR}; border-radius:2px; }}
QSlider#OpacitySlider::sub-page:horizontal {{ background:{PURPLE}; border-radius:2px; }}
QSlider#OpacitySlider::handle:horizontal {{ width:12px; height:12px; margin:-5px 0; background:{PURPLE}; border-radius:6px; }}
QSlider#OpacitySlider::handle:horizontal:hover {{ background:{PURPLE_D}; }}

QScrollBar:vertical {{ background:transparent; width:7px; margin:3px 2px 3px 0; }}
QScrollBar::handle:vertical {{ background:{CUR}; border-radius:3px; min-height:30px; }}
QScrollBar::handle:vertical:hover {{ background:{COMMENT}; }}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{ height:0; }}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{ background:transparent; }}
QScrollBar:horizontal {{ background:transparent; height:7px; margin:0 3px 2px 3px; }}
QScrollBar::handle:horizontal {{ background:{CUR}; border-radius:3px; min-width:30px; }}
QScrollBar::handle:horizontal:hover {{ background:{COMMENT}; }}
QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{ width:0; }}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {{ background:transparent; }}

QSplitter::handle {{ background:{GAP}; }}
QSplitter::handle:horizontal {{ width:6px; }}
QSplitter::handle:vertical {{ height:6px; }}
QToolTip {{ background:{BG3}; color:{FG}; border:1px solid {CUR}; }}

QMenu {{ background:{BG2}; color:{FG}; border:1px solid {CUR}; padding:4px; }}
QMenu::item {{ padding:6px 22px; border-radius:5px; }}
QMenu::item:selected {{ background:{CUR}; color:{CYAN}; }}
QMenu::separator {{ height:1px; background:{CUR}; margin:4px 8px; }}
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


# ───────────────────────── 설정 다이얼로그 ─────────────────────────

class SettingsDialog(QDialog):
    def __init__(self, parent, settings):
        super().__init__(parent)
        self.setWindowTitle("설정")
        self.resize(440, 380)
        self.s = settings
        self.win = parent
        lay = QVBoxLayout(self)
        lay.setContentsMargins(22, 22, 22, 22)
        lay.setSpacing(12)

        def title(t):
            l = QLabel(t)
            l.setStyleSheet(f"color:{PURPLE};font-weight:bold;font-size:14px;")
            return l

        lay.addWidget(title("환경 / 표시"))
        self.cb_dark = QCheckBox("Windows 다크 타이틀바")
        self.cb_dark.setChecked(settings.get_bool("dark_titlebar"))
        self.cb_keep = QCheckBox("풀이 파일 보관 (끄면 종료 시 정리해 용량 절약)")
        self.cb_keep.setChecked(settings.get_bool("keep_solutions"))
        self.cb_stdin = QCheckBox("터미널에 입력(stdin) 칸 표시")
        self.cb_stdin.setChecked(settings.get_bool("show_stdin"))
        for cb in (self.cb_dark, self.cb_keep, self.cb_stdin):
            lay.addWidget(cb)
        row = QHBoxLayout()
        row.addWidget(QLabel("영단어 퀴즈 문항 수"))
        self.combo = QComboBox()
        self.combo.addItems(["10", "15", "20", "30"])
        self.combo.setCurrentText(settings.get("quiz_size", "10"))
        row.addWidget(self.combo)
        row.addStretch(1)
        lay.addLayout(row)

        crow = QHBoxLayout()
        crow.addWidget(QLabel("닫기(X) 버튼 동작"))
        self.combo_close = QComboBox()
        for label, data in [("물어보기", "ask"), ("프로그램 종료", "quit"), ("트레이로 보내기", "tray")]:
            self.combo_close.addItem(label, data)
        cur_close = settings.get("close_action", "ask") or "ask"
        ci = self.combo_close.findData(cur_close)
        self.combo_close.setCurrentIndex(ci if ci >= 0 else 0)
        crow.addWidget(self.combo_close)
        crow.addStretch(1)
        lay.addLayout(crow)

        lay.addWidget(title("관리"))
        for label, cb in [("🎲 문제 변형 리셋", parent._on_reset),
                          ("♻ 내 티어 초기화", parent._reset_tier),
                          ("🔧 환경 점검", parent._env_check)]:
            b = QPushButton(label)
            b.setObjectName("Ghost")
            b.clicked.connect(lambda _=False, fn=cb: (self.accept(), fn()))
            lay.addWidget(b)

        lay.addStretch(1)
        save = QPushButton("저장")
        save.setObjectName("Run")
        save.clicked.connect(self._save)
        lay.addWidget(save)

    def _save(self):
        self.s.set("dark_titlebar", "1" if self.cb_dark.isChecked() else "0")
        self.s.set("keep_solutions", "1" if self.cb_keep.isChecked() else "0")
        self.s.set("show_stdin", "1" if self.cb_stdin.isChecked() else "0")
        self.s.set("quiz_size", self.combo.currentText())
        self.s.set("close_action", self.combo_close.currentData())
        self.win._apply_settings()
        self.accept()


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
            self._ic_done = qta.icon("fa5s.check", color=GREEN)
        else:
            self._ic_right = self._ic_down = self._ic_file = self._ic_done = None

        # 점수/랭크 계산용 전체 문제 목록(랭크 + 실전)
        self._all_problems = list(problems.BY_ID.values()) + list(practice.BY_ID.values())

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
        save_sc.activated.connect(self._save_editor)
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
        # X 버튼: 설정값(close_action)에 따라 종료/트레이, 미설정이면 물어봄
        action = self.settings.get("close_action", "ask") or "ask"
        if action == "ask":
            action = self._ask_close_action()
            if action is None:                  # 취소
                event.ignore()
                return
        if action == "tray" and getattr(self, "tray", None) is not None:
            event.ignore()
            self.hide()
            self.tray.show()
            if not self._tray_hinted:
                self._tray_hinted = True
                self.tray.showMessage("code T", "트레이에서 계속 실행 중 — 아이콘을 클릭하면 다시 열려요.",
                                      QSystemTrayIcon.Information, 3000)
            return
        # 종료
        self._cleanup_solutions()
        if getattr(self, "tray", None) is not None:
            self.tray.hide()
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
        self._tray_menu.addSeparator()
        self._tray_menu.addAction("종료", self._quit_app)
        self.tray.setContextMenu(self._tray_menu)
        self.tray.activated.connect(self._tray_activated)
        self.tray.show()

    def _tray_activated(self, reason):
        if reason in (QSystemTrayIcon.DoubleClick, QSystemTrayIcon.Trigger):
            self._show_normal()

    def _show_normal(self):
        self.showNormal()
        self.raise_()
        self.activateWindow()

    def _tray_hide_mode(self):
        self._show_normal()
        self._set_hide_mode(True)

    def _quit_app(self):
        self._cleanup_solutions()
        if getattr(self, "tray", None) is not None:
            self.tray.hide()
        QApplication.instance().quit()

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
        self._set_hide_mode(not self._hidden_mode)

    def _set_hide_mode(self, on):
        """on: 사이드바·문제설명 숨기고 에디터+터미널만 + 창을 작게. 문제 선택은 상단 콤보로."""
        if on and not self._hidden_mode:
            self._saved_geometry = self.geometry()      # 들어가기 전 창 크기/위치 기억
        self._hidden_mode = on
        self.side.setVisible(not on)
        self.probp.setVisible(not on)
        self.hide_combo.setVisible(on)
        self.rank_label.setVisible(not on)
        self.rank_bar.setVisible(not on)
        self.side_toggle.setVisible(not on)
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
        """Windows 네이티브 타이틀바를 다크로(+Win11이면 CAPTION_COLOR 색으로)."""
        if sys.platform != "win32" or not self.settings.get_bool("dark_titlebar"):
            return
        try:
            import ctypes
            hwnd = int(self.winId())
            dwm = ctypes.windll.dwmapi
            # 다크 모드 캡션 (Win10 2004+/Win11) — attr 20, 구버전 19 폴백
            def cref(hexc):
                hexc = hexc.lstrip("#")
                r, g, b = int(hexc[0:2], 16), int(hexc[2:4], 16), int(hexc[4:6], 16)
                return ctypes.c_int((b << 16) | (g << 8) | r)
            one = ctypes.c_int(1)
            if dwm.DwmSetWindowAttribute(hwnd, 20, ctypes.byref(one), 4) != 0:
                dwm.DwmSetWindowAttribute(hwnd, 19, ctypes.byref(one), 4)
            # Win11 22000+ : 캡션/텍스트/테두리 색을 VSCode 테마에 맞춤 (그 외 버전은 무시)
            cap, txt, bdr = cref(CAPTION_COLOR), cref(FG), cref(BG3)
            dwm.DwmSetWindowAttribute(hwnd, 35, ctypes.byref(cap), 4)  # caption
            dwm.DwmSetWindowAttribute(hwnd, 36, ctypes.byref(txt), 4)  # text
            dwm.DwmSetWindowAttribute(hwnd, 34, ctypes.byref(bdr), 4)  # border
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
        SOLUTIONS_DIR.mkdir(exist_ok=True)
        PROGRESS_FILE.write_text(json.dumps(sorted(self.solved), ensure_ascii=False), encoding="utf-8")

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

        # 실행(출력 확인) / 제출(채점)
        self.run_btn = mkbtn("▶ Run", self.on_run, obj="Ghost", w=80, tip="실행만 — 내 입력으로 출력 확인 (F5)")
        lay.addWidget(self.run_btn)
        self.submit_btn = mkbtn("제출", self.on_submit, obj="Run", w=74, tip="채점 — 정답 판정 (Ctrl+Enter)")
        lay.addWidget(self.submit_btn)
        return bar

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

    def _apply_settings(self):
        self.stdin_box.setVisible(self.settings.get_bool("show_stdin"))

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
        tip = (f"내 랭크: {info['tier_kr']}   ·   점수 {info['score']}   ·   {info['n_solved']}문제 해결\n"
               + "   ".join(f"{profile.RANK_EMOJI[r]} {info['solved'].get(r,0)}/{info['total'].get(r,0)}"
                            for r in profile.RANK_ORDER))
        if info.get("next_goal"):
            tip += f"\n다음 목표: {info['next_goal']}"
        self.rank_label.setToolTip(tip)
        self.rank_bar.setToolTip(tip)

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
        self.tree = QTreeWidget()
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
        sl.addWidget(self.tree, 1)
        split.addWidget(side)

        # 2) 문제 설명
        probp = QFrame()
        self.probp = probp
        probp.setObjectName("PanelBG")
        pl = QVBoxLayout(probp)
        pl.setContentsMargins(10, 10, 8, 10)
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
        self.stdin_box.setPlaceholderText("Run(실행) 시 표준입력으로 들어갈 값 (예: 1 2). 제출(채점) 때는 무시됩니다.")
        ol.addWidget(self.stdin_box)
        self.out = QTextEdit()
        self.out.setObjectName("Output")
        self.out.setReadOnly(True)
        self.out.setFont(QFont(MONO_FAMILY, 9))
        ol.addWidget(self.out, 1)
        right.addWidget(outp)
        right.setSizes([560, 250])
        split.addWidget(right)

        # 텍스트 영역(문제/console/terminal/입력)의 viewport 배경을 카드색과 정확히 일치
        # (QSS 'background'는 viewport 까지 적용 안 되어 팔레트 Base 색이 새어 나오는 걸 방지)
        for w in (self.prob, self.editor, self.out, self.stdin_box):
            pal = w.palette()
            pal.setColor(QPalette.Base, QColor(CARD))
            pal.setColor(QPalette.Window, QColor(CARD))
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

        # 6) 시험 — 단일 도전 항목
        ex = self._group_item(self.tree, "시험", top=True)
        it = QTreeWidgetItem(ex, ["🏁 실전 코딩테스트 도전"])
        if self._ic_file is not None:
            it.setIcon(0, self._ic_file)
        self.item_exam[id(it)] = exam.CHALLENGE
        ex.setExpanded(True)

        # 6) 가이드
        if lessons.GUIDES:
            gd = self._group_item(self.tree, "가이드", top=True)
            for les in lessons.GUIDES:
                self._add_lesson(gd, les)

        # 7) 영단어 (최하단)
        if vocab.total():
            vg = self._group_item(self.tree, "영단어", top=True)
            for lv in vocab.LEVELS:
                words = vocab.BY_LEVEL.get(lv, [])
                if not words:
                    continue
                it = QTreeWidgetItem(vg, [f"{lv} ({len(words)})"])
                if self._ic_file is not None:
                    it.setIcon(0, self._ic_file)
                self.item_vocab[id(it)] = lv

    def _add_lesson(self, parent, les):
        it = QTreeWidgetItem(parent, [les.title])
        if self._ic_file is not None:
            it.setIcon(0, self._ic_file)
        self.item_lesson[id(it)] = les

    def _add_problem(self, parent, p):
        solved = p.id in self.solved
        if self._ic_file is not None:
            it = QTreeWidgetItem(parent, [p.title])
            it.setIcon(0, self._ic_done if solved else self._ic_file)
        else:
            it = QTreeWidgetItem(parent, [("✓ " if solved else "   ") + p.title])
        if solved:
            it.setForeground(0, QColor(GREEN))
        it.setData(0, Qt.UserRole, p.id)
        self.item_problem[id(it)] = p
        self.problem_item.setdefault(p.id, []).append(it)   # 같은 문제가 여러 섹션에 나옴

    def _refresh_item(self, p):
        solved = p.id in self.solved
        for it in self.problem_item.get(p.id, []):
            if self._ic_file is not None:
                it.setText(0, p.title)
                it.setIcon(0, self._ic_done if solved else self._ic_file)
            else:
                it.setText(0, ("✓ " if solved else "   ") + p.title)
            it.setForeground(0, QColor(GREEN if solved else FG))

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
        self._render_problem(self._cur_active)
        self._load_editor()
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

    def _open_lesson(self, les):
        self._mode = "lesson"
        self.current_lesson = les
        self.current = None
        self._cur_active = None
        self._render_lesson(les)
        self.out.clear()
        ext_map = {"python": "py", "java": "java", "cpp": "cpp", "javascript": "js",
                   "css": "css", "scss": "scss"}
        lang = les.lang if les.lang in ext_map else "python"
        self.lang = lang
        self._sync_lang_buttons()
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
        if l.explanation:
            h.append(sec("설명") + f"<div>{esc(l.explanation)}</div>")
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
        h.append("</div>")
        self._show_html(h)

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
        th = RunThread(lang, path)
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

    # ───────────────────────── 영단어 ─────────────────────────

    def _open_vocab(self, level):
        self._mode = "vocab"
        self.vocab_level = level
        self.current = None
        self.current_lesson = None
        self._render_vocab(level)
        self.out.clear()
        self._set_status("단어 학습 · Run 또는 우클릭으로 퀴즈", CYAN)

    def _render_vocab(self, level):
        words = vocab.BY_LEVEL.get(level, [])
        known = self.vocab_db.known_set()
        st = self.vocab_db.stats()
        h = [f"<div style='font-family:Segoe UI;color:{FG};font-size:13px;line-height:1.5;'>"]
        h.append(f"<div style='color:{PURPLE};font-size:18px;font-weight:bold;'>영단어 · {level} "
                 f"<span style='color:{COMMENT};font-size:12px;'>({len(words)}개)</span></div>")
        h.append(f"<div style='color:{COMMENT};font-size:11px;'>누적 — 정답 {st['correct']} · 오답 {st['wrong']} · 외운 단어 {st['known']}</div>")
        h.append(f"<div style='color:{GREEN};font-size:11px;margin-bottom:8px;'>▶ Run 또는 우클릭 → 퀴즈로 테스트</div>")
        for w in words:
            mark = " ✅" if w.word in known else ""
            h.append(f"<div style='margin:7px 0;border-left:2px solid {CUR};padding-left:8px;'>"
                     f"<b style='color:{CYAN};font-size:15px;'>{html.escape(w.word)}</b> "
                     f"<span style='color:{COMMENT};'>{html.escape(w.pos)}</span>{mark}<br>"
                     f"<span style='color:{FG};'>{html.escape(w.meaning)}</span>")
            if w.example:
                h.append(f"<br><span style='color:{YELLOW};font-family:{MONO_FAMILY};font-size:12px;'>{html.escape(w.example)}</span>")
                if w.example_kr:
                    h.append(f"<br><span style='color:{COMMENT};font-size:12px;'>{html.escape(w.example_kr)}</span>")
            h.append("</div>")
        h.append("</div>")
        self._show_html(h)

    def _vocab_quiz(self, level):
        words = vocab.BY_LEVEL.get(level, [])
        if len(words) < 4:
            self._set_status("퀴즈를 보려면 단어가 더 필요합니다", ORANGE)
            return
        n = self.settings.get_int("quiz_size", 10)
        quiz = random.sample(words, min(n, len(words)))
        QuizDialog(self, quiz, words, self.vocab_db).exec()
        self._render_vocab(level)

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
        rem = int(self.exam["deadline"] - time.time())
        if rem <= 0:
            self.exam_label.setText("⏳ 00:00")
            self._submit_exam(auto=True)
            return
        m, s = divmod(rem, 60)
        n, tot = len(self.exam["solved"]), len(self.exam["problems"])
        self.exam_label.setText(f"⏳ {m:02d}:{s:02d}  ·  {n}/{tot}")

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
        code = path.read_text(encoding="utf-8") if path.exists() else self._template(p, self.lang)
        self.editor.set_code(code, self.lang)
        self.file_label.setText(runner.LANGUAGES[self.lang]["filename"])
        if p.type == "func" and self.lang != "python":
            self._set_status("fn: python only", ORANGE)
        else:
            self._set_status("ready", COMMENT)

    def _save_editor(self):
        if not self.current:
            return
        path = self._sol_path(self.current, self.lang)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(self.editor.toPlainText(), encoding="utf-8")

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

    def _prob_menu(self, pos, widget=None):
        widget = widget or self.prob
        if self._mode == "vocab":
            m = QMenu(widget)
            a = m.addAction("📝 퀴즈 10문제 풀기")
            if m.exec(widget.mapToGlobal(pos)) == a:
                self._vocab_quiz(self.vocab_level)
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
        if self._mode == "lesson":
            self._run_lesson()
            return
        if self._mode == "vocab":
            self._vocab_quiz(self.vocab_level)
            return
        if not self.current:
            return
        p, lang = (self._cur_active or self.current), self.lang
        if not runner.compiler_available(lang):
            self.out.clear()
            self._append(f"{runner.LANGUAGES[lang]['name']} 실행기가 없습니다. (가이드의 설치 안내 참고)\n", ORANGE)
            return
        self._save_editor()
        path = self._sol_path(p, lang)
        stdin_text = self.stdin_box.toPlainText()
        self.out.clear()
        self._append(f"$ run {runner.LANGUAGES[lang]['name']}   (실행만 · 채점 아님)\n", CYAN)
        self._set_status("running…", YELLOW)
        self.run_btn.setEnabled(False)
        if p.type == "func":
            # 함수형: 첫 예제 인자로 호출해 반환값 확인 (입력칸 무시)
            import json
            import tempfile
            args = p.examples[0]["args"] if p.examples else []
            d = Path(tempfile.mkdtemp())
            ap = d / "a.json"
            ap.write_text(json.dumps(args), encoding="utf-8")
            self._append(f"  {p.func_name}({', '.join(map(repr, args))}) =>\n", COMMENT)
            from engine.runner import func_cmd, FUNC_HARNESS
            th = RunThread("python", path, cmd=func_cmd(FUNC_HARNESS, path, ap, p.func_name))
        else:
            th = RunThread(lang, path, stdin=stdin_text)
        th.done.connect(self._on_lesson_done)
        th.finished.connect(lambda t=th: self._threads.remove(t) if t in self._threads else None)
        self._threads.append(th)
        th.start()

    def on_submit(self):
        """제출 — 문제의 테스트케이스로 채점해 정답/오답 판정."""
        if self._mode != "problem" or not self.current:
            self._set_status("채점할 문제를 선택하세요", ORANGE)
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
        self._save_editor()
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
        self._render_result(p, lang, res)

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
                    self._append(f"     in : {c.given_input}\n", COMMENT)
                    self._append(f"     exp: {c.expected}\n", COMMENT)
                    self._append(f"     got: {c.actual}\n", COMMENT)
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
    if len(sys.argv) >= 3 and sys.argv[1] == "--exec-py":
        import runpy
        target = sys.argv[2]
        sys.argv = [target] + sys.argv[3:]
        runpy.run_path(target, run_name="__main__")
        return True
    if len(sys.argv) >= 5 and sys.argv[1] == "--func":
        import importlib.util
        import json as _json
        sol, argsp, fn = sys.argv[2], sys.argv[3], sys.argv[4]
        with open(argsp, encoding="utf-8") as f:
            a = _json.load(f)
        spec = importlib.util.spec_from_file_location("usol", sol)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        sys.stdout.write(repr(getattr(m, fn)(*a)))
        return True
    return False


def main():
    if _run_as_python():
        return
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
    app.setStyleSheet(QSS)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
