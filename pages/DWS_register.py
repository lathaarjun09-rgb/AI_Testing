from playwright.sync_api import Page


class RegisterPage:
    
    def __init__(self, page: Page):
        self.page = page
        self.registerlink = page.locator(".ico-register")
        self.gender_male = page.locator("#gender-male") #id:css selctor   
        self.gender_female = page.locator("#gender-female")
        self.firstname = page.locator("#FirstName")
        self.lastname = page.locator("#LastName")
        self.email = page.locator("#Email")
        self.password = page.locator("#Password")
        self.confirm_password = page.locator("#ConfirmPassword")
        self.register_button = page.locator("#register-button")

    def open(self):
        self.page.goto("https://demowebshop.tricentis.com/")

    def register_user(self, firstname, lastname, email, password):
        self.registerlink.click()
        self.gender_female.check()
        self.firstname.fill(firstname)
        self.lastname.fill(lastname)
        self.email.fill(email)
        self.password.fill(password)
        self.confirm_password.fill(password)
        self.register_button.click()
    
    
        