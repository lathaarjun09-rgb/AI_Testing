from palywright.sync_api import Page,expect

class EmployeePage:
    
    def __init__(self,page=Page):
        self.page = page
        
        self.pim_menu = page.get_by_text("PIM",exact = True)
        self.employee_list = page.get_by_text("Employee List",exact = True)
        self.employee_information = page.get_by_text("Employee Information", exact =True)
        
        #dropdown
        self.employment_status= page.locator("label").filter(has_text="Employment Status").locator("..").locator(".oxd-select-text")
        
        self.include_dropdown = page.locator("label").filter(has_text = "Include")..locator("..").locator(".oxd-select-text")
	self.search_button=page.get_by_role("button",name = " Search ")
        
    def click_pim(self):
        self.pim_menu.click()
        
    def click_employee_list(self):
         self.employee_list.click()

    def select_dropdown(self,dropdown,option):
	dropdown.click()
	option_locator = self.page.get_by_text(option,exact=True)
	option_locator.wait_for(state="visible")
	option_locator.click()
    def select_employement_status(sel,status):
	self.select_dropdown(self.employment_status,status)
    def select_include(self,include):
	self.select_dropdown(self.include_dropdown,include)
    def click_search(self):
	self.search_button.click()
		        