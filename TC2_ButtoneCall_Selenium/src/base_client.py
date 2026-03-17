from __future__ import annotations
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_PASSWORD, BASE_TIMEOUT, BASE_URL, BASE_USERNAME, ECU_NUMBER, HEADLESS, LOCATORS

BY_MAP = {"id": By.ID, "name": By.NAME, "xpath": By.XPATH, "css": By.CSS_SELECTOR, "class": By.CLASS_NAME}

class BaseClient:
    def __init__(self) -> None:
        options = Options()
        if HEADLESS:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1600,1000")
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, BASE_TIMEOUT)

    def _find(self, key: str):
        by_name, locator = LOCATORS[key]
        return self.wait.until(EC.presence_of_element_located((BY_MAP[by_name], locator)))

    def login(self) -> str:
        self.driver.get(BASE_URL)
        self._find("username").clear(); self._find("username").send_keys(BASE_USERNAME)
        self._find("password").clear(); self._find("password").send_keys(BASE_PASSWORD)
        self._find("login_button").click()
        return "BASE login success"

    def search_ecu(self, ecu_number: str = ECU_NUMBER) -> str:
        self._find("ecu_search_input").clear()
        self._find("ecu_search_input").send_keys(ecu_number)
        self._find("ecu_search_button").click()
        return f"ECU searched: {ecu_number}"

    def select_ecu(self) -> str:
        self._find("ecu_select_row").click()
        return "ECU selected"

    def verify_msd(self) -> str:
        pos = self._find("msd_position").text.strip()
        ecall_type = self._find("msd_ecall_type").text.strip()
        car_number = self._find("msd_car_number").text.strip()
        if not (pos and ecall_type and car_number):
            raise RuntimeError("MSD data is empty or incomplete")
        return f"position={pos}, ecall_type={ecall_type}, car_number={car_number}"

    def end_ecall(self) -> str:
        self._find("ecall_end_button").click()
        return "BASE eCall End clicked"

    def close(self) -> None:
        self.driver.quit()
