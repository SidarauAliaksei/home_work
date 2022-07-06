from Pages.base_page import BasePage
from Locators.main_page_loc import MainPageLoc
from Locators.login_page_loc import LoginPageLoc


class LoginPage(BasePage):

    def validate_login_page(self):
        login_page_url = self.chrome.current_url
        assert login_page_url == LoginPageLoc.login_url_loc, 'The url of the login page does not match'

    def verify_login_link(self):
        assert self.is_element_present(MainPageLoc.login_loc), "Element is absent!"
