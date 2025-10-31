import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.loginPage import LoginPage
from page_objects.benefitsPage import benefitsPage

from selenium import webdriver
from selenium.webdriver.common.by import By

rowindex = 1 # Default row index

def test_delete_employee(driver):
    loginpage = LoginPage(driver)
    benefits_page = benefitsPage(driver)

    driver.get("https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/Account/LogIn")

    loginpage.login("TestUser824", "/w]b4xL^2_qX")
    WebDriverWait(driver, 5).until(EC.url_contains("Benefits"))

    #-- Get row index by ID (uncomment to use) ---
    #rowindex = benefits_page.get_rowindex_by_id("f6599638-c3de-4800-ac6c-69f66fe63c98")  

    count_before = benefits_page.get_rowcount()
    benefits_page.delete_employee_byID(rowindex)
    count_before_after = benefits_page.get_rowcount()

    assert count_before_after == count_before - 1, "FAIL: Employee not deleted."

    

    time.sleep(5)  # Pause for 5 seconds to inspect the browser manually