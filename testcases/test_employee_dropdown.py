from pages.orange_hrm_login import OrangehrmLogin
from pages.employee_page import EmployeePage
from utils.config import Config

def test_employement_status_dropdown(page):
login_page = OrangehrmLogin(page)
login_page.open(Config.base_url_ohrm)

login_page.login(Config.USERNAME,Config.PASSWORD)

employee_page = EmployeePage(page)
employee_page.click_pim()
employee_page.click_employee_list()
employee_page.select_dropdown()
employee_page.select_employement_status()
employee_page.select_include()
employee_page.click_search()
print("Test case executed successfully")












