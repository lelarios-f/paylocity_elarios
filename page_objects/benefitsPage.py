from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException 
import logging
import time

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
        self.cancel_popup_button_delete = (By.XPATH, " //*[@id='deleteModal']/div/div/div[3]/button[2]")  
        self.update_button = (By.XPATH, "//*[@id='updateEmployee']")

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

    def get_rowindex_by_id(self, id):
        try:
            table = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='employeesTable']"))
            )
            time.sleep(2)  # Wait for 2 seconds to ensure the table is fully loaded
            rows = table.find_elements(By.TAG_NAME, "tr")
            print(f"Total rows found (including header): {len(rows)}")
            for index, row in enumerate(rows[1:], start=1):
                cols = row.find_elements(By.TAG_NAME, "td")
                print(f"Checking row {index} with ID {cols[0].text}")
                if cols[0].text == id:
                    print(f"ID {id} found at row index {index}.")
                    return index
            print(f"ID {id} not found in the table.")
            return -1  # ID not found
        except TimeoutException:
            print("Timeout while locating the employees table.")
            return -1
    
    def delete_employee_byID(self, rowindex = 1):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "employeesTable")))
            delete_button = self.driver.find_element(By.XPATH, f"//*[@id='employeesTable']/tbody/tr[{rowindex}]/td[9]/i[2]")
            delete_button.click()
            
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
            time.sleep(3) #make sure the table is fully loaded
            rows = table.find_elements(By.TAG_NAME, "tr")
            return len(rows) - 1  # Subtract 1 for the header row
        except TimeoutException:
            return 0
        
    def update_employee_byID(self, fname = None,lname = None, dependents = None, rowindex = 1):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "employeesTable")))
            update_button = self.driver.find_element(By.XPATH, f"//*[@id='employeesTable']/tbody/tr[{rowindex}]/td[9]/i[1]")
            update_button.click()
            flags = [False, False, False]

            if fname:
                firstname_input = self.driver.find_element(*self.firstname_input)
                firstname_input.clear()
                firstname_input.send_keys(fname)
                flags[0] = True
            if lname:
                lastname_input = self.driver.find_element(*self.lastname_input)
                lastname_input.clear()
                lastname_input.send_keys(lname)
                flags[1] = True
            if dependents:
                dependents_input = self.driver.find_element(*self.dependents_input)
                dependents_input.clear()
                dependents_input.send_keys(dependents)
                flags[2] = True
            return flags
            
        except TimeoutException:
            pass

    def get_employee_details_byID(self, rowindex = 1):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "employeesTable")))
            table = self.driver.find_element(By.ID, "employeesTable")
            row = table.find_element(By.XPATH, f"./tbody/tr[{rowindex}]")
            cols = row.find_elements(By.TAG_NAME, "td")
            employee_details = {
                "ID": cols[0].text,
                "FirstName": cols[1].text,
                "LastName": cols[2].text,
                "Dependents": cols[3].text,
                "Salary": cols[4].text,
                "BenefitCost": cols[5].text,
                "NetPay": cols[6].text
            }
            return employee_details
        except TimeoutException:
            return {}

    def cancel_button_method(self, is_delete = False):
        if is_delete:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.cancel_popup_button_delete)
            ).click()
            return
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cancel_popup_button)
        ).click()
    
    def update_button_method(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.update_button)
        ).click()

    def delete_button_method(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.confirm_delete_button)
        ).click()