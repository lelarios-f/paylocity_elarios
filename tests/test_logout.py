import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.loginPage import LoginPage
from page_objects.benefitsPage import benefitsPage
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_logout(driver):
    loginpage = LoginPage(driver)
    benefitspage = benefitsPage(driver)

    driver.get("https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/Account/LogIn")

    loginpage.login("TestUser824", "/w]b4xL^2_qX")
    WebDriverWait(driver, 5).until(EC.url_contains("Benefits"))
    
    benefitspage.logout()
    WebDriverWait(driver, 5).until(EC.url_contains("LogIn"))

    assert "LogIn" in driver.current_url, "FAIL: Did not navigate to LogIn page."

    time.sleep(5)  # Pause for 5 seconds to inspect the browser manually