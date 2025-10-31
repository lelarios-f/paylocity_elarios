from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException 
import logging

logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class benefitsPage:
    def __init__(self, driver):
        self.driver = driver
        ## ADD
        self.add_employee_button = (By.XPATH, "//button[@id='add']")  
        
        ##TABLE BUTTONS
        #self.update_employee_button = (By.XPATH, "//button[@id='update-employee']") //*[@id="employeesTable"]/thead/tr/th[5]
        self.confirm_delete_button = (By.XPATH, "//*[@id='deleteEmployee']")  

        ## FORMS
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

    def get_rowindex_by_id(self, id = "f6599638-c3de-4800-ac6c-69f66fe63c98"):
        try:
            table = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='employeesTable']"))
            )
            rows = table.find_elements(By.TAG_NAME, "tr")
            for index, row in enumerate(rows[1:], start=1):
                cols = row.find_elements(By.TAG_NAME, "td")
                if cols[0].text == id:
                    return index
            return -1
        except TimeoutException:
            return -1
    
    def delete_employee_byID(self, rowindex = 1):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "employeesTable")))
            delete_button = self.driver.find_element(By.XPATH, f"//*[@id='employeesTable']/tbody/tr[{rowindex}]/td[9]/i[2]")
            delete_button.click()
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.confirm_delete_button)).click()
            
        except TimeoutException:
            pass

    def logout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.logout_button)
        ).click()   
    
    def get_rowcount(self):
        try:
            table = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='employeesTable']"))
            )
            rows = table.find_elements(By.TAG_NAME, "tr")
            return len(rows) - 1  # Subtract 1 for the header row
        except TimeoutException:
            return 0
