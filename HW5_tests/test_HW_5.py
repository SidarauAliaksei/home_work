from selenium import webdriver
from selenium.webdriver.common.by import By


def test_1():
    chrome = webdriver.Chrome('./chromedriver.exe')
    chrome.implicitly_wait(5)
    chrome.get('https://the-internet.herokuapp.com/dynamic_controls')
    chrome.maximize_window()

    try:
        chrome.find_element(By.XPATH, "//*[@type='checkbox']").click()
        chrome.find_element(By.XPATH, "//*[@onclick='swapCheckbox()']").click()
        message = chrome.find_element(By.CSS_SELECTOR, "p#message").text
        assert message == "It's gone!"

        if len(chrome.find_elements(By.XPATH, "//*[@id='checkbox']")) != 0:
            print('Checkbox here.')
        else:
            print('Checkbox is not found.')

        input_disabled = chrome.find_element(By.XPATH, '//input').get_attribute('disabled')
        if not input_disabled:
            print('No found input_disabled.')

        chrome.find_element(By.XPATH, "//button[@onclick='swapInput()']").click()
        input_enabled = chrome.find_element(By.ID, 'message').text
        assert input_enabled == "It's enabled!"

    finally:
        chrome.quit()
