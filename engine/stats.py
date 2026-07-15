"""풀이 기록/통계 — sqlite 저장.

- time_spent : 문제별 누적 풀이 시간(초) + 첫 정답까지 걸린 시간
- submit_log : 제출 이력 (판정/시간/메모리) — 유형별 정답률·오답 통계용

solutions/app.db 를 설정(SettingsDB)과 공유한다(테이블만 분리).
"""

import time
import sqlite3
from pathlib import Path


class StatsDB:
    def __init__(self, db_path: Path):
        db_path = Path(db_path)
        db_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            self.conn = sqlite3.connect(str(db_path))
            self._init_tables()
        except sqlite3.DatabaseError:
            # 손상 시 통계 기능만 조용히 비활성 (앱 시작은 막지 않는다)
            self.conn = sqlite3.connect(":memory:")
            self._init_tables()

    def _init_tables(self):
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS time_spent ("
            " problem_id TEXT PRIMARY KEY,"
            " seconds INTEGER NOT NULL DEFAULT 0,"
            " solved_seconds INTEGER)")           # 첫 AC 시점의 누적 시간(초)
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS submit_log ("
            " id INTEGER PRIMARY KEY AUTOINCREMENT,"
            " problem_id TEXT NOT NULL,"
            " topic TEXT DEFAULT '',"
            " lang TEXT DEFAULT '',"
            " verdict TEXT NOT NULL,"             # AC/WA/TLE/MLE/RE/CE
            " time_ms REAL DEFAULT 0,"
            " mem_kb INTEGER,"
            " ts INTEGER NOT NULL)")
        self.conn.commit()

    # ---- 풀이 시간 ----
    def add_time(self, problem_id: str, seconds: int):
        if seconds <= 0:
            return
        self.conn.execute(
            "INSERT INTO time_spent(problem_id, seconds) VALUES(?, ?) "
            "ON CONFLICT(problem_id) DO UPDATE SET seconds = seconds + ?",
            (problem_id, seconds, seconds))
        self.conn.commit()

    def get_time(self, problem_id: str) -> int:
        row = self.conn.execute(
            "SELECT seconds FROM time_spent WHERE problem_id=?", (problem_id,)).fetchone()
        return int(row[0]) if row else 0

    def mark_solved(self, problem_id: str, total_seconds: int):
        """첫 정답 시각 기록 — 이미 기록돼 있으면 유지(첫 기록이 진짜 풀이 시간)."""
        self.conn.execute(
            "INSERT INTO time_spent(problem_id, seconds, solved_seconds) VALUES(?, ?, ?) "
            "ON CONFLICT(problem_id) DO UPDATE SET "
            " solved_seconds = COALESCE(solved_seconds, ?)",
            (problem_id, total_seconds, total_seconds, total_seconds))
        self.conn.commit()

    def solved_time(self, problem_id: str):
        row = self.conn.execute(
            "SELECT solved_seconds FROM time_spent WHERE problem_id=?", (problem_id,)).fetchone()
        return int(row[0]) if row and row[0] is not None else None

    # ---- 제출 이력 ----
    def record_submit(self, problem_id: str, topic: str, lang: str, verdict: str,
                      time_ms: float = 0.0, mem_kb=None):
        self.conn.execute(
            "INSERT INTO submit_log(problem_id, topic, lang, verdict, time_ms, mem_kb, ts) "
            "VALUES(?, ?, ?, ?, ?, ?, ?)",
            (problem_id, topic or "", lang or "", verdict, float(time_ms or 0),
             mem_kb, int(time.time())))
        self.conn.commit()

    def verdict_counts_by_topic(self):
        """{topic: {"AC": n, "FAIL": n}} — 유형별 제출 성적(같은 문제 중복 제출 포함)."""
        out = {}
        for topic, verdict, n in self.conn.execute(
                "SELECT topic, verdict, COUNT(*) FROM submit_log GROUP BY topic, verdict"):
            d = out.setdefault(topic or "?", {"AC": 0, "FAIL": 0})
            d["AC" if verdict == "AC" else "FAIL"] += n
        return out

    def fail_counts_by_problem(self):
        """{problem_id: 오답 제출 수} — 고생한 문제 목록용."""
        return {pid: n for pid, n in self.conn.execute(
            "SELECT problem_id, COUNT(*) FROM submit_log WHERE verdict != 'AC' "
            "GROUP BY problem_id")}

    def avg_solved_seconds_by(self, id_to_key):
        """key(예: topic)별 평균 '첫 정답까지 시간'(초). id_to_key: problem_id → key."""
        acc = {}
        for pid, secs in self.conn.execute(
                "SELECT problem_id, solved_seconds FROM time_spent "
                "WHERE solved_seconds IS NOT NULL"):
            key = id_to_key.get(pid)
            if key is None:
                continue
            s, n = acc.get(key, (0, 0))
            acc[key] = (s + secs, n + 1)
        return {k: s / n for k, (s, n) in acc.items() if n}

    def total_seconds(self) -> int:
        row = self.conn.execute("SELECT COALESCE(SUM(seconds), 0) FROM time_spent").fetchone()
        return int(row[0])

    def submit_totals(self):
        """(총 제출 수, AC 수)"""
        row = self.conn.execute(
            "SELECT COUNT(*), SUM(CASE WHEN verdict='AC' THEN 1 ELSE 0 END) "
            "FROM submit_log").fetchone()
        return int(row[0] or 0), int(row[1] or 0)

    def reset(self):
        self.conn.execute("DELETE FROM time_spent")
        self.conn.execute("DELETE FROM submit_log")
        self.conn.commit()
