from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.settings_button = (By.XPATH, "//a[@href='/settings']")  # replace with actual

    def click_settings(self):
        self.driver.find_element(*self.settings_button).click()
