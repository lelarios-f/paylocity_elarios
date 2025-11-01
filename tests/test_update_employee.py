import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.loginPage import LoginPage
from page_objects.benefitsPage import benefitsPage

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_update_employee(driver):
    loginpage = LoginPage(driver)
    benefitspage = benefitsPage(driver)

    NEW_FIRSTNAME = "UpdatedFirstName"
    NEW_LASTNAME = "UpdatedLastName"
    NEW_DEPENDENTS = "3"

    driver.get("https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/Account/LogIn")

    loginpage.login("TestUser824", "/w]b4xL^2_qX")
    WebDriverWait(driver, 5).until(EC.url_contains("Benefits"))
    
    rowindex = benefitspage.get_rowindex_by_id("72cdc636-632d-43bc-b68c-2cb981775a2b")
    print(f"Updating employee at row index: {rowindex}")

    flags = benefitspage.update_employee_byID(NEW_FIRSTNAME,NEW_LASTNAME, NEW_DEPENDENTS, rowindex)
    benefitspage.update_button_method()

    post_update_details = benefitspage.get_employee_details_byID(rowindex)
    print(f"Post-update details: {post_update_details}")

    if flags[0]:
        assert post_update_details['FirstName'] ==  NEW_FIRSTNAME, "FAIL: First name not updated."
    if flags[1]:
        assert post_update_details['LastName'] == NEW_LASTNAME, "FAIL: Last name not updated."
    if flags[2]:
        assert post_update_details['Dependents'] == NEW_DEPENDENTS, "FAIL: Dependents not updated."
    WebDriverWait(driver, 5).until(EC.url_contains("Benefits")) 
    time.sleep(5) # Just for debugging

    assert "Benefits" in driver.current_url, "FAIL: Did not navigate to Benefits page."

    time.sleep(5)  # Pause for 5 seconds to inspect the browser manually

def test_cancel_update_employee(driver):
    loginpage = LoginPage(driver)
    benefitspage = benefitsPage(driver)

    ORIGINAL_FIRSTNAME = "TestFirstName"
    ORIGINAL_LASTNAME = "TestLastName"
    ORIGINAL_DEPENDENTS = "2"

    driver.get("https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/Account/LogIn")

    loginpage.login("TestUser824", "/w]b4xL^2_qX")
    WebDriverWait(driver, 5).until(EC.url_contains("Benefits"))
    
    rowindex = benefitspage.get_rowindex_by_id("72cdc636-632d-43bc-b68c-2cb981775a2b")
    print(f"Cancelling update for employee at row index: {rowindex}")

    flags = benefitspage.update_employee_byID(ORIGINAL_FIRSTNAME,ORIGINAL_LASTNAME, ORIGINAL_DEPENDENTS, rowindex)
    post_cancel_details = benefitspage.get_employee_details_byID(rowindex)
    benefitspage.cancel_button_method()
    print(f"Post-cancel details: {post_cancel_details}")

    WebDriverWait(driver, 5).until(EC.url_contains("Benefits")) 
    time.sleep(5) # Just for debugging
    assert "Benefits" in driver.current_url, "FAIL: Did not navigate to Benefits page."

    time.sleep(5)  # Pause for 5 seconds to inspect the browser manually