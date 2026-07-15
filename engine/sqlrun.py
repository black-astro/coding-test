"""SQL 문제 실행기 — 인메모리 sqlite 에서 셋업 스크립트 + SELECT 쿼리를 실행한다.

- setup_sql : CREATE TABLE + INSERT 스크립트 (문제 테스트케이스의 input)
- query     : 사용자가 작성한 SELECT 문 (한 문장만 허용 — sqlite execute 제약)
- 결과는 각 행을 "|" 로 이어 붙인 텍스트로 정규화해 비교한다.

무한/폭주 쿼리 대비: progress handler 로 시간 제한을 걸어 강제 중단한다.
"""

import sqlite3
import time


class QueryTimeout(Exception):
    pass


def _cell(v) -> str:
    if v is None:
        return "NULL"
    if isinstance(v, float):
        # 12.0 → "12.0" 유지하되 불필요한 지수/오차 없이 (ROUND 결과 표시용)
        return f"{v:.10g}" if v != int(v) else f"{v:.1f}"
    return str(v)


def rows_to_text(rows) -> str:
    return "\n".join("|".join(_cell(v) for v in row) for row in rows)


def run_query(setup_sql: str, query: str, timeout_s: float = 5.0):
    """(결과 텍스트, 컬럼명 리스트) 반환. SQL 오류는 sqlite3.Error 로 전파."""
    conn = sqlite3.connect(":memory:")
    try:
        conn.executescript(setup_sql)
        deadline = time.perf_counter() + timeout_s

        def _guard():
            return 1 if time.perf_counter() > deadline else 0   # 1 → 실행 중단

        conn.set_progress_handler(_guard, 20000)
        try:
            cur = conn.execute(query.strip().rstrip(";"))
            rows = cur.fetchall()
            cols = [d[0] for d in cur.description] if cur.description else []
        except sqlite3.OperationalError as e:
            if "interrupted" in str(e).lower():
                raise QueryTimeout(f"쿼리 시간 초과({timeout_s:.0f}초)") from e
            raise
        return rows_to_text(rows), cols
    finally:
        conn.close()
