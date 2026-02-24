import time
from time import sleep

from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.HomePage  import HomePage
from pages.SubscriptionPage import SubscriptionPage
from selenium.webdriver.firefox.options import Options

# Initialize Chrome driver
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome()

driver.get("https://soft.reelly.io/sign-in")
#driver = webdriver.Firefox(options=options)

# Step 2: Log in
login = LoginPage(driver)
login.enter_username("kavadiasnadine@gmail.com")
time.sleep(2)
login.enter_password("Jesusholdme1!")
time.sleep(2)
login.click_continue()
sleep(3)

home = HomePage(driver)
home.click_settings()
sleep(2)

home.click_subscription_payments()
subscription = SubscriptionPage(driver)
sleep(2)

assert subscription.is_title_visible(), "Title not visible!"
assert subscription.is_back_button_visible(), "Back button not visible!"
assert subscription.is_upgrade_button_visible(), "Upgrade plan button not visible!"













