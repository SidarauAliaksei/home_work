from Pages.base_page import BasePage
from Locators.main_page_loc import MainPageLoc
from Locators.basket_page_loc import BasketPageLoc
import time


class BasketPage(BasePage):

    def check_basket_is_empty(self):
        assert self.is_element_present(MainPageLoc.basket_empty_loc)

    def check_blouse_in_basket(self):
        assert self.is_element_present(BasketPageLoc.check_blouse_in_basket_loc), "Element is absent!"

    def check_faded_short_sleeve_t_shirts_in_basket(self):
        assert self.is_element_present(
            BasketPageLoc.check_faded_short_sleeve_t_shirts_in_basket_loc), "Element is absent"

    def validate_basket_page(self):
        basket_page_url = self.chrome.current_url
        assert basket_page_url == BasketPageLoc.basket_url_loc, 'The url of the basket page does not match'

    def verify_basket_page(self):
        basket_page_text = self.chrome.find_element(*BasketPageLoc.basket_info_loc).text
        assert basket_page_text == 'Your shopping cart'
