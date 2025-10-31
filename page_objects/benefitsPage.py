from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException 

class benefitsPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_employee_button = (By.XPATH, "//button[@id='add']")  
        #self.update_employee_button = (By.XPATH, "//button[@id='update-employee']")
        #self.delete_employee_button = (By.XPATH, "//button[@id='delete-employee']") 
        self.logout_button = (By.XPATH , "/html/body/header/nav/div/ul/li/a") 
        self.firstname_input = (By.XPATH, "//input[@id='firstName']")
        self.lastname_input = (By.XPATH, "//input[@id='lastName']") 
        self.dependents_input = (By.XPATH, "//input[@id='dependants']") 
        self.add_popup_button = (By.XPATH, "//button[@id='addEmployee']") 
        self.cancel_popup_button = (By.XPATH, "//button[@class='btn btn-secondary']") 

    def click_add_employee(self, firstname, lastname, dependents = "0"):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_employee_button)
        ).click()
        self.driver.find_element(*self.firstname_input).send_keys(firstname)
        self.driver.find_element(*self.lastname_input).send_keys(lastname)
        self.driver.find_element(*self.dependents_input).send_keys(dependents)
        self.driver.find_element(*self.add_popup_button).click()

    def click_cancel_popup(self, firstname, lastname, dependents = "0"):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_employee_button)
        ).click()
        self.driver.find_element(*self.firstname_input).send_keys(firstname)
        self.driver.find_element(*self.lastname_input).send_keys(lastname)
        self.driver.find_element(*self.dependents_input).send_keys(dependents)
        self.driver.find_element(*self.cancel_popup_button).click()
    


