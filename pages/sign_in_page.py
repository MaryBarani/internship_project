from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class Sign_In_Page(Page):

    MAIN_PAGE_URL = "https://soft.reelly.io"
    USERNAME_INPUT = (By.ID, "email-2")
    PASSWORD_INPUT = (By.ID, "field")
    LOGIN_BTN = (By.CSS_SELECTOR, "a.login-button.w-button")

    def open_main_page(self):
        self.open_url(self.MAIN_PAGE_URL)

    def log_in_to_main_page(self, username, password):
        self.input_text(*self.USERNAME_INPUT, text=username)
        self.input_text(*self.PASSWORD_INPUT, text=password)
        self.wait_and_click(self.LOGIN_BTN)



