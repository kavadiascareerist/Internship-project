from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "email-2")
        self.password_input = (By.ID, "field")
        self.continue_button = By.XPATH, "//a[@wized='loginButton']"

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()
