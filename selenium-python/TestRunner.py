from BaseClass import SeleniumActions
from TestClass import MainClass

<<<<<<< HEAD
actions = SeleniumActions()
actions.navigate_to_website()
actions.Signup_user()
    # actions.search_for_product("Selenium")
    # actions.click_on_first_product()
    # actions.add_product_to_cart()
    # actions.verify_product_added_to_cart()
actions.close_browser()
=======
driver = SeleniumActions()


driver.NavigateWeb()
MainClass.SignupUser(driver)
driver.CloseBrowser()
>>>>>>> d2c7fb4f5aa89f1a9b4912873590d0e43f0044cf
