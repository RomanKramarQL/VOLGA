from __future__ import annotations

from selenium.webdriver.common.by import By

from .base_page import BasePage, Locator


class ClickEventsPage(BasePage):
    url = "https://practice-automation.com/click-events/"

    DEMO_TEXT: Locator = (By.ID, "demo")

    def open(self) -> None:  # type: ignore[override]
        super().open(self.url)

    def click_animal_button(self, animal: str) -> None:
        locator = (
            By.XPATH,
            f"//button[.//b[normalize-space()='{animal.title()}']]",
        )
        self.click(locator)

    def get_displayed_sound(self) -> str:
        return self.get_text(self.DEMO_TEXT)
