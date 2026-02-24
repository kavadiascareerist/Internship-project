from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.settings_button = (By.XPATH, "//a[contains(@href, '/settings')]")
        self.subscription_button = (
            By.XPATH,
            "//div[@class='setting-text' and normalize-space()='Subscription & payments']"
        )
        #self.subscription_option = (By.ID, "subscriptionPaymentsBtn")
        self.home_page = (By.XPATH, "//span[text()='Settings']")



    def click_settings(self):
        self.driver.find_element(*self.settings_button).click()

    def click_subscription_payments(self):
        self.driver.find_element(*self.subscription_button).click()




