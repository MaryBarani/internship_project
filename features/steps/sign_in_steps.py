from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open the main page')
def open_main_page(context):
    context.app.sign_in_page.open_main_page()


@when('Log in to the page with {username} and {password}')
def log_in_to_main_page(context, username, password):
    context.app.sign_in_page.log_in_to_main_page(username, password)