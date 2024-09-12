from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class MainPage(Page):

    CONNECT_ICON = (By.CSS_SELECTOR, ".get-free-period.menu")
    CONNECT_ICON_2 = (By.CSS_SELECTOR, '.settings-block-menu .button-link-menu.w-inline-block[target="_blank"]')
    MAIN_MENU = (By.CSS_SELECTOR, ".circle-gradient")
    MENU_ICON = (By.CSS_SELECTOR, ".menu-photo_avatar.w-inline-block")

    def click_connect_company_web(self):
        self.wait_and_click(self.CONNECT_ICON)

    def click_connect_company_mobile(self):
        self.wait_and_click(self.MAIN_MENU)
        self.wait_and_click(self.MENU_ICON)
        self.wait_and_click(self.CONNECT_ICON_2)



