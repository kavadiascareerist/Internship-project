from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "email-2")
        self.password_field = By.ID, "field"
        self.login = (By.CSS_SELECTOR,"login-button w-button")

    def enter_username(self, username):
       self.driver.find_element(*self.username_field).send_keys("kavadiasnadine@gmail.com")

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys("Jesusholdme1!")

    def click_login(self):
       self.driver.find_element(*self.continue_button).click()

    def login_as(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
