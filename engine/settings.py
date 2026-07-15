"""앱 설정 — sqlite3 key-value 저장."""

import sqlite3
from pathlib import Path

DEFAULTS = {
    "dark_titlebar": "1",      # Windows 네이티브 타이틀바 다크
    "keep_solutions": "1",     # 풀이 파일(solutions/) 보관 (끄면 채점 후 정리)
    "show_stdin": "1",         # 터미널에 입력(stdin) 칸 표시
    "quiz_size": "10",         # 영단어 퀴즈 문항 수
    "reset_on_start": "0",     # 시작 시 작성 코드·터미널 초기화 (기본 OFF — 작성 코드 보존)
    "autofill_stdin": "1",     # Run 시 입력칸 비면 예제 입력 자동 사용
    "editor_font_size": "11",  # 에디터/터미널 글자 크기(pt)
    "close_action": "quit",    # X 버튼 기본 동작: quit(종료·컨펌) / tray / ask
    "rank_unlock": "0",        # 랭크 잠금 해제 — 켜면 모든 랭크 문제 풀 수 있음
    "wrap_editor": "0",        # 에디터 줄바꿈 (긴 줄을 창 폭에 맞춰 접기)
    "auto_next": "0",          # 정답 시 자동으로 다음 문제 열기
    "resume_last": "1",        # 시작 시 마지막에 보던 문제 이어서 열기
    "exam_to_progress": "1",   # 모의고사 정답을 영구 풀이 기록에도 반영
    "solve_timer": "1",        # 문제별 풀이 시간 측정(⏱ 표시 · 통계에 기록)
    "efficiency_compare": "1", # 정답 시 내 코드 vs 정답 코드 시간/메모리 비교
    "update_check": "1",       # 시작 시 새 버전 확인 (GitHub 릴리즈)
    "boss_key": "1",           # 전역 보스 키 Ctrl+Shift+H — 즉시 트레이로 숨김
}


class SettingsDB:
    def __init__(self, db_path: Path):
        db_path = Path(db_path)
        db_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            self.conn = sqlite3.connect(str(db_path))
            self.conn.execute("CREATE TABLE IF NOT EXISTS setting (k TEXT PRIMARY KEY, v TEXT)")
            self.conn.commit()
        except sqlite3.DatabaseError:
            # DB 파일 손상 → 백업해 두고 새로 만든다 (앱 시작 크래시 방지)
            try:
                self.conn.close()
            except Exception:
                pass
            backup = db_path.with_suffix(db_path.suffix + ".corrupt")
            try:
                backup.unlink(missing_ok=True)
                db_path.rename(backup)
            except OSError:
                pass
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
