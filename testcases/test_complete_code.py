import pytest
from playwright.sync_api import expect


def test_simple_alert(page):
    page.goto("https://testautomationpractice.blogspot.com/")

    with page.expect_dialog() as dialog_info:
        page.get_by_role("button", name="Simple Alert").click()

    dialog = dialog_info.value
    assert dialog.type == "alert"
    dialog.accept()


def test_confirmation_alert_accept(page):
    page.goto("https://testautomationpractice.blogspot.com/")

    with page.expect_dialog() as dialog_info:
        page.get_by_role("button", name="Confirmation Alert").click()

    dialog = dialog_info.value
    assert dialog.type == "confirm"
    dialog.accept()


def test_confirmation_alert_cancel(page):
    page.goto("https://testautomationpractice.blogspot.com/")

    with page.expect_dialog() as dialog_info:
        page.get_by_role("button", name="Confirmation Alert").click()

    dialog = dialog_info.value
    assert dialog.type == "confirm"
    dialog.dismiss()


def test_prompt_alert(page):
    page.goto("https://testautomationpractice.blogspot.com/")

    with page.expect_dialog() as dialog_info:
        page.get_by_role("button", name="Prompt Alert").click()

    dialog = dialog_info.value
    assert dialog.type == "prompt"
    dialog.accept("Playwright Python")


def test_dynamic_button(page):
    page.goto("https://testautomationpractice.blogspot.com/")
    button = page.get_by_role("button", name="START")
    assert button.is_visible()
    button.click()
    assert button.is_visible()


def test_mouse_hover(page):
    page.goto("https://testautomationpractice.blogspot.com/")
    button = page.get_by_role("button", name="Point Me")
    button.hover()
    expect(button).to_be_visible()


def test_double_click_and_copy(page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.locator("input").nth(0).fill("Hello World!")
    page.get_by_role("button", name="Copy Text").dblclick()
    expect(page.locator("input").nth(1)).to_have_value("Hello World!")


def test_drag_and_drop(page):
    page.goto("https://testautomationpractice.blogspot.com/")
    drag = page.locator("text=Drag me to my target")
    drop = page.locator("text=Drop here")
    if drag.count() > 0 and drop.count() > 0:
        drag.first.drag_to(drop.first)
        expect(page.locator("text=Drop here")).to_be_visible()


def test_slider(page):
    page.goto("https://testautomationpractice.blogspot.com/")
    slider = page.locator("input[type='range'], [role='slider']").first
    if slider.count() == 0:
        pytest.skip("Range slider is not present on the page")
    slider.fill("200")
    assert slider.is_visible()


def test_svg_elements(page):
    page.goto("https://testautomationpractice.blogspot.com/")
    assert page.locator("svg").count() >= 1
    page.locator("svg").first.click()


def test_scrolling_dropdown(page):
    page.goto("https://testautomationpractice.blogspot.com/")
    dropdown = page.locator("input[placeholder='Select an item'], input[aria-label='Select an item']").first
    if dropdown.count() == 0:
        pytest.skip("Scrolling dropdown is not available")
    dropdown.fill("Item 5")
    expect(dropdown).to_have_value("Item 5")


def test_static_web_table(page):
    page.goto("https://testautomationpractice.blogspot.com/")
    table = page.locator("table").first
    assert table.locator("tr").count() >= 5
    assert "Learn Selenium" in table.text_content()


def test_dynamic_web_table(page):
    page.goto("https://testautomationpractice.blogspot.com/")
    table = page.locator("table").nth(1)
    assert table.locator("tr").count() >= 4
    assert "System" in table.text_content()


def test_pagination_web_table(page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page_numbers = page.locator("a:has-text('2'), a:has-text('3'), a:has-text('4')")
    if page_numbers.count() > 0:
        page_numbers.first.click()
    assert page.locator("table").count() >= 1


def test_form_and_shadow_dom(page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.locator("input[placeholder='Enter Name']").fill("Test User")
    page.locator("input[placeholder='Enter EMail']").fill("testuser@example.com")
    page.locator("input[placeholder='Enter Phone']").fill("9876543210")
    page.locator("textarea[placeholder='Address:']").fill("Hitech City")
    page.locator("input[value='Male']").check()
    page.locator("input[type='checkbox']").nth(0).check()
    page.locator("#country").select_option("India")
    assert page.evaluate("() => !!document.body.shadowRoot") is False


def test_new_tab(page):
    page.goto("https://testautomationpractice.blogspot.com/")
    with page.expect_page() as new_tab:
        page.get_by_role("button", name="New Tab").click()
    new_page = new_tab.value
    assert new_page.url.startswith("http")
    new_page.close()


def test_popup_window(page):
    page.goto("https://testautomationpractice.blogspot.com/")
    with page.expect_popup() as popup:
        page.get_by_role("button", name="Popup Windows").click()
    popup_page = popup.value
    assert popup_page.url.startswith("http")
    popup_page.close()
