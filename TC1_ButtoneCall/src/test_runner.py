from __future__ import annotations
import time
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Callable, Tuple
from adb_controller import answer_call, end_call, trigger_ecall
from config import CALLBACK_WAIT_SECONDS, CONNECT_WAIT_SECONDS, CYCLE_INTERVAL_SECONDS, DLT_STATUS_PATTERNS, ENABLE_DLT_CLEAR, REPORT_FILENAME, STATUS_WAIT_TIMEOUT, TOTAL_DURATION_HOURS
from dlt_monitor import clear_dlt_view, wait_for_pattern
from report import ReportBuilder

@dataclass
class StepDefinition:
    step_no: int
    step_name: str
    description: str
    expected: str

class TC1Runner:
    TC_ID = "TC1"
    def __init__(self, output_dir: Path) -> None:
        self.output_dir = output_dir
        self.report = ReportBuilder()

    def _record_action_step(self, cycle: int, step: StepDefinition, action: Callable[[], str]) -> bool:
        start = datetime.now()
        try:
            actual = action() or "OK"; result = "PASS"; remark = ""
        except Exception as exc:
            actual = str(exc); result = "FAIL"; remark = "Action execution failed"
        end = datetime.now()
        self.report.add_step(self.TC_ID, cycle, step.step_no, step.step_name, step.description, start, end, result, step.expected, actual, remark)
        return result == "PASS"

    def _record_check_step(self, cycle: int, step: StepDefinition, check: Callable[[], Tuple[bool, str]]) -> bool:
        start = datetime.now()
        try:
            matched, actual = check(); result = "PASS" if matched else "FAIL"; remark = "" if matched else "Timeout or pattern not found"
        except Exception as exc:
            actual = str(exc); result = "FAIL"; remark = "Check execution failed"
        end = datetime.now()
        self.report.add_step(self.TC_ID, cycle, step.step_no, step.step_name, step.description, start, end, result, step.expected, actual, remark)
        return result == "PASS"

    def run(self) -> Path:
        end_time = datetime.now() + timedelta(hours=TOTAL_DURATION_HOURS)
        cycle = 0
        while datetime.now() < end_time:
            cycle += 1
            self._record_action_step(cycle, StepDefinition(1, "eCall Trigger", "Trigger button eCall via ADB", "ADB eCall command success"), trigger_ecall)
            self._record_check_step(cycle, StepDefinition(2, "Status 1 Check", "Check DLT for eCall Status 1", DLT_STATUS_PATTERNS[1]), lambda: wait_for_pattern(DLT_STATUS_PATTERNS[1], STATUS_WAIT_TIMEOUT)[:2])
            self._record_action_step(cycle, StepDefinition(3, "Call Connect", "Answer incoming call on phone", "Phone call connected"), answer_call)
            self._record_check_step(cycle, StepDefinition(4, "Status 2 Check", "Check DLT for eCall Status 2", DLT_STATUS_PATTERNS[2]), lambda: wait_for_pattern(DLT_STATUS_PATTERNS[2], STATUS_WAIT_TIMEOUT)[:2])
            time.sleep(CONNECT_WAIT_SECONDS)
            self._record_action_step(cycle, StepDefinition(5, "Call Disconnect", "End phone call", "Phone call disconnected"), end_call)
            self._record_check_step(cycle, StepDefinition(6, "Status 3 Check", "Check DLT for eCall Status 3", DLT_STATUS_PATTERNS[3]), lambda: wait_for_pattern(DLT_STATUS_PATTERNS[3], STATUS_WAIT_TIMEOUT)[:2])
            time.sleep(CALLBACK_WAIT_SECONDS)
            self._record_check_step(cycle, StepDefinition(7, "Status 0 Check", "Check DLT for callback timeout state", DLT_STATUS_PATTERNS[0]), lambda: wait_for_pattern(DLT_STATUS_PATTERNS[0], STATUS_WAIT_TIMEOUT)[:2])
            if ENABLE_DLT_CLEAR:
                self._record_action_step(cycle, StepDefinition(8, "DLT Clear", "Clear DLT viewer stamp/view for next cycle", "DLT cleared"), lambda: (clear_dlt_view() or "DLT cleared"))
            time.sleep(CYCLE_INTERVAL_SECONDS)
        return self.report.save(self.output_dir / REPORT_FILENAME, self.TC_ID)
