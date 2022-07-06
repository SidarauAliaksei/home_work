from selenium.webdriver.common.by import By


class BasketPageLoc:
    basket_url_loc = 'http://automationpractice.com/index.php?controller=order'

    check_faded_short_sleeve_t_shirts_in_basket_loc = By.XPATH, "//a[text()='Faded Short Sleeve T-shirts']"
    check_blouse_in_basket_loc = (By.XPATH, "//p/a[text()='Blouse']")
