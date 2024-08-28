from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class Book_Presentation(Page):

    OFFER_TXT = (By.CSS_SELECTOR, 'div.h2-text.book')

    def verify_book_presentation_page_is_open(self):
        self.verify_partial_url("book-presentation")
        self.verify_partial_text(self.OFFER_TXT, expected_text="Reelly corporate offer")


