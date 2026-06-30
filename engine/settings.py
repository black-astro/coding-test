"""앱 설정 — sqlite3 key-value 저장."""

import sqlite3
from pathlib import Path

DEFAULTS = {
    "dark_titlebar": "1",      # Windows 네이티브 타이틀바 다크
    "keep_solutions": "1",     # 풀이 파일(solutions/) 보관 (끄면 채점 후 정리)
    "show_stdin": "1",         # 터미널에 입력(stdin) 칸 표시
    "quiz_size": "10",         # 영단어 퀴즈 문항 수
    "reset_on_start": "1",     # 시작 시 작성 코드·터미널 초기화
    "autofill_stdin": "1",     # Run 시 입력칸 비면 예제 입력 자동 사용
    "editor_font_size": "11",  # 에디터/터미널 글자 크기(pt)
    "close_action": "quit",    # X 버튼 기본 동작: quit(종료·컨펌) / tray / ask
    "rank_unlock": "0",        # 랭크 잠금 해제 — 켜면 모든 랭크 문제 풀 수 있음
}


class SettingsDB:
    def __init__(self, db_path: Path):
        db_path = Path(db_path)
        db_path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(str(db_path))
        self.conn.execute("CREATE TABLE IF NOT EXISTS setting (k TEXT PRIMARY KEY, v TEXT)")
        self.conn.commit()

    def get(self, key, default=None):
        cur = self.conn.execute("SELECT v FROM setting WHERE k=?", (key,))
        row = cur.fetchone()
        if row is not None:
            return row[0]
        return DEFAULTS.get(key, default)

    def get_bool(self, key) -> bool:
        return self.get(key, "1") == "1"

    def get_int(self, key, default=0) -> int:
        try:
            return int(self.get(key, str(default)))
        except (TypeError, ValueError):
            return default

    def set(self, key, value):
        self.conn.execute(
            "INSERT INTO setting(k, v) VALUES(?, ?) ON CONFLICT(k) DO UPDATE SET v=?",
            (key, str(value), str(value)))
        self.conn.commit()
