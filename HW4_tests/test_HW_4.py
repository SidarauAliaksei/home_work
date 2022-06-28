from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


def test_press_button():
    chrome = webdriver.Chrome('./chromedriver.exe')
    chrome.implicitly_wait(10)
    chrome.get('https://ultimateqa.com/complicated-page/')

    try:
        chrome.find_element(By.XPATH, "//a[@class='et_pb_button et_pb_button_4 et_pb_bg_layout_light']").click()
        time.sleep(1)
        chrome.find_element(By.CSS_SELECTOR, '.et_pb_button.et_pb_button_4.et_pb_bg_layout_light').click()
        time.sleep(1)
        chrome.find_element(By.CLASS_NAME, 'et_pb_button_4').click()
    except TimeoutException:
        print("Timed out waiting for page to load")

    finally:
        chrome.quit()
