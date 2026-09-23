from playwright.sync_api import Page

class OrangehrmLogin:
    
    def __init__(self,page:Page):
        self.page = page
        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_role("textbox", name = "password")
        self.login_button = page.get_bu_role("button",name =" Login ")
    
    def open_hrm_url(self,url):
        self.page.goto(url)
        
    def login_hrm(self,username,password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()        
        