from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_select_menu():
    chrome = webdriver.Chrome('./chromedriver.exe')
    try:
        url = 'https://demoqa.com/select-menu'
        chrome.fullscreen_window()
        chrome.get(url)
        chrome.maximize_window()
        time.sleep(3)
        option = chrome.find_element(By.CLASS_NAME, 'css-1wy0on6').click()
        select_option = chrome.find_element(By.ID, 'react-select-2-option-0-0').click()
        title = chrome.find_element(By.CLASS_NAME, 'css-yk16xz-control').click()
        select_title = chrome.find_element(By.ID, 'react-select-3-option-0-0').click()
        old_style = Select(chrome.find_element(By.ID, 'oldSelectMenu'))
        old_style.select_by_value('2')
        time.sleep(3)
        chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        multiselect = chrome.find_element(By.XPATH, '//*[@id="selectMenuContainer"]/div[7]/div/div/div/div[2]').click()
        time.sleep(1)
        select_multiselect = chrome.find_element(By.ID, 'react-select-4-option-3').click()
        select_multiselect = chrome.find_element(By.ID, 'react-select-4-option-2').click()
        select_multiselect = chrome.find_element(By.ID, 'react-select-4-option-1').click()
        time.sleep(2)
    finally:
        chrome.quit()


def test_guru99():
    chrome = webdriver.Chrome('./chromedriver.exe')
    try:
        url = 'http://demo.guru99.com/test/newtours/register.php'
        chrome.get(url)
        chrome.maximize_window()
        time.sleep(2)
        first_name = chrome.find_element(By.NAME, 'firstName').send_keys('Aliaksei')
        last_name = chrome.find_element(By.NAME, 'lastName').send_keys('Sidarau')
        phone = chrome.find_element(By.NAME, 'phone').send_keys('+375295555555')
        email = chrome.find_element(By.NAME, 'userName').send_keys('bart@gmail.com')

        address = chrome.find_element(By.NAME, 'address1').send_keys('Street 9/2')
        City = chrome.find_element(By.NAME, 'city').send_keys('Minsk')
        State = chrome.find_element(By.NAME, 'state').send_keys('Minsk')
        postal_code = chrome.find_element(By.NAME, 'postalCode').send_keys('200100')
        time.sleep(1)
        country = Select(chrome.find_element(By.NAME, 'country'))
        country.select_by_visible_text('BELARUS')
        time.sleep(3)

        user_name = chrome.find_element(By.NAME, 'email').send_keys('qwerty123')
        password = chrome.find_element(By.NAME, 'password').send_keys('1111')
        confirm_password = chrome.find_element(By.NAME, 'confirmPassword').send_keys('1111')

        time.sleep(2)
        button = chrome.find_element(By.NAME, 'submit').click()
        time.sleep(2)
        check_name = chrome.find_element(By.XPATH,
                                         '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td/p[1]/font/b').text
        check_nickname = chrome.find_element(By.XPATH,
                                             '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td/p[3]/font/b').text
        assert check_name == 'Dear Aliaksei Sidarau,'
        assert check_nickname == 'Note: Your user name is qwerty123.'
    finally:
        chrome.quit()


if __name__ == '__main__':
    test_select_menu()
    test_guru99()
