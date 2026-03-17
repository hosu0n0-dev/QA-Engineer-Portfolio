from pathlib import Path
ADB_DEVICE = "0123459786"
ADB_PREFIX = ["adb", "-s", ADB_DEVICE]
ECALL_TRIGGER_COMMAND = ["shell", "/usr/bin/factory/sldd", "ecall", "1"]
ANSWER_CALL_COMMAND = ["shell", "input", "keyevent", "KEYCODE_CALL"]
END_CALL_COMMAND = ["shell", "input", "keyevent", "KEYCODE_ENDCALL"]
DLT_LOG_DIR = Path(r"D:\DLT_Log")
DLT_STATUS_PATTERNS = {1:"eCall Status 1",2:"eCall Status 2",3:"eCall Status 3",0:"eCall Status 0"}
STATUS_WAIT_TIMEOUT = 30
POLL_INTERVAL = 0.3
CONNECT_WAIT_SECONDS = 10
CALLBACK_WAIT_SECONDS = 120
CYCLE_INTERVAL_SECONDS = 5
TOTAL_DURATION_HOURS = 24
REPORT_FILENAME = "tc1_final_report.xlsx"
ENABLE_DLT_CLEAR = False
