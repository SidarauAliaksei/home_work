from selenium import webdriver
from selenium.webdriver.common.by import By


def test_iframe():
    chrome = webdriver.Chrome('./chromedriver.exe')
    chrome.implicitly_wait(5)
    chrome.get('http://the-internet.herokuapp.com/frames')
    chrome.maximize_window()

    try:
        chrome.find_element(By.XPATH, '//a[@href="/iframe"]').click()
        chrome.switch_to.frame(chrome.find_element(By.ID, 'mce_0_ifr'))

        text = chrome.find_element(By.XPATH, "//p[text()='Your content goes here.']").text
        assert text == 'Your content goes here.'
    finally:
        chrome.quit()
