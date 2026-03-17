from pathlib import Path
ADB_DEVICE = "0123459786"
ADB_PREFIX = ["adb", "-s", ADB_DEVICE]
ECALL_TRIGGER_COMMAND = ["shell", "/usr/bin/factory/sldd", "ecall", "1"]
ANSWER_CALL_COMMAND = ["shell", "input", "keyevent", "KEYCODE_CALL"]
DLT_LOG_DIR = Path(r"D:\DLT_Log")
DLT_STATUS_PATTERNS = {1:"eCall Status 1",2:"eCall Status 2",3:"eCall Status 3",0:"eCall Status 0"}
BASE_URL = "https://base.example.com/login"
BASE_USERNAME = "your_id"
BASE_PASSWORD = "your_password"
ECU_NUMBER = "002335488812"
LOCATORS = {
    "username": ("id", "username"),
    "password": ("id", "password"),
    "login_button": ("id", "loginBtn"),
    "ecu_search_input": ("id", "ecuSearch"),
    "ecu_search_button": ("id", "searchBtn"),
    "ecu_select_row": ("xpath", "//tr[1]"),
    "msd_position": ("id", "msdPosition"),
    "msd_ecall_type": ("id", "msdType"),
    "msd_car_number": ("id", "carNumber"),
    "ecall_end_button": ("id", "ecallEndBtn"),
}
STATUS_WAIT_TIMEOUT = 30
POLL_INTERVAL = 0.3
BASE_TIMEOUT = 15
CONNECT_WAIT_SECONDS = 10
CALLBACK_WAIT_SECONDS = 120
CYCLE_INTERVAL_SECONDS = 5
TOTAL_DURATION_HOURS = 24
REPORT_FILENAME = "tc2_final_report.xlsx"
HEADLESS = False
