from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from pages.SubscriptionPage import SubscriptionPage


def test_subscription_page():

    mobile_emulation = {"deviceName": "iPhone 11"}

    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://soft.reelly.io")
    sleep(5)

    login_page = LoginPage(driver)
    login_page.enter_username("kavadiasnadine@gmail.com")
    login_page.enter_password("Jesusholdme1!")
    login_page.click_continue()
    sleep(5)
    home_page = HomePage(driver)
    home_page.click_settings()
    home_page.click_subscription_payments()
    sleep(5)
    subscription_page = SubscriptionPage(driver)
    assert subscription_page.is_title_visible()
    assert subscription_page.is_back_button_visible()
    assert subscription_page.is_upgrade_button_visible()







