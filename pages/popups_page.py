from __future__ import annotations

from selenium.webdriver.common.by import By

from .base_page import BasePage, Locator


class PopupsPage(BasePage):
    url = "https://practice-automation.com/popups/"

    ALERT_BUTTON: Locator = (By.ID, "alert")
    CONFIRM_BUTTON: Locator = (By.ID, "confirm")
    PROMPT_BUTTON: Locator = (By.ID, "prompt")
    CONFIRM_RESULT: Locator = (By.ID, "confirmResult")
    PROMPT_RESULT: Locator = (By.ID, "promptResult")
    TOOLTIP_TRIGGER: Locator = (By.CSS_SELECTOR, ".tooltip_1")
    TOOLTIP_TEXT: Locator = (By.ID, "myTooltip")

    def open(self) -> None:  # type: ignore[override]
        super().open(self.url)

    def trigger_alert(self):
        self.click(self.ALERT_BUTTON)
        return self.wait_for_alert()

    def trigger_confirm(self):
        self.click(self.CONFIRM_BUTTON)
        return self.wait_for_alert()

    def trigger_prompt(self):
        self.click(self.PROMPT_BUTTON)
        return self.wait_for_alert()

    def get_confirm_result(self) -> str:
        return self.get_text(self.CONFIRM_RESULT)

    def get_prompt_result(self) -> str:
        return self.get_text(self.PROMPT_RESULT)

    def toggle_tooltip(self) -> None:
        self.click(self.TOOLTIP_TRIGGER)

    def tooltip_is_visible(self) -> bool:
        class_value = self.get_attribute(self.TOOLTIP_TEXT, "class")
        return "show" in class_value.split()
