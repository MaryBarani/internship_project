from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on “Connect the company”')
def click_on_connect(context):
    if context.platform == "Mobile_web":
        context.app.main_page.click_connect_company_mobile()
    else:
        context.app.main_page.click_connect_company_web()

@when("Switch the new tab")
def switch_to_new_tab(context):
    context.app.main_page.switch_to_new_window()

