from pages.base_page import Page
from pages.book_presentation_page import Book_Presentation
from pages.main_page import MainPage
from pages.sign_in_page import Sign_In_Page




class Application:
    def __init__(self, driver):
        self.page = Page(driver)
        self.main_page = MainPage(driver)
        self.sign_in_page = Sign_In_Page(driver)
        self.book_presentation_page = Book_Presentation(driver)
