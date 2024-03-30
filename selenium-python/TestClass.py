import os
import time
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
        self.driver = webdriver.Chrome()
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
    def navigate_to_website(self):
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
    def close_browser(self):
        # Close the browser
        self.driver.quit()

    @classmethod
    def Signup_user(self):
        url_signup = 'https://www.automationexercise.com/login'

        try :
            self.driver.find_element_by_link_text('Signup / Login').click()
            print("redirect to signup / login page")
        except Exception as e :
            print("Unable to get the link", str(e))
       




        

        