from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from pages.SubscriptionPage import SubscriptionPage


USERNAME = "kavadiasnadine_xo7NSM"
ACCESS_KEY = "RVeyucV1rHKSVxRfdyej"


bstack_options = {
    "os": "Windows",
    "osVersion": "10",
    "buildName": "Subscription Flow Build 1",
    "sessionName": "Subscription Test",
    "local": False
}

chrome_options = Options()
chrome_options.set_capability("browserName", "Chrome")
chrome_options.set_capability("browserVersion", "latest")
chrome_options.set_capability("bstack:options", bstack_options)


driver = webdriver.Remote(
    command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub.browserstack.com/wd/hub",
    options=chrome_options
)

try:

    driver.get("https://soft.reelly.io/sign-in")


    login_page = LoginPage(driver)
    login_page.enter_username("kavadiasnadine@gmail.com")
    login_page.enter_password("Jesusholdme1!")
    login_page.click_continue()

    home_page = HomePage(driver)
    home_page.click_settings()
    home_page.click_subscription_payments()

    subscription_page = SubscriptionPage(driver)
    assert subscription_page.is_title_visible()
    assert subscription_page.is_back_button_visible()
    assert subscription_page.is_upgrade_button_visible()

    driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed","reason":"Subscription verified"}}'
    )

except Exception as e:
    driver.execute_script(
        f'browserstack_executor: {{"action":"setSessionStatus","arguments":{{"status":"failed","reason":"{str(e)}"}}}}'
    )
    raise

finally:
    driver.quit()






