from pages.Login_page_internship import  LoginPage
from pages.home_page_Internship import HomePage
from pages.subscription_page_Internship import SubscriptionPage

def test_subscription_page_elements(driver):
    login = LoginPage(driver)
    home = HomePage(driver)
    subscription = SubscriptionPage(driver)

    login.login_as("kavadiasnadine@gmail.com", "Jesusholdme1!")
    home.click_settings()
    subscription.verify_page_opened()
    assert subscription.get_title_text() == "Subscription & payments"
    assert subscription.is_back_button_visible()
    assert subscription.is_upgrade_plan_button_visible()
