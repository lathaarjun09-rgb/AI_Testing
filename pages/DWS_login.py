from playwright.sync_api import Page

class LoginPage:
    
    def __init__(self, page: Page):
        self.page = page
        self.loginlink = page.locator(".ico-login")
        self.email = page.locator("#Email")
        self.password = page.locator("#Password")
        self.login_button = page.locator("input.login-button")
        self.logoutlink = page.locator(".ico-logout")
    
    def open(self):
        self.page.goto("https://demowebshop.tricentis.com/")
        self.loginlink.click()

    def login(self, email, password):
        self.email.fill(email)
        self.password.fill(password)
        self.login_button.click()
        
    def is_logged_in(self):
        return self.logoutlink.is_visible()    