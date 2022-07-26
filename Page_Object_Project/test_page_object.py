import time
import pytest
from selenium import webdriver
from Pages.main_page import MainPage
from Pages.login_page import LoginPage
from Pages.basket_page import BasketPage
# from Pages.contact_us_page import ContactUsPage


@pytest.fixture
def open_browser():
    global browser
    browser = webdriver.Chrome('C:/Users/Aliaksei Sidarau/PycharmProjects/selenium_test/chromedriver.exe')
    browser.implicitly_wait(5)


def test_guest_can_open_login_page(open_browser):
    link = "http://automationpractice.com/index.php"
    main_page = MainPage(browser, link)

    try:
        main_page.open()
        main_page.verify_login_link()
        main_page.open_login_page()
        login_page = LoginPage(browser, url=browser.current_url)
        login_page.open()
        login_page.verify_login_link()
    finally:
        browser.quit()


def test_basket_is_empty(open_browser):
    link = 'http://automationpractice.com/index.php'
    main_page = MainPage(browser, link)
    try:
        main_page.open()
        main_page.open_basket_page()
        basket_page = BasketPage(browser, url=browser.current_url)
        basket_page.check_basket_is_empty()

    finally:
        browser.quit()


def test_add_blouse_and_sleeve_t_shirts_in_basket(open_browser):
    link = 'http://automationpractice.com/index.php'
    main_page = MainPage(browser, link)
    try:
        main_page.open()
        main_page.faded_short_sleeve_t_shirts_add_to_basket()
        main_page.close_field_with_add_thing()
        main_page.blouse_add_to_basket()
        main_page.close_field_with_add_thing()
        main_page.open_basket_page()
        basket_page = BasketPage(browser, url=browser.current_url)
        basket_page.open()
        basket_page.check_blouse_in_basket()
        basket_page.check_faded_short_sleeve_t_shirts_in_basket()

    finally:
        time.sleep(3)
        browser.quit()


def test_check_validate_login_page(open_browser):
    link = 'http://automationpractice.com/index.php'
    main_page = MainPage(browser, link)
    try:
        main_page.open()
        main_page.open_login_page()
        login_page = LoginPage(browser, url=browser.current_url)
        login_page.validate_login_page()

    finally:
        time.sleep(3)
        browser.quit()


def test_check_validate_basket_page(open_browser):
    link = 'http://automationpractice.com/index.php'
    main_page = MainPage(browser, link)
    try:
        main_page.open()
        main_page.open_basket_page()
        basket_page = BasketPage(browser, url=browser.current_url)
        basket_page.validate_basket_page()

    finally:
        time.sleep(3)
        browser.quit()


def test_check_validate_main_page(open_browser):
    link = 'http://automationpractice.com/index.php'
    main_page = MainPage(browser, link)
    try:
        main_page.open()
        main_page.validate_main_page()
    finally:
        time.sleep(3)
        browser.quit()


#
# def test_open_contact_us_page(open_browser):
#     link = 'http://automationpractice.com/index.php'
#     main_page = MainPage(browser, link)
#     try:
#         main_page.open()
#         main_page.contact_us_page()
#         contact_us_page = \
#             ContactUsPage(browser, url=browser.current_url)
#         contact_us_page.check_customer_service_contact_us()
#
#     finally:
#         time.sleep(3)
#         browser.quit()


def test_guest_can_open_basket_page(open_browser):
    link = "http://automationpractice.com/index.php"
    main_page = MainPage(browser, link)

    try:
        main_page.open()
        main_page.open_basket_page()
        basket_page = BasketPage(browser, url=browser.current_url)
        basket_page.open()
        basket_page.verify_basket_page()
    finally:
        browser.quit()
