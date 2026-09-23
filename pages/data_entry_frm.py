from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.name_input = page.locator("#name")
        self.email_input = page.locator("#email")
        self.phone_input = page.locator("#phone")
        self.Address_textarea = page.locator("//textarea[@class='form-control']")
        self.gender_male = page.locator("#male")
        self.gender_female = page.locator("#female")
        self.day1=page.locator("#monday")
        self.day2=page.locator("#tuesday")
        self.day3=page.locator("#wednesday")
        self.day4=page.locator("#thursday")
        self.day5=page.locator("#friday")
        self.day6=page.locator("#saturday")
        self.day7=page.locator("#sunday")
        self.Country = page.locator("#country")        
        self.submit_button = page.locator("(//button[text()='Submit'])[1]")

    def fill_form(self, name: str, email: str, phone: str, message: str, country:str):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.phone_input.fill(phone)
        self.Address_textarea.fill(message)
        self.gender_male.click()
        self.day7.click()
        self.day5.check()
        self.Country.select_option(label = country)
        
        

    def submit_form(self):
        self.submit_button.click()