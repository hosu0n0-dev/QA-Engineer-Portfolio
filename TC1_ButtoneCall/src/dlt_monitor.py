import time
from pathlib import Path
from typing import Optional, Tuple
from config import DLT_LOG_DIR, POLL_INTERVAL

class DLTMonitorError(RuntimeError): pass

def get_latest_log_file(log_dir: Path = DLT_LOG_DIR) -> Path:
    if not log_dir.exists():
        raise DLTMonitorError(f"DLT log directory does not exist: {log_dir}")
    candidates = [p for p in log_dir.iterdir() if p.is_file()]
    if not candidates:
        raise DLTMonitorError(f"No DLT log files found in: {log_dir}")
    return max(candidates, key=lambda p: p.stat().st_mtime)

def wait_for_pattern(pattern: str, timeout_seconds: int, log_dir: Path = DLT_LOG_DIR, start_at_end: bool = True) -> Tuple[bool, str, Optional[Path]]:
    log_file = get_latest_log_file(log_dir)
    deadline = time.time() + timeout_seconds
    with log_file.open("r", encoding="utf-8", errors="ignore") as handle:
        if start_at_end:
            handle.seek(0, 2)
        while time.time() < deadline:
            line = handle.readline()
            if not line:
                time.sleep(POLL_INTERVAL)
                continue
            if pattern in line:
                return True, line.strip(), log_file
    return False, "NOT FOUND", log_file

def clear_dlt_view() -> None:
    raise NotImplementedError("DLT Clear is environment-specific.")
