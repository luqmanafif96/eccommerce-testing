import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import requests as re

class SeleniumActions:
    @classmethod
    def __init__(self):
        # Load environment variables from .env file
        print("load the website")
        load_dotenv()

        # Get website URL from environment variables
        self.website_url = os.getenv("WEBSITE_URL")

        # Initialize Chrome WebDriver
        options = webdriver.ChromeOptions()
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

    @classmethod
    def SignupUser(self):
        

        try :
            self.driver.find_element_by_link_text('Signup / Login').click()
            self.driver.implicitly_wait(10)
            print("redirect to signup / login page")
        except Exception as e :
            print("Unable to get the link", str(e))

        # locate the name and Email address
        # Declare the email and the name

        NameField =  self.driver.find_element(By.NAME,"name")
        EmailField =  self.driver.find_element(By.XPATH,"//input[@data-qa='signup-email']")
        BtnSignUp = self.driver.find_element(By.XPATH, "//button[@data-qa='signup-button']")

        # # check is the attribute require field is present 
        # name_required = "required" in NameField.get_attribute("outerHTML")
        # email_required = "required" in EmailField.get_attribute("outerHTML")

        # print("Name field is required:", name_required)
        # print("Email field is required:", email_required)

        # send without the data 
        # NameField.clear()
        # EmailField.clear()
        # BtnSignUp.click()
        # self.driver.implicitly_wait(10) 
        # send the keys
        NameField.send_keys('TestUser 123')
        self.driver.implicitly_wait(10) 
        EmailField.send_keys('afif123@email.com')
        self.driver.implicitly_wait(10) 
        BtnSignUp.click()
        self.driver.implicitly_wait(10) 



        
       




        

        