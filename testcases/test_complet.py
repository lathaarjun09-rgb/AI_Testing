from playwright.sync_api import expect


def test_form_and_dropdowns(page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.locator("#colors").select_option(["Blue", "Yellow"])
    selected = page.locator("#colors option:checked").all_text_contents()
    assert "Blue" in selected and "Yellow" in selected

    page.locator("#animals").select_option("Elephant")
    expect(page.locator("#animals")).to_have_value("Elephant")

    date_picker_1 = page.locator("#datepicker")
    date_picker_1.fill("09/21/2026")
    expect(date_picker_1).to_have_value("09/21/2026")

    page.locator("input[placeholder='Start Date']").fill("09/01/2026")
    page.locator("input[placeholder='End Date']").fill("09/28/2026")
    expect(page.locator("input[placeholder='Start Date']")).to_have_value("09/01/2026")
    expect(page.locator("input[placeholder='End Date']")).to_have_value("09/28/2026")


def test_new_tab_and_popup(page):
    page.goto("https://testautomationpractice.blogspot.com/")

    with page.expect_page() as new_tab:
        page.get_by_role("button", name="New Tab").click()
    new_page = new_tab.value
    assert new_page.url
    new_page.close()

    with page.expect_popup() as popup:
        page.get_by_role("button", name="Popup Windows").click()
    popup_page = popup.value
    assert popup_page.url
    popup_page.close()

          