import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.loginPage import LoginPage
from page_objects.benefitsPage import benefitsPage

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_add_new_employee(driver):
    loginpage = LoginPage(driver)
    driver.get("https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/Account/LogIn")
    loginpage.login("TestUser824", "/w]b4xL^2_qX")
    WebDriverWait(driver, 5).until(EC.url_contains("Benefits"))

    benefitspage = benefitsPage(driver)
    count_before = benefitspage.get_rowcount()
    benefitspage.click_add_employee("Eduardo", "Larios")
    time.sleep(5)  # Just for debugging
    count_after = benefitspage.get_rowcount()
    assert count_after == count_before + 1, "FAIL: New employee not registered."

def test_cancel_add_new_employee(driver):
    loginpage = LoginPage(driver)
    driver.get("https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/Account/LogIn")
    loginpage.login("TestUser824", "/w]b4xL^2_qX")
    WebDriverWait(driver, 5).until(EC.url_contains("Benefits"))

    benefitspage = benefitsPage(driver)
    count_before = benefitspage.get_rowcount()
    benefitspage.click_cancel_popup("Eduardo", "Larios")
    time.sleep(5)  # Just for debugging
    count_after = benefitspage.get_rowcount()
    assert count_before == count_after, "FAIL: Cancel button not working"


    


