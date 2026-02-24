from selenium.webdriver.common.by import By

class SubscriptionPage:
    def __init__(self, driver):
        self.driver = driver
        self.title = (By.XPATH, "//h1[text()='Subscription & payments']")
        self.back_button = (By.ID, "backBtn")
        self.upgrade_button = (By.ID, "upgradePlanBtn")

    def is_title_visible(self):
        return self.driver.find_element(*self.title).is_displayed()

    def is_back_button_visible(self):
        return self.driver.find_element(*self.back_button).is_displayed()

    def is_upgrade_button_visible(self):
        return self.driver.find_element(*self.upgrade_button).is_displayed()
