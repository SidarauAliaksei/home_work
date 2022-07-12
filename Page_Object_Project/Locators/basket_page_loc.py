from selenium.webdriver.common.by import By


class BasketPageLoc:
    basket_empty_loc = (By.XPATH, '//div[@class="shopping_cart"]//span[contains(text(), "(empty)")]')

    check_faded_short_sleeve_t_shirts_in_basket_loc = By.XPATH, "//a[text()='Faded Short Sleeve T-shirts']"
    check_blouse_in_basket_loc = (By.XPATH, "//p/a[text()='Blouse']")

    basket_info_loc = (By.CLASS_NAME, 'navigation_page')
