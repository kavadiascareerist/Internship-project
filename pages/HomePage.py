
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.settings_button = (By.XPATH, "//a[contains(@href, '/settings')]")
        self.subscription_button = (
        By.XPATH,
        "//div[@class='setting-text' and normalize-space()='Subscription & payments']"
        )

    def click_settings(self):
        self.wait.until(EC.element_to_be_clickable(self.settings_button)).click()

    def click_subscription_payments(self):
        self.wait.until(EC.element_to_be_clickable(self.subscription_button)).click()



