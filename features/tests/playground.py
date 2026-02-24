from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from pages.SubscriptionPage import SubscriptionPage


    options = Options()
    driver = webdriver.Firefox(options=options)
else:
    driver = webdriver.Chrome()

driver.maximize_window()

try:
    # Step 1: Open login page
    driver.get("https://soft.reelly.io/sign-in")

    # Step 2: Login
    login = LoginPage(driver)
    login.enter_username("kavadiasnadine@gmail.com")
    login.enter_password("Jesusholdme1!")
    login.click_continue()

    # Step 3: Initialize HomePage
    home = HomePage(driver)

    # Wait for Settings button
    settings_elem = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(home.settings_button)
    )

    # Click Settings using JS (safer)
    driver.execute_script("arguments[0].click();", settings_elem)

    # Wait for URL to change to /settings
    WebDriverWait(driver, 20).until(
        EC.url_contains("/settings")
    )

    # Wait for Subscription option
    subscription_elem = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(home.subscription_button)
    )

    # Click Subscription using JS
    driver.execute_script("arguments[0].click();", subscription_elem)

    # Step 4: Verify Subscription Page
    subscription = SubscriptionPage(driver)

    assert subscription.is_title_visible(), "Title not visible!"
    assert subscription.is_back_button_visible(), "Back button not visible!"
    assert subscription.is_upgrade_button_visible(), "Upgrade button not visible!"

    print("✅ Test Passed Successfully!")

finally:
    driver.quit()

