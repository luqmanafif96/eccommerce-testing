import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from BaseClass import RegisterPage, SeleniumActions
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

class MainClass(SeleniumActions,RegisterPage):
    # call from Based Class
    def __init__(self,driver):
        super.__init__(driver)

    @staticmethod
    def SignupUser(self):
        
    
        try :
            self.driver.find_element_by_link_text('Signup / Login').click()
            self.driver.implicitly_wait(10)
            print("redirect to signup / login page")
        except Exception as e :
            print("Unable to get the link", str(e))

        # locate the name and Email address
        # Declare the email and the name

        # NameField =  self.driver.find_element(By.NAME,"name")
        # EmailField =  self.driver.find_element(By.XPATH,"//input[@data-qa='signup-email']")
        register_page = RegisterPage(self.driver)
        # BtnSignUp = self.driver.find_element(By.XPATH, "//button[@data-qa='signup-button']")
        # declare the class wau
        Waitforload = self.driver.implicitly_wait(10) 

        #Register name 
        register_page.insert_name('TestUser 123')
        Waitforload
        #register enmail
        register_page.insert_email('afif123@email.com')
        Waitforload
        try :
            response = re.get(self.website_url+'/signup')
            if response.status_code>= 200 and response.status_code < 300 :
                print("Link is valid")
            else:
                print("The link is not valid. Status code:", response.status_code)
            register_page.btn_register(self)
            Waitforload
            register_page.select_male(self)
            Waitforload
            register_page.select_female(self)
            Waitforload
            register_page.select_male(self)

        except re.exceptions.RequestException as e :
            print("Having trouble to access")




        
       




        

        