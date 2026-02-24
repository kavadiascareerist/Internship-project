from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.settings_button = (By.ID, "settingsBtn")
        self.subscription_option = (By.ID, "subscriptionPaymentsBtn")

    def click_settings(self):
        self.driver.find_element(*self.settings_button).click()

    def click_subscription_payments(self):
        self.driver.find_element(*self.subscription_option).click()


