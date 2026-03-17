import subprocess
from typing import Sequence
from config import ADB_PREFIX, ECALL_TRIGGER_COMMAND, ANSWER_CALL_COMMAND

class ADBCommandError(RuntimeError): pass

def _run_adb(args: Sequence[str], timeout: int = 20) -> str:
    cmd = [*ADB_PREFIX, *args]
    completed = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, check=False)
    if completed.returncode != 0:
        raise ADBCommandError(f"ADB command failed: {' '.join(cmd)}\nstdout={completed.stdout.strip()}\nstderr={completed.stderr.strip()}")
    return completed.stdout.strip()

def trigger_ecall() -> str: return _run_adb(ECALL_TRIGGER_COMMAND)
def answer_call() -> str: return _run_adb(ANSWER_CALL_COMMAND)
