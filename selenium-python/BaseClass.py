import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import requests as re

class SeleniumActions:
        # declare variable for Based class 
    def __init__(self,driver):
        self.driver = driver

    @classmethod
    def __init__(self):
        # Load environment variables from .env file
        print("load the website")
        load_dotenv()

        # Get website URL from environment variables
        self.website_url = os.getenv("WEBSITE_URL")

        # Initialize Chrome WebDriver
        options = webdriver.ChromeOptions()
        # We need to bypass cert and avoid any issue trigger
        options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(options=options)
    # check the respond code 1
        

    @classmethod
    def check_resp_code(self):
        print("checking the website or connectivity is always 200")
        try:
            resp = re.get(self.website_url)

            # checking possiblity 
            if resp.status_code == 200:
                return True
            else :
                print("link not found")
                return False
        except Exception as e : 
            print("Python Error respond" . str(e))
            return False
    
    @classmethod
    def NavigateWeb(self):
        print("Check weather are able to navigate")
        if not self.check_resp_code():
            print("abort link")
            return 
        # Wait for the page to load
        try :
            # Navigate to the website

            self.driver.get(self.website_url)
            # we have to wait 10 milisecond to find keywords
            WebDriverWait(self.driver, 10).until(EC.title_contains("Automation Exercise"))
            print("able to get reterive the link")
        except Exception as e :
            print("Unable to get the link", str(e))

    @classmethod
    def CloseBrowser(self):
        # Close the browser
        self.driver.implicitly_wait(10)
        self.driver.quit()


class RegisterPage():
    def __init__(self,driver):
        self.driver = driver

    def insert_name(self,name):
        NameField =  self.driver.find_element(By.NAME,"name")

        # checking 
        if NameField :
            NameField.send_keys(name)
        else :
            print(f"Unable to locate name field ")

    def insert_email (self,email) : 
        EmailField = self.driver.find_element(By.XPATH,"//input[@data-qa='signup-email']")
        # checking 
        if EmailField : 
            EmailField.send_keys(email)
        else :
            print(f"unable to locate email field")
    
    def btn_register(self, RegisterBtn):
        RegisterBtn = self.driver.find_element(By.XPATH, "//button[@data-qa='signup-button']")
        RegisterBtn.click()

        

        