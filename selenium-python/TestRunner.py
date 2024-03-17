from LandingPage import SeleniumActions

actions = SeleniumActions()
actions.navigate_to_website()
    # actions.search_for_product("Selenium")
    # actions.click_on_first_product()
    # actions.add_product_to_cart()
    # actions.verify_product_added_to_cart()
actions.close_browser()