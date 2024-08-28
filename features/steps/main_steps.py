from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on “Connect the company”')
def click_on_connect(context):
    context.app.main_page.click_connect_company()

@when("Switch the new tab")
def switch_to_new_tab(context):
    context.app.main_page.switch_to_new_window()

