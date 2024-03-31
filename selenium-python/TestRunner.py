from BaseClass import SeleniumActions
from TestClass import MainClass

driver = SeleniumActions()


driver.NavigateWeb()
MainClass.SignupUser(driver)
driver.CloseBrowser()