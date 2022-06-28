from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def test_field():
    chrome = webdriver.Chrome('./chromedriver.exe')
    chrome.implicitly_wait(10)
    chrome.get('https://ultimateqa.com/filling-out-forms/')

    try:
        chrome.find_element(By.ID, 'et_pb_contact_message_0').send_keys('111111')
        chrome.find_element(By.ID, 'et_pb_contact_name_0').send_keys('Aliaksei')
        chrome.find_element(By.NAME, 'et_builder_submit_button').click()
        message = chrome.find_element(By.XPATH, "//div/p").text

        assert message == 'Thanks for contacting us'

    finally:
        chrome.quit()


def test_without_field_name():
    chrome = webdriver.Chrome('./chromedriver.exe')
    chrome.implicitly_wait(10)
    chrome.get('https://ultimateqa.com/filling-out-forms/')

    try:
        chrome.find_element(By.ID, 'et_pb_contact_message_0').send_keys('111111')
        chrome.find_element(By.NAME, 'et_builder_submit_button').click()
        error = chrome.find_element(By.CLASS_NAME, 'et-pb-contact-message').text
        assert error == 'Make sure you fill in all required fields.'

    finally:
        chrome.quit()


def test_without_field_message():
    chrome = webdriver.Chrome('./chromedriver.exe')
    chrome.implicitly_wait(10)
    chrome.get('https://ultimateqa.com/filling-out-forms/')

    try:
        chrome.find_element(By.ID, 'et_pb_contact_message_0').send_keys('111111')
        chrome.find_element(By.NAME, 'et_builder_submit_button').click()
        chrome.find_element(By.ID, 'et_pb_contact_message_0').clear()
        chrome.find_element(By.ID, 'et_pb_contact_name_0').send_keys('1111')
        chrome.find_element(By.NAME, 'et_builder_submit_button').click()
        error = chrome.find_element(By.CLASS_NAME, 'et-pb-contact-message').text
        assert error == 'Please, fill in the following fields:\nMessage'

    finally:
        chrome.quit()


if __name__ == '__main__':
    test_field()
    test_without_field_name()
    test_without_field_message()
