from pages.DWS_login import LoginPage
from utils.json_utils import read_user_data


def test_login_user(page):
    login_page = LoginPage(page)

    user_data = read_user_data()

    email = user_data["email"]
    password = user_data["password"]
    login_page.open()

    login_page.login(email=email, password=password)
    assert login_page.is_logged_in()

