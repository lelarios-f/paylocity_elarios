import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.loginPage import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_valid_login():
    driver = webdriver.Chrome()
    loginpage = LoginPage(driver)
    driver.get("https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/Account/LogIn")

    loginpage.login("TestUser824", "/w]b4xL^2_qX")
    WebDriverWait(driver, 5).until(EC.url_contains("Benefits"))
    assert "Benefits" in driver.current_url
    time.sleep(2) # Just for debugging

def test_invalid_login():
    driver = webdriver.Chrome()
    loginpage = LoginPage(driver)
    driver.get("https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/Account/LogIn")
    loginpage.login("TestUser824", "WrongPassword") #Tested only with incorrect password since the app crashes with the wrong username
    time.sleep(2) #Intended to wait for the err msg 
    error_message = driver.find_element(By.XPATH, "/html/body/div/main/div/div/form/div[1]").text
    print(error_message)
    assert "The specified username or password is incorrect." in error_message
    time.sleep(2)
