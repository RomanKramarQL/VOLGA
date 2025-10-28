from __future__ import annotations

from typing import Iterable, List

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from .base_page import BasePage, Locator


class FormFieldsPage(BasePage):
    url = "https://practice-automation.com/form-fields/"

    NAME_INPUT: Locator = (By.ID, "name-input")
    PASSWORD_INPUT: Locator = (By.XPATH, "//label[normalize-space()='Password']/input")
    DRINK_CHECKBOX_TEMPLATE = (By.CSS_SELECTOR, "input[name='fav_drink'][value='{value}']")
    COLOR_RADIO_TEMPLATE = (By.CSS_SELECTOR, "input[name='fav_color'][value='{value}']")
    AUTOMATION_SELECT: Locator = (By.ID, "automation")
    AUTOMATION_OPTION_TEMPLATE = (By.CSS_SELECTOR, "#automation option[value='{value}']")
    EMAIL_INPUT: Locator = (By.ID, "email")
    MESSAGE_AREA: Locator = (By.ID, "message")
    SUBMIT_BUTTON: Locator = (By.ID, "submit-btn")
    AUTOMATION_TOOLS_ITEMS: Locator = (
        By.XPATH,
        "//label[normalize-space()='Automation tools']/following-sibling::ul[1]/li",
    )

    def open(self) -> None:  # type: ignore[override]
        super().open(self.url)

    def fill_name(self, name: str) -> None:
        self.fill(self.NAME_INPUT, name)

    def fill_password(self, password: str) -> None:
        self.fill(self.PASSWORD_INPUT, password)

    def select_drinks(self, drinks: Iterable[str]) -> None:
        for drink in drinks:
            locator = self._format_locator(self.DRINK_CHECKBOX_TEMPLATE, drink)
            self.click(locator)

    def choose_color(self, color_value: str) -> None:
        locator = self._format_locator(self.COLOR_RADIO_TEMPLATE, color_value)
        self.click(locator)

    def choose_automation_option(self, value: str) -> None:
        select_element = self.wait.until(
            lambda driver: Select(driver.find_element(*self.AUTOMATION_SELECT))
        )
        select_element.select_by_value(value)

    def fill_email(self, email: str) -> None:
        self.fill(self.EMAIL_INPUT, email)

    def fill_message_with_tools(self) -> str:
        tools = self.get_automation_tools()
        message = "\n".join(tools)
        self.fill(self.MESSAGE_AREA, message)
        return message

    def get_automation_tools(self) -> List[str]:
        elements = self.wait_for_elements(self.AUTOMATION_TOOLS_ITEMS)
        return [element.text.strip() for element in elements]

    def submit_form(self):
        self.click(self.SUBMIT_BUTTON)
        return self.wait_for_alert()

    def get_message_value(self) -> str:
        return self.get_attribute(self.MESSAGE_AREA, "value") or ""

    def any_drink_selected(self) -> bool:
        checkboxes = self.wait_for_elements((By.CSS_SELECTOR, "input[name='fav_drink']"))
        return any(box.is_selected() for box in checkboxes)

    def selected_color(self) -> str | None:
        radios = self.driver.find_elements(By.CSS_SELECTOR, "input[name='fav_color']")
        for radio in radios:
            if radio.is_selected():
                return radio.get_attribute("value")
        return None

    def selected_automation_value(self) -> str:
        select = Select(self.driver.find_element(*self.AUTOMATION_SELECT))
        return select.first_selected_option.get_attribute("value")

    def _format_locator(self, locator_template: Locator, value: str) -> Locator:
        by, pattern = locator_template
        return by, pattern.format(value=value)
