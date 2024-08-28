from selenium.webdriver.common.by import By
from behave import given, when, then


@then("Verify the book-presentation tab is open")
def verify_expected_page(context):
    context.app.book_presentation_page.verify_book_presentation_page_is_open()