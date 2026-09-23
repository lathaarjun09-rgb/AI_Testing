from pages.data_entry_frm import HomePage


def test_form(page):
    page.goto("https://testautomationpractice.blogspot.com/")
    home = HomePage(page)
    home.fill_form("testuser","test@gmail.com","7890989090","East coast","India")
    home.submit_form()
    print("Form filled successfully")
    