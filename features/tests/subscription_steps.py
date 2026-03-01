from behave import given, when, then
from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from pages.SubscriptionPage import SubscriptionPage

@given('the user is on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://soft.reelly.io")

@when('the user logs in with valid credentials')
def step_impl(context):
    login = LoginPage(context.driver)
    login.login("kavadiasnadine@gmail.com", "Jesusholdme1!")

@then('the Subscription & payments page should be visible')
def step_impl(context):
    subscription = SubscriptionPage(context.driver)
    assert subscription.is_displayed()
    context.driver.quit()