from selenium.webdriver.common.by import By

class SubscriptionPage:
    def __init__(self, driver):
        self.driver = driver
        self.page_title = (By.XPATH, "//a[@href='/subscription']")
        self.back_button =(By.CSS_SELECTOR, ".back-text")
        self.upgrade_plan_button = (By.CSS_SELECTOR,".button-verify w-inline-block")

    #def verify_page_opened(self):

        #return "subscription" in self.driver.current_url

    #def get_title_text(self):
        #return self.driver.find_element(*self.page_title).text

    #def is_back_button_visible(self):
        #return self.driver.find_element(*self.back_button).is_displayed()

    #def is_upgrade_plan_button_visible(self):
        #return self.driver.find_element(*self.upgrade_plan_button).is_displayed()
