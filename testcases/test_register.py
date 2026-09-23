from pages.DWS_register import RegisterPage
from utils.json_utils import generate_dynamic_email, save_user_data


def test_register_user(page):
    register_page = RegisterPage(page)

    firstname = "Test"
    lastname = "Automate"
    password = "Test@123"

    email = generate_dynamic_email()
    register_page.open()

    register_page.register_user(
        firstname=firstname,
        lastname=lastname,
        email=email,
        password=password,
    )

    save_user_data(
        firstname=firstname,
        lastname=lastname,
        email=email,
        password=password,
    )