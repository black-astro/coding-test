"""영단어 학습 진행상황 — sqlite3.

단어별 정답/오답/마지막 학습 시각을 저장해 간단한 통계와 복습 우선순위에 쓴다.
DB 파일은 solutions/ 옆에 vocab.db 로 둔다(빌드 시 exe 옆).
"""

import sqlite3
from pathlib import Path


class VocabDB:
    def __init__(self, db_path: Path):
        db_path = Path(db_path)
        db_path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(str(db_path))
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS word_stat ("
            " word TEXT PRIMARY KEY, correct INTEGER DEFAULT 0,"
            " wrong INTEGER DEFAULT 0, known INTEGER DEFAULT 0)"
        )
        self.conn.commit()

    def record(self, word: str, ok: bool):
        cur = self.conn.execute("SELECT correct, wrong FROM word_stat WHERE word=?", (word,))
        row = cur.fetchone()
        if row is None:
            self.conn.execute("INSERT INTO word_stat(word, correct, wrong) VALUES(?,?,?)",
                              (word, 1 if ok else 0, 0 if ok else 1))
        else:
            c, w = row
            self.conn.execute("UPDATE word_stat SET correct=?, wrong=? WHERE word=?",
                              (c + (1 if ok else 0), w + (0 if ok else 1), word))
        self.conn.commit()

    def set_known(self, word: str, known: bool):
        self.conn.execute(
            "INSERT INTO word_stat(word, known) VALUES(?,?) "
            "ON CONFLICT(word) DO UPDATE SET known=?", (word, int(known), int(known)))
        self.conn.commit()

    def known_set(self) -> set:
        return {r[0] for r in self.conn.execute("SELECT word FROM word_stat WHERE known=1")}

    def stats(self) -> dict:
        cur = self.conn.execute(
            "SELECT COUNT(*), COALESCE(SUM(correct),0), COALESCE(SUM(wrong),0), "
            "COALESCE(SUM(known),0) FROM word_stat")
        n, c, w, k = cur.fetchone()
        return {"words": n or 0, "correct": c or 0, "wrong": w or 0, "known": k or 0}
