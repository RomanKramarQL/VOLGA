from __future__ import annotations

import pytest

from pages.click_events_page import ClickEventsPage


@pytest.mark.parametrize(
    "animal, expected_sound",
    [
        ("cat", "Meow!"),
        ("dog", "Woof!"),
        ("pig", "Oink!"),
        ("cow", "Moo!"),
    ],
)
def test_click_events_display_correct_sound(driver, animal: str, expected_sound: str):
    page = ClickEventsPage(driver)
    page.open()

    page.click_animal_button(animal)
    assert page.get_displayed_sound() == expected_sound
