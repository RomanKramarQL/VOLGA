from __future__ import annotations

import re

from pages.form_fields_page import FormFieldsPage


def test_form_submission_resets_fields(driver):
    page = FormFieldsPage(driver)
    page.open()

    page.fill_name("Automation Aficionado")
    page.fill_password("SuperSecure!123")
    page.select_drinks(["Water", "Ctrl-Alt-Delight"])
    page.choose_color("Blue")
    page.choose_automation_option("yes")
    page.fill_email("automation@example.com")

    message = page.fill_message_with_tools()
    tools = page.get_automation_tools()
    for tool in tools:
        assert re.search(rf"\\b{re.escape(tool)}\\b", message)

    alert = page.submit_form()
    assert alert.text == "Message received!"
    alert.accept()

    assert page.get_message_value() == ""
    assert not page.any_drink_selected()
    assert page.selected_color() is None
    assert page.selected_automation_value() == "default"
