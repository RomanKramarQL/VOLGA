from __future__ import annotations

from pages.popups_page import PopupsPage


def test_alert_popup(driver):
    page = PopupsPage(driver)
    page.open()

    alert = page.trigger_alert()
    assert alert.text == "Hi there, pal!"
    alert.accept()


def test_confirm_popup_accept_and_dismiss(driver):
    page = PopupsPage(driver)
    page.open()

    alert = page.trigger_confirm()
    assert alert.text == "OK or Cancel, which will it be?"
    alert.accept()
    assert page.get_confirm_result() == "OK it is!"

    alert = page.trigger_confirm()
    alert.dismiss()
    assert page.get_confirm_result() == "Cancel it is!"


def test_prompt_popup_accept_and_cancel(driver):
    page = PopupsPage(driver)
    page.open()

    alert = page.trigger_prompt()
    alert.send_keys("SimbirSoft")
    alert.accept()
    assert page.get_prompt_result() == "Nice to meet you, SimbirSoft!"

    alert = page.trigger_prompt()
    alert.dismiss()
    assert page.get_prompt_result() == "Fine, be that way..."


def test_tooltip_visibility_toggle(driver):
    page = PopupsPage(driver)
    page.open()

    page.toggle_tooltip()
    assert page.tooltip_is_visible()

    page.toggle_tooltip()
    assert not page.tooltip_is_visible()
