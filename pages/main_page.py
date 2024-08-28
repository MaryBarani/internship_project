from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class MainPage(Page):

    CONNECT_ICON = (By.CSS_SELECTOR, ".get-free-period")

    def click_connect_company(self):
        self.wait_and_click(self.CONNECT_ICON)




