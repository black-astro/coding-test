"""자동 업데이트 — GitHub Releases 기반.

- check_latest(): 최신 릴리즈(버전/zip 주소/노트) 조회
- 소스 실행(개발): git pull 로 갱신
- 빌드 실행(frozen): 릴리즈 zip 을 내려받아 임시 폴더에 풀고,
  앱 종료를 기다렸다가 파일을 덮어쓰고 재시작하는 .bat 를 띄운다.
  (실행 중인 exe/_internal 은 잠겨 있어 종료 후에만 교체 가능)
"""

import os
import re
import sys
import json
import shutil
import zipfile
import tempfile
import subprocess
import urllib.request
from pathlib import Path

REPO = "black-astro/coding-test"
API_LATEST = f"https://api.github.com/repos/{REPO}/releases/latest"

_NO_WINDOW = subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0


def parse_ver(s: str):
    """'v1.2.0' → (1, 2, 0). 숫자가 아닌 부분은 무시."""
    nums = re.findall(r"\d+", str(s))
    return tuple(int(x) for x in nums[:3]) or (0,)


def is_newer(latest: str, current: str) -> bool:
    return parse_ver(latest) > parse_ver(current)


def check_latest(timeout: float = 6.0):
    """최신 릴리즈 정보. 실패 시 None (오프라인/차단 환경에서 조용히 넘어감)."""
    try:
        req = urllib.request.Request(API_LATEST, headers={
            "User-Agent": "codeT-updater", "Accept": "application/vnd.github+json"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = json.load(r)
        asset = next((a for a in data.get("assets", [])
                      if a.get("name", "").endswith(".zip")), None)
        return {
            "version": str(data.get("tag_name", "")).lstrip("v"),
            "zip_url": asset.get("browser_download_url", "") if asset else "",
            "zip_name": asset.get("name", "") if asset else "",
            "notes": data.get("body", "") or "",
            "page": data.get("html_url", ""),
        }
    except Exception:
        return None


def is_frozen() -> bool:
    return bool(getattr(sys, "frozen", False))


def app_root() -> Path:
    if is_frozen():
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent.parent


def can_git_update() -> bool:
    return (not is_frozen()) and (app_root() / ".git").exists() \
        and shutil.which("git") is not None


def git_update():
    """개발(소스) 실행 → git pull. (ok, 출력) 반환."""
    try:
        r = subprocess.run(["git", "-C", str(app_root()), "pull", "--ff-only"],
                           capture_output=True, text=True, timeout=60,
                           creationflags=_NO_WINDOW)
        out = (r.stdout + "\n" + r.stderr).strip()
        return r.returncode == 0, out
    except Exception as e:
        return False, str(e)


def download_zip(url: str, progress_cb=None) -> Path:
    """릴리즈 zip 다운로드 → 임시 파일 경로. progress_cb(받은 바이트, 전체 바이트)."""
    dest = Path(tempfile.mkdtemp(prefix="codeT_upd_")) / "update.zip"
    req = urllib.request.Request(url, headers={"User-Agent": "codeT-updater"})
    with urllib.request.urlopen(req, timeout=30) as r, open(dest, "wb") as f:
        total = int(r.headers.get("Content-Length") or 0)
        got = 0
        while True:
            chunk = r.read(256 * 1024)
            if not chunk:
                break
            f.write(chunk)
            got += len(chunk)
            if progress_cb:
                progress_cb(got, total)
    return dest


def stage_zip(zip_path: Path) -> Path:
    """zip 을 임시 폴더에 풀어 교체 대기 상태로 만든다."""
    stage = zip_path.parent / "staged"
    with zipfile.ZipFile(zip_path) as z:
        z.extractall(stage)
    if not (stage / "codeT.exe").exists():
        raise RuntimeError("업데이트 zip 구조가 예상과 다릅니다 (codeT.exe 없음)")
    return stage


def apply_and_restart(stage: Path):
    """앱 종료 대기 → 파일 교체 → 재시작하는 .bat 를 띄운다.
    호출한 쪽은 이 함수가 True 를 돌려주면 즉시 앱을 종료해야 한다.

    주의: 이 bat 는 콘솔 없는(detached) cmd 에서 돈다.
    - `A | B` 파이프라인은 detached cmd 에서 B 가 EOF 를 못 받아 영원히 멈출 수 있고,
    - `timeout` 은 콘솔 입력이 없으면 실패한다.
    그래서 파이프 대신 파일 리다이렉트+findstr, sleep 은 ping 을 쓴다. (v1.2.2 에서 수정)
    """
    app = app_root()
    pid = os.getpid()
    bat = stage.parent / "apply_update.bat"
    tl = stage.parent / "tasklist.txt"
    bat.write_text(
        "@echo off\r\n"
        "chcp 65001 >nul\r\n"
        ":wait\r\n"
        "ping -n 2 127.0.0.1 >nul\r\n"                       # 약 1초 대기 (콘솔 불필요)
        f"tasklist /FI \"PID eq {pid}\" /NH >\"{tl}\" 2>nul\r\n"
        f"findstr /C:\"{pid}\" \"{tl}\" >nul\r\n"
        "if not errorlevel 1 goto wait\r\n"
        f"robocopy \"{stage}\" \"{app}\" /E /IS /IT >nul\r\n"
        f"start \"\" \"{app / 'codeT.exe'}\"\r\n"
        f"rd /s /q \"{stage.parent}\"\r\n",
        encoding="utf-8")
    DETACHED = 0x00000008          # DETACHED_PROCESS
    subprocess.Popen(["cmd", "/c", str(bat)],
                     creationflags=DETACHED | _NO_WINDOW,
                     close_fds=True, cwd=str(stage.parent))
    return True
