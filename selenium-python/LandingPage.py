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
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()

        # Get website URL from environment variables
        self.website_url = os.getenv("WEBSITE_URL")

        # Initialize Chrome WebDriver
        self.driver = webdriver.Chrome()
    # check the respond code 1
    def check_resp_code(self):
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
    

    def navigate_to_website(self):
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

    def close_browser(self):
        # Close the browser
        self.driver.quit()

# Example usage:
if __name__ == "__main__":
    actions = SeleniumActions()
    actions.navigate_to_website()
    # actions.search_for_product("Selenium")
    # actions.click_on_first_product()
    # actions.add_product_to_cart()
    # actions.verify_product_added_to_cart()
    actions.close_browser()
