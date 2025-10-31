import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.loginPage import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_add_new_employee(driver):
    loginpage = LoginPage(driver)
    driver.get("https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/Account/LogIn")

    loginpage.login("TestUser824", "/w]b4xL^2_qX")
    WebDriverWait(driver, 5).until(EC.url_contains("Benefits"))

    

    # Additional steps to add a new employee would go here
    # For example:
    # employee_page = EmployeePage(driver)
    # employee_page.add_new_employee("John", "Doe", "