import pytest
from selenium import webdriver
from Pages.main_page import MainPage
from Pages.basket_page import BasketPage
from pytest_bdd import scenarios, given, when, then, parsers

scenarios('./test_bdd_hw.feature')


@pytest.fixture
def open_browser():
    global browser
    browser = webdriver.Chrome('C:/Users/wwwba/PycharmProjects/selenium_test/chromedriver.exe')
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


@given('We open main page')
def open_site(open_browser):
    link = "http://automationpractice.com/index.php"
    global main_page
    main_page = MainPage(open_browser, link)
    main_page.open()


@when('We open basket page')
def open_basket_page():
    main_page.open_basket_page()


@then('We check basket page')
def verify_basket_page():
    basket_page = BasketPage(browser, url=browser.current_url)
    basket_page.verify_basket_page()
