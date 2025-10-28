from __future__ import annotations

from typing import Iterable, Tuple

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

Locator = Tuple[str, str]


class BasePage:
    """Common helpers shared by all page objects."""

    def __init__(self, driver: WebDriver, timeout: float = 10) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str) -> None:
        self.driver.get(url)

    def click(self, locator: Locator) -> None:
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def fill(self, locator: Locator, value: str, clear: bool = True) -> None:
        element = self.wait.until(EC.visibility_of_element_located(locator))
        if clear:
            element.clear()
        element.send_keys(value)

    def get_text(self, locator: Locator) -> str:
        return self.wait.until(EC.visibility_of_element_located(locator)).text.strip()

    def get_attribute(self, locator: Locator, attribute: str) -> str:
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.get_attribute(attribute)

    def wait_for_elements(self, locator: Locator) -> Iterable:
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def wait_for_alert(self):
        return self.wait.until(EC.alert_is_present())
