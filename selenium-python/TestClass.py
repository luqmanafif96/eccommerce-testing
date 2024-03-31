import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from BaseClass import RegisterPage, SeleniumActions

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


        register_page.insert_name('TestUser 123')
        self.driver.implicitly_wait(10) 
        register_page.insert_email('afif123@email.com')
        self.driver.implicitly_wait(10) 
        register_page.btn_register(self)
        self.driver.implicitly_wait(10) 



        
       




        

        