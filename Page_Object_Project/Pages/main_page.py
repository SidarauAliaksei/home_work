import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from Locators.main_page_loc import MainPageLoc
from .basket_page import BasketPage


class MainPage(BasePage):

    def validate_main_page(self):
        MAIN_PAGE = 'http://automationpractice.com/index.php'
        main_page_url = self.chrome.current_url
        assert main_page_url == MAIN_PAGE, 'The url of the main page does not match'

    def open_login_page(self):
        time.sleep(3)
        login_page = WebDriverWait(self.chrome, 20).until(EC.element_to_be_clickable(MainPageLoc.login_loc))
        login_page.click()

    def open_basket_page(self):
        time.sleep(3)
        go_to_basket_link = WebDriverWait(self.chrome, 20).until(
            EC.element_to_be_clickable(MainPageLoc.basket_loc))
        go_to_basket_link.click()

    def verify_login_link(self):
        assert self.is_element_present(MainPageLoc.login_loc), "Element is absent!"

    def verify_basket_is_empty(self):
        assert self.is_element_present(MainPageLoc.basket_empty_loc), "Basket is not empty"

    def blouse_add_to_basket(self):
        time.sleep(3)
        basket_link = WebDriverWait(self.chrome, 20).until(
            EC.element_to_be_clickable(MainPageLoc.blouse_add_to_basket_loc))
        basket_link.click()

    def faded_short_sleeve_t_shirts_add_to_basket(self):
        time.sleep(3)
        basket_link = WebDriverWait(self.chrome, 20).until(
            EC.element_to_be_clickable(MainPageLoc.faded_short_sleeve_t_shirts_loc))
        basket_link.click()

    def close_field_with_add_thing(self):
        time.sleep(3)
        close_field = WebDriverWait(self.chrome, 20).until(
            EC.element_to_be_clickable(MainPageLoc.cross_loc))
        close_field.click()

    def open_dresses_page(self):
        time.sleep(3)
        go_to_dresses_link = WebDriverWait(self.chrome, 20).until(
            EC.element_to_be_clickable(MainPageLoc.dresses_loc))
        go_to_dresses_link.click()

    def contact_us_page(self):
        time.sleep(3)
        go_to_contact_us_page = WebDriverWait(self.chrome, 20).until(
            EC.element_to_be_clickable(MainPageLoc.contact_us_loc))
        go_to_contact_us_page.click()
